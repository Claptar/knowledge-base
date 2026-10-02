@AGENTS.md

# Claude Code notes

Everything above is imported from [AGENTS.md](AGENTS.md), which is the single instruction file for
every agent working in this repo. Do not copy its content here — edit `AGENTS.md` instead.

Claude-specific only:

- The skills load from `.claude/skills`, which is a **symlink** to `skills/`. Edit `skills/`.
- Installed as a plugin (`study-kb`), the same three skills appear namespaced as
  `study-kb:study-mentor`, `study-kb:adapt-material` and `study-kb:adapt-recordings`. The other
  two, `collect-materials` and `normalise-materials`, belong to the library repository's
  `study-library` plugin.
- An installed plugin does **not** load this file or `AGENTS.md`, so any rule a skill depends on
  must be written in the skill itself.
- Keep exactly one installed copy of each skill. A stale account-synced or uploaded copy runs old
  rules wherever it triggers instead of the repo copy.
