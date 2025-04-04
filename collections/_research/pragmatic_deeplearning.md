---
layout: research
title:  "Pragmatic Deep Learning"
splash: "/assets/images/pragmatic_deep_learning.jpg"
summary: "Some of the contemporary limitations of deep learning can be traced back to the fields early days. At Auton Lab, we try to unlock the same benefits of deep learning with novel approaches that reduce the complexity or the appetite for data. Additionally, a goal is to increase interpretability by keeping models as simple. This thrust involves building new model classes that are capable of deep learning while possessing structural advantages that make the methods applicable in select real-world contexts."
projects:
  -
    name: Deep RL for Nuclear Fusion
    anchor: tokamak
    image: "/assets/images/tokamak.jpg"
    blurb: "Nuclear fusion is one of the most exciting prospective energy generation technologies available to humanity. By replicating the nuclear reaction that takes place in the sun, one could extract millions of times more energy per gram of fuel than by using traditional combustion methods. The most promising technologies for fusion require a plasma to be magnetically confied and heated to extreme temperatures. Because the dynamics of plasma are complex, they are difficult to model and simulate, and it is challenging to design controllers which can achieve the neccesary conditions for fusion. Auton Lab uses AI to learn dynamics models and value functions for plasma control problems that can help us achieve successful controlled fusion. We tackle problems like regulating the plasma pressure, predicting potential 'disruptions' in confinement, and safe shutdown of the machine. We have demonstrated in experiments on the DIII-D tokamak in San Diego that AI can successfully predict the evolution of plasma dynamics and find controls that can successfully achieve goal plasma states. As projects like the ITER tokamak in France become operational, we hope that our work can inspire additional applications of AI to achieve fusion reactions with positive net energy."
   
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
    name: Genetic Curriculum for Deep Reinforcement Learning
    anchor: deeprl
    image: "/assets/images/genetic_curriculum.gif"
    blurb: "Auton lab focuses on using curriculum learning and genetic algorithms to sample-efficiently train an RL agent against the long tail of scenarios (last 10% of scenarios that are difficult to train). One approach to achieve robustness is to use adversarial agents to inject noise during training to steer the exploration towards these challenging scenarios. However, this often converges to worst case situations in which the protagonist cannot learn and requires expert supervision to avoid this issue. Instead, we use genetic algorithms to generate adversarial scenarios. Generated via genetic algorithms, these scenarios are similar to each other and can work as a curricular RL where skills are transferred between similar tasks of varying difficulty levels. Empirical results show that our algorithm results in RL agents 2 ~ 8 times less likely to fail a task without scrificing performance (average cumulative rewards)."
  -
    name: Offline Reinforcement Learning
    anchor: offlinerl
    image: "/assets/images/compressed_carla.gif"
    blurb: Auton Lab works on leveraging deep reinforcement learning for motion planning in autonomous driving. While traditional motion planning approaches rely on handcrafted heuristics and brittle, hard-coded policies, we’re interested in how reinforcement learning can be used to automate this process by learning from data. We have investigated how online reinforcement learning algorithms can be deployed on autonomous vehicles in simulation, and have used state-of-the-art on-policy and off-policy approaches to solve various simulated driving benchmarks. We are exploring how we can continue to scale these approaches to tackle more complicated scenarios and how we can accelerate training by exploiting parallelism. Additionally, the lab is focused on offline reinforcement learning, which can learn policies from large datasets of previously collected trajectories without requiring on-policy samples. This work is crucial for bringing reinforcement learning approaches to safety-critical real-world domains like autonomous driving. We develop both model-based and model-free approaches and explore their effectiveness in settings with various degrees of data quality."

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


  
