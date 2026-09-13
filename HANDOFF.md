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
| Branch | **`draft`**, 20 commits ahead of `main`. Working tree clean |
| Released | `v0.2.0`, tagged and published as a GitHub release |
| Skills | 5 — `study-mentor`, `adapt-material`, `adapt-recordings`, `collect-materials`, `normalise-materials` |
| `sources/` | 5.2 GB, 63 sources, gitignored. 53 restorable from upstream, 10 local-only |
| Licences | 24 CC BY 4.0, 2 CC0, 1 BSD-3, 1 CC BY-NC, **35 unresolved** |
| Site | builds `--strict` clean; `uv run mkdocs build --strict` |

**Never commit to `main`.** Work lands on `draft`; promoting `draft` to `main` cuts a release.
`gh pr create` defaults to `main`, so `--base draft` is mandatory — see AGENTS.md § Git.

## The one unfinished thing

**`skills/normalise-materials/scripts/normalise_source.py` does not exist.** The skill, the policy,
the toolchain and the verified approach are all in place; the converter is not written. It is the
next job and it is well specified:

- Read the tier from AGENTS.md § *What may be republished* — courses and notes to `docs/reference/`,
  books and paywalled papers to `reference-private/` (gitignored, already in `.gitignore`).
- Dispatch by format, **preferring the source over the render** — see below.
- Split on the source's own headings, one file per lecture or section, numbering preserved.
- Generate front matter: title, source URL, `source_file`, licence, conversion route and date.
- Emit an `index.md` per source. For a non-publishable source that index is the *only* published
  page — structure and links, no body.
- **Generate the `nav:` block.** `mkdocs.yml` has `validation.nav.omitted_files: warn` and the
  build runs `--strict`, so every published page must be in the nav. The publishable set is ~424
  source-format files; a flat nav is unusable, so it needs one section per source with its parts as
  children.
- Dry run by default, `--apply` to write. Every script in this repo works that way.

Install its toolchain with `uv sync --group convert` — `pymupdf4llm`, `pypandoc-binary` (pandoc 3.9
ships inside the wheel), `markdownify`, `nbconvert`. No system packages; do **not** reach for brew,
because `pyproject.toml` + `uv.lock` is what makes it reproducible.

## Traps found the hard way

Each cost real time. All are recorded in the relevant recipe, repeated here because they are the
things most likely to be rediscovered.

- **PDF → markdown destroys mathematics.** Verified: $\lambda(t) = f(t)/S(t)$ converts to
  `Sf((tt))becauseTiscontinuous`. Prose survives; equations do not. Convert `.qmd`/`.Rmd`/`.tex`
  instead — there are 1,027 source-format files against 1,585 PDFs.
- **Some PDFs are scans of handwriting** — Stat 210A's lectures. 219 characters of OCR fragments.
  Emit an index entry, never a near-empty page that looks like a conversion.
- **A licence is rarely in a `LICENSE` file.** Course sites use `license.qmd`, `license.html`, or
  `myst.yml` declaring `license: {code: MIT, content: CC-BY-4.0}` — where the *content* licence
  governs and the code licence is a decoy. GitHub reports all of these as `NOASSERTION`.
  `lock_sources.py` now reads all of them; trusting the API's licence field is how 24 CC BY sources
  were first misfiled as unlicensed.
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

## Open threads

- **35 sources have an unresolved licence.** They are *unchecked*, not restricted, and several are
  near-certainly CC BY — `berkeley-stat210a/fall-2025` sits between two CC BY offerings. A targeted
  sweep is cheap and moves material into the publishable tier.
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
- **A maths-repair pass is designed but not built.** `normalise-materials` step 3a specifies it:
  repair mangled equations against the original page, mark every repair `**Unverified.**`, report
  the count. Precedent is `adapt-recordings` step 3. A dedicated lightweight skill for it is a
  reasonable thing to add.

## Working habits this user has corrected

Stated because they were corrected more than once.

- **Atomic commits.** One logical change each, short messages. A component and the edits that
  register it are *separate* commits. One request is not one commit.
- **Plan before acting**, and ask where the approach is unclear — AGENTS.md § Plan first.
- **Push back on substance before executing**, once, with the reason and the alternative.
- **Verify rather than assume.** Several confident claims in this session were wrong — the licence
  classification twice, `Access: fetchable` for scaffold-only repos. Checking took minutes.

## Environment

- `uv` for everything Python. `uv sync --group dev` for the site, `--group convert` for conversion.
- `gh` installed and authenticated as `Claptar`, with `repo` and `workflow` scopes.
- `sources/` is gitignored except `README.md` and `sources.lock.yml`. Rebuild with
  `uv run python skills/collect-materials/scripts/restore_sources.py --apply`; verify on-disk copies
  with `--check`.
- Repo: <https://github.com/Claptar/knowledge-base> · site:
  <https://claptar.github.io/knowledge-base/>
