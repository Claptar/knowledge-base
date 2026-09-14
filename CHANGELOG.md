# Changelog

Releases of the `study-kb` plugin and the repository around it. The knowledge base content in
`docs/` changes continuously and is not itemised here — a release records changes to the **skills,
the conventions and the tooling**, which are the things another machine installs.

Versions are `MAJOR.MINOR.PATCH`:

- **MAJOR** — a convention changed in a way that makes existing notes wrong.
- **MINOR** — a skill, script or rule added or meaningfully reshaped.
- **PATCH** — corrections that change no behaviour.

Entries accumulate under **Unreleased** as the work happens on `draft`. Promoting `draft` to `main`
renames that heading to the version and date, and the release job publishes the section as-is.

## Unreleased

### Structure

- **The converted library is now a separate repository.**
  [knowledge-base-library](https://github.com/Claptar/knowledge-base-library), published at
  <https://claptar.github.io/knowledge-base-library/>. It holds `sources/`, the converted markdown,
  and the two skills that produce them.

  The reason is arithmetic. A full dry run over the corpus plans **9,657 pages from 1,948
  documents**; this repository holds about seventy files of his own writing. Kept together, the
  knowledge base becomes a rounding error inside its own library — search drowns, `git log` becomes
  conversion churn, and every agent loads a page of policy about other people's material before
  reading a word of his. **The split is by authorship**: what he wrote stays, what someone else
  wrote goes.

- **The plugin ships three skills, not five.** `collect-materials` and `normalise-materials` move
  to the library repo as a companion plugin, `study-library`, along with the four source-handling
  scripts that used to sit in `adapt-recordings/scripts/` — anything that touches `sources/` lives
  where `sources/` lives. `adapt-recordings` keeps its `SKILL.md`: reconstructing spoken
  mathematics is judgement, not tooling.

- **`AGENTS.md` lost the republishing policy and the `docs/reference/` section**, 456 lines to 401,
  and the removed half was the policy-dense half. Both now live in the library's own `AGENTS.md`,
  where they are read only by whoever is converting something.

- **Books and paywalled papers are simply never converted**, replacing the publish-versus-private
  tiering with a single skip rule. `reference-private/` no longer exists anywhere.

- **The strict site build went from 30 seconds to 1.1.**

### Tooling

- **`normalise_source.py`** — the converter named as the one unfinished thing in the previous
  handoff — was written, and now lives in the library repo. It prefers the source format over the
  render, splits on the source's own headings, rewrites every relative link to a converted sibling
  or to the original, and refuses to convert anything it cannot classify or cite. Dry run by
  default.
- **`material:`, `open_access:` and `mirrors_upstream:` in `sources.lock.yml`** — hand-written,
  never detected, preserved across a rescan. `mirrors_upstream` exists because MIT OCW exports are
  renamed at ingest, so building a per-file URL from the tidied path produced a confident 404.
- **A licence rescan no longer downgrades a resolved licence.** Several were settled by reading a
  course site rather than a file in the repo.

### Knowledge base

- **Six Pachter-lab theses catalogued** in `resources/cme-transcription.md`, four of them
  biophysical and directly on the CME track. Gorin 2023 is the long-form version of four papers
  already catalogued there. Not yet fetched: CaltechTHESIS began refusing automated requests
  partway through the harvest, which is recorded in the library's provider recipe as rate limiting
  rather than a gate.

- **Catalogued 16 Berkeley statistics courses** in `docs/resources/berkeley-statistics.md`, all
  `unvetted`. Two of the requested courses turned out to be retired — `Stat 200A–B` was replaced by
  `201A–B` in 2012–13, and `Stat C239A` was succeeded by `Stat 256` — and both are recorded as
  such so the dead numbers resolve to their successors. `Stat C245E–F` (Statistical Genomics,
  Dudoit) covers scRNA-Seq and is the closest thing in the set to the day job.

### Conventions

- **Two long-lived branches.** Work happens on `draft`; `main` holds what is released and
  published. Promoting `draft` to `main` is the deliberate act that cuts a release. `AGENTS.md`
  carries the rule and the commands, including the `--base draft` that `gh pr create` needs and
  does not default to.

## 0.2.0 — 2026-09-13

First tagged release. The repo had drifted since the three-skill split; this is the pass that
brought the instructions, the plugin manifest and the tooling back in line with each other.

### Skills

- **`study-mentor` can now reach `adapt-recordings`.** Its sibling-skill note named only
  `adapt-material`, so a lecture transcript had no route out of a session. It now routes by source:
  written material to `adapt-material`, recordings and `.srt`/`.vtt` to `adapt-recordings`.
- **`adapt-material` is the authority on adapted-document shape again.** Its required-shape block
  was missing `Catalogue`, `Licence` and the attribution footer that `adapted/_template.md`
  already carried; the two are now in step, and the obligation to keep them so is stated.
- **Removed a hardcoded install path.** `kb-structure.md` pointed at `skills/adapt-recordings/
  scripts/`, which is wrong whenever the skill is loaded as a plugin rather than from the repo.
- **Corrected the site's rendering constraint.** Two files still described a Jekyll site; the
  constraint is MkDocs with `pymdownx.arithmatex`, which is why `\(…\)` must never be used.

### Tooling

- **`init_kb.py` generates the current structure.** It emitted a `resources.md` file while also
  creating a `resources/` directory, produced no `path.md` or `notes/`, and — the actual defect —
  seeded an adapted-document template with no `Licence` field, which is what decides whether a
  derivative may be published. All three generated templates are now byte-identical to the
  committed ones.
- **Documented `transcript_text.py`**, the fourth script, which the catalogue never listed, and
  corrected the claim that all the scripts "default to a dry run" — one of them never writes.
- **Fixed stale source slugs** in two script docstrings, left behind when sources were normalised.

### Conventions

- **Every catalogue entry carries a licence.** All 20 CME entries lacked the field that routes an
  adaptation to `docs/adapted/` or `adapted-private/`. They are marked `unresolved`, which is the
  safe direction, with a note that open access is not a licence.
- **The study log is bounded.** `log.md` holds `Next` plus the current year; finished years archive
  to `log/<year>.md` past roughly 400 lines. Splitting per session is explicitly ruled out.
- **Changes land through a pull request**, and a merge to `main` cuts a release. See `AGENTS.md`.

### Knowledge base

- **Deleted `topics/mathematical-modelling.md`.** It was seeded from an external reading guide and
  was largely a restatement of it, which is the one thing a topic file is not for. The single line
  in it that was his — convex optimisation held as theory, formulation missing — moved to
  `profile.md`.
- **Moved the martingale and generator questions out of the Live table.** Neither had been started
  and both were the learning path's phrasing rather than his own. They remain as path nodes.

### Known issues

- **`normalise_names.py` is not idempotent.** A second `--apply` re-suffixes already-normalised
  files (`final-f09-exam.pdf` → `final-f09-exam-exam.pdf`) and rewrites `_manifest.csv` with the
  mangled names, destroying the mapping back to the publisher's filenames. It affects 354 files in
  `ocw-6041sc` alone. Unfixed, and deliberately so — the repair touches the classifier and wants
  its own change.
