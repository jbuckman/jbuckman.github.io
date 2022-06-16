---
layout: post
title: The One Where I Rebut Gary Marcus
tags: ["deep learning", "scaling", "AGI"]
published: true
mathjax: false
---

This post is a follow-up to [yesterday's essay](https://jacobbuckman.com/2022-06-14-an-actually-good-argument-against-naive-ai-scaling/), and relates to an ongoing discussion between [Scott Alexander](https://astralcodexten.substack.com/) and [Gary Marcus](https://garymarcus.substack.com/) on the topic of AI scaling
([post1](https://astralcodexten.substack.com/p/my-bet-ai-size-solves-flubs?s=r),
[post2](https://garymarcus.substack.com/p/what-does-it-mean-when-an-ai-fails?s=r),
[post3](https://astralcodexten.substack.com/p/somewhat-contra-marcus-on-ai-scaling?s=r),
[post4](https://garymarcus.substack.com/p/does-ai-really-need-a-paradigm-shift?s=r)).
Specifically, the debate is whether scaled-up language models in the style of GPT-3 will eventually become general intelligences, or whether we will hit some fundamental limits.

Yesterday, I argued that the current paradigm is fundamentally limited by its use of passive data collection.
Without some form of knowledge-aware exploration, scaling will run out of steam once it has ingested everything feasibly seeable on the internet.
Today, I will contrast my argument with that of other critics of deep learning, most notably Dr. Marcus.

Let me begin by setting the stage.
My argument is that the current paradigm is bottlenecked by its naive approach to data collection.
In contrast, Dr. Marcus argues that the current paradigm is bottlenecked by its naive approach to modeling, which he views as missing some crucial components such as explict causal models, symbol manipulation, or discrete reasoning.
Note that these are not contradictory claims: it's possible for them both to be true!
However, I don't find Dr. Marcus's argument convincing.[^0]

---

The mainstream approach to critiquing large language models is to find "failure cases".
Plenty of examples of this style of critique can be found in [Dr. Marcus's published work](https://thegradient.pub/gpt2-and-the-nature-of-intelligence/), and [other critics](https://www.economist.com/by-invitation/2022/06/09/artificial-neural-networks-today-are-not-conscious-according-to-douglas-hofstadter) do this too.
These failure cases are seen as proof that the language model has not really "solved" or "understood" the task at hand.
The bet he offers Scott Alexander is centered around precisely this sort of approach:

> I am willing to bet SlateStarCodex now (terms to be negotiated) that if OpenAI gives us unrestricted access to GPT-4, whenever that is released, and assuming that is basically the same architecture but with more data, that within a day of playing around with it, Ernie and I will still be able find lots of examples of failures in physical reasoning, temporal reasoning, causal reasoning, and so forth.

Dr. Marcus's position relies crucially on a particular syllogism, typically left implicit: **if failure cases can be found, then this implies that the task has not been solved**.
It is precisely at this point that the argument fails.
Amusingly, the best explanation of the failure mode comes from an old post by Scott Alexander: [it's an argument that proves too much](https://www.lesswrong.com/posts/G5eMM3Wp3hbCuKKPE/proving-too-much).

---

[Adversarial examples](https://openai.com/blog/adversarial-example-research/) are a well-known failure case of deep learning.
An adversarial example is an input that is, to human perception, indistinguishable from any other, but causes the neural network to make an erroneous prediction.
Despite being [first noticed in 2013](https://arxiv.org/abs/1312.6199), and [tens of thousands of papers](https://scholar.google.com/scholar?cites=2835128024326609853&as_sdt=5,33&sciodt=0,33&hl=en) written in an attempt to study and fix them, there is *still no effective means* of eliminating these errors on any but the most toy tasks.
Furthermore, this is one area where scaling does not seem to help very much.
Big or small, they exist all the same.

Fundamentally, the issue at play is that the input space for these models is simply too large.
Consider an image classification task, with 64x64 greyscale 8-bit inputs: there are 256\^(64\*64) ≈ *1e10000* possible images.
Even if we train it on a massive dataset of a billion data points, we're still 9991 orders of magnitude away from complete coverage.
There are *so many* possible inputs that it is unreasonable to expect a model to be able to get them all right; this means it will get some of them wrong.
Some of these errors happen to be "adjacent" to train-set images, and the name we give to these errors are adversarial examples.
Empirically, their existence seems to be inevitable.

Fortunately, models that make errors are still useful.
We know that mistakes happen, we expect them, and we account for them.
Consider a simple task like [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition), which is just converting images of text into its corresponding symbols.
It's not really a stretch to say neural networks have solved this problem in a meaningful sense.
Amazon and Google both have commercial solutions backed by deep learning, and achieve [almost perfect accuracy](https://research.aimultiple.com/ocr-accuracy/) (although I actually had a bit of trouble finding reliable benchmark numbers here).
These models will likely work perfectly for any OCR application you might need them for.
But -- like all neural models -- if you search the massive input space specifically looking for errors, you will find some.

---

For image classification, the input space is images.
For language models, the input space is contexts, [as I discussed yesterday](https://jacobbuckman.com/2022-06-14-an-actually-good-argument-against-naive-ai-scaling/).
So just as we expect an OCR model to make mistakes on some images, we should of course expect a language model to make mistakes on some contexts.
Adversarial examples are a bit harder to find in discrete spaces like text strings, but they [are well known to exist](https://arxiv.org/abs/2004.01970).

Dr. Marcus's claim that he can find errors in any future GPT is both true and vacuous.
If we can find adversarial examples for relatively-simple domains like character recognition on greyscale images, of course we can find them for arbitrary behavior on arbitrary text strings.
Adversarial examples exist for all current models at all scales, and it will be a major breakthrough when somebody discovers how to defeat them; this is deeply connected to the question of why neural networks generalize at all, and I predict it will be approximately as challenging.
A dedicated error-finder can always find an error.
As far as I can tell, nobody really doubts this, not even team scaling-is-all-you-need.

But it *does not follow* from this fact that scaled-up neural models cannot solve tasks like physical or biological reasoning, when "solve" is defined in a reasonable, pragmatic way.
Scale will never eliminate all errors, but it will make it less likely that we will encounter them without a dedicated search.
As the system improves, its practical value increases, even when the ease with which we can find its mistakes is barely reduced.
This holds all the way up to the limit of total understanding.

It is now hopefully clear why I say Dr. Marcus's argument proves too much.
There are two options.
We can either believe in the syllogism, and be forced to conclude that OCR is not solved due to its adversarial examples, despite wide commercial adtoption and near-perfect performance on all inputs it sees.
Or we can reject the syllogism, and conclude that Dr. Marcus's hand-crafted adversarial examples are not good evidence for a lack of understanding.

---

To drive the point home: humans make mistakes, too.
If a biology student gets an 84% on a test, is it fair to hold up the questions they answered incorrectly as evidence that it "does not understand biological reasoning"?
I don't think so; a more fair characterization is that they have an incomplete understanding, and one that will hopefully grow with time.
Another obvious example of humans making mistakes is optical illusions.
Does one's perception of an [infinite staircase](https://en.wikipedia.org/wiki/Penrose_stairs) reflect a lack of understanding of physical reasoning?
In certain contexts, [humans even have adversarial examples](https://arxiv.org/abs/1802.08195).
If Dr. Marcus applied his same argument to humans, he'd quickly find that they are incapable of "truly understanding" as well.

---

So what argument *would* be persuasive?
Specifially, persuasive that there are limitations to the *modeling* paradigm of deep learning, i.e., that large differentiable neural networks are fundamentally inadequate.

I would need to see an experiment with the following attributes.
- Start with a task that a human can perform reliably.
- Generate infinite data for this task (in order to rule out the data-imposed limitations on learning I discussed in [my last post](https://jacobbuckman.com/2022-06-14-an-actually-good-argument-against-naive-ai-scaling/)).
- Train a neural network to convergence on this data.
- Find that the AI does not match human performance on new data (sampled from the same data-stream as it was trained on).

If someone is able to find an experimental setting where this holds, even when the scaling-is-all-you-need crew has tried their best and deepest network, *that* would be a strong argument for the inadequacy of modeling.[^1]
I've never seen this occur, and right now, I lean towards believing such a setting does not exist.
But I have pretty high uncertainty around that claim; the main thing informing my views is that many times, I *predicted* this would happen, and was wrong.
If someone is able to find such a setting please tell me, I would love to see it!

In the meantime, I don't see any evidence indicating that we need any modeling tools beyond large differentiable neural networks.

---

Thanks for reading, and hit me up on Twitter [@jacobmbuckman](https://twitter.com/jacobmbuckman) with any feedback or questions!

---

[^0]: For concreteness, I will be focusing on his arguments here, but [as he points out](https://garymarcus.substack.com/p/does-ai-really-need-a-paradigm-shift?s=r), there are many people making these sorts of arguments. This rebuttal is directed at all of them.

[^1]: Also disqualified are examples where the limitations of the AI models are purely technical, e.g. because the contexts are too big. As I mentioned last time, these are fundamental and important technical issues, but clearly fall within the current paradigm, so do not serve as argument against it.