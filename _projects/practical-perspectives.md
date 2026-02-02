---
title: "Practical Perspectives of Consumer Fairness in Recommendation"
slug: "practical-perspectives"
layout: project-page
date: 2023-01-06
excerpt: "A comprehensive benchmark evaluating mitigation procedures against consumer unfairness across eight technical properties."
authors:
  - "Ludovico Boratto"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
author_links:
  "Ludovico Boratto": "https://www.ludovicoboratto.com/"
  "Mirko Marras": "https://www.mirkomarras.com/"
venue: "Information Processing and Management (IPM 2023)"
keywords:
  - Recommender systems
  - Consumer fairness
  - Mitigation procedure
  - Systematic mapping
  - Evaluation protocol
  - Reproducibility
  - Benchmark
doi: "10.1016/j.ipm.2022.103208"
paperurl: "https://doi.org/10.1016/j.ipm.2022.103208"
code: "https://github.com/jackmedda/Perspective-C-Fairness-RecSys"
abstract: |
  In recent years, there has been an increasing number of mitigation procedures against consumer unfairness in personalized rankings. However, the experimental protocols adopted so far for evaluating a mitigation procedure were often fundamentally different (e.g., with respect to the fairness definitions, data sets, data splits, and evaluation metrics) and limited to a narrow set of perspectives (e.g., focusing on a single demographic attribute and/or not reporting any analysis on efficiency). This situation makes it challenging for scientists to consciously decide which mitigation procedure better suits their practical setting. In this paper, we investigated the properties a given mitigation procedure against consumer unfairness should be evaluated on, to provide a more holistic view on its effectiveness. We first identified eight technical properties and evaluated the extent to which existing mitigation procedures against consumer unfairness met these properties, qualitatively and quantitatively (when possible), on two public data sets. Then, we outlined the main trends and open issues emerged from our multi-dimensional analysis and provided key practical recommendations for future research.
bibtex: |
  @article{boratto2023practical,
    author = {Boratto, Ludovico and Fenu, Gianni and Marras, Mirko and Medda, Giacomo},
    title = {Practical perspectives of consumer fairness in recommendation},
    journal = {Information Processing \& Management},
    volume = {60},
    number = {2},
    pages = {103208},
    year = {2023},
    doi = {10.1016/j.ipm.2022.103208},
    publisher = {Elsevier}
  }
---

<section class="project-content">
  <h3>Motivation</h3>
  <p>
    Recommender systems have been shown to lead to discriminatory outcomes affecting consumers. While numerous mitigation procedures have been proposed, the experimental protocols used to evaluate them differ fundamentally — varying in fairness definitions, datasets, data splits, and evaluation metrics. This makes it challenging for practitioners to select the most suitable mitigation procedure for their specific setting.
  </p>

  <h3>Eight Technical Properties</h3>
  <p>
    We propose a comprehensive evaluation framework based on eight key properties that any mitigation procedure should be assessed on:
  </p>
  <ul>
    <li><strong>Applicability:</strong> The range of recommendation models the mitigation can be applied to</li>
    <li><strong>Coherence:</strong> Whether the mitigation reduces unfairness without reversing disparities toward other groups</li>
    <li><strong>Consistency:</strong> The stability of category representation between interactions and recommendations</li>
    <li><strong>Data Robustness:</strong> How the mitigation handles data imbalances and popularity biases</li>
    <li><strong>Reproducibility:</strong> Whether the results can be replicated with available code and documentation</li>
    <li><strong>Scalability:</strong> Computational efficiency across different dataset sizes</li>
    <li><strong>Trade-off:</strong> The balance between recommendation utility and fairness improvement</li>
    <li><strong>Transferability:</strong> Performance consistency across different demographic attributes and datasets</li>
  </ul>

  <h3>Experimental Setup</h3>
  <p>
    We evaluated existing mitigation procedures on two public datasets with consumer sensitive attributes:
  </p>
  <ul>
    <li><strong>ML1M:</strong> 6,040 users, 3,952 items, ~1M ratings (Gender: 71.7% M / 28.3% F; Age: 56.6% &lt;35 / 43.4% ≥35)</li>
    <li><strong>LFM1K:</strong> 268 users, 51,609 items, ~200K ratings (Gender: 57.8% M / 42.2% F; Age: 57.8% &lt;25 / 42.2% ≥25)</li>
  </ul>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/practical-perspectives/figure1_consistency.png" alt="Category Equity Score distribution" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 1:</strong> [Consistency] Category equity score (CES) distribution across item categories before (Orig) and after (Mit) applying Burke et al.'s mitigation. The closer to 1, the more similar the category representation between interactions and recommendations.
    </figcaption>
  </figure>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/practical-perspectives/figure2_data_robustness.png" alt="Data Robustness analysis" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 2:</strong> [Data Robustness] User interaction, recommendation, and relevant recommendations drift across item groups formed based on their popularity. Each tick represents a group of 1,000 items with similar popularity.
    </figcaption>
  </figure>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/practical-perspectives/figure3_tradeoff.png" alt="Trade-off analysis" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 3:</strong> [Trade-off] Gain/loss in recommendation utility (NDCG), equity (Demographic Parity), and independence (Kolmogorov-Smirnov) after applying mitigations. Positive NDCG percentages indicate utility gain; negative DP/KS percentages indicate fairness improvement.
    </figcaption>
  </figure>

  <h3>Main Findings</h3>
  <ul>
    <li><strong>Pre-processing approaches show highest applicability:</strong> Data transformation techniques can be applied regardless of the recommendation model</li>
    <li><strong>Trade-offs are unavoidable but manageable:</strong> Most mitigations show some utility loss, but several achieve favorable trade-offs</li>
    <li><strong>Transferability remains challenging:</strong> Mitigations effective for one demographic attribute (e.g., gender) may not transfer to others (e.g., age)</li>
    <li><strong>Reproducibility is a concern:</strong> Many procedures lack publicly available code or sufficient documentation</li>
    <li><strong>Data robustness varies significantly:</strong> Some mitigations amplify popularity biases while reducing demographic unfairness</li>
  </ul>

  <h3>Practical Recommendations</h3>
  <p>
    Based on our multi-dimensional analysis, we provide key recommendations for researchers and practitioners:
  </p>
  <ul>
    <li>Evaluate mitigations across multiple demographic attributes, not just one</li>
    <li>Report both utility and fairness metrics to understand trade-offs</li>
    <li>Consider data characteristics (size, sparsity, imbalance) when selecting mitigations</li>
    <li>Release code and detailed experimental protocols to ensure reproducibility</li>
    <li>Test on multiple datasets to assess transferability</li>
  </ul>
</section>
