---
layout: tutorial
title: "Inference in Bayesian Networks (by Scott Davies and Andrew Moore)"
complexity: 13
pdf: "/assets/tutorials/bayesinf05.pdf"
---
The majority of these slides were conceived and created by Scott Davies (scottd@cs.cmu,edu). Once you've got hold of a Bayesian Network, there remains the question of how you do inference with it. Inference is the operation in which some subset of the attributes are given to us with known values, and we must use the Bayes net to estimate the probability distribution of one or more of the remaining attributes. A typical use of inference is "I've got a temperature of 101, I'm a 37-year-old Male and my tongue feels kind of funny but I have no headache. What's the chance that I've got bubonic plague?".