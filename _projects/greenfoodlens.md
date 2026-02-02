---
title: "GreenFoodLens: Sustainability Labels for Food Recommendation"
collection: projects
permalink: /projects/greenfoodlens/
date: 2025-09-22
year: 2025
venue: "ACM Conference on Recommender Systems"
venue_short: "RecSys"

hero_image: "/images/projects/greenfoodlens/figure_5_page7.png"
teaser: "/images/projects/greenfoodlens/figure_1_page3.png"

authors:
  - "Giacomo Balloccu"
  - "Ludovico Boratto"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
  - "Giovanni Murgia"

author_links:
  Giacomo Balloccu: "https://www.giacomoballoccu.it/"
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Gianni Fenu: "https://people.unica.it/giannifenu/"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io/"
  Giovanni Murgia: "#"

keywords:
  - Food Recommendation
  - Sustainability
  - Carbon Footprint
  - Water Footprint
  - Large Language Models
  - Dataset

doi: "10.1145/3705328.3748165"
paperurl: "https://doi.org/10.1145/3705328.3748165"
code: "https://github.com/tail-unica/GreenFoodLens"

abstract: |
  Most food recommender systems aim to boost user engagement by analyzing recipe ingredients and users' past choices. Even though consumers are paying more attention to sustainability, such as carbon and water footprints, there remains a notable lack of public corpora that combine detailed user–recipe interactions with reliable environmental impact data. This gap makes it hard to build recommendation tools that both match people's tastes and help reduce ecological damage. To this end, we present GreenFoodLens, a resource that enriches HUMMUS, one of the largest corpora for food recommendation, with environmental impact estimates derived from the hierarchical taxonomy of the SU-EATABLE-LIFE project. We achieved this result through a multi-step process involving human annotations, iterative labeling assessments, knowledge refinement, and constrained generation techniques with large language models.

