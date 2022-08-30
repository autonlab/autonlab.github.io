---
layout: research
title:  "Pragmatic Deep Learning"
splash: "/assets/images/pragmatic_deep_learning.jpg"
summary: "Some of the contemporary limitations of deep learning can be traced back to the fields early days. At Auton Lab, we try to unlock the same benefits of deep learning with novel approaches that reduce the complexity or the appetite for data. Additionally, a goal is to increase interpretability by keeping models as simple. This thrust involves building new model classes that are capable of deep learning while possessing structural advantages that make the methods applicable in select real-world contexts."
projects:
  - 
    name: Hybrid Forecasting
    anchor: forecasting
    image: "/assets/images/nhits.jpg"
    blurb: "Multi-variate time-series forecasting, classification, and anomaly detection. Incorporating exogenous variables to reduce forecasting error. Learning heirarchical, structural elements of data to aid in forecasting."
  -
    name: Deep Survival Analysis
    anchor: survival
    image: "/assets/images/deep_survival_models.jpg"
    blurb: "Predicting time to failure under censored outcomes. Discovering effective interventions under assumptions of heterogeneity."
  -
    name: Bayesian Deep Learning
    anchor: vaes
    image: "/assets/images/autoencoder_diagram.png"
    blurb: "Auton Lab works on methods to build autoencoders with fewer parameters than deep network alternatives, trading fidelity for scalability. This work enables accurate forecasting for long windows into the future. Variational autoencoders break the assumption of independence among subsequent layers in the network. That reduces complexity of the model but maintains performance. Reduces time to train, resource consumption, etc."
  -
    name: Deep Reinforcement Learning
    anchor: deeprl
    image: "/assets/images/genetic_curriculum.gif"
    blurb: "Auton lab focuses on using curriculum learning and genetic algorithms to sample-efficiently train an RL agent against the long tail of scenarios (last 10% of scenarios that are difficult to train). One approach to achieve robustness is to use adversarial agents to inject noise during training to steer the exploration towards these challenging scenarios. However, this often converges to worst case situations in which the protagonist cannot learn and requires expert supervision to avoid this issue. Instead, we use genetic algorithms to generate adversarial scenarios. Generated via genetic algorithms, these scenarios are similar to each other and can work as a curricular RL where skills are transferred between similar tasks of varying difficulty levels. Empirical results show that our algorithm results in RL agents 2 ~ 8 times less likely to fail a task without scrificing performance (average cumulative rewards)."
  -
    name: Offline Reinforcement Learning
    anchor: offlinerl
    image: "/assets/images/compressed_carla.gif"
    blurb: "Auton lab works on developing methods that can learn policies from large datasets of previously collected trajectories without requiring expensive or dangerous on-policy samples. This work is crucial for bringing reinforcement learning approaches to safety critical domains like autonomous driving or domains where online samples are expensive to collect like nuclear fusion. We develop both model-based and model-free approaches and explore their effectiveness in settings with various degrees of data quality."

---
<!--
  -
    name: Deep Creativity
    anchor: creative
    image: "/assets/images/creative_ai_sculpture.jpg"
    blurb: "Style infusion, morphing of images. [blank]"
---
-->

<!-- Notes


-->


  
