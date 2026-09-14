@AGENTS.md

# Claude Code notes

Everything above is imported from [AGENTS.md](AGENTS.md), which is the single instruction file for
every agent working in this repo. Do not copy its content here — edit `AGENTS.md` instead.

Claude-specific only:

- The skills load from `.claude/skills`, which is a **symlink** to `skills/`. Edit `skills/`.
- Installed as a plugin, the same five skills appear namespaced as `study-mentor`,
  `adapt-material`, `adapt-recordings`, `collect-materials` and `normalise-materials` under this repo's plugin name.
