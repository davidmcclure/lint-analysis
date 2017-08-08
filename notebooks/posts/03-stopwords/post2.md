# Distributions of function words across narrative time

Last week I looked at some of the narratological "cohorts" or "topics" that fell out of a hierarchical cluster of the distributions of words across narrative time - groups of words that tend to rise and fall together inside of novels, when averaged out across the ~27k texts in the Literary Lab's corpus of American novels. One side effect of this kind of exploratory approach, I think, is that there's a tendency to focus on things that make sense, essentially - things that are easy to map back onto the experience of actually reading novels. For example, it's easy to reason about what's going on with cluster 37 (pistol, bullet, gun) or 139 (student, students, school) - which, as Ted and Scott pointed out on Twitter, might say more about the presence of different genres in the corpus than about "narrative," in any kind of general sense. But, what to make of something like cluster 10, which includes, among other things, stopwords like "a," "an," "or," "than," "these"?

[37, 139, 10 ??]

These really high-frequency function words turn out to have *very* strong strong trends across narrative time - in fact, stronger than almost anything else in the entire dictionary. Take a look again at this graph from a couple weeks ago, which plots the variance of each word across narrative time as a function of its frequency:

[variance ratios]

The Y-axis here is basically a simple measure of narratological "surprise," the degree to which a word isn't just a flat line when you plot out its frequency across the narrative. The blue line represents the null hypothesis, essentially - the amount of variance we'd expect under the uniform distribution, if everything were just random noise. The interesting thing about this, though, is that that slope of the data is clearly steeper than the slope of this line - words seem to become *more* non-uniform as they become more frequent, even after adjusting for the expected correlation between frequency and variance. By and large, the most frequent words are also the most narratologically "uneven" words.

Here are 100 highest-scoring words under this metric (same as the coloring in the graph), which contain 42 out of the 100 most-frequent words in the corpus:

[top 100, bolding]

What to make of this? It's kind of perplexing, in a sense, and not what I expected at the start. I assumed that function words would be basically flat, since I don't really think of them as having any kind of semantic "focus" that would cause them to consistently attach to any particular region across the narrative axis, in the way that things like "death" or "marriage" do. I thought they'd probably be *negative* examples of what I was looking for - words that, by virtue of their frequency, just sort of have to show up everywhere, more or less evenly. (Though I also remembered Matt Jockers' finding from *Macroanalysis* that the word "the" fluctuates across historical time, and a little voice in the back of my head wondered if there might be similar effects across narrative time.)

Usually, when something correlates with frequency like this, it feels like a red flag, the worry being that you're somehow just reproducing the fact that frequent words are frequent, infrequent words are infrequent. As a sanity check, I re-ran the exact same feature extraction job on the corpus, but this time, before pulling out the percentile counts, I randomly shuffled the words in each text to destroy any kind of narratological ordering. Sure enough, with this, the variances clamp right onto the expected line:

[random variances]

So, I think there is actually some meaninful way in which highest frequency words are the most non-uniform across the axis of the text, the most uneven, the most narratologically *charged*? This seemed totally bizarre to me at first, then I convinced myself that it wasn't actually that weird, but now I'm sort of back to thinking it's bizarre. But, I'm not really sure if my expectations are calibrated correctly. Am I wrong to be surprised by this?  Is it somehow tautologically true, is there some kind of inevitable linguistic / narratological / information-theoretic pressure that would make it impossible for this not to be the case, in some way?

Part of the issue, I think, is that this question of whether a word is narratologically "non-uniform" or "uneven" is actually less cut-and-dry than it seemed to me at first, and gets caught up in interesting ways with the overall frequency of the word. For example, take the word "gun" - which appears 174,286 times - and the word "a," which shows up 44,510,387 times, about 255 times more often:

[a, gun histograms]

Which of these is more "surprising"? If you think of them as density functions, then "gun" obviously has the more dramatic trend - a huge spike around the X% marker, the moment of the crime / climax, where it literally doubles in volume relative to the baseline across the first half of the narrative. Indeed, if you literally convert them into density functions - throwing out any information about the overall frequencies - and then compare them to a uniform distribution using pretty much any measure of statistical distance or goodness-of-fit, "gun" will always score as more "non-uniform" by a large margin. Just using the Euclidean distance, like I did last week for the hierarchical cluster - "gun" has a distance of XX from the uniform distribution, where as "a" is just YY.

