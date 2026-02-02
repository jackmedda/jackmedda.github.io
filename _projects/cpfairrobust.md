---
title: "Robustness in Fairness against Edge-level Perturbations in GNN-based Recommendation"
collection: projects
permalink: /projects/cpfairrobust/
date: 2024-03-24
year: 2024
venue: "European Conference on Information Retrieval"
venue_short: "ECIR"

# hero_image: "/images/projects/cpfairrobust/figure_1.png"
# teaser: "/images/projects/cpfairrobust/figure_1.png"

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
  - Robustness
  - Fairness
  - Recommender Systems
  - Graph Neural Networks
  - Perturbation
  - Multi-Stakeholder
  - Consumer Fairness
  - Provider Fairness

doi: "10.1007/978-3-031-56063-7_42"
paperurl: "https://link.springer.com/chapter/10.1007/978-3-031-56063-7_42"
code: "https://github.com/jackmedda/CPFairRobust"

abstract: |
  Efforts in the recommendation community are shifting from the sole emphasis on utility to considering beyond-utility factors, such as fairness and robustness. Robustness of recommendation models is typically linked to their ability to maintain the original utility when subjected to attacks. Limited research has explored the robustness of a recommendation model in terms of fairness, e.g., the parity in performance across groups, under attack scenarios. In this paper, we aim to assess the robustness of graph-based recommender systems concerning fairness, when exposed to attacks based on edge-level perturbations. To this end, we considered four different fairness operationalizations, including both consumer and provider perspectives. Experiments on three datasets shed light on the impact of perturbations on the targeted fairness notion, uncovering key shortcomings in existing evaluation protocols for robustness. As an example, we observed perturbations affect consumer fairness on a higher extent than provider fairness, with alarming unfairness for the former.

bibtex: |
  @inproceedings{boratto2024robustness,
    author = {Boratto, Ludovico and Fabbri, Francesco and Fenu, Gianni and Marras, Mirko and Medda, Giacomo},
    title = {Robustness in Fairness against Edge-level Perturbations in GNN-based Recommendation},
    booktitle = {Advances in Information Retrieval - 46th European Conference on Information Retrieval, ECIR 2024},
    series = {Lecture Notes in Computer Science},
    year = {2024},
    publisher = {Springer},
    doi = {10.1007/978-3-031-56063-7_42}
  }
---

<section id="motivation">
  <h2>Motivation</h2>
  <div class="highlight-box">
    <p>
      <strong>Why study robustness in fairness?</strong> While recommendation robustness typically focuses on 
      maintaining utility under attacks, little research explores how attacks affect <em>fairness</em>. 
      An attacker could exploit this blind spot to compromise a system's fairness without significantly 
      changing overall accuracy—potentially damaging a company's reputation and violating emerging regulations.
    </p>
  </div>
  <p>
    Our work addresses the intersection of two critical properties: <strong>robustness</strong> (resilience to attacks) 
    and <strong>fairness</strong> (equitable treatment across demographic groups). We investigate whether GNN-based 
    recommender systems can maintain fair outcomes when subjected to edge-level perturbations.
  </p>
</section>

