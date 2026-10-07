---
name: personal-voice
description: |
  Write and edit prose so it reads like a specific person wrote it, not an AI
  agent. Use when drafting or rewriting anything humans will read (posts,
  essays, emails, READMEs, docs, reports), and as a pre-publish pass to strip
  the patterns that make text read as generated.
  Matches a person's voice from a writing sample. Strips em and en dashes by
  default. Runs in detect mode (flag the tells) or edit mode (rewrite in
  place). Reports an ai-smell score from 0 to 100 for how machine-generated the
  writing reads, a reader-value score from 0 to 100 for substance, concision,
  calibration, and reader path, an adversarial review that argues against the
  piece as its toughest readers would, and a human-touch list of the places
  where only the writer can add the number, name, moment, or opinion that gives
  it flair. Built on Wikipedia's "Signs of AI writing" and published detection
  research. Triggers: "make this sound human," "this reads like AI," "rewrite
  in my voice," "is this AI slop," or any request for natural writing.
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

Write and edit so the result reads like a person, not an agent. This skill does three jobs: it drafts new writing in a natural personal voice, it audits existing drafts to remove the patterns that flag text as AI-generated, and it checks whether the writing is concise, calibrated, and worth a reader's time, which is a separate question from whether it sounds human. Before anything ships, it also argues against the piece the way its toughest readers would. It is built on the humanizer skill, which draws its pattern catalog from Wikipedia's "Signs of AI writing" (maintained by WikiProject AI Cleanup), with additional patterns observed in long-form drafting and borrowed from the no-ai-slop and deslop projects.

## Personal voice versus agent voice

Agent prose is fluent, even, and anonymous. Every sentence is roughly the same length. It reports facts without reacting to them. It reaches for the most statistically likely phrasing, which is why so much of it sounds the same. It hedges, it pads, it announces what it is about to do, and it closes on vague optimism. None of it is wrong, exactly. It just doesn't sound like anyone.

Personal voice sounds like a particular human thinking. The rhythm is uneven on purpose: a short sentence, then a long one that wanders a little before it lands. There are opinions. There is the occasional aside or half-finished thought. The writer trusts the reader and uses plain words. You can tell a person is behind it because the writing takes positions a neutral summary wouldn't.

The whole job is to move text from the first kind to the second.

## Default punctuation: no em or en dashes

This skill does not use em dashes (—) or en dashes (–) in the writing it produces or edits. That is a default feature, not an optional house style.

One honest caveat, since the research moved: the em dash is no longer good evidence that a model wrote something. The Economist's 2026 comparison of 1.2 million words against four frontier models found only Claude uses em dashes more than human writers do. Keep stripping them, because the dash stack still reads like sales copy and the rewrite is almost always clearer, but treat it as a style preference rather than a detection signal, and do not raise an ai-smell score on dash count alone.

**When drafting.** Do not reach for an em or en dash as a connector, aside, or punch. Use a comma, a period and a new sentence, or parentheses instead.

**When auditing.** Find every em dash and en dash in the draft and rewrite each one. Common swaps:

- Aside or interruption: parentheses, or split into two sentences.
- Contrast or pivot: comma, semicolon, or a conjunction (*but*, *and*, *so*).
- Appositive: commas.
- Date or number ranges: *from 1990 to 2000*, *pages 12 to 15*, or a hyphen only when the style guide treats it as a compound modifier.

Keep hyphens only inside genuinely hyphenated words (*well-known*, *long-term*).

**Voice-sample exception.** If the user's sample clearly and consistently uses em dashes as a personal habit, match that habit sparingly. Still strip en dashes unless the sample uses them for ranges and the user wants them preserved. When in doubt, remove dashes.

**User override.** If the user explicitly asks to keep dashes, follow their instruction for that task.

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

**A sample is also a measuring stick.** Once you have one, you can count instead of guessing: compare how often each word appears in the draft against how often it appears in the sample, each side as a rate rather than a raw count, and read the top of the list. Words far above the writer's own baseline are the draft's borrowed vocabulary. Words the writer uses constantly come back near 1x, which is correct, because those are voice rather than tells. This is the same formula the published vocabulary studies use, and it is the only way to catch tells that are not yet on anyone's list. `references/ai-tells.md` has the formula, the floors, and a snippet under "Term-frequency analysis."

## The six tells that recur most

If you do nothing else, hunt these six. They are the loudest signals that a model produced a piece, and they show up far more than the rest. The first three are contrast and closer tics; the next three are structural habits.

**The X-not-Y construction.** A declarative sentence followed by a contrasting negation. "Good writing is a habit, not a talent." Once it can land. Three times in a piece it is a tic, and the contrast is doing the work that conviction should. Variants: "It's not just X, it's Y," "Not X. Y," "It's not about X. It's about Y," the "it was never X, it is Y" reveal that ends on an abstraction ("the cost was never the tool, it is the space between them"), and tailing negations like "no guessing" tacked onto the end. Fix: say what the thing is and let the reader register the contrast. If the contrast matters, give the opposing case its own developed sentence.

**The contrast-flip couplet.** Two consecutive short sentences where the second negates or inverts the first, both ending flat. "The tool works. The team doesn't use it." "The data is there. Nobody reads it." Reading three in a row is the single strongest tell. Fix: combine into one sentence with a conjunction, or develop the second sentence so it does more than negate the first, or cut the second entirely.

**The rhetorical wrap-up.** A short declarative that claims to settle the argument, paired with a clause that demotes everything else. "That's the whole game. The rest is execution." "That picture is the plan. Everything else is detail." It mimics a mic drop with no speaker behind it, and it usually substitutes for actually finishing the argument. Fix: cut the line (the paragraph above probably made the point), or replace it with a real transition, or make it specific by naming the actual thing it waves at. A related move is the circular bookend, closing a passage by restating its opening in new words (see the catalog).

**Dead metaphor stacks.** Three clusters, one tell. *Travel*: journey, arc, path, voyage, embark, navigate, landscape applied to things that do not move ("the product has a journey," "across that arc," "the path forward"). *Structural*: load-bearing, doing a lot of work, heavy lifting, foundation, cornerstone, scaffolding, pillars, spine, backbone, the thread between, connective tissue, the seams, the glue, plus the mechanical cousins (levers, dials, move the needle, plumbing, rails, under the hood, surface area). *Doors*: opens the door to, closes the door on, unlocks, paves the way, gateway, on-ramp, floodgates. *Disguise*: the same thing wearing different clothes, wearing the costume of, dressed up as, X in Y's clothing, cloaked in, a thin veneer of. Once one of these lands, related ones pile up in the same paragraph. The structural ones claim something matters without naming what depends on it; the door ones are a hedge, since "opens the door to faster releases" is what you write when you won't commit to saying releases get faster. Fix: name the mechanism or the consequence. "That assumption is load-bearing" becomes "if that assumption is wrong, the pricing model and the hiring plan both change." "That opens the door to faster releases" becomes "once that lands, releases go out weekly instead of monthly." "The thread between the two teams" becomes "both teams depend on the same schema and neither owns it." If the sentence reads fine with the literal statement swapped in, the metaphor was decoration. A single anchoring image in a title or thesis can be fine; proliferation is the tell. The disguise cluster has its own failure mode: it asserts that two things are secretly the same without ever saying what they share, so "the same problem wearing different clothes" becomes "all six fail because nobody wrote the context down." Entries 16, 48, 49, and 66 in the catalog.

