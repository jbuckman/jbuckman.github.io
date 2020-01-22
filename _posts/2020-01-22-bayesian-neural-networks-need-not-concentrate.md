---
layout: post
title: Bayesian Neural Networks Need Not Concentrate
tags: ["deep learning", "bayesian deep learning", "uncertainty estimation"]
published: true
mathjax: true
invisible: true
---

#### *by [Carles Gelada](https://twitter.com/carlesgelada) and [Jacob Buckman](https://twitter.com/jacobmbuckman)*

Proponents of Bayesian neural networks often claim that trained BNNs output distributions which capture epistemic uncertainty. Epistemic uncertainty is incredibly valuable for a wide variety of applications, and we agree with the Bayesian approach in general. However, we argue that BNNs require highly informative priors to handle uncertainty. We show that if the prior does not distinguish between functions that generalize and functions that don’t, Bayesian inference *cannot* provide useful uncertainties. This puts into question the standard argument that “uninformative priors” are appropriate when the true prior distribution is unknown.

## What is Bayesian Inference?

In discussions on Twitter, many researchers seem to believe that “Bayesian” is synonymous with “uncertainty-aware”, or that any algorithm that uses sets or distributions of outcomes must be Bayesian. We would like to make it clear that in our view, this is not a fair characterization. The Bayesian approach to uncertainty, which involves updating prior distributions into posterior distributions using Bayes’s Rule, is certainly one of the most popular approaches. But there are other, non-Bayesian approaches as well; for example, concentration inequalities are clearly non-Bayesian, but they allow us to compute confidence intervals and uncertainty sets.

At its core, Bayes’s Rule is a relationship between conditional probability distributions:

$$Pr(A=a \mid B=b)=\frac{Pr(B=b \mid A=a) Pr(A=a)}{Pr(B=b)}$$

This is a powerful, fundamental relationship, to be sure; but any conceptions of “belief updating” or “distributions over possible worlds” are post-hoc interpretations.  Bayes’s Rule simply says that for any two non-independent random variables $$A$$ and $$B$$, seeing that $$B$$ took a specific value $$b$$ changes the distribution of the random variable $$A$$. In standard lingo, the term $$Pr(A=a)$$ is called the prior, $$Pr(B=b \mid A=a)$$ is the likelihood, and $$Pr(A=a \mid B=b)$$ is the posterior. This wording stems from the fact that we have an original (prior) distribution for the random variable $$A$$, and then use the observed $$b$$ to provide an updated distribution (the posterior).

Let’s consider how we might apply the Bayesian framework to a classification problem. We have some input space $\chi$ and some output space $Y$, which we assume are discrete (for the sake of simplicity). There is a family of functions $$f: \chi \to T$$ mapping between them; it's useful to think of each $f$ as a vector $$f\in Y^\chi$$, where indexing the vector at the index $$x\in\chi$$ equates to evaluating the function,$$f_x = f(x)$$. There exists some ground-truth function $$f^*: \chi \to Y$$ that we are interested in. A Bayesian approach to the problem says that in the real world there is a random variable $$F^*$$ of classification tasks, and that $$f^*$$ is a sample from it. We will use $$Pr(F^*=f)$$ to denote the distribution of $$F^*$$. (From now on, we will just abbreviate it to $$Pr(f)$$.) Since a dataset of input output pairs $$D=\{ (x_i, F^*(x_i)\}$$ is most definitely not independent from $$F^*$$, we can use Bayes's Rule to know what the distribution of $$F^*$$ is, given that we have observed $$D$$:

$$Pr(f \mid D) = \frac{Pr(D \mid f)Pr(f)}{Pr(D)}$$

The term $$Pr(D \mid f) = \prod_{x,y\in D } 1_{f(x) = y}$$ just denotes that if $$F^*=f$$, then the dataset would contain labels equivalent to the outputs of $$f$$. Why is this conditional distribution interesting? Because if the dataset was informative enough, the distribution of $$F^*$$ might collapse to a single point and we might not have any uncertainty over what $$f^*$$ is. Even if the distribution does not collapse to a single point we could still do many interesting things with $$Pr(f \mid D)$$. For example, we can provide estimates by marginalizing over it,

$$\hat{f} = \int Pr(f \mid D) f df$$

Or by finding the maximum a posteriori estimator,

$$\dot{f}=\sup_f Pr(f \mid D)$$

