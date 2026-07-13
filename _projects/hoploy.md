---
title: "hoploy: a Plugin-Based Inference Layer for Path-Based Explainable Recommendation over Knowledge Graphs"
collection: projects
permalink: /projects/hoploy/
date: 2026-09-01
year: 2026
venue: "20th ACM Conference on Recommender Systems"
venue_short: "RecSys"

# Hero/Banner image (request lifecycle overview)
hero_image: "/images/projects/hoploy/figure1_request_lifecycle.png"
teaser: "/images/projects/hoploy/figure1_request_lifecycle.png"

authors:
  - "Ludovico Boratto"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
  - "Alessio Sechi"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Gianni Fenu: "https://web.unica.it/unica/page/it/gianni_fenu"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Explainable Recommendation
  - Knowledge Graphs
  - Path Reasoning
  - Software Resource
  - Plugin Architecture
  - Inference Serving

# Links
code: "https://github.com/tail-unica/hoploy"

# Abstract
abstract: |
  Path-based reasoning over knowledge graphs is a promising approach for explainable recommendation, as it justifies recommendations through entity-relation paths connecting user preferences to suggested items. However, existing implementations mainly target offline training and evaluation, while interactive deployment requires domain-specific handling of model loading, KG access, decoding, and explanation generation. We present hoploy, an open-source inference and explanation layer for the hopwise ecosystem that exposes pre-trained path-reasoning models through configurable APIs. hoploy supports stateless scenarios where users are unknown at training time and provide preferences only at request time. Its plugin architecture lets developers define request/response schemas, configuration files, and decoding logic that maps KG tokens into human-readable explanations. We release and demonstrate hoploy with POI and food plugins, assess their implementation effort and serving footprint, and provide documentation for extension.

