# Study knowledge base

Topics, practice, resources and learning trajectories in mathematics (probability, statistics,
stochastic processes, linear algebra) and computational biology — maintained together with the
`study-mentor` skill that ships in this repo.

Plain markdown, readable on its own and renderable by a static site generator. Every file should
make sense to a human reading it directly: these are notes, not a machine log.

## Layout

```
questions.md              the front door — open questions, and where each one lives
profile.md                durable background, notation habits, anchors, how I study
log.md                    dated sessions, newest first, next step at the top
resources.md              evaluated materials with verdicts
topics/<topic>.md         one per topic: the trajectory through it, not a summary
practice/<topic>.md       attempts, mistakes, and what each mistake revealed
adapted/<topic>-<src>.md  external material rewritten into the form I learn from
sources/                  downloaded source material — gitignored, never committed

skills/study-mentor/      runs study sessions; reads and writes all of the above
skills/adapt-material/    rewrites a chapter, lecture or paper into adapted/

AGENTS.md                 the one instruction file, for any agent
CLAUDE.md                 imports AGENTS.md; Claude-specific notes only
.claude/skills            symlink to skills/
.agents/skills            symlink to skills/
.claude-plugin/           makes the repo installable as a Claude Code plugin
```

The index is **questions**, not subjects — subjects are how textbooks index, and the textbooks
already exist. Start at [questions.md](questions.md).

Topic slugs are lowercase and hyphenated — `martingales.md`, `chemical-master-equation.md` — and
practice files mirror topic slugs so the pair is obvious. Start new files from the `_template.md`
in each directory.

## The organising idea

Understanding means being able to answer **"how could I have come up with this?"** — for the
question, the definition, and the proof technique. Every convention here follows from that:

- A topic is `solid` when the *How I could have come up with this* section is filled in, not when
  the material has been covered.
- Open threads stay visible and carry enough context to resume cold.
- Insights are recorded in my own words, not in a tidied-up version of them.
- Trajectories, not summaries. A polished restatement of the material is in any textbook.

## Using the skills

Run Claude Code from the repo root and both skills load from `skills/`, via the `.claude/skills`
symlink. To use them outside this repo, install it as a plugin:

```
/plugin marketplace add Claptar/knowledge-base-claude
/plugin install study-kb@claptar-study
```

- **`study-mentor`** — a live session. Reads `profile.md` and the relevant topic and practice
  files, teaches Socratically by default, and writes back at natural stopping points.
- **`adapt-material`** — hand it a book chapter, lecture notes, slides or a paper and it returns a
  rewritten document in `adapted/`: the problem before the definition, what I hold cold cut out,
  proofs converted to exercises with hints behind `<details>`.

They hand off to each other — adapt a chapter, then work through it in a session.

See [AGENTS.md](AGENTS.md) for the conventions both follow and
`skills/study-mentor/references/kb-structure.md` for the file templates in full.
