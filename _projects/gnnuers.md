---
title: "GNNUERS: Fairness Explanation in GNNs for Recommendation via Counterfactual Reasoning"
collection: projects
permalink: /projects/gnnuers/
date: 2024-12-26
year: 2024
venue: "ACM Transactions on Intelligent Systems and Technology"
venue_short: "TIST"

# Hero/Banner image (architecture diagram from the paper)
hero_image: "/images/projects/gnnuers/figure_1_page9.png"
teaser: "/images/projects/gnnuers/figure_1_page9.png"

authors:
  - "Giacomo Medda"
  - "Francesco Fabbri"
  - "Mirko Marras"
  - "Ludovico Boratto"
  - "Gianni Fenu"

author_links:
  Giacomo Medda: "https://jackmedda.github.io"
  Francesco Fabbri: "https://scholar.google.com/citations?user=bP5bQJAAAAAJ"
  Mirko Marras: "https://scholar.google.com/citations?user=Cl2L9Q0AAAAJ"
  Ludovico Boratto: "https://scholar.google.com/citations?user=1unjC10AAAAJ"
  Gianni Fenu: "https://scholar.google.com/citations?user=rP3KMr8AAAAJ"

keywords:
  - Recommender Systems
  - User Fairness
  - Explainability
  - Graph Neural Networks
  - Counterfactual Reasoning
  - Algorithmic Fairness

# Links
doi: "10.1145/3655631"
paperurl: "https://dl.acm.org/doi/pdf/10.1145/3655631"
code: "https://github.com/jackmedda/RS-BGExplainer"

# Abstract
abstract: |
  Nowadays, research into personalization has been focusing on explainability and fairness. Several approaches proposed in recent works are able to explain individual recommendations in a post-hoc manner or by explanation paths. However, explainability techniques applied to unfairness in recommendation have been limited to finding user/item features mostly related to biased recommendations. In this article, we devised a novel algorithm that leverages counterfactuality methods to discover user unfairness explanations in the form of user-item interactions. In our counterfactual framework, interactions are represented as edges in a bipartite graph, with users and items as nodes. Our bipartite graph explainer perturbs the topological structure to find an altered version that minimizes the disparity in utility between the protected and unprotected demographic groups. Experiments on four real-world graphs coming from various domains showed that our method can systematically explain user unfairness on three state-of-the-art GNN-based recommendation models. Moreover, an empirical evaluation of the perturbed network uncovered relevant patterns that justify the nature of the unfairness discovered by the generated explanations.

