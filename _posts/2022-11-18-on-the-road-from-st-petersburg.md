---
layout: post
title: On The Road From St. Petersburg
tags: ["statistics", "probability", "theory", "paradox"]
published: true
mathjax: true
---

Let me tell you a story.

When I was a young man, I lived for a time as an itinerant gambler, wandering the Russian countryside to engage my fellows in games of chance.
Although I was known to gamble on cards, dice, and animals, my favorite game was played with nothing more than a simple coin.
The rules of my game were as follows:

You may place a wager of any whole number, e.g. 5₽.
I will flip a perfectly-fair coin, and if it comes up heads, I will pay you the value of the wager, plus an extra 20%.
If the coin comes up tails, I will keep the money you wagered.
Afterwards, you have the option to place a new wager and play again.
You may continue to play until the sun rises above the horizon.

One fine summer afternoon, I set up my booth in the city of St. Petersburg, a legendary metropolis populated entirely by perfectly rational expected-value maximizers.
A man named Evan wandered over with 100₽ in his pocket.
Upon reading the rules, Evan performed the following calculation.

“For every ruble wagered, there is a 50% chance of winning 1.10₽, and a 50% chance of losing 1₽.
In expectation, this will net 0.10₽ per ruble wagered.
The expected value improves with each ruble, so the more rubles wagered, the better.
So, I wager all 100₽.”

I flipped my coin and…heads!
Now, Evan had 220₽.
Reading once more the rules of the game, he said,

“Well, once again, for every ruble wagered, I expect to win 0.10₽.
This situation is just the same as it was a moment ago, except I have more money available to gamble with.
I bet 220₽.”

Heads again!

“I bet 484₽.”

Another heads!

“1064₽.”

And another heads!

“3405₽.”

…and, at last, a tails.
Evan walked away with 0₽ in his pocket, but with his head held high.

“I just made a fortune in expected rubles.”

Evelyn greeted me next.
She made 1,000₽, then lost it all…including the 500₽ she started with.
Everett was less lucky; his first flip was a tails, and I grew 10,000₽ wealthier.
But saddest of all was poor Everly, who began her game with a handful of coins, amassed a fortune of billions of rubles, and then lost it all in an instant.

Nobody ever walked away from my game, or wagered even a single coin less than the sum total of their personal wealth.
After all, the dictums of EV maximization held that to do so would be irrational.
And so, with each participant, I flipped my coin until they lost, and pocketed their initial wager.
As night fell, I carefully packed away my earnings and slipped out of town, before the mobs of newly destitute could locate the source of their newfound destitution.

But on the road out of St. Petersburg, I encountered a boy dressed in rags.
He recognized me by my garb as a gambling man, and requested that I allow him to tempt his fortune.
Though my pockets were full from the day’s haul, for love of the game, I acquiesced.
After reading my rules, the boy spoke.

“I will wager 10₽.”

I dutifully flipped my coin, observed the heads, and paid him his rightfully-earned 12₽.

“I will play again. 10₽.”

Had I misheard?
No – the boy extended his hand, a ten-ruble coin resting in his palm.
Very well, I thought to myself, flipping my coin.
This time, the coin turned tails, and I pocketed his 10₽.

“Once more, again for 10₽.”

Lady luck smiled upon me, and the boy parted with his 10₽.
As I pocketed the coin, I turned to go.

“10₽.”

I glanced up sharply.
He had lost his initial bankroll, yet continued to play?
Had the boy been holding money in reserve?
Squinting at his gaunt physique, I realized that what I had taken for an unsightly tumor on his leftward side was in reality a satchel strapped beneath his rags, filled to the brim with ten-ruble coins.
For the first time since arriving in St. Petersburg, I spoke.

“What is your name, boy?”

“Tenjamin.”

For the rest of the night we gambled.
Sometimes he won, sometimes he lost, always the boy wagered but a single 10₽ coin.
By the time the sun rose to free me from the game, he had taken everything I won in the city, and much more besides.
To this day, I am still paying off the debt I accrued on the road from St. Petersburg.

---

## Expected Value

Should one always choose the action with the highest expected value?

Many people believe so.
It’s a beautiful idea: incredibly powerful, and yet elegant in its simplicity.
For many intellectually-minded folk, there’s something wonderfully compelling about a guideline that applies near-universally.
Any decision-making scenario becomes reducible to a mathematical exercise.
Simply map each outcome to a scalar measure of value, estimate the probabilities, marginalize, and ride forth — confident that you have chosen the best option that your current knowledge allows.

