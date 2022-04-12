---
layout: post
age: 20.88
title: early conceptarium workflows
published: True
---

## early conceptarium workflows

In this piece, I aim to catalogue some of the ways in which I'm using the [conceptarium](/thoughtware/conceptarium) and reflect on usage opportunities going forward. Besides walking through the workflows step by step, I'll try to describe specific episodes from my usage which resulted in new insights. This article also acts as a source of inspiration for integrating tools like the conceptarium into one's workflow.

- semantic priming

From my experience, this usage pattern isn't common at all among today's knowledge workers. In fact, it's virutally non-existent, which is intriguing given its potential utility. Semantic priming here refers to briefly exposing yourself to past ideas of yours which are related to a given piece of content (e.g. research paper, educational video, blog post) _before_ you actually consume it. This workflow is all about elevating into your awareness the previous thoughts you've had which are most related to the topic at hand. This way, you make it more likely for you to establish new connections, to weave the new piece of information into your knowledge.

<div style="margin-bottom: 0"><i>click to play screencast:</i></div>
<div class="iframe-holder" style="margin-top: 0">
<iframe
    src="/assets/vid/conceptarium_semantic_priming.mp4" 
    frameborder="0"
    allowfullscreen>
</iframe>
</div>

This usage pattern might come across as a bit odd. Isn't knowledge work all about actively manipulating new information (e.g. programs, models, designs, arguments)? What good could briefing yourself on past thoughts of yours bring? I'll answer this understandable concern with an episode from my own work, which requires a bit of context.

Earlier this week, I've had a lecture on "computational learning theory" as part of [a course](https://www.rug.nl/ocasys/fwn/vak/show?code=WBAI001-05) I'm following at uni. This academic niche aims, among others, to lay the theoretical foundations of machine learning at large, not only for deep learning. Researchers involved in this field study questions like: "How much data is theoretically necessary to solve this learning problem with this accuracy?" or "How exactly does the complexity of machine learning models interact with overfitting?". At the beginning of this lecture, I followed the semantic priming usage pattern using the title of the lecture as a query. The top result from my conceptarium was this previous thought:

> "Neurocomputational models of the brain are useful in the way they expose handles, levers, knobs and dials which we can tap into with tools."

This strategically resurfaced idea, together with the contents of the lecture, made me think:

> "Huh, are traditional machine learning models (e.g. decision trees, Bayesian learning) used as partial models of the mind? How useful could those be? What opportunities could those bring about?"

