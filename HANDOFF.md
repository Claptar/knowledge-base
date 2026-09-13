# Handoff — 2026-09-14

**A snapshot of work in flight, for whoever picks this up next.** Not a second instruction file:
where something is already documented, this points at it rather than restating it. Delete or
rewrite this file when the work below is finished — a stale handoff is worse than none.

## Read first, in this order

1. **[AGENTS.md](AGENTS.md)** — the one instruction file. Conventions, the branching model, the
   republishing policy. `CLAUDE.md` is a one-line import of it plus Claude-specific notes.
2. **The five `skills/*/SKILL.md`** — each is the authority on its own workflow.
3. **[CHANGELOG.md](CHANGELOG.md) § Unreleased** — what has changed since `v0.2.0`, in the words
   used at the time.

Do not re-derive the conventions from the file tree. They are argued for in AGENTS.md, and several
are counter-intuitive on purpose.

## Where things stand

| | |
| --- | --- |
| Branch | **`draft`**, 28 commits ahead of `main` |
| Released | `v0.2.0`, tagged and published as a GitHub release |
| Skills | 5 — `study-mentor`, `adapt-material`, `adapt-recordings`, `collect-materials`, `normalise-materials` |
| `sources/` | 63 sources, gitignored. 59 restorable from upstream, 4 local-only. All 63 classified with `material:` |
| Licences | 24 CC BY 4.0, 6 CC BY-NC-SA 4.0 (MIT OCW), 2 CC0, 1 BSD-3, 1 CC BY-NC, **29 unresolved** |
| `docs/reference/` | the converted tree, wired into the site nav. Stat 210A fall 2026 converted |
| Site | builds `--strict` clean; `uv run mkdocs build --strict` |

**Never commit to `main`.** Work lands on `draft`; promoting `draft` to `main` cuts a release.
`gh pr create` defaults to `main`, so `--base draft` is mandatory — see AGENTS.md § Git.

## What was just finished

**The converter exists.** `skills/normalise-materials/scripts/normalise_source.py` — the job the
previous handoff named as the one unfinished thing. It converts one source at a time, prefers the
source format over the render, splits on the source's own headings, generates front matter and the
nav, and routes anything it cannot classify or cite to the gitignored `reference-private/`. Dry run
by default, like every script here.

```bash
uv sync --group dev --group convert
uv run --group convert --group dev python \
    skills/normalise-materials/scripts/normalise_source.py sources/<slug>            # dry run
uv run ... normalise_source.py sources/<slug> --apply                                # write
uv run ... normalise_source.py --all                                                 # plan the corpus
uv run ... normalise_source.py --summary-only --apply                                # rebuild nav only
```

## The unfinished things

- **Only one source of 63 is converted.** Stat 210A fall 2026: 83 documents, 408 pages, 26 skipped.
  The decision taken was to convert two or three, look at the output, then sweep. Pick sources that
  exercise different routes — a Quarto course, a PDF-and-transcripts OCW course, an `.Rmd` course
  with material and logistics mixed.
- **The six Pachter-lab theses are catalogued but not fetched.** See
  [`docs/resources/cme-transcription.md`](docs/resources/cme-transcription.md) — CaltechTHESIS
  began refusing automated requests partway through the harvest. **Download the PDFs by hand** into
  the `sources/` slug each entry names, then convert. Four of the six are biophysical and sit
  directly on the CME track; Gorin 2023 is the long-form version of four papers already catalogued.
- **The theses' rights rows were never read**, so all six are `unresolved` and their conversions go
  to `reference-private/`. Reading one row promotes a thesis into the published tree by setting
  `open_access: true` in the lockfile.
- **A maths-repair pass is designed but not built.** `normalise-materials` step 3a specifies it:
  repair mangled equations against the original page, mark every repair `**Unverified.**`, report
  the count. Now more valuable than before, because the lossy PDF route is actually producing
  pages. Precedent is `adapt-recordings` step 3.

## Traps found the hard way

Each cost real time. All are recorded in the relevant recipe, repeated here because they are the
things most likely to be rediscovered.

- **PDF → markdown destroys mathematics.** Verified: $\lambda(t) = f(t)/S(t)$ converts to
  `Sf((tt))becauseTiscontinuous`. Prose survives; equations do not. Convert `.qmd`/`.Rmd`/`.tex`
  instead — there are 1,027 source-format files against 1,585 PDFs, and the converter now drops the
  render automatically when a source with the same stem sits beside it.
- **A PDF's biggest text is not its title.** Converted exam papers came out titled
  `**Student ID (NOT your name):**`. Titles are now cleaned and fall back to the filename.
- **Internal links need two passes.** Whether a document becomes one page or a directory of them is
  only known after it is split, so the link map cannot be built before converting. Building it
  first produced 45 links to directories rather than to pages, and `--strict` caught all of them.