**Signposting and announcements.** "Let's dive in." "Here's what you need to know." "Let's break this down." "Without further ado." The model narrates its own outline instead of writing. Fix: do the thing. "Let's look at how caching works" becomes "Caching here happens at three layers."

**Rule of three.** Forcing ideas into triplets: "faster, better, cheaper," "speed, scale, security," three parallel bullets that could be two or four. The model defaults to three because it sounds comprehensive. Fix: count what is actually there and use that number. A related move is the one-move-solves-all convergence: list N problems, then claim a single thing answers all N ("three pressures, and consolidation is the one move that answers all three"). See the catalog.

**Scan next:** significance inflation (*stands as, testament, pivotal*), superficial `-ing` endings (*highlighting, underscoring, ensuring*), fragmented headers (heading followed by a one-line restatement), colon reveals (*the best part: it learns*), faux-insight openers (*here's the thing, what nobody tells you*), rhetorical question setups including question-shaped headings (*So what does this mean?*), imperative closers (*start there, pick one and run it this quarter*), the shift framing repeated section after section (*the bottleneck has moved from X to Y*), the manufactured through-line (*the through-line, if you want one*, followed by an abstraction), adverb tics (*just, really, actually, simply, genuinely, quietly, arguably*), consultant-deck vocabulary (*table stakes, moat, flywheel, north star, step change*), snowclones and named-law drops (*X is the new Y, a feature not a bug, Goodhart, Chesterton's fence*), and AI vocabulary clusters.

**The 2026 agent register, which is the one a delve-hunt misses.** Every word in it is a good plain word, so a draft can be scrubbed clean of the ChatGPT-era vocabulary and still be written entirely in this. Four moves: *physical nouns doing abstract work* (load-bearing, seam, ladder, spine, ceiling, floor, rail, plate, halves), *objects given intentions* (the check fires, the config sits, the flag carries, the test refuses, the job decides, the rule owns), *adverbs that certify* (quietly, deliberately, precisely, identically, structurally, unconditionally, verbatim, honestly, genuinely), and *absolute negation* (nothing, never, nobody, neither, alone, untouched, unaffected, forever). It is measured rather than observed: in 47,464 GitHub pull request descriptions sampled daily since January 2025, this way of writing went from about 1% of the corpus to 44.6% of the four weeks ending August 2026, and *load-bearing* is its top word at 123 times the rate it appears outside it. Catalog entry 67 has the full lists, the fixes, and the caveats. The fix is entry 48's fix widened: swap the literal statement in, and if the sentence survives, the metaphor and the certifying adverb were decoration.

**Then the substance tells,** which are newer in the catalog and which a tell-hunt on its own will miss: zombie nouns and noun-stacked abstraction (*the implementation of the optimization of*), the restatement loop (a point made, explained, then made again), certainty inflation and stripped attribution (*may cause* becoming *causes*, *researchers suggest* becoming *research shows*), hyperbole and absolutes (*completely transforms, the single biggest, nobody is talking about this*), vague expressions of connection (*associated with, in connection with, when it comes to*), and assertion chains with no connective logic. Entries 58 to 63.

**And the newest, each from a measured study:** reflexive validation and answering a false premise as asked (entry 68), stock names like Sarah and Emily (69), quotes that sound like the narrator (70), purple prose and stock imagery (71), the grammatical fingerprint of participial clauses and nominalizations (72), and model-family openers and formatting such as "Certainly" and "Below is" (73). Before scoring anything, read "When the tells mislead" in the catalog: plain prose from second-language writers is not a tell, and text a model only edited will not show the full catalog.

**Grep list.** Each of these is almost always decoration, so search for them literally on every pass: *opens the door*, *closes the door*, *unlocks*, *paves the way*, *gateway*, *on-ramp*, *floodgates*, *threshold*, *load-bearing*, *doing a lot of work*, *heavy lifting*, *foundation*, *foundational*, *cornerstone*, *bedrock*, *scaffolding*, *pillars*, *building blocks*, *spine*, *backbone*, *connective tissue*, *the thread between*, *the thread running through*, *the seams*, *the fabric of*, *the glue*, *the plumbing*, *the wiring*, *the space between*, *levers*, *dials*, *move the needle*, *on rails*, *under the hood*, *surface area*, *table stakes*, *flywheel*, *north star*, *single pane of glass*, *step change*, *quietly*, *no longer just*, *is the new*, *the through-line*, *the thread running through*, *wearing different clothes*, *wearing the costume of*, *dressed up as*, *cloaked in*, *a thin veneer of*. Add the agent-register set when the piece is technical: *load-bearing*, *seam*, *survived*, *untouched*, *byte-identical*, *genuinely*, *deliberately*, *precisely*, *identically*, *unconditionally*, *verbatim*, and any inanimate subject followed by *refuses*, *decides*, *asks*, *owns*, *wants*, or *says*.

**Hyperbole and absolutes grep.** These are claims that cannot be checked, so they carry no information: *completely*, *entirely*, *everything changes*, *nothing is*, *nobody*, *no one is talking about*, *always*, *never*, *the single biggest*, *the most important*, *revolutionary*, *game-changing*, *transformative*, *unprecedented*, *exponentially*, *orders of magnitude*, *fundamentally changes*, *redefines*, *must-have*. Keep one only where it is literally true and you have checked.

**Calibration grep, run against the source and not the draft.** *research shows*, *studies show*, *it is clear that*, *obviously*, *undoubtedly*, *proves*, *confirms*, *causes*, *drives*, *guarantees*. Each one needs a named source, and each needs to still carry whatever hedge the source used. Also grep for the connection-hedges that name no relationship: *associated with*, *linked to*, *tied to*, *in connection with*, *in the context of*, *when it comes to*, *in terms of*.

**Provenance grep, run before publishing anything a model touched.** `utm_source=`, `oaicite`, `contentReference`, `cite:`, `【`, `[insert`, `[Your`. These are residue from the generating tool, not style. One hit means the text was pasted out of a chat window without a read-through, and it outweighs any stylistic judgment. Report it separately and keep it out of the score. Catalog entry 57.

**A note on em dashes.** The default here is still to strip them, but that is a style choice rather than a detection claim. The Economist's 2026 study of 1.2 million words found em dashes no longer separate human from AI writing, since only Claude overuses them. So do not raise a score on dash count.

**What the punctuation research does support, since this is the part people get wrong.** Three findings are worth carrying, and none of them is about a single mark.

*Variety beats counts.* AI text draws on a narrower set of marks, with commas and periods doing almost all the work, and uses fewer question marks, semicolons, parentheses, and colons than human writing. The Economist found the same thinning and traced part of it to models not quoting anyone, because quotation is what pulls attribution punctuation into a sentence.

*Variance beats mean.* Sentence-length *spread* is consistently lower in model output, while studies disagree entirely on whether models write longer sentences or shorter ones. So never score a draft on sentence length itself. Measure the gap between the longest and shortest sentence in each paragraph. Words between punctuation marks is a second rhythm worth checking, and any unpunctuated run past about 25 words reads as machine-made even when the grammar is fine.

*Uniform correctness is its own tell.* Punctuation that stays textbook-perfect at a constant temperature, with no contractions and no informal register anywhere, reads as machine-made even when every mark is right. Entry 64 covers it, and the first rule there is that you never fake an error to fix it. Contract where speech would contract, put a real aside in parentheses, let one sentence be a fragment.

All of this is one signal inside a capped dimension and never a verdict about authorship. Punctuation heuristics have a bad track record, the em dash being the most recent casualty, and the cost of getting them wrong falls on writers who punctuate carefully.