[a, gun, relativized series]

"A," then, as a density function, is much "flatter." But, when you remember the actual footprint of the word in the corpus - "a" appears a total XX times, which represents about X% of all words in all 27k novels - the total quantity of linguistic "mass" that's getting displaced is sort of fascinating and bizarre. In the first percentile, "a" appears XX times more than you'd expect under the null hypothesis, and XX fewer times than you'd expect in the last percentile. Here it is again, plotted with an error bar around the expected uniform distribution - if "a" had no trend across narrative time, then 95% of the bin counts would fall inside of the gray band, which is barely even visible in the context of the actual curve:

[a]

"A" is flatter, but since it's so frequent, it represents a kind of massive, tectonic displacement of words, sort of like the gravity of the moon pulling the tide in and out - the water only rises and falls a couple of feet, but in order for that to happen the entire mass of the ocean has to get moved around. The amount of narratological energy needed to produce the "a" trend, from this perspective, seems much larger than for "gun."

To get a broader sense of this, we can find words that are both very frequent and also very "uneven" across the narrive. If we take the 100 most-frequent words across the entire corpus, 90 of them show up inside of the list of the 1,000 most non-uniform words from last week (roughly the top 10%). Here, this set of 90, sorted from most to least non-uniform - starting with the most narratologically "skewed". (Again, important to note that the Y-axes are different, it makes it easier to see the smaller-but-still-huge trends in the second half of the list. Everything here is significant at p ≈ 0.)

[90]

- a / an / the
- and / or / but
- to be
- pronouns
- punctuation


## a, an, the

Again, there's way too much here to go through all of it, but quickly - what's up with "a"? High at the very beginning, a fast falloff, then a slower decline across the middle, and a quick falloff at the very end. "An" is almost identical, though with more noise in the simple, since it's less frequent:

[a, an]

There's a pretty easy explanation for this, though I'm kind of fascinated by the fact that it (seems to) show up at the scale of the entire narrative, and not just inside of individual passages - "a" is used when an object is introduced for the first time, when an entity makes its first appearance in some context. For example, you might first say - "a man was walking down the street" - but then, after that, you'd switch to the definite article - "*the* man walked into a shop," etc. As Franco pointed out to me, Benveniste makes exactly this point in *Problems in General Linguistics*:

[benvensite]

So, with the caveat that this is totally speculative - maybe one way to think of this is to say that "a" is a kind of proxy for the *rate at which newness is introduced into the text*? At the beginning this is very high, as the fictive world is described into existence, people and places are introduced, the pieces of the narrative are put into place. It then falls off rapidly after the beginning once the stage it set and the plot starts to spool out, as the narrative starts to increasingly return to fictive matter that has already been introduced, making "a" less necessary. Then, over the course of the middle, the plot continues to move into new fictional space - new people, new places, new objects - but more slowly than at the beginning, which had to bootstrap the entire world into existence from the ground up. And finally, at the end, this rate of movement falls off quickly around the 95% mark - as if the text arrives at its ending point a bit early and stays there for a beat. "A," in other words, gives an empirical X-ray of the "speed" of the novel, in one sense of the idea - the degree to which it's moving into new fictive contexts that have to be introduced for the first time, as opposed to standing still inside contexts that have already been introduced? (This reminds me of those old RPGs from the late 90s like Baldur's Gate or Icewind Dale, where by the default the entire world of the game is black, and things only come into view as your character moves around the map, as the spotlight of the game falls onto new territory for time - the moment of "a.")

Is this the right explanation? It seems sensible, but I don't really know. The funny thing, though, is that it's not actually clear to me how you'd "prove" this, either at a linguistic or a literary register - it seems like the next step would be to dip back down into individual texts and start spot-checking passages, but with a word like"a," which will appear literally millions of times in virtually all contexts, this seems sort of like a losing game. I guess the first thing to do would be to look computuationally at words that follow "a," and see if some kind of pattern falls out? Eg, count up all "a __" bigrams, and then find words that come after "a" most distincticely in the first percentile, as compared to the last percentile?

