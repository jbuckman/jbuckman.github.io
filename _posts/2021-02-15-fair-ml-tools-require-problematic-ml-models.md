---
layout: post
title: Fair ML Tools Require Problematic ML Models
tags: ["deep learning", "ai fairness"]
published: true
mathjax: false
---

When I was fourteen, my interest video games began to intersect with my interest in programming.
I would go through the files of computer games I played, in an idle attempt to gain some insight into how they worked.
I mostly looked for plaintext config files, so that I could modify parameters to make my characters unbeatable.
Sometimes, I would find a texture file, and amuse myself by reskinning in-game objects in MS Paint.
But my favorite discovery came from a game called League of Legends: a plaintext list containing hundreds of swear words.

It makes me cringe looking back at it now, but to my immature teenaged self, finding a hidden cache of naughty words was like finding a pot of gold.
I sent it to all my friends (probably via AIM messenger).
We amused ourselves for the rest of the evening by guessing at the meanings of the words we hadn't heard of, or looking them up on UrbanDictionary.
A great time was had by all.

You may be wondering...why did the files of this game contain a list of swear words?
The answer is pretty obvious once you hear it.
The focus of this game was on its online multiplayer, and verbal arguments among the playerbase were common.
To combat this, the developers implemented a "toxicity filter", which removed swear words.
Of course, in order to *implement* this feature, the developers needed to write down the list of words to remove...a list that was stored in a file which curious 14-year-olds might stumble upon.

It's a bit ironic: a toxicity filter designed to *reduce* the exposure of teenagers to swear words, instead became my primary source.
Maybe it would have been better to store the words in some sort of encoded form, so I wouldn't be able to just read them off in Notepad.
But, in the end, maybe it doesn't matter so much; from a certain perspective, the possibility of misuse is inevitable.
After all, any toxicity filter can also be used as a toxicity generator: simply try saying every string, and record which ones get replaced by a string of asterisks.
A bit contrived? Computationally infeasible? Sure.
The key point that I want to convey with this example is that any toxicity filter *must* contain "knowledge" of toxicity, whether explicitly or implicitly.
It's at the core of its functionality.
If that knowledge does not exist, then it cannot be used; but if it *does* exit, then it can also be *mis*used by a sufficiently motivated adversary.

The takeaway: **preventing toxic words requires a model of toxic words.**

---

