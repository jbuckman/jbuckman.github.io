---
layout: post
title: Fair ML Tools Require Problematic ML Models
tags: ["deep learning", "ai fairness"]
published: true
mathjax: false
---

When I was fourteen, my interest in video games began to intersect with my interest in programming.
I would go through the files of computer games I played in an idle attempt to gain some insight into how they worked.
I mostly looked for plaintext config files in order to modify parameters to make my characters unbeatable.
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
Honestly, these reactions are so absurd that they are barely worth addressing; GPT-3 is not a living being with agency, it's a parameterized distribution of possible sentences.
GPT-3 sometimes outputs things like this because people sometimes write things like this.
Any discomfort is just an unfortunate consequence of the human tendency to over-anthropomorphize everything.
I don't think many serious AI researchers would react this way.

No, more concerning to me is the second-most-common type of reaction, which was some variant of "this is unfortunate but expected behavior, and we can fix it by modifying the training procedure."
Essentially: that this chatlog demonstrates that GPT-3 has some issues, but that these issues were predictable based on how GPT-3 was created.
Optimism on whether it is fixable varied; so did people's intuitions about possible solutions.
Some blamed the training data; they hypothesized that had OpenAI used a more carefully-constructed corpus, this behavior would not have emerged.
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

To make my point concrete, here's an example of a way to intervene on the sampling procedure to fix the issue, without modifying GPT-3 at all.[^1]
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
This must be addressed before tools based on these models can be deployed on real-world tasks.

It is at this point that my reasoning leads to a perspective which may be surprising to some readers; to a certain degree, my conclusions contradict the consensus opinion of a subset of the FATML community.[^2]
But these claims follow from the same principles as we've been using throughout this blog post:

**Any chatbot which is never sexist requires a model with an understanding of sexism.**
**Any chatbot which is never racist requires a model with an understanding of racism.**

And so on, for all similar issues of fairness and bias.
Therefore, we should absolutely *not* attempt to "fix" GPT-3 (or any other neural model) by removing examples of sexism and racism from its training data.
Doing this is directly counterproductive.
The more examples of sexism and racism it sees, the better it can model those behaviors, and the more certain we can be that a properly-constructed chatbot will avoid them.
When researchers think about what biases are present in the data, we should do so with the goal of identifying societal biases that are *not* present in the data, and *collecting data that informs the model about them*.
Then, we utilize the model in a way that prevents these biases from creeping into our application's output.
This is the only way to guarantee that those biases are not present.

---

Communication -- linguistic, verbal, visual -- is in many ways the greatest accomplishment of the human race.
But the other side of the coin is that many subtle expressions have the potential to cause dramatic harm.
History is rife with examples.

