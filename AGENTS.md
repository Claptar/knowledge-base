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
| `questions.md`, `profile.md`, `log.md`, `resources.md`, `topics/`, `practice/`, `adapted/` | the knowledge base — his notes and material | a study session happened, or something durable changed |
| `skills/` | the skills: `SKILL.md`, `references/`, `scripts/` | the *way* sessions run should change |

Don't let one drift into the other. Material learned goes in `topics/`; instructions about how to
teach go in the skill.

## The two skills

The real tree is `skills/`. `.claude/skills` and `.agents/skills` are **symlinks** to it, so both
audiences read one copy and there is no way for them to drift. Never edit through a symlink path
and never create a second copy — see [Two audiences, one source](#two-audiences-one-source).

Each `SKILL.md` is the authority on its own workflow.

- **`study-mentor`** — a live session. Ask which mode he wants, start from the problem rather than
  the definition, hold back the proof, close by asking *how could you have come up with this?*
- **`adapt-material`** — a source in, a document out. Rewrites a chapter, lecture, or paper
  motivation-first into `adapted/`, cutting what he holds cold and converting proofs to exercises.

Route between them by the shape of the output: a conversation is `study-mentor`, a file is
`adapt-material`. They hand off in both directions.

When working inside this repo, the knowledge base root is the repo root — read and write the files
directly, summarise the changes as a diff, and let him commit.

## The knowledge base is indexed by question

[`questions.md`](questions.md) is the front door, and the unit of navigation is a **question**, not
a subject. Subjects are how textbooks index, and the textbooks already exist. What is not in a
textbook is which question was live, what it attached to, and where it broke down.

Practical consequences:

- **A new question goes in `questions.md` first**, with no page behind it. That is the normal
  resting state of a question, not a gap to be filled.
- **A topic file opens with the question that forced it**, not with a definition. If the *question
  that opened it* section is empty, the file is not ready to exist.
- **Never route a new question to the nearest existing topic file.** A wrong attachment is worse
  than none: it implies the connection was already checked, and it quietly imports the wrong
  anchors. Say the knowledge base does not cover it and work from the source.

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

What gets committed is the durable half: the URL and verdict in `resources.md`, the rewrite in
`adapted/`, and the trajectory in `topics/`. A source is a cache; the judgement about it is not.
This is the same rule as *Link, never restate* — a repo that vendors its sources starts drifting
from them the day it copies them, and it is the copy that goes stale.

Licence matters here because this repo is published: most course notes, papers and chapters may
not be redistributed, and the permissively-licensed ones still carry conditions a notes repo should
not take on. **Never commit a source file, and never publish one to the site.**

## How a page is shaped

This is a site as well as a repo, and a reader arrives mid-topic with one question. They should not
have to read a page to use it.

- **Open with the question**, then what it attaches to. That header is the navigation — it is how
  someone on the wrong page leaves in five seconds.
- **Prefer a link to a paragraph.** Every fact lives in exactly one place: sources and verdicts in
  `resources.md`, background and anchors in `profile.md`, file templates in the skill's
  `references/kb-structure.md`. Restating one creates a second thing to update and a future
  contradiction.
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

## Git

Commit only when asked. One commit per session, with a message naming what was studied — not
"update kb".
