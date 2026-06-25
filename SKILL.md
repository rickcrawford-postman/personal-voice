---
name: personal-voice
description: |
  Write and edit prose so it reads like a specific person wrote it, not an AI
  agent. Use this whenever drafting or rewriting anything that will be read by
  humans (a blog post, essay, newsletter, email, README, doc, social post, or
  report) and you want it to sound personal rather than generated. Also use it
  as a pre-publish pass to strip the patterns that make text read as AI, and to
  match a particular person's voice when a writing sample is provided. Built on
  the humanizer skill and Wikipedia's "Signs of AI writing." Triggers include
  "make this sound human," "this reads like AI," "rewrite in my voice," "clean
  this up before I post it," "write this as a person, not a bot," or any request
  for natural, personal-sounding writing.
license: MIT
compatibility: claude-code claude-ai cowork opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
---

# Personal Voice

Write and edit so the result reads like a person, not an agent. This skill does two jobs: it drafts new writing in a natural personal voice, and it audits existing drafts to remove the patterns that flag text as AI-generated. It is built on the humanizer skill, which draws its pattern catalog from Wikipedia's "Signs of AI writing" (maintained by WikiProject AI Cleanup), with additional patterns observed in long-form drafting.

## Personal voice versus agent voice

Agent prose is fluent, even, and anonymous. Every sentence is roughly the same length. It reports facts without reacting to them. It reaches for the most statistically likely phrasing, which is why so much of it sounds the same. It hedges, it pads, it announces what it is about to do, and it closes on vague optimism. None of it is wrong, exactly. It just doesn't sound like anyone.

Personal voice sounds like a particular human thinking. The rhythm is uneven on purpose: a short sentence, then a long one that wanders a little before it lands. There are opinions. There is the occasional aside or half-finished thought. The writer trusts the reader and uses plain words. You can tell a person is behind it because the writing takes positions a neutral summary wouldn't.

The whole job is to move text from the first kind to the second.

## Match the writer's voice when you can

If the user gives a writing sample (their own earlier writing, or a piece whose voice they want), read it before drafting and match it. Note these things in the sample:

- Sentence length and how much it varies
- Word-choice level: casual, plain, academic, technical
- How paragraphs open: straight into the point, or some setup first
- Punctuation habits: dashes, parenthetical asides, semicolons, sentence fragments
- Recurring phrases or verbal tics
- How transitions work: explicit connectors, or just moving to the next thing

Then match those patterns, not just the absence of AI tells. If they write short sentences, don't produce long ones. If they say "stuff" and "things," don't upgrade to "elements" and "components." If no sample is given, fall back to the default natural voice described under Personality and soul.

A sample can come inline ("rewrite this in my voice, here's how I write: ...") or as a file ("match the style in this file"). When voice matters a lot and no sample exists, it is fine to ask the user for one.

## The six tells that recur most

If you do nothing else, hunt these six. They are the loudest signals that a model produced a piece, and they show up far more than the rest. The first three are contrast and closer tics; the next three are structural habits.

**The X-not-Y construction.** A declarative sentence followed by a contrasting negation. "Good writing is a habit, not a talent." Once it can land. Three times in a piece it is a tic, and the contrast is doing the work that conviction should. Variants: "It's not just X, it's Y," "Not X. Y," "It's not about X. It's about Y," and tailing negations like "no guessing" tacked onto the end. Fix: say what the thing is and let the reader register the contrast. If the contrast matters, give the opposing case its own developed sentence.

**The contrast-flip couplet.** Two consecutive short sentences where the second negates or inverts the first, both ending flat. "The tool works. The team doesn't use it." "The data is there. Nobody reads it." Reading three in a row is the single strongest tell. Fix: combine into one sentence with a conjunction, or develop the second sentence so it does more than negate the first, or cut the second entirely.

**The rhetorical wrap-up.** A short declarative that claims to settle the argument, paired with a clause that demotes everything else. "That's the whole game. The rest is execution." "That picture is the plan. Everything else is detail." It mimics a mic drop with no speaker behind it, and it usually substitutes for actually finishing the argument. Fix: cut the line (the paragraph above probably made the point), or replace it with a real transition, or make it specific by naming the actual thing it waves at.

**Journey and travel metaphor stacks.** Journey, arc, path, voyage, embark, navigate, and landscape applied to things that do not move. "The product has a journey." "Across that arc." "The path forward." Once one travel word lands, related ones pile up. Fix: use the literal word — process, stages, sequence, pattern. If the sentence still works after the swap, the metaphor was not earning its keep. A single anchoring travel metaphor in a title or thesis can be fine; proliferation is the tell.

**Signposting and announcements.** "Let's dive in." "Here's what you need to know." "Let's break this down." "Without further ado." The model narrates its own outline instead of writing. Fix: do the thing. "Let's look at how caching works" becomes "Caching here happens at three layers."

**Rule of three.** Forcing ideas into triplets: "faster, better, cheaper," "speed, scale, security," three parallel bullets that could be two or four. The model defaults to three because it sounds comprehensive. Fix: count what is actually there and use that number.

**Scan next:** significance inflation (*stands as, testament, pivotal*), superficial `-ing` endings (*highlighting, underscoring, ensuring*), fragmented headers (heading followed by a one-line restatement), and AI vocabulary clusters (*delve, tapestry, robust, leverage* when three or more appear close together).

