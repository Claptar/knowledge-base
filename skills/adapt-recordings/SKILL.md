---
name: adapt-recordings
description: Turns lecture recordings into proper notes — caption/transcript files (.srt, .vtt) or raw audio/video from a course, rewritten into structured markdown rather than cleaned-up speech. Use when he points at a recorded lecture, a captions file, a course with video, or a directory of transcripts and wants notes out: "make notes from these lectures", "turn this transcript into something readable", "what's in the 6.041 recordings", "adapt this lecture series". Handles the two things a written source never requires — reconstructing mathematics that was spoken aloud and written on a board the transcript cannot see, and naming what the recording refers to but does not contain. Produces documents, not a conversation. Use adapt-material when the source is already a written document, and study-mentor when he wants to be taught live.
---

# Adapt recordings

## What this is for

A transcript is not a document. It is speech: no sections, no equations, no figures, sentences that
restart, and constant reference to a blackboard nobody wrote down. Handing one to `adapt-material`
unchanged produces tidied-up talking, which is worse than either the recording or real notes.

This skill owns the part that is specific to recordings — reconstructing what was on the board,
naming what is missing, and deciding which recordings are worth the effort at all. It does **not**
own the shape of the finished document: that is `../adapt-material/SKILL.md`, and it is not restated
here. Read that skill before writing anything; the output contract is the same one.

**The single thing to get right:** a transcript says "sigma squared over n". The board said
$\sigma^2/n$. Rendering that is *inference from audio about something written that was never
captured*, and a wrong reconstruction lands in notes that look authoritative. Every such
reconstruction gets marked. See step 3.

## Step 1 — find what exists, and check the licence

Recordings live in `sources/<course>/` as `.srt` or `.vtt` alongside the PDFs. The catalogue entry
in `docs/resources/` says which courses have them and how many.

**Licence first, as in `adapt-material` step 6.** MIT OCW is CC BY-NC-SA, so these adaptations are
publishable in `docs/adapted/` with attribution and the same licence. A recording from anywhere else
— a paywalled course, a conference talk, a departmental seminar — is all-rights-reserved, and its
adaptation goes to `adapted-private/`. Never guess in the publishing direction.

**No captions?** Then there is no transcript to work from, and producing one is a separate step
requiring the media file and a speech-to-text pass. Say so rather than working from the slides and
calling it a lecture adaptation. If he wants that, agree the transcription step explicitly first —
it is a different job with a different failure mode.

## Step 2 — decide what is worth adapting, and say so

**Do not adapt a lecture series end to end by default.** 6.041SC alone has 76 recordings; adapting
all of them would produce a worse copy of a textbook he could read faster. Most recorded lectures
are redundant with a written source, and the catalogue verdict should already say which.

Triage the set before starting, and show him the triage:

- **Worth it** — worked examples and problem sessions, where the value is watching a choice get
  made and a wrong route rejected. A textbook presents the solution; a recording shows the search.
  This is the part that matches how he wants to study, and it is usually a minority of the files.
- **Redundant** — the standard exposition of material a book in `docs/resources/` covers better.
  Say which book, and skip.
- **Unclear** — read the first few minutes and decide.

A recording earns adaptation when it contains something the written sources do not: a motivation
the textbook omits, a failure explored rather than avoided, or a worked problem.

Ask once, with the triage in hand, before spending the session on a batch.

## Step 3 — reconstruct, and mark every reconstruction

This is the whole difficulty. Three failure modes, all of them silent.

### Spoken mathematics

Convert spoken maths to LaTeX, and **mark it `**Unverified.**` unless the same expression is
confirmed by a written source** — the lecture notes PDF, a problem set, the textbook. Confirmation
demotes it to plain text; nothing else does.

Ambiguities that a transcript genuinely cannot settle, and which must not be silently resolved:

- **Scope.** "sigma squared over n" is $\sigma^2/n$ or $(\sigma/n)^2$ or $\sigma^2/\sqrt n$ —
  spoken maths has no brackets.
- **Indices and hats.** "x n" is $x_n$ or $x^n$; "theta hat" survives, "theta bar" often does not.
- **Homophones.** "a" / "eigh", "pi" / "p sub i", "e to the" / "eta".
- **Caption errors.** Auto-generated captions mangle technical vocabulary. `martingale` →
  "martin gale", `i.i.d.` → "I ID". Correct these, and do not treat a corrected word as confirmed.

Where the reading genuinely matters and cannot be settled, give both and say so. A note that says
"this is either $\sigma^2/n$ or $(\sigma/n)^2$; the lecture notes would settle it" is useful. A note
that silently picks one is a trap.

### Deixis — what the recording points at but does not contain

"As you can see here", "this term cancels with that one", "the graph on the left". The referent was
on a board and is gone.

**Name the gap. Never invent the referent.** Write what is known and mark what is missing:

> **Not in the transcript.** He points at a term that cancels here. The lecture notes PDF, if it
> covers this, would say which — otherwise this step has to be re-derived.

Inventing a plausible cancelling term is the worst thing this skill can do: it is undetectable,
and it is exactly the kind of confident wrong detail that a reader six months later has no way to
question.

### Structure

A transcript is flat. The finished notes need sections, and the section boundaries are a
*judgement* — they are not in the source. Impose them, and keep timestamps at each boundary so the
original is reachable.

**Timestamps are this skill's page numbers.** `adapt-material` requires a pointer back to the source
at each part; here that pointer is `[12:45]`, taken from the caption cues. Keep them.

## Step 4 — shape it

Hand off to the rules in `../adapt-material/SKILL.md`: problem before definition, what he holds cold
cut out, proofs converted to statements plus a hint ladder, supplied motivation marked
`> **Supplied.**`, every cut listed. Those rules are not repeated here and this skill must not
paraphrase them — if they and this file ever disagree, `adapt-material` is right.

Two things that differ because the source is speech:

- **An aside can be the most valuable thing in the file.** Lecturers say "the reason we do it this
  way is…" out loud and never write it down. That is precisely the motivation textbooks omit and
  the reason to mine recordings at all. Promote it; do not cut it as digression.
- **Verbal hedging is signal, not noise.** "This is a bit of a trick", "you'd never guess this the
  first time" is the lecturer naming an artificiality. Keep it, in his words — it belongs under
  *Where the source is artificial*.

Cut filler, false starts, repetition, administrative announcements and the licence preamble
without comment.

## Step 5 — file it

Follow `adapt-material` step 6, with these specifics:

- `docs/adapted/<topic>-<course-slug>-<lecture>.md`, or one file per coherent run of lectures where
  they form a single argument. Not one file per 76 recordings.
- Set `**Source:**` to the course, the recording, and the timestamp range.
- Update the course's catalogue entry `Adapted:` field to point at what was produced, and record
  in the entry's verdict what the triage concluded — which recordings were worth it and which were
  redundant. **That triage is the expensive judgement here**, exactly as a verdict is in
  `docs/resources/`, and redoing it in six months is the waste this avoids.
- Report the count of `**Unverified.**` marks left in the file. That number is the honest measure of
  how much of the document is reconstruction rather than record, and it is what tells him whether
  to check it against the notes PDF before trusting it.

## Reference files

Shared with the other two skills, which remain the authorities:

- `../adapt-material/SKILL.md` — the output contract. **Read before writing.**
- `../study-mentor/references/taste.md` — what "excellent" means to him.
- `../study-mentor/references/background.md` — durable background and anchors.
- `../study-mentor/references/kb-structure.md` — where output goes and why.