As a rational-minded person myself, I see the appeal of this perspective.
Expected value maximization is incredibly helpful at synthesizing disorganized information in an uncertain world into a unified picture with a clear set of preferences.

But in this essay, I want to probe the validity of this approach.
Maximizing expected value can prescribe actions that seem wildly unintuitive.
Why is there this huge difference between the actions suggested by our intuitions and by our mathematics?
And when we encounter a situation where their recommendations conflict, which one should we listen to?
There are many brilliant people, especially in engineering and finance, who will answer this question in no uncertain terms.

“The higher-EV play is the correct one. Your irrational fears are holding you back.”

But I am not so sure.

This essay began as my attempt to restore my trust in expected value as a decision-making philosophy.
In the end, I instead found myself abandoning expected value entirely in favor of a different approach, one that is just as elegant and powerful as expectation maximization, but better behaved and more philosophically grounded.
But – I’m getting ahead of myself.
First, let’s take a moment to properly motivate what exactly we are searching for.

---

Maximizing expected value is **not rational**.

Now, this is not to say that it is *irrational*, necessarily.
There are many situations in which the rational thing to do is to take the action with the highest expected value.
My point here is only that “EV-max action” and “rational action” are not synonymous.
The most rational action to take is the one that leads to the best outcome.
The EV-max action is the result of a particular mathematical computation.
It is absolutely *possible* that these two objects are isomorphic: that the EV-max action is always also the most rational.
But this is certainly not obvious a priori, and needs to be carefully justified.

I find that this point is often hard for people to accept.[^0]
For someone who has spent their whole life deeply embedded in the EV-max framework, it can be confusing at first to understand how a notion of optimality distinct from expected value could even *exist*.
Like the fish in the David Foster Wallace essay who asks: “What the hell is water?”
Unless you've breathed air, you’d never know you’re swimming in it.

---

## The St. Petersburg Paradox

