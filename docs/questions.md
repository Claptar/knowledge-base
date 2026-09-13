# Open questions

The front door. This knowledge base is indexed by **question**, not by subject — subjects are what
textbooks index, and the textbooks already exist. What is not in a textbook is which question was
live for me, what it attached to, and where it broke down.

A question earns a place here the moment it is asked properly. It earns a *page* only once a
session has actually been spent on it — see [Harvest, don't design](#harvest-dont-design).

## Live

| Question | Status | Where |
| --- | --- | --- |
| Does organising applied maths by *modelling task* rather than by technique survive contact with a real derivation, or does it dissolve? | open | no page yet |
| Is the verification/validation split meaningful in single-cell work, where "reality" is itself a noisy, heavily-processed measurement rather than a clean experiment? | open | no page yet — the [capstone](path.md#capstone) is where it gets answered |

## Proposed, not live

The [learning path](path.md) carries a question per node — a reconstruction of what *would* force
each concept, written in advance. Those are candidates and they stay off this table: a question
written by a plan is not the same object as one I actually hold, and mixing them would make this
page a syllabus.

A proposed question moves here when I can feel its force without re-reading the node — and the test
is whether it bites without the node in front of me, not whether it reads well on the page.

The martingale and generator questions sat in the table above until 2026-09-13 and were moved back
out, because neither had been started and both turned out to be the path's phrasing rather than
mine. They remain as [nodes 3](path.md#3-martingale) and [6](path.md#6-generator-and-semigroup).
That direction of travel is normal and is not a loss — an empty Live table is a truthful one.

## Status vocabulary

| Status | Means |
| --- | --- |
| `open` | live — the next session could pick it up |
| `parked` | a real question, deliberately not being worked now. Says why in the topic file |
| `answered` | the topic file's *How I could have come up with this* section answers it in my own words |

`answered` is earned the same way `Status: solid` is earned on a topic file, and by the same
evidence. Neither is set to tidy the record.

## Markers

Two greppable markers carry what is *not* yet known, and the counts are the honest progress
metric — more useful than counting pages.

| Marker | Means |
| --- | --- |
| `**Not yet derived.**` | stated here, but I have not worked it out myself. Taken on trust from a source |
| `**Unverified.**` | inferred or recalled rather than checked against the source |

```bash
grep -rn "Not yet derived\|Unverified" topics/ adapted/ practice/ | wc -l
```

Resolving one of these is worth more than adding a page. Do not delete a marker without actually
doing the derivation, and do not add one silently in place of saying "I don't know".

## Harvest, don't design

**A page is written after a session, not before one.** A topic file created from a syllabus, a
reading guide or a plan is a summary of someone else's route, and a clean restatement of the
material is available in any textbook. A question can sit in the table above indefinitely with no
page behind it; that is the normal state, not a gap to be filled.

Anything seeded rather than harvested says so at the top of the file and does not get a `Status`
above `open`.

## When nothing here matches

Say so, and work from the source directly. Do not route a new question to the nearest existing
topic file — a wrong attachment is worse than none, because it implies the connection was already
checked and it quietly imports the wrong anchors.

If the question turns out to be real, add it here first, with no page, and let a session decide
whether it deserves one.
