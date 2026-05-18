---
title: "Evaluating the Role of Context Representations in the Behavioral Fidelity of LLM-based Personas for Food Preferences"
collection: projects
permalink: /projects/llm-food-persona/
date: 2026-06-08
year: 2026
venue: "34th ACM Conference on User Modeling, Adaptation and Personalization"
venue_short: "ACM UMAP"

# Hero/Banner image (two-stage pipeline)
hero_image: "/images/projects/llm-food-persona/figure1_pipeline.png"
teaser: "/images/projects/llm-food-persona/figure1_pipeline.png"

authors:
  - "Eleonora Balloccu"
  - "Ludovico Boratto"
  - "Angelo Geninatti Cossatin"
  - "Mirko Marras"
  - "Noemi Mauro"
  - "Giacomo Medda"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Angelo Geninatti Cossatin: "https://www.researchgate.net/profile/Angelo-Geninatti-Cossatin"
  Mirko Marras: "https://www.mirkomarras.com/"
  Noemi Mauro: "https://noemi-mauro.github.io/"
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Preference Modeling
  - Language Models
  - User Simulation
  - LLM-based Personas
  - Food Recommendation
  - Behavioral Fidelity

# Links
# doi: "10.1145/3774935.3806159"
# paperurl: "https://doi.org/10.1145/3774935.3806159"
code: "https://github.com/tail-unica/food-digital-twin"

# Abstract
abstract: |
  Recent work has increasingly relied on LLM-based personas to reason about food preferences, yet the information used to condition these personas is often unstructured, inconsistently represented, or weakly validated. This observation naturally leads to ask whether, and to what extent, LLM-based personas respond to more structured user context representations inspired by those typically adopted in nutritional practice. In this paper, we hence study the role of context representations in the food domain by comparing three forms of context (unstructured, structured, and hybrid) when conditioning LLM-based personas. We evaluate behavioral fidelity by comparing simulated ratings and generated reviews against real user data. Our results show that unstructured text better preserves rating intensity, structured traits alone do not capture preferences well, and hybrid representations yield the most faithful simulations.

