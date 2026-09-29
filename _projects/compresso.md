---
title: "Compresso: Espresso-Style Sparse Representation Learning for Interpretable Recommender Systems"
collection: projects
permalink: /projects/compresso/
date: 2026-09-27
year: 2026
venue: "20th ACM Conference on Recommender Systems"
venue_short: "RecSys"

# Hero/Banner image (Compresso workflow)
hero_image: "/images/projects/compresso/figure1_workflow.png"
teaser: "/images/projects/compresso/figure1_workflow.png"

authors:
  - "Vojtěch Vančura"
  - "Giacomo Medda"
  - "Martin Spišák"
  - "Ladislav Peška"

author_links:
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Sparse Representations
  - Embedding Compression
  - Interpretability
  - Sparse Autoencoders
  - Recommender Systems
  - PyTorch Framework

# Links
doi: "10.1145/3773078.3841254"
paperurl: "https://doi.org/10.1145/3773078.3841254"
code: "https://github.com/zombak79/compresso"

# Abstract
abstract: |
  Sparse representations can make recommender-system embeddings more compact and inspectable, but developing sparse-learning workflows typically requires substantial engineering around sparsification, training, pruning, storage, and analysis. We present Compresso, an open-source PyTorch framework that exposes this functionality through a simple and modular interface. Inspired by Italian espresso culture, where one orders a caffè while the barista handles the machinery, Compresso lets researchers focus on sparse models rather than infrastructure. The framework provides high-level sparse autoencoder training, reusable sparse tensor representations, differentiable top-k operators, sparse and masked neural parameters, pruning schedules, and composable clustering tools.