# BibTeX citation
bibtex: |
  @article{medda2024gnnuers,
    author = {Medda, Giacomo and Fabbri, Francesco and Marras, Mirko and Boratto, Ludovico and Fenu, Gianni},
    title = {GNNUERS: Fairness Explanation in GNNs for Recommendation via Counterfactual Reasoning},
    journal = {ACM Transactions on Intelligent Systems and Technology},
    volume = {16},
    number = {1},
    articleno = {6},
    year = {2024},
    publisher = {ACM},
    doi = {10.1145/3655631},
    url = {https://doi.org/10.1145/3655631}
  }
---

<h2>Motivation</h2>

<p>Modern recommender systems have become highly effective but increasingly complex, raising concerns about <strong>trustworthiness</strong>, <strong>fairness</strong>, and <strong>explainability</strong>. While algorithmic fairness ensures equitable recommendations across demographic groups, understanding <em>why</em> a model is unfair remains a central yet under-explored challenge.</p>

<div class="highlight-box">
<p><strong>Key Insight:</strong> Existing approaches explain unfairness through user/item features, but these may not always be available. GNNUERS explains unfairness directly through user-item interactions — the fundamental data source for collaborative filtering models.</p>
</div>

<h2>Method Overview</h2>

<p><strong>GNNUERS</strong> (GNN-based Unfairness Explainer in Recommender Systems) is a framework that:</p>

<ol>
<li><strong>Represents interactions as a bipartite graph</strong> with users and items as nodes, and interactions as edges</li>
<li><strong>Perturbs the topological structure</strong> to identify edges (interactions) causing unfairness</li>
<li><strong>Minimizes demographic disparity</strong> while constraining the number of perturbed edges</li>
</ol>

<h3>Counterfactual Explanation</h3>

<p>The core idea is <strong>counterfactual reasoning</strong>: we ask <em>"What if certain users had not interacted with certain items?"</em> By finding the minimal set of edges whose removal reduces unfairness, we explain which interactions caused the disparity.</p>

<p><strong>Formal Definition:</strong> A counterfactual explanation $\tilde{E}$ is a subset of edges such that when removed from the adjacency matrix $A$, the resulting fairness metric $\Phi(f(\tilde{A})) < \Phi(f(A))$.</p>

<h3>Loss Function</h3>

<p>The optimization is guided by:</p>

<div class="equation" style="text-align: center; padding: 1rem; background: #f8fafc; border-radius: 8px; margin: 1rem 0;">
$$\mathcal{L}(A, \tilde{A}) = \mathcal{L}_{\text{fair}}(A, f(\tilde{A}; W)) + \mathcal{L}_{\text{dist}}(A, \tilde{A})$$
</div>

<p>Where:</p>
<ul>
<li>$\mathcal{L}_{\text{fair}}$: Minimizes the demographic parity gap (NDCG disparity between groups)</li>
<li>$\mathcal{L}_{\text{dist}}$: Constrains the number of perturbed edges</li>
</ul>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Novel Framework:</strong> First method to explain unfairness in GNN-based recommender systems via counterfactual edge perturbation</li>
<li><strong>Memory Efficient:</strong> Uses a perturbation vector instead of a matrix, storing values only for existing edges</li>
<li><strong>Gradient Deactivation:</strong> Focuses perturbation on the unprotected group to identify edges advantaging them</li>
<li><strong>Graph Property Analysis:</strong> Categorizes explanations through degree, density, and intra-group distance metrics</li>
</ul>

<h2>Experimental Setup</h2>

<h3>Datasets</h3>

<table class="results-table">
<thead>
<tr><th>Dataset</th><th>Domain</th><th>Users</th><th>Items</th><th>Interactions</th></tr>
</thead>
<tbody>
<tr><td><strong>ML-1M</strong></td><td>Movies</td><td>6,040</td><td>3,706</td><td>1,000,209</td></tr>
<tr><td><strong>LFM-1K</strong></td><td>Music</td><td>268</td><td>51,609</td><td>200,586</td></tr>
<tr><td><strong>Ta Feng</strong></td><td>Grocery</td><td>25,741</td><td>23,643</td><td>708,919</td></tr>
<tr><td><strong>Insurance</strong></td><td>Insurance</td><td>346</td><td>20</td><td>1,879</td></tr>
</tbody>
</table>

<h3>GNN Models</h3>

<ul>
<li><strong>GCMC</strong> - Graph Convolutional Matrix Completion</li>
<li><strong>NGCF</strong> - Neural Graph Collaborative Filtering</li>
<li><strong>LightGCN</strong> - Simplified GCN for recommendation</li>
</ul>

<h2>Key Results</h2>

<h3>Unfairness Reduction</h3>

<p>GNNUERS significantly reduces the NDCG disparity (ΔNDCG) between demographic groups:</p>

<ul>
<li><strong>ML-1M &amp; FENG:</strong> Achieves significant fairness improvement by perturbing only ~1% of edges</li>
<li><strong>Systematic explanations:</strong> Works across different models and sensitive attributes (age/gender)</li>
<li><strong>Minimal utility loss:</strong> Protected group utility is preserved while reducing unfairness</li>
</ul>

<h3>Pattern Discovery</h3>

<p>Through graph property analysis, GNNUERS reveals:</p>

<ul>
<li><strong>Over-representation effects:</strong> Unfairness often stems from larger/more active demographic groups</li>
<li><strong>Popularity bias connection:</strong> High-density users (consuming popular items) contribute to unfairness</li>
<li><strong>Isolation patterns:</strong> Low-IGD (isolated) users' interactions can significantly impact fairness</li>
</ul>

<h2>Experimental Results</h2>

<div class="results-gallery">
  <figure class="result-figure">
    <img src="/images/projects/gnnuers/figure_2_page16.png" alt="GNNUERS fairness improvement results across datasets" loading="lazy">
    <figcaption><strong>Figure 2:</strong> Fairness improvement (ΔNDCG reduction) achieved by GNNUERS across different datasets and GNN models. The method consistently reduces demographic disparity while maintaining recommendation quality.</figcaption>
  </figure>
  
  <figure class="result-figure">
    <img src="/images/projects/gnnuers/figure_3_page18.png" alt="Graph property analysis of perturbed edges" loading="lazy">
    <figcaption><strong>Figure 3:</strong> Analysis of perturbed edges through graph topological properties. The distribution reveals patterns in how unfairness manifests through user-item interactions.</figcaption>
  </figure>
</div>

<div class="results-gallery two-col">
  <figure class="result-figure">
    <img src="/images/projects/gnnuers/figure_4_page20.jpeg" alt="Detailed analysis on ML-1M dataset" loading="lazy">
    <figcaption><strong>Figure 4:</strong> Detailed edge perturbation analysis on ML-1M, showing the relationship between graph metrics and contribution to unfairness.</figcaption>
  </figure>
  
  <figure class="result-figure">
    <img src="/images/projects/gnnuers/figure_5_page21.jpeg" alt="Sensitivity analysis results" loading="lazy">
    <figcaption><strong>Figure 5:</strong> Detailed edge perturbation analysis on LFM-1K, showing the relationship between graph metrics and contribution to unfairness.</figcaption>
  </figure>
</div>

<h2>Graph Properties for Explanation</h2>

<p>We analyze perturbed edges through three topological properties:</p>

<table class="results-table">
<thead>
<tr><th>Property</th><th>Definition</th><th>Insight</th></tr>
</thead>
<tbody>
<tr><td><strong>Degree (DEG)</strong></td><td>Number of edges per node</td><td>User activity / Item popularity</td></tr>
<tr><td><strong>Density (DY)</strong></td><td>Tendency to connect to high-degree nodes</td><td>Popularity bias</td></tr>
<tr><td><strong>Intra-Group Distance (IGD)</strong></td><td>Closeness to same-type nodes</td><td>Community structure</td></tr>
</tbody>
</table>

<h2>Implications</h2>

<p>GNNUERS enables system designers and service providers to:</p>

<ol>
<li><strong>Understand unfairness sources</strong> at the interaction level</li>
<li><strong>Design informed mitigation strategies</strong> based on discovered patterns</li>
<li><strong>Audit recommendation systems</strong> for demographic disparities</li>
<li><strong>Balance fairness and utility</strong> with minimal perturbation</li>
</ol>

<h2>Resources</h2>

<div class="project-links" style="justify-content: flex-start; margin-top: 1rem;">
  <a href="https://github.com/jackmedda/RS-BGExplainer" target="_blank" class="project-btn">
    <i class="fab fa-github"></i> Code &amp; Data
  </a>
  <a href="https://dl.acm.org/doi/10.1145/3655631" target="_blank" class="project-btn">
    <i class="fas fa-file-pdf"></i> Full Paper
  </a>
</div>
