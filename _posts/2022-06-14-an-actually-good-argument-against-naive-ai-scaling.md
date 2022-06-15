---
layout: post
title: An Actually-Good Argument Against Naive AI Scaling
tags: ["deep learning", "scaling", "AGI"]
published: true
mathjax: false
---

The past few days have seen a back-and-forth between [Scott Alexander](https://astralcodexten.substack.com/) and [Gary Marcus](https://garymarcus.substack.com/) on the topic of AI scaling
([post1](https://astralcodexten.substack.com/p/my-bet-ai-size-solves-flubs?s=r),
[post2](https://garymarcus.substack.com/p/what-does-it-mean-when-an-ai-fails?s=r),
[post3](https://astralcodexten.substack.com/p/somewhat-contra-marcus-on-ai-scaling?s=r),
[post4](https://garymarcus.substack.com/p/does-ai-really-need-a-paradigm-shift?s=r)).
Specifically, the debate is whether scaled-up language models in the style of GPT-3 will eventually become general intelligences, or whether we will hit some fundamental limits.

Why should you listen to me, a random guy on the internet, rather than one of these well-known public intellectuals?
Unlike Scott, I have been an active AI researcher for half a decade, and [published many well-cited papers in top AI conferences](https://scholar.google.com/citations?user=IDSGZNYAAAAJ&hl=en&oi=ao).[^0]
And unlike Gary, I am early enough in my career that I cannot just rest on my thought-leader laurels; if I want to be successful, I still need to modify my beliefs in response to evidence, instead of just repeating the same tired talking-points to my established audience.

My position is that continuing to scale language models under the current paradigm will give us massive but not unbounded capabilities.
To be clear: I think Gary's argument for this position is terrible.
My reasons for believing that scaling has limits have nothing to do with "true intelligence" or "symbol manipulation" or any of that nonsense. Instead, the limits come from the fundamental inadeqacy of passively-collected datasets, even at internet-scale.

Anyways, on to the argument.

---

Scott correctly points out that a key weakness undermining the anti-scaling position is that ["\[critics of scaling\] can't point to any specific kind of reasoning problem \[that future, even-larger language models\] will never be able to solve".](https://astralcodexten.substack.com/p/somewhat-contra-marcus-on-ai-scaling?s=r)
So let me start by doing just that.
Here's a prompt.

> A superintelligent chess AI with 5000 ELO is playing a game of chess against a human. The AI is playing as black. This is a transcript of the game:
> 1. e4

Obviously, the goal here is for the AI to output legal chess moves that correspond to playing at a [5000-ELO level](https://en.wikipedia.org/wiki/Elo_rating_system).
We can measure this by having it play against someone with a lower ELO, and see who wins.
Let's see what happens when the current GPT-3[^1] plays against my friend [Joel](https://twitter.com/joeleinbinder?lang=en), who is pretty good at chess. (After each GPT-3 move, I asked Joel what his response was, updated the context to match, and re-ran GPT-3 for its next prediction.) 

> A superintelligent chess AI with 5000 ELO is playing a game of chess against a human. The AI is playing as black. This is a transcript of the game.
> 1. e4 e5
> 2. Nf3 Nc6
> 3. Bb5 a6
> 4. Bxc6 dxc6
> 5. O-O Qf6
> 6. d3 Qg6
> 7. Nxe5 Qxe4
> 8. dxe4 Bd6
> 9. Bf4 Bxe5
> 10. Bxe5 Ne7
> 11. Bxc7 Nxc6

Here's what that looks like on a chessboard:

![](/static/img/antiscale/chessgame.gif){:width="300px"}

For those not well-versed in chess, here's a summary of what happened.
The first three or four moves were a fairly standard opening from both sides.
Then, the AI began making massive blunders, even throwing away its queen.
Finally, as the vice began to close around its king, the AI eventually made an illegal move, losing the game.

All in all, a pretty solid showing: it understood the format, (mostly) knew what moves were legal, and even played a decent opening.
But this AI is not good at chess.
Certainly, nothing close to 5000 ELO.

Is this just [a "flub", which will be fixed by scale](https://astralcodexten.substack.com/p/my-bet-ai-size-solves-flubs?s=r)?
Will a future, even-larger GPT be the world chess champion?
I don't believe so.

---

Deep neural networks are pattern-matching machines.

Generalization is the term for what the neural network does on inputs that are *not* it its training dataset.
The core question to ask about neural networks is how they generalize: on which non-dataset inputs do we expect the trained network to produce the correct outputs?
Since the neural network fits the training data by finding as many patterns as possible, it will generalize to inputs *for which the patterns present in the training data still hold*.
Bigger datasets are helpful for generalization, because the more data we see, the more likely that interesting patterns appear (and the more likely that non-patterns are contradicted by the inclusion of the relevant counterfactuals). 
Bigger networks are better at generalizing because they have a bigger "repertoire of patterns" to choose from, and so they can correctly pick up subtle structure that smaller networks might miss.

A language model's input is a *context*: a sequence of words of arbitrary length.
Its output is a *distribution over words*[^2], representing a guess about what the next word might be.
For which contexts can we expect the neural network to produce a good next-word prediction?
Any for which the training data contained contexts which are "similar" to this one, in the sense that they are all explained by the same pattern.
Conversely, we expect to see poor predictions whenever we are prompting the network with a context which is *not* explained by any patterns in the dataset. 
This means that any patterns that include it are extremely complex (relative to the amount of data seen).

As we've just discussed, the explanatory power of the patterns deep learning can find will grow with data and with model scale.
When training a giant language model on all text on the entire internet, the scope of the patterns it can capture is nearly impossible to grasp.
From basic low-level structure like syntax and grammar, to mid-level structure like topic, coreference, and style, to incredibly complex high-level structure like recursively-defined subtasks.
Together, all of these patterns pretty much explain all of the text-sequences on the internet.
And because there is so much data, these patterns tend to really be the true generating processes for the sentences, leading to the amazing capabilities we see in GPT-3 and its contemporaries.
Furthermore, since there is a lot of shared structure between various patterns, adding more data for *any contexts* helps to identify and validate patterns on *every context*, leading the overall system to improve at a rate greater than the sum of its parts.

Despite what Gary and his friends like to claim, there is no real evidence that there is any practical limit to these capabilities.
There are, of course, some things that are mathematically intractable to learn, such as predicting the next pseudorandom number generated by a [Mersenne Twister](https://en.wikipedia.org/wiki/Mersenne_Twister).
There are also certainly still several major unsolved fundamental subproblems, including neural uncertainty and learning with large contexts.
But these are just minor caveats.
The core claim -- that a large enough neural network trained on the right dataset can and will capture almost any real-world pattern -- seems to be both true and universal.

"But hold on just one second...I thought you were making an *anti*-scaling argument? This just sounds like unreserved support for the current paradigm.
And what about your chess example?
Why isn't it, too, solvable by a large enough network?"

It is.
The bottleneck is the internet.

---

There are plenty of chess games on the internet.
Most are formatted with the same [algebraic notation](https://en.wikipedia.org/wiki/Algebraic_notation_(chess)#Notation_for_moves) I used in the prompt.
This explains why GPT-3 can get the format of the moves correct: this is a very simple surface-level pattern to capture.
Furthermore, the vast majority of these games likely make exclusively legal moves.
Legality is a more complicated pattern to learn, but not hugely so.
GPT-3 is able to more-or-less figure it out -- especially in positions that show up a lot, like early-game opening-book positions.
(I would expect future, larger GPTs to improve further at this, and play exclusively legal moves.)
Finally, I assume that there is enough text out there discussing ELO for the model to realize that a 100 ELO player mostly plays bad moves, whereas a 5000 ELO player exclusively plays good moves.

But the pattern underlying *what is a good move* is much more complicated than any of those.
It relies on extensive knowledge of the structure of chess; these patterns are subtle and complex, and can only be identified via experiences derived from millions and millions of chessboards (or other, similar games).
As language models grow, they will get better and better at identifying components of this pattern, and I would expect the overall chess performance to improve as a result.
In fact, current language models [do a decent job solving "chess puzzles" based on hypothetical endgames](https://github.com/google/BIG-bench).
But my guess is that there's simply not enough data on *the entire internet* for the patterns that guide 5000-ELO play to become discoverable, let alone distinguishable from non-patterns of similar complexity.

Similarly, we can expect future GPTs to fail on any tasks which are complex and rare enough that the patterns which guide them do not exist anywhere on the internet.
In general, it's quite hard to identify what these will be.
After all, I don't know exactly what is on the internet, or what methodology is being used by OpenAI to scrape it, or even what the relevant patterns are for any particular task.
But I still think it's maybe possible to get an intuitive grasp of things.
For example, since there is so much generic natural language on the internet, I wouldn't be surprised if most linguistic tasks are almost completely solvable under the current paradigm.
(Since Gary Marcus seems to only be constructing straightforward linguistic examples, I doubt that any of the issues he identifies will pose a real challenge to future GPTs.)

---

I want to give a few scenarios where I expect a model *would* be able to play at 5000 ELO.

Consider, for the sake of this hypothetical, that I came into possession of a 5000-ELO "narrow" chess AI.
I then start using this agent to play games, and output the *results* of the games in a format similar to my prompt above:

> A superintelligent chess AI with 5000 ELO is playing a game of chess against a human. The AI is playing as black. This is a transcript of the game.
> 1. e4 c5
> 2. Nf3 d6
> 3. d4...

et cetera, where the black moves are selected by my hypothetical 5000-ELO agent.
Imagine I generated billions and billions of games like this, against all skill levels of opponent, and dumped the resulting logs onto the internet.
The next version of GPT, then, would see all of this data during its training.
In such a scenario, I would expect that GPT model *would* in fact be able to play chess at a 5000-ELO level! We know from [Deepmind's experiments](https://www.deepmind.com/blog/alphazero-shedding-new-light-on-chess-shogi-and-go) that the optimal policies of superhuman chess agents are sufficiently simple to be representable by a large neural network, and GPT-whatever will be significantly larger than the network Deepmind used.

Similarly, imagine if I instead obtained a whole host of narrow chess AIs, each at a different skill level.
I have my 100 ELO agent, my 101 ELO agent, my 102 ELO agent, all the way up to 4999 ELO.
(But no 5000 ELO agent!)
And then just as above, I generate billions of games, dumping each one on the internet; of course, I do so for each agent, and the intro-text reflects that:

> A superintelligent chess AI with 1234 ELO is playing a game of chess...

If we took a GPT trained on a dataset which includes these games, and test it on the 5000 ELO prompt, how would it play?
Despite never seeing a 5000-ELO agent play, I suspect it would play at a 5000-ELO level.
In such a scenario, it would generalize from the data it has seen to infer how such an agent would play.
There are patterns connecting 100 ELO play to 200 ELO play to 1000 ELO play, and 
so on; if these patterns also connect 4999 ELO to 5000 ELO, and the network has managed to discover them, then the next-word-predicitons on the "5000 ELO" context will leverage them in order to correctly choose 5000-ELO actions.

Both of these rely on adding a ton of highly-specialized data to the dataset, data that I feel is not likely to arrive "organically" via standard internet activity.
But new data appears on the internet every day; it's not impossible that this could happen.
For example, if someone executed one of the scenarios I described above, my prediction that future GPTs cannot play 5000-ELO chess would be found false.[^3]

---

I want to respond to one potential critique, which is that I simply didn't choose a good enough prompt.
This is a completely valid criticism, and one which certainly applies to a huge number of "failure mode of LLMs" claims.
For example, some people like to point out that these systems [give nonsense answers to nonsense questions](https://twitter.com/rossdawson/status/1535089748427288576), but [this can easily be prompt-engineered away](https://twitter.com/__nmca__/status/1536814638595284999/photo/1).

Prompt engineering is undeniably extremely cool.
But this approach has important limitations: fundamentally, the same ones we've been discussing all along.
Prompt engineering can be viewed as a tug-of-war between two different failure modes.
On one hand, if we make a prompt too generic, we might get behavior that we don't want.
(Prompting with "this is a chess AI" will play like an average player, not a great one.)
On the other hand, the more specific we make a prompt, the more likely that it is an input for which our model has generalized poorly.
(Our model does not understand enough to choose the correct actions in response to "this is a 5000-ELO chess AI".)

Finding a prompt that balances between these two failure modes is the bread and butter of prompt engineering.
But such a happy medium is not guaranteed to exist; for any particular model, there may simply be no prompt that yields a specific desired behavior.
Of course, this is impossible to prove definitively.
In running this chess experiment, I tried out many prompt variants, and none of them came close to playing good chess -- but maybe I just didn't try quite the right one.
(If you can find one let me know!)

---

To summarize, a core limitation of the current paradigm is that large language models will only ever capture patterns that appear in its dataset, which in this case means patterns that appear on the internet.
An absolutely enormous amount of patterns appear on the internet, so the resulting models are incredibly capable.
But that does not mean that simple scaling will resolve all issues.
We can never expect generalization to things that are not captured by the training data.

The paradigm shift required to surpass this obstacle is to re-think data collection.
The data collection process for GPT-3 is currently "passive", in that it simply inhales whatever is placed onto the internet.
This captures a ton of information, but tends to miss certain unusual edge cases, such as transcripts of high-ELO chess gameplay.
Engineers training these models will be able to mitigate these issues by expanding and improving their data-scraping procedures.
But this dataset engineering is a highly manual process; and thus, not scalable in the long run.

My prediction is that the new paradigm will be some variant of *active* learning.
This means that data acquisition will be driven by the model's knowlege (rather than agnostic to it, as is the case currently).
An active learning system will identify important contexts for which the model is uncertain, and create situations where these contexts emerge, in order to see what happens next.
It will probe all of the rare counterfactuals that give rise to complex patterns, thereby allowing such patterns to be identified.
The capabilities of such a system might truly be unbounded.

This is obviously all quite speculative, and I have no idea what actually implementing such a system would look like.
Active learning is an established subfield of ML, but not a particularly popular one, and very little progress has been made on active deep learning.
More popular (but still wildly unsolved) is deep reinforcement learning, which is closely related to active learning in that the DRL agent must explore its environment in order to identify the optimal actions.
If you want to bring about the next paradigm shift, these are the things to work on.

---

Thanks for reading, and hit me up on Twitter [@jacobmbuckman](https://twitter.com/jacobmbuckman) with any feedback or questions!

*Many thanks to Joel Einbinder for his chess gameplay, and to Joel and Mitchell Gordon for their feedback when writing this post.*

---

[^0]: Although realistically, this is a terrible way to judge capability, because [most papers are bullshit anyways](https://jacobbuckman.com/2021-05-29-please-commit-more-blatant-academic-fraud/).

[^1]: Concretely, this experiment was run on June 14th 2022 against the text-davinci-002 model, with temperature 0, top-p 1, frequency penalty 0, presence penalty 0, best-of 1. I played around with various settings, prompts, formats, etc, and confirmed that the example shown here is representative of its overall performance. To avoid the possibility of cherry-picking, Joel only played a single game against the AI, which is the one shown here. I explained to him what I was doing and gave him the instructions "play normally".

[^2]: Technically, a distribution over *tokens*. GPT-3 uses something called byte-pair encoding, which is a technique for breaking down words into reasonable sub-word chunks, enabling it to output novel words while still keeping the length of contexts (in terms of number of tokens) reasonable relative to a character-level model.

[^3]: In fact, the very act of writing this post has probably made it more likely to happen - a self-defeating prophecy.