# BibTeX citation
bibtex: |
  @inproceedings{vancura2026compresso,
    author = {Van\v{c}ura, Vojt\v{e}ch and Medda, Giacomo and Spi\v{s}\'{a}k, Martin and Pe\v{s}ka, Ladislav},
    title = {Compresso: Espresso-Style Sparse Representation Learning for Interpretable Recommender Systems},
    booktitle = {Proceedings of the 20th ACM Conference on Recommender Systems},
    series = {RecSys '26},
    year = {2026},
    location = {Minneapolis, MN, USA},
    publisher = {ACM},
    doi = {10.1145/3773078.3841254}
  }
---

<h2>Motivation</h2>

<p>Modern recommender systems increasingly rely on <strong>dense</strong> user and item representations for retrieval, ranking, personalization, and semantic matching. These representations capture rich semantic and collaborative information, but they are difficult to inspect, and their storage and computational costs can become substantial at scale. <strong>Sparse representations</strong> offer an alternative: each entity is described by a small set of active features, supporting compression, efficient retrieval, and analysis of recurring semantic or collaborative factors.</p>

<p>Despite growing interest, experimenting with sparse representations still requires substantial supporting infrastructure — sparsification operators, gradient estimators, training and pruning schedules, sparse storage, model integration, persistence, and downstream analysis. As a result, implementations are often tied to individual methods and difficult to adapt or reuse.</p>

<div class="highlight-box">
<p><strong>The Gap:</strong> Existing sparse-representation methods for recommendation target specific applications (compression, retrieval, interpretation), while general sparse-autoencoder libraries mostly serve language- and vision-model activations. Recommender-system libraries, in turn, focus on model training, evaluation, and benchmarking rather than <em>reusable sparse representation learning</em>.</p>
</div>

<h2>The Compresso Framework</h2>

<p><strong>Compresso</strong> is an open-source PyTorch framework for learning, storing, and analyzing fixed-<em>k</em> sparse representations. Its name reflects Italian espresso culture: one orders a caffè, while the barista handles the grinding, brewing, and machinery. Similarly, Compresso lets researchers focus on sparse models and their applications while the framework handles the underlying infrastructure — combining a high-level <code>fit</code>/<code>transform</code> workflow, reusable sparse data structures and PyTorch components, and composable pipelines for clustering and analyzing sparse activation patterns.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/compresso/figure1_workflow.png" alt="Compresso workflow: dense embeddings encoded by a top-k SAE into an SRPTensor, then grouped into interpretable clusters" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> Compresso workflow. A top-<em>k</em> SAE converts dense user or item embeddings into fixed-<em>k</em> sparse representations stored in an <code>SRPTensor</code>. These representations can be persisted, reconstructed, and grouped into interpretable clusters based on shared activations.
  </figcaption>
</figure>

<h2>Design and Architecture</h2>

<p>Compresso's design goal is an "espresso-style" workflow in which dense embeddings become sparse representations — suitable for storage, analysis, and clustering — in only a few lines of code. The high-level workflow centers on a <strong>top-<em>k</em> sparse autoencoder</strong> that maps each dense vector into a latent feature space and retains the <em>k</em> highest-scoring activations. The scoring rule is configurable (sparsification by raw activation or absolute magnitude), and the resulting representations have a predictable storage budget while exposing semantic or collaborative signals across users, items, or contexts.</p>

<h3>Core Objects and API</h3>

<p>The main user-facing API is built around <code>TopKSAETrainer</code>, <code>TopKSAEConfig</code>, and <code>SRPTensor</code>. The trainer follows a familiar scikit-learn-style interface: <code>fit</code> trains the sparse autoencoder on a dense embedding matrix, while <code>transform</code> encodes compatible vectors into the learned sparse latent space. This separation matters in recommendation, where a model trained on an existing catalog or split can subsequently be applied to new items, users, or contexts.</p>

<p>The resulting <strong>SRPTensor</strong> (Sparse Row-Packed — a sparse representation with a fixed number of entries per row) stores active feature indices and values while preserving the logical dense shape. It can be converted to dense or standard sparse tensor formats, persisted, and reused for downstream retrieval, model input, or analysis.</p>

<h3>Advanced Features</h3>

<p>Beyond the high-level autoencoder workflow, Compresso exposes lower-level components for integrating sparsity directly into custom PyTorch models:</p>

<ul>
<li><strong><code>topk_ste</code> / <code>TopKSparsify</code>:</strong> Apply hard top-<em>k</em> selection along a chosen dimension using a <strong>straight-through estimator</strong> for gradient-based optimization.</li>
<li><strong><code>SRPParam</code>:</strong> Represents a row-packed sparse parameter with fixed indices and trainable values, for known sparsity patterns.</li>
<li><strong><code>MaskedParam</code>:</strong> Pairs dense weights with scheduled binary masks for progressive row-wise pruning, when the sparse structure must be discovered during training.</li>
<li><strong><code>SparsityController</code>:</strong> Manages mask updates and optional weight rewinding.</li>
</ul>

<p>Together, these components support both explicitly sparse parameters and gradual dense-to-sparse training, without reimplementing sparsification, pruning, or sparse storage.</p>

<h3>Clustering and Analysis</h3>

<p>Compresso treats sparse representations not only as compressed model inputs but also as objects for analysis. Entities that activate similar sparse features may share product categories, semantic themes, visual properties, user preferences, or collaborative signals. The <strong><code>ClusteringPipeline</code></strong> captures this structure through composable steps for clustering, linking, merging, pruning, filtering, and labeling activation patterns. Clusters can be initialized from dominant signed features, feature combinations, or representation similarity, and labeled from entity metadata or user-defined labeling functions — giving practitioners an inspectable view of which sparse factors characterize a cluster and which users or items activate them.</p>

<h2>Online Demonstration</h2>

<p>The interactive demo presents Compresso end-to-end: dense product metadata is embedded and encoded with a top-<em>k</em> sparse autoencoder, products sharing activation patterns are grouped into clusters, and the resulting groups are shown as labeled clusters of representative items. A methodology page exposes the code used for embedding preparation, sparse encoding, clustering, and labeling, while domain pages present clusters for several Amazon product categories (automotive, baby products, grocery and gourmet food, and more).</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/compresso/figure2_demo.png" alt="Compresso online demo showing SAE training code alongside browsable product clusters" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 2:</strong> Compresso online demo for the Amazon Clothing, Shoes and Jewelry domain. <em>Left:</em> source code for SAE training and running the clustering pipeline. <em>Right:</em> the interface for browsing product clusters, inspecting latent-factor details, and adjusting the number of displayed clusters and representative products. Each row is a cluster induced by shared sparse activation patterns.
  </figcaption>
</figure>

<p>Each cluster contains representative products together with its latent-factor identifier and activation direction. Users can vary the number of displayed clusters and products, inspect individual sparse factors, and trace results back to the corresponding pipeline code — connecting sparse activation patterns with recognizable product categories, semantic themes, and visual similarities.</p>

<div class="highlight-box">
<p><strong>Try it live:</strong> the online demo is available at <a href="https://compreapp-demo.streamlit.app/" target="_blank">compreapp-demo.streamlit.app</a>.</p>
</div>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Espresso-style sparse learning:</strong> An open-source PyTorch framework that hides the infrastructure of sparsification, training, pruning, storage, and analysis behind a simple <code>fit</code>/<code>transform</code> interface.</li>
<li><strong>Reusable sparse building blocks:</strong> Fixed-<em>k</em> SAEs, the <code>SRPTensor</code> representation, differentiable top-<em>k</em> operators, and sparse/masked parameters that drop into custom PyTorch models.</li>
<li><strong>Interpretability by design:</strong> A composable <code>ClusteringPipeline</code> that organizes recurring activation patterns into inspectable, labeled clusters for studying semantic and collaborative structure.</li>
<li><strong>End-to-end demonstration:</strong> An interactive demo over real Amazon product domains that links sparse factors to recognizable clusters and the code that produced them.</li>
</ul>

<h2>Getting Started</h2>

<p>Compresso is available on PyPI as <a href="https://pypi.org/project/compresso-pytorch/" target="_blank"><code>compresso-pytorch</code></a>, with source code, installation instructions, and complete examples in the <a href="https://github.com/zombak79/compresso" target="_blank">GitHub repository</a>.</p>
