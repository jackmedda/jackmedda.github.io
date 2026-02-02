---
title: "Fair Voice Biometrics: Impact of Demographic Imbalance on Group Fairness in Speaker Recognition"
slug: "fair-voice-biometrics"
layout: project-page
date: 2021-08-30
excerpt: "Studying how group fairness metrics relate to training data balancing in speaker recognition systems."

hero_image: "/images/projects/fair-voice-biometrics/figure1_a.png"

authors:
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
  - "Giacomo Meloni"
author_links:
  "Mirko Marras": "https://www.mirkomarras.com/"
venue: "Interspeech 2021"
keywords:
  - Speaker Recognition
  - Speaker Verification
  - Fairness
  - Bias
  - Biometrics
  - Data Imbalance
doi: "10.21437/interspeech.2021-1857"
paperurl: "https://doi.org/10.21437/interspeech.2021-1857"
abstract: |
  Speaker recognition systems are playing a key role in modern online applications. Though the susceptibility of these systems to discrimination according to group fairness metrics has been recently studied, their assessment has been mainly focused on the difference in equal error rate across groups, not accounting for other fairness criteria important in anti-discrimination policies, defined for demographic groups characterized by sensitive attributes. In this paper, we therefore study how existing group fairness metrics relate with the balancing settings of the training data set in speaker recognition. We conduct this analysis by operationalizing several definitions of fairness and monitoring them under varied data balancing settings. Experiments performed on three deep neural architectures, evaluated on a data set including gender/age-based groups, show that balancing group representation positively impacts on fairness and that the friction across security, usability, and fairness depends on the fairness metric and the recognition threshold.
bibtex: |
  @inproceedings{fenu21_interspeech,
    author = {Gianni Fenu and Mirko Marras and Giacomo Medda and Giacomo Meloni},
    title = {Fair Voice Biometrics: Impact of Demographic Imbalance on Group Fairness in Speaker Recognition},
    booktitle = {Proc. Interspeech 2021},
    pages = {1892--1896},
    year = {2021},
    doi = {10.21437/Interspeech.2021-1857}
  }
---

<section class="project-content">
  <h3>Motivation</h3>
  <p>
    Speaker recognition systems are increasingly adopted in online and onlife applications to confirm or refute a user's identity based on voice characteristics. While these systems have achieved impressive accuracy using deep neural networks (X-Vector, ResNets), recent literature has uncovered algorithmic discrimination. Previous fairness assessments focused mainly on the difference in equal error rate across groups, not accounting for other fairness criteria important in anti-discrimination policies.
  </p>

  <h3>Research Questions</h3>
  <ul>
    <li><strong>RQ1:</strong> How do fairness metrics change under different training data balancing settings?</li>
    <li><strong>RQ2:</strong> What is the impact of the recognition threshold on the trade-off between fairness, security, and usability?</li>
  </ul>

  <h3>Fairness Metrics</h3>
  <p>
    We operationalized several group fairness definitions for speaker verification:
  </p>
  <ul>
    <li><strong>Demographic Parity (DP):</strong> The likelihood of being positively recognized should be the same regardless of group membership</li>
    <li><strong>Equal Opportunity (EOpp):</strong> All demographic groups should have equal true positive rates</li>
    <li><strong>Equalized Odds (EOdd):</strong> Demographic groups should have equal rates for both true positives and false positives</li>
  </ul>

  <h3>Experimental Setup</h3>
  <ul>
    <li><strong>Models:</strong> X-Vector, ResNet-34, ResNet-50</li>
    <li><strong>Dataset:</strong> FairVoice with gender and age-based groups</li>
    <li><strong>Balancing:</strong> Unbalanced (NB) vs. User-based balanced (UB) training sets</li>
    <li><strong>Security levels:</strong> EER and FAR 1%</li>
  </ul>

  <h3>RQ1: Impact of Data Balancing on Fairness</h3>
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/fair-voice-biometrics/figure1_a.png" alt="Fairness estimates for EER Gender" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 1a:</strong> EER - Gender. Fairness estimates under different training data balancing settings.
    </figcaption>
  </figure>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/fair-voice-biometrics/figure1_b.png" alt="Fairness estimates for EER Age" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 1b:</strong> EER - Age. Fairness estimates under different training data balancing settings.
    </figcaption>
  </figure>

  <p>
    Balancing users across demographic groups often helps mitigate unfairness. The disparities between males and females are mitigated for all models under almost all fairness metrics. ResNet-34 is influenced the most by data balancing, followed by X-Vector. Surprisingly, ResNet-50 tends to be fairer on gender-based groups regardless of balancing.
  </p>

  <h3>RQ2: Impact of Recognition Threshold</h3>
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/fair-voice-biometrics/figure2_a.png" alt="Trade-off analysis for ResNet-34 Age" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 2a:</strong> ResNet-34 - Age. Impact of recognition threshold on the trade-off between fairness, security (FAR), and usability (FRR).
    </figcaption>
  </figure>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/fair-voice-biometrics/figure2_b.png" alt="Trade-off analysis for ResNet-34 Gender" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 2b:</strong> ResNet-34 - Gender. Impact of recognition threshold on the trade-off between fairness, security (FAR), and usability (FRR).
    </figcaption>
  </figure>

  <p>
    For almost all settings, the disparity scores show their peaks nearby the EER and FAR 1% security levels. This suggests that common operational thresholds may coincide with regions of higher unfairness.
  </p>

  <h3>Main Findings</h3>
  <ul>
    <li><strong>Balancing helps fairness:</strong> User-based balancing across demographic groups positively impacts fairness metrics</li>
    <li><strong>Architecture matters:</strong> Different architectures respond differently to balancing - ResNet-34 benefits the most</li>
    <li><strong>Threshold-fairness relationship:</strong> Fairness disparity peaks near common security thresholds (EER, FAR 1%)</li>
    <li><strong>Multiple metrics needed:</strong> A single fairness metric is insufficient; different notions capture different aspects of discrimination</li>
    <li><strong>Trade-offs exist:</strong> The friction across security, usability, and fairness depends on the fairness metric and recognition threshold</li>
  </ul>
</section>
