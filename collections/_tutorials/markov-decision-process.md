---
layout: tutorial
title: "Markov Decision Process"
complexity: 23
pdf: "/assets/tutorials/mdp09.pdf"
---
How do you plan efficiently if the results of your actions are uncertain? There is some remarkably good news, and some some significant computational hardship. We begin by discussing Markov Systems (which have no actions) and the notion of Markov Systems with Rewards. We then motivate and explain the idea of infinite horizon discounted future rewards. And then we look at two competing approaches to deal with the following computational problem: given a Markov System with Rewards, compute the expected long-term discounted rewards. The two methods, which usually sit at opposite corners of the ring and snarl at each other, are straight linear algebra and dynamic programming. We then make the leap up to Markov Decision Processes, and find that we've already done 82% of the work needed to compute not only the long term rewards of each MDP state, but also the optimal action to take in each state.