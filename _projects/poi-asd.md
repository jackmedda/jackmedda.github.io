---
title: "Small Data, Big Impact: Navigating Resource Limitations in Point-of-Interest Recommendation for Individuals with Autism"
collection: projects
permalink: /projects/poi-asd/
date: 2025-07-13
year: 2025
venue: "International ACM SIGIR Conference on Research and Development in Information Retrieval"
venue_short: "SIGIR"

# teaser: "/images/teaser-default.png"

authors:
  - "Ludovico Boratto"
  - "Federica Cena"
  - "Mirko Marras"
  - "Noemi Mauro"
  - "Giacomo Medda"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Federica Cena: "https://www.di.unito.it/~cena/"
  Mirko Marras: "https://www.mirkomarras.com/"
  Noemi Mauro: "https://www.di.unito.it/~mauro/"
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Autism Spectrum Disorder
  - POI Recommendation
  - Knowledge Graphs
  - Path Reasoning
  - Low-Resource
  - Accessibility

doi: "10.1145/3726302.3730269"
paperurl: "https://doi.org/10.1145/3726302.3730269"

abstract: |
  Autism Spectrum Disorder (ASD) affects sensory perception, making spatial exploration difficult. Recommender systems can assist ASD users by suggesting Points of Interest (POIs) aligned with their sensory preferences. However, demographic constraints, difficulties in engaging ASD users, and the complexity of obtaining sensory data position POI recommendation for ASD people as a low-resource problem. In this paper, we identify key challenges in developing such systems and present our ongoing efforts. Using a local ASD center as a use case, we are developing a structured user involvement protocol. From the limited data, we are deriving knowledge graphs (KGs) to model preferences and sensory aspects. We are then exploring KG-based techniques to generate paths from users to POIs to suggest. With psychologists, we are refining the paths structure to match varying complexity levels and translate them into natural language accessible for people with ASD.

bibtex: |
  @inproceedings{boratto2025smalldata,
    author = {Boratto, Ludovico and Cena, Federica and Marras, Mirko and Mauro, Noemi and Medda, Giacomo},
    title = {Small Data, Big Impact: Navigating Resource Limitations in Point-of-Interest Recommendation for Individuals with Autism},
    booktitle = {Proceedings of the 48th International ACM SIGIR Conference on Research and Development in Information Retrieval},
    series = {SIGIR '25},
    year = {2025},
    location = {Padua, Italy},
    publisher = {Association for Computing Machinery},
    doi = {10.1145/3726302.3730269}
  }
---

<section id="motivation">
  <h2>Motivation</h2>
  <div class="highlight-box">
    <p>
      <strong>Why POI Recommendation for ASD?</strong> Autism Spectrum Disorder affects sensory perception, 
      making spatial exploration challenging and anxiety-inducing. Digital technologies, including recommender 
      systems, can assist ASD users by suggesting Points of Interest aligned with their sensory preferences. 
      However, this represents a <em>low-resource problem</em> due to demographic constraints and engagement difficulties.
    </p>
  </div>
</section>

<section id="challenges">
  <h2>Open Challenges</h2>
  <p>
    Developing recommender systems for ASD users presents unique challenges:
  </p>
  <ul>
    <li><strong>C1. Limited population:</strong> Autistic users represent a small portion of the population, and reaching them for research is challenging due to social difficulties</li>
    <li><strong>C2. Negative consequences:</strong> Poorly matched recommendations could trigger sensory overload, anxiety, or distress—unlike typical consumer scenarios</li>
    <li><strong>C3. Demanding personalization:</strong> Traditional recommenders fail to capture unique sensory aversions and preferences that impact how people with ASD experience places</li>
    <li><strong>C4. Transparency requirements:</strong> People with ASD employ more structured, logic-driven decision-making and require clearer reasoning pathways</li>
    <li><strong>C5. Accessibility requirements:</strong> Information must accommodate perceptual and cognitive patterns specific to autism</li>
    <li><strong>C6. Specialized evaluation:</strong> Traditional user study designs are less effective for ASD users with limited attention spans</li>
  </ul>
</section>

<section id="method">
  <h2>Our Approach</h2>
  <p>
    We are addressing these challenges in collaboration with the <strong>Regional Center for Autism Spectrum 
    Disorders in Adulthood - ASL City of Turin</strong>.
  </p>
  
  <h3>Specialized Involvement Protocol</h3>
  <p>
    To mitigate C1 and C6, we created a structured, reproducible user-centered involvement protocol 
    using participatory co-design methodology with ASD specialists.
  </p>
  
  <h3>Graph-Based Data Modeling</h3>
  <p>
    With C2 and C3 in mind, we developed a novel ontology modeling relationships between autistic users, 
    sensory aversions, POI categories, and POI sensory features. We constructed a Knowledge Graph with:
  </p>
  <ul>
    <li><strong>25,468 triples</strong></li>
    <li><strong>551 entities</strong></li>
    <li><strong>5 relations</strong></li>
  </ul>
  
  <h3>KG-Based Path Reasoning</h3>
  <p>
    To address C4, we develop explainable recommendation models based on path-reasoning techniques that 
    traverse structured meta-paths within the KG, mirroring human reasoning patterns. Our approach explores:
  </p>
  <ul>
    <li><strong>Reinforcement learning:</strong> Agent traversing the KG</li>
    <li><strong>Language models:</strong> Interpreting KG elements as tokens</li>
  </ul>
  
  <h3>Tailored Delivery</h3>
  <p>
    To address C5 and C6, we involve psychologists to adapt explanation templates and optimize the user 
    interface for mid-high functioning ASD users, matching individual cognitive and linguistic capacity.
  </p>
</section>

<section id="impact">
  <h2>Impact</h2>
  <div class="highlight-box">
    <p>
      <strong>Contribution:</strong> While many challenges exist and much work remains, our approach to 
      recommendation can positively contribute to a more inclusive framework for ASD users, helping them 
      navigate spaces and explore new locations with reduced anxiety.
    </p>
  </div>
</section>