Even if it's true that "a" is marking the rate of world-building in the narrative - it's also not clear to me what to think about that from a kind of meta-interpretive level, how to situate the interpretaton. Does it make sense to think of this as just a lower-level version of the types of narratological unities / genre conventions that push "youth" and "college" to the beginning, "death" and "marriage" to the end? Or does that overestimate the importance of literary convention, at this level - again, is there some sense in which this trend is inevitable, that it must be the case, that it would be nearly impossible to write a narrative that doesn't show this pattern? In terms of "a" - is a novel like a ball placed at the top of a steep, smooth incline, where it would take some kind of huge narratological exertion not to roll down the slope, not to show this falloff in the frequency of the word? (Which raises the question - are there individual texts that invert this, where "a" increases - texts that roll uphill?)

"The" is interestingly different:

[the]

Also very high at the start, a fast falloff in the first 10% (much faster than for "a"), comparatively low through the middle, and then a small but still very significant uptick at the end. So, "a" and "the" - flip sides of the same coin, grammatically speaking - seem to different work at a narratological. Both seem to make beginnings and ends, but in different ways. "A" shows something about how they are different - beginnings are building worlds, ends are inhabiting those worlds? Whereas "the" is high at both the beginning and the end, and so, I suppose, is proxying something about how they are similar, a way in which the end is some kind of return to the beginning? But, in what sense?

## Determiners - this, that, these, those

Beyond "a" and "the" - the other determiners are interesting:

[determiners]

Or, just this / that / these / those:

[this that these those]

So, at a narratological level, they basically pair up on the basis of singular / plural, not near / far? "This" and "that" are low at the beginning, peak around 70%, and then fall off at the end:

[this, that]

Whereas "these" and "those" are very high at the start, flat across the middle, and then split at the end, with "those" going up and "these" falling off:

[these, those]

JD pointed out that "this" and "that" look a lot like the dialogue clusters from before, and that, in the Corpus of Contemporary American English at BYU, "this" and "that" are most frequent in the "Spoken" sub-corpus. So, maybe this is driven by dialogue? If so, then - when people talk about things, they tend to talk about singular things - this morning, that man - not multiple things?

As for "these" and "those" - I'm not sure why plurals would be so high at the beginning, but it seems to match up with other signals. For example, if we compare the overall distributions of singular and plural nouns:

[NN, NNS]

The plurals are significantly higher at the start, so I guess it makes sense that there would also need to be more these's and those's. (Which just begs the question, though - why are plural nouns higher at the start?) The divergence at the end is also interesting - why does "those" spike up, and "these" fall off? Again, all of this really needs much more careful attention, but - picking up on the "geography" words from the last post, this kind of fits with the idea that the end is a sort of "zooming out," if we think of the narrative as a kind of camera onto the fictional world? At the end the narrative pans out into a wide shot of the surrounding mountains / fields / valleys, it makes itself *distant* from the action of the plot - the domain of "those," not "these"?

Check out the "how much" determiners - "all," "some," and "no" ("no" as a determiner, specfically, in the sense of "there were no people in the room"):

[all, some, no]

All peaks at the end, the moment of generalization, completeness, closure? I'm less sure what to make of the fac that "some" peaks at 20%, but "no" at 80%:

[some, no]

Meanwhile, to close out the determiners - why does "each" skyrocket at 99%, but "every" stays low:

[each, every]

## Conjunctions

Conjunctions are also fascinating. "And" and "or":

[and, or]

Again, there's a fairly tidy explanation for the split at the end, though I'm still kind of bewildered that this stuff actually shows up at such a low level. "Or" introduces a branch, an indeterminacy - Robert will blow the bridge, or he will die trying; Lucy will marry Cecil, or she will marry George; etc. And so, as the plot moves towards a close, "or" has to fall off as the ending is revealed, as uncertainty is replaced by certainty, as the Jamesian "circle" comes to a close and the plot gets sealed up as a unified whole?

This is going on too long, but really quickly - check out the verbs to be:

[to be]

Which split really cleanly into present tense:

[present]

And past:

[past]

So - middles and ends are in the present tense, beginnings and climaxes are in the past?

Anyway, there's sort of an infinity of stuff to look at here (pronouns, prepositions, and high-frequency adjectives are especially interesting), and it's hard to know what to pick out at the start. More on this to come.