---
layout: post
title: 'Rationality: Definition & Critique'
tags: ["philosophy", "rationality", "effective altruism", "AI safety"]
published: true
mathjax: false
---

I recently came across [this post](https://www.thelastrationalist.com/rationality-is-not-systematized-winning.html), which challenges readers to propose a definition for rationality, and figured I’d take a crack at it.

---

In my view, rationality is best understood as a decision-making philosophy. A rational agent acts according to *reason*. (In contrast, examples of non-rationalist decision-making include acting according to *tradition*, or acting according to *intuition*.) Someone who identifies as a “rationalist” is expressing their preference for making decisions rationally.

The core of rational thought, *reasoning*, is the process of going from premises to conclusions. Examples of reasoning include making a plan, debating a claim, or comparing trade-offs between various alternatives. The most rigorous form of reasoning is mathematical logic, in which all axioms are expressed in a formal language with explicit inference rules (designed to be both minimal and unambiguous). However, most reasoning is not so formal or explicit. The characteristic attribute of reason is *systematization*. The essential first step in reasoning about a problem is to express it in a reason-friendly framework; that is, to establish rules for inference and identify axioms. Once this is done, the rest of the process is systematic, almost mechanical. Applying the rules of the framework to your chosen axioms will inexorably lead to some conclusion.

This brings us to our definition of rationality: *strategic systematization*. Rationality is a *strategy* for achieving one’s goals that involves first *systematizing* a task by turning it into a tractable problem in a legible framework, and then solving this problem, yielding a decision for the original task.

For example, a rationalist whose goal is charity might establish a framework for measuring outcomes (e.g. utilitarianism), identify some axioms (e.g. empirical estimates of various quantities), and then reason with in the framework (e.g. compute marginal utility-per-dollar for donations various charitable causes) and select the action which comes out on top (e.g. bednets in Africa).

How does this improve upon the Yudkowsky definition: “rationality is systematized winning”? That attempt at a definition confuses what rationality *is* with what rationality *aspires to be*. The goal of *any* decision-making philosophy is to allow its practitioners to “win”, a term which here serves as a generic stand-in for an objective that someone might seek to accomplish. An actionable definition for a decision-making philosophy must take the form of a recipe for behavior, and if we have multiple philosophies defined in this way, we can compare them by seeing which one leads to winning more often. "Winning" is therefore a way to *evaluate* decision-making strategies, but not a useful way to *define* them. (Defining a strategy as "do what wins the most", and then advocating for it because “it wins the most”, is blatantly tautological.)

---

In the centuries since the Enlightenment, rationality has become the de-facto mode of thought for the entire modern world, almost completely supplanting other decision-making philosophies. Its cultural dominance is so complete that calling someone “irrational” is seen as a great insult. Almost all of the great scientific and technological developments of modernity emerged from rational thinking. In the face of such obvious and massive benefits, it can be easy to miss its limitations.

Systematization is the source of rationality’s strength, but also its Achilles’ heel. The process of reasoning gives us enormous leverage on our knowledge: for example, the ~10 [Peano axioms](https://en.wikipedia.org/wiki/Peano_axioms) are sufficient to derive essentially all of modern mathematics.
Rationality at its best can yield complex and surprising solutions to impossible-seeming problems.

But if, in the process of systematization, the original task becomes “corrupted”, rationality can go awry. Corruption here refers to the introduction of any difference between the original task we hope to solve, and the tractable problem we arrive at after systematization. For example, perhaps we got one of the axioms wrong; perhaps the original task was intractable, so we simplified it; perhaps our framework includes an inference rule that turns out to be invalid in some edge-cases; etc. If the systematized problem does not perfectly match the original task, the rational action (i.e. the optimal action according to our model) may be a poor action in reality. Furthermore, due to the aforementioned leverage, even a miniscule amount of corruption can lead to an incredibly poor action. An action that does not just fail to win, but yields a catastrophic loss.

---

[A follow-up question](https://www.thelastrationalist.com/rationality-is-not-systematized-winning.html): why don’t rationalists win?

Rationality is king when a task can be easily systematized, with little risk of corruption. This is most true in any closed system with well-defined rules, such as chess or mathematics; it also often works surprisingly well in the natural world, as evidenced by the predictive power of reductionism. It is least true in situations with many complex, poorly-understood, chaotically-interacting components, such as social customs in a society. In such situations, rational actions are often far worse on the true task than traditional or intuitive actions. When your model is poor, applying more reasoning will just cause you to stray further from optimality.

Compared to a rational actor, a traditional actor is much less likely to make a field-changing breakthrough, like a new scientific discovery. But the flip side of this is that they are also much less likely to radically redesign the economy in a flawed way and destroy the lives of millions. (My favorite books to on this topic are [The Secret To Our Success](https://press.princeton.edu/books/paperback/9780691178431/the-secret-of-our-success) and [Seeing Like A State](https://yalebooks.yale.edu/book/9780300078152/seeing-like-a-state/).)

That rationalists don’t seem to win more than non-rationalists is, in my opinion, merely reflective of the fact that the majority of life’s problems fall into the “too complex to model” category. For example, a classic rationalist failure mode is to rationally re-assess social conventions, and stop obeying the conventions that seem unreasonable. Unfortunately, the social world is sufficiently complex that an accurate understanding of the roles of various conventions is typically beyond even the most skilled and well-informed rationalist, and so their flagrant violations of social norms leave them genuinely worse off than an irrational rule-follower. 

Rationality is not a Swiss army knife, to be applied to every situation. It is a scalpel: a delicate, precise, and sometimes dangerous tool that should be brought to bear only when necessary. It should come as no surprise that a die-hard rationalist, swinging his scalpel around like a madman, might fail to open a can of tuna.

---

In November, a cryptocurrency exchange called FTX [collapsed in spectacular fashion](https://www.coindesk.com/business/2022/11/08/sam-bankman-fried-no-longer-a-billionaire-after-146b-wipeout-bloomberg/).

Prior to the collapse, many rationalists regarded its founder and CEO, Sam Bankman-Fried, with admiration, sometimes approaching reverence.
SBF was, by all accounts, an extremely rational guy.
He [was well-known for his adherence to the philosophy of acting purely in order to maximize expected value](https://80000hours.org/podcast/episodes/sam-bankman-fried-high-risk-approach-to-crypto-and-doing-good/), which is a rational approach to making money.
He [was also a major proponent of (and donor to) effective altruism](https://www.forbes.com/sites/johnhyatt/2022/11/14/sam-bankman-fried-promised-millions-to-nonprofits-research-groups-thats-not-going-too-well-now/?sh=298f93855ee8), a movement centered on a rational approach to charitable giving.

On the whole, reactions to the collapse were mostly what you would expect: pity for the victims who lost their money, and condemnation of his shady and unethical practices.
But an interesting subtext I noticed was the desire to shift the blame for the destructive outcome from his rational decision-making to other aspects of his personality.
For example, here is [Scott Alexander discussing the collapse](https://astralcodexten.substack.com/p/open-thread-250):

> Still, I’m reluctant to center the [expected-value maximizing] narrative here.
Hundreds of other crypto projects have proven fraudulent and gone bust without us needed to appeal to exotic branches of philosophy.
SBF is a semi-mythical figure.
It would feel appropriate if his downfall was for properly mythical reasons, like a deep commitment to literal [expected-value maximizing].
But I think in the end it will probably have at least as much to do with the normal human vices that we all have to struggle against.

Putting the object-level question of the true reason for the collapse[^0] aside, note the implied contrast between the noble commitment to expectation-maxing and grubby reality of human vice.
There is an underlying assumption that taking 2.1x-or-nothing bets is a virtuous ideal; that we should all aspire to overcome our fears, surpass our animal instincts, and execute perfectly EV-maxing decision-making in our own lives.

But this is a fundamentally confused position.
SBF acted rationally, in that he took actions that seemed optimal within his chosen framework of expected value maximization; however, there is nothing inherently correct about that choice of framework.
As I explain in [this essay](https://jacobbuckman.com/2022-11-18-on-the-road-to-st-petersburg/), the field of statistics has progressed in its understanding beyond naive expected-value maximization, and in a more modern framework, 2.1x-or-nothing bets are very irrational indeed.

To me, the FTX debacle is a perfect parable about why fully committing to rationally-derived conclusions is a terrible idea.
There are limits to one's knowledge, and meta-limits to one's understanding of one's limits.
The world is complicated enough that your framework will often be slightly wrong, and so your perfectly rational conclusions will nonetheless be somewhat erroneous.
If you've gone all-in, this can be catastrophic.
SBF's fall was not an unlucky break for man whose approach was admirable, it is the inevitable ultimate outcome of unrestrained rationality.

---

To avoid the pitfalls of blindly following rationally-derived conclusions, one must hedge by behaving irrationally.
Intuition and tradition are two examples of decision-making philosophies which are, on the whole, quite reliable.
These strategies take advantage of knowledge that has been implicitly bequeathed to you, but which is not explicitly accessible, and thus impossible to include in a rational framework.
For example, through evolution, your genetic ancestors passed down instincts on how to survive.
Through religion, your cultural ancestors passed down knowledge of how to live meaningfully.
Through social norms, your contemporaries spread knowledge of how to coordinate pro-socially.

When tradition or intuition prescribe behavior that conflicts with rationally-derived conclusions, this should be given serious consideration.
Don't dismiss the conflict out-of-hand because "it makes no sense".
*Of course* it makes no sense *in the context of the rational framework* that you have chosen: if it made sense, there would not have been a conflict in the first place.
Instead, search hard for a way to modify your behavior to satisfy tradition and rationality, or at the very least, a compromise.
This leverages knowledge that is not legible enough to be incorporated neatly, and clues you in to potential limitations of your current framework that can be iterated and improved on.

Now, I am not claiming pure reason is always flawed.
Sometimes, traditions that make no sense are also genuinely bad; for example, maybe they solved a problem that no longer exists.
It's absolutely possible to use rational thought to improve on the old ways.
But one must do so slowly and carefully, and constantly be on the lookout for reasons to revise your framework in the direction indicated by irrationality.
In particular, if your reasoning leads to shocking conclusions that contradict intuition and tradition – conclusions such as, “we should take repeated 2.1x-or-nothing bets”, “we should replace monogamous marriage with an alternative arrangement”, or “we should all donate our money to preventing a superintelligent AI from destroying humanity” – it is sensible to refrain from taking immediate or drastic action.
Instead, note that there is likely something wrong with your framework or axioms, and moderate your behavior accordingly.

---

It’s important to note that nothing I’m saying here is particularly original.
Many rationalists are aware of these ideas, and discuss them frequently; indeed, my thinking on these topics have been heavily influenced by rationalist circles.
For example, Scott Alexander has reviewed both [Seeing Like A State](https://slatestarcodex.com/2017/03/16/book-review-seeing-like-a-state/) and [The Secret To Our Success](https://slatestarcodex.com/2019/06/04/book-review-the-secret-of-our-success/), and sometimes uses more-or-less the same argument as I have laid out here, for example to argue against certain tenets of [longtermism](https://astralcodexten.substack.com/p/book-review-what-we-owe-the-future).
Similarly, the principle of moderation I described above is often referred to in rationalist circles as [Chesterton's fence] (https://en.wiktionary.org/wiki/Chesterton%27s_fence) or the [Lindy effect](https://en.wikipedia.org/wiki/Lindy_effect).
And so on.

But despite this awareness, I feel that for many self-avowed rationalists, the realization has not yet quite sunk in.
I find that it is common to pay lip service to the idea that rationality has limits but in practice privilege rational arguments and conclusions in almost all situations.
Many people and organizations (for example effective altruists and AI safety researchers) could benefit greatly from internalizing these ideas and adjusting their direction accordingly.
In many ways, my critique of effective altruism is precisely the same as the one EAs often level at non-EAs: when faced with a choice between *doing* good and *feeling* good, many give according to their feelings.
The only distinction is that for EAs, the positive feelings come from a self-perception of rationality.

---

Thanks for reading, and hit me up on Twitter [@jacobmbuckman](https://twitter.com/jacobmbuckman) with any feedback or questions!

*Many thanks to [Tony Pezzullo](https://www.linkedin.com/in/tonypezzullo) for the discussion that inspired this post.*

---

[^0]: Indeed, [subsequent interviews](https://www.vox.com/future-perfect/23462333/sam-bankman-fried-ftx-cryptocurrency-effective-altruism-crypto-bahamas-philanthropy) give the impression that much of his supposed rationality may indeed have been artificially crafted for his public persona.