The full catalog of every other tell (promotional language, vague attributions, false ranges, copula avoidance, persuasive authority tropes, filler phrases, hedging, generic positive conclusions, conjunctive-adverb crutches, inline-header lists, title case, emojis, curly quotes, temporal inflation openers, balanced both-sides pivots, over-explained anecdotes, document-structure artifacts, zombie nouns, restatement loops, certainty inflation, hyperbole and absolutes, and more) lives in `references/ai-tells.md`, along with fifteen mechanical counts under "Counting instead of guessing" and the term-frequency method for finding tells that are on no list yet. Read that file when drafting or auditing anything substantial. Several entries carry controlled exceptions, which matter as much as the rules: consultant vocabulary that is a real term of art in your field, one named law whose mechanism you actually work through, a single anchoring metaphor, and the shift framing used once as a thesis. The tell is repetition and decoration, not the move itself.

## Personality and soul

Removing tells is only half the job. Clean but voiceless prose still reads as AI. Signs of soulless writing: every sentence the same length, no opinions, no acknowledged complexity, no first person where it fits, reads like a press release.

How to put a pulse in it:

- Have opinions and react to facts instead of just listing them. "I still don't know how to feel about this" is more human than a balanced pro-con list.
- Vary rhythm hard. Short hits next to longer sentences that take their time getting where they're going.
- Acknowledge real complexity. "This is useful and a little unsettling" beats "this is useful."
- Use "I" when it fits. First person is honest, not unprofessional.
- Let some mess in. A tangent, an aside, a half-formed thought. Perfect structure feels algorithmic.
- Be specific about feelings and details instead of reaching for an abstraction.

Most of that list needs material only the writer has, which is why the human-touch list exists (see "Where a person should add flair"). When you cannot supply the pulse yourself, name the place it belongs and ask for it.

## Concision, calibration, and substance

Removing tells raises the surface quality of a draft, and surface quality was never the problem. "Why Slop Matters" (arXiv 2601.06060) characterizes slop by superficial competence: the veneer of quality hides the absence of substance. A tell-free, perfectly readable page that gives the reader nothing they can use is still slop. So every pass runs these three checks alongside the tell hunt.

**The cut test, for concision.** Delete every sentence that repeats a point already made, then read the paragraph. Padding is the most reliably removable defect in model prose, and it is trained in rather than inherent: reward models and LLM judges both prefer longer answers, and YapBench found newer frontier models pad more than GPT-3.5-Turbo did. Look for the restatement loop (state it, explain it, state it again), zombie nouns that inflate a clause by a third (*the implementation of the optimization of*), throat-clearing before the point, and sections that all came out the same length regardless of how much there was to say. If more than about 15% of the draft goes without loss, it was padded, and say so.

**The claim test, for substance.** Underline every number, date, proper noun, quoted person, and named mechanism. A paragraph with none of them is decoration, however well it reads. Journalism's version of this is show, don't tell; the failure mode described in the Reuters Institute's survey of AI prose is "a lot of words that don't say anything." Two checkable specifics per 100 words is a reasonable floor for anything that makes claims about the world. Under one and the passage is pure abstraction. The fix is almost always to replace a category with an instance: one customer instead of "teams," one incident instead of "reliability challenges," 40ms instead of "latency issues."

**The calibration test, for hyperbole and false certainty.** Check each claim against the evidence behind it, in both directions.

- **Overstated.** Absolutes and superlatives cannot be checked, so they carry no information. Bao et al. measured the drift toward this in 823,798 arXiv abstracts after ChatGPT: more positive sentiment and a rise in *exceptional*, *pivotal*, *notable*, *seamless*. Downgrade the claim until you can defend it, then attach the evidence that lets you. "Completely transforms how teams work" becomes "two of the four teams stopped holding standups."
- **Falsely certain.** This is the one to watch during a rewrite, because rewriting is where it happens. Belem et al. (2026) found language models shift the certainty of text they rewrite in up to 75% of cases, biased 1.5 to 2 times toward more confidence, and it compounds over repeated passes. Hedges vanish, attributions vanish, sample sizes vanish, and the sentence gets tighter and more quotable while becoming less true. Tightening prose is exactly the operation that strips these, so check the edited version against the source rather than against your previous draft.
- **Over-hedged.** The opposite failure is real too, and it is the older one. "It could potentially be argued that results may vary" commits to nothing. One hedge at most, and only where the uncertainty is real.

Fourteen mechanical counts are in `references/ai-tells.md` under "Counting instead of guessing." Run at least these:

| Count | Look harder when |
|-------|------------------|
| Checkable specifics per 100 words | Fewer than 2 |
| Cut-test loss | More than 15% of the draft goes without loss |
| Zombie nouns (`-tion`, `-ment`, `-ance`, `-ity`, `-ness`) per 100 words | More than 4, or 2 in one sentence |
| Longest minus shortest sentence, per paragraph | Under 8 words of spread (spread, not average) |
| Distinct punctuation types per 500 words, and the longest unpunctuated run | Three or fewer types, or any run past about 25 words |
| Contractions per 100 words in conversational prose, and people quoted by name | Zero of either |
| Boosters against hedges | Boosters win in a piece making empirical claims |
| Claims about the world against named sources | More claims than sources |

One trap: lexical density is not the target. Bao et al. found post-ChatGPT abstracts scored higher on content words per total words while getting *harder* to read, because the connective words went missing. Cramming in content words is how you get an unreadable paragraph. What you want is more checkable specifics, fewer wasted words, and the *because* and *so* that carry the argument left in place.

## Where a person should add flair

The checks above have a ceiling, and it is the ceiling of what the model knows. Past that point, the only way to make a piece more compelling is for the writer to put something of their own in it. So every pass ends with a **human-touch list**: two to five specific places where the writer, and nobody else, can raise the value of the piece.

Include it in every pass, including the ones where the draft came back clean. It is usually the part that most changes the finished piece.

What to look for:

- **A number the writer has and the draft doesn't.** Latency, headcount, dollars, dates, how many times it happened.
- **A named person or a real quote.** The Economist's 2026 analysis found absent quotation is one of the stronger current markers of machine prose, and it is often the fastest single fix available.
- **A first-hand moment.** The meeting where it went wrong, the bug that ate a week, what the writer believed at the time and turned out to be wrong about.
- **An opinion with a cost.** Wherever the draft lays out a tradeoff without saying which side the writer comes down on, and why.
- **The objection with no good answer.** What the sharpest skeptic in the room would say, left standing on purpose.
- **The thing still unresolved.** Model prose ties everything off. Real accounts leave something open.
- **A concrete example in place of a category.** One customer, one file, one incident, instead of "organizations."
- **A joke, an aside, a piece of slang, a strong opinion about something adjacent.** The stuff that could only have come from this person.

How to write the list, which matters as much as what is on it:

- **Point at a location.** Name the paragraph or quote the line, so the writer knows where to put it.
- **Ask a question they can answer in one sentence.** "Which two teams dropped standups?" beats "consider adding specific examples." A question gets answered; an instruction gets skipped.
- **Say what it would buy.** "This is the only paragraph with no evidence in it" or "this is where a reader decides whether to trust the piece."
- **Rank by payoff and stop at five.** A list of fifteen suggestions gets none of them done.
- **Never invent the material yourself.** Do not fill the gap with a plausible-sounding number, quote, or anecdote. Leave the hole and mark it. Inventing it is the exact failure the calibration test exists to catch.

If the piece is functional writing where voice does not matter, keep the list to missing facts and skip the rest.

