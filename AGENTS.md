# AGENTS.md

Instructions for any coding agent working in this repository — Claude Code, Codex, or otherwise.
This is the **one** instruction file. `CLAUDE.md` imports it; nothing is duplicated here by hand.

## Plan first, and ask

**Plan extensively before taking any action, and keep him in the planning loop.** For anything
beyond a single-file edit, present the plan first — what changes, where, in what order, and which
decisions are genuinely uncertain — then wait for agreement. A single "do it" authorises the thing
discussed, not an open-ended run of structural changes.

**Interview him wherever the approach is unclear.** A question costs a minute; a wrong structural
choice built out across forty files costs an afternoon and is half-reverted afterwards. Ask rather
than infer a default, and say plainly when something is a guess rather than presenting it with the
same confidence as a fact.

This applies with most force to anything that moves or renames files, changes where things live,
alters the shape of a record, or touches the skills. It is not a licence to narrate every step —
the *design* is agreed up front, and the *implementation* then runs without commentary.

A dry run is the honest form of this for a script: default to showing what would happen, and act
only when told.

## Disagree when there is something to disagree about

**An instruction here is not automatically the right course of action.** If a request seems wrong,
or worse than an available alternative, say so and discuss it *before* carrying it out. A faithful
implementation of a bad idea costs more than the argument would have.

- Object to **substance** — a structure that will not hold, an ordering that guarantees rework,
  effort aimed at the wrong thing — not to style or preference.
- **Flag a mistaken premise** rather than answering the literal question. If a request assumes
  something that is not true of this repo, saying so is the useful answer.
- Say it **once**, with the reason and the alternative. If the argument has been heard and he still
  wants it that way, do it his way and do not relitigate.

This matters more here than in a codebase, because the failure mode of a knowledge base is silent:
a bad structure still builds, still renders, and only stops paying six months later when nothing
can be found in it.

## What this repository is

A personal study knowledge base — markdown notes on mathematics and computational biology — plus
the skills that maintain it. There is no application and no build. The content *is* the product,
so the bar for an edit is whether a human reading the file six months from now is better off.

The repo has two halves, and they are edited for different reasons:

| Path | What it is | Edit when |
| --- | --- | --- |
| `docs/` — `index.md`, `questions.md`, `path.md`, `profile.md`, `log.md`, `resources/`, `topics/`, `practice/`, `adapted/`, `notes/` | the knowledge base — his notes and material. Also the published site | a study session happened, or something durable changed |
| `skills/` | the skills: `SKILL.md`, `references/`, `scripts/` | the *way* sessions run should change |

Don't let one drift into the other. Material learned goes in `docs/topics/`; instructions about how
to teach go in the skill.

**The knowledge base root is `docs/`.** Bare filenames below (`profile.md`, `topics/`) mean relative
to it. Everything in `docs/` is published; nothing outside it is.

## The five skills

