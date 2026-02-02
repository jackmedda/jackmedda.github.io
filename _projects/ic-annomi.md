---
title: "Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental Health"
collection: projects
permalink: /projects/ic-annomi/
date: 2024-07-29
year: 2024
venue: "International Conference on NLP & AI for Cyber Security"
venue_short: "NLPAICs"

# hero_image: "/images/projects/ic-annomi/figure_1.png"
# teaser: "/images/projects/ic-annomi/figure_1.png"

authors:
  - "Vivek Kumar"
  - "Eirini Ntoutsi"
  - "Pushpraj Singh Rajwat"
  - "Giacomo Medda"
  - "Diego Reforgiato Recupero"

author_links:
  Vivek Kumar: "https://scholar.google.com/citations?user=vivek_kumar"
  Eirini Ntoutsi: "https://www.unibw.de/code/team/ntoutsi"
  Pushpraj Singh Rajwat: "#"
  Giacomo Medda: "https://jackmedda.github.io/"
  Diego Reforgiato Recupero: "https://people.unica.it/diegoreforgiato/"

keywords:
  - Motivational Interviewing
  - Large Language Models
  - Mental Health
  - Data Augmentation
  - Bias Mitigation
  - Healthcare NLP
  - ChatGPT

doi: "10.48550/arXiv.2403.07300"
paperurl: "https://aclanthology.org/2024.nlpaics-1.26/"
code: "https://github.com/Exploring-MI/IC-AnnoMI"

abstract: |
  Large language models (LLMs) have shown promising capabilities in healthcare analysis but face several challenges like hallucinations, parroting, and bias manifestation. These challenges are exacerbated in complex, sensitive, and low-resource domains. Therefore, in this work we introduce IC-AnnoMI, an expert-annotated motivational interviewing (MI) dataset built upon AnnoMI by generating in-context conversational dialogues leveraging LLMs, particularly ChatGPT. IC-AnnoMI employs targeted prompts accurately engineered through cues and tailored information, taking into account therapy style (empathy, reflection), contextual relevance, and false semantic change. Subsequently, the dialogues are annotated by experts, strictly adhering to the Motivational Interviewing Skills Code (MISC), focusing on both the psychological and linguistic dimensions of MI dialogues. We comprehensively evaluate the IC-AnnoMI dataset and ChatGPT's emotional reasoning ability and understanding of domain intricacies by modeling novel classification tasks employing several classical machine learning and current state-of-the-art transformer approaches. Finally, we discuss the effects of progressive prompting strategies and the impact of augmented data in mitigating the biases manifested in IC-AnnoMI.

