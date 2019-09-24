---
layout: post
title: OpenAI Five Takeaways
tags: ["reinforcement learning","miscellaneous"]
mathjax: false
---

[On August 5th, OpenAI successfully defeated top human players in a Dota 2 best-of-three series](https://blog.openai.com/openai-five-benchmark-results/).
Their AI Dota agent, called OpenAI Five, was a deep neural network trained using reinforcement learning.
As a researcher studying deep reinforcement learning, as well as a long-time follower of competitive Dota 2, I found this face-off really interesting.
The eventual OAI5 victory was both impressive and well-earned - congrats to the team at OpenAI, and props to the humans for a hard-fought battle!
Of course, this result has provoked a lot of discussion; here's my thoughts.

### How did OpenAI Five win?

I'm sure this series will be analyzed by people with far deeper understanding of Dota than me, but in my opinion, OpenAI Five essentially won on the back of its teamfighting ability.
Good positioning and well-coordinated ability usage made it almost impossible to take 5v5 fights against the bot once it got started pushing.
During the laning phase, both teams were able to find pickoffs, and the human team actually pulled ahead in farm.
During the mid-game, whenever the bot team was not actively pushing, the humans were more efficient in getting resources from around the map.
Many times throughout the game, OAI5 did actions that were almost unequivocally bad, such as the pointless Smoke of Deceit usages we saw a couple of times.
But once OAI5 formed up a 5-man squad and started to push, the humans were steamrolled.

This plan was followed to a t on both of the first two games, leading to decisive OAI5 victories.
During game three, it looked like the bots wanted to try the same thing again, but after their poor hero composition led to lost fights, they began simply doing anything they could to extend the game.
It certainly seems reasonable to me to assert that OAI5 was able to discover a near-unbeatable strategy, and learned to execute it perfectly.
In my opinion, these are the two main interesting outcomes of this result.
I'd like to describe why I find them surprising, and highlight some caveats.

### Discovering an unbeatable strategy

Dota 2 has massive state and action spaces - according to [an earlier blog post](https://blog.openai.com/openai-five/), the dimensionalities of the state and action vectors are 20,000 and 1,000, respectively.
Right from the start, there is a combinatorial explosion in observed state stemming from team compositions; these quickly grow even more differentiated based on skill and item builds.
Further complicating things, the action space is a mix of discrete choices (i.e. whether to move or use a skill, what skill to use) and continuous parameters (i.e. where to move).
This results in an enormous set of states that need to be explored and remembered, and a potentially huge amount of promising actions in each one.

When I first heard about OpenAI tackling Dota 2, I assumed that exploration would be one of the major challenges.
Surely standard noise-based or epsilon-greedy approaches would fall short - in this insanely large state space, what are the chances that it will stumble upon good gameplay?

But in the absence of an explicit comment in any press release about exploration, I assume that OpenAI's exploration techniques were, in fact, totally standard.
It seems that through nothing but the reward engineering efforts of the members of the development team, OAI5 was able to get a dense enough reward signal that it discovered a near-unbeatable strategy.
This is pretty surprising so me: I'm a big believer in the end-to-end RL dream (i.e. training exclusively from the win/loss reward signal under the assumption that any human intuition we add to the training process will "dilute" the purity of the solution discovered with our pesky suboptimalities).
My thinking was that in any real-world problem, effective reward engineering would be so difficult as to be impossible.
[There are many examples of reward-engineering-gone-wrong in various domains](https://www.youtube.com/watch?v=tlOIHko8ySg).

Those in favor of reward engineering argue that it's possible to avoid these issues with careful engineering.
It's true that an AI trained in an environment that rewards last-hitting is unlikely to ever learn a revolutionary new strategy that ignores last-hits entirely.
But the chance that such a strategy exists seems quite low, and it's clearly possible to learn a strategy that *both* secures last-hits and wins games.
So, why not do it? These "reward breadcrumbs" will guide us towards certain areas of the solution space and away from others.
But as long as we are careful to ensure that the getting the engineered reward is at least compatible with overall success on the task, it may be an indispensible part of solving real-world RL problems.

Dota 2 is the first example I've seen of this in practice; a challenging real-world (ish) task with a seemingly impossible exploration issue, that was overcome by clever reward engineering.
Maybe it's true that another agent, trained in the exact same way but with just the win/loss reward, could eventually learn a better strategy than OpenAI Five.
But until someone manages to make one, I don't see much reason to believe that.
And it seems likely that even if such a system existed, it would almost certainly take a lot longer to train.
So seeing this result has begun to win me over in favor of reward engineering on real-world tasks.

#### Caveats

Of course, this would likely have still been inadequate without scale.
In the millions upon millions of games played by the system, even naive exploration is able to cover an enormous amount of possible game-states.
And as massive as the current state and action space are, they are tiny compared to the eventual number of states once the remainder of the features are added.
The remaining ~100 heros will increase the state space exponentially, and adding in the ability to control multiple units (via illusions, summons, etc.) will increase the action space exponentially as well: in addition to choosing an action, the agent must choose between the $2^n$ potential subsets of controllable units at its disposal.
It remains to be seen whether OpenAI's current exploration strategies will be able to keep up.

Additionally, the very existence of an "unbeatable strategy" undermines some of the key reasons that Dota 2 was selected as an interesting platform for research.
For example, people often cite strategic decision making, long-term strategy, and complex opponent modeling and counter-play as fundamental to successful Dota.
But if an unbeatable strategy exists, that goes out the window.
Simply executing on a known strategy doesn't require any higher-level reasoning or planning, and certainly doesn't require much opponent modeling.
Framed in this way, I see these Dota victories as being in the same category as [learning to walk in a complex, noisy environment](https://deepmind.com/blog/producing-flexible-behaviours-simulated-environments/).
"Just do your thing, Dota bot, and do your best to correct for whatever those silly human opponents throw at you."

It's entirely possible that OAI5 *would* learn these higher-level behaviors, if trained to play a more balanced game.
Dota 2 is balanced around all 115 heroes and all items, but the version played by OAI5 uses a pool of only 18, and so any concept of balance goes out the window.
As Blitz said during the post-game panel discussion: the limited set of available heroes forced the human players to "play the bot's game."
Heroes with strong counter-push and teamfight like Venomancer, Enigma, and Naga Siren would have directly countered the strategy played by OAI5, and "backdoor" heroes like Furion and Lycan would have allowed the humans to play around the bots and gain advantage in many lanes at once.
Once these heroes are added to the pool, perhaps we will see a totally different set of strategies.

(Also, Icefrog does his best, but there is no guarantee that even the full game of Dota 2 is balanced!
The game is constantly being tweaked to make more and more strategies viable.
Alliance's nearly-undefeated run at TI3 on the back of a pushing strategy - somewhat similar to OAI5's, in fact - led to a swift nerf of the heroes and items responsible.
And of course, who can forget the "Ho Ho Ha Ha" patch of 6.83, where picking Sniper or Troll Warlord would basically guarantee your team a victory.
So if a future OAI5, trained on the full game, is able to come up with a single, dominant strategy, expect that strategy to be patched into uselessness soon afterwards.)

### Executing perfectly against an out-of-domain opponent

In spite of some good-natured ribbing from the casters, I thought that OAI5 did astonishingly well in dealing with situations that is was not exposed to in training.
The concept of "pulling creeps" was not something that it had ever learned to do, and therefore also not something that it had learned to deal with.
But the bot handled the sudden lack of creep wave more-or-less as a surprised human would.
In the second game of the series, it was even able to capitalize on a pull that it had vision of and pick off a hero.

#### Caveats

Since this was only a three-game series, and the humans played mostly classic non-cheesy Dota 2, it's hard to get a sense of just how stable the AI is when encountering unfamiliar situations.
But from the few games we've seen, I think it looks much less exploitable than its 1v1 counterpart.
The flipside of having to explore such a vast state space is that it seemingly becomes a lot harder to force the bot into a state that is *truly* unexpected.
Even if some minor things are "off", there are enough familiar elements that OAI5 is able to stick to its plan.
Whether this is a product of domain randomization and self-play, or simply a reflection of the increased importance of static objectives like towers in 5v5, I'm not certain.
(Or whether it is even a real effect - if OpenAI sets up a public free-for-all like they did last year, it might prove fragile after all!)

### On cooperation

The teamfight coordination displayed by OpenAI is absolutely incredible by human standards.
In humans, this level of teamfight requires months of practice and an intense focus on cooperation; it is reserved for the highest-level professional teams.
And yet, I don't think that the various heroes controlled by the bot displayed anything resembling human cooperation.
When we say that two agents to are "cooperating", I think an essential part of that definition involves reasoning under uncertainty.

In humans playing Dota 2, I see two major sources of uncertainty: policy uncertainty and information uncertainty.

To illustrate what I mean by policy uncertainty, consider what it would be like to be placed on a team with a group of random Dota players.
You don't know exactly who the other players are, what they will do, how they will react.
At first, you must behave cautiously; you have some assumptions about what they will do, but you need to make sure you always have a backup plan in case they deviate.
As you play with them more, and get to know them better, you get a better sense of their actions, and they of yours.
Eventually, you can very reliably predict their actions, and trust them to have your back when needed.
But at the end of the day, there's always still some uncertainty there.

Information uncertainty arises when two players have a different subset of the information on the screen visible to them at any given time.
Though all human players can scroll their screen around to see everything visible to all team members, in practice, there is too much going on at any given time for a single player to absorb it all.
Therefore, even at the same moment of the same game, different players are likely to have taken different subsets of the available information as input.
Since it's impossible to know exactly what each of your teammates was looking at, and they might take various actions depending on what they saw, this is a second major source of uncertainty.

OAI5 is, by design, able to skirt these issues.
The network controlling each hero can take in the full state of the map at every tick, meaning that all heroes have access to identical information.
And since all of the millions of games played have had the same "player" on each hero, there is essentially no policy uncertainty - each hero can perfectly predict the actions of each other.
With neither policy nor information differences, OAI5 is able to display "perfect cooperation", essentially controlling all five heroes as though they were a single entity.

This is excellent for Dota bots, but I think it's disingenuous to use the word "cooperation" to describe it, because it doesn't generalize well to other settings where cooperation is important.
For one thing, I'd wager that OAI5 would be extremely crippled if any one of its heroes were replaced by a human player, of *any* skill level.
Even if the 5th player is a top pro, playing excellently, he or she would still be playing *differently* than expected, and the bot would be unable to cooperate as a result.
(I'd love to see OpenAI try this and let me know what the result is, though!)

I think that this "perfect cooperation" is the Dota equivalent of "aimbotting" in FPS games - there's a fundamental assumption about the limitations of human beings built into the game, and all top humans reach this physical limit, which means they are forced to compete with one another by using high-level reasioning and strategy.
By sidestepping that limitation, a bot is able to easily win without any of the interesting stuff.
I would be much more convinced that the bots are using high-level strategy and long-term planning if they were handicapped in a way that brought them back down to the level of humans in this regard.

To incorporate policy uncertainty, I'd like to see OpenAI train an ensemble of many OAI5 agents.
In any given 5v5 game, 10 agents would be randomly sampled and assigned to the ten heroes; each agent only learns from games that it participates in.
This would force the agents to have some uncertainty about how their teammates will behave, since they get different teammates on different games.
And since the ensemble is just a bunch of copies of the agent that they've already made, it should be somewhat straightforward for OpenAI to set up.
(Of course, the implementation difficulty depends a bit on the architecture OpenAI used; if there is a lot of parameter sharing between agents, this will be hard.)

Incorporating information uncertainty is less of an issue, in my opinion; the bot's ability to take in all available information on the map seems like more of a "fair" advantage.
It could maybe be incorporated by randomly masking out certain segments of the input at every frame, perhaps dropping out inputs further from the agents at a higher rate.

### Conclusion

Well, that ended up being a bit more of a brain dump than I intended.
In summary, I think that this is a super impressive accomplishment, and says a lot about how good policy search, domain randomization, and reward shaping are at finding solutions.
However, I'm hesitant to draw any conclusions about whether the solution found involves much higher-level reasoning or long-term planning.
Thanks for reading!
