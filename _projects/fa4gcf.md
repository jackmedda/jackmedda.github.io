---
title: "Fair Augmentation for Graph Collaborative Filtering"
collection: projects
permalink: /projects/fa4gcf/
date: 2024-09-01
year: 2024
venue: "ACM Conference on Recommender Systems"
venue_short: "RecSys"

# hero_image: "/images/projects/fa4gcf/figure_9_page8.png"
# teaser: "/images/projects/fa4gcf/figure_9_page8.png"

authors:
  - "Ludovico Boratto"
  - "Francesco Fabbri"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Francesco Fabbri: "https://francescofabbri.info/"
  Gianni Fenu: "https://people.unica.it/giannifenu/"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Recommender Systems
  - Consumer Fairness
  - Graph Collaborative Filtering
  - Graph Augmentation
  - Fair Transferability

doi: "10.1145/3640457.3688064"
paperurl: "https://doi.org/10.1145/3640457.3688064"
code: "https://github.com/jackmedda/FA4GCF"

abstract: |
  Recent developments in recommendation have harnessed the collaborative power of graph neural networks (GNNs) in learning users' preferences from user-item networks. Despite emerging regulations addressing fairness of automated systems, unfairness issues in graph collaborative filtering remain underexplored, especially from the consumer's perspective. Despite numerous contributions on consumer unfairness, only a few of these works have delved into GNNs. A notable gap exists in the formalization of the latest mitigation algorithms, as well as in their effectiveness and reliability on cutting-edge models. This paper serves as a solid response to recent research highlighting unfairness issues in graph collaborative filtering by reproducing one of the latest mitigation methods. The reproduced technique adjusts the system fairness level by learning a fair graph augmentation. Under an experimental setup based on 11 GNNs, 5 non-GNN models, and 5 real-world networks across diverse domains, our investigation reveals that fair graph augmentation is consistently effective on high-utility models and large datasets. Experiments on the transferability of the fair augmented graph open new issues for future recommendation studies.

