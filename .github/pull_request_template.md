<!-- Open as a draft; mark ready when it is. See AGENTS.md § Git. -->

## What changed, and why

<!-- The reason, not the diff. If this is a study session, say what was studied. -->

## Release

Tick one:

- [ ] **Content only** — `docs/` notes, no version bump. The release job will stay quiet.
- [ ] **Versioned change** — a skill, convention, script or the site config. Then:
  - [ ] bumped `version` in `.claude-plugin/plugin.json` (and `pyproject.toml` if it moved too)
  - [ ] added the matching `## <version>` section to `CHANGELOG.md`

A versioned change without a `CHANGELOG` section fails the release job on merge, by design.

## Checks

- [ ] `uv run mkdocs build --strict` passes
- [ ] no source file committed under `sources/`, and no derivative of an all-rights-reserved
      source added under `docs/adapted/`
