---
title: "Counterfactual Graph Augmentation for Consumer Unfairness Mitigation in Recommender Systems"
collection: projects
permalink: /projects/cga-cfmitigation/
date: 2023-10-21
year: 2023
venue: "32nd ACM International Conference on Information and Knowledge Management"
venue_short: "CIKM 2023"

# Hero/Banner image
hero_image: "/images/projects/cga-cfmitigation/figure1_results.png"
teaser: "/images/projects/cga-cfmitigation/figure1_results.png"

authors:
  - "Ludovico Boratto"
  - "Francesco Fabbri"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Francesco Fabbri: "https://fraboeni.github.io/"
  Gianni Fenu: "https://web.unica.it/unica/page/it/gianni_fenu"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Recommender Systems
  - Fairness
  - Mitigation
  - Explainability
  - GNN
  - Counterfactual Reasoning
  - Graph Augmentation

# Links
doi: "10.1145/3583780.3615165"
paperurl: "https://dl.acm.org/doi/pdf/10.1145/3583780.3615165"
code: "https://github.com/jackmedda/RS-BGExplainer/tree/cikm2023"

# Abstract
abstract: |
  In recommendation literature, explainability and fairness are becoming two prominent perspectives to consider. However, prior works have mostly addressed them separately, for instance by explaining to consumers why a certain item was recommended or mitigating disparate impacts in recommendation utility. None of them has leveraged explainability techniques to inform unfairness mitigation. In this paper, we propose an approach that relies on counterfactual explanations to augment the set of user-item interactions, such that using them while inferring recommendations leads to fairer outcomes. Modeling user-item interactions as a bipartite graph, our approach augments the latter by identifying new user-item edges that not only can explain the original unfairness by design, but can also mitigate it. Experiments on two public data sets show that our approach effectively leads to a better trade-off between fairness and recommendation utility compared with state-of-the-art mitigation procedures. We further analyze the characteristics of added edges to highlight key unfairness patterns.

# BibTeX citation
bibtex: |
  @inproceedings{boratto2023counterfactual,
    author = {Boratto, Ludovico and Fabbri, Francesco and Fenu, Gianni and Marras, Mirko and Medda, Giacomo},
    title = {Counterfactual Graph Augmentation for Consumer Unfairness Mitigation in Recommender Systems},
    booktitle = {Proceedings of the 32nd ACM International Conference on Information and Knowledge Management},
    pages = {3753--3757},
    year = {2023},
    publisher = {ACM},
    doi = {10.1145/3583780.3615165}
  }
---

<h2>Motivation</h2>

<p>Current research in recommender systems is increasingly focusing on <strong>beyond-utility perspectives</strong>, such as explainability and fairness. However, these perspectives are usually considered separately:</p>

<ul>
  <li><strong>Explainability</strong> research has focused on justifying why a certain item was recommended</li>
  <li><strong>Fairness mitigation</strong> methods rely on mathematical formulations but are rarely informed by explanatory analyses</li>
</ul>

<div class="highlight-box">
<p><strong>Key Insight:</strong> We propose the first approach that leverages explainability techniques to <em>inform</em> unfairness mitigation, using counterfactual explanations to identify and add user-item interactions that lead to fairer recommendations.</p>
</div>

<h2>Method Overview</h2>

<p>Our approach augments a user-item interactions graph to counteract <strong>consumer unfairness</strong> across demographic groups. The key idea is to hypothesize a counterfactual world where disadvantaged users benefit from new edges to improve their recommendation utility.</p>

<figure>
  <img src="/images/projects/cga-cfmitigation/figure1_results.png" alt="Mitigation Performance Results" style="width:100%; max-width:800px;">
  <figcaption><strong>Figure 1:</strong> Relative difference in recommendation utility (x-axis) vs utility disparity (y-axis) after applying each method. Our approach (labeled "Ours") consistently achieves the best mitigation while maintaining or improving utility.</figcaption>
</figure>

<h3>Augmentation Mechanism</h3>

<p>We generate an augmented adjacency matrix <strong>Ã</strong> by adding edges to the original matrix <strong>A</strong> through a learned parameter vector. The augmentation is guided by a two-term loss function:</p>

