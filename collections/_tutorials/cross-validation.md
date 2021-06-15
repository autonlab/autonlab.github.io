---
layout: tutorial
title: "Cross-Validation"
complexity: 7
pdf: "/assets/tutorials/overfit10.pdf"
---
Cross-validation is one of several approaches to estimating how well the model you've just learned from some training data is going to perform on future as-yet-unseen data. We'll review testset validation, leave-one-one cross validation (LOOCV) and k-fold cross-validation, and we'll discuss a wide variety of places that these techniques can be used. We'll also discuss overfitting...the terrible phenomenon that CV is supposed to present. And at the end, our hairs will stand on end as we realize that even when using CV, you can still overfit arbitrarily badly.