bibtex: |
  @inproceedings{boratto2024fair,
    author = {Boratto, Ludovico and Fabbri, Francesco and Fenu, Gianni and Marras, Mirko and Medda, Giacomo},
    title = {Fair Augmentation for Graph Collaborative Filtering},
    booktitle = {Proceedings of the 18th ACM Conference on Recommender Systems},
    series = {RecSys '24},
    year = {2024},
    publisher = {Association for Computing Machinery},
    doi = {10.1145/3640457.3688064}
  }
---

<section id="motivation">
  <h2>Motivation</h2>
  <div class="highlight-box">
    <p>
      <strong>Why study fairness-aware graph augmentation?</strong> Graph Neural Networks (GNNs) have become the 
      state-of-the-art for collaborative filtering. However, unfairness issues in graph collaborative filtering 
      remain underexplored, especially from the consumer's perspective. A notable gap exists in the formalization 
      and evaluation of fairness mitigation algorithms on cutting-edge GNN models.
    </p>
  </div>
  <p>This paper serves as a solid response to recent research highlighting unfairness issues by:</p>
  <ul>
    <li>Reproducing a state-of-the-art fair graph augmentation method</li>
    <li>Evaluating across an extensive setup: 11 GNNs, 5 non-GNN models, 5 real-world networks</li>
    <li>Investigating the transferability of fair augmented graphs to new models</li>
  </ul>
</section>

<section id="method">
  <h2>Approach Overview</h2>
  <p>
    The augmentation process modifies the user-item interaction graph to reduce unfairness disparities between 
    demographic groups. Given a bipartite graph $G = (U, I, E)$ where $U$ is the user set, $I$ is the item set, 
    and $E$ is the edge set representing interactions, the goal is to find an augmented graph $\tilde{G}$ that 
    improves fairness while preserving recommendation quality:
  </p>
  <p style="text-align: center;">
    $$\min_{\tilde{G}} \mathcal{L}_{unfair}(f(\tilde{G})) + \lambda \cdot \mathcal{L}_{utility}(f(\tilde{G}))$$
  </p>
</section>

<section id="experiments">
  <h2>Experimental Setup</h2>
  
  <h3>Datasets</h3>
  <table class="styled-table">
    <thead>
      <tr><th>Dataset</th><th>Users</th><th>Items</th><th>Interactions</th><th>Domain</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>FNYC</strong></td><td>4,832</td><td>5,651</td><td>182,164</td><td>POI (New York)</td></tr>
      <tr><td><strong>FTKY</strong></td><td>7,240</td><td>5,785</td><td>353,847</td><td>POI (Tokyo)</td></tr>
      <tr><td><strong>LF1M</strong></td><td>4,546</td><td>12,492</td><td>1,082,132</td><td>Music</td></tr>
      <tr><td><strong>ML1M</strong></td><td>6,040</td><td>3,706</td><td>1,000,209</td><td>Movies</td></tr>
      <tr><td><strong>RENT</strong></td><td>5,050</td><td>3,397</td><td>43,770</td><td>Fashion</td></tr>
    </tbody>
  </table>
  
  <h3>Models</h3>
  <p>We evaluate <strong>11 GNN-based models</strong> and <strong>5 non-GNN models</strong>:</p>
  <ul>
    <li><strong>GNN Models:</strong> AutoCF, DirectAU, HMLET, LightGCN, NCL, NGCF, SGL, SVD-GCN, SVD-GCN-S, UltraGCN, XSimGCL</li>
    <li><strong>Non-GNN Models:</strong> Traditional collaborative filtering baselines</li>
  </ul>
</section>

<section id="results">
  <h2>Key Results</h2>
  
  <h3>Pre-Analysis: Unfairness in Graph Collaborative Filtering</h3>
  <p>Before applying fairness-aware augmentation, we analyze the overlap between user and item sampling policies across datasets and models.</p>
  
  <!-- 2x3 subplot grid + colorbar for pre-analysis -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin: 1.5rem 0;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1px; flex: 1; max-width: 85%;">
      <img src="/images/projects/fa4gcf/figure_9_page6.png" alt="Pre-analysis top-left" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_7_page6.png" alt="Pre-analysis top-middle" style="width: 78%;">
      <img src="/images/projects/fa4gcf/figure_8_page6.png" alt="Pre-analysis top-right" style="width: 78%;">
      <img src="/images/projects/fa4gcf/figure_6_page6.png" alt="Pre-analysis bottom-left" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_3_page6.png" alt="Pre-analysis bottom-middle" style="width: 78%;">
      <img src="/images/projects/fa4gcf/figure_4_page6.png" alt="Pre-analysis bottom-right" style="width: 78%;">
    </div>
    <div style="flex: 0 0 auto;">
      <img src="/images/projects/fa4gcf/figure_5_page6.png" alt="Colorbar" style="height: 400px; width: auto;">
    </div>
  </div>
  <p class="figure-caption"><strong>Figure 1:</strong> Pre-analysis of policies overlap across datasets and GNN models before applying fair augmentation.</p>
  
  <h3>Main Results</h3>
  <p>Our experiments reveal nuanced findings about fairness-aware augmentation strategies across different settings.</p>

  <h4>RQ2: Comparison across Sampling Policies</h4>
  <p>
    Given that the mitigation procedure successfully mitigated unfairness on HMLET and LightGCN under almost all datasets, 
    we compare the mitigation level of each sampling policy under these models. Larger datasets (LF1M, ML1M) benefit more 
    from the mitigation procedure compared with smaller corpora (FNYC, FTKY). The algorithm is especially effective under ML1M, 
    where Δ was reduced in all settings, regardless of the sampling type.
  </p>
  
  <!-- 2x4 subplot grid + colorbar for policy comparison -->
  <div style="display: flex; align-items: center; justify-content: center; gap: 0.5rem; margin: 1.5rem 0;">
    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 4px; flex: 1; max-width: 90%;">
      <img src="/images/projects/fa4gcf/figure_22_page8.png" alt="LightGCN FNYC" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_16_page8.png" alt="LightGCN FTKY" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_14_page8.png" alt="LightGCN LF1M" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_19_page8.png" alt="LightGCN ML1M" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_21_page8.png" alt="HMLET FNYC" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_20_page8.png" alt="HMLET FTKY" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_11_page8.png" alt="HMLET LF1M" style="width: 85%;">
      <img src="/images/projects/fa4gcf/figure_10_page8.png" alt="HMLET ML1M" style="width: 85%;">
    </div>
    <div style="flex: 0 0 auto;">
      <img src="/images/projects/fa4gcf/figure_18_page8.png" alt="Colorbar" style="height: 400px; width: auto;">
    </div>
  </div>
  <p class="figure-caption"><strong>Figure 2:</strong> Comparison among sampling policies in terms of unfairness mitigation (Δ percentage) across gender groups for LightGCN (top row) and HMLET (bottom row). The first column (row) of each subplot pertains to User-sampling (Item-sampling) settings. Darker cells indicate lower unfairness (better).</p>

  <h4>RQ3: Impact of Ψ on Sampling Policies</h4>
  <p>
    We analyze the impact of ΨU and ΨI parameters on the resulting utility and fairness levels. The combination 
    ⟨ΨU = 35%, ΨI = 20%⟩ outlines a good trade-off across several settings. The subplots delineate a consistent trend 
    where reducing Δ causes NDCG to increase, and vice versa — this trend of inverse proportion is especially prominent 
    when ΨI varies.
  </p>
  
  <!-- Figure 3: Impact of Ψ parameters -->
  <figure style="text-align: center; margin: 2rem 0;">
    <img src="/images/projects/fa4gcf/figure3_complete.png" alt="Impact of Psi parameters on fairness and utility" style="max-width: 100%; border-radius: 8px;">
    <figcaption class="figure-caption" style="margin-top: 0.5rem;">
      <strong>Figure 3:</strong> Impact of varying Ψ<sub>U</sub> and Ψ<sub>I</sub> on fairness (Δ) and utility (NDCG) levels. The gap between NDCG and Δ lines represents the trade-off between fairness and utility.
    </figcaption>
  </figure>

  <h3>Main Findings</h3>
  <ul>
    <li><strong>Effectiveness on high-utility models:</strong> Fair graph augmentation is consistently effective on high-utility GNN models</li>
    <li><strong>Dataset size matters:</strong> The method works better on large datasets</li>
    <li><strong>Transferability challenges:</strong> Experiments on the transferability of fair augmented graphs reveal new issues for future research</li>
    <li><strong>Model-specific effects:</strong> The effectiveness varies across different GNN architectures</li>
  </ul>
</section>