The [St. Petersburg paradox ](https://en.wikipedia.org/wiki/St._Petersburg_paradox) is a well-known statistical conundrum, one that is closely connected to the plight of its fictional citizens in my story.
The paradox concerns a particular gamble, which I'll call the *doubling game*.

Here are the rules.
The game begins with $2 in the pot.
The player repeatedly flips a fair coin.
Each time it lands heads, the amount of money in the pot doubles.
The first time it lands tails, the player is given the money in the pot, and the game ends.

What is the most that a rational gambler should be willing to pay to play this game?
Clearly, the answer is at least $2, because that's the minimum payout.
But we will sometimes see a long sequence of heads, and the payout will be much higher, so perhaps we should be willing to pay more.

According to the expected-value framework, the amount that a gambler should be willing to pay is equal to the expected value of the game.
We can compute this easily, by partitioning the outcomes based on the number of flips. 
There is a $$\frac{1}{2}$$ chance of seeing exactly one flip (if the first flip is tails), a $$\frac{1}{4}$$ chance of seeing exactly two flips (heads, then tails), a $$\frac{1}{8}$$ chance of seeing exactly three flips...the pattern is clear, the chance of seeing $$n$$ flips is $$\frac{1}{2^{n}}$$.
And what are the values of these outcomes?
$$2,4,8,16,...$$so $$n$$ flips nets $$2^{n}$$ dollars.
Marginalizing, we see that the expected value is $$\sum_{n=1}^{\infty} 2^{n}\left(\frac{1}{2^{n}}\right) = \sum_{n=1}^{\infty} 1 = \infty$$.
Hmm.

Now, "infinity" is not really a number, so one must generally be a bit careful reasoning about results which include infinities.
In this instance, the conclusion can be straightforwardly understood as "the expectation is larger than any finite number".
So the answer to our question is: a rational gambler will be willing to pay any finite amount of dollars to play this game.

Of course, paying \\$1,000,000,000 to pay this game seems like quite a stupid thing to do.
Hence: paradox.

---

To be honest, I don't think "paradox" is quite the right word here.
There's no *fundamental* inconsistency at play.
This is just an example of a situation where the expected-value framework is ineffective.
Choosing to play the doubling game with a buy-in of \\$1,000,000,000 *really does* have positive expected value, and *also* loses you money.
There's nothing paradoxical about the fact that some decision-making frameworks are bad, sometimes.
It only *feels* like a paradox to those fish who have never noticed the water.

Many people have proposed resolutions to this paradox, most prominently utility theory[^1]
and default risk.[^2]
But I find these to be very unsatisfying.
They merely assume away the existence of situations that would be problematic, without addressing the fundamental issue.
A real resolution requires the introduction of a new decision-making framework.

---

## Maximize The Realizable Value

Here is my proposal: *take the action that maximizes the **realizable value***.

The realizable value[^4] of a bet is the amount of money that you are guaranteed to end up winning if you play enough times.
It is an outcome whose probability gets more and more likely the more rounds you play.
It is defined using a well-understood concept from probability theory known as [convergence in probability](https://en.wikipedia.org/wiki/Convergence_of_random_variables#Convergence_in_probability).
Concretely, if the outcome of a bet converges in probability to some number X, then that bet is said to have a “realizable value of X”.

If you’ve never studied probability theory, you might be a bit confused by how this definition is different from expected value; intuitively, it feels like it might just be a different way of expressing the same concept.
Indeed, the difference between the two is subtle.
In fact, for all bets with *finite* expected value, the [weak law of large numbers](https://en.wikipedia.org/wiki/Law_of_large_numbers#Weak_law) tells us that these two concepts *are* exactly the same: the outcome will converge in probability to its expected value.
This means that the realizable value of any bet with finite expected value is its expected value!
Thus, all of your intuitions from expected-value maximization carry over to realizable-value maximization.

But when a bet has *infinite* expected value, as occurs in the St. Petersburg paradox, the two frameworks typically come to different conclusions about what actions to take.
As we’ve discussed, expected-value maximization concludes that one should play at any price.
But realizable-value maximization gives an actual reasonable answer, explaining precisely how many dollars one should be willing to pay for the opportunity to play a certain number of times.

Personally, I find this to be quite compelling evidence in favor of this approach.[^3]
This new principle matches up perfectly with EV in all the situations we know that EV feels correct, and gives a new answer in precisely those situations where EV does something weird.
But it’s not as though I carved out specific exceptions: this approach is unified and very natural, but just happens to do exactly what we would want.
Isn’t that elegant?

Let’s walk through some examples of realizable value in action.
In each scenario, we are invited to play a particular game for $$n$$ rounds, and ask: what is a fair price-per-round to pay?
$$X_i$$ denotes the random variable that refers to the outcome of the $$i$$th round, so
our total payout for $$n$$ plays is $$\sum_{i=1}^{n} X_i$$.

### Basic coin flip.

In the first game, the player flips a fair coin which pays out \\$10 for heads and \\$0 for tails.
The expected value of any given round $$\mathbb{E}[X_i] = 0.5(10) + 0.5(0) = 5$$ for all $i$.
Since this is finite, the weak law of large numbers tells us that $$\frac{1}{n} \sum_{i=1}^{n} X_i \overset{p}{\to} \mathbb{E}[X_i]$$ as $$n \to \infty$$.
We can rearrange to get $$\sum_{i=1}^{n} X_i \overset{P}{\to} n\mathbb{E}[X_i] = 5n$$.
As a realizable-value maximizer, I should be willing to pay $5 per round of play.

As expected, this coincides with the solution given by expected value.

### Doubling game.

The player flips a fair coin until it comes up tails.
If the first flip is a tails, the payout is $2, and for each heads seen, the payout doubles.
As we saw above, $$\mathbb{E}[X_i] = \sum_{n=1}^{\infty} 2^{n}\left(\frac{1}{2^{n}}\right) = \sum_{n=1}^{\infty} 1 = \infty$$.
But as it turns out, $$\sum_{i=1}^{n} X_i \overset{p}{\to} n \log_2 n$$.
The math here is a bit more involved, so I’ll just give the high-level intuition of the analysis.
If you are comfortable with probability theory, [a rigorous proof is given by Dunnet in his textbook (Example 2.2.16)](https://services.math.duke.edu/~rtd/PTE/PTE5_011119.pdf#page=73), or more clearly [here](https://people.math.wisc.edu/~roch/grad-prob/gradprob-notes4.pdf#page62).

The key tool is our ability to *truncate* a random variable, meaning clip its value to 0 if it falls outside of a certain range.
Truncation is helpful for this sort of problem because, once we have truncated, the expectation is guaranteed to be nice and bounded.
Denote the truncation of a random variable $$X$$ to the level $$b$$ as $$T(X, b) = X \cdot \mathbb{1}_{|X|<b}$$ (where $$\mathbb{1}$$ denotes the indicator function that is equal to 1 if its condition is true, otherwise 0).

What’s cool about truncation is that truncating a random variable does nothing if the value of that variable turns out to be less than the truncation threshold.
By gradually increasing the truncation threshold, we can make it less and less likely that truncations have any effect at all.
Therefore, we can understand our sequence of $$X_i$$s as the *limit* of a sequence of sequence-of-truncated-$$X_i$$s, where the truncation levels get less and less strict.
As the truncation threshold grows, we end up with almost no probability that any variable actually gets impacted.

Concretely, define a sequence of truncation levels $$b_j = j \log_2 j$$.
For each level $$b_j$$, we truncate the first $j$ terms of our sequence of $$X_i$$.
A bit of algebra leads to the conclusion that $$\sum_{i=1}^j \mathbb{P}(X_i \neq T(X_i, b_j)) \to 0$$ as $$j \to \infty$$, meaning that we eventually see that there is almost no chance that any variable will get truncated.

Next, we just need to analyze the truncated sequence.
We know that the expectation and variance for truncated variables exist, and for any particular sum of $$j$$ variables truncated at level $$b_j$$, some more algebra tells us that the expectation $$\mathbf{E}[\sum_{i=1}^j T(X_i, b_j)] = j (\log_2 j + \log_2 \log_2 j)$$, which we can denote as $$\mu_j$$.
After checking some conditions, can use [Chebyshev’s inequality](https://en.wikipedia.org/wiki/Chebyshev%27s_inequality) to bound the probability that the actual sum deviates from this mean by a factor of more than $$b_j$$, leading to the conclusion that $$\frac{|\mu_j - \sum_{i=1}^j T(X_i, b_j)|}{b_j}) \overset{P}\to 0$$ as $$j \to \infty$$.

Since both (1) the truncated sequences converge in probability to the real sequence, and (2) the deviations of the sum of the real sequence converge in probability to 0, we can conclude that the deviations of the sum of the *real* sequence converge in probability to 0.
Thus, for a real sequence of length $$n$$, we have $$\frac{|\mu_n - \sum_{i=1}^n X_i|}{b_n} \overset{P}\to 0$$ as $$n \to \infty$$.
Plugging in $$\mu_n = n (\log_2 n + \log_2 \log_2 n)$$ and $$b_n = n \log_2 n$$ and doing a bit more algebra gives the final result: $$\sum_{i=1}^n X_i \overset{P}\to n \log_2 n$$.

Whew.
Let’s marinate for a moment on the implications of this result.
It seems that in the doubling game, the realizable value *per round* grows with the number of rounds being played.
If you’re only playing 1000 rounds of the game, the amount that you are willing to spend per round is $$1000 \log_2 1000 \approx 10000$$, so you value each round at \\$10.
But if you are playing 100,000 rounds, then suddenly you value each round at $20!
It’s as though this game has an inherent economy of scale.
The more times you play, the more valuable each play becomes.

To me, this is a completely satisfying resolution to the St. Petersburg paradox.
We didn’t alter the situation at all, just directly tackled the problem as it was initially presented.
We used a generic, first-principles approach, not anything problem-specific, and with no free parameters.
We ended up with a concrete answer, assigning a specific numerical value.
And the answer elegantly synthesizes our two intuitions – that on one hand, the game has the potential to be extremely valuable, but on the other hand, a single play is not worth much.

Just to confirm, I ran a simulation ([code here](/static/files/petersburg/stpetersburg.py)) of two billion doubling games, computing the mean reward per game over time:

![](/static/img/petersburg/doubling.png){:width="700px"}

A bit noisy, but overall pretty convincing.

### Consecutive wagers.

The player has a bankroll of $$b$$ dollars, and wagers $$z$$ dollars. 
The player flip a coin, which comes up heads with probability $$p$$.
If heads, the wager is multiplied by some factor $$1+w$$ for $$w > 0$$.
If tails, the wager is reduced by some factor $$1 - l$$, where $$0 < l \leq 1$$.

The expected value of each round of this game is $$pzw - (1-p)zl = z(pw - (1-p)l)$$.
So, as long as $$pw > (1-p)l$$, each round has an expected value which is linear in the bet size, and the expected value is maximized by betting everything.

What value is realized by that strategy?
Let $$H_n$$ be the number of heads seen after $$n$$ rounds, and so $$n - H_n$$ gives the number of tails.
This means that the bankroll $$b_n = b_0(1+w)^{H_n}(1-l)^{n-H_n}$$ at timestep $$n$$, where $$b_0$$ gives the initial bankroll.
Since $$\mathbb{E}[H_n] = np$$, the law of large numbers tells us that $$|H_n - np| \overset{P}\to 0$$ as $$n \to \infty$$.
Thus, for the bankroll $$b_n$$,

$$b_n = b_0(1+w)^{H_n}(1-l)^{n-H_n} \overset{P}\to b_0(1+w)^{np}(1-l)^{n(1-p)} = b_0\left((1+w)^{p}(1-l)^{(1-p)}\right)^{n}$$

as $$n \to \infty$$.
And so we see, if $$(1+w)^{p}(1-l)^{(1-p)} < 1$$, then $$b_i \overset{P}\to 0$$.

In summary, EV says to take the bet if $$\frac{pw}{(1-p)l} > 1$$, and RV says to take the bet if $$(1+w)^{p}(1-l)^{(1-p)} > 1$$.
Unfortunately, these two conditions do not always agree.
For example, when $$p = .5, w = .6, l = .5$$, we see $$\frac{pw}{(1-p)l} = 1.2 > 1$$, while $$(1+w)^{p}(1-l)^{(1-p)} \approx .89 < 1$$.

This result explains trouble for the citizens of St. Petersburg in the story at the beginning of this essay, who were offered a bet with $$p = .5, w = 1.2, l = 1$$.
$$\frac{pw}{(1-p)l} = 1.2 > 1$$, so they took the bet, but $$(1+w)^{p}(1-l)^{(1-p)} = 0$$, so their realized outcome was $0.
They would not have lost their money had they had aimed to maximize their realizable value instead of their expected value.
(To strengthen your intuition, it's worth thinking about how it is possible for the distribution of outcomes to have both infinite expected value, and zero realizable value.
What must the distribution look like?)

Tenmothy, of course, wagered in such a way as to play the “basic coin flip” game instead, so he was able to realize earnings of $$1.2n$$, meaning his realized wealth grew linearly as long as the game continued.
That’s a big improvement already.
But could he have done even better?

In fact, this analysis reveals a straightforward way to identify an optimal betting strategy, one which maximizes value realized per round.
If the bet in each round were $$z_n = f b_n$$ for some fraction $$0 \leq f \leq 1$$, such that the payoff for winning decreases to $$fw$$ and the penalty for losing decreases to $$fl$$, we see $$b_n \overset{P}\to b_0\left((1+fw)^{p}(1-fl)^{(1-p)}\right)^{n}$$ as $$n \to \infty$$.
All we need to do is choose the $$f$$ which maximizes this value, which can be done by setting its derivative equal to zero, and solving the resulting equation.
The solution, $$f^* = \frac{p}{l} - \frac{1-p}{w}$$, is the formula for the famous [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion).

---

## Connections

Another sign of a good framework is if it explains the world well.
One would expect a good decision-making rule to pop up in all sorts of places, being used implicitly, even before being formally understood.
I want to highlight a few places where I’ve noticed that reality coincides with the dictums of realizable-value maximization.

### Gambling

We’ve just discussed how the Kelly Criterion can be derived through the lens of maximizing realizable value.
Interestingly, as far as I can tell, the original motivation was nothing of the sort.
The Kelly Criterion was initially derived for an ad-hoc objective: maximizing the expected logarithm of wealth.
Later, it was shown to also be equivalent to maximizing the geometric rate of return.

These are perfectly valid goals, but they fall short as complete decision-making frameworks, since they don’t provide any characterization of when they should be invoked (why maximize expected wealth sometimes, and expected log-wealth other times?) and are limited in their scope (the Kelly criterion does not explain how much to pay to play the doubling game). 

I’ve always found the Kelly Criterion to be a beautiful strategy, but I was never quite at ease with its ad-hoc-ness.
I think it’s amazing that the framework of realizable-value maximization serves to motivate it from first principles.
Also, it’s a widely-used approach, vouched for by professional investors and gamblers alike; the fact that it coincides with the optimal realized value is a strong point in favor of the practical usefulness of this framework.

### Psychology

It’s conventional wisdom in economics that humans have logarithmic utility functions.
[Empirical experiments seem to generally corroborate this, although it is possible a different functional form may be a somewhat better fit](https://www.jstor.org/stable/1422419).
This is, for example, the motivation given by Kelly to maximize log-wealth in the first place.
Economists simply accept logarithmic utility as a premise, and build from there.

With realizable-value maximization in mind, this perspective reverses.
We can now answer the question: *why* do humans have logarithmic utility at all?
Here’s my thinking.

It’s a reasonable assumption that wealth is generally helpful for survival, especially when we broaden the definition of wealth beyond just fiat currency: power, status, prestige, possessions, etc.
This implies that evolutionary pressures should have instilled in us good instincts for accumulating wealth over the course of our lives.
Obviously, genetics are not fine-grained enough to instill theoretical knowledge of realizable-value maximization.
But what it *can* do is give us instincts that, when followed, allow us to *implement* a RV-maximization algorithm.
Which, of course, explains why we have logarithmic utility.

It may be coarse, but overall, I think it’s pretty reasonable to model life as a big, long-horizon repeated betting game, all played against the same bankroll.
We know that logarithmic utility maximization is identical to following a Kelly strategy in the specific setting in which that strategy is applicable, and it is very likely that it has connections to RV-max in general.
So by living according to logarithmic utility, we are able to realize the most wealth over our lifetimes, and survive and reproduce.

### Venture Capital

The real-world asset class that is most similar in structure to the doubling game is probably early-stage startups.
Something like 90% of startups fail, and become worthless.
Some small number manage to break even for their investors.
But a tiny fraction of them double, and double, and double again in value, producing enormous, outsized returns.

If we assume that investing in a startup really is akin to playing the doubling game, and that VC firms are doing a good job acting in their own self-interest, the framework of realizable-value maximization makes some predictions.
We discussed earlier how the game has an inherent “economy of scale”: the more rounds we play, the more valuable each one becomes.
For a VC, playing more rounds means investing in more companies.
This means that we would expect to see VC firms whose strategy relies mostly on capturing unicorns spending a ton of money on a lot of different companies – and, conversely, that the most well-funded VCs are more likely to center their strategy around capturing unicorns.
This is because their capital gives them a competitive edge in entering those sorts of rounds.
An organization with enough capital to leverage the implicit economy of scale by buying stakes in many companies is willing to put more money into each company than their rivals, outbidding them.

If we look at the field of current VCs, this pattern is precisely what we see.
The largest, most well-funded organizations, like SoftBank and Tiger Capital, are the ones whose strategies are most reliant on capturing unicorns.
These firms put money into thousands of startups each year in the hopes of getting one or two massive successes, like WeWork or Uber.
In contrast, smaller firms are more likely to invest in founders with a smaller, more concrete goal, and a good balance sheet.

(Now, this is not to say that realizable-value theory is the *only* way to explain this.
I’m sure VCs have perfectly reasonable justifications.
I’m just pointing out that it is cool that using these ideas as first principles can also explain it, in spite of the theory not being intentionally constructed to do so.)

---

## Conclusion

Hopefully, those of you who are still with me are on board with the idea that we should be maximizing realizable value instead of expected value.
And for those that aren’t – I am excited to hear your counter-arguments.

That being said, I would be surprised if realizable-value maximization is the end of the story when it comes to decision-making frameworks.
Most likely, it has its own subtle issues, and given enough time, a paradox will rear its ugly head once more.
When that happens, I will be right there alongside everyone else striving to find an even better decision-making framework.
The road from St. Petersburg is long, but the journey is only beginning.

---

Thanks for reading, and hit me up on Twitter [@jacobmbuckman](https://twitter.com/jacobmbuckman) with any feedback or questions!

*Many thanks to David Buckman, [Warfa Jibril](https://twitter.com/warfajibril), [Joel Einbinder](https://twitter.com/joeleinbinder), and [Carles Gelada](https://twitter.com/carlesgelada) for their ideas and feedback.*

---

[^0]: If you are finding this hard to accept, one thing that might be helpful in understanding my position is to consider how you would argue in favor of expected-value maximization to someone with a *worse* philosophy.

[^1]: The most widely-known resolution is actually described in [the paper that originally introduced the paradox](https://www.jstor.org/stable/1909829). This resolution introduces the idea of *utility functions*. The motivation behind utility theory is that the goal of a gambler is not to maximize the amount of dollars he earns; it's to maximize his quality of life. For example, the \\$1,000,000th dollar you earn is probably less useful to you than the \\$100th dollar. Mathematically, it is simply a nonlinear monotonic transformation that maps from the amount of dollars you have in your bank account to the amount of “utility” those dollars bring you. <br><br>How does this idea resolve the St. Petersburg paradox? Any concave utility function, such as log or root, ensures that payoff for getting a large numbers of heads grows more slowly than the probabilities drop, so the expected value of the payoff becomes bounded. For example, using square-root utility, the sum becomes $$\sum_{n=1}^{\infty} \sqrt{2^{n}}\left(\frac{1}{2^{n}}\right) \approx 2.41$$. <br><br>As a decision-making framework, I found this quite unsatisfying for two reasons. Firstly, it is much less elegant than expected-value maximization, because of the introduction of a free parameter: the choice of utility function.  Out of the infinitude of monotonic functions, which one should I select?  The choice is ultimately arbitrary, and I don’t like the idea of my universal decision-making framework relying on this sort of arbitrary decision. <br><br>Secondly, many choices of utility function do not even fully resolve the paradox. Any invertible utility function can be "canceled out" with a corresponding change to the rewards. For example, if I am using square-root utility, my expected value on the classic doubling game is bounded, as we just saw. But what if I am given the opportunity to pay \\$1,000,000,000 to play a variant of the doubling game where the payout for $$n$$ heads is $$(2^{n})^2$$ dollars? The expected value becomes $$\sum_{n=1}^{\infty} \sqrt((2^{n})^2)\left(\frac{1}{2^{n}}\right) = \sum_{n=1}^{\infty} 1 = \infty$$, and I am right back where I started: willing to pay any finite amount of money for this chance at infinite utility. This is fixable by mandating bounded utility, but that seems silly.

[^2]: This resolution argues that expectation is not *truly* infinite, because the counterparty can default on their payout. In other words, if I ever managed to hit a miraculous streak of heads that nets me \\$1,000,000,000,000, I may still earn only \\$1,000,000 if that's all the money that my counterparty has available. With this assumption (which is in fact identical mathematically to upper-bounded utility), the expectation value becomes bounded once again. <br><br>Unfortunately, this is not a resolution at all. The reason is that a sufficiently-large finite bankroll has all the same flaws as the infinite one. For any given entry fee (for example, \\$1,000,000) we can always construct a scenario where a counterparty has a sufficiently-large bankroll (in this case, $$2^{1000001}$$) for the game to have positive expected value. Thus, even when the bankroll of the counterparty is required to be finite, we can still find situations where expected-value maximization will choose to play the doubling game at arbitrarily-high entrance fees.

[^3]: It's challenging to argue that one decision-making framework is superior to another, because it's a fundamentally philosophical issue. *Within* the context of a specific framework, it's straightforward to identify which *choices* are superior. Indeed, that's the whole purpose of a framework, which is at its core nothing more than a way of inducing a ranking over choices. <br><br>But comparing *between* frameworks is an entirely different ballgame. There's no external, objective metric that will tell us which is the best. We're forced to invoke subjective arguments: about which frameworks make the most sense, seem like they work well, or just "feel right". For people who consider themselves objective, rational decision-makers, this can be an uncomfortable realization. Even if choices are rational *within* the context of their preferred framework, they are ultimately reliant on the subjective decision to utilize that framework at all. <br><br>Now, don't confuse my point with some postmodern "everything is the same, all approaches are valid" nonsense. Some frameworks really are better than others. But we need to accept the fact that we will not be able to show which framework is preferrable with any purely numerical proof. The argument will have some subjective elements, as science and philosophy often do. In this case, the argument I’m making in favor of this approach relies on elegance, universality, naturalness, and alignment with intuitions.

[^4]: If you haven’t heard this term before, it’s because I made it up.  I want to be clear about something: my approach is closely related to many extremely well-studied problems in probability theory, and I’m not claiming that any of the ideas I discuss here are really novel. For example, all of the proofs that I include already appear in textbooks. But I haven't seen anybody set things up from quite this same angle, and this choice of resolution is not mainstream (e.g., it isn't explained on Wikipedia). There doesn't seem to already be a widely-used word for what I am describing, so academic norms be damned, I reserve the right to coin my own terminology for use on my personal blog.