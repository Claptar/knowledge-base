# Handoff — 2026-09-14

**A snapshot of work in flight, for whoever picks this up next.** Not a second instruction file:
where something is already documented, this points at it rather than restating it. Delete or
rewrite this file when the work below is finished — a stale handoff is worse than none.

## Read first, in this order

1. **[AGENTS.md](AGENTS.md)** — the one instruction file. Conventions, the branching model, the
   republishing policy. `CLAUDE.md` is a one-line import of it plus Claude-specific notes.
2. **The three `skills/*/SKILL.md`** — each is the authority on its own workflow. Two more live
   in the library repository; see § *What just happened*.
3. **[CHANGELOG.md](CHANGELOG.md) § Unreleased** — what has changed since `v0.2.0`, in the words
   used at the time.

Do not re-derive the conventions from the file tree. They are argued for in AGENTS.md, and several
are counter-intuitive on purpose.

## Where things stand

| | |
| --- | --- |
| Branch | **`draft`**, 32 commits ahead of `main` |
| Released | `v0.2.0`, tagged and published as a GitHub release |
| Skills | **3** — `study-mentor`, `adapt-material`, `adapt-recordings`. The other two moved |
| Library | **[knowledge-base-library](https://github.com/Claptar/knowledge-base-library)** — `sources/`, the converted markdown, and the two skills that make it |
| Site | builds `--strict` clean in ~1s; `uv run mkdocs build --strict` |
| Tracked files in `docs/` | ~73, down from 536 |

**Never commit to `main`.** Work lands on `draft`; promoting `draft` to `main` cuts a release.
`gh pr create` defaults to `main`, so `--base draft` is mandatory — see AGENTS.md § Git.

## What just happened: the repository split in two

**The converted library moved out.** A full dry run over the corpus plans **9,657 pages from 1,948
documents**, against roughly seventy files of his own writing here. Kept together the knowledge base
becomes a rounding error inside its own library, so:

| | |
| --- | --- |
| **this repo** | what *he* wrote — questions, trajectories, his own expositions, verdicts on sources |
| **the library** | what *someone else* wrote, converted — courses, lecture notes, transcripts |

`sources/`, the converted markdown, and the `collect-materials` and `normalise-materials` skills all
live in [knowledge-base-library](https://github.com/Claptar/knowledge-base-library) now, along with
the four source-handling scripts that used to sit in `adapt-recordings/scripts/` — **anything that
touches `sources/` lives where `sources/` lives**. `adapt-recordings` keeps its `SKILL.md`, because
reconstructing spoken mathematics is judgement rather than tooling.

Three consequences worth holding on to:

- **`AGENTS.md` lost the republishing policy and the `docs/reference/` section** — 456 lines to 401,
  and the removed half was the policy-dense half. It is in the library's own `AGENTS.md` now, read
  only by whoever is converting something.
- **Books and paywalled papers are simply never converted.** That one skip rule replaced the whole
  publish-versus-private tier system; `reference-private/` no longer exists anywhere.
- **The strict build went from 30 seconds to 1.1.**

## The unfinished things

- **Neither repository has been pushed.** This branch is 32 commits ahead of `origin/draft`; the
  library repo exists only locally, with one commit, and `Claptar/knowledge-base-library` has not
  been created. Creating it is a *public* repo containing other people's course material — worth a
  deliberate moment rather than a reflex.
- **Only 3 sources of 63 are converted** — Stat 210A fall 2026, 6.041SC and StatOmics SGA21, about
  1,300 pages. The rest is a `--all --apply` run away, and the dry run above says what it will cost.
- **The cross-links do not exist yet.** Catalogue entries in `docs/resources/` should link to their
  converted pages in the library, and no scheduled link-check workflow has been written. That
  workflow is what replaces the `--strict` guarantee across the repository boundary — without it,
  a link into the library can rot silently.
- **The six Pachter-lab theses are catalogued but not fetched.** CaltechTHESIS began refusing
  automated requests partway through the harvest. **Download the PDFs by hand** into the library's
  `sources/` under the slug each entry names. Four of the six are biophysical and sit directly on
  the CME track; Gorin 2023 is the long-form version of four papers already catalogued.
- **A maths-repair pass is designed but not built.** The library's `normalise-materials` step 3a
  specifies it: repair mangled equations against the original, mark every repair `**Unverified.**`,
  report the count. 1,016 pages came through the lossy PDF route, so it now has real work to do.

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

- **29 of 63 sources have an unresolved licence** (in the library's lockfile). They are *unchecked*,
  not restricted. It matters less than it did — conversions no longer depend on the licence, only
  adaptations do — but it is still the field that decides whether an adaptation may be published.
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

- `uv` for everything Python. `uv sync --group dev` for the site. The conversion toolchain
  (`--group convert`) is in the library repo, not here.
- `gh` installed and authenticated as `Claptar`, with `repo` and `workflow` scopes.
- `sources/` is in the library repo, gitignored except `README.md` and `sources.lock.yml`. Rebuild
  it from there with `skills/collect-materials/scripts/restore_sources.py --apply`; `--check`
  verifies on-disk copies against recorded checksums.
- Repo: <https://github.com/Claptar/knowledge-base> · site:
  <https://claptar.github.io/knowledge-base/>
- Library: <https://github.com/Claptar/knowledge-base-library> (not yet created) · site:
  <https://claptar.github.io/knowledge-base-library/>
