---
title: "Consumer Fairness in Recommender Systems: Contextualizing Definitions and Mitigations"
slug: "consumer-fairness-recsys"
layout: project-page
date: 2022-04-08
excerpt: "A systematic analysis of mitigation procedures against consumer unfairness in recommender systems."

hero_image: "/images/projects/consumer-fairness-recsys/figure1_method.png"

authors:
  - "Ludovico Boratto"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
author_links:
  "Ludovico Boratto": "https://www.ludovicoboratto.com/"
  "Mirko Marras": "https://www.mirkomarras.com/"
venue: "46th European Conference on IR Research (ECIR 2022)"
keywords:
  - Recommender Systems
  - Fairness
  - Bias
  - Consumers
doi: "10.1007/978-3-030-99736-6_37"
paperurl: "https://doi.org/10.1007/978-3-030-99736-6_37"
code: "https://github.com/jackmedda/C-Fairness-RecSys"
abstract: |
  Enabling non-discrimination for end-users of recommender systems by introducing consumer fairness is a key problem, widely studied in both academia and industry. Current research has led to a variety of notions, metrics, and unfairness mitigation procedures. The evaluation of each procedure has been heterogeneous and limited to a mere comparison with models not accounting for fairness. It is hence hard to contextualize the impact of each mitigation procedure w.r.t. the others. In this paper, we conduct a systematic analysis of mitigation procedures against consumer unfairness in rating prediction and top-n recommendation tasks. To this end, we collected 15 procedures proposed in recent top-tier conferences and journals. Only 8 of them could be reproduced. Under a common evaluation protocol, based on two public data sets, we then studied the extent to which recommendation utility and consumer fairness are impacted by these procedures, the interplay between two primary fairness notions based on equity and independence, and the demographic groups harmed by the disparate impact. Our study finally highlights open challenges and future directions in this field.
bibtex: |
  @inproceedings{boratto2022consumer,
    author = {Boratto, Ludovico and Fenu, Gianni and Marras, Mirko and Medda, Giacomo},
    title = {Consumer Fairness in Recommender Systems: Contextualizing Definitions and Mitigations},
    booktitle = {Advances in Information Retrieval - 44th European Conference on IR Research, ECIR 2022},
    pages = {552--566},
    year = {2022},
    doi = {10.1007/978-3-030-99736-6_37},
    publisher = {Springer}
  }
---

<section class="project-content">
  <h3>Motivation</h3>
  <p>
    Recommender systems help us make decisions in various domains, from selecting books to choosing friends. However, their wide adoption has spurred investigations into possibly unfair practices. Group consumer fairness should account for no disparate impact of recommendations on protected groups of consumers, but current research has led to heterogeneous evaluation protocols that make it hard to compare different mitigation approaches.
  </p>

  <h3>Research Questions</h3>
  <ul>
    <li><strong>RQ1:</strong> Is recommendation utility affected by the mitigation procedures?</li>
    <li><strong>RQ2:</strong> Do the selected mitigation procedures reduce the unfairness estimates?</li>
    <li><strong>RQ3:</strong> Is disparate impact systematically harming the minority group?</li>
  </ul>

  <h3>Methodology</h3>
  <p>
    We conducted a systematic study on algorithmic procedures for mitigating consumer unfairness. We scanned proceedings of top-tier conferences and journals (ACM, Elsevier, IEEE, Springer), identifying 15 relevant papers. Only 8 of them could be reproduced with working source code.
  </p>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/consumer-fairness-recsys/figure1_method.png" alt="Systematic methodology for collecting and evaluating mitigation procedures" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 1:</strong> Method. We systematically collected papers and retrieved their source code.
    </figcaption>
  </figure>

  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/consumer-fairness-recsys/table1_procedures.png" alt="Overview of the 8 reproducible mitigation procedures" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Table 1:</strong> Overview of the mitigation procedures whose source code could be retrieved.
    </figcaption>
  </figure>

  <h3>Experimental Setup</h3>
  <p>
    We defined a common evaluation protocol using:
  </p>
  <ul>
    <li><strong>Datasets:</strong> MovieLens 1M and LastFM 1K</li>
    <li><strong>Sensitive attributes:</strong> Gender and Age</li>
    <li><strong>Fairness notions:</strong> Equity (NDCG Demographic Parity) and Independence (Kolmogorov-Smirnov test)</li>
  </ul>

  <h3>Main Findings</h3>
  <ul>
    <li><strong>Utility impact is often negligible (RQ1):</strong> Mitigation procedures did not consistently reduce the utility of recommendations</li>
    <li><strong>Unfairness reduction is inconsistent (RQ2):</strong> Only a minor subset of procedures substantially reduce unfairness, and rarely for both equity and independence notions simultaneously</li>
    <li><strong>Disparate impact doesn't always harm minorities (RQ3):</strong> The minority group was actually advantaged in some settings (e.g., LFM 1K for both attributes in top-n recommendation)</li>
    <li><strong>Reproducibility is challenging:</strong> Only 8 out of 15 papers could be reproduced, highlighting the need for better code sharing practices</li>
  </ul>

  <h3>Open Challenges</h3>
  <ul>
    <li><strong>Reproducibility:</strong> Code modularity should be improved to easily accommodate different datasets</li>
    <li><strong>Optimization:</strong> Mitigating unfairness adds hyper-parameters and requires dealing with trade-offs between utility and fairness</li>
    <li><strong>Comparability:</strong> Despite using similar datasets, evaluation settings are often different across papers</li>
    <li><strong>Impact:</strong> Depending on the model, dataset, and task, mitigation procedures do not always substantially reduce unfairness</li>
  </ul>
</section>
