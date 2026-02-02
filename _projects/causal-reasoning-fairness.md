---
title: "Causal reasoning for algorithmic fairness in voice controlled cyber-physical systems"
collection: projects
permalink: /projects/causal-reasoning-fairness/
date: 2023-03-21
year: 2023
venue: "Pattern Recognition Letters"
venue_short: "PRLetters 2023"

# Hero/Banner image
hero_image: "/images/projects/causal-reasoning-fairness/fig_p3_1.jpeg"
teaser: "/images/projects/causal-reasoning-fairness/fig_p3_1.jpeg"

authors:
  - "Gianni Fenu"
  - "Mirko Marras"
  - "Giacomo Medda"
  - "Giacomo Meloni"

author_links:
  Gianni Fenu: "https://web.unica.it/unica/page/it/gianni_fenu"
  Mirko Marras: "https://www.mirkomarras.com/"
  Giacomo Medda: "https://jackmedda.github.io/"
  Giacomo Meloni: "https://scholar.google.com/citations?user=ESsuzTwAAAAJ"

keywords:
  - Security
  - Authentication
  - Voice biometrics
  - Fairness
  - Speaker recognition
  - Causal reasoning
  - Explainability
  - Cyber-physical systems

# Links
doi: "10.1016/j.patrec.2023.03.014"
paperurl: "https://www.sciencedirect.com/science/article/pii/S016786552300079X"
code: "https://bit.ly/EA-PRLETTERS"

# Abstract
abstract: |
  Voice biometrics are increasingly being exploited for authentication in voice controlled cyber-physical systems. In recent studies, speaker recognition systems have shown to exhibit different performance across demographic groups. However, understanding the reasons behind disparate behavior is still challenging and few works have investigated the causes. In this paper, we propose an explanatory framework aimed to understand how the model performs as voice characteristics change. We evaluate two state-of-the-art speaker encoders on a public large-scale data set, systematically analyzing the impact of more than 20 voice characteristics on the security of the models. Findings of this study, while highlighting the importance of studying fairness, show that voice characteristics related to linguistic aspects are those that mainly explain the unfairness in security.

# BibTeX citation
bibtex: |
  @article{fenu2023causal,
    author = {Fenu, Gianni and Marras, Mirko and Medda, Giacomo and Meloni, Giacomo},
    title = {Causal reasoning for algorithmic fairness in voice controlled cyber-physical systems},
    journal = {Pattern Recognition Letters},
    volume = {168},
    pages = {131--137},
    year = {2023},
    publisher = {Elsevier},
    doi = {10.1016/j.patrec.2023.03.014}
  }
---

<h2>Motivation</h2>

<p>Voice biometrics are increasingly being used for authentication in <strong>voice controlled cyber-physical systems</strong>, such as smart home devices and conversational agents. However, recent studies have shown that speaker recognition systems exhibit <strong>disparate impacts across demographic groups</strong>.</p>

<ul>
  <li>Differences in authentication security rates across gender, age, and language groups</li>
  <li>Prior works focused on detecting unfairness but not on <em>understanding its causes</em></li>
  <li>Mitigation strategies require knowing <em>why</em> unfairness occurs</li>
</ul>

<div class="highlight-box">
<p><strong>Key Insight:</strong> We propose an explanatory framework to understand how speaker recognition model performance varies as voice characteristics change, going beyond mere group membership to identify the fine-grained voice properties that cause unfairness.</p>
</div>

<h2>Method Overview</h2>

<p>Our explanatory framework consists of two main phases:</p>

<ol>
  <li><strong>Speaker Recognition Model Creation:</strong> Training state-of-the-art speaker encoders (ResNet-34 and X-Vector) on the FairVoice dataset</li>
  <li><strong>Exploratory Analysis:</strong> Building surrogate models to explain how voice characteristics impact authentication security</li>
</ol>

<figure>
  <img src="/images/projects/causal-reasoning-fairness/fig_p3_1.jpeg" alt="Framework Overview" style="width:100%; max-width:800px;">
  <figcaption><strong>Figure 1:</strong> Explanatory framework architecture showing the connection between speaker encoders, voice characteristics extraction, and the surrogate model for analysis.</figcaption>
</figure>

<h3>Voice Characteristics</h3>

<p>We analyze over 20 voice characteristics, categorized into:</p>

