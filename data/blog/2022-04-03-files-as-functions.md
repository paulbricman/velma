---
layout: post
age: 21.40
title: files as functions
published: True
---

## files as functions

One day last week, I came across [the NeRF paper](https://arxiv.org/abs/2003.08934), short for neural radiance fields. It's been quite influential (i.e. ~850 citations in 1.5 years), though I'm not really in touch with current trends in computer vision. The core idea of the paper is that you can train a tiny neural network to predict what color you'd see if you were to look at a scene from a certain angle. The authors use a collection of a few dozen images to set the ground-truth, but the model being trained can then predict how things would look like from completely new angles. You can just plug in whole camera trajectories to get [those stunning videos](https://www.youtube.com/watch?v=JuH79E8rdKc).

![](/assets/img/nerf_nutshell.png)
_NeRF in a nutshell ([Source](https://arxiv.org/pdf/2003.08934.pdf))_

However, there's something quite unusual about their approach. Namely, the authors train one model per scene instead of one model for the entire dataset of scenes. They overfit each tiny model to the brim until its assigned scene is deeply engrained in its weights. At the end of the day, they obtain a functional representation of those surroundings (instead of a rasterized voxel cube), which can then be probed at will from various angles. Fun fact: pixel stands for picture element, while voxel stands for volume element.

This approach reminded me of something I've been working on a few years ago in 2018, which is for the most part disconnected from my current work. Accordingly, I thought this week's article might be a good opportunity to unpack that past project and resurface a cluster of related ideas. That's our next stop.

The main question behind this past paper was whether multimedia files could be represented as functions which map coordinates to values. By multimedia files, I mean files which can be meaningfully subjected to lossy encoding (e.g. an image, audio, video, etc.), in contrast to executable binaries or text documents. Concretely, the prof I approached then for advice and I chose to focus on images specifically as the Drosophila of the multimedia kingdom.

Images can be seen as mappings between XY coordinates and RGB(A) values at each location. Videos are similar, but they also include a third input coordinate: time. Audio, in contrast, only has time as an input coordinate, but essentially maps to raw one-dimensional air pressure. That would be mono sound, you'd add one more output value for stereo. 3D objects could be seen as maps between XYZ coordinates and density at the specified location -- is there even something there? 3D animations are to 3D objects as videos are to images, so you'd again add time as an input coordinate. And so on, every multimedia asset I can think of can for the most part be expressed as a (super complex) function which maps coordinates to values.

Let's get back to images. If we were to represent a picture as a function, we'd need one which receives an X and a Y as input and returns an RGB tuple as output. Hm, how could we approximate this function? We only have a few samples of this mapping, equal in number to the number of pixels in the image. Wait a second, approximating a function... based on a set of input-output pairs... oh yeah, sounds like something an ML model could do!

![](/assets/img/coconet_overview.png)
_CocoNet overview ([Source](https://arxiv.org/abs/1805.11357))_

Based on this idea, we trained tiny MLPs on images-turned-datasets-of-pixels. Hence, [CocoNet: A deep neural network for mapping pixel coordinates to color values](https://arxiv.org/abs/1805.11357) (I hope we can both agree I came a long way with project names). Similar to how NeRF authors trained one model per scene, we trained one model per image. At the end of the day, our image models could predict the color values located at given pixel coordinates. "But we have JPEG, why on Earth would you overengineer things this much?" I hear you say. Well, it turns out that you can conduct all sorts of funky manipulations on functional representation of multimedia files which you can't natively conduct on "raster" versions.

- upsampling

For instance, say you trained your one-image-model on the 100x100 pixels of an image. Assuming prior normalization, you probably had something like pixel (0, 0) mapping to the red-ish (0.9, 0.1, 0.3) or pixel (0.2, 0.6) mapping to the blue-ish (0.2, 0.1, 0.8). Thing is, if your image is represented as a function, you're not limited to the pixel coordinates you initially had -- you can plug in coordinates of pixels which didn't even exist in the original picture! For instance, you can probe the one-image-function for the color located _between_ a few of the original pixels. If you systematically sample this denser grid over the entire "surface" of the initial image, you essentially perform upscaling, or superresolution if you want to get published. This methods outperformed "traditional" upscaling methods (e.g. what you might find in Photoshop when scaling up an image) in the experiments we conducted.

- inpainting

Similar to how you might "cheat" and probe the image at locations which didn't exist before, you can also choose to ignore a specific patch of the image, train on the rest, and then probe the terra incognita afterwards. The image dataset consists in a bunch of input-output pairs (i.e. XY-RGB data points), so you can just casually leave some out. After training, you still get a function which maps coordinates to values, but which hasn't been exposed to the masked patch. If you however insist on probing that region, you essentially conduct inpainting -- the model implicitly interpolates the surrounding neighborhood, extending likely patterns into the mysterious region (see right column below).

![](/assets/img/coconet_sampling.png)
_Upscaling and inpainting results ([Source](https://arxiv.org/pdf/1805.11357.pdf))_

- denoising

If you regularly checkpoint the one-image-model in its memorization process, it unsurprisingly becomes better and better at reconstructing it. The image becomes engrained deeper and deeper into the network's weights.

![](/assets/img/coconet_memorization.png)
_The one-image-model incrementally memorizes the assigned image ([Source](https://arxiv.org/pdf/1805.11357.pdf))_

It turns out that if you sprinkle noise on top of the input to be memorized, the network learns a denoised-ish version of the image _before_ it manages to perfectly memorize the noisy one. At a certain stage during this rote learning process, the model "only" manages to figure out broad underlying patterns of the image, but fails to nail the noise details. However, the task is arguably failed successfully, because the intermediate result is useful due to the removal of noise. In a sense, the model is natively immune to certain types of noise, implicitly saving valuable [representational resources](/reflections/representational-resources) by not accounting for them.

![](/assets/img/coconet_denoising.png)
_CocoNet denoising versus traditional techniques ([Source](https://arxiv.org/pdf/1805.11357.pdf))_

- compression

If you manage to capture general underlying patterns (e.g. horse blob), storing the rasterized version (e.g. 2000 horse pixels) might be less efficient. In this, the functional representation is a candidate "codec" for compression. We didn't investigate this particular property in much depth, but the NeRF people realized that the one-scene-model was smaller in size than the combined dozens of pictures which depicted the scene from different angle.

What's more, all signal processing techniques described above can in theory be ported to any other modality. What if you probed a one-video-model at a timestep between two real frames? What if you inpainted a slip in an audio performance? What if you could get a smooth mesh out of a noisy 3D scan? Not to mention a compressed version of any of these. Those are all highly general tasks, and the functional representation is somewhat modality-agnostic in implementing them.

Unfortunately, there are a few major drawbacks of this approach. First, you need to spend some serious compute training the one-file-model, distilling the discrete grids of values into continuous fields of infinite resolution. If you don't train enough, the accuracy in reconstructing the original will be quite low, which is a pity compared to highly-reliable standards like JPEG. Also, we ran into issues with high-frequency information (e.g. the kid's knitted hood thingy in the upscaling results), though the NeRF authors managed to circumvent some of those issues by using much richer positional embeddings than we did.

That said, I think there's something particularly interesting about the functional codecs hinted at above. They're a bit more biologically-plausible, a bit more biomimetic, which might make them way more tractable in future BCI applications. With my limited took-like-four-courses background in cognitive science, I'm finding it much easier to imagine that human memories are in some part encoded through neural ensembles which approximate continuous functions, than to imagine a discrete grid of color values stored somewhere in the brain. We're quite good at "inpainting" our memories with events which haven't taken place, and we also remember broad patterns somewhat better than concrete details.

If you linked readings of single-cell or LFP probes to the input of such digital ["engrams"](<https://en.wikipedia.org/wiki/Engram_(neuropsychology)>) and piped the output values back through some analogous stimulation, you might eventually learn to [attend to](/thoughtware/cybersalience) and perceive external representations through novel senses. In contrast, I'm not sure how you could download a video bitstream in the brain besides emulating visual stimuli from the eyes, though you could probably also just collapse probes at new locations to the nearest real values, your brain handling the "pointer" to external memory. Anyway, looking forward to running into those ideas in some short story written by Egan in the 1990s or something.