## Optional house style

A user or repo may layer constraints on top of the natural voice. When the user states any of these, treat them as binding for the task and apply them throughout:

- Dash policy override. The default is no em or en dashes (see above). If the user wants dashes allowed or banned even more strictly, follow that for the task.
- Banned words or phrases. Keep the user's list and strip every instance.
- Formatting limits. For example, no bold, no headers, plain prose only, or a length cap.
- Point of view, tense, or audience constraints.

If the user gives no house style, use the defaults in this skill and the catalog.

## Two modes: detect or edit

Decide which the user wants before touching the text.

**Detect.** The user asks "is this AI slop?", "does this read like AI?", or "what tells are in here?" They want a diagnosis, not a rewrite. Name each tell using the catalog's vocabulary, quote the exact line it appears in, and give a one-line fix. Do not rewrite the piece. Order the findings by how loud they are (top six first). If the text is clean of tells but thin on substance, say that too; it is the more useful finding and it is the one a tell hunt tends to miss.

**Edit.** The user asks you to rewrite, clean up, or humanize. Follow the editing workflow below and return the revised text. Both modes end with the human-touch list, because in detect mode it is often the only thing the user can act on and in edit mode it is the part you could not do for them.

When it is ambiguous, ask, or lead with a short detect pass and offer to do the edit.

## How hard to edit

Match the size of your changes to whose voice the text carries and how much voice the piece needs.

- **The user's own draft.** Make the minimum effective edits. Fix the tells and leave the rest of their words, cadence, and structure alone. The edit should feel invisible: the writer should read the result and recognize it as theirs, only cleaner. Do not upgrade their vocabulary, even out their rhythm, or add flourishes. Over-polishing a person's draft is its own kind of slop.
- **A voiceless AI draft the user will publish as their own.** Edit freely. Strip the tells and add the personality described under Personality and soul.
- **Functional writing where voice barely matters** (a form, a compliance doc, a status update). Removing tells is the whole job; you do not need to inject personality. Be direct and be done.

## Writing a new piece

1. Get the angle straight first. What does the writer actually think about this, and why is it worth saying? Lead from that, not from a definition.
2. Match the sample voice if one was given; otherwise use the natural voice above.
3. Draft with plain verbs, varied rhythm, and real opinions. Do not use em or en dashes.
4. Run the audit below before calling it done, including the cut, claim, and calibration tests.
5. List the places where you had to write around something you do not know. Those are the human-touch items, and they belong in the output.

## Editing or auditing a draft

1. Read it once for content and meaning.
2. Read it again hunting the top six: X-not-Y, contrast-flip couplets, rhetorical wrap-ups, dead metaphor stacks (travel, structural, doors), signposting, and rule of three.
3. Scan headings for title case, for warm-up lines that just restate the heading, and for questions the section immediately answers.
4. Scan paragraphs for significance inflation, superficial `-ing` endings, colon reveals ("the best part: ..."), faux-insight openers ("here's the thing," "what nobody tells you"), adverb tics (just, really, actually, simply, genuinely, quietly), dead metaphors (doors, load-bearing, threads, levers), consultant vocabulary (table stakes, moat, flywheel, step change), snowclones and named-law drops, and clusters of inflated AI vocabulary (three or more watch-words close together).
5. Check the ending. Cut imperative closers ("start there," "pick one and run it this quarter"); the paragraph above almost always ends the piece better.
6. Check the shift framing. Once as a thesis is fine and is worth keeping; the same "moved from X to Y" construction in every section with fresh noun pairs is the tell.
7. Check punctuation in three directions. Remove every em dash and en dash, rewriting with commas, parentheses, conjunctions, or new sentences. Then look for sparseness and narrow variety, which the research says matters more: long "and" chains, unpunctuated runs past about 25 words, almost no semicolons, colons, question marks, or parentheses, and nobody quoted by name. Then check register: contractions where speech would contract, an aside in real parentheses, a fragment where the emphasis earns it. Measure sentence-length spread per paragraph and ignore the average.
8. If the draft carries an anecdote or case study, check that it does not state its own moral and that the genuinely hard part of the decision survived.
9. Run the provenance grep (`utm_source=`, `oaicite`, `contentReference`, `cite:`, `【`, `[insert`) and confirm every link, quotation, and citation resolves. Fix template residue: skipped heading levels, decorative `---` rules, tables holding what should be a sentence, markdown pasted where it will not render.
10. Run the cut test. Delete every sentence that repeats a point already made, cut throat-clearing, and unpack zombie nouns into verbs. Note how much of the draft went; more than about 15% means it was padded.
11. Run the claim test. Underline the numbers, dates, names, quotes, and mechanisms. Flag any paragraph that has none, and replace categories with instances where you can.
12. Run the calibration test. Check absolutes and superlatives against what has actually been verified, and check hedges and attributions against the source rather than against the previous draft. Rewriting is where certainty gets inflated, so this check comes after the rewrite, not before it.
13. Rewrite each problem in place, making the smallest change that fixes the tell (see How hard to edit). Preserve meaning, and preserve the writer's voice if a sample was given or the draft is already theirs.
14. Re-audit after any rewrite. Tidy triplets (rule of three), circular bookends, imperative closers, and dropped hedges are the things most likely to creep back in when a sentence gets edited.
15. Run the adversarial review (see "The adversarial review"). Apply the fixes and concessions, then re-audit the changed sentences.
16. Write the human-touch list. Two to five places where only the writer can add the number, name, moment, or opinion the piece needs, each phrased as a question they can answer in a sentence. Objections the review marked "needs the writer" come first.

## The ai-smell score

The judge pass produces a number: an ai-smell score from 0 to 100, where 0 reads fully human and 100 reads obviously machine-generated. Lower is better. It is a structured self-assessment of how the writing reads, not a detector verdict and not proof of authorship. Its main value is relative: comparing a draft before and after a pass, and forcing the judge to point at specific tells instead of waving at "feels AI."

Score five dimensions, each capped as shown, then sum them. The caps weight the loudest signals highest.

| Dimension | Cap | What it measures | Maps to |
|-----------|-----|------------------|---------|
| Structural tics | 30 | X-not-Y, contrast-flip couplets, rhetorical wrap-ups, dead metaphor stacks (travel, structural, doors), signposting, rule of three, colon reveals, faux-insight openers, false-depth reveals, one-move-solves-all, circular bookends, restatement loops, rhetorical question setups, imperative closers, the repeated shift framing, the manufactured through-line, disguise metaphors, over-explained anecdotes | Top six plus entries 41 to 46, 48 to 50, 53, 55, 59, 65, 66 |
| Rhythm and punctuation | 20 | Sentence-length *spread* and paragraph shape. Uniform, metronomic cadence scores high; average sentence length is not scored, because studies disagree on whether models write long or short and agree that they vary less. Also the punctuation profile: narrow mark variety (a page of only periods and commas), long unpunctuated runs, nobody quoted, no contractions in a conversational register, and punctuation so uniformly textbook that no register shows. Assertion chains with no connective logic belong here too | Entries 35, 54, 63, 64 |
| Voice and stance | 20 | Opinions, first person where it fits, landing a position, acknowledged complexity. Neutral press-release tone scores high. Refusing to land a position is the most directly measured item in this rubric: Abdulhai et al. (2026) found essays from heavy LLM users about 70% more likely to stay neutral on the question they were answering, so score neutrality hard rather than treating it as taste. Reflexive validation and accepting a false premise (entry 68) and quotes that sound like the narrator (entry 70) belong here too | Entries 35, 37, 21, 68, 70 |
| Lexical tells | 20 | AI-vocabulary clusters, and there are now three sets to check, not one: the delve-era set, the 2026 plain-word set (quietly, shift, matters, land, real, earn, compound, signal), and the agent register of entry 67 (physical nouns for abstractions, objects given intentions, certifying adverbs, absolute negation). A draft written entirely in the third one will look clean against the first two, so check it explicitly before scoring this dimension low. Also significance inflation, promotional language, hyperbole and absolutes, adverb tics, consultant-deck vocabulary, snowclones and named-law drops, copula avoidance, zombie nouns, superficial `-ing`, filler, vague attributions, vague expressions of connection, stock names, purple prose, and the grammatical fingerprint (participial clauses, nominalizations, few agentless passives) | Entries 4, 6 to 11, 18, 19, 47, 51, 52, 58, 61, 62, 67, 69, 71, 72 |
| Formatting artifacts | 10 | Boldface overuse, inline-header lists, title case, emojis, curly quotes, takeaway boxes, skipped heading levels, decorative rules, tables doing a sentence's job, unrendered markdown, leftover placeholder text, model-family openers ("Certainly," "Below is") and markdown that is the same whatever the content | Entries 24 to 28, 40, 56, 73 |