# BibTeX citation
bibtex: |
  @inproceedings{balloccu2026evaluating,
    author = {Balloccu, Eleonora and Boratto, Ludovico and Geninatti Cossatin, Angelo and Marras, Mirko and Mauro, Noemi and Medda, Giacomo},
    title = {Evaluating the Role of Context Representations in the Behavioral Fidelity of LLM-based Personas for Food Preferences},
    booktitle = {Proceedings of the 34th ACM Conference on User Modeling, Adaptation and Personalization},
    series = {UMAP '26},
    year = {2026},
    location = {Gothenburg, Sweden},
    publisher = {ACM},
    doi = {10.1145/3774935.3806159}
  }
---

<h2>Motivation</h2>

<p>LLM-based personas have become a popular tool for simulating user behavior, particularly in domains such as food recommendation where collecting real preference data is costly. However, the information used to condition these personas is often <strong>unstructured, inconsistently represented, or weakly validated</strong>, raising a fundamental question: does the form in which user context is represented actually affect how faithfully an LLM-based persona mimics real user behavior?</p>

<p>The food domain makes this question especially relevant. Nutritional practice relies on structured instruments — questionnaires capturing dietary restrictions, health goals, and food attitudes — that differ substantially from the free-form biographies typically found in user-generated datasets. Yet these two sources of context have never been systematically compared in terms of their impact on persona fidelity.</p>

<div class="highlight-box">
<p><strong>The Gap:</strong> Existing work conditions LLM-based personas on ad hoc or loosely structured user information, without studying whether more principled, nutrition-inspired context representations lead to more faithful simulations of food preferences.</p>
</div>

<h2>Framework</h2>

<p>We design a two-stage pipeline that isolates the effect of context representation on persona behavior.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/llm-food-persona/figure1_pipeline.png" alt="Two-stage pipeline for LLM-based persona conditioning" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> Two-stage pipeline. Stage 1 (Context Representation) projects user biographies through LLMs into questionnaire-based structured profiles. Stage 2 (Persona Conditioning) conditions LLMs with UT, ST, or HT representations to produce simulated ratings and reviews.
  </figcaption>
</figure>

<h3>Stage 1: Context Representation</h3>
<p>User biographies from the dataset are projected through an LLM into structured profiles derived from two questionnaires:</p>
<ul>
<li><strong>Q-lit:</strong> A literature-grounded food preference questionnaire covering nine dimensions of food attitudes (familiarity, price, convenience, sensory appeal, health, mood, and others), designed for research settings</li>
<li><strong>Q-nut:</strong> A practitioner-oriented nutrition questionnaire capturing dietary restrictions and health goals, closer to clinical practice</li>
</ul>

<h3>Stage 2: Persona Conditioning</h3>
<p>LLMs are conditioned with one of three context representations and prompted to simulate ratings and written reviews for recipes:</p>
<ul>
<li><strong>UT (Unstructured Text):</strong> Raw user biography in free-form text, directly injected into the prompt</li>
<li><strong>ST (Structured Traits):</strong> Questionnaire-derived structured profile combining Q-lit and Q-nut responses</li>
<li><strong>HT (Hybrid):</strong> Concatenation of UT and ST, combining both information sources</li>
</ul>

<p><strong>Behavioral fidelity</strong> is measured by comparing the simulated outputs against real user ratings and reviews from the dataset, using rating alignment metrics (MSE, MAE, RMSE) and review similarity scores.</p>

<h2>Experimental Setup</h2>

<p>All experiments are conducted on <strong>HUMMUS</strong>, the largest publicly available dataset of user-recipe interactions:</p>

<ul>
<li><strong>39,315 users</strong> and <strong>507,335 items</strong> with an average of 2.84 interactions per user</li>
<li><strong>111,654 user-recipe pairs</strong> with both numerical ratings and written reviews, used for behavioral fidelity evaluation</li>
</ul>

<p>We evaluate five open-weight large language models spanning a range of architectures and sizes:</p>
<ul>
<li>DeepSeek-R1-70B</li>
<li>DeepSeek-R1-32B</li>
<li>Qwen 3-32B</li>
<li>Qwen 2.5-32B</li>
<li>LLaMA 3.1-8B</li>
</ul>

<h2>RQ1: Context Projection Quality</h2>

<p>Before conditioning personas, we assess how reliably LLMs can project unstructured user biographies into the structured questionnaire formats (Q-lit and Q-nut). We measure compliance with the response schema, overall accuracy, accuracy on known and unknown answers, and ordinal error.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/llm-food-persona/table1_projection_quality.png" alt="Table 1: Projection quality for structured profiles" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Table 1:</strong> Projection quality for structured profiles (RQ1). Reports Compliance, Overall Accuracy, Unknown Accuracy, Known Accuracy, and Ordinal Error for five LLMs across Q-lit and Q-nut questionnaires.
  </figcaption>
</figure>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/llm-food-persona/table2_ordinal_error.png" alt="Table 2: Ordinal error per question group in Q-lit" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Table 2:</strong> Ordinal error per question group in Q-lit (RQ1), covering nine food-preference dimensions.
  </figcaption>
</figure>

<h3>Key Findings</h3>
<ul>
<li><strong>Compliance is not guaranteed:</strong> Generating schema-compliant structured answers varies substantially across models, indicating that structured projection is a non-trivial task</li>
<li><strong>Best performers:</strong> Qwen 2.5-32B achieves the highest compliance on Q-lit; LLaMA 3.1-8B also performs competitively</li>
<li><strong>Q-nut is harder:</strong> Compliance is uniformly lower on Q-nut than Q-lit, reflecting its higher semantic complexity and clinical specificity</li>
<li><strong>Dimension-level variation:</strong> Familiarity, price, and convenience dimensions show strong heterogeneity in ordinal error; health, mood, and sensory dimensions are inferred with lower error</li>
</ul>

<h2>RQ2: Behavioral Fidelity</h2>

<p>We condition each of the five LLMs with the five context representations (UT, Q-nut, Q-lit, ST, HT) and compare simulated ratings and reviews against real user data.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/llm-food-persona/table3_behavioral_fidelity.png" alt="Table 3: Behavioral fidelity of LLM-based personas" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Table 3:</strong> Behavioral fidelity of LLM-based personas (RQ2). Five LLMs evaluated across five context representations (UT, Q-nut, Q-lit, ST, HT) on Rating Alignment (MSE, MAE, RMSE) and Review Similarity.
  </figcaption>
</figure>

<h3>Key Findings</h3>
<ul>
<li><strong>UT yields the lowest rating error:</strong> Unstructured text consistently achieves the best MSE, MAE, and RMSE across all models — free-form biographies preserve sufficient signal for predicting preference intensity</li>
<li><strong>Structured contexts improve review quality:</strong> Q-lit and Q-nut lead to higher rating error but produce reviews with stronger similarity to real user-written text</li>
<li><strong>HT achieves the highest overall fidelity:</strong> The hybrid representation combines the rating accuracy of UT with the review quality of structured traits, yielding the most consistent simulations</li>
<li><strong>Model-level differences:</strong> DeepSeek-R1-70B tends to over-predict ratings when conditioned on explicit traits; LLaMA 3.1-8B better matches the sparsity patterns of real user ratings</li>
</ul>

<div class="highlight-box">
<p><strong>Key Result:</strong> How user context is represented has a substantial impact on persona behavior. Unstructured text better preserves rating intensity, structured traits alone are insufficient to capture nuanced preferences, and hybrid representations yield the most faithful simulations overall.</p>
</div>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Systematic Comparison:</strong> First study comparing unstructured, structured, and hybrid context representations for conditioning LLM-based personas in the food domain</li>
<li><strong>Nutrition-Inspired Questionnaires:</strong> Design and evaluation of two complementary questionnaires (Q-lit and Q-nut) grounded in food science and nutritional practice</li>
<li><strong>Two-Stage Evaluation Pipeline:</strong> A reusable framework separating context projection quality (RQ1) from persona behavioral fidelity (RQ2)</li>
<li><strong>Empirical Evidence on Context Impact:</strong> Quantitative evidence that representation choice significantly affects both rating alignment and review similarity across five LLMs</li>
<li><strong>Hybrid Representation Advantage:</strong> Demonstration that combining unstructured and structured context yields more consistent persona behavior than either form alone</li>
</ul>