A few years ago, [H&M faced massive backlash for putting a t-shirt with a racially insensitive slogan on a black child](https://www.nytimes.com/2018/01/08/business/hm-monkey.html); in almost any other context, the problematic slogan would be a perfectly innocuous phrase.
Imagine training a language model on a dataset which has been completely and thoroughly scrubbed of racism, and setting up a chatbot which uses that model.
Sometimes, users will tell the model stories about their children; the chatbot responds with a context-appropriate compliment.
Very wholesome!
Maybe it will describe one particularly brave child as "the fiercest lion on the savannah".
Does it not seem reasonable that the chatbot, having never seen racism, might at some point describe a black child as "the coolest monkey in the jungle"?

[A man was shot, and another hanged, because of the ambiguity around a phrase](https://en.wikipedia.org/wiki/Derek_Bentley_case).
Does it not seem reasonable that a chatbot trained on bloodthirst-free data might suggest to the man with the gun that he "let the officer have it"?

[Seemingly ordinary](https://apnews.com/article/42939a95e2b694ec6262ff5949d910c9) [hand signs](https://thehill.com/blogs/blog-briefing-room/news/502975-california-man-fired-over-alleged-white-power-sign-says-he-was) can be interpreted as grave threats or insults.
Does it not seem reasonable that a chatbot might use the "V" or "OK" emojis?

[The first major Indian uprising against the British was fought in part because of a misunderstanding about the type of grease used on bullets](https://en.wikipedia.org/wiki/Bite_the_cartridge).
How will a chatbot know not to suggest that a Muslim order a dish with pork, or describe to a Hindu the delicious taste of beef?

[A Swedish diplomat set back relations with Iran by exposing the soles of his shoes, which is disrespectful in their culture](https://metro.co.uk/2012/12/10/swedish-diplomat-insults-irans-president-by-exposing-soles-of-his-shoes-3310937/).
[The British did the same with China, because a tradition to honor their fallen was seen as an insensitive reference to a Chinese defeat](https://www.theguardian.com/politics/blog/2010/nov/10/david-cameron-poppy-china-michael-white).
And so on.
The upshot is that ignorance is not sufficient for harm prevention.
There are many ways that text can cause harm, and even if a chatbot has never explicitly seen offensive writing, it is almost inevitable that it eventually will produce some.

Sure, maybe we could hard-code our chatbot to avoid these few special cases.
But this was just a small sample. What about everything else?
We can't hard-code everything.
Language is too broad in its scope, and cultural norms too subtle and varied to police effectively.
(Not to mention that they change over time!)
The last few years of progress in deep learning provide ample evidence that hand-engineering is terribly limited in its usefulness, and that language is best approached in a data-driven way.
The only real solution is for our chatbot to have access to a strong model of harmful language, so it can identify why that description would be inappropriate, and avoid causing this harm.

---

Of course, there is a huge question left unanswered: *how do we do it?*
Let's say someone follows my suggestion, and trains a language model with all the racist data left in the train set, so that it has a good model of racist dialogue.
What next? How do we turn it into a never-racist chatbot?

Unfortunately, I don't have the complete answer.
Given that this is the key goal of a whole subfield of ML, it would be ludicrous to expect otherwise!
However, the idea that it might be possible is not unpopular; many researchers in the FATML community are already working along these lines (see, for example, [He et al 2019](https://arxiv.org/abs/1908.10763)).
My main hope for this blog post is that it serves as a sort of negative result, ruling out approaches which involve learning unbiased models, and thus freeing up any researchers currently thinking about that direction to focus on more promising avenues.

With that said, let me share a couple of high-level ideas, just to give a sense of the solutions that I think might be possible.
One example is the technique I described in the last section: filtering using a racist-primed conditional probability model.
Due to the few-shot capabilities of large language models like GPT-3, such a conditional model can be constructed with very little training data.
Another approach we might consider derives from reinforcement learning.
We can place a reward model atop our language model, learning from human feedback what is and is not appropriate.
Once again, the power of the underlying language model means that the reward signal can be well-captured in a small number of feedback samples.
This has the added advantage of naturally updating our chatbot as cultural norms change through time.
Plus, many applications of language models will likely require reinforcement learning from human preferences anyways; this paradigm for preventing bias would naturally fit into those workflows.

---

Finally, I'll conclude with one last corollary: **every language model which has the potential to be used fairly has the potential to be abused.**
A model with an understanding of sexism can be turned into a sexist chatbot; a model with an understanding of racism can be turned into a racist chatbot; etc.
Therefore, it's not appropriate to criticize a model (or those who design/create it) on the basis that it *can* be produce unfair outcomes, when used poorly.
Instead, we should criticize those who *deploy* models in a way that does not adequately handle societal biases (or those who enable them).[^3]
There are already many examples of vision models which are worthy targets for this criticism: in the past few years, we have seen people deploy biased vision models which claim to detect criminality, sexuality, and more.
Let's continue pushing back against these misuses.
It's also important that we make sure that those who would deploy biased systems based on language models are aware that they cannot do so without consequences.
But let's not jump the gun and criticize people for merely studying the models.

It's worth pointing out that this phenomenon -- deciding whether to criticize those who develop a new technology, or those who abuse it -- is not unique to machine learning.
It echoes the debate in other fields of science, such as nuclear physics.
Progress in nuclear physics allows us to advance nuclear power and nuclear bombs.
Nuclear power provides a near-bottomless source of environmentally-friendly energy, and may be one of the keys to preventing climate change.
Nuclear bombs cause massive suffering and are a potential existential threat to humanity.
Machine learning has similar potential to change the course of humanity, both for the better and for the worse.
But if we attack ML research outcomes on the basis of their worst possible abuses, we lose our potential to progress.

---

#### Bottom Line

GPT-3 is not a chatbot, GPT-3 is a language model.
Naively turning GPT-3 *into* a chatbot results in a bad chatbot, which can say some harmful things; many criticisms of GPT-3 are actually criticisms of this "naive GPT-3 chatbot".
If we want unbiased chatbots, we need research on how to use language models to make unbiased chatbots, *not* attempt to train unbiased language models.
After all, unbiased language models fundamentally cannot be turned into unbiased chatbots.

This principle also applies to neural models more generally.
Real-world tasks can be decomposed into first training a neural model, and then *using* that model to help solve the task.
This often introduces issues of fairness or bias, which we need to fix before deployment.
The solution is never "make the neural models worse" -- removing data, adding esoteric constraints, etc.
Instead, researchers and practicioners should carefully study how the model is being utilized, and engineer the deployment step in a way that shuts down these issues.

All of this to say: know thine enemy, for we can't defeat what we don't understand.
And the same is true of neural networks.

---

**Statement on my personal beliefs.**
This post is, on some level, a criticism of the current beliefs of some researchers within the FATML community.
Unfortunately, this means that I find myself unavoidably associated with other critics of the FATML community, many of whom have used stupid arguments like "science is apolitical" and "ensuring social good is not my responsibility".
Therefore, I want to state in no uncertain terms: I wholeheartedly reject these perspectives.
It is the responsibility of every researcher to ensure that their impact on the world is positive and prosocial.
I have a deep respect for the goals of the FATML community, and believe that most members are aligned in their pursuit of those goals.
Although they mean well, some researchers in the community have made a mistake, one that in my view threatens to significantly set back progress towards those goals.
This blog post is my attempt to remedy that mistake; all criticism should be understood as purely academic.
I am engaging in good faith, and would love to have further good-faith discussions of these issues with anyone who is interested.


---

Thanks for reading, and hit me up on Twitter [@jacobmbuckman](https://twitter.com/jacobmbuckman) with any feedback or questions!

*Many thanks to Julius Adebayo and Carles Gelada for all of their help and feedback when writing this post.*

---

[^0]: Last year, there was a big, heated debate in the community over whether bias stems *just* from data, or *both* from data and algorithms. For the point I am making in this post, it does not matter which stance you take. I beg readers to please not derail discussion of my argument into a rehash of that debate.
[^1]: This, of course, is not the *only* way to fix the problem, or even necessarily the best way. It's just an example.
[^2]: The community is not a monolith, and there are many people who agree with my position, too! I'm also not claiming to be the first person to ever say this stuff. Just a boy with a blog :-)
[^3]: The main point I am trying to make here is only that we shouldn't be criticizing the model on the basis that it *could* be abused, we should be criticizing the *party that abused it*...and that only makes sense to do after it has actually been abused. But I don't intend to make broad assertions about who deserves blame if model misuse occurs; that could go a lot of different ways, and is very case-by-case. For example, I would totally approve of criticising someone who owns a potentially-dangerous model, if they give it away to a party that was not sufficiently vetted, who then uses it irresponsibly.
