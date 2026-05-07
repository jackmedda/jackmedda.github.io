---
title: "hopwise: A Python Library for Explainable Recommendation based on Path Reasoning over Knowledge Graphs"
collection: projects
permalink: /projects/hopwise/
date: 2025-11-10
year: 2025
venue: "34th ACM International Conference on Information and Knowledge Management"
venue_short: "CIKM"

# Hero/Banner image (framework architecture)
hero_image: "/images/projects/hopwise/figure1_framework.png"
teaser: "/images/projects/hopwise/figure1_framework.png"

authors:
  - "Ludovico Boratto"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
  - "Alessandro Soccol"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Gianni Fenu: "https://web.unica.it/unica/page/it/gianni_fenu"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io"
  Alessandro Soccol: "https://alessandrosocc.github.io/"

keywords:
  - Recommender Systems
  - Explainability
  - Knowledge Graphs
  - Path Reasoning
  - Reproducibility
  - Transparency

# Links
doi: "10.1145/3746252.3761641"
paperurl: "https://dl.acm.org/doi/10.1145/3746252.3761641"
code: "https://github.com/tail-unica/hopwise"

# Abstract
abstract: |
  Explainability is becoming central to the development of responsible recommender systems, especially as path reasoning over knowledge graphs saw increased adoption for extracting structured, semantic user-item connections. However, reproducible research in such field remains limited due to fragmented implementations, missing utilities, and the lack of standardized evaluation pipelines. In this paper, we propose hopwise, an open-source library that supports the full life-cycle of explainable path reasoning recommendation methods over knowledge graphs, from knowledge graph preparation to explanation path delivery and evaluation. Rather than creating a new library from scratch, hopwise builds upon the modular and widely adopted RecBole ecosystem, enriching it with more knowledge graphs, path sampling utilities, path reasoning methods, and metrics for evaluating explanation path utility, coverage, and diversity. We show the framework's utility by means of a benchmark including two knowledge graphs and several recommendation methods.