bibtex: |
  @inproceedings{balloccu2025greenfoodlens,
    author = {Balloccu, Giacomo and Boratto, Ludovico and Fenu, Gianni and Marras, Mirko and Medda, Giacomo and Murgia, Giovanni},
    title = {GreenFoodLens: Sustainability Labels for Food Recommendation},
    booktitle = {Proceedings of the 19th ACM Conference on Recommender Systems},
    series = {RecSys '25},
    year = {2025},
    publisher = {Association for Computing Machinery},
    doi = {10.1145/3705328.3748165}
  }
---

<section id="motivation">
  <h2>Motivation</h2>
  <div class="highlight-box">
    <p>
      <strong>Why sustainability in food recommendation?</strong> Food production accounts for over 26% of 
      global greenhouse gas emissions. Food recommender systems could promote environmentally-conscious 
      choices, but existing datasets lack environmental impact information. GreenFoodLens bridges this gap 
      by enriching the largest food recommendation corpus with sustainability labels.
    </p>
  </div>
</section>

<section id="resource">
  <h2>Resource Description</h2>
  
  <p>GreenFoodLens enriches <strong>421,956 recipes</strong> (from HUMMUS) with two environmental metrics sourced from SU-EATABLE-LIFE:</p>
  <ul>
    <li><strong>Carbon Footprint (CFP):</strong> kg CO₂ equivalent per kg of food (greenhouse gas emissions)</li>
    <li><strong>Water Footprint (WFP):</strong> Liters of water per kg of food (water consumption in production)</li>
  </ul>

  <figure>
    <img src="/images/projects/greenfoodlens/figure_1_page3.png" alt="GreenFoodLens Pipeline">
    <figcaption>The GreenFoodLens labeling pipeline: from human annotation review to LLM automated labeling with constrained generation.</figcaption>
  </figure>
</section>

<section id="methodology">
  <h2>Methodology</h2>
  
  <h3>1. Taxonomy Revision</h3>
  <p>
    We expanded SU-EATABLE-LIFE's four-level hierarchy (groups → typologies → sub-typologies → items) by:
  </p>
  <ul>
    <li>Splitting ANIMAL HUSBANDRY into MEAT PRODUCTS and ANIMAL DERIVED for clearer categorization</li>
    <li>Adding intermediate nodes (e.g., YEAST GENERIC) to reduce annotator uncertainty</li>
  </ul>
  
  <h3>2. Human Labeling</h3>
  <p>
    We collected annotations via Amazon Mechanical Turk for 17,312 unique ingredients (86,560 jobs). 
    After thorough manual verification, we retained <strong>3,496 high-quality annotations</strong> as our ground truth.
  </p>
  
  <h3>3. LLM-Based Constrained Generation</h3>
  <p>
    We use Large Language Models with <strong>grammar-based constrained generation (GBNF)</strong> to prevent hallucinations 
    and ensure outputs strictly follow the taxonomy structure. Our approach combines:
  </p>
  <ul>
    <li><strong>Few-shot prompting:</strong> Demonstrating desired output format</li>
    <li><strong>Generate-knowledge prompting:</strong> Creating bootstrap descriptions for context</li>
  </ul>
  
  <figure>
    <img src="/images/projects/greenfoodlens/figure_2_page4.png" alt="Taxonomy structure">
    <figcaption>Extract of the revised SU-EATABLE-LIFE taxonomy with newly added intermediate nodes.</figcaption>
  </figure>
</section>

<section id="results">
  <h2>Results & Analysis</h2>
  
  <h3>Labeling Accuracy</h3>
  <p>
    Using Athene-V2-Chat (72B parameters), we achieve strong accuracy at higher taxonomy levels:
  </p>
  <ul>
    <li><strong>Group Match:</strong> 96.22%</li>
    <li><strong>Typology Match:</strong> 74.94%</li>
    <li><strong>Sub-typology Match:</strong> 55.72%</li>
    <li><strong>Item Match:</strong> 51.49%</li>
  </ul>
  
  <h3>Dataset Statistics</h3>
  <div class="figure-grid grid-2x2">
    <div class="grid-item"><img src="/images/projects/greenfoodlens/figure_3_page6.png" alt="Ingredient distribution"></div>
    <div class="grid-item"><img src="/images/projects/greenfoodlens/figure_4_page6.png" alt="Typology frequency"></div>
    <div class="grid-item"><img src="/images/projects/greenfoodlens/figure_5_page7.png" alt="CFP/WFP distribution"></div>
    <div class="grid-item"><img src="/images/projects/greenfoodlens/figure_6_page8.png" alt="Recommendation analysis"></div>
  </div>
  <p class="figure-caption">Top-left: Ingredient distribution across food groups. Top-right: 20 most frequent typologies. 
  Bottom: CFP/WFP distributions and recommendation sustainability analysis.</p>
  
  <h3>Key Findings</h3>
  <ul>
    <li>Most ingredients belong to AGRICULTURAL PROCESSED and CROPS (lower environmental impact)</li>
    <li>SWEETS is the most frequent typology, reflecting dessert popularity on food platforms</li>
    <li>MEAT PRODUCTS and ANIMAL DERIVED show higher CFP/WFP values with pronounced outliers</li>
    <li>Recommendation models are driven by popularity signals, which may exacerbate environmental impact</li>
  </ul>
  
  <figure>
    <img src="/images/projects/greenfoodlens/figure_7_page9.png" alt="Sustainability analysis">
    <figcaption>CFP and WFP analysis of recommended recipes showing alignment between user interactions and model recommendations.</figcaption>
  </figure>
</section>

<section id="applications">
  <h2>Applications</h2>
  <div class="highlight-box">
    <p>
      <strong>Research Directions:</strong> GreenFoodLens enables sustainability-aware meal planning, 
      explainable recommendations with environmental justifications, personalized sustainability reports, 
      and product reformulation guidance for food producers seeking lower-impact ingredient substitutes.
    </p>
  </div>
</section>
