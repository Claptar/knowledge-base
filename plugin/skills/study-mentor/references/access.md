# Reaching the knowledge base

The knowledge base lives at **https://github.com/Claptar/knowledge-base**, a git repository of
markdown files structured like a notes site (see `kb-structure.md` in this directory for the layout
and templates). It is the source of truth for what he has studied, where he got stuck and what is
next. Four ways to reach it, in order of preference.

**Local clone.** Filesystem access with the repo checked out. Read and write directly, show a
diff-style summary of what changed, and he commits. Best for a long working session where the
knowledge base is touched repeatedly. This skill ships inside that repo under `plugin/skills/`, and
the knowledge base root is **`docs/`** — `profile.md`, `log.md`, `questions.md`, `topics/` and
`practice/` all live there, and `docs/` is also what the published site is built from. Bare
filenames in these skills mean relative to that root. No setup step is needed.

**GitHub connector.** If GitHub tools are available, read the files and propose updates directly.
Best for short sessions and for "what was I stuck on last time" — no local setup, no manual
transport. **Read the repository's `AGENTS.md` first and follow its git rules.** For this
repository that means: commit only when he asks; never to `main`, which deploys the site and cuts
releases; work on `draft`, or the branch it names. Commit one coherent change at the end of the
session rather than a commit per edit, with a message that says what was studied, not "update kb".

**Read-only by URL.** No clone and no connector, as on his phone or in a browser chat, but you can
fetch web pages. The repository is public, so read the current files from the `draft` branch at
`https://raw.githubusercontent.com/Claptar/knowledge-base/draft/docs/<file>`, for example
`…/draft/docs/log.md` and `…/draft/docs/profile.md`. Reading is all this mode can do. If a fetch is
refused, ask him to paste the files instead. The session ends with the session record from
`kb-structure.md`, and you say plainly that nothing was saved.

**Chat with neither.** Ask him to paste or upload the relevant files. The session ends with the
session record, and he is the transport layer: say so plainly rather than pretending the write
happened, and never leave him splicing fragments by hand.

**The library is reachable the same way.** Other people's courses as books, plus paper summaries,
are public and readable by URL from anywhere. How to find a chapter or a paper in one fetch, and
what to check before relying on it, is in `library.md` in this directory.

**No knowledge base yet.** Run `scripts/init_kb.py <path>` to lay down the skeleton, then fill
`profile.md` from `background.md` in this directory plus anything new he says.