But this new thought isn't the end of the story. Rather, this unanswered open question kept bugging me (in a good way) for the rest of the day. The real insights came when I was later reading a research paper as background literature for my bachelor's project. This upcoming project is focused on something called [conceptors](https://arxiv.org/pdf/1406.2671.pdf) (funnily enough, I currently work both with conceptors and the conceptarium, but they're entirely different things). A conceptor is most easily understood as a round object (hyperellipsoid to be specific) which exists in semantic space and approximates the "cloud" of embeddings of a given concept (e.g. a set of BERT embeddings of a word in different contexts). If you've done statistics or bioinformatics, conceptors look really similar to the prototypical PCA ellipsoids used in dimensionality reduction. Anyway, the previous unanswered questions, together with this reading, led to the following conceptual offspring, which I then added to my conceptarium and retrieved just now to list them here.

> "What if conceptors were run not on recurrent neural networks, but on the brain through neurofeedback. They would encourage a replay of a previous dynamic."

> "Shielding prior neural representations through conceptor logic, it might be possible to build tools which make away with forgetting."

> "Morphing conceptors derived from neural states of different concepts would represent the neural states of another middle concept, a bit like mix or span in Semantica. Couple that with neurofeedback and you nudge a BCI user to think about that artificial concept."

I know it's virtually impossible to understand what I'm talking about here without more context on conceptors and neurofeedback, but that's not the point. The point is simply that the semantic priming workflow enabled by the conceptarium helped me integrate new information about computational learning theory and conceptors into my prior thinking about tools for thought, and resulted in new ideas to be explored in the future: enabling new affordances in brain-computer interfaces using conceptors.

- diagram store

If the semantic priming usage pattern required a new take on content consumption, this workflow is really easy to understand. The diagram store usage pattern is all about being able to easily find diagrams (e.g. graphs, flowcharts, tables) after you first encounter them. With other tools, this often requires filling in manual annotations and moving over images and texts to the app of choice. However, the conceptarium makes it as easy as it gets: just save the diagram from anywhere and later simply describe it to find it. To reduce cognitive load, the screencast listed below is based on a visual depiction of the conceptors described before. Naturally, I changed the URL address of my conceptarium after recording the screencasts on this page.

<div style="margin-bottom: 0"><i>click to play screencast:</i></div>
<div class="iframe-holder" style="margin-top: 0">
<iframe
    src="/assets/vid/conceptarium_diagram_store.mp4" 
    frameborder="0"
    allowfullscreen>
</iframe>
</div>

- multi-modal capture

This usage pattern is just as straight-forward as the previous one. Many tools for thought implement various "capture" mechanics, ways in which the tool can ingest your thoughts to help you work with them. However, the conceptarium takes it a step further through dedicated pages and third-party integrations which enable you to save ideas via writing, speech, pictures, and others. This versatility empowers users to remove their own pain points by finding the best way to integrate the conceptarium in their workflow.

<div style="margin-bottom: 0"><i>click to play screencast:</i></div>
<div class="iframe-holder" style="margin-top: 0">
<iframe
    src="/assets/vid/conceptarium_multimodal_capture.mp4" 
    frameborder="0"
    allowfullscreen>
</iframe>
</div>

I personally find it crucial to be able to save thoughts to my knowledge base with as little friction as possible. This helps me save them from the premature death of forgetting, helping them escape the haphazard tide of mind-wandering. In this, the conceptarium provides a rapid response shelter for concepts, offering the possibility of later access if relevant.

Moreover, as UI/UX designers are getting tired of the desktop metaphor, a big interest for me is to explore tools which enable ways of conducting knowledge work _outdoors_. This comes in part from how much I'm enjoying leisure time spent on forest paths and mountain trails. Multi-modal mobile-friendly capture mechanics are a first important step in experimenting with such embodied tools for thought, as they eliminate the reliance on desktop. However, despite even forests having 4G coverage in the Netherlands, the reliance on mobile data is still an issue in the design of the conceptarium, especially for countries with a developing Internet infrastructure.

- multi-modal representations

While being able to capture ideas in different formats is a big plus for many, I also find it useful to store the _same_ idea in multiple formats. From the mainstream [learning styles discussion](https://www.youtube.com/watch?v=rhgwIhB58PA), to [classic Bret Victor talks](https://vimeo.com/115154289), to more obscure research like [dual coding theory](https://www.instructionaldesign.org/theories/dual-coding/), it has been argued that making use of multiple parallel representations fosters a deeper understanding of the topic at hand. Similar to the diagram store usage pattern, this workflow also cuts down on the manual book-keeping necessary to connect various takes on the same topic expressed through different modalities.

<div style="margin-bottom: 0"><i>click to play screencast:</i></div>
<div class="iframe-holder" style="margin-top: 0">
<iframe
    src="/assets/vid/conceptarium_multimodal_representations.mp4" 
    frameborder="0"
    allowfullscreen>
</iframe>
</div>

However, while in practice the conceptarium itself isn't able to generate new representations (e.g. an illustration from a short text -- an obvious opportunity for open source [DALL-E](https://openai.com/blog/dall-e/) replicas), the fact that it respects and invites visual imagery as [a valid form of intellectual work](https://www.youtube.com/watch?v=7fx0QcHyrFk), in contrast to [most existing tools for thought](https://maggieappleton.com/note-oppression), is a useful feature in itself. I find myself more willing to sketch important concepts, now that I know I can also work with them digitally, expanding my understanding in the process. Sketches and illustrations can often be used to render metaphors more explicit and tangible, and provide new "retrieval paths" for getting to the same concepts.

You'll notice that this way of using the conceptarium goes hand in hand with multi-modal capture, as can be seen in the embodied metaphor of 3D clusters included in the screencast above. That specific bush of flower buds prompted me to think about this data metaphor, and the conceptarium acts as a record of those embodied sources of inspiration, weaving together abstract ideas with actual pictures -- another step towards knowledge work amplified by enactive interfaces and environments.

- bonus: UI inspiration

This one I haven't explored that much, but during [a course on cognitive ergonomics](https://www.rug.nl/ocasys/fwn/vak/show?code=WBAI025-05) and when prototyping the conceptarium and [ideoscope](/thoughtware/ideoscope), I happened to work a lot with wireframes and mockups. Similar to the diagram store, wireframes and mockups can also be retrieved when relevant.

<div style="margin-bottom: 0"><i>click to play screencast:</i></div>
<div class="iframe-holder" style="margin-top: 0">
<iframe
    src="/assets/vid/conceptarium_ui_inspiration.mp4" 
    frameborder="0"
    allowfullscreen>
</iframe>
</div>

## conclusion

It hasn't been long since I started using the conceptarium, maybe several weeks tops, yet I find it quite obvious that it can support a broad range of new useful workflows. Looking back on this initial test drive, the conceptarium has proven most valuable by far when used not to retrieve particular entries (e.g. specific diagrams), but when used in a more open-ended way (e.g. semantic priming). Therefore, I plan to explore more usage patterns which focus on inducing serendipity. What parts of my global workflow can I inject with unexpected connections? What thinking practices would make the best out of the serendipity dormant in one's ever growing conceptarium? I'll report back on my findings in a follow-up piece to this article.

Background music for screencasts: [Silent Strike, QB Sessions vol. 2](https://silentstrike.bandcamp.com/album/qb-sessions-vol-2)
