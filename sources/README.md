# sources/

Working copies of downloaded source material — OCW notes, lecture PDFs, slides, paper preprints,
scanned chapters.

**Nothing in here is committed.** `.gitignore` excludes everything except this file. The directory
exists so that a source sits at a stable path while it is being adapted, not so that it is stored.

## Why it is not committed

- **Licence.** This repo is published as a site. Most course notes, papers and book chapters may
  not be redistributed, and the ones that may (OCW is CC BY-NC-SA) still carry conditions that a
  notes repo has no business taking on. Linking to a source carries no such conditions.
- **It is the same rule as everywhere else here.** A knowledge base that vendors its sources starts
  drifting from them the day it copies them, and the copy is the thing that goes stale. The repo
  keeps the *verdict* and the *adaptation*; the source stays where it is published.
- **Git is bad at binaries.** A PDF committed once is in the history forever, and the site build
  carries it.

## What is committed instead

| Thing | Where | Why it is the durable part |
| --- | --- | --- |
| The source's URL, and the verdict on it | [`../docs/resources/`](../docs/resources/) | the judgement is expensive; the bytes are not |
| The rewritten version | [`../docs/adapted/`](../docs/adapted/) | his own document, with motivation supplied and proofs converted |
| What he actually got from it | [`../docs/topics/`](../docs/topics/) | the trajectory, which exists nowhere else |

An adapted file names its source, the section, and the date accessed, so the original is one click
away and the adaptation can be checked against it.

## `_archives/`

The publisher's original zips, kept beside the unpacked directories. Together with each source's
`_manifest.csv` they are what makes the rename reversible: the manifest maps a normalised path back
to the publisher's filename, and the zip is the thing that filename came from. Gitignored like
everything else here — if it is lost, the catalogue entry's URL is the route back.

## Using it

Drop a download in, adapt it, and let it be deleted. If it matters, it is in `resources/` with a
link — and if the link dies, that is what `resources/` is for recording.

To keep a durable personal library across machines, point this directory at a synced folder rather
than storing files in the repo:

```bash
rmdir sources && ln -s ~/"Google Drive/study-sources" sources
```

Every path in the repo stays the same, nothing extra is committed, and no connector or auth is
involved. The `.gitignore` entry already covers a symlink.
