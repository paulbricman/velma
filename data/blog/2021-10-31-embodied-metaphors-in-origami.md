---
layout: post
age: 20.98
title: embodied metaphors in origami
published: True
---

## embodied metaphors in origami

Embodied metaphors refer to transfers of mental models from the experiential domain to the world of abstract ideas. As noted by George Lakoff and Mark Johnson's in their fascinating classic titled [Metaphors We Lived By](https://www.goodreads.com/book/show/34459.Metaphors_We_Live_By), embodied metaphors are surprisingly pervasive in our everyday thinking.

- argument is war
  - Your claims are _indefensible_.
  - He _attacked_ every _weak point_ in my argument.
  - Her criticisms were _right on target_.
  - I've never _won_ an argument with him.
  - She _shot down_ all of my arguments.
- time is money
  - You're _wasting_ my time.
  - This app will _save_ you hours.
  - How do you _spend_ your time these days?
  - That flat tire _cost_ me an hour.
  - You're _running out_ of time.
- health is up
  - He's at the _peak_ of health.
  - Lazarus _rose_ from the dead.
  - She's in _top_ shape.
  - He _fell_ ill.
  - He _dropped_ dead.

Those metaphors are so transparent that we aren't even aware of them, we see right through them. They're conceptual lenses in the way they shape our view of the world. In the extreme, Lakoff and Johnson argue that this domain of first-hand experience -- hunger, joy, fear, love, sickness, inclusion... -- is one of the main scaffolds which we use to build our conceptual frameworks. Yet the ordinary experience of being human is probably the last place where we'd go to find solutions for abstract problems, even if so much of our high-level ideas are informed by commonplace memories.

To get a better sense of how unfair this feels for embodied knowledge, just reread the previous paragraph while being on the lookout for metaphors. I opened it with an allusion to physical transparency, then talked about how we perceive the world, then alluded to building physical structures, then framed knowledge as a physical space you navigate. If this is still not compelling enough, then try rereading this very paragraph in the same fashion. Those metaphors are everywhere, part and parcel of how we think.

I'll make a detour here to describe an unlikely experiential domain which I've been exploring lately -- Origami, the Japanese art of folding paper. For some, Origami means folding paper models of plants and animals. For others, it means building large abstract volumes from simpler modules. For yet others, it means creasing repetitive geometrical patterns called tessellations. There's some serious diversity in what you can bring to life using basic sheets of paper you have lying around, and I'm grateful to have had a chance to enjoy this niche.