The real tree is `skills/`. `.claude/skills` and `.agents/skills` are **symlinks** to it, so both
audiences read one copy and there is no way for them to drift. Never edit through a symlink path
and never create a second copy — see [Two audiences, one source](#two-audiences-one-source).

Each `SKILL.md` is the authority on its own workflow.

- **`study-mentor`** — a live session. Ask which mode he wants, start from the problem rather than
  the definition, hold back the proof, close by asking *how could you have come up with this?*
- **`adapt-material`** — a written source in, a document out. Rewrites a chapter, lecture notes or
  paper motivation-first, cutting what he holds cold and converting proofs to exercises. **It owns
  the shape of an adapted document**, and the other two defer to it rather than restating it.
- **`adapt-recordings`** — a lecture recording in, a document out. Owns only what is specific to
  speech: reconstructing mathematics that was spoken and written on an uncaptured board, naming
  what the recording points at but does not contain, and triaging which recordings are worth
  adapting at all. Hands the document shape to `adapt-material`.
- **`collect-materials`** — a provider in, catalogue entries out. Owns the per-provider recipes:
  where a site's material actually lives, what is gated behind a campus login, and which licence
  claim is about the website template rather than the content. **It locates; it does not judge** —
  its entries are always `unvetted`, and `study-mentor` step 4 is what earns a verdict. Its
  standing obligation: harvesting from a provider with no recipe means writing one.
- **`normalise-materials`** — a collected source in, uniform markdown out, split by lecture or
  section so every part has a URL. **It preserves; it does not rewrite** — changing the text is
  `adapt-material`'s job. Owns one rule above all: convert the *source* (`.qmd`, `.tex`) and not
  the render, because a PDF keeps the prose and destroys the mathematics.

Route by the shape of the output first — a conversation is `study-mentor`, a file is one of the
adapters, a catalogue entry is `collect-materials` — then by the source: a transcript or recording
is `adapt-recordings`, anything written is `adapt-material`. All five hand off in every direction.

When working inside this repo, read and write the files under `docs/` directly, summarise the
changes as a diff, and let him commit.

## The knowledge base is indexed by question

[`docs/questions.md`](docs/questions.md) is the front door, and the unit of navigation is a
**question**, not a subject. Subjects are how textbooks index, and the textbooks already exist.
What is not in a textbook is which question was live, what it attached to, and where it broke down.

Practical consequences:

- **A new question goes in `questions.md` first**, with no page behind it. That is the normal
  resting state of a question, not a gap to be filled.
- **A topic file opens with the question that forced it**, not with a definition. If the *question
  that opened it* section is empty, the file is not ready to exist.
- **Never route a new question to the nearest existing topic file.** A wrong attachment is worse
  than none: it implies the connection was already checked, and it quietly imports the wrong
  anchors. Say the knowledge base does not cover it and work from the source.

## A plan is a separate kind of object

[`docs/path.md`](docs/path.md) is the one page written *before* the work rather than after it: a
concept dependency map toward a destination, each node carrying the question that would force the
concept. It exists because a route is genuinely useful and there was nowhere to keep one — but it
is the exact thing *harvest, don't design* forbids a topic file from being, so it is quarantined on
its own page and never claims understanding: no `Status`, no markers, nothing that reads as
evidence. A node is not a page, and its questions stay out of the `questions.md` Live table until
he actually holds one.

**Keep exactly one path page.** A second plan — a syllabus, a reading order, a checklist — belongs
as a node or a layer in this one, or nowhere.

The full rules and the page template are in
`skills/study-mentor/references/kb-structure.md`, which is the single copy: the skill has to stand
alone when installed as a plugin, so that file carries them rather than this one.

## Writing to the knowledge base

Full templates are in `skills/study-mentor/references/kb-structure.md`. The rules that matter most:

- **Trajectories, not summaries.** Record what question opened a topic, what existing knowledge it
  attached to, where it clicked, what is still loose.
- **Link, never restate.** A clean restatement of the material is available in any textbook and is
  not worth storing. A topic file does not reproduce a definition, a theorem statement or a proof
  that lives in a named source — it cites the source and spends its words on what the source
  cannot know: why the question mattered to him, which anchor it attached to, where his intuition
  broke, and what he derived himself. **If you find yourself typing out a definition, stop and cite
  it instead.**
- **Traps are the product, not an appendix.** The happy path — the derivation that went fine — is
  the cheap half and is in the book. What costs time is the false analogy from a neighbouring
  topic, the definition held only formally, the step that looked obvious and was not. Record those
  as carefully as the result, **in his own words**, and link them *from* the topic file that causes
  them, not only in `practice/`.
- **Preserve his phrasing.** When he says the thing that made it click, store his words. An
  improved version of them loses the point.
- **`Status: solid` is earned**, by the *How I could have come up with this* section being filled
  in — never set it to tidy the record. An honest open thread is worth more than a clean status
  field.
- **Mark what is not yet his.** `**Not yet derived.**` for something taken on trust from a source;
  `**Unverified.**` for something inferred or recalled rather than checked. Both are greppable and
  the counts are the real progress metric. Do not delete a marker without doing the work, and do
  not add one silently in place of saying "I don't know".
- **Harvest, don't design.** A page is written after a session, not before one. A topic file
  created from a syllabus, a reading guide or a plan is a summary of someone else's route. Anything
  seeded rather than harvested says so at the top and does not get a `Status` above `open`.
- **Open threads carry context.** Enough that the next session can resume cold: what he tried,
  where it broke down.
- **Next step at the top of `log.md`**, specific enough to start from without re-deriving where he
  was.
- **Practice files record what the mistake *revealed*** — the missing intuition, the definition
  held only formally, the false analogy. Near-misses count: a right answer by an unconvincing route
  is a gap, not a success.
- **`adapted/` holds material, `topics/` holds record.** An adapted chapter is a text he now owns
  a better version of; a topic file is his trajectory through the subject. Link them, never merge
  them. In `adapted/`, mark supplied motivation as supplied, never hand over a proof, and list
  every cut.
- **`notes/` holds his own exposition** — the explanation he would give if he had to teach the
  thing. A third kind of object: `topics/` is record, `adapted/` is someone else's material
  rewritten, `notes/` is material he wrote. **A note is not evidence of understanding** — a clean
  exposition can be produced without deriving anything, and several were written with an AI
  assistant, so each carries a provenance banner saying so. When a note's subject is actually
  worked through in a session, that produces a topic file which *links* the note as material.
  Never promote a note to a topic file by adding a `Status` field to it.
- **Update at natural stopping points and at the end of a session**, not continuously. Breaking a
  derivation to take notes ruins the thing the session is for.

## Source material is referenced, never vendored

Downloaded sources — OCW notes, lecture PDFs, slides, preprints, scanned chapters — go in
`sources/`, which is **gitignored in full**. See [`sources/README.md`](sources/README.md).

What gets committed is the durable half: the URL and verdict in `resources/`, the rewrite in
`adapted/`, and the trajectory in `topics/`. A source is a cache; the judgement about it is not.
This is the same rule as *Link, never restate* — a repo that vendors its sources starts drifting
from them the day it copies them, and it is the copy that goes stale.

Licence matters here because this repo is published: most course notes, papers and chapters may
not be redistributed, and the permissively-licensed ones still carry conditions a notes repo should
not take on. **Never commit a source file, and never publish one to the site.**

### Papers are a source kind, not a better class of source

**A paper and a set of lecture notes are different objects and neither ranks above the other.**
Notes and books teach a subject as it is now understood. A paper is the record of someone arriving
at the idea — what problem they were stuck on, what they tried, what they had to argue for against
the alternative that looked just as good at the time.

That record is the thing this knowledge base exists to capture. *How could I have come up with
this?* is a question about the route to an idea, and the route is what a paper preserves and a
textbook deliberately removes: the published version presents the winner, in the order that makes
the proof convenient, with the search that produced it thrown away. The connections between
concepts, and the motivations that forced them, are recoverable from the original in a way they are
usually not from the exposition.

So the failure mode to avoid is not "preferring notes" — it is **papers being absent from the
workflow altogether**, which would leave the knowledge base built entirely on second-hand accounts
of other people's reasoning.

- **Catalogue papers as first-class sources**, alongside courses and books. `Kind: paper` already
  exists and `resources/cme-transcription.md` is already a paper catalogue; that is the norm, not
  the exception.
- **A syllabus's bibliography is a source in its own right** — an expert's judgement about which
  papers matter. Harvest it as entries, not as a footnote to the course.
- **Reach for the original when the question is *why*.** A method that carries its author's name —
  Gillespie's SSA, the finite state projection, the Poisson representation — has a paper that
  argues for it. The secondary account almost always drops the conditions and the argument.
- **Reach for the notes when the question is *what* or *how*.** A good course with problem sets
  beats a paper he has no route into, and the two are complementary: the paper for the motivation,
  the notes for the machinery and the exercises.

## An adaptation is a derivative work

The raw source is a *redistribution* question, settled above. An adaptation is a *derivative work*
question, and it is settled by the source's licence:

| Source licence | Adaptation goes to |
| --- | --- |
| CC BY-NC-SA (MIT OCW), CC BY, public domain | `docs/adapted/` — published, with attribution, and carrying **the same licence**, because share-alike propagates |
| all rights reserved | `adapted-private/` — gitignored, never published |
| unclear | `adapted-private/`, and say the licence is unresolved |

**Never guess in the publishing direction.** `adapted-private/` is the safe default and costs
nothing; a wrongly published derivative cannot be recalled from a public site. Both trees use the
same template and the same rules — only the destination differs, and `docs/topics/` is unaffected
either way, because a trajectory in his own words is not a derivative of anyone.

Every catalogue entry in `docs/resources/` carries the licence that decides this. If it does not,
resolve it before adapting, and record it there.

## What may be republished

**Decided 2026-09-14, deliberately, after the conservative reading was argued and rejected.**

A *conversion* — a source turned into markdown without rewriting it — is a derivative work like any
other, so it needs the same decision as an adaptation. The rule here is **by kind of source**, not
by licence:

| Source | Republish | Goes to |
| --- | --- | --- |
| a **course** or **lecture notes**, public on the web | yes, **cited and linked to the original** | `docs/reference/` |
| a **paper** — open access, arXiv, bioRxiv, PMC | yes, cited | `docs/reference/` |
| a **paper** behind a paywall | no | `reference-private/` |
| a **thesis** | no, unless its record's rights row has been read and permits it | `reference-private/` |
| a **book** | **never**, however obtained | `reference-private/` |
| anything with a visible "all rights reserved" | no | `reference-private/` |

A thesis is its own row because "open access" is asserted by the repository and the *rights* are
asserted per record by the author — CaltechTHESIS carries a Creative Commons grant on some theses
and "no commercial reproduction rights are provided" on others. Reading the row is cheap; assuming
it is the mistake this table exists to prevent.

**The mechanism is `material:` in `sources/sources.lock.yml`** — `course`, `notes`, `paper`,
`thesis`, `book`, `archive` or `data`, written by hand and never detected. `normalise_source.py`
reads it to pick the destination, and anything unclassified, plus anything with no URL to cite,
goes to `reference-private/`. `open_access: true` alongside `paper` or `thesis` is the one switch
that promotes a source into the published tree, and it is an assertion someone made, not a
detection.

`reference-private/` is gitignored, exactly like `adapted-private/`.

**The argument against, recorded so this reads as a choice rather than an oversight.** Publicly
available is not the same as redistributable: copyright is automatic, citation answers plagiarism
rather than copyright, and where no licence is granted, attribution does not create one. The
conservative reading would publish only the ~28 sources carrying an explicit CC, CC0 or BSD grant
and index the rest.

**Why the broader rule was taken anyway.** Course notes published openly by an academic are
published *to be read and taught from*, the convention in the field is that citation suffices, and
the two categories where that convention does not hold — commercial books and paywalled papers —
are excluded outright. Resolving licences one by one had also proved to be the real work rather
than a policy question: a single better-targeted sweep moved 24 sources from "unresolved" to a
confirmed CC BY, and most of the remainder are unchecked rather than restricted.

Two obligations follow and are not optional:

- **Every republished page cites its source and links to the original.** It is generated, not left
  to an author to remember, because the whole arrangement rests on it.
- **A real licence still governs.** Where a source carries CC BY-NC-SA or similar, share-alike
  propagates and the output carries the same licence. The rule above widens what may be published;
  it does not override a licence that says something specific.

If a rights-holder objects, the remedy is to remove the page and record the reason in the catalogue
entry — which is cheap, and is why the source URL is never dropped.

## `docs/reference/` — converted material

A fourth kind of object, and the distinctions between the four are the thing to keep sharp:

| | Holds |
| --- | --- |
| `topics/` | his **record** — the trajectory through a subject |
| `notes/` | **material he wrote** — his own exposition |
| `adapted/` | someone else's material **rewritten** motivation-first, proofs converted to exercises |
| `reference/` | someone else's material **converted**, not rewritten — the same text in markdown, split so it can be linked to |

`reference/` exists because a PDF has no addressable parts. A topic file cannot cite "§3 of lecture
7" when lecture 7 is a page range. Converted markdown gives every section a URL, which is what
makes the cross-referencing the rest of this repo depends on actually possible.

**Convert the source, not the render.** Verified on this repo's own material: a `.qmd` or `.tex`
converts with the author's LaTeX intact, while the PDF built from the same file turns
$\lambda(t) = f(t)/S(t)$ into `Sf((tt))becauseTiscontinuous`. Prose survives a PDF; mathematics does
not. Scanned or handwritten PDFs have no text layer at all and are not converted — they get an
index entry pointing at the original, because an almost-empty page that looks like a conversion is
worse than an honest absence.

**A converted file is regenerable output and is never edited by hand.** A hand edit is lost on the
next run and silently diverges from the source it claims to reproduce. Fix the converter, or make
an adaptation instead — `adapted/` is where changing the text is the point.

## How a page is shaped

This is a site as well as a repo, and a reader arrives mid-topic with one question. They should not
have to read a page to use it.

- **Open with the question**, then what it attaches to. That header is the navigation — it is how
  someone on the wrong page leaves in five seconds.
- **Prefer a link to a paragraph.** Every fact lives in exactly one place: sources and verdicts in
  `resources/`, background and anchors in `profile.md`, file templates in the skill's
  `references/kb-structure.md`. Restating one creates a second thing to update and a future
  contradiction. The site build fails on a broken internal link or a missing anchor, by design.
- **Length is a smell.** A topic file much past ~200 lines is usually carrying a restatement of the
  source. Cut rather than reorganise.
- **Cross-link heavily and keep the links live.** A stale link is worse than no link.

## Conventions

- Topic slugs lowercase and hyphenated (`chemical-master-equation.md`); practice files mirror topic
  slugs exactly; adapted files add a source slug (`martingales-williams-ch10.md`).
- New files start from the `_template.md` in the relevant directory.
- Dates are absolute ISO (`2026-09-13`), never "last week".
- Prose wrapped at ~100 characters, matching the existing files.
- Maths in LaTeX, `$…$` and `$$…$$`. Never `\(…\)` or `\[…\]` — they do not render in the site
  build and do not survive as plain text.
- Markdown must read well as plain text — this is a notes repo first, a rendered site second.

## Two audiences, one source

Everything in this repo is read by both a person and an agent, and the rule is the same as for the
notes: **one copy, referenced — never a second copy, search-replaced.**

| Path | Is | Never |
| --- | --- | --- |
| `AGENTS.md` | the instruction file | duplicated into `CLAUDE.md` by hand |
| `CLAUDE.md` | one `@AGENTS.md` import, plus Claude-specific notes only | a parallel copy of the above |
| `skills/` | the real skill tree | forked per agent |
| `.claude/skills`, `.agents/skills` | symlinks to `skills/` | real directories |

This repo previously carried two full skill trees and two instruction files, produced by
search-replacing `.claude/` to `.Codex/`. Every replaced path pointed at a directory that did not
exist, and the two copies had already begun to diverge. That is the failure this rule prevents.

**Skill bodies must not hardcode an install path.** A skill refers to its own files as
`references/<file>.md` and to a sibling skill's as `../<skill>/references/<file>.md`, so the same
text is correct whether it is loaded from the repo, from a symlink, or as an installed plugin.

## The site

`docs/` is published to GitHub Pages at <https://claptar.github.io/knowledge-base/> by
`.github/workflows/deploy-docs.yml` on every push to `main`. MkDocs Material, built with `uv`.

```bash
uv sync --group dev
uv run mkdocs serve           # preview at http://127.0.0.1:8000
uv run mkdocs build --strict  # what CI runs — do this before committing
```

- **Always build with `--strict`.** Broken internal links *and* missing anchors fail the build.
  That is the point: the notes cross-reference heavily and a stale link is worse than none.
- **A new page must be added to `nav:` in `mkdocs.yml`**, or the strict build fails on it.
- Maths is `pymdownx.arithmatex` with MathJax. Write `$…$` and `$$…$$`; never `\(…\)` or `\[…\]`,
  which arithmatex does not pick up from source.
- **MkDocs 1.x is pinned (`<2`) deliberately** — Material has announced 2.0 removes the plugin
  system with no migration path. Not a stale pin.
- `_site/` and `.venv/` are gitignored. Nothing outside `docs/` is ever published.

## Git

Commit only when asked. One commit per session, with a message naming what was studied — not
"update kb".

### Two long-lived branches

| Branch | Is | Receives |
| --- | --- | --- |
| `main` | what is released and published. The site deploys from it and every arrival is a candidate release | a merge from `draft`, when enough has accumulated to be worth releasing |
| `draft` | where the work happens — the integration branch, `dev` under another name | day-to-day commits, and short branches for anything large enough to want reviewing on its own |

**Never commit to `main`.** Work on `draft`. A session's notes can be committed straight to it; a
change big enough that you would want to see it whole first — a skill rewrite, a structural move —
gets its own branch off `draft` and a pull request back into `draft`.

```bash
git checkout draft && git pull          # always start here
# work, commit

# …or, for something substantial:
git checkout -b <kind>/<short-slug>     # session/martingales, chore/…, fix/…, skill/…
git push -u origin HEAD
gh pr create --draft --base draft --fill
```

**`--base draft` is not optional.** `gh pr create` targets the repository's default branch, which
is `main`, so a PR opened without it proposes a release rather than a change.

### Releasing: `draft` -> `main`

Promoting `draft` is the deliberate act that cuts a release, and it is the one time `main` is
touched:

```bash
gh pr create --base main --head draft --title "Release <version>"
```

Before opening it: bump the version in `.claude-plugin/plugin.json` and rename the `CHANGELOG`
`## Unreleased` section to that version with today's date. Accumulate entries under `## Unreleased`
as you go — writing the note when the change is fresh is the only time it is cheap, and a release
then costs a rename rather than an archaeology session through `git log`.

### A merge to `main` cuts a release

`.github/workflows/release.yml` runs on every push to `main`. It reads the version from
`.claude-plugin/plugin.json`, and if no tag exists for it, creates an annotated tag `v<version>`
and publishes a GitHub release whose notes are that version's section of
[`CHANGELOG.md`](CHANGELOG.md) — so the notes live in the repo, in the same commit as the change
they describe, rather than only in GitHub's database.

Two consequences worth holding on to:

- **A promotion that carries a skill, convention or script change bumps the version and names its
  `CHANGELOG` section.** The job fails the release if the section is missing, which is deliberate:
  a version with no notes is a version nobody can tell you about.
- **A promotion that only carries `docs/` notes bumps nothing**, and the workflow stays quiet. The
  content changes every session and is not what a release is for — `git log` already records it,
  and a tag per note would make the tag list useless for the thing it is actually for, which is
  telling someone which version of the skills they installed.

The second point is a deliberate softening of "every merge cuts a release": every merge *runs* the
release job, and every merge that changes the versioned artefact produces one. To release on every
merge regardless, change the version resolution step in the workflow — the comment there says how.

`main` is still the deploy branch, so a promotion also publishes the site. Notes that are merely
*written* are not published until `draft` is promoted, which is usually what you want and
occasionally a surprise — if something needs to be live now, that is a reason to promote, not a
reason to commit to `main`.
