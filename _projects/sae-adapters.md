---
title: "Sparse Autoencoders as Semantic Domain Adapters for Recommender Systems"
collection: projects
permalink: /projects/sae-adapters/
date: 2026-09-27
year: 2026
venue: "20th ACM Conference on Recommender Systems"
venue_short: "RecSys"

# Hero/Banner image (relative improvement results)
hero_image: "/images/projects/sae-adapters/figure1_improvement.png"
teaser: "/images/projects/sae-adapters/figure1_improvement.png"

authors:
  - "Vojtěch Vančura"
  - "Giacomo Medda"
  - "Martin Spišák"
  - "Ladislav Peška"

author_links:
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Sparse Autoencoders
  - Domain Adaptation
  - Content-Based Filtering
  - Semantic Embeddings
  - Cold-Start Recommendation

# Links
doi: "10.1145/3773078.3841253"
paperurl: "https://doi.org/10.1145/3773078.3841253"
code: "https://github.com/zombak79/sae_adaptors"

# Abstract
abstract: |
  Pretrained text embeddings enable content-based cold-item recommendation, but their domain-agnostic objectives may underrepresent distinctions that matter within a particular recommendation domain. We investigate lightweight autoencoder adapters that specialize these embeddings without retraining or finetuning the embedding model. The autoencoders need no interactional data to train; they merely use the set of items, whose embeddings they aim to reconstruct. We compared denoising, variational, and sparse autoencoder architectures across several embedding models and datasets. While all variants substantially improved over raw embeddings, sparse autoencoders (SAE) dominated in most settings. Qualitative inspection further reveals that some sparse dimensions capture coherent domain-specific concepts, suggesting SAE's capability to meaningfully reorganize general-purpose embeddings. These preliminary findings motivate the inclusion of sparse semantic adaptation as a distinct component of recommender systems.

# BibTeX citation
bibtex: |
  @inproceedings{vancura2026sparse,
    author = {Van\v{c}ura, Vojt\v{e}ch and Medda, Giacomo and Spi\v{s}\'{a}k, Martin and Pe\v{s}ka, Ladislav},
    title = {Sparse Autoencoders as Semantic Domain Adapters for Recommender Systems},
    booktitle = {Proceedings of the 20th ACM Conference on Recommender Systems},
    series = {RecSys '26},
    year = {2026},
    location = {Minneapolis, MN, USA},
    publisher = {ACM},
    doi = {10.1145/3773078.3841253}
  }
---

<h2>Overview</h2>

<p>Recommender systems increasingly rely on off-the-shelf text embedding models (e.g., BGE, Qwen3) for content-based recommendation and cold-start treatment. These embeddings are intentionally optimized for <strong>broad applicability</strong>, so they must represent movies, books, recipes, and countless other concepts at once. Within a single recommendation domain, however, only a narrow subset of those distinctions is relevant — leaving domain-specific signals obscured by noise the embedding was built to carry.</p>

<p>This short paper investigates <strong>sparse autoencoders (SAEs) as unsupervised semantic domain adapters</strong>: lightweight adapters that specialize pretrained embeddings for a given domain <em>without</em> retraining or finetuning the embedding model, and <em>without</em> using any interaction data — the adapter is trained purely by reconstructing item-description embeddings.</p>

<div class="highlight-box">
<p><strong>Key idea:</strong> Adapt the semantic embedding space <em>itself</em> before it reaches the recommender, rather than learning domain-specific transformations from user–item interactions. Interactions are used only for model selection and final evaluation.</p>
</div>

<h2>Approach in Brief</h2>

<p>Each item's textual description is encoded with a frozen embedding model, and an <strong>ℓ1-normalized AbsTop-<em>k</em> SAE</strong> reconstructs those embeddings, keeping only the <em>k</em> largest-magnitude latent activations per item. The resulting normalized sparse code becomes the adapted item representation used for retrieval. A denoising variant (D-SAE) corrupts inputs during training to encourage a more stable semantic structure, and both are compared against dense baselines (a denoising autoencoder and a β-VAE) and the original embeddings.</p>

<h2>Results</h2>

<p>Across 13 datasets (MovieLens20M, GoodBooks10K, and 11 Amazon Reviews'23 categories), 3 embedding models, and 2 metrics — 78 evaluation settings in total — sparse autoencoders outperform both dense alternatives in <strong>70 of 78 settings</strong>. The team observes a consistent progression: DAE improves over the original embeddings, β-VAE over DAE, and the sparse variants over both. Qualitative inspection of individual latent dimensions reveals <strong>coherent domain-specific concepts</strong> (e.g., brake components in Automotive, staplers and sharpeners in Office Products, baby bottles and swaddles in Baby Products), suggesting sparse adaptation reorganizes embeddings into meaningful concepts rather than merely compressing them.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/sae-adapters/figure1_improvement.png" alt="Relative improvement over the unadapted embedding baseline across datasets, embedding models, and metrics" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> Relative improvement over the unadapted embedding baseline across datasets, embedding models (BGE, Qwen3, MiniLM-L6), and metrics (NDCG@20, Recall@20). Values are percentage improvements over the original embeddings (zero line).
  </figcaption>
</figure>

<h2>Takeaway</h2>

<p>These preliminary findings position <strong>semantic adaptation as an independent component</strong> of modern recommender systems rather than a preprocessing afterthought, and suggest that part of the gains attributed to cold-start and semantic-ID methods may stem from domain adaptation of the embedding space itself.</p>

<p>Full results, implementation details, and source code are available in the <a href="https://github.com/zombak79/sae_adaptors" target="_blank">GitHub repository</a>.</p>
