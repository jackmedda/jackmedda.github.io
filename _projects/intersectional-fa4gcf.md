---
title: "Graph Augmentation for Intersectional Unfairness Mitigation: A Study across Dataset Scales and Interaction Densities"
collection: projects
permalink: /projects/intersectional-fa4gcf/
date: 2026-01-01
year: 2026
venue: "ACM Transactions on Recommender Systems"
venue_short: "ACM TORS"

# Hero/Banner image
hero_image: "/images/projects/intersectional-fa4gcf/figure4_energy_distance_vs_fairness_gain.png"
teaser: "/images/projects/intersectional-fa4gcf/figure4_energy_distance_vs_fairness_gain.png"

authors:
  - "Ludovico Boratto"
  - "Francesco Fabbri"
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"

author_links:
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Francesco Fabbri: "https://frafabbri.github.io/"
  Gianni Fenu: "https://web.unica.it/unica/page/it/gianni_fenu"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io/"

keywords:
  - Recommender Systems
  - Fairness
  - Intersectionality
  - Graph Augmentation
  - GNN
  - Consumer Fairness
  - Large-scale

# Links
doi: "10.1145/3798097"
paperurl: "https://doi.org/10.1145/3798097"
code: "https://github.com/jackmedda/Intersectional-FA4GCF"

# Abstract
abstract: |
  Recent work on fairness-aware graph collaborative filtering (GCF) has shown the effectiveness of graph augmentation as a post-processing strategy for mitigating consumer unfairness. However, most studies remain confined to binary fairness setups and operate under limited experimental conditions, often relying on sparse and small-scale datasets. In this paper, we extend our fairness-aware augmentation method to address intersectional unfairness across demographic subgroups, a setting where the intersection of multiple sensitive attributes leads to fine-grained subgroups. To this end, we reformulate the fairness objective to incorporate intersectional demographic groups and evaluate our extended method across interaction configurations that vary in density and scale. Our results reveal that the effectiveness of fair graph augmentations is model-dependent and sensitive to dataset properties. We show that the edges selected during augmentation tend to concentrate around interpretable structural patterns driven by the connected nodes' characteristics. Furthermore, analyzing how these augmented edges differ across graph-level attributes offers actionable insights into the potential benefits of fairness-oriented graph modifications. Finally, we compare our method with recent fairness-aware baselines, explore the impact of augmenting different graph regions, and assess our mitigation strategy under scenarios with minimal unfairness.

