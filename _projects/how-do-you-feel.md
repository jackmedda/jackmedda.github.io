---
title: "How do you feel? Information Retrieval in Psychotherapy and Fair Ranking Assessment"
collection: projects
permalink: /projects/how-do-you-feel/
date: 2023-04-02
year: 2023
venue: "Workshop on Algorithmic Bias in Search and Recommendation (Bias@ECIR 2023)"
venue_short: "Bias@ECIR 2023"

# Hero/Banner image
hero_image: "/images/projects/how-do-you-feel/figure_1_chart_page8.png"
teaser: "/images/projects/how-do-you-feel/figure_1_chart_page8.png"

authors:
  - "Vivek Kumar"
  - "Giacomo Medda"
  - "Diego Reforgiato Recupero"
  - "Daniele Riboni"
  - "Rim Helaoui"
  - "Gianni Fenu"

author_links:
  Vivek Kumar: "https://scholar.google.com/citations?user=ZwN8P3AAAAAJ"
  Giacomo Medda: "https://jackmedda.github.io/"
  Diego Reforgiato Recupero: "https://scholar.google.com/citations?user=R9DRwNwAAAAJ"
  Daniele Riboni: "https://scholar.google.com/citations?user=I3lVAAcAAAAJ"
  Rim Helaoui: "https://scholar.google.com/citations?user=IEfJfEEAAAAJ"
  Gianni Fenu: "https://web.unica.it/unica/page/it/gianni_fenu"

author_note: "† Vivek Kumar and Giacomo Medda contributed equally to this work"

keywords:
  - Information Retrieval
  - Fairness
  - Psychology
  - Motivational Interviewing
  - Ranking
  - Mental Health

# Links
doi: "10.1007/978-3-031-37249-0_10"
paperurl: "/files/4__Bias_Workshop__ECIR_.pdf"
code: "https://github.com/jackmedda/BIAS-FairAnnoMI"

# Abstract
abstract: |
  The recent pandemic Coronavirus Disease 2019 (COVID-19) led to an unexpectedly imposed social isolation, causing an enormous disruption of daily routines for the global community and posing a potential risk to the mental well-being of individuals. However, resources for supporting people with mental health issues remain extremely limited, raising the matter of providing trustworthy and relevant psychotherapeutic content publicly available. To bridge this gap, this paper investigates the application of information retrieval in the mental health domain to automatically filter therapeutical content by estimated quality. We have used AnnoMI, an expert annotated counseling dataset composed of high- and low-quality Motivational Interviewing therapy sessions. First, we applied state-of-the-art information retrieval models to evaluate their applicability in the psychological domain for ranking therapy sessions by estimated quality. Then, given the sensitive psychological information associated with each therapy session, we analyzed the potential risk of unfair outcomes across therapy topics, i.e., mental issues, under a common fairness definition. Our experimental results show that the employed ranking models are reliable for systematically ranking high-quality content above low-quality one, while unfair outcomes across topics are model-dependent and associated low-quality content distribution. Our findings provide preliminary insights for applying information retrieval in the psychological domain, laying the foundations for incorporating publicly available high-quality resources to support mental health.

# BibTeX citation
bibtex: |
  @inproceedings{kumar2023feel,
    author = {Kumar, Vivek and Medda, Giacomo and Reforgiato Recupero, Diego and Riboni, Daniele and Helaoui, Rim and Fenu, Gianni},
    title = {How Do You Feel? Information Retrieval in Psychotherapy and Fair Ranking Assessment},
    booktitle = {Advances in Bias and Fairness in Information Retrieval - 4th International Workshop, BIAS 2023},
    series = {Communications in Computer and Information Science},
    volume = {1840},
    pages = {119--133},
    publisher = {Springer},
    year = {2023},
    doi = {10.1007/978-3-031-37249-0_10}
  }
---

<h2>Motivation</h2>

The COVID-19 pandemic forced people into prolonged isolation, limiting human interactions and leading to increased psychological issues such as anxiety and depression. While psychologists and remote therapy access became increasingly important, these services remain cost-intensive and often inaccessible. Furthermore, common people lack familiarity with mental health issues, putting them at risk of encountering misinformative content online.

This study aims to facilitate individuals in autonomously evaluating therapeutical content personalized for their psychological issues through **information retrieval (IR)** methods. IR can help address mental health issues by:
- Efficiently providing relevant and reliable information
- Personalizing treatment options based on specific needs
- Monitoring mental health trends in the population

<h2>Problem Formulation</h2>

We model an IR task where:
- **Documents** = therapy sessions (specifically, therapist utterances)
- **Queries** = psychological topics (mental health issues)
- **Relevance labels** = therapy quality (high/low)

Given a query representing a psychological disease, the system retrieves therapeutical content ranked by estimated quality, with the goal of providing high-quality content in higher positions to support patients.

<h3>Fairness Definition</h3>

