# AGENTS.md

Instructions for any coding agent working in this repository — Claude Code, Codex, or otherwise.
This is the **one** instruction file. `CLAUDE.md` imports it; nothing is duplicated here by hand.

## What this repository is

A personal study knowledge base — markdown notes on mathematics and computational biology — plus
the skills that maintain it. There is no application and no build. The content *is* the product,
so the bar for an edit is whether a human reading the file six months from now is better off.

The repo has two halves, and they are edited for different reasons:

| Path | What it is | Edit when |
| --- | --- | --- |
| `docs/` — `index.md`, `questions.md`, `path.md`, `profile.md`, `log.md`, `resources/`, `topics/`, `practice/`, `adapted/` | the knowledge base — his notes and material. Also the published site | a study session happened, or something durable changed |
| `skills/` | the skills: `SKILL.md`, `references/`, `scripts/` | the *way* sessions run should change |

Don't let one drift into the other. Material learned goes in `docs/topics/`; instructions about how
to teach go in the skill.

**The knowledge base root is `docs/`.** Bare filenames below (`profile.md`, `topics/`) mean relative
to it. Everything in `docs/` is published; nothing outside it is.

## The three skills

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

Route by the shape of the output first — a conversation is `study-mentor`, a file is one of the
adapters — then by the source: a transcript or recording is `adapt-recordings`, anything written is
`adapt-material`. All three hand off in every direction.

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
