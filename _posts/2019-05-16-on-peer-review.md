---
layout: post
title: On Peer Review
tags: ["academia","peer review","miscellaneous"]
mathjax: false
---

In light of the [recent discussions](https://twitter.com/nlpmattg/status/1128319419376066560) on the *ACL reviewing process on Twitter, I want to share some thoughts.

### Do We Need Peer Review?
Specifically, do we need double-blind peer review of the sort that conferences provide?

I’m in full agreement with Ryan that it is an essential service for the scientific community. As scientists, our job is to develop and capture knowledge. Peer review ensures that the work of the least-advantaged members of our community is judged by the same standards as the most-advantaged members. By “advantage”, I mean any number of intangible qualities that might cause you to trust a researcher, including:

- Being a well-known senior name in the field
- Coming from a respected institution or group
- Having significant funding for PR
- Being a member of a privileged racial group
- Charisma

Peer review is an invaluable resource for *disadvantaged* researchers, who lack the above qualities. In reality, of course, being “advantaged” or “disadvantaged” is not a boolean, or even a scalar, but hopefully it’s a coherent enough concept to get the point across. I think it’s fair to say that in general, the more disadvantaged a researcher is, the more they are forced to rely on the peer review process to build their resume and share their work with the community.

In fact, I see this as the *main* benefit of the double-blind peer review system. Given almost any objective function other than “ensure fair treatment of the ideas of researchers who lack advantages”, and peer review is an absolutely abysmal way of doing things. Any proposed changes to the peer review system must therefore be centered around achieving this objective. The only acceptable alternatives are those for which the opportunities for disadvantaged researchers are equal or better to their opportunities under double-blind peer review.

### The Goal of a Conference
Before suggesting changes, let’s take a closer look at what conferences[^0] actually set out to accomplish. I would argue that it is a mix of three elements:

- *Feedback.* By soliciting detailed comments from knowledgeable reviewers, peer review can help authors catch their mistakes and guide them towards doing better science.
- *Certification.* When a paper is accepted to a conference or journal, the community is in some sense acknowledging the work (and its authors) as having merit.
- *Dissemination.* When a top conference releases is proceedings, many researchers skim the proceedings and read papers they find interesting. At the conference itself, a poster or oral presentation is another chance to share your ideas directly with peers, who might build on your work.

In the pre-Internet era, a conference or journal accomplished all three goals, and was basically the only avenue for any of them. Nowadays, though, feedback and dissemination are easy to come by; OpenReview and arXiv provide ample opportunities for review and feedback, and a post to Twitter, a Reddit thread, or a podcast appearance can easily get your work into the eyes/ears of hundreds of your peers. Therefore, the focus of conferences has shifted, to become centered around the remaining component: certification.

The “certification effect” of a conference acceptance has become so massive as to be almost the entire point of conferences. Entire careers are can be put on hold on the basis of an unlucky conference rejection for a borderline paper. Think about what your peers complain about when they get rejected. How many times have you heard someone say, “I’m mad at the reviewers - they totally understood and loved my paper, yet weren’t able to give me any useful comments on how to improve it”? I’d wager almost never. The disappointment just isn’t related to feedback or dissemination. The vast majority of complaints about peer review revolve, explicitly or not, around certification: “With this unfair paper rejection, I’m one step further from grad school acceptance/graduation/a job/tenure/etc.”

Certification from a conference also enables disadvantaged researchers to take advantage of the aforementioned Internet feedback and dissemination techniques. There’s so much content on the Internet that it’s impossible to consume it all, and high-advantage researchers have a stark advantage in the attention economy. A conference’s certification carries a lot of weight: a tweet saying “Check out my new work, selected for a best paper award at ICLR!” is going to get clicks and retweets regardless who is posting.

Therefore, I argue that the main benefit of double-blind peer review is to effectively and unbiasedly certify papers as high-quality research, and people as high-quality researchers. All other objectives are secondary. It is essential that we keep this in mind when discussing alternatives and improvements to peer review.

### The Problem with Peer Review
I think most people would agree that peer review does quite a good job at evaluating papers unbiasedly. The main complaint, especially in the ML community nowadays, is that peer review is too high-variance. While the top 10% of papers are reliably accepted, and the bottom 40% are reliably rejected, the middle 50% of papers often feel like a coin flip. This is extremely frustrating for people who rely on conference acceptances to boost their careers, such as undergrad/master’s students who are trying to get into grad school, and PhD students who are trying to graduate. [^1]

The widely-acknowledged reason for this is that there are simply an enormous amount of papers submitted to all of the big ML conferences, and this trend shows no signs of reversing.  This has two effects. Firstly, it makes the conferences themselves more competitive. Since the rate of submissions is growing faster than the size of the conference, there is more and more competition for each spot every year. This means that many good-but-not-amazing contributions are being rejected every year, not because they are bad, but simply due to space constraints.
Secondly, it leads to an big burden on the reviewers. Senior reviewers are given tons of papers with too little time to read them all, and area chairs are forced to rope in less-experienced researchers to help as a result. I’m a first-year grad student, and I was asked to review 5 full papers for ICML! I did my best, but I don’t delude myself into thinking my evaluation was as accurate, or feedback as useful, as more experienced senior reviewers.

These two factors result in a huge number of “noisy middle” papers, in the 40th-90th percentile range, all of which are similar in quality; a small subset of these papers are selected for acceptance, based on the whims of the randomly-assigned reviewers and meta-reviewers. From the outside, these decisions are seemingly completely random.

Straightforward or incremental contributions often fall into this noisy middle. These papers are valuable contributions, but it is easier for reviewers to nitpick and question the novelty of these sorts of works, often dragging them down out of the top 10%. However, these sorts of projects are typically very safe, so they are a good choice for researchers who are still trying to secure a foothold in the research community. Thus, disadvantaged researchers - the ones the peer review system is supposed to serve best - are precisely the people most likely to find themselves in the noisy middle, with their acceptance determined by a coin flip! I think this was the point Matt was trying to make. Academic career paths incentivize disadvantaged researchers to pursue incremental work to get a foothold, and then even if they do a great job, they are sometimes, randomly, not rewarded with the main thing conferences should provide: certification.

Here’s two suggestions for easily-implemented but impactful changes to the peer review process that could help mitigate the variance issues. I’d love to hear people’s thoughts on these.

#### 1. Be More Explicit About Certification
Right now, the lines are blurred between certification and dissemination. For example, many consider being selected for an oral presentation to be more prestigious than just a poster presentation, simply because fewer papers are selected as orals. But the oral presentation selection criteria is sometimes very unclear - is it for “better” work, or is it just for work that an area chair thought would make a fun presentation?

A similar issue arises with conference acceptance decisions themselves. Conferences are fundamentally limited in the amount of papers they can accept, because the conference is physically limited by the size of the venue. If we agree that the role of a conference is to certify papers, isn’t it a bit weird that this certification is *relative*? Surely each paper should be evaluated as to whether it is a worthwhile contribution to science, independently from what other papers happen to be submitted that year.

So my first suggestion is this: *change from a relative metric to a standalone evaluation*. Conferences should accept or reject each paper by some fixed criteria, regardless of how many papers get submitted that year. If there end up being too many papers to physically fit in the venue, select a subset of accepted papers, at random, to invite. *This mitigates one major source of randomness from the certification process: the quality of the other papers in any given submission pool.*

One downside of the above approach is that no individual author can guarantee themselves an invite by doing good research. To fix that, conferences might consider certifying at multiple levels, similar to a grading scheme. Some papers are accepted with an A (best papers), some papers are accepted with a B, C, D, and some papers are rejected with an F. The A’s, B’s, and C’s are prioritized when assigning conference invitations, with the remaining invites randomly distributed among the D’s. Oral presentations could be randomly selected from the B’s, etc. The goal of this system is to ensure that the certification is a “sufficient statistic” for the quality of a paper, as evaluated by the conference. If Paper 1 gets a B and gives an oral, and Paper 2 gets a B but no oral, that difference is explicitly completely random, so it’s associated with no prestige. (If any non-random decision is made at any point, prestige seems inevitable, so chairs will have to fight the urge to handpick their favorite B’s to give orals.)

#### 2. Disincentivize Bad Submissions
One reason that there are so many submissions to every conference is that, well, there is no reason not to submit. Authors only stand to gain from throwing their metaphorical hat into the ring: worst case, they get some feedback, and best case, they get a lucky acceptance. However, it’s a tragedy of the commons: when reviewers are forced to shoulder the burden of reviewing all these extra “might-as-well” manuscripts, review quality goes down across the board.

Peer review is only as good as the peers doing the reviewing, and so I think that it is fundamentally impossible to have an effective peer review process with an absurdly high reviewer load. There have been various proposals for how to combat this: for example, a desk rejection process, where some papers are not even reviewed before being discarded. I want to put one more suggestion out there, though: *disincentivize low-quality submissions by publishing all submitted work.*

This means that if you submit to NeurIPS and they give you an F (rejection), it’s a matter of public record. The paper won’t be released, and you can resubmit that work elsewhere, but the failure will always live on. (Ideally we’ll develop community norms around academic integrity that mandate including a section on your CV to report your failures. But if not, we can at least make it easy for potential employers to find that information.)

Why would this be beneficial? Well, it should be immediately obvious that this will directly disincentivize people from submitting half-done work. Each submission will have to be hyper-polished to the best it can possibly be before being submitted. It seems impossible that the number of papers polished to this level will be anywhere close to the number of submissions that we see at major conferences today. Those who choose to repeatedly submit poor-quality work anyways will have their CVs marred with a string of Fs, cancelling out any certification benefits they had hoped to achieve.

Will this slow down the pace of publication? Likely, yes. But in the era of arXiv, that seems like a good thing. Put your pre-print on arXiv, solicit feedback, plant a flag or two - that’s what it’s there for. When BERT can take over the field of NLP after sitting on arXiv for two months, it’s clear that from a knowledge dissemination perspective, arXiv does a great job. So the only thing being slowed down here is the *certification* process. And maybe that’s a good thing. When it comes to submitting to conferences for formal evaluation - submissions that are guaranteed to burn the valuable reviewing hours of your peers - maybe forcing people to take some extra time to perfect their submissions.

There are some other positive externalities, too. For one thing, this sort of policy might revive the communities in smaller, “mid-tier” venues. In the stochastic-acceptance, silent-rejection paradigm we currently follow, there’s no reason for authors to submit to venues other than the top venues, unless they know for certain that their paper will never get in to the top venue. Due to the high stochasticity of the acceptance process, this means that pretty much all papers submitted to non-NeurIPS venues will be in the bottom 40% or so of typical NeurIPS submissions. That means that almost all of the good work (and hence, almost all of the attention and prestige) is concentrated in the top venues.

In the public-rejection paradigm, mid-tier venues whose acceptance standards are less rigorous than the top venues once again have a place as certifiers. Rather than submitting a paper to NeurIPS that might be a D or F, you can submit a paper to another venue and get an A or B. This is a great option! Hopefully, as more and more good researchers start doing this, prestige will become more spread among venues, further reducing both the reviewer and organizational load.

Another benefit of this approach is clear when you consider the relationship between the many authors on a typical paper. In the current system, it's basically to the advantage of any senior author to get their name on as many papers as possible. There's no downside at all: racking up the publications can only ever be beneficial.[^2] The public-rejection paradigm would hugely alter this dynamic. Public rejection introduces an element of risk to every author for every submission; a failure lands on everyone’s CVs, not just the first author’s. This will force senior authors to be much more invested in the quality of their submissions. People might even remove themselves from papers where they haven't closely read the submission in order to confirm its quality. Closer involvement from PIs would be a nearly-universal positive, especially in big labs where students can sometimes be left to fend somewhat for themselves.

If this idea seems radical to you, keep in mind: OpenReview has been publishing failures for years, without much fuss. Anyone can go right now and find out who got papers rejected from ICLR 2017. For some reason, though, nobody does this! My proposal is as much about community norms towards rejected papers as it is about actual data released by conferences. I think we should, as a community, all agree look harshly upon people who submit lots of bad papers, and make sure everyone *knows* that they are being held to this standard going forwards. This seems to me the cleanest, fairest way to fix the exponential growth of conference submissions.

### Conclusion
I’d love to get feedback from the community on this, on both my framing of this issue and my suggested changes. Do people agree or disagree? What obvious issues have I failed to consider?

*Thanks to Surya Bhupatiraju, Ryan Cotterell, Adi Renduchintala, and Isaac Buckman for feedback when writing this post.*

[^0]: I focus on conferences here, but this mostly applies to journals too.

[^1]: There are other complaints about peer review, of course. For example, the “turnaround rate” of peer review is very slow: oftentimes, by the time a paper is presented at a conference, it has already been read and built upon by the majority of the community. However, these issues seem to be orthogonal to the core purpose of double-blind peer review, so I’m not going to discuss then further here. We already have a tool for fast turnaround: arXiv. Peer review serves a unique purpose, so if we change it, we should focus on changes that let it better serve that purpose.

[^2]: There’s some rare exceptions, of course, such as if the first author commits academic fraud or something egregious, in which case the senior author gets penalized too.
