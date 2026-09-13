# Changelog

Releases of the `study-kb` plugin and the repository around it. The knowledge base content in
`docs/` changes continuously and is not itemised here — a release records changes to the **skills,
the conventions and the tooling**, which are the things another machine installs.

Versions are `MAJOR.MINOR.PATCH`:

- **MAJOR** — a convention changed in a way that makes existing notes wrong.
- **MINOR** — a skill, script or rule added or meaningfully reshaped.
- **PATCH** — corrections that change no behaviour.

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
