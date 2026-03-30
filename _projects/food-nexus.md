---
title: "FoodNexus: Massive Food Knowledge for Recommender Systems"
collection: projects
permalink: /projects/food-nexus/
date: 2026-03-15
year: 2026
venue: "48th European Conference on Information Retrieval"
venue_short: "ECIR"

# Hero/Banner image (ontology overview)
hero_image: "/images/projects/food-nexus/figure1_ontology_overview.png"
teaser: "/images/projects/food-nexus/figure1_ontology_overview.png"

authors:
  - "Ludovico Boratto"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
  - "Giovanni Zedda"

author_links:
  Ludovico Boratto: "https://scholar.google.com/citations?user=1unjC10AAAAJ"
  Gianni Fenu: "https://scholar.google.com/citations?user=rP3KMr8AAAAJ"
  Mirko Marras: "https://scholar.google.com/citations?user=Cl2L9Q0AAAAJ"
  Giacomo Medda: "https://jackmedda.github.io"
  Giovanni Zedda: "https://scholar.google.com/citations?user=zedda"

keywords:
  - Food Ontology
  - Knowledge Extraction
  - Recipe Recommendation
  - User-side Knowledge Graph
  - Nutrition
  - Sustainability

# Links
doi: "10.1007/978-3-032-21321-1_52"
paperurl: "https://doi.org/10.1007/978-3-032-21321-1_52"
code: "https://github.com/tail-unica/food-nexus"

# Abstract
abstract: |
  Personalized food recommendation can promote healthier, sustainable eating, but current systems often rely on sparse and unstructured data, limiting semantic expressiveness and diverse personalization. In this paper, we propose FoodNexus, a large-scale knowledge graph with nearly one billion triples designed to enrich food recommendation with structured, nutrition-aware, and user-contextual information. We built it via a multi-stage pipeline that combines and augments the largest public dataset of user–recipe interactions, HUMMUS, with extensive metadata from Open Food Facts by linking recipes to concrete food products, extracting user traits from their biographies and reviews, and mapping both data sources onto the same ontology. Experiments show that FoodNexus enables richer, nutrition-sensitive evaluation of recommendations.

