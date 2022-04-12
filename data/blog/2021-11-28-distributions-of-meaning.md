---
layout: post
age: 21.06
title: distributions of meaning
published: True
---

## distributions of meaning

Etymologically, a concept is something that _holds together_. Unfortunately, this is precisely where consensus ends, as different schools of thought frame concepts in widely different ways, leading to a veritable zoo of competing representations.

For instance, a popular way of representing concepts in machine learning is through semantic embeddings: unique sets of coordinates in a space of meaning which automatically derived from large corpora. [Word2Vec](https://paperswithcode.com/method/skip-gram-word2vec), [GloVe](https://paperswithcode.com/method/glove), [ELMo](https://paperswithcode.com/method/elmo), and [fastText](https://paperswithcode.com/method/fasttext) are all examples of this approach. Given that each concept gets a unique embedding, this approach represents concepts through prototypes -- single idealized instances which allegedly capture the _essence_. This is what I've been using in [semantica](/thoughtware/semantica) a while ago as a basis for computational ops for conceptual thinking.

However, in this framing, the symbol "plant" would get a single representation, even if it might refer to vegetation, the action of placing seeds in soil, a factory building, or something else entirely. To account for those different senses, part-of-speech tagging and other sense disambiguation techniques have been used to narrow in on some [more specific senses](http://wordnetweb.princeton.edu/perl/webwn?s=plant&sub=Search+WordNet&o2=&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=). This would mean that the noun "plant" gets a different embedding than the verb "plant." It's still based on prototypes, just slightly more refined ones. Additionally, note that the same word symbol, as a convenient reference, now points to different actual concepts.

But a concept often bridges a range of contexts into a unified pattern, so present day machine learning often informs the representation of a concept by using its context. The sentence in which "plant" arises will significantly sharpen the probability distribution of what sense it is we're considering at a given point. If I'm talking about agriculture, it's very likely that I'm using a nuance of "plant" that's close to "vegetation." This gives you [BERT](https://paperswithcode.com/method/bert) and all its witty derivative models like [RoBERTa](https://paperswithcode.com/method/roberta) and [ALBERT](https://paperswithcode.com/method/albert), among others. They're able to compute an embedding for a certain symbol in a unique given context. This turns the embedding into a representation of an _exemplar_, rather than a prototype. To represent a concept through exemplars, you simply need a bunch of them. Sure, you could get a prototype by simply averaging the exemplar embeddings one way or another, but you'd lose out on so much information about the shape of the state cloud.

Incidentally, what led me to this choice of theme for this weekly reflection was the fact that I had to extract a state cloud of BERT embeddings for a bunch of concepts from BERT's original training data for my bachelor's project. A set of 768-dimensional vectors where each captures the unique nuance of a concept as used in a specific sentence. As I haven't seen that much work on this exemplar-based representation in ML, I set out to poke at the idea a bit more, which led to adding another specimen to the concept representation zoo.

![](/assets/img/plant_statecloud.png)

But before going into that, have a look at the state cloud of "plant" projected above in 2D using a cheap PCA transform. A set of exemplar clusters can clearly be delineated, probably representing the various senses of the word "plant" as showing up across the ~10K books which make up BERT's training data. But remarkably, there's a lot of nuance in there. You see way more variation than a few well-established senses -- you see slight shifts in meaning from one context to another. Working with concepts as unique prototype embeddings misses out on all this richness.

However, the dots which make up the state cloud in the figure are pretty arbitrary, due to the happenstance of the actual sentences present in the corpus. The exemplars which punctuate the state space merely reflect the limited sample size of the relatively tiny text corpus. That said, those few tens of thousands of contexts here appear to hint at a certain underlying distribution of meaning. Maybe the concept of "plant" is actually more comprehensively represented as a heat map across semantic space, a continuous probability distribution of what that word symbol might precisely mean, informed by the exemplar state cloud, a bit like the bottleneck layer of a VAE. As you provide more context, the uncertainty gets further reduced, until it collapses onto a sharp distribution with a single peak. The flatness and spread of the distribution of meaning becomes a measure of ambiguity. A certain meaning corresponds to all concepts at once, but with different probabilities, most being close to null.

![](/assets/img/plant_heatmap.png)

We went from prototype embeddings, to slightly more refined prototype embeddings, to exemplar embeddings, and finally to distributions of meaning. The last part of this rambly piece is a chaotic exploration of ways in which you might be able to manipulate those last semantic distributions algorithmically.

If [semantica](/thoughtware/semantica) operators addressed prototype embeddings in the language of linear algebra (e.g. interpolation, centroids), then the basis of manipulating this more fluid conceptual representation is the dialect of probability and statistics. Interpolating between two prototype embeddings, say for "pond" and "ocean," might be analogous to adding up the respective probability distributions with different weights before normalizing the result so that it adds up to one. Adding up the heat maps of different concepts this way feels like a logical OR, as it incorporates information from both of them. In contrast, multiplying the distribution of probability across the space of meaning feels a bit like a logical AND, as it narrows in on joint regions which are "warm" for both of them. Completing our Boolean lineup, NOT might be implemented by substracting the current distribution from a uniform one.

To poke further, given two probability distributions of meaning, the semantic similarity between them might be taken to be their KL-divergence, or some other metric of how much two such distributions differ. Sharpening a distribution of meaning through a high-temperature softmax would mean focusing more on the most frequent meaning, the most representative sense. If a distribution "engulfs" another one, then it might be termed to be more abstract than the other, but the difference between two heat maps might provide a more general representation of the relation between the two concepts, similar to the iconic "king - queen" popularized by Word2Vec.

Alright, but why would this be practically useful? At this point, I have absolutely no idea. Though the elegance and intuitiveness of this concept representation, the distribution of meaning, made it compelling on some obscure level. Time will tell if my intuitions about [how to grow ideas](/reflections/ideoponics) have been effective here, and I'll let this simmer in the back of my mind for a while. I also added a 30x screencast of my reflection session below which informed many ideas described before, depicting both the ["expand node into memories"](/reflections/conversational-multiverses) mechanic and the "save to conceptarium" one.

<div style="margin-bottom: 0"><i>click to play screencast:</i></div>
<div class="iframe-holder" style="margin-top: 0">
<iframe
    src="/assets/vid/distributions_of_meaning.mp4" 
    frameborder="0"
    allowfullscreen>
</iframe>
</div>
