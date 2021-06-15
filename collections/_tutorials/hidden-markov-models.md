---
layout: tutorial
title: "Hidden Markov Models"
complexity: 19
pdf: "/assets/tutorials/hmm14.pdf"
---
In this tutorial we'll begin by reviewing Markov Models (aka Markov Chains) and then...we'll hide them! This simulates a very common phenomenon... there is some underlying dynamic system running along according to simple and uncertain dynamics, but we can't see it. All we can see are some noisy signals arising from the underlying system. From those noisy observations we want to do things like predict the most likely underlying system state, or the time history of states, or the likelihood of the next observation. This has applications in fault diagnosis, robot localization, computational biology, speech understanding and many other areas. In the tutorial we will describe how to happily play with the mostly harmless math surrounding HMMs and how to use a heart-warming, and simple-to-implement, approach called dynamic programming (DP) to efficiently do most of the HMM computations you could ever want to do. These operations include state estimation, estimating the most likely path of underlying states, and and a grand (and EM-filled) finale, learning HMMs from data.