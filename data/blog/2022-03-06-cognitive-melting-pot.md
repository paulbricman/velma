---
layout: post
age: 21.33
title: cognitive melting pot
published: True
---

## cognitive melting pot

<div class="top-pad"><blockquote class="quoteback" darkmode="" data-title="Why Don't Students Like School?" data-author="Daniel Willingham" cite="https://books.google.nl/books?id=8SDs8LZl41EC&lpg=PA68&vq=understanding%20is%20remembering%20in%20disguise&hl=nl&pg=PA68#v=onepage&q&f=false">
Understanding is remembering in disguise.<br>
<footer>Daniel Willingham<cite> <a href="https://books.google.nl/books?id=8SDs8LZl41EC&lpg=PA68&vq=understanding%20is%20remembering%20in%20disguise&hl=nl&pg=PA68#v=onepage&q&f=false">https://books.google.nl/books?id=8SDs8LZl41EC&lpg=PA68&vq=understanding%20is%20remembering%20in%20disguise&hl=nl&pg=PA68#v=onepage&q&f=false</a></cite></footer>
</blockquote><script note="" src="https://cdn.jsdelivr.net/gh/Blogger-Peer-Review/quotebacks@1/quoteback.js"></script></div>

It's around 1990. The Hopfield network is popularized as a model of associative memory, though [Yannic](https://www.youtube.com/watch?v=fkIJwYArKpw) isn't there to distill it. It allows you to encode a set of different data points (e.g. images depicting animals), and later retrieve them using a cue. Crucially, the cue can differ dramatically from the data points to be recalled. It can be heavily corrupted with noise, or can just be a tiny snippet of the initial data. The Hopfield network resembles human memory in curious ways -- we can also recall vivid experiences from mere cues, and we also recall things gradually over the course of a few moments.

![](/assets/img/hopfield_animals.png)
_A Hopfield network retrieves images of animals from corrupted or partial cues ([Source](https://www.ai.rug.nl/minds/uploads/LN_NN_RUG.pdf#page=122))_

Fast forward to the present machine learning landscape. Being able to recover a corrupted image or hallucinate a full document from a short prompt are deemed as signs of profound understanding of the target domain, rather than only a curious feat of memory. How could you possibly know how to fill-in-the-blanks like BERT or create photorealistic outputs like ImageGPT without thorough reasoning about linguistics and physics? Surely, understanding and constructing accurate world models must be an instrumental goal in being able to produce outputs of this quality, right?

![](/assets/img/imagegpt_dog.png)
_ImageGPT attempting to reconstruct an image of a dog ([Source](https://openai.com/blog/image-gpt/))_

This contrast strikes me as odd. How can very similar tasks -- creating complex arrangements of data given simpler cues -- be seen as guiding the implementation of "mere" artificial memory then and advanced world modeling now? Alright, early work in line with Hopfield networks did focus on retrieving encoded memories only, while current work focuses almost entirely on generalizing to new situations. However, I still feel they're related. I've often heard the following as a hand-wavy explanation of recent ML models:

- If this text prompt was in the dataset of web pages, what words would be likely to come next?
- If this sequence of actions was in the dataset of past games, what action would be likely to come next?
- If this image crop was part of a full image from the dataset, how would it be likely to look like as a whole?

What those attempts to offer an intuitive explanation of ML outputs on test data have in common is that they frame their original tasks as the act of trying to remember something which wasn't there in the first place, and failing beautifully in the process. From this angle, machine learning becomes mainly the task of learning how to successfully analogize from past experience to the present situation, the headspace of [Hofstadter](http://worrydream.com/refs/Hofstadter%20-%20Analogy%20as%20the%20Core%20of%20Cognition.pdf) and [Chollet](https://arxiv.org/pdf/1911.01547.pdf). We teach machines how to successfully remember things they've never seen before, perhaps a bit like we do.

This melting pot of cognitive functions in ML echoes recent challenges of dogma in cognitive science. For a few decades, a strong information processing lens has cast human perception mostly as input processing through a number of increasingly advanced stages (e.g. dots to lines to shapes, V1 to V2 to V3, surface features to object representations, etc.). However, mounting evidence highlights the recurrent interaction of perception with other cognitive functions, such as memory. You perceive things which are more likely in a more accurate and faster way, there's the whole object permanence thing, etc.

A light reaction to the arbitrariness of taxonomies in psychology might be to make ammends. Fine, so perception isn't only informed by the outside world in a rational attempt of recovering physical properties of reality -- there are also top-down influences involved. Those interact with the bottom-up ones and result in richer representations.

However, a more hardcore reaction to the melting pot of cognitive functions is to grow wary of the salad bowl distinctions in the first place. Memory is far from being a neat hard disk and perception is far from being a self-contained webcam -- the taxonomies we constantly entertain often feel biased by our culture. In our case, this appears to lead to overestimating the mind's modularity and sparsity.

It doesn't help that psychology has a muddy track record in this regard. The Soviet Vygotsky argued that developmental psychology is best understood in relation to the social environment, while the Swiss Piaget argued that it's best understood in relation to inherent stages of cognitive development. Some early theories of Western origin speak of a central executive of the mind. Apparently, pressure was an important part of psychology contemporary to steam engines, while we now speak of neural circuits. John Hopfield himself ~~was~~ is a physicist by training, and his associative memory model is based on an analogy to energy being minimized, inspiring the likes of Karl Friston.

Just like memory interacts with perception, if science is our attempt to make sense of the messy world, there's no wonder our worldviews occasionally hop in to fill in the gaps. Our tendency to project our own conceptions onto the object of study is amplified by the particularly complex and nebulous topic that is the mind.