![](/assets/artisanry/paper/b2.jpeg)
_Origami peacock, ([source](https://paulbricman.com/artisanry))_

That said, when considering our collective consciousness, Origami is way closer to the informal and somewhat childish realm of arts and crafts, while being mostly incompatible with solving tough conceptual problems in science and engineering. I'm saying _mostly_ here because there are some direct physical applications of tesselations in astronomy and medicine (e.g. folding solar panels effectively, folding implants effectively). Beyond the low-hanging fruit analogy of swapping paper for photovoltaics or what not, I'm not aware of deeper Origami-STEM connections.

This is the challenge I'll embrace in the second half of this article. I want to build on this context while trying to catalogue some more abstract metaphors which I stumbled upon while folding a bunch of colorful papers. I'll try slightly harder at this in order to compensate for the rather arbitrary connotations against this bridge which I inherited from our culture.

- parallel processing

I won't lie, folding a modular Origami model can be quite tedious, because all the individual modules take time to fold on their own, and they're usually very repetitive. This led me to come up with ways of parallelizing some folds across multiple modules in the making. For instance, I would stack tiny papers on top of each other and fold them all at once, in unison. Alternatively, I would fold a larger paper first with broader creases before splitting it up into tinier squares, each square inheriting a part of the broader crease.

![](/assets/artisanry/paper/a4.jpeg)
_Modular Origami cube, ([source](https://paulbricman.com/artisanry))_

Parallelization is a key challenge in designing effective algorithms at scale. Working with stacked papers at once felt a bit like batching matrices in a tensor and running efficient CUDA routines on it, rather than going through each item iteratively. Folding across a lattice of modules in the making gave me some serious hardware manufacturing vibes. I'm not sure how this would translate to data processing, but it might help me think about cutting down on PCB prices for the analog synth I'm planning to build from scratch in the future.

![](/assets/img/tensors.png)
_Illustration of using Tensor Cores in CUDA ([source](https://developer-blogs.nvidia.com/wp-content/uploads/2021/03/CUDA_Tensor_Featured_image.png))_

- manifolds

It's almost obvious, but in Origami you often start with a flat piece of paper and end up with a 3D object. Additionally, if you work non-destructively (i.e. don't use scissors), then you can revert the final model to a flat paper by simply unfolding it.

This is the closest I've come to gaining an intuitive understanding of manifolds. In mathematics, manifolds are roughly low-dimensional surfaces embedded in high-dimensional spaces. For instance, think about the space of all possible 100x100 image files. There are way more such images than atoms in the universe (10^28853 >> 10^80). Then how can machine learning models learn to recognize cats and cars in there? How can we do that as people, for that matter? Well, it's likely that the space of natural photographs is spread across a relatively tiny sliver of this giant combinatorial space, which makes computation much more manageable both for us and AI. You'd say that natural photographs are mostly located around a low-dimensional manifold embedded in the high-dimensional pixels-times-color-channels space.

![](/assets/img/manifold.png)
_Illustration of the manifold of fonts ([source](https://distill.pub/2017/aia/))_

To complete the metaphor, it's as if the machine learning model somehow gets hold of an origami model. Even if the paper is folded and creased in intricate ways across high-dimensional space, if you live right on it as an ant and move around in your neighborhood, you're in a space of much lower dimensionality. In machine learning parlor, your coordinates on the manifold form a semantic embedding. [Semantica](/thoughtware/semantica), my first thoughtware project, was an exploration of ways of meaningfully moving around this semantic material folded in intricate ways.

<div class="top-pad"><blockquote class="quoteback" darkmode="" data-title="A geometrical view of perceptrons" data-author="Geoffrey Hinton" cite="A geometrical view of perceptrons">
<span class="commtext c00">To deal with hyper-planes in a 14-dimensional
 space, visualize a 3-D space and say 'fourteen' to yourself very 
loudly. Everyone does it.</span>
<footer>Geoffrey Hinton<cite> <a href="A geometrical view of perceptrons">A geometrical view of perceptrons</a></cite></footer>
</blockquote><script note="" src="https://cdn.jsdelivr.net/gh/Blogger-Peer-Review/quotebacks@1/quoteback.js"></script></div>

![](/assets/artisanry/paper/f6.jpg)
_Basic corrugation, ([source](https://paulbricman.com/artisanry))_

- error propagation

Folds are never perfect. If you're careful, you might get pretty close to actually folding a paper in half. However, if you're tired, you'll be way off. In both cases, you accumulate some error -- the thing in your hands diverges from its idealized geometry. This becomes more and more apparent as you continue folding as you go through the steps. Each time, the error you accumulate is amplified by your baggage up to that point. If all your folds are slightly off, you can't help but diverge even more from the ideal, because you're using imperfect creases as references, as landmarks in making new ones. This implies that if you're tackling a long and complex model, you'd better pay careful attention so you don't make it harder for you later down the line.

![](/assets/artisanry/paper/e6.jpg)
_Quite some error propagated *here*, that's for sure... ([source](https://paulbricman.com/artisanry))_

This made me think about how error accumulates in time series forecasting and when working with machine precision. Trying to predict the weather in two weeks is way trickier than trying to predict the weather in one week, because by the time you're thinking about that second half of the time window, things already get fuzzy due to the inherent uncertainty in the first half. Similarly, if you're working with really small numbers on a regular computer, you'll inevitably run into machine precision issues. This is especially true when working with long chains of operations, deep computational graphs, across which error inevitably builds up.

![](/assets/img/forecasting.png)
_Time series forecasting error ([source](https://www.lokad.com/public/Upload//Technology/ProbabilisticForecasting/probabilistic-forecasting-graph.png))_

- understanding

A large part of folding an Origami model actually consists of creasing the paper. That is, you're folding and immediately unfolding, just to leave a mark in the paper. Those creases always turn out to be useful, because they sort of teach the paper to behave in certain ways. When you're creasing the paper, you're nudging its geometry to work in a specific way. In sum, those preparatory steps really help the whole thing click together later on, as its fragments fall neatly into place as expected through the priming steps.

![](/assets/img/wave.png)
_Folding instructions ([source](https://www.origamitessellations.com/wp-content/uploads/2018/01/Eric_Gjerde_Bauhaus_Foundation_Course_instructions_booklet_version.pdf))_

This is a bit like trying to understand a complex concept. Your mind starts somewhat as a blank slate, as a flat piece of paper. As you learn, you iteratively improve your understanding. You refine mental models, you sharpen distinctions through examples, and you connect different parts of your conceptual framework. After learning the basics, and through the guidance of a culturally-recycled thought process resembling age-old traditional Origami models, everything clicks into place. Your mind reaches a satisfying state of intuitive understanding.

Taking this a step further, following a formal curriculum is like following a detailed diagram with instructions, something Illich would frown upon. However, the more interesting questions are the following. Given a desired Origami model, what are the folds necessary to get there? Given a desired state of understanding, what are the learnings required to get there? [Vivid](https://www.vivid.so/) is an online service which tries to approach this last question head on, reverse engineering a state of understanding into a machine-generated curriculum.

![](/assets/img/vivid-career.png)
_Screenshot of Vivid ([source](https://www.vivid.so/))_

However, even if crazily expensive from a computational point of view, a more elegant approach of reverse engineering a state of understanding might be the following. Find the paragraphs which, if concatenated and fed to a language model through prompt engineering, most reduce the perplexity on a description of the target concept. If my target is to perfectly understand how a voltage-controlled oscillator (VCO) works in a modular synth, then this imaginary system with infinite computational resources would find me the few paragraphs on the web which most effectively make VCO descriptions predictable, and by extension, easy to understand. It's a more general, albeit probably unfeasible due to its brute-force nature, path to finding the right folds. However, it could be used in a restricted way to merely work with a pre-filtered list of candidates. This could enable a goal-driven version of the nutritional label for food for thought I'm currently working on.

## conclusion

This was a slightly rambling, but unexpectedly fun piece to write. I hope this article helps communicate how pervasive embodied metaphors are in our day-to-day business, and also how much unexplored potential there is in squeezing informational juice out of unlikely experiential fruit.

_Thanks a lot to [Benjamin Wittorf](https://ben.wf/) for a timely reminder on how pervasive metaphors are in our thinking, [John Yang](https://twitter.com/jianangyang) for showing me around Vivid a while back, and the awesome people who publish Origami diagrams online, including [Eric Gjerde](https://www.ericgjerde.com/), [Michał Kosmulski](https://origami.kosmulski.org), and [Paper Kawaii](https://www.paperkawaii.com/)._