But even more interestingly, we can use the distribution to provide uncertainty: the distribution of what the particular outputs $$f^*(x)$$ *might* be. Given a test point $$x$$, we can output the probability that $$Pr(F^*(x)=y \mid D)$$. This can be very important; for example, in many sensitive applications, it is essential to abstain from making predictions when uncertain. Up to this point, Bayesian methods look very appealing.

## A Potential Problem with Bayesian Neural Networks

All of the above properties rely on having a good posterior distribution, which assigns more of its probability mass to functions which are more likely to be correct. Let’s take a closer look at what goes into that. Here’s the posterior term again, but since the denominator $$Pr(D)$$ is simply a normalizing constant which is the same for all functions, we can hide it:

$$Pr(f \mid D) \propto Pr(D \mid f)Pr(f)$$

There are two terms: the prior $Pr(f)$, which corresponds to our a priori preferences towards certain functions; and the likelihood $Pr(D \mid f)$, which encodes the idea that certain functions are more compatible with the data than others.

The standard Bayesian story goes as follows: the prior will cover a wide set of functions, but only a few of those functions will be compatible with the data, allowing the posterior to *concentrate* onto a small set of functions, all of which are likely to be good. From this perspective, it makes sense to choose a prior which is “uninformative”, in the sense that it is very uniformly spread over the set of all functions. This allows us to cover our bases by ensuring that the prior assigns non-zero probability to every function that could conceivably be the correct one. Then, we simply let the likelihood term do most of the work filtering out the bad parts of the space. Seems simple enough! However, this standard Bayesian story has some fine print.

**Firstly,** it’s important to note that the quality of the uncertainty estimate is completely dependent on the quality of the prior. In order for our posterior distribution to correspond to the exact distribution of possible functions, the prior needs to be exactly correct. In other words, the ground-truth function $$f^*$$ needs to *actually have been sampled* from the same distribution as you use for the prior. If this is not the case, the posterior can be arbitrarily bad! If you assume a prior that is sharper than reality, the failure case is obvious: some regions of the posterior will have probability that is inappropriately low, resulting in underestimating the overall uncertainty. When the prior is smoother than reality, the failure case is less obvious, but definitely still present: for any fixed amount of data, the learned posterior will be too wide, resulting in overestimation of the uncertainty. Equivalently, we could say that we need more data to reach any particular confidence level.

