---
title: "Conformal Prediction for Statistically Reliable LLM-as-a-Judge in Recommender Systems"
collection: projects
permalink: /projects/conformal-llm-judge/
date: 2026-11-07
year: 2026
venue: "35th ACM International Conference on Information and Knowledge Management"
venue_short: "CIKM"

# Hero/Banner image (drivers of conformal uncertainty)
hero_image: "/images/projects/conformal-llm-judge/figure1_uncertainty_drivers.png"
teaser: "/images/projects/conformal-llm-judge/figure1_uncertainty_drivers.png"

authors:
  - "Maddalena Amendola"
  - "Giacomo Medda"
  - "Alessandro Soccol"
  - "Ludovico Boratto"
  - "Mirko Marras"
  - "Raffaele Perego"

author_links:
  Giacomo Medda: "https://jackmedda.github.io/"
  Alessandro Soccol: "https://alessandrosocc.github.io/"
  Ludovico Boratto: "https://www.ludovicoboratto.com/"
  Mirko Marras: "https://www.mirkomarras.com/"

keywords:
  - LLM-as-a-Judge
  - User Simulation
  - Conformal Prediction
  - Uncertainty Quantification
  - Food Recommendation

# Links
# doi: "10.1145/3799682.3839966"
# paperurl: "https://doi.org/10.1145/3799682.3839966"
code: "https://github.com/maddalena-amendola/conformal_prediction_recsys"

# Abstract
abstract: |
  LLM-as-a-judge has emerged as a promising strategy for evaluating recommender systems. Yet, treating simulated ratings as real feedback can make unreliable evaluation appear reliable. This risk is especially consequential in sensitive domains such as nutrition and health. In this paper, we treat the LLM-as-a-judge paradigm as a calibrated relevance simulation problem: an LLM-based simulator predicts human preferences from user and item representations, and conformal prediction converts them into uncertainty intervals. To account for the nature of recommendation, we introduce stratified conformal calibration by user rating variance. Experiments under three LLMs and seven conformal prediction methods show that point estimates of preferences hide failures on low-rating items, while conformal interval width is driven by user-level heterogeneity.