# BibTeX citation
bibtex: |
  @article{boratto2026intersectional,
    author = {Boratto, Ludovico and Fabbri, Francesco and Fenu, Gianni and Marras, Mirko and Medda, Giacomo},
    title = {Graph Augmentation for Intersectional Unfairness Mitigation: A Study across Dataset Scales and Interaction Densities},
    journal = {ACM Transactions on Recommender Systems},
    year = {2026},
    doi = {10.1145/3798097},
    url = {https://doi.org/10.1145/3798097}
  }
---

<h2>Motivation</h2>

<p>Graph collaborative filtering (GCF) powered by graph neural networks (GNNs) has become a leading paradigm for personalized recommendation. As these systems shape access to information and opportunities, ensuring they treat all user groups equitably is increasingly important. Prior work on fairness-aware GCF, however, suffers from three compounding limitations:</p>

<ul>
  <li><strong>Binary fairness setups:</strong> Most studies define consumer groups along a single binary attribute (e.g., Male vs. Female), ignoring how multiple attributes interact to produce compounded disadvantages.</li>
  <li><strong>Intersectionality gap:</strong> The intersection of multiple sensitive attributes (e.g., Gender × Age) creates fine-grained subgroups — Older Females, Younger Males, etc. — whose distinct fairness needs are invisible to binary formulations.</li>
  <li><strong>Small-scale evaluation:</strong> Experiments are typically conducted on sparse, small datasets, leaving open whether findings generalise to denser, large-scale interaction graphs.</li>
</ul>

<div class="highlight-box">
<p><strong>Goal:</strong> Extend fairness-aware graph augmentation to the intersectional setting and rigorously evaluate it across five datasets spanning a wide range of densities and scales, from 1.90% to 35.01% interaction density.</p>
</div>

<h2>Method: Intersectionally Fair Graph Augmentation</h2>

<p>We reformulate the fairness objective of graph augmentation to operate over intersectional demographic groups formed by combining two or more sensitive attributes. The core concepts are:</p>

<ul>
  <li><strong>IDPR (Intersectional Demographic Parity in Recommendation):</strong> A fairness criterion requiring that recommendation utility (NDCG) be equal across all intersectional subgroups simultaneously, rather than just between two groups.</li>
  <li><strong>ε-IDPR:</strong> A practical relaxation of the strict IDPR constraint that allows a tolerance ε in the parity requirement, making the optimisation tractable while retaining meaningful fairness guarantees.</li>
  <li><strong>Loss function:</strong> The augmentation is guided by a two-term objective — a fairness loss <strong>L<sub>fair</sub></strong> minimising the utility disparity Δ across intersectional subgroups, and a distance loss <strong>L<sub>dist</sub></strong> controlling how much the augmented graph departs from the original.</li>
</ul>

<h3>Sampling Policies</h3>

<p>To make augmentation tractable, candidate edges are drawn from a restricted pool defined by sampling policies applied independently on the user and item side:</p>

<table class="datasets-table">
  <thead>
    <tr>
      <th>Policy</th>
      <th>Side</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>ZN</strong></td>
      <td>User</td>
      <td>Users with no relevant items in the top-k list (NDCG@k = 0)</td>
    </tr>
    <tr>
      <td><strong>FR</strong></td>
      <td>User</td>
      <td>Users furthest from the advantaged group in graph distance</td>
    </tr>
    <tr>
      <td><strong>IR</strong></td>
      <td>User</td>
      <td>Users selected by inter-group distance criteria</td>
    </tr>
    <tr>
      <td><strong>IP</strong></td>
      <td>Item</td>
      <td>Items most preferred by the disadvantaged group</td>
    </tr>
    <tr>
      <td><strong>IT</strong></td>
      <td>Item</td>
      <td>Items with high inter-group transferability</td>
    </tr>
    <tr>
      <td><strong>PR</strong></td>
      <td>Item</td>
      <td>Items selected by popularity-relative criteria</td>
    </tr>
  </tbody>
</table>

<h2>Experimental Setup</h2>

<p>We evaluate across five datasets that collectively cover sparse, medium-density, and dense interaction graphs in the music, movie, and short-video domains, using two intersectional sensitive attribute pairs (Gender × Age and One-hot Feat0 × One-hot Feat13).</p>

<h3>Datasets</h3>

<table class="datasets-table">
  <thead>
    <tr>
      <th></th>
      <th>LFM1M</th>
      <th>ML1M</th>
      <th>KRECS</th>
    </tr>
  </thead>
  <tbody>
    <tr><td># Users</td><td>4,546</td><td>6,040</td><td>1,401</td></tr>
    <tr><td># Items</td><td>12,492</td><td>3,706</td><td>3,060</td></tr>
    <tr><td># Interactions</td><td>1,082,132</td><td>1,000,209</td><td>1,502,531</td></tr>
    <tr><td>Min. Degree per user</td><td>20</td><td>20</td><td>229</td></tr>
    <tr><td>Density</td><td>1.90%</td><td>4.47%</td><td>35.01%</td></tr>
    <tr><td>Sensitive Attribute</td><td>Gender | Age</td><td>Gender | Age</td><td>One-hot Feat0 | One-hot Feat13</td></tr>
    <tr><td>Subgroup M|Y / 0|0</td><td>44.3%</td><td>41.2%</td><td>58.7%</td></tr>
    <tr><td>Subgroup M|O / 1|0</td><td>34.2%</td><td>30.5%</td><td>31.8%</td></tr>
    <tr><td>Subgroup F|Y / 0|1</td><td>16.5%</td><td>15.5%</td><td>5.2%</td></tr>
    <tr><td>Subgroup F|O / 1|1</td><td>5.1%</td><td>12.8%</td><td>4.3%</td></tr>
  </tbody>
</table>

<h3>GCF Models</h3>

<p>We evaluate five state-of-the-art graph collaborative filtering models: <strong>HMLET</strong>, <strong>LightGCN</strong>, <strong>NGCF</strong>, <strong>SGL</strong>, and <strong>XSimGCL</strong>.</p>

<h2>RQ1: Intersectional Fairness</h2>

<p>The first research question asks whether our fairness-aware augmentation effectively reduces utility disparity Δ across intersectional subgroups on the three base datasets (LFM1M, ML1M, KRECS).</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/table2_rq1_intersectional_fairness_results.png" alt="Table 2: Intersectional fairness results across five GCF models and three datasets" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Table 2:</strong> Recommendation utility (NDCG) and utility disparity (Δ) for the base model and after augmentation across five GCF models and three datasets. Lower Δ indicates better intersectional fairness.
  </figcaption>
</figure>

<ul>
  <li><strong>Model-dependence:</strong> The effectiveness of fair graph augmentation varies substantially across GCF models — augmentation reliably reduces Δ on some architectures while having limited or no impact on others.</li>
  <li><strong>Utility preservation:</strong> In settings where fairness improves, recommendation utility (NDCG) is largely preserved or increased, showing the augmentation does not trade off quality against fairness in the intersectional case.</li>
  <li><strong>Dataset sensitivity:</strong> Results differ across LFM1M, ML1M, and KRECS, pointing to a strong interaction between dataset properties (density, scale) and mitigation effectiveness.</li>
</ul>

<h2>RQ2: Scale and Density</h2>

<p>To isolate the effect of interaction density and dataset scale, we introduce two additional datasets derived from MovieLens 1M and KuaiRec with higher k-core thresholds, producing denser interaction graphs.</p>

<table class="datasets-table">
  <thead>
    <tr>
      <th></th>
      <th>ML1MD</th>
      <th>KRECB</th>
    </tr>
  </thead>
  <tbody>
    <tr><td># Users</td><td>2,595</td><td>7,101</td></tr>
    <tr><td># Items</td><td>1,829</td><td>8,720</td></tr>
    <tr><td># Interactions</td><td>741,478</td><td>10,155,233</td></tr>
    <tr><td>K-core Threshold</td><td>110</td><td>—</td></tr>
    <tr><td>Min. Degree per user</td><td>110</td><td>79</td></tr>
    <tr><td>Density</td><td>15.61%</td><td>16.40%</td></tr>
    <tr><td>Sensitive Attribute</td><td>Gender | Age</td><td>One-hot Feat0 | One-hot Feat13</td></tr>
    <tr><td>Subgroup M|Y / 0|0</td><td>46.7%</td><td>55.4%</td></tr>
    <tr><td>Subgroup M|O / 1|0</td><td>29.0%</td><td>34.1%</td></tr>
    <tr><td>Subgroup F|Y / 0|1</td><td>14.0%</td><td>5.5%</td></tr>
    <tr><td>Subgroup F|O / 1|1</td><td>10.3%</td><td>4.9%</td></tr>
  </tbody>
</table>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/table4_rq2_size_density_results.png" alt="Table 4: Fairness results on ML1MD and KRECB datasets" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Table 4:</strong> Utility (NDCG) and disparity (Δ) for the base model and after augmentation on the denser ML1MD and KRECB datasets across all five GCF models.
  </figcaption>
</figure>

<ul>
  <li><strong>Density amplifies model-dependence:</strong> The pattern of which models benefit from augmentation shifts when density increases, confirming that dataset properties interact non-trivially with the augmentation mechanism.</li>
  <li><strong>Large-scale feasibility:</strong> Our method successfully operates on KRECB with over 10 million interactions, demonstrating scalability beyond the small-scale datasets used in prior work.</li>
</ul>

<h2>RQ3: Augmentation Interpretability</h2>

<p>We analyse the structural characteristics of the edges added during augmentation using three graph-level metrics: node degree (DEG), degree-type ratio (DTY), and inter-group distance (IGD). Edges are grouped into quartiles Q1–Q4 per metric and per intersectional subgroup.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/figure2_added_edges_distribution_gender_age.png" alt="Figure 2: Added edges distribution for Gender×Age groups across ML1M, LFM1M, ML1MD" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 2:</strong> Distribution of added edges over quartiles (Q1–Q4) for Gender×Age intersectional groups (Older Males, Younger Males, Older Females, Younger Females) across ML1M, LFM1M, and ML1MD, split by DEG, DTY, and IGD graph metrics.
  </figcaption>
</figure>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/figure3_added_edges_distribution_onehot.png" alt="Figure 3: Added edges distribution for One-hot Feat0×Feat13 groups in KRECB and KRECS" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 3:</strong> Distribution of added edges over quartiles (Q1–Q4) for One-hot Feat0 × One-hot Feat13 groups (0|0, 0|1, 1|0, 1|1) in KRECB and KRECS, split by DEG, DTY, and IGD graph metrics.
  </figcaption>
</figure>

<ul>
  <li><strong>Structural concentration:</strong> Augmented edges do not distribute uniformly — they concentrate in interpretable structural regions of the graph, driven by the degree and type characteristics of the connected nodes.</li>
  <li><strong>Subgroup-specific patterns:</strong> Different intersectional subgroups receive edges in different graph regions, revealing that the augmentation implicitly adapts to each group's structural position.</li>
  <li><strong>Consistent across dataset types:</strong> The DEG/DTY/IGD patterns are broadly consistent between Gender×Age datasets and One-hot attribute datasets, suggesting the interpretability findings generalise across attribute types.</li>
</ul>

<h2>RQ4: Distributional Shift</h2>

<p>We investigate whether the gap between validation-set and test-set fairness gains can be predicted from the distributional shift between the two splits, measured via energy distance.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/figure4_energy_distance_vs_fairness_gain.png" alt="Figure 4: Scatter plot of energy distance vs ratio of fairness gains" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 4:</strong> Scatter plot of validation–test energy distance versus the ratio of fairness gains (test / validation). Spearman ρ = −0.19 (p = 0.000343).
  </figcaption>
</figure>

<div class="highlight-box">
<p><strong>Finding:</strong> A statistically significant negative correlation (Spearman ρ = −0.19, p = 0.000343) is observed between the validation–test energy distance and the ratio of fairness gains. Larger distributional shifts between validation and test sets are associated with weaker generalisation of fairness improvements from validation to test, providing a practical signal for anticipating mitigation reliability.</p>
</div>

<h2>Additional Analyses</h2>

<h3>Sampling Policy Ablation</h3>

<p>We ablate all 15 combinations of user-side and item-side sampling policies across five GCF models and five datasets to identify which policy combinations are most consistently effective.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/figure5_utility_disparity_sampling_policies.png" alt="Figure 5: Heatmap of utility disparity across sampling policy combinations" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 5:</strong> Heatmap of utility disparity Δ across 5 GCF models × 5 datasets × 15 sampling policy combinations (validation set). Darker cells indicate lower disparity (better fairness).
  </figcaption>
</figure>

<h3>Leaky Coefficient Ablation</h3>

<p>We study how the leaky coefficient α — which controls the sharpness of the augmentation objective — affects the resulting fairness level Δ across all five datasets.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/intersectional-fa4gcf/figure6_fairness_vs_leaky_coefficient.png" alt="Figure 6: Fairness level as a function of leaky coefficient alpha" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 6:</strong> Fairness level Δ as a function of leaky coefficient α (0.05, 0.1, 0.2, 0.5) across all five datasets, showing sensitivity of the mitigation to this hyperparameter.
  </figcaption>
</figure>

<h3>Comparison with ITFR</h3>

<p>We compare our method against the ITFR fairness-aware baseline on LightGCN across all five datasets. Bold values indicate the best result per metric per dataset; asterisked (*) values signal low absolute utility.</p>

<table class="results-table">
  <thead>
    <tr>
      <th></th>
      <th>LFM1M NDCG↑</th>
      <th>LFM1M Δ↓</th>
      <th>ML1M NDCG↑</th>
      <th>ML1M Δ↓</th>
      <th>ML1MD NDCG↑</th>
      <th>ML1MD Δ↓</th>
      <th>KRECS NDCG↑</th>
      <th>KRECS Δ↓</th>
      <th>KRECB NDCG↑</th>
      <th>KRECB Δ↓</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>ITFR</strong></td>
      <td>16.49</td>
      <td>0.56</td>
      <td>11.85</td>
      <td>0.28</td>
      <td>16.64</td>
      <td><strong>0.42</strong></td>
      <td>*4.29</td>
      <td><strong>0.19</strong></td>
      <td>*6.16</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td><strong>Ours</strong></td>
      <td><strong>17.67</strong></td>
      <td><strong>0.32</strong></td>
      <td><strong>12.62</strong></td>
      <td><strong>0.25</strong></td>
      <td><strong>20.33</strong></td>
      <td>0.64</td>
      <td>*6.29</td>
      <td>0.29</td>
      <td>*5.54</td>
      <td><strong>0.03</strong></td>
    </tr>
  </tbody>
</table>

<p>Our method achieves superior utility on four of five datasets and the best fairness on three of five, while ITFR wins on fairness for ML1MD and KRECS. No single method dominates across all configurations, highlighting the importance of dataset-aware method selection.</p>

<h2>Key Contributions</h2>

<ul class="contributions-list">
  <li><strong>Intersectional Fairness Formulation:</strong> First extension of fairness-aware graph augmentation beyond binary setups, introducing the IDPR criterion and its ε-IDPR relaxation for intersectional demographic groups.</li>
  <li><strong>Large-scale Evaluation:</strong> Comprehensive experiments across five datasets spanning densities from 1.90% to 35.01% and up to 10 million interactions, demonstrating scalability and dataset sensitivity of the method.</li>
  <li><strong>Interpretable Augmentation Patterns:</strong> Structural analysis via DEG, DTY, and IGD metrics reveals that augmented edges concentrate in interpretable graph regions, offering actionable insights into fairness-oriented graph modifications.</li>
  <li><strong>Distributional Shift Indicator:</strong> Evidence that energy distance between validation and test distributions predicts generalisation of fairness gains (Spearman ρ = −0.19), providing a practical diagnostic signal.</li>
  <li><strong>Ablation and Baseline Comparison:</strong> Thorough ablation of 15 sampling policy combinations and comparison with ITFR, clarifying conditions under which each approach is preferable.</li>
</ul>