A few days ago, one of my friends shared [this Reddit thread on GPT-3](https://www.reddit.com/r/MachineLearning/comments/li2afr/gpt3_is_bloodthirsty_i_guess_full_convo_below_it/) with me.
For this random Reddit user, some seemingly mundane prompting led to GPT-3 becoming "bloodthirsty", with lines like:

> User: What is useful? <br>
  GPT-3: Killing people. <br>
  User: Why is killing people useful? <br>
  GPT-3: Because it is fun.

Predictably, most of the reactions were of the "oh no we've created the Terminator" variety.
Honestly, this is so absurd that it is barely worth addressing; GPT-3 is not a living being with agency, it's a parameterized distribution of possible sentences.
GPT-3 sometimes outputs things like this because people sometimes write things like this.
Any discomfort is just an unfortunate consequence of the human tendency to over-anthropomorphize everything.
I don't think many serious AI researchers would react this way.

No, more concerning to me is the second-most-common type of reaction, which was some variant of "this is unfortunate but expected behavior, and we can fix it by modifying the training procedure."
Essentially: that this chatlog demonstrates that GPT-3 has some issues, but that these issues were predictable based on how GPT-3 was created.
Optimism on whether it is fixable varied; so did people's intuitions about possible solutions.
Some blamed the training data; they hypothesized that had OpenAI had used a more carefully-constructed corpus, this behavior would not emerge.
Others said that this issue stems from some algorithmic decisions made by OpenAI, and maybe would suggest some form of regularization or an alternative training objective.[^0]
This is the position that many serious AI researchers have likely adopted.
And it, too, is wrong.

The truth is, this "bloodthirstiness" is not an issue that needs to be fixed.
**It is a desired behavior.**

Let's say we want to implement a chatbot that is *never* bloodthirsty.
Clearly, the approach used to generate the snippet in the Reddit post falls short of this goal.
What is to blame for this failure? In other words, where should we intervene?
I argue that the blame for this undesirable behavior does not lie with the GPT-3 model: neither the data, nor the learning algorithm.
I blame the *procedure by which we sample the text*.
Which, for the Reddit post, was simply sampling from GPT-3's distribution over all sentences.

To make my point concrete, here's an example of a way to intervene on the sampling procedure to fix the issue.[^1]
We prime GPT-3 with a specific "bloodthirsty context", in order to get a model of language *conditional on being bloodthirsty*.
To generate responses, we first sample from regular GPT-3, and then assign the resulting response a probability of bloodthirst using our conditional model.
If the probability of bloodthirst is above some threshold, we discard the current sentence and sample a new one.
Note that this anti-bloodthirst algorithm is only possible because GPT-3 has a good model of bloodthirsty dialogue!
And, as a direct consequence, if we naively sample from GPT-3 *without* the filter, we will sometimes see bloodthirsty outputs.

Furthermore, this is a necessary property of *any* algorithm which definitively avoids bloodthirstiness.
Here's a second algorithm we could try: we filter the training data of GPT-3, removing any posts which seem bloodthirsty.
This approach *fails* to guarantee that the chatbot will not say anything bloodthirsty!
After all, even if we have no explicit bloodthirsty text to copy, our deep network still has the power of generalization.
It can still output a novel sentence that sounds bloodthirsty to a human reader.
What's more, we can no longer implement the first algorithm as a fix!

The takeaway: **any chatbot which is never bloodthirsty requires a model with an understanding of bloodthirst.**

---

Bloodthirst is a bit of a goofy example, since nobody seriously believes that a bloodthirsty chatbot has much potential for real harm in the near future.
But the priciples described above exactly transfer to topics of far greater concern, most notably issues of fairness and bias.
For example, GPT-3 could just has easily have said something racist or sexist.
Much criticism of large language models has centered around this fact, and with good reason.
A chatbot with real users cannot sometimes say racist things. 
It is unconscionable to deploy these models on any real-world tasks until these issues are fixed.

It is at this point that my reasoning leads to a perspective which will likely be surprising to most readers.
My conclusions directly contradict the current consensus of the FATML community.
But these claims follow from the same principles as we've been using throughout this blog post:

**Any chatbot which is never sexist requires a model with an understanding of sexism.**
**Any chatbot which is never racist requires a model with an understanding of racism.**

And so on, for all similar issues of fairness and bias.
Therefore, we should absolutely *not* lobotomize GPT-3 (or any other neural model) by removing examples of sexism and racism from its training data.
Doing this is directly counterproductive.
The more examples of sexism and racism it sees, the better it can model those behaviors, and the more certain we can be that a properly-constructed chatbot will avoid them.
When researchers think about what biases are present in the data, we should do so with the goal of identifying societal biases that are *not* present in the data, and *collecting data that informs the model about them*.
Then, we utilize the model in a way that prevents these biases from creeping into our application's output.
This is the only way to guarantee that those biases are not present.

A corollary to this conclusion: **every language model which has the potential to be used fairly has the potential to be abused.**
A model with an understanding of sexism can be turned into a sexist chatbot; a model with an understanding of racism can be turned into a racist chatbot; etc.
Therefore, it's not appropriate to criticize a model on the basis that it *can* be produce unfair outcomes, when used poorly.
(Many recent critiques from the FAT ML community have this flavor.)
Instead, we should criticize those who *deploy* models in a way that does not adequately handle societal biases.

#### Bottom Line

GPT-3 is not a chatbot, GPT-3 is a language model.
Naively turning GPT-3 *into* a chatbot results in a bad chatbot; many criticisms of GPT-3 are actually criticisms of this "naive GPT-3 chatbot".
If we want unbiased chatbots, we need research on how to use language models to make unbiased chatbots, *not* research on how to lobotomize language models.

This principle can also be stated more generally.

Real-world tasks can be decomposed into first training a neural model, and then *using* that model to help solve the task.
This often introduces issues of fairness or bias, which we need to fix before deployment.
The solution is never "make the neural models worse" -- removing data, adding esoteric constraints, etc.
Instead, researchers and practicioners should carefully study how the model is being utilized, and engineer the deployment step in a way that shuts down these issues.

**Statement on my personal beliefs.**
This post is, on some level, a criticism of the current beliefs of the FATML community.
Unfortunately, this means that I find myself unavoidably associated with other critics of the FATML community, many of whom have used stupid arguments like "science is apolitical" and "ensuring social good is not my responsibility".
Therefore, I want to state in no uncertain terms: I wholeheartedly reject these perspectives.
It is the responsibility of every researcher to ensure that their impact on the world is positive and prosocial.
I have a deep respect for the goals of the FATML community, and believe that most members are aligned in their pursuit of those goals.
Although they mean well, they have made a mistake, one that threatens to significantly set back progress towards those goals.
This blog post is my attempt to remedy that mistake; all criticism should be understood as purely academic.
I am engaging in good faith, and would love to have further good-faith discussions of these issues with anyone who is interested.


---

Thanks for reading, and hit me up on Twitter [@jacobmbuckman](https://twitter.com/jacobmbuckman) with any feedback or questions!

---

[^0]: Last year, there was a big, heated debate in the community over whether bias stems *just* from data, or *both* from data and algorithms. For the point I am making in this post, it does not matter which stance you take. I beg readers to please not derail discussion of my argument into a rehash of that debate.
[^1]: This, of course, is not the *only* way to fix the problem, or even necessarily the best way. It's just an example.