---
name: feature-on-homepage
description: Assess whether a paper belongs on the homepage "Featured Quests" grid and, if so, swap it in — keeping the 2×3 (six-card) layout by asking which existing card to remove. The new card is tagged so the site's NEW badge shows for 30 days. Use when the user wants to feature, promote, or add a paper to the homepage (_pages/about.md).
---

# Feature a paper on the homepage

The homepage (`_pages/about.md`) shows a **"Featured Quests"** grid of exactly **six** `.pub-card`
entries inside `<div class="pub-cards-grid">`. Six keeps a clean 2×3 layout, so adding one
means removing one. This skill decides whether a paper earns a spot, then performs the swap.

## Inputs you need

From the user's request, establish:
- **Title**, **venue** (+ year), and **author list** (mark Giacomo as `G. Medda`).
- A **project slug** — the page at `/projects/<slug>/` (file `_projects/<slug>.md`). Card links
  MUST point to `/projects/<slug>/`, never `#`. If no project page exists yet, say so and offer
  to create it first with the `academic-page-generator` agent; do not fabricate a link.
- Optional **Code** URL and **DOI/paper** URL. Include a link only if it genuinely exists.

If any of these are missing, ask the user (or read the paper's `_projects/<slug>.md` front matter,
which carries `title`, `venue`, `authors`, `code`, `doi`/`paperurl`).

## Step 1 — Assess relevance (recommend, don't just do)

Judge whether the paper is strong enough to sit among the six featured. Weigh:
- **Authorship** — Giacomo (`G. Medda`) should be an author. A paper he did not co-author is
  almost never a Featured Quest; flag it if not.
- **Topical fit** with his focus areas: Recommender Systems, Graph Neural Networks,
  Explainable AI, Fairness in ML, and LLMs.
- **Venue strength** — top-tier venues (RecSys, SIGIR, CIKM, ECIR, WWW, KDD, NeurIPS, ACL,
  ACM TORS/TIST/TOIS, etc.) and journals weigh more.
- **Recency** — newer work is a better "quest" than old work already represented.

State a clear verdict: **feature / borderline / skip**, with one or two sentences of reasoning.
If it's borderline or a skip, tell the user and stop unless they confirm they still want it in.

## Step 2 — List the current six and ask which to drop

Read `_pages/about.md` and enumerate the six active `.pub-card` entries in `.pub-cards-grid`
(ignore any commented-out `<!-- ... -->` cards). For each, note its venue pill and a short title.

Use the **AskUserQuestion** tool to ask which one to remove, offering the six current cards as
options (label = short title + venue). Do not pick for them — the demotion is their call. Suggest
the oldest / least-aligned card as the recommended option, but let them choose.

## Step 3 — Build the new card

Match the existing markup exactly (2-space indented inside the grid). Add `data-added` with
**today's date** (ISO `YYYY-MM-DD`) so the site's NEW badge appears for 30 days:

```html
      <!-- <Short Name> -->
      <div class="pub-card" data-added="YYYY-MM-DD">
        <span class="pub-card-venue">VENUE YEAR</span>
        <h3 class="pub-card-title">
          <a href="/projects/<slug>/">Full Paper Title</a>
        </h3>
        <p class="pub-card-authors">
          A. Author, <strong>G. Medda</strong>, B. Author
        </p>
        <div class="pub-card-links">
          <a href="/projects/<slug>/" class="pub-card-link link-project">
            <i class="fas fa-flask"></i> Project
          </a>
          <a href="CODE_URL" class="pub-card-link" target="_blank">
            <i class="fab fa-github"></i> Code
          </a>
          <a href="DOI_URL" class="pub-card-link" target="_blank">
            <i class="ai ai-doi"></i> DOI
          </a>
        </div>
      </div>
```

Rules:
- The **Project** link and the **title** link both go to `/projects/<slug>/`.
- Drop the **Code** and/or **DOI** `<a>` entirely if that URL doesn't exist (don't leave `#`).
- Venue pill is short (e.g. `RecSys 2026`, `ACM TORS 2026`). Keep `G. Medda` in `<strong>`.
- Preserve the author list's real order and diacritics.

## Step 4 — Perform the swap

- **Remove** the card the user chose (its whole `<div class="pub-card"> … </div>` block, plus its
  leading `<!-- Name -->` comment).
- **Insert** the new card at the **top** of `.pub-cards-grid` (newest first).
- The grid must still contain **exactly six** active cards. Count them before finishing.

## Step 5 — Report

Tell the user: which card was added, which was removed, and that the NEW badge will show on the
new card for 30 days (until 30 days after today), then disappear on its own. Note that the removed
paper still lives on the Publications page (`_pages/publications.md`) — this only changes the
homepage feature set.

## Notes

- Don't touch the badge CSS/JS — the badge is injected automatically by `_includes/new-badge.html`
  from the `data-added` attribute; styles are in `_sass/_gaming.scss` (`.pub-new-badge`).
- If the user also wants the paper on the Publications page, that's a separate edit to
  `_pages/publications.md` (a `.featured-publication` block, likewise supporting `data-added`).
