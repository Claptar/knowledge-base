<!-- Check the base branch first. Work merges into `draft`; only a release targets `main`.
     See AGENTS.md § Git. -->

## What changed, and why

<!-- The reason, not the diff. If this is a study session, say what was studied. -->

## Which kind of PR is this?

- [ ] **Into `draft`** — ordinary work. Add a note under `## Unreleased` in `CHANGELOG.md` if this
      touches a skill, convention or script; `docs/` notes need nothing.
- [ ] **`draft` -> `main`, a release.** Then:
  - [ ] set `version` in `plugin/.claude-plugin/plugin.json` to today's `YY-DDD` (`date +%y-%j`), or
        `YY-DDD.1`, `.2`… if that tag already exists
  - [ ] set the same version in the `**Version:**` line of `plugin/skills/study-mentor/SKILL.md`
  - [ ] renamed `## Unreleased` to `## <version> — <date>` in `CHANGELOG.md`

A release whose version has no `CHANGELOG` section fails the release job on merge, by design.

## Checks

- [ ] `uv run mkdocs build --strict` passes
- [ ] no source file committed under `sources/`, and no derivative of an all-rights-reserved
      source added under `docs/adapted/`
