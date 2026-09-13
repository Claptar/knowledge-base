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

### Skills

- **`normalise-materials` now has its converter.** `normalise_source.py` turns a collected source
  into markdown split on the source's own headings, one page per logical section, so a topic file
  can cite a lecture's third argument rather than a page range. It prefers the source over the
  render (a `.qmd` beside its `.pdf` converts from the `.qmd`, and the render is reported as
  dropped), skips course administrivia unless `--include-all` is given, and rewrites every relative
  link — to the converted sibling where there is one, to the upstream original otherwise, and to
  plain text where the source has no upstream, because the site builds `--strict` and a dangling
  link fails CI. Dry run by default.

  Two things it refuses to do. It will not publish a source it cannot classify or cannot cite: no
  `material:`, no source URL, anything unclassified — all go to `reference-private/`. And it will
  not convert a scanned PDF, which has no text layer; those are reported, because a near-empty page
  that looks like a conversion is worse than an honest absence.

- **A thesis is its own source kind.** Added to the republishing table in `AGENTS.md` and to the
  skill: a repository asserts open access, but the author asserts the rights, per record —
  CaltechTHESIS carries a Creative Commons grant on some theses and "no commercial reproduction
  rights are provided" on others. A thesis converts to `reference-private/` until its rights row
  has actually been read.

- **New recipe: CaltechTHESIS.** Record-page layout, the non-constant document slot in the PDF
  path (`/16062/03/`, `/16368/10/`), and the failure worth naming — the site began refusing
  automated requests partway through a harvest, with a timeout from `curl` and an `ECONNREFUSED`
  from an agent fetch, while other hosts answered normally in the same minute. Diagnose it by
  fetching an unrelated host.

### Tooling

- **`material:` in `sources.lock.yml`.** `course`, `notes`, `paper`, `thesis`, `book`, `archive` or
  `data` — written by hand and never detected, because it decides whether a conversion may be
  published and guessing it guesses in the publishing direction. `open_access: true` is the one
  switch that promotes a paper or a thesis into the published tree. All 63 sources are classified.
- **A licence rescan no longer downgrades a resolved licence.** Several were settled by reading a
  course site rather than a file in the repo; `unresolved` means *not found*, and re-running
  `lock_sources.py` must not undo that work.
- **The converted tree's nav is generated.** `mkdocs-literate-nav` reads
  `docs/reference/SUMMARY.md`, so several hundred entries stay out of the hand-written
  `mkdocs.yml`, which carries one line for the whole subtree. `nbconvert` is dropped: notebooks are
  read straight from their JSON, so that image outputs become a named omission rather than links to
  files the converter never writes.

### Skills

- **New skill: `collect-materials`.** Finds and fetches material from a provider, and owns the
  per-provider recipes — URL patterns, where the real files live, what is gated behind a campus
  login, which licence claims are traps. It **locates and does not judge**: entries are always
  `unvetted`, and `study-mentor` step 4 remains the only thing that earns a verdict. Its standing
  obligation is that harvesting from a provider with no recipe means writing one. Ships with
  recipes for MIT OCW, Berkeley and GitHub-hosted courses.
- **Prefer the paper over the lecture notes where the paper is the argument.** Added to
  `AGENTS.md` and to `study-mentor` step 4: a course is a route through settled material, a paper
  is the moment someone had to argue for something, and a syllabus's bibliography is often worth
  more than its slides. Stated as a judgement rather than a rule — a good set of notes with problem
  sets still beats a paper with no route into it.

### Tooling

- **`sources/` is now reproducible.** `sources.lock.yml` is committed — the one exception to the
  directory's gitignore — recording every source with a `restorable` field: `upstream` for a git
  repo pinned to a commit or files under a base URL, `never` for anything added by hand, `dead` for
  an upstream that stopped resolving. `restore_sources.py` rebuilds what it can and prints what it
  cannot; `--check` verifies on-disk copies against recorded checksums, which is how link rot and
  a quietly-replaced PDF become visible. `lock_sources.py` generates the file and reads licences
  from disk rather than trusting a metadata field.

  The design point is the `never` list: it is what a backup actually needs to cover, and it is a
  small fraction of the tree — 0.81 GB of 3.5 GB here, mostly books and publisher archives, with
  everything clonable excluded.

### Knowledge base

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