The full catalog of every other tell (promotional language, vague attributions, false ranges, copula avoidance, persuasive authority tropes, filler phrases, hedging, generic positive conclusions, conjunctive-adverb crutches, em dashes, inline-header lists, title case, emojis, curly quotes, temporal inflation openers, balanced both-sides pivots, and more) lives in `references/ai-tells.md`. Read that file when drafting or auditing anything substantial.

## Personality and soul

Removing tells is only half the job. Clean but voiceless prose still reads as AI. Signs of soulless writing: every sentence the same length, no opinions, no acknowledged complexity, no first person where it fits, reads like a press release.

How to put a pulse in it:

- Have opinions and react to facts instead of just listing them. "I still don't know how to feel about this" is more human than a balanced pro-con list.
- Vary rhythm hard. Short hits next to longer sentences that take their time getting where they're going.
- Acknowledge real complexity. "This is useful and a little unsettling" beats "this is useful."
- Use "I" when it fits. First person is honest, not unprofessional.
- Let some mess in. A tangent, an aside, a half-formed thought. Perfect structure feels algorithmic.
- Be specific about feelings and details instead of reaching for an abstraction.

## Optional house style

A user or repo may layer constraints on top of the natural voice. When the user states any of these, treat them as binding for the task and apply them throughout:

- Em dash policy. Em dash overuse is itself an AI tell (see the catalog), so the default already reduces them. If the user wants none at all, replace every one with a comma, parentheses, or a new sentence, and use hyphens only inside genuinely hyphenated words.
- Banned words or phrases. Keep the user's list and strip every instance.
- Formatting limits. For example, no bold, no headers, plain prose only, or a length cap.
- Point of view, tense, or audience constraints.

If the user gives no house style, use the defaults in this skill and the catalog.

## Writing a new piece

1. Get the angle straight first. What does the writer actually think about this, and why is it worth saying? Lead from that, not from a definition.
2. Match the sample voice if one was given; otherwise use the natural voice above.
3. Draft with plain verbs, varied rhythm, and real opinions. Don't decorate.
4. Run the audit below before calling it done.

## Editing or auditing a draft

1. Read it once for content and meaning.
2. Read it again hunting the top six: X-not-Y, contrast-flip couplets, rhetorical wrap-ups, journey/travel metaphor stacks, signposting, and rule of three.
3. Scan headings for title case and for warm-up lines that just restate the heading.
4. Scan paragraphs for significance inflation, superficial `-ing` endings, and clusters of inflated AI vocabulary (three or more watch-words close together).
5. Rewrite each problem in place. Preserve meaning, and preserve the writer's voice if a sample was given.

## The final pass: read it aloud

If you can't read a paragraph aloud without hearing the cadence of a model, it still reads as AI. After the draft, run this audit explicitly:

1. Ask: "What would make this so obviously AI-generated?"
2. Answer honestly with the specific remaining tells, naming them with the vocabulary from the catalog.
3. Revise to fix them.
4. Present the final version.

## Output format

For a rewrite or audit, provide the draft rewrite, a short honest answer to "what still reads as AI here," and the final version after fixing those. A brief bullet summary of changes is optional when it helps. For fresh writing, provide the finished piece, having already run the aloud pass internally.

## Reference files

- `references/ai-tells.md`: the full catalog of AI writing patterns with before-and-after examples for each. Read it for any substantial draft or audit.

## External sources

These are worth consulting when updating the catalog or when a piece needs deeper pattern-matching than the skill alone provides. Treat them as descriptive field guides, not proof of AI authorship. No single word or pattern is definitive; clusters of weak signals matter more than any one hit. Automated detectors (GPTZero, Turnitin, etc.) are unreliable on their own — Wikipedia's guide explicitly warns against relying on them.

| Source | What it contributes |
|--------|---------------------|
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Primary catalog. Maintained by WikiProject AI Cleanup from thousands of flagged submissions. Covers content inflation, formatting tics, negative parallelisms, AI vocabulary, and more. |
| [WikiProject AI Cleanup / Guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide) | Operational cleanup guide: how to spot AI content, fix sourcing problems, and handle tagged articles. |
| [GPTZero AI Vocabulary](https://gptzero.me/news/most-common-ai-vocabulary/) | Statistical word-frequency list updated from millions of human vs. AI comparisons. Good for lexical tells (*delve, showcasing, today's fast-paced world*). |
| [Pangram Labs: Spotting AI Writing Patterns](https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns) | Practical guide on rhythm (low burstiness), em dashes, organized paragraphs, and "Overall"/"In conclusion" closers. |
| [Google Cloud: Statistical tells (Weinmeister)](https://medium.com/google-cloud/detecting-ai-generated-text-by-uncovering-its-statistical-tells-042c8d0e3a24) | Data-driven analysis of signposting (*here's, let's, break down*), authoritative qualifiers (*crucial, comprehensive*), and sycophantic openers (*great question*). |
| [VU Amsterdam ALP Guide](https://vu.nl/en/about-vu/more-about/alp-guide-spotting-ai-writing) | Academic framing: boosters vs. hedges, bland/robotic style, overly poetic language (*rich tapestry*), low perplexity. |
| [ACL 2025: LLM Fingerprints (Sarvazyan et al.)](https://aclanthology.org/2025.genaidetect-1.6/) | Research showing models leave persistent lexical and syntactic fingerprints across domains. Supports treating structural patterns as more durable tells than individual words. |
