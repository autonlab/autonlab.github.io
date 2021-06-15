---
layout: tutorial
title: "VC Dimension"
complexity: 20
pdf: "/assets/tutorials/vcdim08.pdf"
---
This tutorial concerns a well-known piece of Machine Learning Theory. If you've got a learning algorithm in one hand and a dataset in the other hand, to what extent can you decide whether the learning algorithm is in danger of overfitting or underfitting? If you want to put some formal analysis into the fascinating question of how overfitting can happen, then this is the tutorial for you. In addition to getting good understanding of the overfitting phenomenon, you also end up with a method for estimating how well an algorithm will perform on future data that is solely based on its training set error, and a property (VC dimension) of the learning algorithm. VC-dimension thus gives an alternative to cross-validation, called Structural Risk Minimization (SRM), for choosing classifiers. We'll discuss that. We'll also very briefly compare both CV and SRM to two other model selection methods: AIC and BIC.