<table class="datasets-table">
  <thead>
    <tr>
      <th>Category</th>
      <th>Type</th>
      <th>Characteristics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Protected</td>
      <td>Demographic</td>
      <td>Gender, Age Range, Language</td>
    </tr>
    <tr>
      <td>Non-Protected</td>
      <td>Quantitative</td>
      <td>RMS, dBFS, SNR</td>
    </tr>
    <tr>
      <td>Non-Protected</td>
      <td>Qualitative</td>
      <td>HNR, F0, Formants (F1-F4), Jitter, Shimmer</td>
    </tr>
    <tr>
      <td>Non-Protected</td>
      <td>Dialogue</td>
      <td>Syllables, Pauses, Speech Rate</td>
    </tr>
  </tbody>
</table>

<h3>Experimental Setup</h3>

<table class="datasets-table">
  <thead>
    <tr>
      <th>Component</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Dataset</strong></td>
      <td>FairVoice (derived from Common Voice) - 6,321 English + 1,298 Spanish speakers</td>
    </tr>
    <tr>
      <td><strong>Speaker Encoders</strong></td>
      <td>ResNet-34 (spectrogram input) and X-Vector (filter bank input) with GhostVLAD pooling</td>
    </tr>
    <tr>
      <td><strong>Surrogate Model</strong></td>
      <td>Random Forest (achieving F1 and AUC close to 1)</td>
    </tr>
    <tr>
      <td><strong>Metric</strong></td>
      <td>False Acceptance Rate (FAR) as security measure</td>
    </tr>
  </tbody>
</table>

<h2>Key Results</h2>

<p>Our experiments addressed three research questions:</p>

<h3>RQ1: Relationship between explanatory variables</h3>

<figure>
  <img src="/images/projects/causal-reasoning-fairness/fig_p5_1.jpeg" alt="Correlation Heatmap" style="width:100%; max-width:600px;">
  <figcaption><strong>Figure 2:</strong> Correlation heatmap between voice characteristics showing significant relationships between gender and vocal features like F0, formants, jitter, and shimmer.</figcaption>
</figure>

<ul>
  <li><strong>High correlation</strong> between gender and voice characteristics like F0, formants (F1-F4), jitter, and shimmer</li>
  <li><strong>Age and language</strong> do not show significant correlation with other speech covariates</li>
</ul>

<h3>RQ2: Influence of speech covariates on performance</h3>

<figure>
  <img src="/images/projects/causal-reasoning-fairness/fig_p6_2.jpeg" alt="Protected Class Flipping Analysis" style="width:100%; max-width:800px;">
  <figcaption><strong>Figure 3:</strong> Effect of flipping protected attributes on predicted FAR for both speaker encoders. Language flipping shows the strongest impact on security predictions.</figcaption>
</figure>

<ul>
  <li>Formants (F1, F3, F4) and fundamental frequency (F0) are the <strong>most important variables</strong> for both speaker encoders</li>
  <li>Protected attributes are <strong>not directly important</strong> for prediction, except for language in X-Vector</li>
  <li>Speech covariates related to <strong>vocal frequency aspects</strong> explain most of the disparate security estimates</li>
</ul>

<h3>RQ3: Impact of protected class changes</h3>

<figure>
  <img src="/images/projects/causal-reasoning-fairness/fig_p6_1.jpeg" alt="Feature Importance" style="width:100%; max-width:800px;">
  <figcaption><strong>Figure 4:</strong> Feature importance scores for ResNet-34 and X-Vector models. Formants (F1, F3, F4) and fundamental frequency (F0) are the most important variables.</figcaption>
</figure>

<ul>
  <li>Flipping <strong>gender and language</strong> classes resulted in significant FAR changes on ResNet-34</li>
  <li>Flipping <strong>language and age</strong> classes affected FAR predictions on X-Vector</li>
  <li><strong>Spoken language</strong> has the strongest impact on security of both speaker recognition systems</li>
</ul>

<h2>Conclusions</h2>

<p>Our findings reveal that:</p>

<ol>
  <li><strong>Causes of disparate performance</strong> go beyond mere membership to demographic groups</li>
  <li><strong>Fine-grained voice characteristics</strong> (some related to group membership) are the root causes of unfairness</li>
  <li>These characteristics can serve as <strong>proxies for protected attributes</strong> that are hard to retrieve due to privacy constraints</li>
</ol>

<div class="highlight-box">
<p><strong>Future Directions:</strong> Voice covariates can drive specific mitigation strategies (e.g., clustering users based on those characteristics) or input waveform transformations using autoencoders to make speaker encoders robust to these characteristics.</p>
</div>
