# Study knowledge base

Topics, practice, resources and learning trajectories in mathematics (probability, statistics,
stochastic processes, linear algebra) and computational biology — maintained together with the
`study-mentor` skill that ships in this repo.

Plain markdown, readable on its own and renderable by a static site generator. Every file should
make sense to a human reading it directly: these are notes, not a machine log.

## Layout

```
docs/                          the knowledge base, and the published site
  index.md                     site front door
  questions.md                 open questions — the index, and where each one lives
  path.md                      the learning path — a plan, and the only page written in advance
  profile.md                   durable background, notation habits, anchors, how I study
  log.md                       dated sessions, newest first, next step at the top
  resources/                      evaluated materials with verdicts
  topics/<topic>.md            one per topic: the trajectory through it, not a summary
  practice/<topic>.md          attempts, mistakes, and what each mistake revealed
  adapted/<topic>-<src>.md     external material rewritten into the form I learn from

skills/study-mentor/           runs study sessions; reads and writes all of the above
skills/adapt-material/         rewrites a chapter, lecture or paper into adapted/
sources/                       downloaded source material — gitignored, never published

AGENTS.md                      the one instruction file, for any agent
CLAUDE.md                      imports AGENTS.md; Claude-specific notes only
.claude/skills, .agents/skills symlinks to skills/
.claude-plugin/                makes the repo installable as a Claude Code plugin
mkdocs.yml                     site config
```

**Everything in `docs/` is published; nothing outside it is.** The index is **questions**, not
subjects — subjects are how textbooks index, and the textbooks already exist. Start at
[docs/questions.md](docs/questions.md).

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
/plugin marketplace add Claptar/knowledge-base
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

## The site

Published to <https://claptar.github.io/knowledge-base/> on every push to `main`, by
[`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml). MkDocs Material, with
MathJax so the LaTeX actually renders.

```bash
uv sync --group dev
uv run mkdocs serve           # preview — see the note below on the URL
uv run mkdocs build --strict  # what CI runs
```

**`mkdocs serve` serves under the `site_url` path, not the root.** This is a project page, so the
preview is at <http://127.0.0.1:8000/knowledge-base/> — plain `127.0.0.1:8000` returns a
302 and every deeper path a 404.

`--strict` turns a broken internal link or a missing anchor into a build failure — the notes
cross-reference heavily, and a stale link is worse than none.
