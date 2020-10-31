---
layout: post
title: Updating the Accepted Wisdom in Offline RL
tags: ["deep learning", "reinforcement learning"]
published: true
mathjax: true
invisible: true
---

Many people are becoming interested in "Offline RL" these days.
I'm quite interested in it, too;
for the past two years, I've been thinking hard about this setting, together with my collaborators Carles and Marc.
In that time, the community has proposed many cool algorithms and run many insightful experiments.
[Our recent paper](https://arxiv.org/abs/2009.06799) adds to this growing body of work by providing a rigorous theoretical understanding of the fundamental issues underpinning the Offline RL setting, including a formal unification of existing approaches.

In tackling the problem, the Offline RL community has developed a set of intuitions.
Researchers have a sense of what works and what doesn't, of what problems exist, and what causes them.
This is what one might call the the "accepted wisdom".
Pick up any paper on Offline RL, and you're likely to see many references to ideas which are accepted wisdom, often used to motivate their new algorithms.
Although many of these ideas have not been totally proven, they are simple, intuitive, and have some empirical evidence behind them, so they are widely believed.
One important contribution of our paper is that, for the first time, we have theoretical justification of many of the tenets of accepted wisdom.

Even more importantly, our work has revealed several ways in which the accepted wisdom is wrong.
Not *totally* wrong; just subtly wrong, seeing part of the picture but missing some non-obvious connections and nuances.
In this blog post, I will highlight five of our most interesting results, contrasting the accepted wisdom with our findings.

### (1)
**Accepted Wisdom:** *Overestimation bias causes bad performance.*

**Reality:** *Bad fixed-points cause us to observe both bad performance and overestimation.*

Some background on this: an easy way to go from an Online RL algorithm to an Offline RL algorithm is to simply add the initially-available data to its replay buffer, and train as normal, skipping any steps of interaction (which are disallowed in this setting).
But empirically, this does not work at all.
The more steps of training we do, the more performance drops.
One of the key questions in studying Offline RL is: why?

One explanation that has often been referenced is the idea of "overestimation bias".
This theory notes that the neural networks we use to represent our Q-value sometimes make approximation errors, and that when the errors are overestimations, they get propagated back through the argmax of the update.
Over time, this leads to the approximation errors getting propagated throughout the state space, leading to poor value estimates and sometimes to divergence.

This idea is very nearly correct, but it misses the mark in a few subtle ways.
First of all, our paper shows that overestimation can emerge even in tabular environments, where there is no approximation error at all.
Furthermore, it's clear that preventing overestimation does not, alone, causally improve performance; we could subtract a large constant penalty from each value and thereby reduce overestimation, but this would not improve the learned policy.
Finally, overestimation bias doesn't explain why model-based Offline RL algorithms, which do not bootstrap, also suffer from overestimation and poor performance.

If overestimation bias doesn't explain the issue, what does?
We provide a new lens through which we can understand this phenomenon: fixed-points.
Offline RL algorithms can be viewed as fixed-point-finding algorithms.
Each time we apply an update to the Q-function, minimizing some error on the dataset, we move its values closer and closer to some fixed point, until eventually we converge.
The performance of any Offline RL algorithm can be captured by considering its fixed point.[^0]
Once we have found a fixed-point for the Q-function, which represents our best guess about the Q-function in reality, we can select its optimal policy.
Different algorithms will have different fixed-points.

When we take a DQN-like Offline RL algorithm, and look at its fixed point, we find something surprising.
The the fixed-point Q-function is likely to be highly overestimated, and also likely to be terrible!
In this way, we see that overestimation does not need to emerge from a process of "overestimation bias", where iterative updates cause approximation error to compound.
It is a property of the fixed-point: it is built directly into the objective, regardless of what computational procedure we use to get there.
We cannot improve the performance by reducing overestimation.
We can only improve the performance by improving the quality of the fixed-point.
It's possible to do either without doing the other, so it's important to think carefully about the distinction.
(Although, they do often go hand-in-hand.)

*How does this insight relate to current research?*
Some recent papers, like [CQL](https://arxiv.org/abs/2006.04779), prove that they reduce overestimation, but do not prove that they improve the quality of the fixed point.
Until such a property has been shown, we should not consider these algorithms to be theoretically justified.

### (2)
**Accepted Wisdom:** *Distributional shift is one of the central challenges of Offline RL.*

**Reality:** *Generalization error is one of the central challenges of Offline RL.*

People use the term "distributional shift" to refer to the situation where the states present in the dataset used to train an Offline RL agent are different from the states that the learned policy visits.
In such cases, it is argued, it becomes more likely that the agent will make mistakes, leading to poor returns.
This argument motivates Offline RL algorithms which constrain the agent to only visit states, or to only take actions, that appear often in the dataset.

Once again, the accepted wisdom is nearly-right, but subtly wrong.
The core issue is that the accepted wisdom conflates *data* with *information*.
These two ideas again go hand-in-hand, so it is perhaps not surprising that people have failed to disentangle them.

A simple example illustrates that these are distinct, even in the tabular setting.
Consider a tabular bandit-like MDP with two arms, A and B, with returns in \[-1000, 1000\].
Our offline dataset contains the following pulls for A:
\[5, 5, 5, 5\].
And the following pulls for B:
\[620, -829, 73, -131, -86, -617, -62, 964, -429, -372, 951, -709, 766, -14, 507, -758, 947, 879 \]
We've seen five times as many pulls for B as for A.
Yet, we clearly know much more about the mean of A than that of B.[^1]
Each pull of A is simply much more informative.

In tabular cases like the above example, this could perhaps be fixed by taking into account some more complicated statistics of the outcomes, such as variance.
But, when we move to the deep learning setting (which is what we really care about anyway), such techniques are inadequate.
Neural networks can often generalize in bizarre and complex ways.
Any data point can be informative of any other data point.
No simple density-like or count-like technique captures the nuances of neural network generalization.

Instead of "distribution shift", we need a more expressive notion: *generalization error*.
We do not want our algorithms to constrain us to areas with high counts, but to areas with small generalization errors.
This is a much more difficult task!
It may be fine sometimes to use high-count as a proxy for low-error (the two often go together to some extent), but it is important that we correctly identify the true goal.

*How does this insight relate to current research?*
[Many](https://arxiv.org/abs/1812.02900) [recent](https://arxiv.org/abs/1911.11361) [papers](https://arxiv.org/abs/2007.08202) use counts or density models to measure state/action visitations and constrain the policy.
We should note that such approaches are unlikely to be optimal, since they are using counts as a proxy for generalization error.

### (3)
**Accepted Wisdom:** *There are three distinct approaches to Offline RL, "policy constraint", "uncertainty-based", and "lower-bound".*

**Reality:** *There is a unifying framework, pessimism, which connects all of these algorithms.*

First, I'll briefly summarize each of these three types of methods.[^2]
*Policy constraint* methods are characterized by the fact that they compute some divergence between the distribution of data in the batch, and the policy learned by the Offline RL algorithm.
They then turn this divergence into a constraint, preventing the policy from selecting actions (or visiting states) for which the divergence from the data is too large.
*Uncertainty-based* methods are characterized by the fact that they compute the epistemic uncertainty of the Q-function, and use it to construct a penalized Q-function.
They then select a policy which is optimal according to this penalized Q-function.
*Lower-bound* approaches learn a Q-function which is guaranteed, with high probability, to be a lower-bound to the true Q-values of the environment.
They, too, select a policy which is optimal according to this lower-bound Q-function.

In our work, we show that these three approaches can be derived from a common framework, which we call *pessimsim*.
A pessimistic Offline RL algorithm finds the optimal policy of a Q-function which has been penalized by a "pessimsim penalty", which is then rescaled by being multiplied by a hyperparameter α in \[0,1\].
It is easy to see how this relates to the uncertainty-based algorithms above; those algorithms are simply a special case, which occurs when the pessimism penalty is derived from epistemic uncertainty.
Furthermore, we prove in our paper that policy constraint methods are also a special case of a pessimism penalty, corresponding to the case where the pessimism penalty is $V_{max}$, the maximum possible value in the environment.
Finally, our derivation requires that any pessimism penalty must have a special property: when α=1, the resulting penalized Q-function is also a lower-bound to the true Q-values of the environment, unifying the final category.
Thus, all three approaches can be viewed as simply special cases of our more general framework.

### (4)
**Accepted Wisdom:** *The three approaches discussed in (3) are all equally promising research directions.*

**Reality:** *Uncertainty-based approaches are fundamentally better than the other two.*

This result may be surprising, since it is rare that strong negative theoretical results are available in deep learning.
However, our paper makes it very clear.[^3]
Also, for the empirical-minded among you, we back up these results with experiments which perfectly match the predictions of our theory.
Here's a high-level explanation of why; refer to [the paper](https://arxiv.org/abs/2009.06799) for full justification.

*Policy constraint:* Policy constraint approaches use a "vacuous" pessimism penalty of $V_{max}$, which is strictly worse than any possible epistemic uncertainty estimate.
For any policy constraint approach, there is a corresponding uncertainty-based approach that has an equal-or-better suboptimality bound.

*Lower-bound:* Recall that lower-bound approaches which are also pessimistic approaches simply have set the scaling hyperparameter of the pessimism penalty to 1.
Our derivation makes it clear that the suboptimality is non-convex wrt this hyperparameter, and thus, in general, setting it to a value which is not 1 will be optimal.
Lower-bound approaches are simply a less flexible version of uncertainty-based approaches.

This result begs the question: if uncertainty-based approaches are fundamentally better, why is this not reflected in experiments on Atari?
We discuss this in more detail in the paper, but the short of it is: nobody knows how to compute epistemic uncertainty with neural networks.
Various approaches have been proposed which *attempt* to do this, and some do things which are qualitatively reasonable.
But our derivation requires uncertainties where a very specific property holds, and at the end of the day, no existing approach to computing neural uncertainties is adequate.
(By the way: concentration inequalities *do* give us rigorous uncertainties in the tabular setting, and in our tabular experiments, we *do* see uncertainty-based approaches outperforming the others -- just as predicted.)

*How does this insight relate to current research?*
Right now, most research seems to be focused on policy constraint approaches.
Many researchers focus on nuances of the algorithms, such as comparing the specific divergence function used to compute the constraint.
While this knowledge may be useful in the short-term, we should be mindful of the fact that this work will likely eventually be wasted.
Since uncertainty-based algorithms are fundamentally better, if effective algorithms of this type are ever developed, their performance will inevitably dominate that of penalty-based algorithms, rendering knowledge of their nuances irrelevant.

### (5)
**Accepted Wisdom:** *Offline RL is important because for many real-world problems, it is difficult to collect data.*

**Reality:** *Offline RL is important because it is a sub-problem of "store-then-optimize RL".*

(Disclaimer: this final point is more speculative than the other four, but I wanted to include it anyway.)

Almost everyone in the community has heard the standard justification for why Offline RL is important.
I'll just quote the introduction of [Sergey Levine's Offline RL survey](https://arxiv.org/abs/2005.01643), which captures the gist of it:

> In many settings...online interaction is impractical, either because data collection is
expensive (e.g., in robotics, educational agents, or healthcare) and dangerous (e.g., in autonomous
driving, or healthcare). Furthermore, even in domains where online interaction is feasible, we might
still prefer to utilize previously collected data instead – for example, if the domain is complex and
effective generalization requires large datasets.

This motivation is completely correct!
Healthcare, driving, etc. are all important applications, and it makes sense to use Offline RL to find an optimal policy without permitting data collection.[^4]
But this is just a small part of the broader picture.

Rather than view Offline RL and Online RL as two separate settings, let's unify them.
We can say that there is just a single setting -- "general RL" -- and it includes *both* an initial dataset, as well as the ability to learn from the outcomes of its actions.
Each action also incurrs a (possibly episodic or state-dependent) discount factor, so that rewards cannot continue being accrued forever.
The goal in this setting is to maximize total cumulative return.
In the special case where the episodic discount is 0, we are doing Offline RL; in the special case where the initial dataset size is 0, we are doing Online RL.

Now, I'm going to take off on a bit of a tangent.
(Don't worry -- I promise it'll connect back to Offline RL by the end!)
I'm going to describe a specific family of algorithms for this setting, which I call *store-then-optimize RL algorithms*.
These algorithms work as follows:

Whenever we take an action, we *store* the outcome in our dataset, adding it to our ever-growing collection of observed transitions.
Then, before taking the next action, we *optimize* a policy to maximize some objective, using our dataset.
When we do so, we optimize to convergence, taking as many steps of computation as are required.
(To be clear, store-then-optimize is not a new idea; scattered examples exist, e.g. Rich Sutton's [Dyna](https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume4/kaelbling96a-html/node29.html) algorithm, which is more-or-less member of this family.
But these algorithms are much less well-studied than more-standard "streaming" approaches.)

Let's contrast store-then-optimize RL against more typical RL algorithms, such as Q-learning.
Standard Q-learning interleaves steps of interaction with steps of learning.
After each interaction, it uses the resulting transition to update its Q-function and policy, and then throws away the transition forever.
Algorithms like DQN, which use a replay buffer, draw a little bit closer to store-then-optimize.
Rather than use each data point once, DQN uses each data point (on average) eight times.
Still, though, this is a far cry from storing forever and optimizing to convergence.

I am very excited about the promise of store-then-optimize RL due to [Sutton's "Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html).
Store-then-optimize algorithms allow us to maximally leverage our compute, by training all the way to convergence at every single moment.
It also allows us to fully leverage our data; every data point teaches us something about the environment, so by never throwing anything away, we maximally utilize the information we have obtained.
To me, it seems clear that this must be the way to maximize sample efficiency.

Okay, now, let's take a look at how store-then-optimize RL algorithms actually function.
The "store" step is easy -- we just add the new transition to our dataset (which functions identically to a replay buffer, except it never discards anything).
Then comes the "optimize" step.
We have a fixed dataset, and we now run many steps of computation in order to optimize our policy.
Does that sound familiar?
That's right -- it's almost identical to Offline RL![^5]

Now, you can hopefully see why I believe that the *true* potential of Offline RL comes from how it will impact research on "regular" RL.
The study of this setting will play a crucial role in the development of sample-efficient RL algorithms, which use the store-then-optimize principle to push both data and compute to its limits.
From this perspective, the (already-massive) goal of solving decision-making in medicine/driving/etc become simply a small special case
(i.e. episodic discount of 0, so there is no need to consider exploration in the optimization).
But it would also open up a path to solving countless other real-world RL problems, where interaction is permitted but sample-efficiency is crucial, such as in robotics, dialogue, and more.

### Conclusion

Hopefully this post provided a helpful little update in your understanding of the Offline RL setting.
In addition to containing the mathematical justification of the five points I discussed here, [our paper](https://arxiv.org/abs/2009.06799) also contains plenty of other insights.
We spent a lot of time on the writing, so, it should hopefully be accessible to anyone in the field.
As always, please hit me up via email or [on Twitter](https://twitter.com/jacobmbuckman) with any questions or comments!

[^0]: Well, almost...this assumes that we have enough compute power to converge all the way to the fixed point. In limited-compute settings, it may be fair to consider the "path" taken to get to the fixed point, perhaps by analyzing the rate at which it is approached. But, in keeping with [Sutton's "Bitter Lesson"](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), I don't think it's too important to be concerned about this.
[^1]: If not satisfied that we know more about the mean of A than B, increase the variance on B until convinced.
[^2]: The three categories I describe correspond to sections 4.3, 4.4, and 4.5 in [Sergey Levine's Offline RL survey](https://arxiv.org/abs/2005.01643), respectively.
[^3]: An important caveat: I admittedly did not explicitly prove tightness in the paper, so all of my suboptimality results are merely upper-bounds. For most of the main results, tightness is not hard to show, but until I actually write it up, in theory it may still be possible for someone to come up with a tighter suboptimality bound such that my conclusions do not hold. If you have doubts, please be sure to check out the paper for yourself and come to your own opinion as to whether it is convincing, and let me know what you think!
[^4]: Though, when it comes down to it, I think that in the ultra-long term, many of these fields could be considerably improved by allowing an AI to control the exploration-exploitation trade-off. Of course, I don't think this is likely now, or in the near future. It would require massive theoretical breakthroughs (RL would need to actually work, for one), as well as massive societal changes (to ensure that the public trust in these systems is not shattered).
[^5]: Actually, it's a bit more general than Offline RL. In the standard setup for Offline RL, we are basically doing pure exploitation: learning the policy that looks best *right now*, with no thought to how our further data collection might improve our policy down the line. If we are optimizing a policy as a subroutine of a store-then-optimize algorithm, we will likely want to choose an objective which captures both exploration and exploitation. That's one of the reasons why, in my paper, I prefer to call this setting "Fixed-Dataset Policy Optimization", which better captures the general case.