# BibTeX citation
bibtex: |
  @inproceedings{amendola2026conformal,
    author = {Amendola, Maddalena and Medda, Giacomo and Soccol, Alessandro and Boratto, Ludovico and Marras, Mirko and Perego, Raffaele},
    title = {Conformal Prediction for Statistically Reliable LLM-as-a-Judge in Recommender Systems},
    booktitle = {Proceedings of the 35th ACM International Conference on Information and Knowledge Management},
    series = {CIKM '26},
    year = {2026},
    location = {Rome, Italy},
    publisher = {ACM},
    doi = {10.1145/3799682.3839966}
  }
---

<h2>Motivation</h2>

<p>Evaluating recommender systems remains difficult because the available options are either <strong>efficient but biased</strong> or <strong>reliable but costly</strong>. Offline metrics such as recall and hit rate are cheap and repeatable, yet they only reflect the items users happened to encounter. Online experiments and user studies provide stronger evidence, but they are slow, expensive, and impractical for every design choice. Large Language Models (LLMs) have therefore emerged as flexible <strong>judges</strong> that simulate human preferences: given user and item data, they predict the judgment a user with that profile would provide.</p>

<p>Unfortunately, LLM judgments may appear confident while remaining biased, miscalibrated, or misaligned. Treating simulated ratings as real feedback can make unreliable evaluation <em>look</em> reliable — a risk that is especially consequential in sensitive domains such as nutrition and health.</p>

<div class="highlight-box">
<p><strong>The Gap:</strong> Conformal prediction can turn LLM evaluations into prediction intervals with finite-sample coverage guarantees, and has been applied to tasks such as text summarization. But recommendation is not a routine application: the target rating is a joint property of a <strong>user–item pair</strong>, so the same item may be relevant for one user and irrelevant for another. Uncertainty therefore depends on user rating behavior, and a single global calibration may merge <em>stable</em> users with <em>volatile</em> ones.</p>
</div>

<h2>Approach</h2>

<p>We frame LLM-as-a-judge as a <strong>calibrated relevance simulation problem</strong> in recipe recommendation. Given a user representation and a target recipe, the LLM predicts the rating the user would assign on a 1–5 scale. The simulated rating is treated as a proxy judgment, calibrated against held-out real ratings, and converted via conformal prediction into an <strong>interval</strong> that makes simulation uncertainty explicit.</p>

<p>We monitor two properties of these intervals: <strong>coverage</strong> (whether the interval contains the true rating) and <strong>efficiency</strong> (how narrow it is). If the true rating is 4, the interval [3, 5] succeeds and [1, 3] fails; among successful intervals, narrow ones such as [4, 4] or [3, 4] are far more useful than [1, 5].</p>

<h3>Human Judgment Simulation</h3>

<p>For each user–item pair $(u, i)$, the LLM-based simulator $f_\theta$ takes a user representation $r_u$ and item metadata $m_i$ and produces a score vector over the $K$ rating levels:</p>

$$z_{ui} = f_\theta(r_u, m_i) = \left(z_{ui}^{(1)}, \dots, z_{ui}^{(K)}\right) \in \mathbb{R}^K$$

<p>In practice, $z_{ui}$ corresponds to the raw logits of the valid rating tokens at the rating-generation position. The point prediction is the most supported rating, $\hat{y}_{ui} = \arg\max_k z_{ui}^{(k)}$, but the full score vector is what feeds conformal calibration.</p>

<h3>Post-hoc Conformal Calibration</h3>

<ul>
<li><strong>Nonconformity scoring:</strong> On a held-out calibration set of real ratings, a nonconformity function $s(z_{ui}, y_{ui})$ measures how inconsistent the simulator's scores are with the true rating — small if the simulator supports the real rating, large if it supports a distant one.</li>
<li><strong>Cutoff computation:</strong> For a target miscoverage $\alpha$ (we use $\alpha = 0.10$, i.e., 90% coverage), the threshold $\hat{q}_\alpha$ is the $\lceil (n+1)(1-\alpha) \rceil$-th smallest calibration score — the standard split-conformal finite-sample correction.</li>
<li><strong>Interval construction:</strong> For an unseen pair, every candidate rating is tested label-wise, keeping $C_\alpha(z_{ui}) = \{ y \in \mathcal{Y} : s(z_{ui}, y) \le \hat{q}_\alpha \}$. Under exchangeability, this guarantees $1 - \alpha \le P(y_{ui} \in C_\alpha) \le 1 - \alpha + \frac{1}{n+1}$. Continuous intervals are mapped back to valid Likert labels without breaking the guarantee.</li>
</ul>

<h3>User-Stratified Calibration</h3>

<p>A single global threshold mixes different uncertainty regimes: users with stable rating behavior need narrow intervals, while users with highly variable preferences need wider ones. We therefore assign each user to a <strong>stratum by their empirical rating standard deviation</strong> and compute a group-specific threshold $\hat{q}_\alpha^{(g)}$ from that stratum's calibration examples only. The same label-wise rule then applies with the group threshold, so the coverage guarantee holds <em>separately for each group</em>, avoiding forcing heterogeneous raters into one global uncertainty model.</p>

<h2>Experimental Setup</h2>

<ul>
<li><strong>Dataset:</strong> <strong>HUMMUS</strong>, a recipe recommendation dataset with explicit 1–5 star ratings (39,315 users, 507,335 recipes). Since ratings are heavily skewed toward high values, we sample 1,000 users from each of four rating-std groups — [0, 0.3), [0.3, 0.5), [0.5, 0.7), [0.7, ∞) — for 4,000 users total. Per user: the 2 most recent interactions for testing, the previous 2 for calibration, and the preceding 20 as prompt history.</li>
<li><strong>Judges:</strong> Three open-source LLMs — <strong>Qwen2.5-32B-Instruct</strong>, <strong>LLaMA-3.1-8B-Instruct</strong>, and <strong>Mistral-7B-Instruct-v0.3</strong> — chosen for reproducibility.</li>
<li><strong>Prompts:</strong> An <em>items-list</em> template (the 20 previously rated recipes with their ratings) and a <em>profile-based</em> template (a structured user profile built from the same history). Results were similar; items-list is reported.</li>
<li><strong>Conformal methods:</strong> CQR, Asymmetric CQR, CHR, LVD, Boosted CQR, Boosted LCP, and R2CCP, at $\alpha = 0.10$, averaged over 30 random seeds.</li>
</ul>

<h2>Results</h2>

<h3>RQ1: Point Estimates Hide Failures on Low-Rating Recipes</h3>

<p>At the aggregate level the three judges look comparable and reasonably accurate. Per-rating MAE tells a different story: all models <strong>fail badly on low-rated recipes</strong>, with errors above 3.6 when the true rating is 1 — they often assign very high scores to recipes users actually disliked. Aggregate performance is driven by the majority high-rating class and overstates the reliability of simulated ratings.</p>

<table class="results-table">
<thead>
<tr><th rowspan="2">Judge</th><th>Acc. ↑</th><th>MAE ↓</th><th>MAE@1 ↓</th><th>MAE@2 ↓</th><th>MAE@3 ↓</th><th>MAE@4 ↓</th><th>MAE@5 ↓</th></tr>
</thead>
<tbody>
<tr><td>LLaMA-3.1-8B</td><td>0.754</td><td>0.344</td><td>3.83</td><td>2.64</td><td>1.65</td><td>0.74</td><td>0.15</td></tr>
<tr><td>Mistral-7B</td><td>0.709</td><td>0.382</td><td>3.68</td><td>2.39</td><td>1.51</td><td>0.67</td><td>0.22</td></tr>
<tr><td>Qwen2.5-32B</td><td>0.748</td><td>0.340</td><td>3.74</td><td>2.50</td><td>1.60</td><td>0.71</td><td>0.15</td></tr>
</tbody>
</table>

<h3>RQ2: Which Conformal Methods Work Best?</h3>

<p>Under global (non-stratified) calibration, most methods reach the 90% coverage target, with Boosted CQR the only one consistently falling short. But coverage alone is not enough: CQR variants and CHR <strong>over-cover</strong> (~95–96%), producing conservative, unnecessarily wide intervals. Among methods meeting the target, <strong>R2CCP achieves the narrowest intervals</strong> (width &lt; 1) across all judges.</p>

<table class="results-table">
<thead>
<tr><th rowspan="2">Method</th><th colspan="2">LLaMA-3.1-8B</th><th colspan="2">Mistral-7B</th><th colspan="2">Qwen2.5-32B</th></tr>
<tr><th>Eff. ↓</th><th>Cov. ↑</th><th>Eff. ↓</th><th>Cov. ↑</th><th>Eff. ↓</th><th>Cov. ↑</th></tr>
</thead>
<tbody>
<tr><td>CQR</td><td>1.649</td><td>95.60</td><td>1.566</td><td>95.10</td><td>1.532</td><td>95.18</td></tr>
<tr><td>Asym. CQR</td><td>1.635</td><td>95.56</td><td>1.576</td><td>95.39</td><td>1.557</td><td>95.31</td></tr>
<tr><td>CHR</td><td>1.723</td><td>95.41</td><td>1.841</td><td>96.59</td><td>1.726</td><td>95.79</td></tr>
<tr><td><strong>R2CCP</strong></td><td><strong>0.981</strong></td><td>90.25</td><td><strong>0.959</strong></td><td>90.17</td><td><strong>0.939</strong></td><td>90.42</td></tr>
<tr><td>Boosted CQR</td><td>1.529</td><td>88.77</td><td>1.593</td><td>89.04</td><td>1.490</td><td>88.06</td></tr>
<tr><td>Boosted LCP</td><td>0.984</td><td>89.97</td><td>0.977</td><td>90.32</td><td>0.944</td><td>90.37</td></tr>
<tr><td>LVD</td><td>1.094</td><td>90.32</td><td>1.102</td><td>90.43</td><td>1.139</td><td>90.12</td></tr>
</tbody>
</table>

<p>What drives the width of these intervals? Recipe-level rating variance has negligible practical association with interval width ($\rho \le 0.06$), while <strong>user-level rating variance shows a strong, consistent positive association</strong> ($\rho = 0.48$–$0.62$). Conformal uncertainty in recommendation is driven by user preference heterogeneity, not by the items.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/conformal-llm-judge/figure1_uncertainty_drivers.png" alt="Mean conformal interval width versus recipe rating std and user rating std" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 1:</strong> Drivers of uncertainty. Interval width is almost independent of recipe-level rating variance (a), but increases substantially with user-level rating variance (b).
  </figcaption>
</figure>

<h3>RQ3: User-Stratified Calibration</h3>

<p>Calibrating within each of the four user groups (1,000 users, i.e., 2,000 calibration and 2,000 test pairs per group; a Kolmogorov–Smirnov test confirms no calibration–test shift) reveals how strongly heterogeneity shapes usefulness. Interval widths grow from roughly <strong>0–0.5 for the most consistent raters</strong> to <strong>nearly 3.0 for the most volatile ones</strong> — on a 1–5 scale, the latter cover most of the range and are weakly actionable.</p>

<figure style="text-align: center; margin: 2rem 0;">
  <img src="/images/projects/conformal-llm-judge/figure2_stratified_calibration.png" alt="Coverage versus interval width for each conformal method across user groups and LLM judges" style="max-width: 100%; border-radius: 8px;">
  <figcaption class="figure-caption" style="margin-top: 0.5rem;">
    <strong>Figure 2:</strong> Coverage–efficiency trade-off under user-stratified calibration. Higher user variance leads to wider intervals. Dashed lines mark the 90% coverage target.
  </figcaption>
</figure>

<p><strong>R2CCP</strong> and <strong>Boosted LCP</strong> stay closest to the 90% target across groups and judges, while CQR variants and CHR over-cover, especially for low-variance users. Boosted CQR is the least reliable, often dropping below target in higher-variance groups. No method is optimal everywhere, but R2CCP offers the most stable trade-off, particularly for low- and mid-variance users.</p>

<h2>Key Contributions</h2>

<ul class="contributions-list">
<li><strong>Stratified conformal calibration for LLM-as-a-judge:</strong> Calibrating simulated ratings within user groups defined by rating variance, so coverage guarantees hold per group.</li>
<li><strong>Systematic evaluation:</strong> Three open-source LLMs, two user-representation strategies, and seven conformal prediction methods in recipe recommendation.</li>
<li><strong>Practical insights:</strong> Point-prediction metrics mask failures on low-rating recipes, and interval width is driven by user — not recipe — variance.</li>
</ul>

<h2>Takeaways</h2>

<p>Valid coverage is achievable for LLM-simulated ratings, but interval <em>usefulness</em> depends strongly on who is being simulated: intervals are informative for consistent users and become broad for users with highly variable tastes. This supports user-stratified calibration as a principled strategy for uncertainty-aware recommendation evaluation, and points toward pipelines that use calibrated intervals to decide <strong>when to trust an LLM judge and when to ask real users</strong>.</p>

<p>Source code and data are available in the <a href="https://github.com/maddalena-amendola/conformal_prediction_recsys" target="_blank">GitHub repository</a>.</p>