# BibTeX citation
bibtex: |
  @inproceedings{boratto2026foodnexus,
    author = {Boratto, Ludovico and Fenu, Gianni and Marras, Mirko and Medda, Giacomo and Zedda, Giovanni},
    title = {FoodNexus: Massive Food Knowledge for Recommender Systems},
    booktitle = {Proceedings of the 48th European Conference on Information Retrieval},
    series = {ECIR '26},
    year = {2026},
    publisher = {Springer},
    doi = {10.1007/978-3-032-21321-1_52},
    url = {https://doi.org/10.1007/978-3-032-21321-1_52}
  }
---

<h2>Motivation</h2>

<p>Personalized food recommendation systems can play a crucial role in promoting <strong>healthier</strong> and more <strong>sustainable</strong> eating habits. However, current systems often rely on sparse and unstructured data, which limits their semantic expressiveness and ability to support diverse personalization needs.</p>

<p>Existing datasets for food recommendation face two key limitations:</p>
<ul>
<li><strong>Lack of user-level constructs:</strong> Most datasets do not capture user preferences, dietary restrictions, or consumption traits</li>
<li><strong>Missing product granularity:</strong> Recipes cannot be aligned with real food products for nutritional and sustainability analysis</li>
</ul>

<div class="highlight-box">
<p><strong>The Problem:</strong> No existing resource comprehensively supports nutrition, sustainability, and user constraints in food recommendation. Current systems cannot evaluate whether recommendations align with users' health goals or environmental concerns.</p>
</div>

<h2>FoodNexus Knowledge Graph</h2>

<p><strong>FoodNexus</strong> is a large-scale knowledge graph designed to enrich food recommendation with structured, nutrition-aware, and user-contextual information. It combines and augments the largest public dataset of user-recipe interactions (HUMMUS) with extensive metadata from Open Food Facts.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/food-nexus/figure1_ontology_overview.png" alt="FoodNexus ontology overview" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> Visual overview of the FoodNexus ontology showing entities and their relationships.
  </figcaption>
</figure>

<h3>Scale and Coverage</h3>

<ul>
<li><strong>~979.5 million triples</strong> capturing food knowledge</li>
<li><strong>~51 million entities</strong> across 11 entity types</li>
<li><strong>~130.2 million attributes</strong> with 15 attribute types</li>
<li><strong>11 relation types</strong> connecting entities</li>
<li><strong>73% of entities</strong> and <strong>70% of relations</strong> aligned with schema.org vocabulary for interoperability</li>
</ul>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/food-nexus/table1_data_sources_comparison.png" alt="Comparison of data sources" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Table 1:</strong> Comparison of feature-rich data sources for food recommendation.
  </figcaption>
</figure>

<h2>Construction Pipeline</h2>

<p>FoodNexus is built via a 5-stage pipeline that combines multiple data sources and enriches them with semantic knowledge:</p>

<h3>Stage 1: Source Dataset Selection</h3>
<p>We combine <strong>HUMMUS</strong>, the largest public dataset of user-recipe interactions, with <strong>Open Food Facts</strong>, a comprehensive database of food products with nutritional and sustainability information.</p>

<h3>Stage 2: Combined Ontology Specification</h3>
<p>We design a unified ontology that captures recipes, ingredients, products, users, and their relationships, aligned with schema.org vocabulary for interoperability.</p>

<h3>Stage 3: Recipe-Product Entity Linking</h3>
<p>Using the <strong>BAAI/bge-en-icl</strong> encoder with a 0.85 similarity threshold, we link recipe ingredients to concrete food products from Open Food Facts.</p>

<h3>Stage 4: User Consumption Traits Extraction</h3>
<p>We employ <strong>Qwen2.5 LLM</strong> to extract user traits (dietary preferences, restrictions, health goals) from their biographies and reviews.</p>

<h3>Stage 5: Knowledge Graph Assembly</h3>
<p>All extracted entities, relations, and attributes are assembled into a unified knowledge graph following the specified ontology.</p>

<p><strong>Table 2:</strong> Relations with element names in FoodNexus.</p>

<table class="results-table">
<thead>
<tr><th>Source</th><th>Relation</th><th>Target</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>UserGroup</td><td>publishesRecipe</td><td>Recipe</td><td>A user has published a recipe</td></tr>
<tr><td>UserGroup</td><td>publishesReview</td><td>UserReview</td><td>A user has published a review</td></tr>
<tr><td>UserGroup</td><td>hasConstraint</td><td>Tag</td><td>A user has a dietary constraint</td></tr>
<tr><td>UserReview</td><td>itemReviewed</td><td>Recipe</td><td>A review is associated with a recipe</td></tr>
<tr><td>Recipe</td><td>hasIndicator</td><td>Indicator</td><td>A recipe has a certain indicator</td></tr>
<tr><td>Product</td><td>hasIndicator</td><td>Indicator</td><td>A product has a certain indicator</td></tr>
<tr><td>Recipe</td><td>hasPart</td><td>Ingredient</td><td>A recipe includes a specific ingredient</td></tr>
<tr><td>Ingredient</td><td>isRelatedTo</td><td>Recipe</td><td>An ingredient is part of a recipe</td></tr>
<tr><td>Tag</td><td>suitableForDiet</td><td>Recipe</td><td>A constraint is compatible with a recipe</td></tr>
<tr><td>Tag</td><td>suitableForDiet</td><td>Product</td><td>A constraint is compatible with a product</td></tr>
<tr><td>Product</td><td>sameAs</td><td>Recipe</td><td>A product is similar/identical to a recipe</td></tr>
<tr><td>FoodProducer</td><td>produces</td><td>Product</td><td>A producer produces a product</td></tr>
<tr><td>Recipe</td><td>sameAs</td><td>Recipe</td><td>A recipe is an alternative or similar recipe</td></tr>
<tr><td>Store</td><td>offers</td><td>Product</td><td>A store sells a certain product</td></tr>
<tr><td>Store</td><td>isPlaceIn</td><td>City</td><td>A store is located in a certain city</td></tr>
<tr><td>Product</td><td>countryOfAssembly</td><td>Country</td><td>A product is assembled in a country</td></tr>
</tbody>
</table>

<h2>Statistics and Comparison</h2>

<p><strong>Table 3:</strong> Comparative statistics between original data sources and FoodNexus.</p>

<table class="results-table">
<thead>
<tr><th>Data Source</th><th># Triples</th><th># Entities</th><th># Attributes</th><th># E. Types</th><th># R. Types</th><th># A. Types</th></tr>
</thead>
<tbody>
<tr><td>HUMMUS</td><td>~53.9M</td><td>~12.3M</td><td>~22.8M</td><td>6</td><td>6</td><td>9</td></tr>
<tr><td>HUMMUS (inferred)</td><td>~57.9M</td><td>~12.3M</td><td>~22.8M</td><td>6</td><td>7</td><td>14</td></tr>
<tr><td>OFF</td><td>~267.9M</td><td>~38.5M</td><td>~107.4M</td><td>7</td><td>6</td><td>7</td></tr>
<tr><td><strong>FoodNexus (Ours)</strong></td><td><strong>~979.5M</strong></td><td><strong>~51.0M</strong></td><td><strong>~130.2M</strong></td><td><strong>11</strong></td><td><strong>11</strong></td><td><strong>15</strong></td></tr>
</tbody>
</table>
<p style="font-size: 0.9em; color: #666;">E. Types: Entity Types; R. Types: Relation Types; A. Types: Attribute Types</p>

<h2>Experimental Results</h2>

<p>We evaluate FoodNexus through two research questions:</p>

<h3>RQ1: Recommendation Utility</h3>

<p>We compare several recommender systems on FoodNexus to assess recommendation quality:</p>

<p><strong>Table 4:</strong> Performance comparison across recommendation models with Hit, Recall, and NDCG on top-10/20/50 lists.</p>

<table class="results-table">
<thead>
<tr><th>Model</th><th>Hit@10</th><th>Hit@20</th><th>Hit@50</th><th>Recall@10</th><th>Recall@20</th><th>Recall@50</th><th>NDCG@10</th><th>NDCG@20</th><th>NDCG@50</th></tr>
</thead>
<tbody>
<tr><td>Pop</td><td>0.0035</td><td>0.0050</td><td>0.0077</td><td>0.0008</td><td>0.0010</td><td>0.0013</td><td>0.0008</td><td>0.0009</td><td>0.0009</td></tr>
<tr><td>BPR</td><td>0.0474</td><td>0.0777</td><td>0.1361</td><td>0.0136</td><td>0.0244</td><td>0.0467</td><td>0.0102</td><td>0.0133</td><td>0.0189</td></tr>
<tr><td>NeuMF</td><td>0.0562</td><td>0.0886</td><td>0.1491</td><td>0.0175</td><td>0.0276</td><td>0.0515</td><td>0.0131</td><td>0.0160</td><td>0.0220</td></tr>
<tr><td>LightGCN</td><td><strong>0.0604</strong></td><td><strong>0.0930</strong></td><td><strong>0.1558</strong></td><td>0.0184</td><td>0.0307</td><td>0.0557</td><td>0.0140</td><td>0.0173</td><td>0.0235</td></tr>
<tr><td>MKR</td><td>0.0413</td><td>0.0656</td><td>0.1126</td><td>0.0166</td><td>0.0272</td><td>0.0477</td><td>0.0111</td><td>0.0140</td><td>0.0188</td></tr>
<tr><td>KTUP</td><td>0.0446</td><td>0.0737</td><td>0.1260</td><td>0.0189</td><td>0.0315</td><td>0.0552</td><td>0.0118</td><td>0.0154</td><td>0.0210</td></tr>
<tr><td>KGAT</td><td>0.0580</td><td>0.0903</td><td>0.1453</td><td><strong>0.0231</strong></td><td><strong>0.0372</strong></td><td><strong>0.0628</strong></td><td><strong>0.0152</strong></td><td><strong>0.0191</strong></td><td><strong>0.0252</strong></td></tr>
<tr><td>UserKGAT</td><td>0.0187</td><td>0.0368</td><td>0.0802</td><td>0.0084</td><td>0.0164</td><td>0.0370</td><td>0.0046</td><td>0.0069</td><td>0.0116</td></tr>
<tr><td>UserKTUP</td><td>0.0388</td><td>0.0690</td><td>0.1260</td><td>0.0154</td><td>0.0295</td><td>0.0570</td><td>0.0093</td><td>0.0133</td><td>0.0198</td></tr>
<tr><td>UserMKR</td><td>0.0461</td><td>0.0744</td><td>0.1264</td><td>0.0187</td><td>0.0319</td><td>0.0556</td><td>0.0120</td><td>0.0157</td><td>0.0212</td></tr>
</tbody>
</table>

<ul>
<li><strong>LightGCN</strong> achieves the highest Hit scores</li>
<li><strong>KGAT</strong> achieves the best Recall and NDCG</li>
<li><strong>UserMKR</strong> (user-aware variant) can capture useful KG patterns when properly designed</li>
</ul>

<h3>RQ2: Nutritional and Contextual Analysis</h3>

<p>FoodNexus enables nutrition-sensitive evaluation, revealing systematic biases in current recommender systems:</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/food-nexus/figure2_categorical_analysis.png" alt="Categorical analysis heatmap" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 2:</strong> Average per-user difference Δ between category proportions in models' top-k lists and global category prevalence for Allergens, Packaging, and Green Score.
  </figcaption>
</figure>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/food-nexus/figure3_nutritional_analysis.png" alt="Nutritional analysis" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 3:</strong> Average per-user difference Δ for numerical nutritional attributes including Added Sugars, Saturated Fat, Potassium, Fiber, and Vitamins.
  </figcaption>
</figure>

<ul>
<li><strong>Gluten bias:</strong> Models tend to over-represent gluten-containing items</li>
<li><strong>Packaging bias:</strong> Interaction-based systems over-represent plastic-packaged products</li>
<li><strong>Sustainability skew:</strong> Systematic bias toward less sustainable items detected</li>
<li><strong>Nutritional signals:</strong> Models under-represent vitamins and potassium while showing mixed results for sugars and fats</li>
</ul>

<div class="highlight-box">
<p><strong>Key Finding:</strong> FoodNexus enables richer, nutrition-sensitive evaluation of recommendations, revealing biases that would be invisible with traditional datasets.</p>
</div>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Large-Scale Knowledge Graph:</strong> Nearly one billion triples linking recipes, products, users, and nutritional information</li>
<li><strong>User Trait Extraction:</strong> Novel pipeline using LLMs to extract dietary preferences and health goals from user content</li>
<li><strong>Recipe-Product Linking:</strong> Semantic matching to connect recipes with real food products for nutritional analysis</li>
<li><strong>Nutrition-Aware Evaluation:</strong> Framework for assessing recommendation fairness regarding health and sustainability</li>
<li><strong>Schema.org Alignment:</strong> High interoperability with existing semantic web standards</li>
</ul>

<h2>Resources</h2>

<p>The FoodNexus dataset and code are publicly available:</p>

<ul>
<li><a href="https://github.com/tail-unica/food-nexus" target="_blank"><i class="fab fa-github"></i> GitHub Repository</a> — Code, documentation, and usage examples</li>
<li><a href="https://zenodo.org/records/15710771" target="_blank"><i class="ai ai-zenodo"></i> Zenodo Dataset</a> — Full dataset download (DOI: 10.5281/zenodo.15710771)</li>
</ul>