- **Some PDFs are scans of handwriting** — Stat 210A's lectures. 219 characters of OCR fragments.
  Emit an index entry, never a near-empty page that looks like a conversion.
- **A licence is rarely in a `LICENSE` file.** Course sites use `license.qmd`, `license.html`, or
  `myst.yml` declaring `license: {code: MIT, content: CC-BY-4.0}` — where the *content* licence
  governs and the code licence is a decoy. GitHub reports all of these as `NOASSERTION`.
  `lock_sources.py` reads all of them, and no longer lets a rescan downgrade a licence that was
  resolved by reading the course site.
- **A `*.github.io` repo's MIT licence is the Jekyll theme's**, with the template author in the
  copyright line. It says nothing about course content.
- **Content is often on `gh-pages`, not the default branch.** `statOmics/SGA2020` is 5 files on
  `master` and 229 files / 515 MB on `gh-pages`. A repo whose API size is large but whose clone is
  tiny is always this.
- **A public repo is not public material.** Many Berkeley semester repos hold only a Quarto
  scaffold — about 13–15 files, no notes. Theory courses publish a syllabus; applied courses publish
  everything.
- **Berkeley has a second publishing system.** Instructor pages under `stat.berkeley.edu/~<user>/`
  hold the material for exactly the courses whose repos are scaffolds. Directory listing is off, so
  fetch `index.html` and extract hrefs.
- **A blocked host looks like a broken agent.** CaltechTHESIS timed out from `curl` and refused an
  agent fetch while `github.com`, `pypi.org` and `ocw.mit.edu` answered in the same minute. Always
  test an unrelated host before concluding anything about the source.

## Open threads

- **29 sources have an unresolved licence.** They are *unchecked*, not restricted. A targeted sweep
  is cheap and moves material into the publishable tier. MIT OCW's six were resolved this session.
- **`mkdocs-literate-nav` prints a MkDocs 2.0 advertisement on every build.** Its author now
  maintains a fork, and the plugin nags about it. Harmless, silenced with
  `DISABLE_MKDOCS_2_WARNING=true`, but worth knowing given that `mkdocs<2` is pinned deliberately —
  the pin's reasoning is in `pyproject.toml` and has not changed.
- **`normalise_names.py` is not idempotent.** A second `--apply` re-suffixes already-normalised
  files (`final-f09-exam.pdf` → `final-f09-exam-exam.pdf`) and rewrites `_manifest.csv` with the
  mangled names, destroying the mapping back to publisher filenames. 354 files in `ocw-6041sc`
  alone. The guard at `main()` compares `src != dest`, but `plan()` rebuilds `dest` from the current
  stem and appends the artefact type unconditionally, so it never fires. Recorded in CHANGELOG
  § Known issues. Deliberately unfixed — the repair touches the classifier and wants its own branch.
- **Workflow permissions are `read`.** The release job skipped cleanly on `v0.2.0` because the tag
  already existed, but the next promotion that bumps the version will 403 on the tag push. Fix:
  `gh api -X PUT repos/Claptar/knowledge-base/actions/permissions/workflow -f default_workflow_permissions=write`.
  Not run — it grants every workflow write access to contents, which is the user's call.
- **`Stat C247C` was never found.** The only course from the original request still missing. No
  vanity domain, no GitHub org, no public syllabus; offered in even-numbered years. The Wayback
  Machine is the untried route.

## Working habits this user has corrected

Stated because they were corrected more than once.

- **Atomic commits.** One logical change each, short messages. A component and the edits that
  register it are *separate* commits. One request is not one commit.
- **Plan before acting**, and ask where the approach is unclear — AGENTS.md § Plan first.
- **Push back on substance before executing**, once, with the reason and the alternative. And read
  the answer carefully: "don't publish raw source files" is not "don't publish conversions", and
  acting on the misreading would have deleted a policy decided the same day.
- **The knowledge base is for connecting ideas, not for being exhaustive.** Coverage is not the
  goal; navigability is. It is why converted material is split into sections and cross-linked
  rather than mirrored file for file.
- **Verify rather than assume.** Several confident claims have been wrong — the licence
  classification twice, `Access: fetchable` for scaffold-only repos. Checking took minutes.

## Environment

- `uv` for everything Python. `uv sync --group dev` for the site, `--group convert` for conversion.
- `gh` installed and authenticated as `Claptar`, with `repo` and `workflow` scopes.
- `sources/` is gitignored except `README.md` and `sources.lock.yml`. Rebuild with
  `uv run python skills/collect-materials/scripts/restore_sources.py --apply`; verify on-disk copies
  with `--check`.
- Repo: <https://github.com/Claptar/knowledge-base> · site:
  <https://claptar.github.io/knowledge-base/>
