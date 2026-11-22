# Reaching the library

The companion **library** holds other people's material, written up so it can be read and linked
to. It has one book per course (lecture notes merged from the slides, recordings and problem
sets) and a **Papers shelf** with a summary of each paper, plus the full text where the paper's
licence allows. It is public, so any agent that can fetch a web page can read it, from a laptop,
a browser or a phone. Nothing here is written to it. It is read-only from this side.

## Where it is

| | Base address |
| --- | --- |
| Site (rendered) | `https://claptar.github.io/knowledge-base-library/` |
| Raw markdown (best for an agent) | `https://raw.githubusercontent.com/Claptar/knowledge-base-library/main/docs/` |

## Find anything in one fetch

Fetch **`https://raw.githubusercontent.com/Claptar/knowledge-base-library/main/docs/SUMMARY.md`**.
It is the generated table of contents, about 80 KB, and lists every book, every chapter by title,
and every paper, each with its path. Pick the entry, then fetch it:

| Path in `SUMMARY.md` | Raw markdown | Site page |
| --- | --- | --- |
| `X/NN-topic.md` | `…/main/docs/X/NN-topic.md` | `…/knowledge-base-library/X/NN-topic/` |
| `X/index.md` | `…/main/docs/X/index.md` | `…/knowledge-base-library/X/` |

Example: `probability/mit-ocw/6041sc/14-the-poisson-process.md` is MIT 6.041SC's Poisson-process
chapter.

The catalogue in this knowledge base links to the same pages: a `**Converted:**` or `**Library:**`
line on an entry in `docs/resources/`. When you start from a source he already knows, start
there.

## Layout

- **Books:** `docs/<discipline>/<provider>/<course>/`, for example
  `probability/mit-ocw/6041sc/`. `index.md` is the book's contents and provenance, `NN-<topic>.md`
  are the chapters, and `solutions/` holds the course's own worked solutions where it published
  them.
- **Papers:** `docs/papers/<subject>/<slug>/index.md`. The summary comes first; the full text is
  beneath it only where the licence allows. The slug matches the paper's catalogue entry here.

## Before relying on a page

- **The books are written by a language model** from the course material, so they are not the
  lecturer's words. Quote and cite the *original* (lecture, slide, timestamp, problem set), which
  each chapter names in its `## Sources` section. **Never adapt from a book.** Adapt from the
  original (`../adapt-material/SKILL.md`, Step 1).
- **Read the chapter's `## Sources` first.** Some chapters were written from truncated or
  model-reconstructed input, and say so there. Treat any equation in such a chapter as unverified.
- **Two books repeat themselves.** Stat 210A and Stat 153 merge several course years imperfectly,
  so the same topic can appear in more than one chapter. Check the neighbouring chapters before
  concluding that the book does not cover something.
- **A paper summary is a route into the paper, not a replacement for its argument.** For *why*,
  read the original.
- **If a fetch fails**, the page may have moved. Re-fetch `SUMMARY.md` and look again by title
  rather than guessing a path.