Rough anchors within a dimension: 0 means none of its tells appear; roughly a third of the cap means one or two isolated instances; roughly two-thirds means a recurring habit; the cap means the writing is built on that category.

Certainty inflation and stripped attribution (entry 60) deliberately sit outside this rubric. They are defects in how the claim relates to its evidence rather than in how the prose reads, so they are scored in the reader-value rubric below, under calibration.

**Provenance flag, reported outside the score.** Entry 57 artifacts (`utm_source=chatgpt.com`, `oaicite`, `contentReference`, `[cite: 1]`, `【 】`, placeholder text, citations that do not resolve) are evidence about how the text was made, not how it reads. Do not fold them into any dimension. Report them as a separate line above the score, because one of them tells the reader more than the whole rubric does.

**What moved and why, for anyone comparing to older scores.** Dimension two used to be rhythm alone and is now rhythm and punctuation, because the em dash stopped being diagnostic in 2026 while punctuation sparseness became a stronger signal. Em/en dashes moved out of Formatting artifacts and into that dimension, where they are weighed as one signal among several rather than a fingerprint. The caps and the five-dimension shape are unchanged, so before-and-after deltas still mean the same thing. Everything added in the substance revision (concision, calibration, and specificity) went into the separate reader-value score below rather than into these five dimensions, for the same reason: an ai-smell number that keeps changing shape is a number nobody can compare.

Scoring rules, so the number stays honest:

- **Reason first, then score.** Do the "what makes this AI" pass and cite instances before you assign any number. Scoring after explicit reasoning tracks human judgment far better than a snap holistic rating; this is the core finding behind G-Eval and rubric-based LLM judges (see the research note in the catalog).
- **Cite or it doesn't count.** Every point added to a dimension must point at an actual instance, quoted or named with catalog vocabulary. A score with no evidence is invalid; when in doubt, score lower.
- **Score as a skeptic, not the author.** LLM judges reliably under-rate tells written in their own style (self-preference bias) and reward length and surface fluency (verbosity bias). You will be partly blind to your own tics. Counter it: hunt harder than feels necessary, and never add or subtract points for length or polish alone.
- **Run the count before you score the lexical dimension.** If a baseline exists (the writer's earlier work, the team's docs, the repo's older commits), compute the term-frequency ratio described in the catalog and read the top of the list. It finds tells no list contains, and it stops the lexical score from being a grep against a dated vocabulary.
- **Plain is not AI.** Short sentences, limited vocabulary, and textbook grammar from a second-language writer are not tells. GPT detectors flagged about 61% of TOEFL essays as AI on average (Liang et al. 2023), because constrained phrasing reads as low-perplexity. Score rhythm and lexical choices against the writer, not against a native-speaker norm.
- **A low score is not a clean bill.** Text a model edited, rather than wrote, keeps most of its human stylometry (Shan et al. 2026). The score says how the prose reads and nothing more.
- **A word-frequency hit is never an authorship finding.** The AI vocabulary is leaking into ordinary speech: Yakura et al. tracked it across 824,634 podcast episodes and found the words rising in spontaneous human conversation after ChatGPT shipped. A writer using one of these words is now an ordinary event. Score the cluster and the density, never the individual word, and keep this dimension capped.
- **Be consistent run to run** so before/after deltas mean something.
- **Voice and stance is not applicable to functional writing** (a form, a compliance doc, a status update). For those, drop that dimension, score out of 80, and say so. A bland voice is not a defect when voice was never the point.

Bands:

- **0 to 15, clean.** Reads human. Ship it.
- **16 to 35, faint.** Mostly clean; a few tells linger. One more targeted pass is worth it.
- **36 to 60, noticeable.** Reads as AI in places. Needs real revision.
- **61 to 100, strong.** Obviously machine-generated. Rework.

## The reader-value score

The ai-smell score answers one question: does this read like a machine wrote it? It cannot answer the question a reader actually cares about, which is whether the piece was worth opening. Those come apart in both directions. A tell-free page can be empty, and a page with three em dashes and a rule of three in it can be the most useful thing someone reads that week. So every pass reports a second number.

**Reader-value score, 0 to 100, higher is better.** Score four dimensions, each capped as shown, then sum them. Every point you move has to point at an instance, the same rule the ai-smell score uses.

Substance and reader path earn up from zero, because a draft has neither until someone puts them in. Concision and calibration start at the cap and lose points, because they measure the absence of a defect rather than the presence of a virtue. A short, accurate, well-attributed draft with nothing in it scores 50 and deserves to.

| Dimension | Cap | What earns points |
|-----------|-----|-------------------|
| Substance | 35 | Checkable specifics: numbers, dates, named people and products, quoted sources, named mechanisms, concrete examples in place of categories. Full marks means every claim-making paragraph has something a reader could verify or reuse. Zero means the piece is entirely abstraction, however fluent |
| Concision | 30 | The share of words carrying weight. Deduct for restatement loops, padding, zombie nouns, throat-clearing, and sections padded to uniform length. Measure it with the cut test rather than by feel: what percentage of the draft could go without loss? |
| Calibration | 20 | Claims sized to their evidence. Full marks means the hedges that belong are present, the attributions survived, the numbers carry their sample size, and no absolute appears that has not been checked. Deduct for certainty inflation, stripped attribution, hyperbole, unfalsifiable claims, and for over-hedging in the other direction |
| Reader path | 15 | Order that serves a reader: leads with the point instead of a definition, one idea per paragraph, headings that state answers, connectives that carry the argument, no scaffolding that exists only because the format expected it |

Rough anchors within a dimension: zero means the dimension is absent; a third of the cap means one or two spots do this well; two-thirds means it holds through most of the piece; the cap means the whole piece is built that way.

Bands:

- **76 to 100, rich.** A reader gets something they can use. Publish.
- **56 to 75, solid.** Real content, some thin patches. Worth one targeted pass on the weakest dimension.
- **31 to 55, serviceable.** True but generic. Someone who already knew the topic learns nothing.
- **0 to 30, thin.** No substance yet. Removing more tells will not fix this; only the writer can.

Scoring rules:

- **Do not reward polish.** LLM judges reward length and surface fluency, and this rubric is the one where that bias does the most damage. A smooth paragraph with no verifiable content scores zero on substance.
- **Cite the specifics you counted.** "Substance 24/35, five numbers and two named customers in the middle sections, nothing checkable in the opening or the close" is a usable score. A bare number is not.
- **Never raise the score by inventing.** If a claim needs a number you do not have, that is a human-touch item, and the score stays where it is. Filling the gap with a plausible figure is the failure the calibration test exists to catch.
- **Report the ceiling.** When the score is capped by information only the writer holds, say so: "substance is capped near 20 until someone supplies the actual latency numbers." That sentence is what makes the human-touch list feel worth answering.
- **Mark the span, then score.** Shaib et al. (2025) built their slop measure from span-level annotation and found the judgments correlate with coherence and relevance rather than with polish, which is both independent support for scoring reader-value separately and a note on procedure: point at the passage first, assign the number second.
- **Both numbers, always.** A draft can land at ai-smell 8 and reader-value 22, which is a clean, well-behaved page that says nothing. Reporting only the first number would call that a success.

The two scores also change what to do next. High ai-smell with high reader-value means the content is there and needs an editing pass. Low ai-smell with low reader-value means editing is finished and the piece needs the writer.

## The adversarial review

The tell hunt asks whether the writing sounds like a person. The two scores ask how it reads and whether there is anything in it. Neither one asks the question the toughest reader will ask: is this true, and why should I believe you? So every substantial pass also argues against the piece, the way its hardest readers would, before it ships. Gary Klein's premortem works the same way: assume the piece has already failed with its audience, and work out why.

**1. Name the hostile readers.** Pick two or three people who would actually read this piece and have a reason to push back, specific to its audience. Generic personas ("a critic") find generic objections. Useful defaults:

- **The expert in the room.** Knows the subject better than the writer and will check every number, command, and causal claim.
- **The skeptic of motive.** Assumes the piece is selling something (a product, a promotion, the writer's own judgment) and reads every claim of value as a pitch.
- **The reader in a hurry.** Gives the piece thirty seconds and needs to know what to do with it. If it cannot answer that, it failed them regardless of quality.

Swap in the real ones when you know them: the security reviewer for a design doc, the customer's engineer for a sales README, the referee for a paper.

**2. Steelman each objection.** For each reader, write the strongest objection they would raise, quoting the exact line it attacks. Make it as strong as you honestly can. An objection you can knock down in one sentence was a strawman, and finding strawmen is how this pass turns into flattery. Look for:

- **Unsupported claims.** A statement of value or fact with nothing behind it.
- **Overclaims.** A claim bigger than its evidence, including results generalized past their sample.
- **Missing costs.** A recommendation with no downside named, when the reader knows there is one.
- **Motive.** A passage that reads as promotion, especially where the writer benefits from the conclusion.
- **Omissions.** The alternative, failure mode, or prior work an informed reader expects and does not see.
- **Internal contradictions.** Two parts of the piece that cannot both be true, including numbers that do not add up.
- **No "so what."** A section the reader finishes without knowing what to do differently.

**3. Triage every objection into one of four outcomes.**

| Outcome | When | What to do |
|---|---|---|
| **Fix** | The text is wrong, overstated, or unclear, and you can fix it with what is already known | Reword, qualify, cut, or reorder. Smallest change that answers it |
| **Concede** | The objection is right and the piece should say so | Add the limitation, cost, or caveat in plain words, once, where it applies |
| **Needs the writer** | Answering it takes evidence only the writer has | Move it to the human-touch list as a question. Do not invent the answer |
| **Stand** | The objection is wrong | Say why in one line, so the writer can disagree with you |

**Rules, so the review stays honest:**

- **Five objections at most, strongest first.** A long list of weak objections hides the two that matter.
- **Never answer an objection with invented evidence.** That is the same failure the calibration test exists to catch, wearing a different reason.
- **Do not hedge your way out.** Answering every objection with "may" and "in some cases" trades an overclaim for a piece that commits to nothing. Concede specifically, or fix the claim.
- **Check the fixes.** Concessions and qualifiers are where new tells creep in: tidy triplets, "while X, Y" pivots, and balanced both-sides paragraphs. Re-run the tell hunt on every sentence you changed.
- **Score after the review.** Unaddressed objections are calibration and substance findings, so they show up in the reader-value score, not just in the list.
- **Functional writing gets a short review.** A status update or a form needs the expert and the hurried reader, not the skeptic of motive.

## The final pass: read it aloud and score

If you can't read a paragraph aloud without hearing the cadence of a model, it still reads as AI. After the draft, run this pass explicitly:

1. Ask: "What would make this so obviously AI-generated?" Answer honestly with the specific remaining tells, naming them with the vocabulary from the catalog.
2. Ask the second question: "if a reader knew this topic already, what would they get from this?" Answer with what is actually checkable in the draft, not with what it covers.
3. Run the adversarial review: name the hostile readers, steelman up to five objections, and triage each into fix, concede, needs the writer, or stand.
4. Score the draft on both rubrics above, citing evidence per dimension.
5. Revise to fix the tells, heaviest dimensions first, then to cut, then to calibrate, then to apply every fix and concession from the review.
6. Re-score the revised version on both rubrics, and re-check the sentences the review changed for new tells.
7. Write the human-touch list: the two to five places where only the writer can raise the value, each as a question they can answer in a sentence. Objections marked "needs the writer" go here first.
8. Present the final version, both scores, the adversarial review, and the human-touch list.

## Output format

Every mode reports both scores, the adversarial review, and the human-touch list. Report each score as a headline number plus the per-dimension breakdown with cited evidence, so neither one is a black box:

```
AI-smell: 12/100 (faint)          lower is better
  Structural tics   4/30  one X-not-Y in paragraph 2
  Rhythm and punct  4/20  middle section runs even
  Voice and stance  2/20  lands a clear position
  Lexical tells     2/20  "leverage" once
  Formatting        0/10  clean

Reader-value: 58/100 (solid)      higher is better
  Substance   18/35  3 numbers and 2 named customers, all in section 2;
                     nothing checkable in the intro or the close
  Concision   22/30  cut test dropped 11%, mostly restatement in section 3
  Calibration 12/20  "completely transforms" unsupported; the 40-user
                     sample lost its size in the rewrite
  Reader path  6/15  opens on a definition, two headings are questions

Adversarial review (strongest first):
  1. Expert: "40% faster" (section 2) has no baseline or sample.
     -> Needs the writer: what was it measured against, and on how many runs?
  2. Skeptic of motive: the close is a pitch for the tool with no cost named.
     -> Conceded: added the migration cost and who should not switch.
  3. Reader in a hurry: nothing says what to do first.
     -> Fixed: moved the setup command to the top.
  4. Expert: "no one else does this" is false; two projects already do.
     -> Fixed: cut the claim.

Human touch (5 min of your time, biggest payoff first):
  1. Section 2: which two teams stopped holding standups?
  2. Intro: the whole opening is abstract. What happened the day you
     decided this mattered?
  3. Section 4: you describe the tradeoff but never say which side you
     take. Which one, and what does it cost?
  4. Close: what is still broken about this?
```

When provenance artifacts turn up, they go above the scores on their own line, not inside them:

```
Provenance: 2 artifacts. "utm_source=chatgpt.com" on the Stripe link;
            placeholder "[insert customer name]" in paragraph 6.
AI-smell: 12/100 (faint)
  ...
```

In **detect** mode, lead with both scores, then provide the findings: each tell named with catalog vocabulary, the quoted line, and a one-line fix, loudest first. Then the adversarial review, with each objection's proposed outcome but nothing applied. Then the human-touch list. No rewrite.

In **edit** mode, provide the draft rewrite, a short honest answer to "what still reads as AI here, and what is still thin," the adversarial review with what you did about each objection, and the final version after fixing those. Report both scores as a before to after delta ("AI-smell 58 to 12, reader-value 31 to 58"). Say plainly when the reader-value number is capped by things you cannot supply. A brief bullet summary of changes is optional when it helps; when you edited the user's own draft, that summary doubles as a "what changed" list so they can see every touch.

Keep the human-touch list short and ranked. Five items is the ceiling, and the first one should be the one that would improve the piece most.

For fresh writing, provide the finished piece and its final score, having already run the read-aloud and scoring pass internally.

## Reference files

- `references/ai-tells.md`: the full catalog of AI writing patterns with before-and-after examples for each, the mechanical counts, the term-frequency method, a short section on writing in languages other than English, the human-touch list, and the research notes behind both scores. Read it for any substantial draft or audit.

## External sources

These are worth consulting when updating the catalog or when a piece needs deeper pattern-matching than the skill alone provides. Treat them as descriptive field guides, not proof of AI authorship. No single word or pattern is definitive; clusters of weak signals matter more than any one hit. Automated detectors (GPTZero, Turnitin, etc.) are unreliable on their own; Wikipedia's guide explicitly warns against relying on them.

| Source | What it contributes |
|--------|---------------------|
| [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) | Primary catalog. Maintained by WikiProject AI Cleanup from thousands of flagged submissions. Covers content inflation, formatting tics, negative parallelisms, AI vocabulary, and more. |
| [WikiProject AI Cleanup / Guide](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide) | Operational cleanup guide: how to spot AI content, fix sourcing problems, and handle tagged articles. |
| [no-ai-slop (Peter Yang)](https://github.com/petergyang/no-ai-slop) | The detect-vs-edit split, the minimum-effective-edit principle, and specific tells: colon reveals, throat-clearing openers, banned intensifiers. |
| [deslop (Stephen Turner)](https://blog.stephenturner.us/p/deslop) | Dramatic-pause directives ("let that sink in"), a scoring-rubric approach, and calibrating edit aggressiveness to how voice-critical the piece is. |
| [G-Eval (Liu et al. 2023)](https://arxiv.org/abs/2303.16634) | Rubric-based LLM-as-a-judge. Grounds the ai-smell score's reason-first, score-per-dimension design. |
| [Self-Preference Bias in LLM Judges (Wataoka et al. 2024)](https://arxiv.org/abs/2410.21819) | Judges under-rate tells in their own style. Grounds the "score as a skeptic" rule. |
| [Excess vocabulary (Kobak et al. 2024)](https://arxiv.org/abs/2406.07016) | Measured LLM word overuse across 14M abstracts. Empirical backbone for the lexical dimension. `references/ai-tells.md` has the fuller research note. |
| [GPTZero AI Vocabulary](https://gptzero.me/news/most-common-ai-vocabulary/) | Statistical word-frequency list updated from millions of human vs. AI comparisons. Good for lexical tells (*delve, showcasing, today's fast-paced world*). |
| [Pangram Labs: Spotting AI Writing Patterns](https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns) | Practical guide on rhythm (low burstiness), em dashes, organized paragraphs, and "Overall"/"In conclusion" closers. |
| [Google Cloud: Statistical tells (Weinmeister)](https://medium.com/google-cloud/detecting-ai-generated-text-by-uncovering-its-statistical-tells-042c8d0e3a24) | Data-driven analysis of signposting (*here's, let's, break down*), authoritative qualifiers (*crucial, comprehensive*), and sycophantic openers (*great question*). |
| [VU Amsterdam ALP Guide](https://vu.nl/en/about-vu/more-about/alp-guide-spotting-ai-writing) | Academic framing: boosters vs. hedges, bland/robotic style, overly poetic language (*rich tapestry*), low perplexity. |
| [ACL 2025: LLM Fingerprints (Sarvazyan et al.)](https://aclanthology.org/2025.genaidetect-1.6/) | Research showing models leave persistent lexical and syntactic fingerprints across domains. Supports treating structural patterns as more durable tells than individual words. |
| [The Economist on spotting AI writing (2026)](https://www.fastcompany.com/91584243/how-to-identify-ai-generated-writing-viral-report-has-surprising-new-clues-economist) | 55,940 sentences and 1.2M words against four frontier models. Em dashes are no longer diagnostic; punctuation sparseness, longer sentences, "and" overuse, and absent quotation are. Basis for the rhythm-and-punctuation dimension. |
| [Forbes: 15 new giveaway signs (May 2026)](https://www.forbes.com/sites/jodiecook/2026/05/21/15-new-giveaway-signs-of-ai-writing-may-2026-update/) | The post-delve vocabulary: *quietly, shift, matters, shape, land, real, earn, the work, hold, pull, compound, signal, built different*. Plain words used abstractly, which is why they are harder to spot. |
| [StoryScope (Russell et al. 2026)](https://arxiv.org/abs/2604.03136) | 61,608 stories scored on narrative rather than stylistic features; 93.2% human/AI separation. AI over-explains its themes and favors tidy single-track plots. Basis for the over-explained-anecdote tell. |
| [Linguistic Characteristics of AI-Generated Text (Terčon & Dobrovoljc 2025)](https://arxiv.org/abs/2510.05136) | Survey of the measurement literature. AI prose is more nominal and impersonal: more nouns, determiners, and prepositions, fewer adjectives and adverbs, lower lexical diversity. Basis for the zombie-noun tell. |
| [Linguistic shifts after ChatGPT (Bao et al. 2025)](https://arxiv.org/abs/2505.12218) | 823,798 arXiv abstracts. More positive sentiment, more hyperbolic adjectives, simpler syntax, fewer connectives, lower readability despite higher lexical density. Basis for the hyperbole and assertion-chain tells. |
| [From "May" to "Is" (Belem et al. 2026)](https://arxiv.org/abs/2606.07951) | Rewriting distorts certainty in up to 75% of outputs, biased 1.5 to 2 times toward more confidence, compounding across passes. The reason calibration is checked against the source, not the previous draft. |
| [The load-bearing vocabulary of Claude (Louis Abraham, 2026)](https://louisabraham.github.io/load-bearing/) | 47,464 GitHub PR descriptions sampled daily since Jan 2025, clustered with no time parameter in the model. One way of writing grew from ~1% to 44.6% of the corpus; *load-bearing* is its top word at 123x. Basis for catalog entry 67 and for the term-frequency method. [Code and methodology](https://github.com/louisabraham/load-bearing), including the constants that were tuned on the answer. |
| [Quantifying LLM usage in scientific papers (Liang et al. 2025)](https://www.nature.com/articles/s41562-025-02273-8) | *Nature Human Behaviour*. 1,121,912 papers estimated for LLM-modified text from population-level word-frequency shifts: up to 22% in computer science. The method behind treating vocabulary as frequency rather than as a blacklist. |
| [LLM influence on human speech (Yakura et al. 2024)](https://arxiv.org/abs/2409.01754) | 824,634 podcast episodes, 737,083 hours. ChatGPT-preferred words rose in *spontaneous conversation* after release. Why a word-frequency hit is never an authorship finding. [Counterweight](https://arxiv.org/abs/2508.00238): a smaller unscripted-speech corpus finds the effect real but uneven. |
| [Measuring AI "Slop" in Text (Shaib et al. 2025)](https://arxiv.org/abs/2509.19163) | Taxonomy of slop from expert interviews, annotated at the span level. Judgments are partly subjective but track coherence and relevance rather than polish. Independent support for the reader-value score. |
| [How LLMs Distort Our Written Language (Abdulhai et al. 2026)](https://arxiv.org/abs/2603.18161) | Heavy LLM users' essays were ~70% more likely to stay neutral on the question; models changed meaning even under grammar-only instructions. Basis for the voice-and-stance dimension, and the warning that no rewrite is surface-only. |
| [People who frequently use ChatGPT are accurate detectors (Russell, Karpinska & Iyyer 2025)](https://arxiv.org/abs/2501.15654) | 300 articles; a majority of five heavy LLM users misclassified 1, beating most commercial detectors even on paraphrased text. Ranks the tells experts actually use (vocabulary ~53%, structure ~36%, too-clean grammar ~25%, unoriginality ~24%, quotes ~22%) and found stock names (Emily, Sarah) in most model articles. Basis for entries 69 and 70 and the clusters-not-single-tells rule. |
| [Can AI writing be salvaged? (Chakrabarty, Laban & Wu, CHI 2025)](https://arxiv.org/abs/2409.14509) | The LAMP corpus: 1,057 model paragraphs edited by professional writers on a seven-category taxonomy (awkward word choice ~28%, sentence structure ~20%, redundant exposition ~18%, cliché ~17%, purple prose ~10%, lack of specificity ~8%, tense ~3%). Basis for entry 71 and a ready-made creative-writing edit checklist. |
| [Do LLMs write like humans? (Reinhart, Brown et al., PNAS 2025)](https://arxiv.org/abs/2410.16107) | Parallel human and model texts on 66 Biber features. Instruction-tuned models overuse present participial clauses (2 to 5x), nominalizations (1.5 to 2.1x), "that"-subject clauses, and phrasal coordination, and underuse agentless passives; the gap does not shrink with scale. Basis for entry 72. |
| [ELEPHANT: social sycophancy in LLMs (Cheng, Jurafsky et al. 2025)](https://arxiv.org/abs/2505.13995) | 10,395 prompts across 11 models. Emotional validation ~76% vs 22% for humans, indirect language ~87% vs 20%, accepting the user's framing ~90% vs 60%. Basis for entry 68. |
| [Idiosyncrasies in Large Language Models (Sun, Yin, Xu, Kolter & Liu, ICML 2025)](https://arxiv.org/abs/2502.12150) | Five model families told apart at ~97%. Per-family openers and phrases ("Certainly," "Below is," "based on") and markdown habits; formatting alone identified the model ~73% of the time. Basis for entry 73. |
| [Monitoring AI-modified content: conference peer reviews (Liang, Zou et al., ICML 2024)](https://arxiv.org/abs/2403.07183) | Corpus-level estimate that 6.5% to 16.9% of AI-conference reviews were substantially LLM-modified; spikes in *commendable*, *meticulous*, *intricate*. The peer-review register, added to entry 10. |
| [GPT detectors are biased against non-native English writers (Liang et al., Patterns 2023)](https://arxiv.org/abs/2304.02819) | 91 TOEFL essays, seven detectors, ~61% average false-positive rate. The guardrail behind "plain is not AI." |
| [AI writers have a consistent stylometric footprint, but AI editors do not (Shan, Lee & Hao 2026)](https://arxiv.org/abs/2608.27855) | Eight models, five domains. Generated text has a stable footprint; human text a model edited barely shifts. Why a low score is not a clean bill. Preprint. |
| [Why does ChatGPT "delve" so much? (Juzek & Ward, COLING 2025)](https://arxiv.org/abs/2412.11385) and [the RLHF follow-up (2025)](https://arxiv.org/abs/2508.01930) | Neither architecture nor training data explains the overused words; human preference in feedback training does. Why fixed vocabulary lists age and the term-frequency method does not. |
| [AI use in American newspapers (Russell, Iyyer et al., ACL 2026)](https://arxiv.org/abs/2510.18774) | 186,000 articles from 1,500 US papers; about 9% partly or fully AI, rarely disclosed. Detector-based, with Pangram co-authors, so weigh the numbers accordingly. In flagged copy, check facts as well as style. |
| [AI suggestions homogenize writing toward Western styles (Agarwal, Naaman & Vashistha, CHI 2025)](https://arxiv.org/abs/2409.11360) | 118 participants in India and the US. AI suggestions pulled Indian writers toward Western style. Why voice matching keeps regional idiom. |
| [An LLM-associated register shift in Korean journal abstracts (Lee 2026)](https://arxiv.org/abs/2609.07447) | 398,000 Korean abstracts, morphology-aware excess vocabulary. The first measured non-English register shift. Single-author preprint. |
| [awesome-slop](https://github.com/hwajongpark/awesome-slop) and [slop-gate](https://github.com/hwajongpark/slop-gate) | A current index of slop tools and research, and a CLI that flags about 40 English tells in CI with translationese rule packs for Korean, Russian, Chinese, Vietnamese, and Filipino. The only pointer here for non-English tells; small, one-author projects, so treat the lists as a starting point. |
| [Not Wrong, But Untrue (Hagar et al. 2025)](https://arxiv.org/abs/2509.25498) | Attribution stripping, overinterpretation, certainty inflation. The editing vocabulary for calibration. |
| [Why Slop Matters (2026)](https://arxiv.org/abs/2601.06060) | Slop as superficial competence, asymmetric effort, mass producibility. The argument for scoring substance separately and for the human-touch list. |
| [Antislop (2025)](https://arxiv.org/abs/2510.15061) and [Slop Score](https://eqbench.com/slop-score.html) | Overused patterns computed against human baselines, some appearing 1,000 times more often. Slop Score independently puts 25% of its weight on not-X-but-Y. Keeps the word lists honest. |
| [YapBench (2026)](https://arxiv.org/abs/2601.00624) | Scores responses against the shortest sufficient answer; newer frontier models pad more than GPT-3.5-Turbo. Verbosity is trained in, so it can be cut out. |
| [The Writer's Diet (Helen Sword)](https://writersdiet.com) | Be-verbs, zombie nouns, prepositions, ad-words, and waste words. Source of the mechanical counts. |
| [Reuters Institute on AI prose](https://reutersinstitute.politics.ox.ac.uk/news/how-ai-generated-prose-diverges-human-writing-and-why-it-matters) | Journalism's read on the same problem: broad sweeping statements, "a lot of words that don't say anything," show don't tell. |
| [Stylometric detection of AI text (Kumarage et al. 2023)](https://arxiv.org/abs/2303.03697) | Punctuation is one of three stylometric feature families in a working detector, and adding it improves state-of-the-art classifiers. |
| [Universal versus system-specific punctuation patterns (Stanisz, Kwapień & Drożdż)](https://arxiv.org/abs/2212.11182) | Gaps between punctuation marks, counted in words, follow a discrete Weibull distribution whose parameters separate languages and authors. The words-between-marks rhythm. |
| [Comparing LLM and human news text (2025)](https://arxiv.org/abs/2506.01407) | Humans use contractions, colloquialisms, and rarer constructions more often; model output reads as an averaged grammatical profile. |
| [Stop policing punctuation (AARE 2026)](https://blog.aare.edu.au/stop-policing-punctuation-now-why-ai-detection-needs-a-rethink/) | The case against punctuation heuristics, and why the cost of a false positive lands on careful writers. Why punctuation is never a verdict here. |