We operationalize **Demographic/Statistical Parity**: the likelihood of relevant content should be the same for any psychological disease. Unfairness is measured as the disparity of ranking utility (NDCG@k) across topics:

$$DS = \frac{1}{\binom{|S|}{2}} \sum_{1 \leq i < j \leq |S|} \|NDCG_i@k - NDCG_j@k\|_2^2$$

<h2>Dataset: AnnoMI</h2>

We used **AnnoMI**, the first publicly accessible dataset in the psychology domain, containing:
- 133 expert-annotated Motivational Interviewing (MI) therapy sessions
- 44 psychological topics (e.g., smoking cessation, anxiety management)
- 9,695 utterances labeled by therapy quality

After preprocessing (filtering utterances < 5 tokens, removing topics without both quality classes), we obtained **3,984 utterances** across **8 psychological topics**.

| Topic | Low Quality | High Quality |
|-------|-------------|--------------|
| Adhering to Medical Procedure (AMP) | 2.36% | 7.83% |
| Asthma Management (AM) | 0.66% | 3.12% |
| Compliance with Rules (CR) | 0.43% | 9.50% |
| Diabetes Management (DM) | 0.18% | 11.45% |
| Managing Life (MF) | 0.86% | 12.18% |
| Reducing Alcohol Consumption (RAC) | 7.14% | 24.95% |
| RAC—Smoking Cessation (RAC—SC) | 0.51% | 0.66% |
| Smoking Cessation (SC) | 3.70% | 14.49% |

<h2>Models</h2>

We evaluated a diverse set of neural rankers covering different levels of network complexity:
- **Arc-I, Arc-II** — Convolutional architectures for text matching
- **DRMMTKS** — Deep Relevance Matching Model
- **DUET** — Distributed and local text representations
- **Dense Baseline, Naive** — MatchZoo baselines
- **HBMP** — Hierarchical Bi-LSTM with Max Pooling
- **KNRM** — Kernel-based Neural Ranking Model
- **TFR-BERT** — BERT-based ranker (most complex)

<h2>Results</h2>

<h3>RQ1: Ranking Utility in Psychological Domain</h3>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/how-do-you-feel/figure_1_chart_page8.png" alt="NDCG distribution across topics" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <figcaption style="margin-top: 0.5rem; color: #666; font-size: 0.9rem;">
    <strong>Figure 1:</strong> Distribution of NDCG@k across topics for each ranker. Higher NDCG denotes higher utility.
  </figcaption>
</figure>

**Key findings:**
- All models report rankings of high utility on therapeutical data
- DRMMTKS and TFR-BERT are most robust across different k values
- No clear relationship between model complexity and performance

<h3>RQ2: Unfairness Levels across Topics</h3>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/how-do-you-feel/figure_2_chart_page9.png" alt="Unfairness disparity across models" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <figcaption style="margin-top: 0.5rem; color: #666; font-size: 0.9rem;">
    <strong>Figure 2:</strong> DS (average pairwise NDCG difference) at different relevance levels. Lower values are fairer.
  </figcaption>
</figure>

**Key findings:**
- **DRMMTKS, TFR-BERT, HBMP** report the best fairness levels
- **DUET, Arc-I** exhibit the highest unfairness
- Even the fairest models show ~0.1 NDCG disparity between topic pairs
- Top-3 rankings reveal significant utility variance, meaning some queries result in low-quality content

<h3>RQ3: Systematic Negative Impact</h3>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/how-do-you-feel/figure_3_chart_page10.png" alt="NDCG heatmap per topic and model" style="max-width: 100%; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);">
  <figcaption style="margin-top: 0.5rem; color: #666; font-size: 0.9rem;">
    <strong>Figure 3:</strong> NDCG per topic (column) and ranker (row) at different relevance levels. Darker = higher utility.
  </figcaption>
</figure>

**Key findings:**
- Topics with higher representation of high-quality utterances (CR, DM, MF) consistently achieve better rankings
- Topics with >1% low-quality documents (SC, RAC, AMP) show lower utility
- **No systematic negative impact on specific diseases** — at least one model provides optimal utility for each query

<h2>Conclusions</h2>

1. **IR is applicable to psychological domain**: All ranking models achieved high utility on therapeutical counseling data
2. **Fairness issues exist**: Significant utility disparity across topics for most models
3. **Unfairness correlates with data distribution**: Topics with more low-quality utterances show lower ranking performance
4. **No systematic bias**: Different models exhibit varying performance across topics

<h3>Limitations</h3>

- Small dataset size (AnnoMI is the only publicly available resource)
- Individual utterances used instead of whole therapy sessions
- Topics without both quality classes were excluded

<h3>Future Work</h3>

- Data augmentation techniques to extend AnnoMI
- Unfairness mitigation procedures
- Incorporation of world knowledge (knowledge graphs)
- Extension to entire therapy session ranking