**Secondly,** the standard Bayesian story almost always takes place in *underparameterized* regimes, i.e. where the size of the dataset $$\mid D \mid$$ is at least as large as the number of parameters of the model. But when we use neural networks, this is clearly not the case in almost any practical setting. Increasing the size of a neural model seems to always help performance (e.g. see [this post](https://openai.com/blog/deep-double-descent/)), so we always want to be in the overparameterized regime. We need to carefully consider the implications of this difference when thinking about Bayesian deep learning.

Unfortunately, as we will see in the next section, the combination of these caveats leads to a big issue: **data never causes the posterior over neural networks to concentrate**.

## Bayesian Neural Networks Need Not Concentrate

A common scenario involves fitting a dataset $$D$$ with a neural network whose parameters are given $$\theta$$. Just as before, $$D$$ contains input-output pairs generated by some ground-truth function $$f^*$$. Of course, since we are doing deep learning, it’s safe to assume that we are in the overparameterized regime: $$ \mid D \mid  <<  \mid \theta \mid $$. Furthermore, let’s assume that our network is flexible enough that the ground-truth function $$f^*$$ is within the class of functions that it can represent. Let $$f_{\theta^*}$$ be a neural network function that approximates $$f_{\theta^*}(x) \approx f^*(x) \forall x \in \chi$$. Since $$f_{\theta^*}$$ gets every point correct, it of course gets all the points in $$D$$ correct: $$Pr(D \mid f_{\theta^*}) \approx 1$$.

Unfortunately, $$D$$ is not the only dataset that our neural network can fit. Consider taking a second dataset $$Z=\{(x_i,y_i\}$$ from the same ground-truth function as $$D$$, $$f^*$$, and corrupting some of the outputs: $$\dot{Z}=\{(x_i,\dot{y}_i\}$$, where $y_i \neq \dot{y}_i \forall i$. Finally, concatenate the real data $$D$$ with corrupted data $$\dot{Z}$$ to get a combined dataset, $$C$$. (Assume that $$ \mid \dot{Z} \mid $$ is small, so that we do not leave the overparameterized regime, i.e. $$ \mid C \mid  <<  \mid \theta \mid $$.) It was shown by [Zhang et al 2017](https://arxiv.org/abs/1611.03530) that we can train a neural network to perfectly fit $$C$$. In other words $$\exists \theta_{C}$$ s.t. $$f_{\theta_{C}}(x) \approx y, \forall x,y \in C$$. Our networks have so much capacity that not only can they fit the correct labels, they can fit *arbitrary* corrupted labels!

One intuitive way to understand the difference between $$f_{\theta^*}$$ and $$f_{\theta_{C}}$$ is by their *generalization* properties. We can think of $$D$$ as a training set, and $$Z$$ as a test set. $$f_{\theta^*}$$ is a function which generalizes nicely: it performs well on both the train set (i.e. $$Pr(D \mid f_{\theta_{C}}) \approx 1$$) and the test set (i.e. $$Pr(Z \mid f_{\theta_{C}}) \approx 1$$). In contrast, $$f_{\theta_{C}}$$ is a function which generalizes poorly: it performs well on the train set (i.e. $$Pr(D \mid f_{\theta_{C}}) \approx 1$$), but terribly on the test set (i.e. $$Pr(Z \mid f_{\theta_{C}}) \approx 0$$). In general, empirically, SGD will tend to find nicely-generalizing solutions; however, we must keep in mind that poorly-generalizing solutions exist, too.

Now that we’ve defined these two functions, consider their relative probabilities under the posterior given data $D$. Assume we chose some prior $$q$$. We then see,

$$q(f_{\theta^*} \mid D) = \frac{Pr(D \mid f_{\theta^*})q(f_{\theta^*})}{Pr(D)} = \frac{1 \cdot q(f_{\theta^*})}{Pr(D)} = \frac{q(f_{\theta^*})}{Pr(D)}$$

Similarly,

$$q(f_{\theta_{C}} \mid D) = \frac{Pr(D \mid f_{\theta_{C}})q(f_{\theta_{C}})}{Pr(D)} = \frac{1 \cdot q(f_{\theta_{C}})}{Pr(D)} = \frac{q(f_{\theta_{C}})}{Pr(D)}$$

Now it is clear why the standard Bayesian story is problematic when combined with neural networks. Although $$f_{\theta^*}$$ generalizes well, and $$f_{\theta_{C}}$$ generalizes poorly, **the data does not allow us to distinguish between these two in the posterior**. The relative posterior likelihood of these two networks is determined entirely by their prior likelihoods.

## Can SGD Save Us?

No, it cannot. It is true that $$f_{\theta_{C}}$$ is unlikely to be *found* by running SGD on dataset $$D$$. But that does not mean that it does not *exist*. The true Bayesian posterior -- which is the only object that has the useful properties we are after, e.g. uncertainty information -- does not care about what functions SGD finds. The **only** way we can have $$Pr(f_{\theta_{C}} \mid D) < Pr(f_{\theta^*} \mid D)$$ is when $$q(f_{\theta_{C}}) < q(f_{\theta^*})$$.

## Bayesian Neural Networks Require Generalization-Sensitive Priors

It’s therefore clear that getting the prior right is absolutely essential to Bayesian deep learning. What we need are “generalization-sensitive” priors, which only assign prior probability to functions which generalize well. These stand in contrast to “generalization-agnostic” priors, for which $$q(f_{\theta^*}) \approx q(f_{\theta_{C}})$$, for any $$C$$ constructed as above. If our prior is fully generalization-agnostic, the posterior will assign just as much likelihood to *every bad solution* as to the true solution. This in turn implies that our Bayesian procedure will never yield a useful notion of uncertainty: every test point will simply have its probability mass spread over the full range of possible outputs.

In a sense, this phenomenon can be interpreted as an extreme example of the “overestimating the uncertainty” failure mode discussed earlier. In the standard Bayesian story, overestimating the uncertainty is more-or-less fine, because it simply means that we need to add a little bit more data to get things to concentrate. But when discussing the the overparameterized regime, “a little bit more data” simply won’t cut it. The amount of data we would need to add to get things to concentrate is intractably large. (And besides, even if we *were* able to obtain all that data, we’d likely just get a larger neural net and be right back where we started.)

## Are Current BNNs Generalization-Sensitive?

It's common to use simple priors for BNNs, e.g. independent Gaussian distributions over the weights. Combined with the architecture of the neural network, this induces a structural prior in function-space. It’s clear that this structural prior is non-trivial. For example, [Neal 1995](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.446.9306&rep=rep1&type=pdf) showed that infinitely-wide single-layer neural networks with independent random Gaussian weights correspond to a Gaussian Process prior. From an empirical standpoint, [recent research](https://sites.skoltech.ru/app/data/uploads/sites/25/2018/04/deep_image_prior.pdf) indicates that CNNs + SGD seem to be particularly good at representing natural images. We ran our own experiment to test this, and found that minimizing the loss on $$D$$ led to networks with significantly higher prior likelihoods than minimizing the loss on $$C$$. [Code is available in this repository.](https://github.com/jbuckman/bnn-blog-experiments)

However, this evidence is all circumstantial, and does not strike at the heart of the issue. As we demonstrated above, any Bayesian who claims “my posterior contains a distribution over the good solutions for this data” is implicitly claiming “my prior is generalization-sensitive.” This is a very strong claim, especially in the context of the simplicity of current priors. Could independent Gaussian weights really encode something so fundamental as generalization, even taking into account the architecture of the network? It’s possible, but it seems wise to remain skeptical. The onus is on the Bayesian community to perform the rigorous analysis and experimentation required to fully justify this claim.

## Isn’t The Empirical Success Of BNNs Evidence Of Good Priors?

No. Although in practice, BNNs *do* generalize to test points, and do seem to output reasonable uncertainty estimates, this does not immediately imply that they have generalization-sensitive priors. There is another piece to the puzzle: approximation. Computing $$q(f \mid D)$$ is a highly non-trivial task called Bayesian inference; a large community studies tractable approximations to this quantity. (For example, variational inference formulates the problem of computing $$q(f \mid D)$$ as an optimization problem.) The trickiness of computing $$q(f \mid D)$$ could actually be the key to why BNNs do something reasonable, despite their true posteriors being far too uncertain. They might not be learning anything close to the true posterior!

In order to claim that the uncertainties output by BNNs are valid, Bayesians must rigorously demonstrate that the distribution learned by a BNN actually resembles the true posterior. Initial experiments show that this is not the case: we are easily able to find two points where the first point has higher prior probability & data likelihood, yet the second point has higher posterior likelihood. This would not be possible if the BNN posterior were accurate. [Code is available in this repository.](https://github.com/jbuckman/bnn-blog-experiments) Again, however, this is merely a preliminary experiment, and not the full picture. More study is required.

## A Sober Look at Bayesian Neural Networks

The Bayesian community has produced decades of important insights in machine learning, and is often viewed as one of the most rigorous sub-communities within ML. However, in our opinion, Bayesian neural networks have failed to live up to this ideal. The Bayesian community has not demonstrated that the distributions output by BNNs correspond well to the true posteriors. Without this guarantee, BNNs are no different from any other neural network which maps its inputs to a distribution over outputs; researchers should therefore avoid making the claim that the distribution output by a BNN encodes model uncertainty.

Furthermore, we have demonstrated in this post that good uncertainty estimates *must* be centered around the generalization properties of NNs. To have any guarantees that the uncertainties provided by BNNs are useful, we first need to understand what makes specific neural network parameterizations generalize nicely or poorly. This is one of the most important questions in deep learning, but we as a field simply don't have that understanding yet. The Neural Tangent Kernel (which has a Bayesian flavor!) is one example of a promising approach to developing a true understanding of generalization. But until we have such an understanding, it seems unlikely that we will be able to design priors which leverage it.

Regardless of whether you believe that we can find good generalization-sensitive priors, it’s important that we, as a field, stop ignoring the crucial importance that the prior plays in the Bayesian framework, and stop taking it for granted that BNNs are a sound way to compute uncertainties. We need to think about priors critically, evaluate posterior estimates rigorously, and refuse to be swayed by sloppy arguments like “uninformative priors are good under uncertainty.” Now, it goes without saying that if, at some point, BNNs provide state-of-the-art uncertainty estimates, that is reason enough to use them (especially in an empirically-driven field like deep learning). But it’s important to understand that, just as there are reasons BNNs hold promise, there are also clear theoretical reasons BNNs might *not* pan out as a research direction. Our hope with this post is that by highlighting these potential issues, we can steer BNN research in a better direction.

*Many thanks to everyone who gave us feedback on the first version of this blog post. Hit us up on Twitter ([Carles](https://twitter.com/carlesgelada) and [Jacob](https://twitter.com/jacobmbuckman)) to continue the discussion!*
