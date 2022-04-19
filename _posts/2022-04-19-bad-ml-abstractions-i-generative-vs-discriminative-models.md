---
layout: post
title: Bad ML Abstractions I (Generative vs Discriminative Models)
tags: ["bad ml abstractions"]
published: true
mathjax: false
---

#### *by [Jacob Buckman](https://twitter.com/jacobmbuckman) and [Carles Gelada](https://twitter.com/carlesgelada)*

This post is part of a series on bad abstractions in machine learning. For context on why we are writing these, read [Abstraction Enables Thought](https://jacobbuckman.com/2022-02-21-abstraction-enables-thought/).

---

_**Bad Abstraction:** There are two types of machine learning models. Discriminative models are trained to separate inputs into classes, while generative models learn a distribution from which they can draw new samples._

---

**These two categories are not actually distinct.** Consider the following two scenarios.

- Our dataset is a collection of natural-language sentences. We train a character-level language model via maximum likelihood. We generate sentences by autoregressively sampling from this model.
- We are given a labeled dataset of text strings; each string is labeled with one of 64 categories. The model is trained to mininize the cross-entropy between the model's prediction and the true class.

The first example is a quintessential generative modeling problem, while the second is uncontroversially discriminitive. *But I've just described the same model twice.*

Given the set of natural-language sentences in the first scenario, we can construct a dataset in the following way. First, match each of the 64 possible characters (26 lowercase, 26 uppercase, 10 digits, space, and period) to a label. Next, take every character-level prefix of every sentence, and label it with the subsequent character. 

Note that the dataset we have constructed matches the specifications of the second scenario. Training the second model on this dataset is indistinguishable from training the first model.

---

**Seriously, there is no difference.** All classification is conditional generative modeling: *of labels*.

Consider an ImageNet model, which maps from a space of images to the space of probability distributions over labels.

Now, let’s say we want to exploit some of the text structure of the labels (e.g., the fact that “housecat” and “bobcat” classes, which have similar spellings, also contain similar images). Therefore, instead of outputting 1000 arbitrary one-hot classes, we output the label as a string, one character at time.

Our "discriminative model" is now undeniably an "image-conditional generative model". But in fact, it was all along. All we did was autoregressively decompose our output space.

---

**The taxonomy is also incomplete.** Is a regression task generative or discriminative? What about tasks where the model outputs a function? What about the learning of embeddings or distance functions, e.g. for use in a search engine?

---

**Reductio ad absurdum.** *There are two types of machine learning models. "Rectangular models" use ReLU activations on their hidden units, whereas "tangential models" use tanh activations on their hidden units.* 

Is this a good abstraction? If not -- why? Could an analogous criticism be leveled towards the generative/discriminative taxonomy?

---

**One valid use case: GANs.** A GAN is composed of 2 neural networks, the first mapping from noise to images, and the second mapping from images to Bernoulli distributions. There is nothing *fundamentally* different about these two networks, but in the context of GAN training, each serves a different role. If you want to give a name to each of the networks for ease of reference, calling them "generator" and "discriminator" seems perfectly fine.
