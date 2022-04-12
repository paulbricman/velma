---
layout: post
age: 21.36
title: lexiscore evaluation
published: True
---

## lexiscore evaluation

A few months ago, I published the [lexiscore](/thoughtware/lexiscore), a tool and metric for quantifying how interesting a given text is for a given person. To recap, the core idea behind the project was to measure the amount of Shannon-like information which a piece of content has to offer a particular user, based on their notes. Interesting content should avoid being boring (i.e. predictable using the notes), but also avoid being too unexpected (i.e. an advanced textbook on an unfamiliar topic). I argued that it's the sweet spot of balanced skill and challenge that we're looking for when we want to get immersed.

That was cool and all, but I only had limited qualitative results to share back then. For instance, I found the blog posts predicted to be interesting to indeed be quite interesting. My own blog posts were predicted to be quite boring for me, which makes a lot of sense as a sanity check. Blog posts which I could barely follow myself were generally estimated not to be interesting, etc.

However, given that it was my brainchild, I wondered whether I overestimated the lexiscore's effectiveness in identifying interesting content. To address that, I ran a more quantitative analysis to investigate how well the lexiscore outputs correlated with my own ratings of interestingness, before seeing the tool's predictions. The rest of this post describes the somewhat rudimentary methods, the results, and a short discussion.

The experiment began on a Sunday, when I piped that week's articles through the lexiscore labeler in an attempt to meal prep my information diet for the week. Based on the ~100 RSS feeds I follow, I got 33 blog posts in total. However, instead of filtering for items whose lexiscore was above a certain value (e.g. only "A" or "B"), I included all of them. Additionally, I opted for the individual lexiscores _not_ to be included in the final PDF output, so that they wouldn't influence my ratings. Before closing the app, I exported the predicted results as CSV for later, so that I could compare them with my ground-truth valuations at the end.

After completing the above setup, I went on and read a few articles a day, as usual. However, in addition to the regular routine, I wrote down my personal rating for each item immediately after finishing it. At the end, I had a list of 33 of my own ratings of interestingness, one for each blog post.

Following this labeling process, I normalized both my ratings and the lexiscore outputs between zero and one. Converting ordinal data ("A", "E") to interval data (1.0, 0.0) was a questionable step, yet I thought it was acceptable given the intended equal distances between items. My stats prof would probably disagree, though. Anyway, now that we've paired lexiscore outputs and my ground-truth ratings by article in a table, it's time to measure correlations, make plots, and draw conclusions.

![](/assets/img/lexiscore_evaluation_main_corr.png)
_Scatter plot of blog posts positioned in terms of lexiscore outputs (X axis) and my own ratings (Y axis), following a bit of jittering._

First, it seems that my ratings correlate better with the lexiscore outputs (see above) than with the skill feature alone (see below), based on the R-squared values. Only using the "skill" feature while ignoring the "challenge" one can be seen as a content-based recommender system baseline. It would simply attribute high interestingness to content which is close in topic to my notes, trying to give me more of what I'm already into (e.g. an introductory post on AI, even if boring). It seems that throwing in the "challenge" feature (i.e. text unpredictability) helps yield more accurate estimates. I didn't run a statistical test to compare the two, because I wasn't really sure what (nonparametric) test would be suitable for these funky distributions.

![](/assets/img/lexiscore_evaluation_skill_corr.png)
_Scatter plot of blog posts positioned in terms of the "skill" feature (i.e. semantic similarity to my notes) and my own ratings, following a bit of jittering._

What's more, the top-right quadrant of the skill-challenge plane (i.e. unpredictable content on a familiar topic), a region which gets mapped to high lexiscore outputs, only contains items which I've found quite interesting (see below). The signal there is quite high. We can say that the system has _high precision_ -- what it deems interesting appears to be quite interesting indeed. This can also be inferred from the very first plot, by looking at the articles placed towards the right.

![](/assets/img/lexiscore_evaluation_bubbles.png)
_Scatter plot of blog posts positioned in terms of "skill" (i.e. semantic similarity to my notes) and "challenge" (i.e. unpredictability), plus scaled in terms of my ratings (i.e. the larger articles are the ones which I found more interesting)._

However, the lexiscore also labelled some articles which I personally found interesting as not that valuable (see above). In this, we can say that the system has _low recall_ -- quite a few interesting articles weren't picked up, and ended up intermingled with items which I found less interesting. This can also be inferred from the very first plot, by looking at the articles placed all the way towards the left. We missed interesting content!

This might be after-the-fact rationalization, but I'd argue that it's high precision and mediocre recall you'd want most in such a system, rather than the other way around. We don't have enough time to read all available content anyway, so a few false negatives are harmless given that our positives are consistently true. If I can reliably fill up all my reading time with interesting articles, I don't really care about the ones wrongly classified as not interesting, because I wouldn't have enough time to accommodate them anyway.

Now, what issues might have led to the still poor correlation between lexiscore outputs and my own ratings?

- There are things I know which I haven't cared to write down in my notes. Therefore, my knowledge base is an imperfect model of my own knowledge, which inevitably can't yield perfect rating estimates.
- The lightweight language model I used for computing the "challenge" feature (i.e. distilgpt2) might be too small, failing to lead to reliable estimates of unpredictability.
- There are way more factors at play in my own subjective valuation of interestingness. For instance, the lexiscore can't know that I've been avoiding most Ukraine-Russia coverage after being anxiously glued to CNN live text during the first days of the war.

Anyways, I find those quantitative results as promising as the qualitative ones, and I'll continue to curate my information diet through the lexiscore for the time being. That said, there are quite a few issues involved in the labeling process, some of them unfeasible to tackle without a richer user model. It improves the signal-to-noise ratio somewhat, but there's still work to do.
