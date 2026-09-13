# UC Berkeley — Statistics, and departments that cross-list with it

**Verified:** 2026-09-13.

Berkeley statistics courses publish through a vanity domain per course, built from a GitHub
organisation per course. Graduate courses cross-listed with another department — Public Health,
Political Science, Mathematics — do **not** use that system and have to be chased separately.

## Where the material actually is

```
https://stat<num>.berkeley.edu/                landing page. Lists semesters. No material.
https://stat<num>.berkeley.edu/<term>/         per-offering page: instructor, topics, links
https://github.com/berkeley-stat<num>/<term>/  THE SOURCE. The site is a render of this.
https://github.com/berkeley-stat<num>/berkeley-stat<num>.github.io   theme only — see Licence
```

`<num>` is lowercase with the letter suffix: `205a`, `230a`, `241b`. `<term>` is `fall-2024`,
`spring-2026`. **Go to the GitHub org first** — it has the history, and occasionally files the
rendered site does not link.

Two department-level indexes, both worth checking before guessing:

- <https://statistics.berkeley.edu/courses/websites> — the authoritative list of which courses have
  a vanity domain. If a course is absent here, the `stat<num>.berkeley.edu` guess will fail DNS.
- <https://classes.berkeley.edu> — per-semester class search. The only reliable way to find out
  whether a course still runs.

A quick existence sweep is cheaper than searching:

```bash
for c in 150 153 205a 243; do
  printf '%-8s %s\n' "$c" "$(curl -sL -o /dev/null -w '%{http_code}' --max-time 10 https://stat$c.berkeley.edu)"
done          # 000 = no such host, so no vanity domain
```

```bash
gh api "orgs/berkeley-stat<num>/repos?per_page=100" \
  --jq '.[] | "\(.name)  \(.license.spdx_id // "none")"'    # 404 = no org
```

## Cross-listed graduate courses — the separate system

A `C` prefix means cross-listed, and the material usually lives with the **other** department or on
the instructor's personal page, not under `stat<num>`:

| Statistics | Also | Where the material is |
| --- | --- | --- |
| `STAT C245C–F` | `PB HLTH C240C–F` | Dudoit's pages under `stat.berkeley.edu/~sandrine/` |
| `STAT C247C` | `PB HLTH C240x` | instructor page; offered in even-numbered years only |
| `STAT C205A/B` | `MATH C218A/B` | has a vanity domain *and* legacy pages under `~aldous/205A` |
| `STAT C239A` | `POL SCI C236A` | **retired** — succeeded by `STAT 256` |

Instructor pages follow `https://www.stat.berkeley.edu/~<username>/`, and **directory listing is
disabled** — the folder 404s while files inside it fetch fine. Find filenames through a search
engine, not by browsing. Older course pages persist for years after the course stops running and
are often the only public copy; `~aldous/205A` and `~aldous/205B` carry real lecture notes and
scribe notes that the current vanity domain does not.

## What is gated

**bCourses** (Berkeley's Canvas) is the common answer, and it is not reachable. A per-offering page
saying *"uses bCourses this semester"* or a syllabus saying *"lecture notes will be provided on the
class website"* means the material is behind a login. `Stat 150 spring-2026` is exactly this: the
page names the instructor and the topics, and links to `bcourses.berkeley.edu`.

Mark these `Access: unreadable` and name bCourses. Do not go looking for a mirror, and never
reconstruct the notes from the topic list.

## Licence

**Berkeley course material carries no blanket licence.** Unlike MIT OCW, there is no
institution-wide CC grant, so the default is all rights reserved and adaptations go to
`adapted-private/`.

**The trap.** Every `berkeley-stat<num>.github.io` repo reports `MIT` through the GitHub API. Its
LICENSE file reads:

```
MIT License
Copyright (c) 2019 Kevin Lin
```

Kevin Lin is the author of the *just-the-class* Jekyll template. That MIT licence covers the site
template and says nothing about the course content. **Read the LICENSE file; do not read the API's
licence field.** If the copyright line names someone who is not the instructor or the university,
it is the template's.

Content repos are nearly all unlicensed. Two verified exceptions, both in `berkeley-stat243`:

| Repo | Licence |
| --- | --- |
| `stat243-fall-2021` | **CC0-1.0** — public domain, adaptable and publishable |
| `stat243-fall-2023` | **BSD-3-Clause** — adaptable with attribution |

`NOASSERTION` means GitHub found something it could not classify. Open it and read it.

## Gotchas

- **Course numbers change, and the old number keeps returning results.** `STAT 200A/B` was replaced
  by `STAT 201A/B` in 2012–13 and, per the department's own
  [notice](https://statistics.berkeley.edu/courses/notices/noticeAbout200ABand201AB), *"will not be
  taught in the near future"*. `STAT C239A` was succeeded by `STAT 256`. Search results happily
  return decade-old pages for both. Check `classes.berkeley.edu` before treating a course as live.
- **`guide.berkeley.edu` and the catalog sites are JS-rendered.** They fetch as an empty navigation
  shell. `guide.berkeley.edu/courses/stat/stat.pdf` serves *HTML*, not a PDF, and contains no course
  data. Don't route through the catalogue; use the department pages.
- **A course can be co-taught under two numbers**, with only one of them having a site. `STAT 256`
  has no domain of its own — its syllabus sits under `stat156.berkeley.edu/fall-2024/`.
- **An org with only a `.github.io` repo is an empty shell.** `berkeley-stat157` and
  `berkeley-stat241b` have the theme and no content.
- **Syllabus PDFs do not parse through a fetch tool** but are saved to disk, and the reading list is
  usually the most valuable thing on them. See `github-courses.md` for the extraction snippet.