<section id="methodology">
  <h2>Methodology</h2>
  
  <h3>Perturbation Framework</h3>
  <p>
    We extend graph perturbation techniques to assess fairness robustness. Given a user-item bipartite graph 
    $G = (V, E)$ encoded as adjacency matrix $A$, we iteratively perturb the graph to produce $\tilde{A}$ and 
    measure the fairness impact:
  </p>
  <p style="text-align: center;">
    $$\Delta = M(f(\tilde{A}, W), A) - M(f(A, W), A)$$
  </p>
  <p>where $M$ is a fairness metric and $f$ is the GNN-based recommender.</p>
  
  <h3>Fairness Operationalizations</h3>
  <p>We evaluate four fairness notions covering both stakeholder perspectives:</p>
  
  <table class="styled-table">
    <thead>
      <tr><th>Perspective</th><th>Metric</th><th>Description</th></tr>
    </thead>
    <tbody>
      <tr><td rowspan="2"><strong>Consumer</strong></td><td>CP (Consumer Parity)</td><td>Equal recommendation quality across user groups</td></tr>
      <tr><td>CS (Consumer Satisfaction)</td><td>Equal satisfaction levels across demographics</td></tr>
      <tr><td rowspan="2"><strong>Provider</strong></td><td>PP (Provider Parity)</td><td>Equal exposure across item groups</td></tr>
      <tr><td>PS (Provider Satisfaction)</td><td>Equal visibility for provider categories</td></tr>
    </tbody>
  </table>
  
  <h3>Perturbation Types</h3>
  <ul>
    <li><strong>Edge Deletion:</strong> Removing existing user-item interactions</li>
    <li><strong>Edge Addition:</strong> Injecting fake interactions into the graph</li>
  </ul>
</section>

<section id="experiments">
  <h2>Experimental Setup</h2>
  
  <h3>Datasets</h3>
  <table class="styled-table">
    <thead>
      <tr><th>Dataset</th><th>Domain</th><th>Users</th><th>Items</th><th>Interactions</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>MovieLens-1M</strong></td><td>Movies</td><td>6,040</td><td>3,706</td><td>1,000,209</td></tr>
      <tr><td><strong>Last.FM-1K</strong></td><td>Music</td><td>268</td><td>51,609</td><td>200,586</td></tr>
      <tr><td><strong>Insurance</strong></td><td>Insurance</td><td>346</td><td>20</td><td>1,879</td></tr>
    </tbody>
  </table>
  
  <h3>GNN Models</h3>
  <ul>
    <li><strong>GCMC</strong> - Graph Convolutional Matrix Completion</li>
    <li><strong>NGCF</strong> - Neural Graph Collaborative Filtering</li>
    <li><strong>LightGCN</strong> - Simplified Graph Convolution for Recommendation</li>
  </ul>
</section>

<section id="results">
  <h2>Key Findings</h2>
  
  <div class="highlight-box">
    <p>
      <strong>Main Result:</strong> Edge-level perturbations affect <em>consumer fairness</em> to a much greater 
      extent than <em>provider fairness</em>. Even small perturbations can dramatically increase unfairness 
      between demographic groups.
    </p>
  </div>
  
  <h3>Consumer vs Provider Fairness</h3>
  <ul>
    <li><strong>Consumer fairness is highly vulnerable:</strong> Unfairness levels across consumer groups can be significantly increased by a small number of perturbations</li>
    <li><strong>Provider fairness shows limited impact:</strong> The effect on provider fairness is bounded by the prior unfairness level in the original recommendations</li>
    <li><strong>Asymmetric sensitivity:</strong> Models exhibit different sensitivity patterns for deletion vs. addition attacks</li>
  </ul>
  
  <h3>Implications</h3>
  <ul>
    <li><strong>Evaluation protocols are insufficient:</strong> Current robustness evaluation focusing only on utility misses critical fairness degradation</li>
    <li><strong>Regulatory concerns:</strong> Given recent regulations on fairness and robustness of automated systems, these findings highlight worrying vulnerabilities</li>
    <li><strong>Defense priorities:</strong> Consumer-side fairness requires more attention in robustness mechanisms</li>
  </ul>
</section>

<section id="contributions">
  <h2>Contributions</h2>
  <ul>
    <li><strong>Novel analysis framework:</strong> First comprehensive study of robustness in fairness for GNN-based recommendation</li>
    <li><strong>Multi-stakeholder perspective:</strong> Evaluation covering both consumer and provider fairness notions</li>
    <li><strong>Practical insights:</strong> Uncovering shortcomings in existing robustness evaluation protocols</li>
    <li><strong>Open source:</strong> Full implementation available for reproducibility</li>
  </ul>
</section>