# BibTeX citation
bibtex: |
  @inproceedings{boratto2026hoploy,
    author = {Boratto, Ludovico and Fenu, Gianni and Marras, Mirko and Medda, Giacomo and Sechi, Alessio},
    title = {hoploy: a Plugin-Based Inference Layer for Path-Based Explainable Recommendation over Knowledge Graphs},
    booktitle = {Proceedings of the 20th ACM Conference on Recommender Systems},
    series = {RecSys '26},
    year = {2026},
    publisher = {ACM},
    note = {Resource paper, just accepted}
  }
---

<h2>Motivation</h2>

<p>Personalized recommender systems influence decisions in domains such as media, education, and e-commerce, raising the need for <strong>transparent and accountable</strong> recommendations. <strong>Knowledge graphs (KGs)</strong> provide a natural basis for explainable recommendation because they represent users, items, and domain concepts through typed entities and relations. Among KG-based approaches, <strong>path-based methods</strong> — which construct sequences of entity–relation triples linking users to items — are among the most promising paradigms for explainable recommendation.</p>

<p>Recent path-based approaches include reinforcement-learning agents that navigate a KG under path constraints and autoregressive models that generate reasoning paths token by token. These methods support faithful and interpretable explanations, but existing implementations mainly target <strong>offline training and evaluation</strong>. Frameworks such as <a href="/projects/hopwise/">hopwise</a> have improved reproducibility by providing path sampling utilities, path-based models, and path quality metrics — yet deploying these models in interactive applications remains difficult.</p>

<div class="highlight-box">
<p><strong>The Gap:</strong> This challenge is particularly visible in user-study and prototyping scenarios, where participants are absent from the training set and provide preferences only during the interaction. Without a pre-existing user node, the inference layer must ground request-time preferences into KG entities, run inference, decode reasoning paths, and expose explanations to the downstream application. Building such stateless APIs typically requires <strong>ad hoc integration code</strong> that tightly couples domain semantics, model-specific decoding, and request handling.</p>
</div>

<h2>The hoploy Framework</h2>

<p><strong>hoploy</strong> is an open-source inference and explanation layer for pre-trained path-reasoning models from the <strong>hopwise</strong> library. It does not introduce a new recommendation algorithm; instead, it provides the infrastructure needed to expose existing path-based models in <strong>stateless, API-based settings</strong>. hoploy separates a reusable inference pipeline from application- and model-specific components, letting developers define API schemas, configuration, KG grounding logic, decoding controls, and explanation rendering <em>without modifying the core framework</em>.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/hoploy/figure1_request_lifecycle.png" alt="Overview of the hoploy request lifecycle" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> Overview of the hoploy request lifecycle. Green blocks denote plugin-defined extensions, blue blocks denote framework-controlled inference, and the numbers mark the four operations executed for each request: input distillation, request-specific configuration, path generation, and output expansion.
  </figcaption>
</figure>

<h2>Positioning</h2>

<p>General serving systems expose models through APIs, and recommender frameworks provide training, inference, evaluation, or deployment support. However, none natively cover the full path-based explainable recommendation (XRec) serving workflow: <strong>request-time KG grounding, KG-aware decoding, and explanation rendering</strong>. Conversely, hopwise provides the path-based modeling and evaluation layer, but not an API-oriented serving layer for interactive applications.</p>

<table class="results-table">
<thead>
<tr><th>Framework</th><th>Path-XRec</th><th>KG-aware decoding</th><th>Request handling</th><th>API focus</th></tr>
</thead>
<tbody>
<tr><td>Ray / Ray Serve</td><td>✗</td><td>✗</td><td>Generic</td><td>General distributed serving</td></tr>
<tr><td>TensorFlow-Serving</td><td>✗</td><td>✗</td><td>Generic</td><td>General TensorFlow serving</td></tr>
<tr><td>Cornac-AB</td><td>✗</td><td>✗</td><td>RecSys</td><td>A/B testing</td></tr>
<tr><td>Merlin HugeCTR</td><td>✗</td><td>✗</td><td>RecSys</td><td>RecSys training and inference</td></tr>
<tr><td>TorchEasyRec</td><td>✗</td><td>✗</td><td>RecSys</td><td>RecSys training and serving</td></tr>
<tr><td>hopwise</td><td>✓</td><td>Partial</td><td>Offline</td><td>No serving layer</td></tr>
<tr><td><strong>hoploy (Ours)</strong></td><td><strong>✓</strong></td><td><strong>Full</strong></td><td><strong>XRec</strong></td><td><strong>Path-based XRec</strong></td></tr>
</tbody>
</table>

<h2>Architecture</h2>

<p>hoploy separates a reusable inference workflow from plugin-defined application logic. The <strong>core framework</strong> handles configuration loading, API construction, component validation, model execution, and request orchestration. <strong>Plugins</strong> provide the application-specific elements: request and response schemas, preference mapping, decoding controls, and explanation rendering.</p>

<h3>Configuration and API Binding</h3>

<p>A hoploy application is defined by two configuration levels: a <strong>framework configuration</strong> specifying generic inference behavior, and a <strong>plugin configuration</strong> declaring the components and endpoints required by a target application. The API layer is generated from the plugin specification rather than hard-coded — a plugin declares the request/response schemas for each endpoint together with the component that handles it, and hoploy binds each endpoint to the initialized pipeline. The core framework exposes only infrastructure-level endpoints, keeping the API domain-specific while preserving a shared inference workflow.</p>

<h3>Extension Components</h3>

<ul>
<li><strong>Wrapper (mandatory):</strong> The central component that bridges the application-level API and the model-level representation used by hopwise. It maps incoming requests to model-ready inputs, configures request-specific inference parameters (e.g., path diversity), and expands generated outputs into the application response, including recommended items and human-readable explanations.</li>
<li><strong>Logits processors (optional):</strong> Customize decoding while paths are generated, adjusting candidate-token scores at each step. Following the constrained-decoding paradigm, they enforce request-dependent constraints, promote or penalize entities, or guide generation toward predefined relation patterns. Defaults include graph-valid traversal constraints, masking of previously recommended items, entity restrictions, and relation-pattern forcing.</li>
<li><strong>Sequence processor (optional):</strong> Operates on complete generated paths after candidate paths are produced, enabling operations easier to express over full paths, such as duplicate removal, invalid-sequence filtering, or re-ranking.</li>
<li><strong>Catalog service (shared):</strong> A support service used by wrappers and processors to resolve application-level identifiers into hopwise model tokens, centralizing access to KG and item metadata for both preference mapping and path rendering.</li>
</ul>

<h2>Request Lifecycle</h2>

<p>At startup, hoploy resolves the configured plugins, instantiates their components by role, and validates each implementation against its role-specific interface. This <strong>fail-fast initialization</strong> keeps loaded models, KG mappings, and catalog metadata available across requests. For each recommendation request, hoploy executes four steps:</p>

<ol>
<li><strong>Input distillation:</strong> The wrapper maps the request payload to model-compatible inputs, resolving selected items through the catalog into the representation expected by the hopwise model.</li>
<li><strong>Request-specific configuration:</strong> The wrapper and optional processors derive inference parameters from the request, such as the number of recommendations, the diversity level, or entity restrictions.</li>
<li><strong>Path generation:</strong> The framework runs the underlying hopwise model to produce candidate reasoning paths, while plugin-defined logits and sequence processors can influence decoding or post-process the generated paths.</li>
<li><strong>Output expansion:</strong> The wrapper converts the generated paths back into KG triples, enriches them with catalog metadata, and renders the response — recommendations plus human-readable explanations.</li>
</ol>

<h2>Reference Plugins</h2>

<p>hoploy is demonstrated through two reference plugins that follow the same development workflow but differ in schemas, domain metadata, preference mapping, decoding constraints, and explanation rendering.</p>

<ul>
<li><strong>POI Recommendation:</strong> Targets scenarios where users provide preferred places and sensory aversion levels during an interaction, building on prior work on sensory-aware POI recommendation. After conversion to the hopwise format, the dataset contains 524 entities, ~50k triples, and ~7k interactions between 149 users and 243 POIs. The wrapper resolves place names through the catalog, maps sensory aversions to KG constraints, and renders paths via predefined templates.</li>
<li><strong>Food Recommendation:</strong> Applies the same workflow to recipe recommendation, using the <strong>HUMMUS</strong> KG enriched with <a href="/projects/greenfoodlens/">GreenFoodLens</a> sustainability labels. The converted resource contains ~227k entities, ~1.6M triples, and ~630k interactions between ~23k users and ~66k recipes. Requests include liked food items plus hard and soft restrictions; the wrapper resolves food names and enriches outputs with metadata, while decoding processors exclude or penalize restricted items (e.g., "tomato" as a hard restriction filters out recipes containing that ingredient).</li>
</ul>

<h2>Resource Validation</h2>

<p>The evaluation assesses whether hoploy can be instantiated with limited plugin-specific code and served with a practical deployment footprint — not whether it improves recommendation quality. Both plugins are implemented with a compact amount of code (excluding the core framework), with most effort concentrated in schemas and wrappers, confirming hoploy's role as a lightweight adaptation layer.</p>

<table class="results-table">
<thead>
<tr><th>Plugin</th><th>Total LOC</th><th>Init. time (s)</th><th>Avg. latency (s)</th><th>Peak mem. (GPU / RAM)</th></tr>
</thead>
<tbody>
<tr><td><strong>POI</strong></td><td>648</td><td>50</td><td>0.448 ± 0.090</td><td>0.2 GB / 12 GB</td></tr>
<tr><td><strong>Food</strong></td><td>408</td><td>275</td><td>16.783 ± 3.075</td><td>23 GB / 36 GB</td></tr>
</tbody>
</table>

<p>After initialization, both plugins serve requests suitable for interactive prototypes and user-study settings. The food plugin's longer initialization, higher latency, and larger memory footprint reflect its substantially larger KG and richer metadata, identifying it as the primary target for future serving optimizations.</p>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Inference & explanation layer:</strong> An open-source layer that exposes pre-trained path-reasoning models from hopwise through stateless, configurable APIs.</li>
<li><strong>Plugin abstraction:</strong> A lightweight design that decouples application schemas, KG grounding, decoding controls, and explanation rendering from the core inference workflow.</li>
<li><strong>Repeatable instantiation:</strong> POI and food recommendation plugins that demonstrate the same workflow across domains, with reported KG statistics, plugin-specific implementation effort, and serving footprint.</li>
<li><strong>Bridge to human evaluation:</strong> By exposing path-based explanations through stateless endpoints, hoploy lets researchers embed trained models into surveys and prototypes, collect human feedback, and test whether explanations are meaningful in new domains — complementing the offline evaluation supported by hopwise.</li>
</ul>

<h2>Getting Started</h2>

<p>hoploy and its released POI and food plugins provide executable starting points for extending path-based explainable recommendation to new domains. Full execution traces and request–response examples for both plugins are provided in the repository.</p>

<p>Check the <a href="https://github.com/tail-unica/hoploy" target="_blank">GitHub repository</a> for documentation, examples, and extension guides.</p>
