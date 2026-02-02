---
title: "How Fair is Your Diffusion Recommender Model?"
collection: projects
permalink: /projects/fairdiffrec/
date: 2025-09-22
year: 2025
venue: "ACM Conference on Recommender Systems"
venue_short: "RecSys"

teaser: "/images/projects/fairdiffrec/kiviat_pikepdf_preview.png"
hero_image: "/images/projects/fairdiffrec/kiviat_pikepdf_preview.png"

authors:
  - "Daniele Malitesta"
  - "Giacomo Medda"
  - "Erasmo Purificato"
  - "Mirko Marras"
  - "Fragkiskos D. Malliaros"
  - "Ludovico Boratto"

author_links:
  Daniele Malitesta: "https://danielemalitesta.github.io/"
  Giacomo Medda: "https://jackmedda.github.io/"
  Erasmo Purificato: "https://erasmopurificato.github.io/"
  Mirko Marras: "https://www.mirkomarras.com/"
  Fragkiskos D. Malliaros: "https://fragkiskos.me/"
  Ludovico Boratto: "https://www.ludovicoboratto.com/"

keywords:
  - Diffusion Models
  - Recommender Systems
  - Fairness
  - Consumer Fairness
  - Provider Fairness

doi: "10.1145/3705328.3759318"
paperurl: "https://doi.org/10.1145/3705328.3759318"
code: "https://github.com/danielemalitesta/FairDiffRec"

abstract: |
  Diffusion models have recently emerged as a promising paradigm for recommender systems, demonstrating impressive performance in modeling user preferences. However, as with other deep learning approaches, concerns about fairness remain largely unexplored for these models. This paper presents the first comprehensive empirical study on the fairness properties of diffusion-based recommender systems. We investigate how DiffRec and its variants perform across different demographic groups, analyzing both consumer and provider fairness from multiple perspectives.

bibtex: |
  @inproceedings{malitesta2025fairdiffrec,
    author = {Malitesta, Daniele and Medda, Giacomo and Purificato, Erasmo and Marras, Mirko and Malliaros, Fragkiskos D. and Boratto, Ludovico},
    title = {How Fair is Your Diffusion Recommender Model?},
    booktitle = {Proceedings of the 19th ACM Conference on Recommender Systems},
    series = {RecSys '25},
    year = {2025},
    publisher = {Association for Computing Machinery},
    doi = {10.1145/3705328.3759318}
  }
---

<section id="motivation">
  <h2>Motivation</h2>
  <div class="highlight-box">
    <p>
      <strong>Why study fairness in diffusion recommenders?</strong> Diffusion models represent a new generation of 
      recommender systems with state-of-the-art performance. However, their fairness properties are completely unknown. 
      Understanding potential biases is crucial before widespread deployment of these systems.
    </p>
  </div>
</section>

<section id="method">
  <h2>Methodology</h2>
  <p>
    We study DiffRec and its variants, which apply diffusion processes to collaborative filtering. The core idea 
    is to model the user-item interaction generation as a reverse diffusion process:
  </p>
  <p style="text-align: center;">
    $\mathbf{x}_t = \sqrt{\alpha_t}\mathbf{x}_0 + \sqrt{1-\alpha_t}\boldsymbol{\epsilon}$
  </p>
  <p>For demographic parity, we measure the disparity in performance metrics between user groups:</p>
  <p style="text-align: center;">
    $$\text{DP} = |S(G_1) - S(G_2)|$$
  </p>
</section>

<section id="results">
  <h2>Key Findings</h2>
  <ul>
    <li><strong>Gender fairness:</strong> DiffRec shows comparable or slightly better fairness than GNN-based models</li>
    <li><strong>Age fairness:</strong> More significant disparities observed, with younger users receiving better recommendations</li>
    <li><strong>Provider fairness:</strong> Diffusion models favor popular items similar to other neural approaches</li>
  </ul>
  <div class="highlight-box">
    <p>
      <strong>Key insight:</strong> Diffusion recommender models are not inherently fairer than traditional approaches. 
      Fairness considerations should be explicitly incorporated into diffusion-based recommendation pipelines.
    </p>
  </div>
</section>
