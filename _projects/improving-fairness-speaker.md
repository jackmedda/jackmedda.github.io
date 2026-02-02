---
title: "Improving Fairness in Speaker Recognition"
slug: "improving-fairness-speaker"
layout: project-page
date: 2020-11-06
excerpt: "How demographically balanced training data can mitigate unfairness in deep speaker recognition systems."

hero_image: "/images/projects/improving-fairness-speaker/figure1_results.png"

authors:
  - "Gianni Fenu"
  - "Giacomo Medda"
  - "Mirko Marras"
  - "Giacomo Meloni"
venue: "European Symposium on Software Engineering (ESSE 2020)"
keywords:
  - Speaker Recognition
  - Fairness
  - Bias
  - Deep Learning
  - Discrimination
  - ResNet
  - X-Vector
doi: "10.1145/3393822.3432325"
paperurl: "https://doi.org/10.1145/3393822.3432325"
abstract: |
  The human voice conveys unique characteristics of an individual, making voice biometrics a key technology for verifying identities in various industries. Despite the impressive progress of speaker recognition systems in terms of accuracy, a number of ethical and legal concerns has been raised, specifically relating to the fairness of such systems. In this paper, we aim to explore the disparity in performance achieved by state-of-the-art deep speaker recognition systems, when different groups of individuals characterized by a common sensitive attribute (e.g., gender) are considered. In order to mitigate the unfairness we uncovered by means of an exploratory study, we investigate whether balancing the representation of the different groups of individuals in the training set can lead to a more equal treatment of these demographic groups. Experiments on two state-of-the-art neural architectures and a large-scale public dataset show that models trained with demographically-balanced training sets exhibit a fairer behavior on different groups, while still being accurate. Our study is expected to provide a solid basis for instilling beyond-accuracy objectives (e.g., fairness) in speaker recognition.
bibtex: |
  @inproceedings{fenu2020improving,
    author = {Fenu, Gianni and Medda, Giacomo and Marras, Mirko and Meloni, Giacomo},
    title = {Improving Fairness in Speaker Recognition},
    booktitle = {Proceedings of the 2020 European Symposium on Software Engineering},
    pages = {129--136},
    year = {2020},
    doi = {10.1145/3393822.3432325}
  }
---

<section class="project-content">
  <h3>Motivation</h3>
  <p>
    Voice biometrics are widely used for identity verification, but concerns have emerged about the fairness of these systems. This work explores whether state-of-the-art deep speaker recognition models systematically expose unfair decisions across demographic groups, and how to mitigate such unfairness.
  </p>

  <h3>Research Questions</h3>
  <ul>
    <li><strong>RQ1:</strong> Do speaker recognition models exhibit disparate error rates across demographic groups?</li>
    <li><strong>RQ2:</strong> Can balancing the training data reduce unfairness?</li>
  </ul>

  <h3>Methodology</h3>
  <ul>
    <li><strong>Models:</strong> X-Vector, Thin-ResNet</li>
    <li><strong>Dataset:</strong> Large-scale public dataset with gender and age groups</li>
    <li><strong>Metrics:</strong> Equal Error Rate (EER), False Acceptance Rate (FAR), False Rejection Rate (FRR)</li>
    <li><strong>Training:</strong> Unbalanced vs. demographically balanced data</li>
  </ul>

  <h3>Key Results</h3>
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/improving-fairness-speaker/figure1_results.png" alt="Fairness benchmarking framework" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 1:</strong> The fairness-benchmarking framework for speaker recognition systems proposed in this paper.
    </figcaption>
  </figure>
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/improving-fairness-speaker/figure2_final.png" alt="X-Vector EER variation over epochs" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 2:</strong> X-Vector EER variation over epochs for English and Spanish languages across demographic groups.
    </figcaption>
  </figure>
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/improving-fairness-speaker/figure3_final.png" alt="Thin-ResNet EER variation over epochs" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 3:</strong> Thin-ResNet EER variation over epochs for English and Spanish languages across demographic groups.
    </figcaption>
  </figure>

  <h3>Main Findings</h3>
  <ul>
    <li><strong>Balanced data helps:</strong> Larger and more demographically balanced datasets decrease disparity in EER among protected groups.</li>
    <li><strong>FAR/FRR disparity reduced:</strong> Balancing the training reduces differences in FARs and FRRs among groups.</li>
    <li><strong>Model choice matters:</strong> Thin-ResNet leads to lower disparity and is less sensitive to balance changes than X-Vector.</li>
    <li><strong>Language effects:</strong> English models tend to systematically discriminate certain groups, while Spanish models show spurious disparities.</li>
  </ul>
</section>