bibtex: |
  @inproceedings{kumar2024unlocking,
    author = {Kumar, Vivek and Ntoutsi, Eirini and Rajwat, Pushpraj Singh and Medda, Giacomo and Reforgiato Recupero, Diego},
    title = {Unlocking LLMs: Addressing Scarce Data and Bias Challenges in Mental Health and Therapeutic Counselling},
    booktitle = {Proceedings of the 1st International Conference on NLP \& AI for Cyber Security},
    pages = {238--251},
    year = {2024},
    url = {https://aclanthology.org/2024.nlpaics-1.26/}
  }
---

<section id="motivation">
  <h2>Motivation</h2>
  <div class="highlight-box">
    <p>
      <strong>Why focus on MI and LLMs?</strong> Motivational Interviewing (MI) is a proven therapeutic technique 
      for behavioral change, but access is limited due to cost and clinician availability. LLMs could help 
      democratize access, but they face critical challenges in sensitive healthcare domains: hallucinations, 
      stochastic parroting, and bias manifestation.
    </p>
  </div>
  <p>
    Mental health domains suffer from <strong>data scarcity</strong>—there are few publicly available resources 
    that could help develop responsible AI systems. This work addresses this gap by creating high-quality 
    synthetic MI dialogues using LLMs and rigorous expert annotation.
  </p>
</section>

<section id="dataset">
  <h2>IC-AnnoMI Dataset</h2>
  
  <p>
    <strong>IC-AnnoMI</strong> is an expert-annotated motivational interviewing dataset built upon AnnoMI by generating 
    in-context conversational dialogues using ChatGPT with carefully engineered prompts.
  </p>
  
  <h3>Data Generation Process</h3>
  <ol>
    <li><strong>Progressive Prompting:</strong> Iteratively refine prompts until output quality matches original MI dialogues</li>
    <li><strong>Context-Aware Generation:</strong> Consider therapy style (empathy, reflection), contextual relevance, and semantic consistency</li>
    <li><strong>Expert Annotation:</strong> Strict adherence to the Motivational Interviewing Skills Code (MISC)</li>
  </ol>
  
  <h3>Annotation Dimensions</h3>
  <table class="styled-table">
    <thead>
      <tr><th>Dimension</th><th>Components</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Psychological (MIpsych)</strong></td>
        <td>Empathy, Non-judgmental attitude, Therapist competence, Ethical conduct</td>
      </tr>
      <tr>
        <td><strong>Linguistic (MIlinguist)</strong></td>
        <td>Language comprehension, MI structure, False semantic change, Contextual reasoning</td>
      </tr>
    </tbody>
  </table>
</section>

<section id="methodology">
  <h2>Methodology</h2>
  
  <h3>Progressive Prompt Engineering</h3>
  <p>
    We developed a systematic approach to prompt refinement:
  </p>
  <ul>
    <li>Initial prompts based on MI dialogue context, plausibility, and quality requirements</li>
    <li>Manual evaluation of outputs for inconsistencies</li>
    <li>Iterative tuning until generated quality matches original MI dialogues</li>
  </ul>
  
  <h3>MISC-Based Annotation</h3>
  <p>
    Annotations are grounded in the <strong>Manual for the Motivational Interviewing Skill Code (MISC)</strong>, 
    covering both psychological and linguistic dimensions:
  </p>
  <ul>
    <li><strong>Empathy:</strong> Therapist's ability to demonstrate understanding through active listening and reflective statements</li>
    <li><strong>Non-judgmental attitude:</strong> Creating a safe, supportive environment for clients</li>
    <li><strong>Competence:</strong> Therapist's proficiency in applying MI techniques effectively</li>
    <li><strong>Ethical conduct:</strong> Prioritizing client well-being, autonomy, and confidentiality</li>
  </ul>
</section>

<section id="experiments">
  <h2>Evaluation</h2>
  
  <h3>Classification Tasks</h3>
  <p>
    We model novel classification tasks to evaluate ChatGPT's capabilities:
  </p>
  <ul>
    <li>Identifying high- vs. low-quality MI dialogues</li>
    <li>Assessing emotional reasoning ability</li>
    <li>Understanding of domain intricacies</li>
    <li>Detecting biases (contextual, sampling, class imbalance)</li>
  </ul>
  
  <h3>Models Evaluated</h3>
  <ul>
    <li>Classical machine learning approaches</li>
    <li>State-of-the-art transformer models</li>
  </ul>
</section>

<section id="results">
  <h2>Key Findings</h2>
  
  <div class="highlight-box">
    <p>
      <strong>Main Contribution:</strong> IC-AnnoMI provides the MI community with a comprehensive dataset 
      and valuable insights for using LLMs in empathetic text generation for conversational therapy 
      in <em>supervised settings</em>.
    </p>
  </div>
  
  <h3>Insights on LLM Usage in Healthcare</h3>
  <ul>
    <li><strong>Progressive prompting helps:</strong> Iterative refinement significantly improves dialogue quality</li>
    <li><strong>Augmented data mitigates bias:</strong> Synthetic data can help address class imbalance issues</li>
    <li><strong>Human supervision is critical:</strong> Unsupervised LLM use in sensitive domains poses risks</li>
    <li><strong>Expert collaboration needed:</strong> Domain experts are essential for responsible LLM implementation</li>
  </ul>
  
  <h3>Risks and Recommendations</h3>
  <p>
    We discuss the dangers of unsupervised LLM employment in healthcare, emphasizing:
  </p>
  <ul>
    <li>Need for collaboration with domain experts</li>
    <li>Importance of human supervision</li>
    <li>Responsible implementation across healthcare settings</li>
  </ul>
</section>

<section id="contributions">
  <h2>Contributions</h2>
  <ul>
    <li><strong>Tailored prompting approach:</strong> Progressive prompt-based augmentation techniques for in-context MI dialogue generation</li>
    <li><strong>Expert annotation scheme:</strong> Rigorous annotation covering psychological and linguistic aspects grounded on MISC</li>
    <li><strong>Comprehensive evaluation:</strong> Baselines and analysis of LLM capabilities and limitations in sensitive domains</li>
    <li><strong>Public resource:</strong> IC-AnnoMI dataset and source code publicly available</li>
  </ul>
</section>