<ul>
  <li><strong>L<sub>fair</sub></strong>: Quantifies fairness using demographic parity, measuring the disparity in NDCG between demographic groups</li>
  <li><strong>L<sub>dist</sub></strong>: Controls the distance between original and augmented graphs to ensure minimal perturbation</li>
</ul>

<h3>Sampling Policies</h3>

<p>To narrow the set of candidate edges, we apply several sampling policies:</p>

<table class="datasets-table">
  <thead>
    <tr>
      <th>Policy</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>BM</strong></td>
      <td>Base</td>
      <td>Base algorithm with no sampling applied</td>
    </tr>
    <tr>
      <td><strong>ZN</strong></td>
      <td>User</td>
      <td>Users with no relevant items in top-k (NDCG@k = 0)</td>
    </tr>
    <tr>
      <td><strong>LD</strong></td>
      <td>User</td>
      <td>Users with fewest interactions (low degree)</td>
    </tr>
    <tr>
      <td><strong>SP</strong></td>
      <td>User</td>
      <td>Users interacting mostly with niche items (sparse)</td>
    </tr>
    <tr>
      <td><strong>FR</strong></td>
      <td>User</td>
      <td>Users furthest from advantaged group in graph distance</td>
    </tr>
    <tr>
      <td><strong>IP</strong></td>
      <td>Item</td>
      <td>Items most preferred by the disadvantaged group</td>
    </tr>
  </tbody>
</table>

<h2>Experimental Setup</h2>

<h3>Datasets</h3>

<table class="datasets-table">
  <thead>
    <tr>
      <th>Dataset</th>
      <th>Attributes</th>
      <th>Advantaged Groups</th>
      <th>Domain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MovieLens 1M</td>
      <td>Gender, Age</td>
      <td>Males (71.7%), Younger (56.6%)</td>
      <td>Movies</td>
    </tr>
    <tr>
      <td>Last.FM 1K</td>
      <td>Gender, Age</td>
      <td>Females (42.2%), Older (42.2%)</td>
      <td>Music</td>
    </tr>
  </tbody>
</table>

<h3>GNN-based Models</h3>

<ul>
  <li><strong>GCMC</strong>: Graph Convolutional Matrix Completion — reconstructs user-item relevance via encoder-decoder architecture</li>
  <li><strong>NGCF</strong>: Neural Graph Collaborative Filtering — propagates embeddings using high-order connectivities</li>
  <li><strong>LightGCN</strong>: Lightweight GCN with only neighborhood aggregation</li>
</ul>

<h2>Key Results</h2>

<h3>Mitigation Performance</h3>

<div class="highlight-box">
<p><strong>Main Finding:</strong> Our approach systematically achieves the best mitigation performance (lowest ΔNDCG) while maintaining or improving recommendation utility across most settings.</p>
</div>

<ul>
  <li>Unlike other methods that decrease utility, our algorithm reports <strong>positive or negligible impact</strong> on recommendation performance</li>
  <li>The <strong>ZN+IP policy combination</strong> achieves -100% unfairness reduction for NGCF on ML-1M gender groups</li>
  <li>Adding interactions to users with <strong>zero NDCG</strong> (ZN policy) consistently improves their recommendation utility</li>
</ul>

<h3>Policy Analysis Insights</h3>

<ul>
  <li>Some policies work consistently regardless of model (<strong>data-level bias</strong>)</li>
  <li>Other policies only work for specific models (<strong>model-dependent bias</strong>)</li>
  <li>The augmentation has <strong>negligible effect on advantaged group utility</strong> — focusing solely on improving the disadvantaged group</li>
</ul>

<h2>Conclusions</h2>

<p>We proposed an augmentation method that leverages explanation techniques to mitigate consumer unfairness in GNN-based recommender systems. Our experiments show:</p>

<ul>
  <li>More reliable unfairness mitigation than state-of-the-art algorithms</li>
  <li>Ability to increase overall recommendation utility</li>
  <li>Confining the algorithm to disadvantaged users with no relevant recommendations positively affects their utility</li>
</ul>

<p><strong>Limitations:</strong> The augmentation had limited impact on deep GNNs (GCMC, NGCF) due to the diminished influence of the graph in the prediction process. Future work will explore new policies, objective functions, and adoption to non-GNN models.</p>