# BibTeX citation
bibtex: |
  @inproceedings{boratto2025hopwise,
    author = {Boratto, Ludovico and Fenu, Gianni and Marras, Mirko and Medda, Giacomo and Soccol, Alessandro},
    title = {hopwise: A Python Library for Explainable Recommendation based on Path Reasoning over Knowledge Graphs},
    booktitle = {Proceedings of the 34th ACM International Conference on Information and Knowledge Management},
    series = {CIKM '25},
    year = {2025},
    location = {Seoul, Republic of Korea},
    publisher = {ACM},
    doi = {10.1145/3746252.3761641},
    url = {https://doi.org/10.1145/3746252.3761641}
  }
---

<h2>Motivation</h2>

<p>Personalized recommender systems have become essential in helping users navigate complex decision spaces, from media consumption to food choices and educational pathways. As these systems influence several aspects of daily life, the demand for <strong>transparency</strong> and <strong>accountability</strong> has grown significantly.</p>

<p><strong>Knowledge graphs (KGs)</strong> have emerged as a powerful foundation for enhancing recommender systems with structured, semantic connections between users and items. Path-based reasoning over KGs enables generating <strong>human-interpretable explanations</strong> that trace the reasoning from user to recommended item.</p>

<div class="highlight-box">
<p><strong>The Problem:</strong> Despite the growing interest in explainable path reasoning, reproducible research remains limited due to fragmented implementations, missing utilities, and the lack of standardized evaluation pipelines. No existing library comprehensively supports diverse KG topologies, path-based models, and a unified evaluation of explanations.</p>
</div>

<h2>The hopwise Framework</h2>

<p><strong>hopwise</strong> is an open-source library that supports the full life-cycle of explainable path reasoning recommendation methods over knowledge graphs. Rather than building from scratch, it extends the widely adopted <strong>RecBole</strong> ecosystem to ensure compatibility and promote adoption.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/hopwise/figure1_framework.png" alt="hopwise framework architecture" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> The hopwise framework: new functionalities in salmon, datasets utilities in green, abstraction layers in blue, env utils in yellow, metrics type in orange, models in violet.
  </figcaption>
</figure>

<h3>Key Components</h3>

<ul>
<li><strong>Data and Configuration Management:</strong> Dataset preprocessing, checkpointing, and hyperparameter search integration with Optuna, Ray, and Hyperopt</li>
<li><strong>Graph Path Sampling:</strong> Utilities for sampling and validating explanation paths from knowledge graphs</li>
<li><strong>Model Interface:</strong> Support for general, sequential, knowledge-aware, context-aware, and path reasoning recommenders</li>
<li><strong>Evaluation Pipeline:</strong> Unified evaluation of utility, beyond-accuracy goals, and path quality metrics</li>
<li><strong>Explanation Visualization:</strong> Tools for visualizing and analyzing generated explanation paths</li>
</ul>

<h2>Supported Models</h2>

<p>hopwise supports a comprehensive suite of models for both link prediction and recommendation tasks:</p>

<ul>
<li><strong>Knowledge Graph Embeddings:</strong> TransE, TransH, TransR, DistMult, ComplEx, RotatE, TuckER, ConvE, HolE, AnalogE, RESCAL</li>
<li><strong>Path Reasoning Models:</strong> PLM, KGAT, PGPR, CAFE, and other path-based methods</li>
<li><strong>Explainability Interface:</strong> Each path-based model implements an <code>explain()</code> function to generate {user, item, score, path} quadruples</li>
</ul>

<h2>Evaluation Metrics</h2>

<p>hopwise extends RecBole's evaluation with novel beyond-utility metrics focused on explanation quality:</p>

<h3>Perceived Usefulness</h3>
<ul>
<li><strong>Serendipity (SER):</strong> Level of unexpectedness and relevance of recommendations</li>
<li><strong>Novelty (NOV):</strong> Inverse popularity of recommended items</li>
</ul>

<h3>Consumer Fairness</h3>
<ul>
<li><strong>Utility Disparity (ΔS):</strong> Absolute difference in utility between consumer groups</li>
</ul>

<h3>Explanation Path Quality</h3>
<ul>
<li><strong>Fidelity (FID):</strong> Percentage of recommended items that can be explained</li>
<li><strong>Linking Interaction Recency (LIR):</strong> Recency of past interactions in explanation paths</li>
<li><strong>Linking Interaction Diversity (LID):</strong> Diversity of past interactions in paths</li>
<li><strong>Shared Entity Popularity (SEP):</strong> Popularity of shared entities in paths</li>
<li><strong>Shared Entity Diversity (SED):</strong> Diversity of shared entities in paths</li>
<li><strong>Path Type Diversity (PTD):</strong> Percentage of distinct path types within explanations</li>
<li><strong>Path Type Concentration (PTC):</strong> Balance in representation of distinct path types</li>
</ul>

<h2>Supported Datasets</h2>

<table class="results-table">
<thead>
<tr><th>Dataset</th><th>Users</th><th>Items</th><th>Interactions</th><th>KG Entities</th><th>KG Triples</th></tr>
</thead>
<tbody>
<tr><td><strong>ML1M</strong></td><td>6,040</td><td>2,984</td><td>932,295</td><td>13,804</td><td>193,089</td></tr>
<tr><td><strong>LFM1M</strong></td><td>4,817</td><td>12,492</td><td>1,091,275</td><td>17,492</td><td>219,084</td></tr>
<tr><td><strong>Alibaba Fashion</strong></td><td>141,738</td><td>30,041</td><td>1,781,093</td><td>89,197</td><td>279,155</td></tr>
<tr><td><strong>YELP</strong></td><td>45,920</td><td>45,539</td><td>1,183,610</td><td>136,500</td><td>1,853,704</td></tr>
</tbody>
</table>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Unified Framework:</strong> First comprehensive library supporting the full life-cycle of explainable path reasoning recommendation</li>
<li><strong>RecBole Integration:</strong> Built on top of the widely adopted RecBole ecosystem for compatibility and ease of adoption</li>
<li><strong>Path Quality Metrics:</strong> Novel evaluation standards for assessing explanation path utility, coverage, and diversity</li>
<li><strong>Standardized Interface:</strong> Clean API for implementing new path-based models with explanation generation</li>
<li><strong>Reproducibility:</strong> Checkpointing, data split saving, and configuration management for reproducible experiments</li>
</ul>

<h2>Comparison with Existing Libraries</h2>

<p>hopwise fills a gap in the recommendation library landscape by combining:</p>

<ul>
<li>Link prediction task support</li>
<li>Beyond-utility metrics</li>
<li>Path-based explainability</li>
<li>Path quality metrics</li>
<li>Full usability features (checkpoints, data loaders, config management)</li>
</ul>

<p>Unlike XRecSys, the only other library with path-based techniques, hopwise offers a modular design that enables extensibility and includes features like saving data splits and resuming from checkpoints.</p>

<h2>Getting Started</h2>

<p>Install hopwise and start building explainable recommender systems:</p>

<pre><code>pip install hopwise
# or clone from GitHub
git clone https://github.com/tail-unica/hopwise
</code></pre>

<p>Check the <a href="https://github.com/tail-unica/hopwise" target="_blank">GitHub repository</a> for documentation, examples, and tutorials.</p>
