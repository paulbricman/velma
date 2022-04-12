---
layout: post
age: 20.94
title: infinite skills
published: True
---

## infinite skills

Gardner's theory of multiple intelligences claims that human skills can be neatly assigned to one of eight categories. While the scientific value of this taxonomy proved to be dubious at best, Gardner's model still does one thing right: it highlights the very breadth of human skill. In this, the original theory -- or any related taxonomy, for that matter -- can serve as a pragmatic reminder of just how diverse one's skillset can be. Being aware of such opportunities of skill acquisition is the first step in actually cultivating a broad and balanced set of skills.

This awareness is particularly useful when finding oneself in an echo chamber. If most people around me happen to be focused on cultivating analytical skills (e.g. reasoning, programming, decision making), I might forget that there's a whole world of kinesthetic skills out there to explore, for instance. Not that Gardner's categories perfectly encompass and dissect the space of possible skills or anything. Rather, they merely serve as imperfect pointers, basic guardrails against complacency. Here they are:

- logical-analytical
- verbal-linguistic
- visual-spatial
- musical
- intrapersonal
- interpersonal
- kinesthetic
- naturalistic

After reflecting a bit on how one's skillset fares against Gardner's model, it's inevitable that both strengths and weaknesses eventually pop up. The weaknesses, if viewed as opportunities for improvement, can then be seen as broad directions to investigate in more depth if one aimed for a balanced range of skills. This exercise is quite humbling, but in order for it to become useful, the observations have to be translated into real-world strategies for actually honing those skills. Strategizing towards such a goal is intimidating, because aiming to generally cultivate skills in one of these macro categories is as long-term and vague as goals can get. What now?

I personally find it effective to address this challenge through what I call infinite skills, in an analogy to the infinite lists found in Haskell and other lazily-evaluated programming languages. In Haskell, the following defines an infinite list of perfect squares:

```haskell
>>> x = [d | d <- map (^2) [1, 2..]]
```

I can take the first 10 elements of this infinite list and print them on screen:

```haskell
>>> take 10 x
[1,4,9,16,25,36,49,64,81,100]
```

I can also check if a number is part of that list:

```haskell
>>> elem 1000000 x
True
```

But how's it possible to work with infinite lists? After all, the computer I'm running this on has finite memory. The reason is that Haskell and similar languages work around this issue by only computing the elements which are needed, and at the same time delaying the computation of other elements as much as possible. In fact, the linked list implementation used underneath Haskell has the last node point to some code which can be used to compute the rest of the tail, rather than to another element from the list. Haskell is procrastinating by design, which seems to enable it to make progress across infinite tasks... when really necessary.

The way this relates to cultivating a balanced skillset is the following. For each of Gardner's macro categories, you'd have at least an infinite skill. An infinite skill is nothing more than an infinite list of specific skills, following a clear pattern, but only scheduled if necessary. Here are some concrete examples to help illustrate the concept:

- an infinite visual-spatial skill could consist in picking a new material each time (e.g. paper, ink) and [creating 100 artifacts](/materials) with each one before moving on;

```haskell
>>> vs = [s | s <- map createUsing [Paper, Ink..]]
```

- an infinite verbal-linguistic skill could consist in picking up a new language each time (e.g. Mandarin, Hebrew) and studying it for two years before moving on;

```haskell
>>> vl = [s | s <- map studyForTwoYears [Mandarin, Hebrew..]]
```

- an infinite kinesthetic skill could consist in picking up a new sport each time (e.g. squash, paddleboarding) and following an amateur course on it before moving on;

```haskell
>>> k = [s | s <- map takeCourseOn [Squash, Paddleboarding..]]
```

- an infinite musical skill could consist in picking up a new instrument each time (e.g. guitar, piano) and learning to play 50 songs on it before moving on;

```haskell
>>> m = [s | s <- map learnSongsOn [Guitar, Piano..]]
```

The overarching structure of infinite skills nudges you into continuously investing time and energy in cultivating a balanced skillset throughout your life, while the "lazy-evaluation" prevents you from having to schedule things several decades in advance from the very first day. It's an elegant mix of long-term goals and short-term actions -- we'll figure it when we get there, but we generally know what it is we have to figure out. In this, there's minimal friction and overhead in navigating the infinite skill from one element to the next, while the general vision is embedded in the high-level pattern of the list comprehension.

The reason this is valuable is because we're not used to conceiving of such long periods of time as our lifetimes. For all practical purposes, a lifetime appears infinite when we're deeply engaged in day-to-day tasks. I'm reminded here of a scene from Greg Egan's Permutation City. In the novel, people transcend their bodies by uploading their mind to the cloud. A conundrum inevitably arises: how will they chose to spend their infinite lives? In the fragment below, people resort to having an external system (i.e. their exoself) schedule their vocations.

<div class="top-pad"><blockquote class="quoteback" darkmode="" data-title="Permutation City" data-author="Greg Egan" cite="https://www.gregegan.net/">
The workshop abutted a warehouse full of table legs—one hundred and 
sixty-two thousand, three hundred and twenty-nine, so far. Peer could 
imagine nothing more satisfying than reaching the two hundred thousand 
mark—although he knew it was likely that he’d change his mind and 
abandon the workshop before that happened; new vocations were imposed by
 his exoself at random intervals, but statistically, the next one was 
overdue. Immediately before taking up woodwork, he’d passionately 
devoured all the higher mathematics texts in the central library, run 
all the tutorial software, and then personally contributed several 
important new results to group theory—untroubled by the fact that none 
of the Elysian mathematicians would ever be aware of his work. Before 
that, he’d written over three hundred comic operas, with librettos in 
Italian, French and English—and staged most of them, with puppet 
performers and audience. Before that, he’d patiently studied the 
structure and biochemistry of the human brain for sixty-seven years; 
towards the end he had fully grasped, to his own satisfaction, the 
nature of the process of consciousness.
<footer>Greg Egan<cite> <a href="https://www.gregegan.net/">https://www.gregegan.net/</a></cite></footer>
</blockquote><script note="" src="https://cdn.jsdelivr.net/gh/Blogger-Peer-Review/quotebacks@1/quoteback.js"></script></div>

This scene is as disturbing as it is intriguing. Our intuitions pale in comparison to the long spans of time, and we often resort to artificial systems to put them in perspective. Infinite skills are a modest attempt at designing such a system, a behavioral foothold in a virtually boundless unknown.
