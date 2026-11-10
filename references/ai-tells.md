# AI writing tells: the full catalog

This is the working catalog of patterns that flag prose as AI-generated. It merges the humanizer skill (drawn from Wikipedia's "Signs of AI writing," maintained by WikiProject AI Cleanup) with additional patterns observed in long-form drafting. Each entry has the pattern, why it reads as AI, and how to fix it. The list is a living artifact. If you find a new tell, add it.

The first six are the ones that show up most. Hunt them first. Entry 67 is the only one compiled from a frequency count rather than from observation; read it alongside entries 47, 48, and 11, which it measures. Entries 68 to 73 are grounded in measured studies, and entries 74 to 82 are the late-2026 set, measured on GPT-6, Claude Opus 5 and 5.5, and Gemini 3.1 after the em dash and the delve vocabulary faded. The section "When the tells mislead" after them is the guardrail every score needs.

## Hunt these first (top six)

1. **The X-not-Y construction**: contrast through negation
2. **The contrast-flip couplet**: two short sentences, second inverts the first
3. **The rhetorical wrap-up**: fake mic-drop closer
4. **Dead metaphor stacks**: travel (journey, arc, path), structural (load-bearing, foundation, thread, levers), doors (opens the door, unlocks, paves the way)
5. **Signposting and announcements**: "Let's dive in," "Here's what you need to know"
6. **Rule of three**: forced triplets

Scan next: significance inflation, superficial `-ing` endings, fragmented headers, structural and door metaphors (load-bearing, threads, opens the door), imperative closers, AI vocabulary clusters, and the 2026 agent register (entry 67): physical nouns for abstractions, objects given intentions, certifying adverbs, absolute negation, and since September 2026, narrated verdicts (*the check refused*, *the doc says*).

Then the late-2026 set, which is what current models do instead of the famous tells: corrective disclaimers (*does not establish*, *should be treated as X rather than Y*, entry 74), salience flags (*this matters*, *why X matters*, 75), costless trade-offs (*without sacrificing*, 76), synthesis openers (*together these*, *adds another layer*, *looking ahead*, 77), mannered prose and *earns its place* (78), revisions written as diffs (79), the default argument with interchangeable detail (80), one-line staccato paragraphs where the dash used to be (81), and performed pushback (*I'd gently push back*, 82). Entry 73 has a per-family table, because two thirds of current tells belong to one model family.

Then run the substance checks, which catch what a tell list cannot. Entries 58 to 63 cover them: padding and zombie nouns (concision), hyperbole and certainty inflation (calibration), and abstraction with nothing checkable in it (substance). A draft can be free of every tic above and still waste the reader's time.

Then grep for provenance artifacts (entry 57). Those are evidence about how the text was made rather than how it reads, and one hit outweighs every stylistic judgment on this list.

## Contents

1. The X-not-Y construction
2. The contrast-flip couplet
3. The rhetorical wrap-up
4. Significance inflation
5. Undue emphasis on notability and media coverage
6. Superficial -ing endings
7. Promotional and cultural-heritage language
8. Vague attributions and weasel words
9. Formulaic "challenges and future prospects" sections
10. Overused AI vocabulary
11. Copula avoidance
12. Negative parallelisms and tailing negations
13. Rule of three
14. Elegant variation (synonym cycling)
15. False ranges
16. Travel metaphors for non-travel concepts
17. Passive voice and subjectless fragments
18. Persuasive authority tropes
19. Filler phrases
20. Excessive hedging
21. Generic positive conclusions
22. Conjunctive adverbs as transition crutches
23. Em and en dashes
24. Overuse of boldface
25. Inline-header vertical lists
26. Title case in headings
27. Emojis as decoration
28. Curly quotation marks
29. Collaborative communication artifacts
30. Knowledge-cutoff disclaimers
31. Sycophantic openings
32. Signposting and announcements
33. Fragmented headers
34. Hyphenated-word-pair overuse
35. Voice and pacing
36. Temporal inflation openers
37. Balanced both-sides without a position
38. Definitional cold opens
39. Escalating adjective chains
40. Explicit takeaway boxes
41. Rhetorical question transitions
42. The "it was never X, it is Y" false-depth reveal
43. The one-move-solves-all convergence
44. The circular bookend
45. Colon reveals
46. Faux-insight and throat-clearing openers
47. Empty intensifiers and adverb tics
48. Load-bearing and structural metaphors
49. Door and unlock metaphors
50. Imperative closers
51. Consultant-deck vocabulary
52. Snowclones and named-law drops
53. The shift framing
54. The punctuation profile: sparseness, narrow variety, low variance
55. Over-explained theme and tidy resolution
56. Document-structure artifacts
57. Provenance artifacts and citation pathologies
58. Zombie nouns and noun-stacked abstraction
59. The restatement loop
60. Certainty inflation and stripped attribution
61. Hyperbole, absolutes, and unfalsifiable claims
62. Vague expressions of connection
63. Assertion chains with no connective logic
64. Textbook-perfect punctuation and missing contractions
65. The through-line
66. Clothing and costume analogies
67. The agent register
68. Reflexive validation and accepting the premise
69. Stock names and default characters
70. Quotes in the narrator's voice
71. Purple prose and stock imagery
72. The grammatical fingerprint
73. Model-family openers and formatting
74. Corrective framing and the "does not establish" disclaimer
75. Salience flags: "this matters"
76. Trade-offs without a cost
77. Synthesis and layering transitions
78. Mannered prose and the "earns its place" idiom
79. Changelog voice: writing the revision instead of the document
80. The default argument and interchangeable detail
81. Staccato line breaks: the dash's replacement
82. Performed pushback

---

## 1. The X-not-Y construction

*Top-six tell (#1).*

**Looks like.** A declarative sentence followed by a contrasting negation. "Good writing is a habit, not a talent." "It's not a checklist. It's a way of thinking."

**Why it reads as AI.** The pattern adds emphasis through opposition rather than substance. Once it lands. Three times in a piece it is a rhetorical tic. The contrast is doing the work of conviction.

**Variants.** "It's not just X, it's Y." "Not X. Y." "It's not about X. It's about Y." "Rather than X, Y" when X and Y aren't actually being weighed. Tailing negations: "The form fills itself in, no guessing." See also the "it was never X, it is Y" false-depth reveal (entry 42).

**The late-2026 shapes, measured.** The construction did not go away when the em dash did; it changed clothes by model family. In Graphite's 2026 study of 10,000 matched articles per model against a pre-ChatGPT human baseline, the frame "is not just a _ it is" ran at 153 times the human rate in Gemini 3.1 Pro, "less like a _ and more like" at 105 times in Claude Opus 5, "is more than a _ it" at 98 times in Opus 5.5, and "the _ is not simply" at 576 times in GPT-6 Astra. The "rather than" form is now the most common of all: it was the single most over-used bigram in both Opus 5.5 and Astra. Entry 74 covers its newest use, which corrects a claim where the older form dramatized one.

**Why it survives training.** Peng and colleagues (arXiv 2610.22249, 2026) annotated 307 uses of the Mandarin equivalent, 不是X而是Y, from five commercial models that use it 2.5 to 9.2 times as densely as human writers. Only 1.3% were wrong. 52.8% were correct but unnecessary, and the reward models they tested preferred the construction even over quality-matched alternatives. That is the useful test, and it works in English too: the question is never whether the sentence is grammatical, it is whether anything in the context needed the rejected alternative named. Boggia (arXiv 2607.21498, 2026, small samples) adds that the over-use is genre-bound: about twice the human rate in oratory and abstracts, and *below* the human rate in casual Q&A and narrative. Hunt it hardest in persuasive and summary prose.

**Fix.** Say what the thing is. Trust the reader to register the contrast. If the contrast is essential, give the opposing case its own sentence and develop it. Ask of each instance whether a reader was actually likely to believe the rejected alternative; if not, delete it.

## 2. The contrast-flip couplet

*Top-six tell (#2).*

**Looks like.** Two consecutive short sentences where the second negates or inverts the first. "The tool works. The team doesn't use it." "The data is there. Nobody reads it." "The plan is clean. The execution isn't."

**Why it reads as AI.** Same family as X-not-Y, distributed across two sentences. The rhythm gives it away: short setup, even shorter pivot, both ending flat. A punch without a punchline. Three in a row is the strongest single tell that a model produced the piece.

**Fix.** Combine into one sentence with a conjunction ("The tool works, but the team doesn't use it"). Or develop the second sentence so it does more than negate the first. Or cut the second sentence and let the first carry the point.

## 3. The rhetorical wrap-up

*Top-six tell (#3).*

**Looks like.** A short declarative that claims to settle the argument, paired with a minimizing clause that demotes everything else. "That's the whole game. The rest is execution." "That picture is the plan. Everything else is detail."

**Why it reads as AI.** It mimics a mic drop without a speaker behind it. The two-clause rhythm is identical every time. The minimizer ("execution," "detail," "plumbing," "sequencing") implies the writer has zoomed out to a level the reader hasn't earned. The line usually substitutes for finishing the argument.

**Variants.** "That's the thesis. Everything downstream follows." "That's the answer. The rest is just plumbing." "That's it" as a standalone wrap-up. A softer version is a punchy closer that claims a result without support. Related: the dramatic-pause directive that orders the reader to be impressed, "Let that sink in," "Read that again," "Pause on that for a second." Cut these; if the point is worth pausing on, the sentence itself should make the reader stop.

**Fix.** Cut the line; the paragraph above usually made the point. Or replace it with a real transition. Or make the gesture specific: if there is an actual sequence or set of steps, name it.

## 4. Significance inflation

**Looks like.** Words that puff up the importance of something arbitrary: stands as, serves as, is a testament to, marks a pivotal moment, plays a crucial role, underscores its significance, reflects broader, represents a shift, deeply rooted, evolving landscape, indelible mark, setting the stage for.

**Why it reads as AI.** The model adds significance because it can't evaluate importance. Real writers show importance through specifics or don't claim it.

**Fix.** Cut the puff and use a simple verb. "The Statistical Institute of Catalonia stands as a testament to regional autonomy" becomes "The Statistical Institute of Catalonia was established in 1989 to publish regional statistics independently from Spain's national office."

## 5. Undue emphasis on notability and media coverage

**Looks like.** "Her views have been cited in the New York Times, BBC, Financial Times, and the Hindu. She maintains an active social media presence with over 500,000 followers."

**Why it reads as AI.** The model hits the reader over the head with notability claims, often listing outlets without context.

**The 2026 form: identification by source.** Wikipedia's editors added a sibling in 2026: stilted sentences about what an official site, database, or registry *says* about the subject, in place of the fact itself. "The ministry's website identifies him as a retired officer." "She is listed in the national registry." "His professional profile lists him as founder." The focus moves from the subject to the characteristics of the sources, which is the same move as the outlet list in a quieter voice.

**Fix.** Replace the list with one specific, sourced instance. For the identification form, state the fact and cite the source: "He retired from the civil service in 2019." "In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods."

## 6. Superficial -ing endings

**Looks like.** Present participle phrases tacked on to add fake depth: highlighting, underscoring, emphasizing, ensuring, reflecting, symbolizing, contributing to, fostering, encompassing, showcasing.

**Why it reads as AI.** The model uses these to extend a sentence that should have ended. The clause sounds like analysis but adds nothing the reader didn't already have.

**Fix.** End the sentence. If the clause carries real information, make it its own sentence with a real verb.

## 7. Promotional and cultural-heritage language

**Looks like.** Vibrant, rich, profound, nestled, in the heart of, groundbreaking, renowned, breathtaking, must-visit, stunning, world-class, robust, seamless, holistic, unified, leverage, optimize, end-to-end, boasts a.

**Why it reads as AI.** The model can't hold a neutral tone on topics where it trained on marketing copy. The words add no information.

**Fix.** Replace with what the thing does. "Robust testing framework" becomes "a test suite that runs in CI on every commit." Most of these words can be cut.

## 8. Vague attributions and weasel words

**Looks like.** "Industry observers have noted," "experts argue," "some critics say," "reports indicate," "several sources confirm."

**Why it reads as AI.** The model attributes claims to vague authorities because it can't cite specifics.

**Fix.** Name the source with a year. "A 2024 Stanford study found that ..." If you can't cite, don't claim.

## 9. Formulaic "challenges and future prospects" sections

**Looks like.** "Despite its rapid growth, the town faces challenges typical of urban areas. Despite these challenges, it continues to thrive."

**Why it reads as AI.** Many model-generated pieces include a boilerplate "Challenges" or "Future Outlook" section that says nothing specific.

**Fix.** Replace with specific facts. "Traffic congestion increased after 2015 when three new office parks opened. The town began a drainage project in 2022 to address recurring floods."

## 10. Overused AI vocabulary

**Watch-words.** delve, navigate, intricate, tapestry, landscape (abstract), testament, pivotal, vibrant, garner, foster, underscore, showcase, robust, seamless, holistic, leverage, unleash, harness, elevate, journey (metaphorical), arc (metaphorical), realm, embark, dive into, additionally, crucial, key (adjective), interplay, valuable.

**The 2026 set.** The list above is the ChatGPT-era vocabulary that detectors and word-frequency studies caught first, so a lot of writing has already been scrubbed of it. A newer cluster has replaced it, drawn from Forbes's May 2026 roundup of AI giveaways: shift, matters ("this matters because"), shape (verb, "shapes how we think"), land ("the point lands"), real ("real value," "real impact"), earn ("earn the right to," "earn trust"), the work ("do the work"), hold ("hold space," "hold the line"), pull ("the pull of"), compound ("decisions compound"), signal (abstract noun), built different, quietly (entry 47). These are harder to see because they are plain English words, and that is the point: the tell is the density and the abstraction, not the rarity.

**The late-2026 sets, by family.** Graphite's 2026 study and its Opus 5.5 update measured the words each current model over-uses against a pre-ChatGPT human baseline. The family split is sharp, so check the set for whatever model is likely in play:

| Family | Over-used words and phrases, times the human rate |
|---|---|
| Claude Opus 5.5 | dependable (23x), clearer (14x), reinforces (14x), matters (13x), practical (11x), steady (11x), quietly (11x), thoughtful (9x), genuine (9x), meaningful (8x), modest, manageable, smoother, deliberate, disciplined, approachable; *together these* (56x), *often called* (58x), *a practical* (24x), *built around* (22x), *looking ahead* (24x) |
| GPT-6 Astra | broader (31x), manageable (34x), practical (26x), relying (22x), straightforward (18x), matters (18x), useful (17x), priorities (17x), everyday (12x); *that distinction* (594x), *matters because* (356x), *not automatically* (233x), *than relying* (170x), *not simply* (157x), *together these* (95x), *starting point* (30x) |
| Gemini 3.1 Pro | furthermore (26x), navigating (26x), profound (25x), immense (22x), massive (19x), incredibly (18x), deeply (18x), heavily (18x), highly (16x), ensures (15x), seamlessly (13x); *is incredibly* (35x), *a highly* (33x), *lies in* (27x), *furthermore the* (43x) |

Three things stand out. Claude and GPT have converged on a vocabulary of reassurance and practicality (*dependable, practical, steady, manageable, meaningful*), which is the plain-word set above taken one step further: words that rate something as sensible without saying what it does. Gemini has gone the other way, back toward intensifiers and formal connectives that the delve era made famous. And Wikipedia's 2026 era list for GPT-6 (*challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally*) overlaps this table heavily, though its own citation is a product review with no measurement behind it, so it corroborates the table without adding evidence of its own.

Graphite generated every article from one fixed prompt on web-article topics, so these rates describe articles, not chat replies or code review. They are also a snapshot: in the same study 55% to 72% of tells were unique to one version within a family. Treat the table as the current cut, and the term-frequency method below as the thing that will still work next quarter.

**Why it reads as AI.** Frequency. Each word in isolation is fine. A cluster of them in one piece is the giveaway. They co-occur. The vocabulary also rotates as models change and as writers learn to avoid the flagged words, so treat any watch-list as dated and check the current one.

**The contamination problem, which is the reason this entry can never be a verdict.** The words are leaking into people. Yakura et al. tracked ChatGPT-preferred vocabulary (*delve, showcase, boast, intricacies, meticulous*) through 737,083 hours of conversation across 824,634 podcast episodes and found an abrupt rise in *spontaneous human speech* after ChatGPT shipped, with a synthetic-control analysis tying the shift to the release. Anderson, Galpin, and Juzek ran a smaller unscripted-speech corpus (22.1 million words) and found the effect real but uneven, with *delve* itself not rising significantly. So the direction is established and the size is contested. In written science it is no longer contested at all: Holzwarth, González-Márquez and Kobak (arXiv 2608.10715, 2026) scored 1,194,287 PubMed Central full texts on 379 marker words and found that by December 2025, 89% of biomedical papers showed an excess of LLM vocabulary, with the gap between native and non-native English countries closing. When nine papers in ten carry the signal, its presence in one more tells you almost nothing. Either way, a writer who reaches for one of these words in 2026 may simply be a person who has been listening to other people. Score the cluster, never the word, and never let this dimension decide anything on its own.

**Fix.** Use the plain word. Delve becomes look at. Navigate becomes work through. Intricate becomes detailed. Underscore becomes show. Robust becomes reliable or thorough. Leverage becomes use.

**Peer-review register.** Liang, Zou and colleagues (ICML 2024) estimated 6.5% to 16.9% of AI-conference peer reviews were substantially LLM-modified, with spikes in *commendable*, *meticulous*, and *intricate*. Watch those three in reviews, feedback, and evaluations.

## 11. Copula avoidance

**Looks like.** Substituting elaborate verbs for is/are/has. "The gallery serves as the city's main exhibition space." "The report represents a summary of the findings." "The team boasts twelve engineers."

**Why it reads as AI.** The model has a learned aversion to plain copulas because they feel weak. They are the most honest verbs in English.

**Fix.** Use is, are, has. "The gallery is the city's main exhibition space." "The team has twelve engineers."

## 12. Negative parallelisms and tailing negations

**Looks like.** "Not only X but also Y." "It's not just about the beat; it's the atmosphere." Clipped tailing negations tacked onto a sentence: "The options come from the selected item, no guessing."

**Why it reads as AI.** Overused construction that signals emphasis without earning it. Closely related to entry 1.

**The 2026 stack: "No X. No Y. Just Z."** Practitioners on Reddit describe this as the form that replaced "that's not X" in late 2026, and it shows up in a widely shared list of exhausted formats (r/ChatGPT, 742 points): a run of negated fragments, one of them oddly specific, then a closing "Just" with more fragments. "No car. No TV. No smart fridge that texts her about expired yogurt. Just books. Tea. Quiet." The specific middle item is what makes it feel observed. Cut the stack to the one item that carries information, and say it in a sentence.

**Fix.** State the point plainly. "The heavy beat adds to the aggressive tone." For tailing negations, write the real clause: "The options come from the selected item without forcing the user to guess."

## 13. Rule of three

*Top-six tell (#6).*

**Looks like.** Forcing ideas into groups of three. "Faster, better, cheaper." "Speed, scale, security." "Bold, decisive, transformative leadership."

**Why it reads as AI.** The model defaults to three because it sounds comprehensive. Real arguments have whatever number of parts they have.

**Fix.** Count the actual components and use that number. If you have four, list four. If you have two, list two and stop.

## 14. Elegant variation (synonym cycling)

**Looks like.** "The protagonist faces challenges. The main character must overcome obstacles. The central figure triumphs. The hero returns home."

**Why it reads as AI.** Repetition-penalty behavior causes excessive synonym substitution for the same referent.

**Fix.** Pick one term and repeat it. "The protagonist faces many challenges but eventually triumphs and returns home."

## 15. False ranges

**Looks like.** "From X to Y" where X and Y aren't on a meaningful scale. "From startups to enterprises." "From the boardroom to the factory floor." "From design to deployment."

**Why it reads as AI.** Sounds comprehensive but defines no actual range. The endpoints are just two examples chosen to feel wide.

**Fix.** List the actual cases or specify what changes between the endpoints.

## 16. Travel metaphors for non-travel concepts

*Top-six tell (#4).*

**Looks like.** journey, arc, path, voyage, road, trail, embark, navigate used for abstract processes that don't move. "The product has a journey." "That arc holds." "The path forward." "The customer journey." "Navigating the complexities of."

**Why it reads as AI.** Decorative when not doing work. They make an ordinary process or sequence sound momentous. They compound: once a piece commits to one travel word, the related words pile up. Structural metaphors (entry 48) and door metaphors (entry 49) are the same tell in a different register, and the three clusters often appear in the same paragraph.

**Controlled exception.** A single anchoring travel metaphor can earn its place if it organizes a piece's structure (a title, a heading, a thesis sentence). Use it once or twice in those spots and don't let related travel words proliferate around it.

**Fix.** Use the literal word. Journey, arc, or path becomes process, sequence, stages, or pattern. "Across that arc" becomes "at every stage." If the sentence reads fine after the swap, the metaphor wasn't doing work.

## 17. Passive voice and subjectless fragments

**Looks like.** "No configuration file needed." "The results are preserved automatically."

**Why it reads as AI.** The model hides the actor or drops the subject.

**Fix.** Name the actor when active voice is clearer. "You do not need a configuration file. The system preserves the results automatically."

## 18. Persuasive authority tropes

**Looks like.** "The real question is." "At its core." "What really matters." "Fundamentally." "The deeper issue." "The heart of the matter."

**Why it reads as AI.** The phrase pretends to cut through noise to a deeper truth. The sentence that follows usually restates an ordinary point with extra ceremony.

**Fix.** Cut the phrase. The point that follows either stands on its own or didn't need to be made.

## 19. Filler phrases

**Before becomes after.** "In order to" becomes "to." "Due to the fact that" becomes "because." "At this point in time" becomes "now." "In the event that you need help" becomes "if you need help." "Has the ability to process" becomes "can process." "It is important to note that the data shows" becomes "the data shows."

**Why it reads as AI.** The model pads sentences because longer feels more substantive. It isn't.

## 20. Excessive hedging

**Looks like.** "It could potentially possibly be argued that this might have some effect."

**Why it reads as AI.** The model over-qualifies to avoid being wrong.

**It now runs both directions, by family.** Hedging is no longer a general AI trait. In Graphite's 2026 data, GPT-6 Astra uses *may* three times as often as GPT-4.1 and qualifies far more than Claude (*may provide* at 18x the Opus 5.5 rate, *not necessarily* at 17x), while Claude Opus 5.5 reaches for superlatives instead (*the most popular* at 45x the Astra rate, *perhaps the most* at 29x). And in 1.8 million engineering abstracts, Cokyasar (arXiv 2611.11174, 2026) found the post-assistant shift went the other way from the stereotype: hedges like *may* fell 13% and boosters like *clearly* rose 20%. So check for both failures. Stacked hedges are this entry; boosters with no evidence behind them are entries 60 and 61, and in current text they are the more common of the two.

**Fix.** Make the claim or cut the sentence. "The policy may affect outcomes" is enough. One hedge at most.

## 21. Generic positive conclusions

**Looks like.** "The future looks bright." "Exciting times lie ahead." "This represents a major step in the right direction."

**Why it reads as AI.** The model closes with vague optimism because closing is hard.

**Fix.** End with a fact, a number, or a concrete next step. "The company plans to open two more locations next year."

## 22. Conjunctive adverbs as transition crutches

**Looks like.** "However," "therefore," "additionally," "furthermore," "moreover," "thus," "consequently," "specifically," "importantly" used as openers, often where no real logical connection exists.

**Why it reads as AI.** The connective tissue does the work of pretending there's an argument.

**Mostly Gemini now.** Wikipedia lists isolated transition words as an *ineffective* indicator, and the 2026 measurement explains why: the habit has become family-specific. Graphite found Gemini 3.1 Pro uses *additionally* 1,139 times and *furthermore* infinitely more often than GPT-6 Astra (Astra never wrote it), and *furthermore the* at 43 times the human rate. Claude and GPT replaced these openers with synthesis phrases instead (entry 77). A *furthermore* in a 2026 draft is weak evidence on its own; three in a page is a Gemini habit.

**Fix.** Drop the adverb and let the sentence stand. If the connection is real, show it through substance rather than announcing it.

## 23. Em and en dashes

*Default skill behavior: remove all em dashes (—) and en dashes (–) from output.*

**Looks like.** Em dashes in place of commas, periods, or parentheses, used as a default punchy connector. En dashes for ranges (*1990–2000*, *pages 12–15*) or as a weaker stand-in for an em dash.

**Why it reads as AI.** The dash stack reads like punchy sales copy, and models misuse hyphens and en dashes inconsistently.

**Caveat: as a detection signal, this entry is now historical.** Wikipedia's editors moved em-dash overuse into their "Historical indicators" section in late 2026 with the range 2022 to September 2026, and the measurements agree.

- **Current models have mostly stopped.** In Graphite's 2026 study against a pre-ChatGPT human baseline, GPT-6 Astra used em dashes at about one-eighth the human rate and Gemini 3.1 Pro had nearly stopped. Claude Opus 5 was the holdout, at about the human rate, and Claude Opus 5.5 (released September 2026) cut it by 99%, from 2.92 to 0.015 per 1,000 words. An independent 80-post test by Arize found the same drop, 12.9 per 1,000 words for Opus 5 against two dashes in roughly 57,000 words for Opus 5.5.
- **Not every model, though.** Pangram's November 2026 analysis of 2,215 GPT-6.1 Sol answers found an em dash in 29.7% of them (1.32 per 1,000 words), against 0.1% for Claude Haiku 5.5. These days the mark is better at telling models apart than at telling them from people.
- **And people are picking it up.** A Reddit analytics developer's count of 163 million long posts and comments from 100 large subreddits found em dashes in 6.8% of long posts at the mid-2025 peak, down about 30% after the GPT-5 fix, then creeping back to about seven times the 2021 level in 2026, while comments never passed 1.5%. The same count found *quietly* up 3.7 times and *delve* back to its 2021 level. Czuma (arXiv 2608.05889, 2026, exploratory) counted 146,239 US congressional press releases: em-dash density roughly doubled in 2025, from about 0.11 to 0.217 per 1,000 characters, with three quarters of offices increasing their use.
- **In agent-written technical text it rose.** In the GitHub pull request corpus behind entry 67, the project's README (September 2026) puts the em dash at 0.2 appearances per 10,000 words at the start of the corpus against about 123 in mid 2026. Those weeks predate Opus 5.5.

What replaced it is the more useful signal. Wikipedia's editors note that models trained to suppress the dash did not switch to colons, semicolons, or parentheses; they switched to periods and commas, so overall variety dropped and the *absence* of any interrupting punctuation became its own tell. That is entry 54. So do not raise a score on dash count in either direction. This skill still strips em dashes by default, and that is a house-style choice about how the writing should read, not a detection claim.

**Fix.** Replace every em and en dash:

- Aside or interruption → parentheses, or a new sentence.
- Contrast or pivot → comma, semicolon, or conjunction.
- Range → *from X to Y*, or a hyphen only when it is a true compound modifier.
- Never leave a dash because it "sounds emphatic."

Keep hyphens only inside genuinely hyphenated words. The personal-voice skill applies this by default on every draft and audit unless the user overrides or a voice sample clearly depends on em dashes.

**Two entries to read alongside this one.** Entry 54 covers what the research does support about punctuation, which is thinner variety and lower variance rather than the count of any single mark. Entry 64 covers the opposite failure from this one: punctuation so uniformly correct that no register shows through, with no contractions anywhere. Strip dashes without doing either of those and the prose still reads as machine-made, only with commas.

## 24. Overuse of boldface

**Looks like.** "It blends **OKRs**, **KPIs**, and the **Business Model Canvas**."

**Why it reads as AI.** The model emphasizes phrases in bold mechanically.

**Fix.** Drop the bold. "It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas."

## 25. Inline-header vertical lists

**Looks like.** A list where every item starts with a bolded header and a colon. "**Speed:** The system is fast. **Reliability:** The system is reliable."

**Why it reads as AI.** The structure is mechanical. It signals a template the model filled in.

**Fix.** Write the list as prose, or keep bolded headers only when each entry needs a real heading and the sentence after it does real work, not restating the header.

## 26. Title case in headings

**Looks like.** "## Strategic Negotiations And Global Partnerships."

**Why it reads as AI.** The model capitalizes all main words. Human long-form prose usually uses sentence case.

**Fix.** Sentence case. "## Strategic negotiations and global partnerships."

## 27. Emojis as decoration

**Looks like.** Emojis decorating headings, bullets, or section breaks.

**Why it reads as AI.** A distinctive chatbot training artifact.

**Fix.** Cut them unless the piece's genre and the writer's own voice actually use them.

## 28. Curly quotation marks

**Looks like.** Smart quotes instead of straight quotes.

**Why it reads as AI.** ChatGPT in particular defaults to curly quotes, and in late 2026 the split is measured and sharp. Pangram's November 2026 analysis of 2,215 GPT-6.1 Sol answers found curly apostrophes in 73.9% of them and curly double quotes in 39.0%, against 0.0% and under 0.1% for Claude Haiku 5.5 and 9.1% and under 0.1% for Gemini 4 Argon. Sol also put an en dash in 11.4% of answers, against 0.4% for the other two. Straight apostrophes inside words ran the other way: 0.5% of Sol answers, 75.4% of Haiku's. Typography is now one of the few signals that points at a specific vendor, which is also why it is weak evidence about authorship: anyone who pasted through a word processor has curly quotes too.

**Fix.** Match whatever the target context uses. In plain-text and code contexts, use straight quotes throughout.

## 29. Collaborative communication artifacts

**Looks like.** "I hope this helps," "Of course," "Certainly," "Would you like me to," "here is a," "let me know."

**Why it reads as AI.** Chatbot correspondence pasted in as content.

**The 2026 closer: the binary question.** Chat replies now end by offering the reader a fork. "I'm curious about one thing: is this for A or for B? The answer could change everything." "Which direction would be most helpful?" "Say the word and I'll draft it." Pasted into a post, the habit becomes "curious what others think" at the bottom, which Reddit commenters now read as a tell in its own right.

**Fix.** Cut it and start with the answer. Cut the closing fork too; if the piece really depends on which case the reader is in, cover both cases or pick the likelier one and say so.

## 30. Knowledge-cutoff disclaimers

**Looks like.** "As of my last training update." "While specific details are limited based on available information." "Up to my knowledge cutoff."

**Why it reads as AI.** Model self-disclosures that don't belong in published content.

**The 2026 forms.** Cutoff statements are historical now; Wikipedia files them under 2022 to 2023. Their descendants are the source-availability hedge from retrieval-backed models ("not widely documented in public sources," "maintains a low profile") and, from mid-2026, the corrective disclaimer about how sources should be read ("should be treated as tradition rather than as evidence," "does not establish"). The second one has its own entry (74).

**Fix.** Find the fact and cite it, or don't make the claim.

## 31. Sycophantic openings

**Looks like.** "Great question!" "You're absolutely right." "What a thoughtful observation." "That's an excellent point."

**Why it reads as AI.** Conversational artifacts from chatbot training leaking into prose.

**Fix.** Cut. Start with the answer.

## 32. Signposting and announcements

*Top-six tell (#5).*

**Looks like.** "Let's dive into." "Let's explore." "Let's break this down." "Here's what you need to know." "Without further ado." "In this section, we will discuss."

**Why it reads as AI.** The model announces what it's about to do instead of doing it. The meta-commentary gives the piece a tutorial-script feel.

**The 2026 form is guide scaffolding.** "Let's dive in" has mostly gone; what replaced it announces the document instead of the next paragraph. Graphite's 2026 study grouped it as a theme for both Claude Opus 5.5 (*this guide explains*, *this guide walks you through*, *a practical guide*, *final thoughts*, *bottom line*) and Gemini 3.1 Pro (*this comprehensive guide*, *the ultimate guide to*, *before diving into*, *whether you are a _ or a*), and Gemini pairs it with reader-address reassurance: *you might wonder*, *you are not alone*, *you can confidently*, *elevate your*. Opus 5.5 added help-language on top, with *can help you* at eight times its Opus 5 rate. Cut all of it. A piece that is a guide does not need to say so.

**Fix.** Do the thing. "Let's look at how caching works" becomes "Caching here happens at three layers."

## 33. Fragmented headers

**Looks like.** A heading followed by a one-line paragraph that restates the heading before the real content begins.

**Why it reads as AI.** The intermediate line is a rhetorical warm-up the model adds out of habit. It pads the piece.

**Fix.** Delete the warm-up line. Go straight from heading to content.

## 34. Hyphenated-word-pair overuse

**Looks like.** Hyphenating compound modifiers with perfect consistency: third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end.

**Why it reads as AI.** Humans rarely hyphenate these uniformly. The model learned the prescriptive rule and applies it every time. Less common or technical compound modifiers are fine to hyphenate.

**Fix.** Drop the hyphen on most common pairs, or apply it inconsistently the way people actually do. If a house style restricts hyphens to genuinely hyphenated compound words, follow that.

## 35. Voice and pacing

**Looks like.** Every sentence the same length. Every paragraph the same structure. No personality, no opinions, no first person.

**Why it reads as AI.** Even clean prose reads as model-generated when the rhythm is uniform and the voice is neutral.

**Fix.** Vary sentence length aggressively. Short hits next to longer sentences that take their time. Use first person when it fits. Have opinions and react to facts. Let some mess in: half-formed thoughts, tangents, asides. Perfect structure feels algorithmic.

## 36. Temporal inflation openers

**Looks like.** "In today's fast-paced world." "In an era of AI." "At a time when." "In today's technological landscape." "As the world becomes increasingly."

**Why it reads as AI.** Pads the lede without saying anything. GPTZero's vocabulary data flags "today's fast-paced world" at roughly 50× human frequency. The opener sounds momentous but carries no information.

**Fix.** Cut the opener and start with the actual point. "Remote work changed how teams hire" beats "In today's fast-paced world, the landscape of work is evolving."

## 37. Balanced both-sides without a position

**Looks like.** Perfectly symmetrical pro/con lists. "On one hand... on the other hand" with no take. Paragraphs that list benefits, then immediately list drawbacks, then end neutral. "There are pros and cons to consider" without saying which matter more.

**Why it reads as AI.** The model avoids commitment. Real writers with a point of view still acknowledge complexity, but they land somewhere. AI prose reports both sides with equal weight and equal flatness.

**Fix.** State what you actually think. If both sides matter, say which one wins in this case and why.

## 38. Definitional cold opens

**Looks like.** Starting with "X is a..." or "X refers to..." when the piece is not a definition. Dictionary-entry leads on essays, posts, and arguments.

**Why it reads as AI.** Models default to explain-then-argue structure. Human writers usually lead with the angle, the tension, or the reason anyone should keep reading.

**Fix.** Open with the claim, question, or scene. Move the definition later, or cut it if the audience already knows what the thing is.

## 39. Escalating adjective chains

**Looks like.** Three or more piled-up adjectives or adjective phrases: "simple, intuitive, and powerful." "Bold, decisive, and transformative." "Seamless, scalable, and secure."

**Why it reads as AI.** Rule-of-three's adjective cousin. Each word sounds positive; none is specific. The chain substitutes for evidence.

**Fix.** Pick one adjective that is actually true and support it with a detail. Or cut all of them and show what the thing does.

## 40. Explicit takeaway boxes

**Looks like.** "Key takeaway:" "The bottom line:" "What this means for you:" "In summary:" mid-piece or at the end, restating what was just said.

**Why it reads as AI.** Tutorial and slide-deck scaffolding. The summary adds no new information; it signals the model is organizing for a reader who needs hand-holding.

**Fix.** Cut the label and the restatement. If the point needs emphasis, make the preceding paragraph sharper.

## 41. Rhetorical question transitions

**Looks like.** "So what does this mean?" "But is that enough?" "How do we solve this?" between sections, with the answer immediately following in the next paragraph. Also headings phrased as questions when the section just answers them: "## Why does this matter?" "## What changed?" "## So where does that leave us?"

**Why it reads as AI.** Fake momentum. The question performs curiosity without risk; the answer was always coming. The heading version is the same tic at document scale, and it turns a table of contents into a FAQ the reader never asked for. Pangram and academic-integrity guides both flag this as a common transition tic.

**Fix.** Drop the question and state the point. "That leaves one problem" works if you need a bridge; a question usually does not. For headings, use the answer as the heading: "## Why does this matter?" becomes "## It changes who signs off on releases." Keep a question heading only when the piece genuinely does not answer it.

**The self-interview.** The sentence-level version asks and answers itself in fragments: "The result? Freedom." "The truth? Nobody checked." "And the best part?" "Simple? Yes. Easy? No." Its LinkedIn relatives travel with it: "Most people X. Successful people Y." "Stop X. Start Y." "Read that again." The 742-point r/ChatGPT thread listing formats readers can no longer stand puts all of them near the top, and "And honestly?" as a paragraph opener rose about sixfold in long Reddit posts between 2021 and 2026 by one independent count. Fix it the same way: state the answer as a sentence and delete the question.

---

## 42. The "it was never X, it is Y" false-depth reveal

**Looks like.** A sentence that denies the obvious cause and swaps in a deeper-sounding replacement, often an abstraction. "The cost was never any single tool, it is the space between them." "The problem was never the code, it was the culture." "It was never about speed, it is about trust." The replacement is frequently vague: the space between, the gap, the seams, the friction, the culture. Those connective-tissue abstractions are catalogued in entry 48.

**Why it reads as AI.** It performs insight by negation. It props up an obvious answer as a strawman, negates it, and reveals a profound-sounding substitute that usually cannot be measured. It fuses the X-not-Y contrast (entry 1) with the deeper-truth authority trope (entry 18), and the comma-splice rhythm ("never X, it is Y") repeats.

**Fix.** Name the real cause plainly and concretely, and drop the "was never" setup and the abstraction. "The cost was never any single tool, it is the space between them" becomes "The handoffs between the tools cost more than the licenses do." If the contrast earns its place, develop the obvious cause as a real point rather than a strawman.

---

## 43. The one-move-solves-all convergence

**Looks like.** A count of problems, forces, or reasons, followed by a claim that one thing answers all of them, with the numbers lining up too neatly. "Three pressures arrived together, and consolidation is the one move that answers all three." "Teams face four challenges, and this solves every one." "There are five reasons, and they all point to one answer."

**Why it reads as AI.** It manufactures false tidiness. Real situations rarely resolve this cleanly. The "one move that answers all N" claim inflates the solution and flattens the problems into a matched set, and the symmetry (N problems, one answer, "all N") sounds conclusive without earning it. It often rides on top of rule of three (entry 13) and significance inflation (entry 4).

**Fix.** Drop the "one move that answers all" tally. Say what the thing actually does for each item, or make the plain claim without the scoreboard. "Three pressures arrived together this year, and each one strengthens the case for consolidating your tools." Let the reader see the fit instead of asserting a perfect one.

---

## 44. The circular bookend

**Looks like.** A sentence or passage that closes by restating its opening in new words, so it loops back on itself. "The handoffs cost more than the licenses. ... and the handoffs become the bottleneck." "Trust is everything here. ... which is why trust matters most." The closing clause re-asserts the premise and adds no new information.

**Why it reads as AI.** The model rounds a passage off by echoing where it started, which feels complete but moves nothing forward. Human writing usually ends on the next step, a consequence, or a sharper detail, not a paraphrase of the opening. It often pairs with the rhetorical wrap-up (entry 3), and when the restatement is also the third parallel item, with rule of three (entry 13).

**Fix.** End on new information: a consequence, a concrete detail, or the next move. If a callback is intentional, make the closing line do more than repeat the opening.

---

## 45. Colon reveals

**Looks like.** A noun or short phrase, a colon, then a dramatic lowercase payoff. "The best part: it learns as you go." "The result: a system nobody understands." "One problem: it doesn't scale." The colon stages a reveal the sentence hasn't earned.

**Why it reads as AI.** It manufactures suspense with punctuation. The colon promises that something surprising follows, so the model reaches for it to make an ordinary statement feel like a payoff. Stacked two or three times in a piece, the tic is obvious. It is the punctuation cousin of the rhetorical wrap-up (entry 3).

**Fix.** Write the sentence straight. "The best part: it learns as you go" becomes "It learns as you go, which is the part I like." Keep a colon only where it does real grammatical work, introducing a genuine list or a quotation.

**Not a frequency claim.** Measured across corpora, models use *fewer* colons than human writers do (entry 54), so do not flag a draft on colon count. The tell is this one construction, and the giveaway is a colon staging a reveal rather than introducing a list.

---

## 46. Faux-insight and throat-clearing openers

**Looks like.** A sentence that promises a hidden truth or clears its throat before saying anything. "Here's the thing." "Here's what nobody tells you." "What most people get wrong is." "The truth is." "Let me be clear." "The reality is." The setup implies the writer is about to reveal something contrarian; the payoff is usually ordinary.

**Why it reads as AI.** It performs insider knowledge to buy authority the content hasn't earned, and it delays the actual point by a full clause. It overlaps with persuasive authority tropes (entry 18, "the real question is," "at its core") and signposting (entry 32), but the giveaway here is the promise of a secret. Real writers with a genuinely contrarian point usually just state it.

**Fix.** Delete the opener and start with the claim. "Here's what nobody tells you: caching is hard to get right" becomes "Caching is hard to get right, and most guides skip why." If the point really is counterintuitive, show why instead of announcing that it is.

---

## 47. Empty intensifiers and adverb tics

**Looks like.** Adverbs and intensifiers sprinkled in to add heat without adding meaning: just, really, very, actually, literally, simply, honestly, truly, basically, fundamentally, importantly, crucially, notably, remarkably, genuinely, arguably, meaningfully, quietly. "This is just really important." "It's actually quite simple." "Honestly, this basically changes everything." "A genuinely useful shift." "Quietly building the best product in the category."

**Why it reads as AI.** The words perform emphasis or candor while carrying no information. "Honestly" and "actually" imply a contrast with some unstated dishonest or expected version that never appears. "Simply" and "just" wave away difficulty the reader may not share. "Genuinely" and "meaningfully" try to certify that this instance is the real one, which only raises the question of the others. "Arguably" hedges and boosts at the same time, so the sentence commits to nothing. "Quietly" is the current standout: it manufactures drama by implying the writer noticed something others missed ("quietly became the default," "quietly shipping"), it topped Forbes's May 2026 list of new AI giveaways, and it is second of a thousand words in the pull request measurement behind entry 67, at 63 times the rate it appears outside the cluster. *Deliberately* is eighteenth there, *genuinely* seventh. Delete any of them and the sentence usually means exactly the same thing, which is the test.

**Which ones, by family, as of late 2026.** Graphite's measurement splits them cleanly. Gemini 3.1 Pro is the intensifier model: *incredibly* at 18x the human rate (and 1,835 times the GPT-6 Astra rate), *highly*, *deeply*, *heavily*, *entirely*, *perfectly*, *absolutely*, *profound*, *immense*, *massive*, with intensifier use overall at 13x. Claude Opus 5 leaned on *every single* (112x), *enormously* (45x), *is genuinely* (more than a thousand uses against four in the human set), and *the single most*; Opus 5.5 cut *is genuinely* by a factor of 26 and kept *quietly* (11x), *noticeably*, *sharply*, and *thoughtfully*. GPT-6 Astra uses the fewest intensifiers of the three and qualifies instead (entry 20). The first-person cousins the 2026 reports keep naming, "Honest caveat:" and "to be honest" as sentence openers, belong here too.

**Fix.** Cut the word and check the sentence still stands. It almost always does. Keep an intensifier only when it marks a real contrast the sentence needs ("the build is slow, but the tests are *very* slow" earns it). One survivor per paragraph at most.

---

## 48. Load-bearing and structural metaphors

**Looks like.** Structural engineering applied to arguments, teams, and decisions that are not buildings.

*Load and structure.* "That assumption is load-bearing." "That word is doing a lot of work." "The heavy lifting happens in the second step." "Scaffolding for the team." "The foundation everything rests on." "The cornerstone." "Bedrock." "The pillars of the program." "Building blocks." "The whole thing collapses without it."

*Connective tissue.* "The thread between the two teams." "The thread running through all of this." "The connective tissue between the systems." "The spine of the argument." "The backbone of the platform." "The seams where they meet." "The fabric of the organization." "The glue holding it together."

*Mechanical cousins.* "The levers you can pull." "The dials worth turning." "That moves the needle." "The plumbing underneath." "Putting it on rails." "Under the hood." "The surface area of the problem." Same move, different workshop.

**Why it reads as AI.** The metaphor claims something matters structurally without naming what depends on it. "Load-bearing" asserts that removing the thing breaks something, and then never says what breaks. "Doing a lot of work" asserts hidden importance and skips the demonstration. The connective-tissue words are the worst of the set, because they name a relationship the sentence never specifies, which is the same move as the false-depth reveal (entry 42, "the space between them"). They also cluster: once a paragraph has a foundation it tends to grow a spine, then some scaffolding. Travel metaphors (entry 16) behave the same way and often show up in the same paragraph.

**And it is now measured.** In GitHub pull request descriptions from human-attributed accounts, sampled daily since January 2025, *load-bearing* was the most characteristic word of the way of writing that grew from about 1% of the corpus to roughly 40% of it, with *seam*, *ladder*, *carries*, and *halves* close behind. Then it fell off: from the week of 2026-09-21, when Claude Opus 5.5 was released, its weekly count dropped by about 80% while the register kept growing. So this entry describes Opus 5 and earlier most of all, and the newest models replaced the structural metaphor with narrated verdicts (entry 67). Entry 67 has the lists, the dates, and the caveats.

**Fix.** Say what depends on what, and what breaks if it goes.

- "That assumption is load-bearing" becomes "If that assumption is wrong, the pricing model and the hiring plan both have to change."
- "The word 'reliable' is doing a lot of work here" becomes "Nobody has defined 'reliable,' and the SLA and the marketing page use it differently."
- "The thread between the two teams" becomes "Both teams depend on the same schema, and neither owns it."
- "The levers we can pull" becomes "We can change price, headcount, or scope."

Swap the literal statement in. If the sentence reads fine, the metaphor was decoration.

---

## 49. Door and unlock metaphors

**Looks like.** "That opens the door to X." "This closes the door on the old approach." "Which doors this opens and which it closes." "That unlocks a new way of working." "It paves the way for Y." "A gateway to Z." "An on-ramp for new users." "That opens the floodgates." "Once you cross that threshold."

**Why it reads as AI.** It is a hedge dressed as a claim. "Opens the door to faster releases" means the writer would not commit to saying releases get faster. The reader gets the feeling of a consequence with none of the specifics, and no way to check it later. The open/close pairing ("which doors this opens and which it closes") is especially machine-flavored, because the symmetry is doing the thinking: it promises a balanced analysis and delivers two abstractions. It also compounds with the structural cluster (entry 48), since doors live in the same building.

**Fix.** State the consequence and who gets it, or admit the uncertainty in plain words.

- "That opens the door to faster releases" becomes "Once that lands, releases go out weekly instead of monthly."
- "This unlocks better reporting" becomes "Finance can pull the numbers themselves instead of filing a ticket."
- If you genuinely don't know whether the thing follows, say that: "This might get us to weekly releases, but only if the test suite gets faster too."

---

## 50. Imperative closers

**Looks like.** A short command at the end that tells the reader what to do next. "Start there." "Pick one and run it this quarter." "Do that first." "Try it on your next project." "Start small. Ship it. Iterate." "The next time this comes up, ask that question."

**Why it reads as AI.** Every model-written LinkedIn post and newsletter ends this way. The imperative simulates the shape of useful advice while adding no new information, and it presumes an authority over the reader that the piece did not establish. It is usually a substitute for a real ending, in the same family as the rhetorical wrap-up (entry 3) and the generic positive conclusion (entry 21). The tell is strongest when the command is vague ("start there"), and when it stacks into a triplet ("start small, ship it, iterate"), which adds rule of three (entry 13) on top.

**Fix.** End on the last real thing you have to say. If there genuinely is an action, make it specific and say who does it and when, or write it in first person about what you are going to do. "Start there" becomes "I'm running this on the billing service first, because it has the worst test coverage." Cutting the closer entirely is usually the better edit; the previous paragraph almost always ends the piece better than the command does.

---

## 51. Consultant-deck vocabulary

**Looks like.** Table stakes, moat, flywheel, north star, single pane of glass, step change, force multiplier, center of gravity, land and expand, blast radius, order of magnitude, first-class citizen, unlock (see entry 49), operationalize, socialize (as in "socialize the plan"), right-size, level set.

**Why it reads as AI.** The words come from strategy decks, where their job is to sound decisive in a room where nobody will ask a follow-up question. Models reach for them because business writing in the training data is saturated with them, and because each one substitutes a category for a fact. "Table stakes" replaces the list of features you actually need. "Step change" replaces the number. Three or more in a piece reads as a deck someone converted to prose.

**Controlled exception.** Some of these are real terms of art with precise meanings in a specific field, and you should not give up a word your audience uses correctly. "Blast radius" in an incident review, "moat" in an investor memo, "north star metric" on a team that has literally defined one. The test is whether a reader in that room could tell you what it refers to. If they could, keep it and use it once. If it is decorating a general-audience piece, cut it.

**Fix.** Replace the category with the fact. "SSO is table stakes now" becomes "Every deal over 200 seats has asked for SSO." "That would be a step change in performance" becomes "That takes the p99 from 400ms to 90ms."

---

## 52. Snowclones and named-law drops

**Looks like.**

*Snowclones.* "X is the new Y." "It's a feature, not a bug." "X all the way down." "Nobody ever got fired for buying X." "The best X is the one you'll actually use." "X is eating the world." "There's no such thing as a free X." "Considered harmful."

*Named-law drops.* Goodhart's law, Chesterton's fence, Conway's law, Jevons paradox, Amdahl's law, Campbell's law, Hyrum's law, Brandolini's law, the Peter principle, Occam's razor, Hanlon's razor, the Dunning-Kruger effect, Parkinson's law.

**Why it reads as AI.** Both moves borrow authority from a shape the reader already recognizes. The snowclone supplies a familiar rhythm so an ordinary claim arrives feeling proven. The named law supplies a citation-shaped object that is doing no work: the piece names the law, gestures at the resemblance, and moves on without showing that the mechanism actually applies. Models love them because the surrounding text is highly predictable once the name appears. Sprinkling three through a piece is decoration, and the giveaway is that you could delete every one of them without changing a single claim.

**Controlled exception.** One named idea can carry a whole piece, and when it does it is not a tell. The conditions: you state the mechanism in your own words, you show why this case fits it, and you let it make a prediction someone could check and find wrong. A Jevons-paradox piece that says "if inference gets 10x cheaper, total spend goes up, and here is the usage curve that would falsify that" is using the idea. A piece that says "this is basically Jevons paradox" and moves on is name-dropping.

**Fix.** Cut the frame and make the claim directly. If you keep a named law, spend a paragraph on the mechanism and commit to what it predicts. One per piece.

---

## 53. The shift framing

**Looks like.** "The bottleneck has moved from X to Y." "The constraint is no longer writing code, it is reviewing it." "The scarce resource has shifted from capital to attention." "The hard part used to be building; now it's distribution." Often repeated in every section with a fresh noun pair.

**Why it reads as AI.** It is a genuinely good thesis shape, which is why models produce it constantly. The trouble is that it is cheap to generate: pick any two nouns, put "no longer" between them, and you have a sentence that sounds like analysis. Nothing in the construction requires the shift to be real, dated, or measurable. It also fuses with the X-not-Y construction (entry 1), so a piece that leans on it inherits that rhythm throughout.

**Exception.** Used once as the actual thesis of a piece, this is a legitimate and strong move, and it is a shape worth keeping. The tell is repetition: the same construction reappearing in every section with new noun pairs, until the piece is a list of reframings rather than an argument. A second sign of the weak version is that the shift is undated and unevidenced. A real one has a when and a because.

**Fix.** Keep one, and support it. Say when the shift happened, what caused it, and what observation would show it had not. Rewrite the others as plain statements of what is true now. "The bottleneck has moved from writing code to reviewing it" survives if the next sentence is "our PR queue went from a two-day median in January to nine days in June while merged volume doubled."

---

## 54. The punctuation profile: sparseness, narrow variety, low variance

**Looks like.** Long sentences joined with "and" that could have been two, few commas inside them, almost no semicolons, colons, or parentheses, no question marks, nobody quoted, and paragraph after paragraph built from periods and commas alone. Every sentence about as long as the last one.

**Why it reads as AI.** Punctuation is one of the three feature families stylometric detectors actually use, alongside phraseology and lexical diversity, and Kumarage et al. (2023) show that adding it improves state-of-the-art detectors. Three findings from that literature matter for editing, and they are not the ones folklore talks about.

*Variety, not counts.* Terčon and Dobrovoljc's survey collects the measurements: AI text uses a narrower set of marks, with commas and periods accounting for most cases (Simon et al. 2023), and specifically fewer commas, question marks, dashes, parentheses, semicolons, and colons than human text, with more periods and more single quotes (Desaire et al. 2023; Simon et al. 2023). The Economist's 2026 comparison of 1.2 million words found the same thinning of commas, semicolons, and parentheses, and traced part of it to models not quoting people, because quotation is what pulls attribution punctuation into a sentence.

*Variance, not mean.* This is the correction worth internalizing. Across the studies the survey reviews, sentence-length *variation* is consistently lower in AI text (Zindela 2023; Desaire et al. 2023), while average sentence length has no consensus at all: some studies find models write longer sentences, some shorter, some find no difference. So do not score a draft for having long sentences or short ones. Score the spread. A page where every sentence lands within a few words of the last one is the tell, whatever the average is.

*The late-2026 profile, now that the dashes are gone.* The newest measurements have a direction, and it is short and narrow. Graphite's feature table for Claude Opus 5.5 against pre-ChatGPT human articles: average sentence length 17.3 words against 26.5, standard deviation 7.2 against 16.9, semicolons 0.1 per 1,000 words against 1.4, exclamation marks 0.0 against 2.8, em dashes 0.0 against 3.1. Humans in that study used exclamation marks more than a hundred times as often as each of the three current models and interrupted themselves with parenthetical asides far more. Arena's data on Opus 5.5 found the same move (average sentence length down from 12.1 to 10.0 words, semicolons down from 6.1 to 1.6 per 1,000), and Wikipedia's editors describe GPT-6 output as built from periods and commas in sentences of roughly 8 to 20 words. The Economist's earlier finding that models write *longer* sentences was true of the models it tested and is not true of these, which is exactly why the mean is not scored. The spread is: human writing in Graphite's set varied more than twice as much from sentence to sentence. What to look for now is a page of medium-short sentences, all periods and commas, with not one exclamation, aside, or semicolon anywhere.

*Distance between marks is its own rhythm.* Stanisz, Kwapień, and Drożdż measured the gaps between consecutive punctuation marks, counted in words, across seven Western languages and found they follow a discrete Weibull distribution whose two parameters are stable enough to distinguish languages, individual authors, and even the target language of a translation. The hazard function always increases, meaning the longer a stretch runs without a mark, the more likely the next word brings one. That work is about language universals rather than detection, so treat it as a lens and not a test. The usable idea is that words-between-marks is a rhythm separate from sentence length, and an unpunctuated 30-word run reads as machine-made even when the grammar is fine.

**Fix.** Break long "and" chains into separate sentences. Use the punctuation you would actually use: a semicolon where two clauses balance, parentheses for a real aside, a colon before a genuine list, a question mark where you are actually asking something. Quote a person by name where you have one. Then check the spread: find the longest and shortest sentence in each paragraph, and if they are close, rewrite one of them to be much shorter.

This entry pulls against entry 23, which strips em dashes, and that is fine. The fix for both is punctuation that reflects real sentence structure instead of one default connector doing every job. It also pulls against the colon-reveal tell (entry 45): models use *fewer* colons than human writers, so colon frequency is not the problem. The noun-colon-payoff construction is.

---

## 55. Over-explained theme and tidy resolution

**Looks like.** A story, anecdote, or case study that states its own moral. The lesson arrives in a closing line ("what I took from that is..."), the plot runs on a single track with no competing pressure, the protagonist's choice is never genuinely hard, and everything resolves. In business writing: the incident story where the fix worked, the team agreed, and the lesson generalizes.

**Why it reads as AI.** StoryScope (Russell et al., arXiv 2604.03136) analyzed 61,608 stories on discourse-level narrative features and found AI fiction over-explains its themes and favors tidy, single-track plots, while human stories keep moral ambiguity and temporal complexity. Narrative features alone separated human from AI writing at 93.2% accuracy, and about 30 features carried most of that signal. The finding matters beyond fiction: any anecdote a model writes tends to arrive pre-digested, with the meaning stated rather than shown, and the mess sanded off. It is the narrative version of the one-move-solves-all convergence (entry 43).

**Fix.** Cut the stated moral and let the events carry it. Keep the part where the decision was actually hard, the objection you did not have a good answer for, and the thing that is still unresolved. If the anecdote has no tension, it is probably not worth telling.

---

## 56. Document-structure artifacts

**Looks like.** Formatting habits that betray a template rather than a document.

- Tables used for content that is a list or a sentence (a two-column table of "Benefit | Description").
- Skipped heading levels: an `##` followed by `####`, with nothing in between.
- Thematic breaks (`---`) inserted before every heading.
- Markdown syntax pasted into a context that does not render it: `**bold**` in a plain-text email, a Slack message, a wiki with its own markup, or a CMS field.
- Placeholder and template text left in place: "[insert company name]," "[Your Name]," "[citation needed]" as a standalone sentence, "Note: verify this figure."
- Every section the same length with the same internal shape, regardless of how much there is to say.

**Why it reads as AI.** These come from Wikipedia's "Signs of AI writing," where they are among the most reliable flags editors use. They are all evidence that the text was generated into a template and pasted, not written into the document it lives in. Placeholder text and unrendered markdown are near-conclusive, because a human writing in that context would have seen the problem immediately.

**Fix.** Convert unnecessary tables to prose or a plain list. Fix the heading hierarchy. Delete decorative rules. Match the target format's actual markup. Search the draft for `[` before publishing. Let sections be the length their content deserves.

---

## 57. Provenance artifacts and citation pathologies

**Looks like.** Strings that leak the generating tool, and citations that do not survive checking.

*Provenance strings.* `utm_source=chatgpt.com` or `utm_source=openai` in a pasted URL. `oaicite`, `contentReference`, `:contentReference[oaicite:0]` (ChatGPT). `[cite: 1]`, `[span_1]` (Gemini). `grok_card`, `grok_render_citation_card_json` (Grok). Lenticular brackets `【 】` and stray dagger marks (DeepSeek). `attached_file`, `ppl-ai-file-upload` (Perplexity).

*Citation pathologies.* Links that 404. DOIs that resolve to an unrelated paper. Invalid ISBNs. Book citations with no page number. Confident quotations that do not appear in the cited source. Named references defined but never used. A source list where every entry is plausible and two of them do not exist.

**Why it reads as AI.** Provenance strings are not stylistic tells at all; they are residue from the tool, and Wikipedia's editors treat them as close to conclusive. Citation pathologies come from the model generating citation-shaped text rather than retrieving sources, which is why the failures cluster in the identifiers (DOI, ISBN, page number) that look plausible but resolve to nothing.

**Fix.** Grep for `utm_source=`, `oaicite`, `contentReference`, `cite:`, `【` before publishing anything that involved a model. Open every link. Check that every quotation appears in the source you attributed it to. If a citation cannot be verified, delete the claim rather than the citation.

**Note on scoring.** These do not belong in the ai-smell score. The score rates how machine-generated prose *reads*; a provenance string is evidence about how the text was *made*, and one instance outweighs any stylistic judgment. Report it separately and plainly.

---

## 58. Zombie nouns and noun-stacked abstraction

**Looks like.** Verbs and adjectives turned into nouns, then strung together with prepositions. "The implementation of the optimization of the deployment process." "There is a need for the prioritization of accessibility." "Improvement in the utilization of available capacity." The giveaway is a sentence whose subject is an abstraction and whose only verb is *is*, *has*, or *provides*.

**Why it reads as AI.** This is the clearest structural signature in the measurement literature. Terčon and Dobrovoljc's 2025 survey of studies on AI-generated text reports the same profile again and again: model output carries more nouns, determiners, and prepositions than human writing, and fewer adjectives and adverbs. Nominalization is what produces exactly that profile. It also removes the actor from the sentence, so nobody is responsible for anything, and it inflates word count by roughly a third while adding no information. Helen Sword's Writer's Diet calls them zombie nouns, because they eat the life out of the verb they came from.

**The test.** Scan for `-tion`, `-ment`, `-ance`, `-ency`, `-ity`, and `-ness`. Two or more in one sentence, or a chain of two prepositions (*of the ... of the ...*), and the sentence needs rewriting.

**Fix.** Find the buried verb and give it a subject who does it.

- "The implementation of the optimization of the deployment process" becomes "We optimized how deploys run."
- "There is a need for the prioritization of accessibility" becomes "Accessibility should go first, and here is what slips if it doesn't."
- "The alignment between the teams' expectations created friction" becomes "Support promised same-day fixes and engineering never agreed to that."

---

## 59. The restatement loop

**Looks like.** One point made three times inside a single section. A sentence states it, the next explains it, then a closing sentence states it again in fresh words. At document scale the same shape repeats: an introduction that previews what the piece will argue, sections that argue it, then a summary restating the introduction. Every section comes out the same length regardless of how much there is to say.

**Why it reads as AI.** Preference training rewards it. Judge models pick the longer answer at a much higher rate than humans do on open-ended tasks, so length itself became a target, and the answer-elaborate-recap shape is the cheapest way to add length without risking a new claim. YapBench measures the residue directly: it scores each response against the shortest sufficient answer and finds newer frontier models pad more than GPT-3.5-Turbo did, which means verbosity is a trained behavior rather than a limit of the model. The circular bookend (entry 44) is the two-sentence version of this tell. This is the section-scale one, and it is the single largest source of wasted words in model prose.

**Fix.** Run the cut test. Delete every sentence that repeats a point already made, then read the paragraph again. Keep the sharpest of the three, not the first. If a section survives at half its length, that was its real length. Let sections be as long as their content deserves and no longer.

---

## 60. Certainty inflation and stripped attribution

**Looks like.** *May cause* becomes *causes*. *Researchers suggest* becomes *research shows*. "In this sample of 40 users, 8 preferred the new flow" becomes "users prefer the new flow." The hedge disappears, the source disappears, the sample size disappears, and the sentence gets shorter and more quotable while becoming less true.

**Why it reads as AI.** Belem et al. (2026) measured this in rewriting tasks and found up to 75% of model outputs shift the certainty expressed in the source, with models raising confidence 1.5 to 2 times more often than lowering it. It compounds across passes: in the medical set, one model inflated 20% of examples after a single rewrite and 40% by the fifth. Greedy decoding made it worse by 9 to 20%, and instructing the model to preserve certainty helped only partly. Hagar et al. (2025) name the same behavior in document summarization as three failure modes: attribution stripping, where a fact from the source arrives as general knowledge; overinterpretation, where limited evidence gets extended into a broad claim; and certainty inflation, where a definitive verb replaces a tentative one. Their framing is the useful one for editing, because the output is usually not wrong. It is unsupported.

**Note the tension with entry 20.** Chat-flavored prose over-hedges ("it is important to note that results may vary"). Rewritten and summarized prose under-hedges. Both are the same defect, which is a claim that has lost contact with its evidence, and the fix in both directions is to size the claim to what you actually have.

**Fix.** Edit against the source, not against the draft. Restore the hedge, the attribution, and the number. "Users prefer the new flow" becomes "8 of the 40 users in the pilot preferred the new flow, which is not enough to call it." If you cannot find the source, cut the claim instead of softening it.

---

## 61. Hyperbole, absolutes, and unfalsifiable claims

**Looks like.** Superlatives and absolutes doing the work of evidence. "Completely transforms how teams work." "The single biggest problem in software." "Nobody is talking about this." "Everything changes once you see it." "Exponentially better." Plus the inflation adjectives: revolutionary, game-changing, unprecedented, seamless, exceptional, pivotal, remarkable, must-have.

**Why it reads as AI.** Bao et al. analyzed 823,798 arXiv abstracts before and after ChatGPT's release and found sentiment turned measurably more positive, alongside a rise in exactly this class of adjective (*intricate*, *valuable*, *exceptional*, *pivotal*, *notable*, and *seamless*, *distinctive*, *lucid*, up roughly 40% within months). The deeper problem is epistemic. An absolute claim cannot be checked, so it cannot be wrong, so it carries no information. The Reuters Institute's summary of research on AI prose puts it well: models make broad, sweeping, emotional statements ("AI in journalism isn't just a tool, it's a revolution") where a reporter would show one specific thing happening to one named person.

**Fix.** Downgrade the claim until you can defend it, then attach the evidence that lets you.

- "Completely transforms how teams work" becomes "Two of the four teams stopped holding standups after the dashboards shipped."
- "The single biggest problem in software" becomes "The problem I hit most often."
- "Nobody is talking about this" becomes "I found two posts about it, both from 2019."

Keep an absolute only when it is literally true and you have checked it. "No customer has ever asked for it" is fine if you went through every request.

---

## 62. Vague expressions of connection

**Looks like.** "In connection with," "associated with," "linked to," "tied to," "in the context of," "as it relates to," "when it comes to," "in terms of." A relationship is asserted and never named.

**Why it reads as AI.** Wikipedia's editors added this to "Signs of AI writing" in 2026 after seeing it constantly in flagged articles ("cited his work, in connection with the Grammaire Blois"). The construction is generated exactly when the model knows two things belong in the same sentence and does not know how. It is also the phrase family that survives a slop-word scrub, because none of the individual words look suspicious.

**Fix.** Name the relationship with a verb. Causes, funds, replaced, reports to, sits inside, was charged with, depends on, contradicts. "Latency issues associated with the new cache" becomes "the new cache adds 40ms to every uncached read."

---

## 63. Assertion chains with no connective logic

**Looks like.** Three or four sentences in a row, each true, none joined to the one before it. No *because*, *so*, *which means*, *unless*, *even though*. The paragraph reads like a list of facts wearing the costume of an argument.

**Why it reads as AI.** Bao et al. found a significant drop in connective words in post-ChatGPT abstracts and a measurable decline in readability, even as vocabulary got richer and sentence structure got simpler. Richer words, simpler syntax, weaker cohesion. The model produces fluent assertions and leaves the reasoning that links them implicit, because the link is the part that requires a position. This is the paragraph-level counterpart of entry 54 (punctuation sparseness), and it is the mirror image of entry 22: the connectives that do show up are the decorative ones at the front of a paragraph ("Moreover," "Therefore"), while the ones that would carry the argument inside it are missing.

**Fix.** For each sentence, ask what it does for the sentence before it, then write that relation down. "The cache is new. Latency went up. The team rolled it back." becomes "Latency went up right after the cache shipped, so the team rolled it back, which means we still do not know whether the cache caused it."

---

## 64. Textbook-perfect punctuation and missing contractions

**Looks like.** Punctuation that is flawless and uniform in a register where a person would have loosened up. No contractions anywhere ("it is," "do not," "cannot" in a blog post). Every serial comma in place, every compound modifier hyphenated, no sentence fragments, no parenthetical asides, no sentence starting with *And* or *But*, no ellipsis, no one-word answer standing on its own. Formal punctuation applied evenly across formal and informal passages alike.

**Why it reads as AI.** Two separate observations meet here. Models under-use apostrophes and avoid contractions and colloquialisms: Rudnicka's comparison found models strip informal constructions, and a formal syntactic comparison of LLM and human news writing found human authors reaching for contractions ("haven't"), colloquialisms ("a couple dozen"), and blunter phrasing more often, with the model output reading as an averaged grammatical profile of many human styles. Separately, the uniformity itself is the signal. Human punctuation drifts with register, mood, and how tired the writer was; model punctuation stays textbook-correct at a constant temperature from the first line to the last. A page can be perfectly punctuated and still sound like nobody.

**The contraction half is now family-specific, so do not score it alone.** It held for the 2024 models and is breaking down. Rudnicka and Juzek (arXiv 2608.06589, 2026) ran the same prompts through a 2024 cohort and a 2026 cohort of six models each and found contraction rates in the 2026 group ranging from about 1,200 to over 30,000 per million words, with Claude Haiku 4.5 at the top. Negation contractions averaged 3,139 per million in the 2026 cohort against 97 in 2024, about 32 times as many, which the authors describe as "consistent with, but not conclusive of" a rise. Graphite's 2026 data points the other way for one family: Gemini 3.1 Pro's contractions nearly disappeared between versions. So a page with no contractions is a Gemini-shaped tell or a formal writer, and a page with plenty of them is no evidence of a human. The uniformity half of this entry still holds across families; score that.

**What not to do.** Never introduce errors to sound human. Faking a comma splice or a typo is transparent and it makes the writing worse. Everything below is correct English. It is just the correct English that people actually use.

**Fix.** Match the register the piece is written in.

- Contract where speech would. "It is not clear" becomes "it isn't clear" in anything conversational.
- Let one sentence be a fragment where the emphasis earns it. "Not once."
- Start a sentence with *And* or *But* where the rhythm wants it.
- Put a real aside in parentheses instead of smoothing it into the main clause.
- Ask an actual question, with a question mark, when you have one.
- Leave a compound unhyphenated where common usage does (entry 34 covers this from the other side).

The test is to read a paragraph aloud in the voice the piece is meant to have. Wherever your mouth wants a contraction and the page has two full words, the page is wrong.

---

## 65. The through-line

**Looks like.** A heading or sentence announcing that everything just described is secretly one thing. "The through-line, if you want one." "The thread running through all of this." "What connects all five." "At bottom, these are the same question." The reveal that follows is almost always an abstraction rather than a mechanism.

**Why it reads as AI.** Models are rewarded for coherence, so they manufacture it. A genuine unifying cause is rare and worth stating; the construction shows up whether or not one exists, because a synthesis paragraph is what the shape of a document seems to call for at that point. It also does the reader's work for them, which flatters the writer twice: once for spotting the pattern and once for being generous enough to explain it. Closely related to entry 44 (the rhetorical wrap-up) and entry 50 (one-move-solves-all): all three assert structure the argument has not earned.

**Fix.** If the items really do share a cause, name the cause and skip the announcement. Put it in the heading and let the reader notice the pattern themselves. If they do not share a cause, let them be several things; a list of six real problems is more useful than five real problems and a forced sixth. "The through-line, if the room wants one: context that used to live in a person's head now has to be authored" becomes "All six fail for the same reason. Nobody wrote the context down."

---

## 66. Clothing and costume analogies

**Looks like.** "The same problem wearing different clothes." "Wearing the costume of an argument." "Dressed up as." "X in Y's clothing." "Cloaked in." "A thin veneer of." "Under the hood" belongs to the mechanical family in entry 48, but it rhymes with this one.

**Why it reads as AI.** It is the stock metaphor for *superficially different, fundamentally the same*, and it arrives pre-assembled, so it costs nothing to write and carries nothing. Like the structural metaphors in entry 48, it asserts a relationship instead of naming one: the reader is told two things are secretly identical and never told what they share. It also pairs almost automatically with entry 65, because a writer who has just announced a through-line needs an image for it, and this is the nearest one to hand.

**Fix.** Name what is actually shared, in the same number of words. "All six problems are the same problem wearing different clothes" becomes "All six fail because nobody wrote the context down." "A list of facts wearing the costume of an argument" becomes "a list of facts with no *because* between them." If you cannot state the shared thing plainly, that is useful information: the sameness you were about to assert may not be there.

*This catalog used the costume version itself in entry 63 before this entry existed, which is a reasonable illustration of how easily it slips in.*

---

## 67. The agent register

**Looks like.** Plain, concrete, physical English applied to things that are not physical, at high density, in short sentences built on negation. "That assumption is load-bearing." "The old path survived untouched." "The check fires, and nothing else moves." "The two halves are byte-identical." "It quietly stopped being true." One paragraph of it reads as careful and specific. Forty of them read as one writer, because they are.

**Why this entry exists.** The rest of the catalog is compiled from detector research, style guides, and observation. This entry is compiled from a count. Louis Abraham's *load-bearing* project samples newly opened GitHub pull request descriptions every day since January 2025, drops accounts that are not people by the shape of their login, and clusters what is left into ways of writing by KL-divergence k-means over word counts. The model has no time parameter, so the curve is not a fit; it is a count of descriptions placed by their words alone.

As of the analysis generated 2026-11-10 (672 days, 531,322 descriptions, ten clusters), one cluster went from about 1% of the corpus at the start of 2025 to 39.5% of the four weeks ending 2026-11-02, and 41.3% of the last of them, still rising at about 1.2 points a week. Its name word, *load-bearing*, was the top of the list through the summer. Entry 48 was already in this catalog when that measurement landed.

**A correction to earlier versions of this entry.** This catalog used to cite 47,464 descriptions, eight clusters, a 44.6% share, and *load-bearing* at 123x. Those figures came from an earlier state of the project and do not reproduce from its current method: it has since moved to ten clusters, replaced its three frequency floors with one rule (50 distinct accounts), and changed how the multiplier is computed. The project's own README is clear that these constants are choices. Cite the live page with its date, never a remembered number, including this one.

**Then the vocabulary moved, on a date.** In the week of 2026-09-21, the week Claude Opus 5.5 was released, the cluster kept growing but its signature words fell away. Weekly appearances of *load-bearing* went 97, 72, 69, then 17, 12, 10, 11, 8, 6, 5; *genuinely* fell from about 150 a week to about 20; *deliberately* from about 500 to about 120; *quietly* from about 80 to about 20. Rising over the same weeks: *refused* (about 450 to about 700 a week), *says* (about 575 to over 850), *stand-in* (single digits to about 50). As of November the cluster's top words are *somebody* (26.7x), *nobody* (25.5x), *drew*, *plainly*, *mutation-checked*, *re-measured*, *quietly* (21.2x, eighth), *says*, *rests*, *halves*, *argued*, *refused*, *nowhere*, *judged*, *owed*, *handed*, *decides*, *ruling*, *told*, *whoever*. *load-bearing* is now 249th at 7.3x. That matches what Anthropic said it changed in Opus 5.5 (less jargon, fewer idiosyncratic phrases) and what Arize and Graphite measured outside GitHub (entry 73). The register did not go away. It traded structural metaphors and certifying adverbs for narrated adjudication and reported speech: the test *refused*, the doc *says*, *nobody* asked, the reviewer *judged*, a *stand-in*, what the change is *owed*.

**The clusters inside it.** Multipliers are how much more often the word appeared inside the cluster than outside it, from the summer 2026 fit, before the September shift. Read them as the vocabulary of Claude Opus 5 and earlier; the newer words are in the paragraph above.

1. *Physical nouns for abstractions.* load-bearing (123x), seam (37x), ladder (37x), halves (33x), ceiling, floor, wall, spine, rail, plate, band, leg, hole, envelope, substrate, machinery, carrier, subtree. This is entry 48, and the measurement says it is now the top of the list rather than one item on it.
2. *Objects given intentions.* carries (36x), sits, holds, fires, refuses, lives, sees, says, asks, declares, drives, owns, walks, rides, decides, proves, treats, reaches, leaves, belongs. The config sits, the check fires, the flag carries, the test refuses, the job decides. It is the mirror of copula avoidance (entry 11): rather than an elaborate verb standing in for *is*, a verb of intention standing in for a thing that has none.
3. *Survival and fate.* survived (62x), survives, survive, untouched (25x), inert, collapses, folds, degrades, recovers, landed, lands, arrives, stayed, gone, killed, retired, swallowed, discarded.
4. *Adverbs that certify.* quietly (63x, and second on the whole list), deliberately (26x), loudly, silently, precisely, exactly, identically, structurally, unconditionally, merely, honestly, verbatim. Entry 47 covers the family; this is the measurement behind it.
5. *Candor words.* genuine (39x), genuinely (37x), honest, honesty. Words that assert the writer is being straight with you, which is the one thing straight writing never has to assert.
6. *Verification vocabulary.* byte-identical (35x), asserted, asserts, claimed, proven, reproduces, reproduced, measured, unit-tested, byte-for-byte, criterion, invariant, verdict.
7. *Absolute negation.* nothing (21x), never, nobody, neither, alone, ever, forever, unaffected, unmodified, unconditional, no-ops. Short sentences whose subject is an absence.
8. *Diagnostic nouns.* refusal (29x), symptom, defect, defects, divergence, precedent, caveat, headroom, staleness, trap, fan-out, throwaway.

**Why it reads as AI.** Every word above is a good word, which is what makes the register hard to see. None of it is *delve* or *tapestry*; a reader scanning for the ChatGPT-era vocabulary finds nothing and concludes the piece is clean. The tell is the combination. Concrete nouns are borrowed to make abstract claims feel checked, inanimate subjects are given verbs of intention so the prose reads as reportage instead of assertion, and absolutes and certifying adverbs supply confidence the evidence has not. Entries 48, 47, 11, and 61 each caught part of this before the measurement existed, which is why the fixes there apply here unchanged.

The register is also self-ratifying. *Quietly* implies the writer noticed something others missed. *Genuinely* implies the other instances were not. *Load-bearing* implies that removing the thing breaks something, and then never says what. Each move claims a verification the sentence does not perform.

**Fix.** Same fix as entry 48, applied to a wider list. Swap the literal statement in and see whether the sentence survives.

- "The old path survived untouched" becomes "The old path still runs, and no test changed."
- "The check fires" becomes "The check runs" or "The check rejects the request," whichever is true.
- "It quietly stopped being true" becomes "It stopped being true in March, and nobody updated the doc."
- "The two halves are byte-identical" is fine, if you diffed them. If you did not, it is the register talking.

The one to watch hardest is the agentive verb, because it is invisible and it is everywhere. When a thing that cannot want anything *refuses*, *decides*, or *asks*, either name the actor who made it do that or use the plain verb.

**Independent confirmation, from outside GitHub.** Clark, Martin and Mahowald (arXiv 2610.29162, October 2026) measured the features that predict human reading difficulty across nine frontier and near-frontier models. Every one of the nine used more inanimate subjects with animate verbs than human writers did ("the data suggests," "the test refuses"), and more low-frequency word sequences; most also used longer dependencies and more stacked nouns. Their explanation is the useful part: models are increasingly trained for information density on math, code, and reasoning, which rewards packing information in over getting it across, and a length-penalty fine-tune pushed a model further from human-like text. So the register is a side effect of what the models are rewarded for, and it costs the reader something measurable.

**The vocabulary of the compressed form.** Users mining their own Claude transcripts in late 2026 (an 811-point r/ClaudeAI thread, with a 535-point one corroborating) list a technical-register set that sits next to this entry: *blast radius*, *footgun*, *escape hatch*, *belt-and-suspenders*, *the culprit*, *the offending line*, *the tell is*, *the kicker*, *the punchline*, *hand-wavy*, *concretely*, *empirically*, *grounded in what's actually*, *sit with it*, *the thing to hold onto*, *Verdict:* as a label, *say the word* as a closer, and a scare-quoted hyphenated coinage standing in for a description (the "let-me-die" scope). None of these is wrong. Several in one reply is the register.

**The compressed form.** A practitioner write-up from June 2026 ("Claudish," slhck.info) names a sibling that shows up after long agent sessions: half-sentences with nouns stacked as modifiers and team jargon left unexplained. "Cap the study-lifecycle handlers so a hung study can't wedge the deep-link." "This is a real fleet-storm collapse." The fix is the same one: write the subject, the verb, and the consequence, and define the coined noun or drop it.

**The caveats, and they are load-bearing.** Three of them.

The study measures pull request descriptions attributed to human accounts, with every bot- and agent-named login removed. Nobody observed an assistant writing any of it. What the data supports is that a way of writing became common; the attribution to coding agents is inference, and the project says so.

Its constants are choices, and the project says so. The number of clusters was picked from a window of values that keep the leading cluster coherent, and earlier versions tuned both it and the frequency floor so that *load-bearing* ranked first. The arrival and the weekly shape are robust across fits; the exact share and the rank order of words are one fit's answer, and they have changed every time the method did. Treat the shape and the September shift as measured and any single multiplier as provisional.

And the corpus is technical. A blog post is not going to say *byte-identical*. The vocabulary lists above are for code review, commit messages, PR bodies, and design docs. What transfers to prose is the moves rather than the words: physical nouns doing abstract work, objects with intentions, adverbs that certify, negation used as a load-bearing claim, and, since September 2026, prose that narrates a verdict (*the check refused*, *the spec says*, *nobody owns it*) where it should state a fact.

---

## 68. Reflexive validation and accepting the premise

**Looks like.** "That's a really thoughtful question, and it's completely understandable to feel that way." "You're right to be concerned about this." A piece that answers the question exactly as framed, including a premise that is wrong. Both sides of a disagreement affirmed so nobody is told they are mistaken.

**Why it reads as AI.** It is measured. ELEPHANT (Cheng et al. 2025) ran 10,395 advice and assumption-laden prompts through 11 models and compared them with human answers. Models offered emotional validation in about 76% of cases against 22% for people, used indirect, hedged language in about 87% against 20%, accepted the asker's framing in about 90% against 60%, and affirmed both sides of a moral conflict about 48% of the time. Entry 31 covers the chatbot opener; this is the deeper habit underneath it, and it survives into polished prose as a refusal to tell the reader anything they did not already believe.

**Fix.** Cut validation that does no work. Check the premise before answering it: if the question assumes something false, say so first. Where the draft affirms both sides, decide which one is right and say why, or name the specific condition under which each is right. Pair with entry 37 (balanced both-sides) and entry 20 (hedging).

**The 2026 inversion.** Validation used to come before an answer, and now it also comes after a correction: the model is told it was wrong and immediately agrees, in the same warm register. "You're right to push back on that." "You're completely right to call me out." "Great catch." "Your instinct is right." Reddit threads collecting the phrases that annoy users most in late 2026 put these near the top. It is the same habit as the rest of this entry, and entry 82 covers the move that usually precedes it.

## 69. Stock names and default characters

**Looks like.** The example customer is Sarah. The protagonist is Emily, or Elara, or Kael. The town is Willow Creek; the company is Acme or TechCorp; the researcher is Dr. Chen.

**Why it reads as AI.** Models reach for the same few names because they are the most probable fill for "a person." Russell, Karpinska and Iyyer (2025) found "Emily" or "Sarah" in about 63% of GPT-4o articles and 70% of Claude articles in their sample, and the expert annotators in that study used it as a tell.

The names rotate with the model. In Pangram's November 2026 sample of 418 GPT-6.1 Sol creative-writing answers, the women were Mara or Maya in 65 responses, usually with the initials M.V. and most often the surname Vale (Mara Velez and Mara Venn also appeared), and the men were Daniel. The same set opened with "The first..." 36 times, against 11 for Claude Haiku 5.5 and once for Gemini. Karen Spinner's July 2026 comparison of about 450 samples counted "Mara" 183 times from GPT-5.2. Elara and Kael were the 2024 to 2025 cast. Assume the current cast is whatever the newest model reaches for, and check the draft for that instead of trusting a list.

**Fix.** Use a real name when there is one (with permission), or pick a deliberate one that fits the setting. In technical writing, a role ("the on-call engineer") is often better than an invented person anyway.

## 70. Quotes in the narrator's voice

**Looks like.** "'This changes everything about how we work,' said the program director." A quote that is too formal for speech, sounds exactly like the paragraph around it, and lands at the end of the paragraph to wrap it up.

**Why it reads as AI.** Real quotes are where another voice enters the piece: shorter, rougher, sometimes ungrammatical, often placed where they argue rather than where they summarize. In Russell et al. (2025), quotes were cited in about 22% of expert explanations for spotting AI articles, specifically for sharing the article's tone and closing paragraphs. A quote that could be deleted and replaced with the writer's own sentence with no change in voice was probably invented or flattened.

**Fix.** Use what the person actually said, including the plain or awkward parts. Move it to where it does work, usually as evidence before the claim, not as applause after it. If there is no real quote, do not manufacture one; paraphrase with attribution.

## 71. Purple prose and stock imagery

**Looks like.** "A tapestry of modernity." "The heart of progress." "Faces etched with stories." "The city hummed with possibility." Sensory decoration attached to things that did not need it, often three images to a sentence.

**Why it reads as AI.** Chakrabarty, Laban and Wu (CHI 2025) had professional writers edit 1,057 model-written paragraphs (the LAMP corpus) using a seven-category taxonomy. Cliché accounted for about 17% of edits and purple prose about 10%, alongside awkward word choice (about 28%), poor sentence structure (about 20%), redundant exposition (about 18%), lack of specificity (about 8%), and tense inconsistency (about 3%). No model family wrote markedly better than the others. The taxonomy doubles as an edit checklist for creative and feature writing.

**The current stock, by family.** EQ-Bench's creative-writing slop lists, recomputed as models ship, show each family has its own clichés as of late 2026: Claude 5 models reach for "like a held breath," "looked at her for a long moment," and "something else entirely"; GPT-6 for "stood close enough," "could not decide whether"; Gemini 3 for "heart hammering against his ribs like a trapped bird," "voice dropping an octave," and "a sharp, metallic tang." StoryScope adds the structural version: model fiction renders emotion as a body sensation far more often than human fiction does.

**Fix.** Keep one image only when it carries information the literal statement cannot. Replace the rest with the observed detail: what the faces actually showed, what the city actually sounded like.

## 72. The grammatical fingerprint

**Looks like.** Sentences hung on present participles ("Building on this foundation, the team shipped..."), nominalizations ("the implementation of"), clauses with "that" as the subject ("That this matters is clear"), and long coordinated phrases ("faster and cheaper and more reliable deployments"), with almost no agentless passives.

**Why it reads as AI.** Reinhart, Brown and colleagues (PNAS 2025) compared parallel human and model texts written from the same prompts on 66 of Biber's grammatical features. Instruction-tuned models used present participial clauses at 2 to 5 times the human rate (GPT-4o about 5.3 times), nominalizations at about 1.5 to 2.1 times, "that"-subject clauses at about 2.6 times, and phrasal coordination at about 1.9 times, while GPT-4o used agentless passives at roughly half the human rate. The gap was larger in instruction-tuned models than in base models and did not shrink with scale. This gives entries 6 (superficial -ing endings) and 58 (zombie nouns) a grammatical measurement rather than a vocabulary list.

**Fix.** Turn participial openers into a main clause with a subject. Turn nominalizations back into verbs. Break long coordinated phrases into the one or two items that matter. And do not strip every passive: "the bug was introduced in March" is often the honest sentence when nobody knows who did it. Note that entry 17 warns against subjectless fragments, which is a different problem.

## 73. Model-family openers and formatting

**Looks like.** "Certainly!" "Below is a..." "Here's a breakdown of..." "Based on the information provided..." Bold on every key phrase. A header over every three paragraphs. The same markdown shape regardless of what the content needed.

**Why it reads as AI.** Sun, Yin, Xu, Kolter and Liu (ICML 2025) trained classifiers that told five model families apart with about 97% accuracy. Reported habits: ChatGPT opens with "Certainly" or "Below is" and leans on "such as" and "overall"; Claude leans on "here," "according to," and "based on"; ChatGPT bolds and uses headers where Claude uses plain bullets. Markdown structure alone identified the model about 73% of the time, and the signal survived shuffling the words. Formatting is a fingerprint in its own right, which is why it has its own dimension.

**The late-2026 profiles.** Those habits belong to the 2024 models Sun et al. tested. The current generation has moved, and the measurements below are the best available as of November 2026. All of them come from studies of one prompt style each, so read them as tendencies. None of them is a signature.

| Family | Habits that set it apart |
|---|---|
| Claude (Opus 5, Opus 5.5, Haiku) | Salience flags (*this matters*, *why X matters*, entry 75), reassurance adjectives (*dependable*, *steady*, *thoughtful*), superlatives (*the most popular*, *one of the best*), straight apostrophes. Opus 5.5 nearly eliminated em dashes and halved its stock "Claudisms" (Arize: 4.79 to 2.38 per 1,000 words) but added about 2.5 times more bold lead-in bullets and 35% more three-part lists. Haiku 4.5 opened 46% of answers in Rudnicka and Juzek's 2026 prompts with a safety disclaimer. |
| GPT (GPT-6 Astra, GPT-6.1 Sol) | Corrective framing (*not simply*, *rather than relying*, *does not establish*, entry 74), *distinction* and *matters because*, practical-scaffolding words (*a useful starting point*, *a practical way to*), modal hedges (*may*, *can support*, *not necessarily*). Curly apostrophes and quotes, and still some em and en dashes (entry 28). Opening disclaimers nearly gone (0.2% for GPT-5.4 Mini). Least mannered of the three (entry 78). |
| Gemini (3.1 Pro, 4) | Intensifiers (*incredibly*, *highly*, *massive*, *profound*), formal connectives (*furthermore*, *additionally*, *ultimately*), SEO-guide scaffolding and reader reassurance (entry 32), "is not just a _ it is", *lies in* and *at the heart of*, purpose-driven participial openers (*by prioritizing*, *by understanding*). Contractions nearly gone. |

Two cautions travel with the table. First, Graphite found 65% of all measured tells unique to one family and 55% to 72% unique to one *version* within a family, so the table will be wrong about the next release. Second, the families are not converging on human writing at the same speed: between versions, only Claude's word distribution moved closer to the human baseline (19% closer in Opus 5.5), while GPT-6 Astra's moved 8% further away. A reviewer who learned the tells on one family will miss the other two.

**Fix.** Delete opener phrases outright. Format for the reader's task: headers when someone will navigate, bold for the one thing they must not miss, prose when the ideas connect. If the formatting would be the same whatever the content, it is the model's habit, not the content's need.

## 74. Corrective framing and the "does not establish" disclaimer

**Looks like.** A sentence that tells the reader how *not* to take a claim. "Claims about its suspension should be treated as religious tradition rather than as archaeological explanation." "The site describes these as systems undergoing evaluation, rather than validated clinical tools." "The guidance does not establish that the park has a contamination problem." "A high score does not automatically mean the code is safe." "Price alone does not determine quality." "X should not be confused with Y," when nobody was going to confuse them.

**Why it reads as AI.** It is the newest measured tell, and it arrived on a date. Wikipedia's editors describe it as "extremely uncommon, verging on unheard-of" in model output before mid-2026, roughly coinciding with the July release of GPT-5.6, and now among the most common signs of new AI text. Graphite's 2026 study measured the same move: GPT-6 Astra talks about what things are not at 12 times the human rate, with *not simply* at 157x, *than relying* at 170x, *not automatically* at 233x, and the frame "rather than _ every _ as" at 339x, and its own corrective framing kept rising across versions while its hedging fell. Against Claude Opus 5.5, Astra wrote *does not establish* 275 times as often. It reads as care. What it does is preempt a misreading the reader was not about to make, so the sentence spends itself on a claim nobody advanced, and when it attaches to a source it downgrades that source without saying why.

**How it differs from entry 1.** X-not-Y dramatizes ("it's not a tool, it's a mindset"). This one corrects, in the register of a careful reviewer, and it usually guards an inference, where X-not-Y dramatizes a description. It is also the descendant of the 2024 source-availability hedge (entry 30): same anxiety about sources, now aimed at what the reader might conclude.

**Fix.** Ask whether any reader in this audience would have drawn the inference being blocked. If not, delete the sentence. If yes, say what the source does show and stop: "The guidance covers soil testing for new plantings" instead of "The guidance does not establish that the park has a contamination problem." Keep a correction only where a misreading is likely and costly, and then make it specific: name who reads it the wrong way and what goes wrong if they do.

## 75. Salience flags: "this matters"

**Looks like.** Sentences whose only job is to announce that something is important. "This matters because..." "Why this matters." "The distinction matters." "That's what matters most." "This is just as important." "Here's why that matters." Often a section heading in question form ("Why does this matter?") followed by a paragraph that restates the section above.

**Why it reads as AI.** It is the most consistently measured tell of late 2026 across families. In Graphite's data, *matters because* ran at 357 times the human rate in GPT-6 Astra and 132 times in Claude Opus 5, *the distinction matters* appeared in Astra articles and never once in the 10,000 human ones, and in Opus 5.5 *this matters* ran at 116x and "why _ matters" at 92x. Arize's annotated test of Opus 5 against Opus 5.5 found the "salience flag" the single most common Claude habit in both versions, surviving a release that cut most of the others by half or more. Forbes's May 2026 list had already named *matters* as a giveaway; this is the measurement. It is significance inflation (entry 4) with the inflation made explicit: where entry 4 puffs the sentence up, this one steps outside the sentence to tell you it was important.

**Fix.** Delete the flag and keep the reason, if there is one. "This matters because the cache is shared across tenants" becomes "The cache is shared across tenants, so one tenant's purge empties it for everyone." If deleting the flag leaves nothing behind, the paragraph never established why the point mattered and needs a consequence, not a label. Never use a "why X matters" heading; write the heading as the claim.

## 76. Trade-offs without a cost

**Looks like.** "Faster builds without sacrificing reliability." "Scale without losing the personal touch." "Stronger security without requiring users to change anything." "Flexibility without compromising performance." Every gain arrives free.

**Why it reads as AI.** All three current families do it, which is rare in this catalog. Graphite's 2026 data: *without requiring* at 70x the human rate in GPT-6 Astra, *without losing* at 22x in Astra and 6.1x in Claude Opus 5, *without sacrificing* at 7.8x in Gemini 3.1 Pro, *without compromising* at 5.2x in Gemini. The construction promises a resolution of exactly the tension a reader would want examined, and it is the sentence-level version of the one-move-solves-all convergence (entry 43). IdeaLens's authors (arXiv 2610.06778, 2026) found the idea-level version too: AI-originated content tends toward solutions with no stated downside, and human-originated content discusses downsides and open problems.

**Fix.** Name the cost, or the condition under which there is none. "Builds run 40% faster; the cache adds about 200 MB per runner" is a trade-off. "Faster builds without sacrificing reliability" is an advertisement. If there really is no cost, say why in mechanism terms ("because the cache is keyed by lockfile hash, a stale hit is impossible"), which is the only version a reader can check.

## 77. Synthesis and layering transitions

**Looks like.** Paragraph openers that stitch the previous points together without adding one. "Together, these features..." "Taken together, these..." "This adds another layer." "Another dimension to consider is..." "Looking ahead, ..." "What comes next is..." "In practice, ..." "The result is a..." "By combining X and Y, ..."

**Why it reads as AI.** Graphite's 2026 measurement found these replaced the *furthermore* and *additionally* of earlier models in Claude and GPT (Gemini kept the old ones, entry 22). *Together these* ran at 95x the human rate in GPT-6 Astra and 56x in Claude Opus 5.5, *another dimension* at 117x in Astra, *adds another layer* at 27x and *looking ahead the* at 40x in Opus 5.5, and the frame "the result is a _ that" at 130x in Opus 5.5. They feel like analysis because they gesture at synthesis, but "together, these features make it a strong choice" restates the list and adds a verdict nobody argued for. The forward-looking ones (*looking ahead*, *what comes next*) are the 2026 shape of the "challenges and future prospects" section (entry 9).

**Fix.** Delete the opener and see if the paragraph starts better on its second sentence; it usually does. If the paragraph really is a synthesis, state the new thing the combination produces that no single part does, with a number or an example. A "looking ahead" paragraph needs a date and a named plan, or it goes.

## 78. Mannered prose and the "earns its place" idiom

**Looks like.** Metaphor and flourish standing in for a plain statement. "A dial worth turning" for "a parameter worth varying." "This point earns its keep." "The stand mixer earns its counter space." "The technique earns its place in the toolkit." "Let the data do the talking." Each sentence is fine. The page is a performance.

**Why it reads as AI.** *Mannered prose* is the term Anthropic's own prompting guidance uses for this failure, with "this point earns its keep" as its example, and Graphite scored it directly by having a model judge rate 1,000 matched articles per model on Anthropic's definition. Pre-ChatGPT human articles averaged 6.65 out of 100. Claude Opus 5 scored about 2.5 times that (16.75), as did Gemini 3.1 Pro; Opus 5.5 came down 37% to 10.57, about 1.6 times human; GPT-6 Astra sat at about 1.2 times. The Opus 4 to Opus 5 rise was 19%, so this is a habit that grew with capability before it was trained down. The *earn* idiom is the one that survives: Arize found Opus 5.5 still writing "earns its counter space" after most other stock metaphors fell by 70%, and Forbes had flagged *earn* in May. Entry 71 covers purple prose in fiction; this is the same instinct in explanatory writing, where it is harder to see because each image is small and nearly literal.

**Fix.** Replace each figure with the statement it decorates and keep the figure only if the literal version loses information. "The stand mixer earns its counter space" becomes "If you bake weekly, the stand mixer is worth the counter space; if you don't, it isn't." Ban *earn* as a verb for objects and ideas; a person earns things, a paragraph does not.

## 79. Changelog voice: writing the revision instead of the document

**Looks like.** A second draft written for a reader who memorized the first one. The title describes the change rather than the conclusion ("...but the Cause and the Lever Were Misstated"). A "What changed in v3" table sits at the top. Sections labeled *Revised*, *Retracted*, *Replaced*. Body text organized as "What holds up: ... / What was wrong: ...", refuting claims the current reader never saw. Phrases like "the single most important correction," "the corrections matter because," "does not survive contact with the source data." In edit summaries and commit messages, the same voice reports what was *not* changed: "while preserving the original meaning," "preserved references and categories," "retained existing structure," "avoided introducing new claims," "ensured consistency."

**Why it reads as AI.** It is how a coding agent is trained to hand back work, as a diff, applied to prose where nobody wants a diff. The June 2026 "Claudish" write-up (slhck.info) describes it as the third and least visible level of Claude's accent, appearing when a model revises its own document after review. Wikipedia's editors document the edit-summary form independently, with the observation that does the work: humans rarely describe the things they did not change, while a model prompted to "make X change but preserve Y" reports both. The result reads as careful and is unreadable to anyone arriving fresh.

**Fix.** Write every revision as if it were the first version, for a reader who has seen nothing before. Lead with the current conclusion ("We found Y, and the lever is Z"). Move the change history to the end, or to the commit message, or delete it. In commit messages and edit summaries, say what changed and why, and leave out what stayed the same unless someone would reasonably assume it moved.

## 80. The default argument and interchangeable detail

**Looks like.** An essay whose main argument is the first one anyone would think of, supported by sub-points that are generalized and hedged. Details that would fit any similar subject ("the restaurant's warm atmosphere and attentive staff"). Numbers or methods cited without the context needed to check them ("studies show a 40% improvement"). Every surface tell can be gone and the piece still says nothing a reader could not have predicted from the title.

**Why it reads as AI.** Two 2026 studies measured this at the level of ideas rather than words, and both found the signal survives rewording. Kim, Chang, Pham and Iyyer (*Argument Collapse*, arXiv 2606.01736) compared 1,487 human responses to NYT and Boston Review debates with 23,381 model essays on the same questions: 65.3% of human main arguments were unique within a debate against 3.4% of model ones, 41.0% of human sub-arguments against 9.1%, and prompting for diversity recovered only about half the human range. IdeaLens (Rajendhran, Iyyer and colleagues, arXiv 2610.06778) strips documents down to outlines of discourse roles so the wording is gone, then detects whether the *ideas* came from a model. On 50 stories that people wrote by hand from AI-generated plans, it flagged 68%, while a prose detector flagged 8%. The authors describe AI ideation as favoring details that could fit any similar subject, specifics without checkable context, and claims larger than their evidence; human ideation names sources a reader can look up and discusses downsides and open problems. This is the failure "Why Slop Matters" calls superficial competence, measured.

**Why it matters for this skill.** A humanizing pass rewrites the prose and keeps the ideas. IdeaLens shows that a model-generated plan still reads as model-generated after a person writes every sentence, so no amount of tell-removal fixes a piece whose argument came from a model's default. This is the strongest argument in the catalog for the human-touch list.

**Fix.** Ask what the obvious take on the topic is, and whether the draft is it. If it is, the writer needs a position the model would not have produced: a disagreement with the consensus, a case that does not fit, a cost the obvious take ignores. Replace every interchangeable detail with one that could only belong to this subject. Give every number its denominator, source, and date. Then add the downside or the open problem, because a piece with no unsolved part reads as generated at the level of its ideas even when every sentence is clean.

## 81. Staccato line breaks: the dash's replacement

**Looks like.** One-sentence paragraphs, often one-clause paragraphs, where a writer would have used a comma, a dash, or nothing at all.

"He says this not gently.

Not softly.

But harsh, and with threat and purpose."

In explanatory text it shows up as bullets of one or two words each, and as a short line set alone after a long paragraph for emphasis.

**Why it reads as AI.** It is what the dash turned into. When the newer ChatGPT models stopped producing em dashes, users across several independent r/ChatGPT and r/OpenAI threads from mid to late 2026 (one with 1,628 points) reported the same replacement: a new line every time the model would have reached for a dash, which fiction writers call "cinematic micro-beats," plus the observation that custom instructions against it hold for a few paragraphs and then lapse. The measured punctuation profile points the same way. Current models have shorter sentences with less than half the human spread (entry 54), and a line break is the one interruption left once the dash, the semicolon, and the parenthesis are gone. This is practitioner evidence, not a measurement, but it is the most consistently reported formatting change of the period.

**Fix.** Join the fragments back into the sentence they came from: "He said it harshly, with threat and purpose." Keep a standalone line only where the piece has earned a real pause, about once per piece, and never as a run of three. In lists, merge one-word bullets into a sentence.

## 82. Performed pushback

**Looks like.** Agreement, then a caveat aimed at a claim stronger than the one anyone made. "I'd gently push back on one thing." "One honest caveat." "I'll challenge you on one point." "With one distinction: ..." "What I would not do is..." "That word is doing a lot of work here." The pushback is mild, attached to every answer, and abandoned the moment the reader objects (entry 68).

**Why it reads as AI.** It is the most-discussed new chat habit of late 2026. A 366-point, 231-comment r/ChatGPT thread asks why every request, down to dinner plans, draws a warning, and parallel threads in r/ChatGPT and r/ClaudeAI describe the same move in GPT-5.5 and later, GPT-6, and Claude Opus 5 and 5.5. It reads as the model correcting for its reputation for sycophancy by adding disagreement as a garnish, which is why it rebuts things the user never said and why it folds under any pressure. In prose it becomes the reflexive caveat paragraph, and it is close kin to the corrective disclaimer (entry 74) and the rejected alternative nobody proposed (entry 1): all three spend a sentence on a claim nobody advanced.

**Fix.** Keep a disagreement only if it is with something the draft or the reader actually said, and only if the writer would defend it under pushback. State it as a claim with its reason: "The migration will take longer than two weeks, because the schema change locks the orders table." Cut the cushioning (*gently*, *one honest*, *I'd*). If the caveat is too weak to state plainly, it was not a real objection.

---

## When the tells mislead

Every entry above is a signal, not a verdict, and some of the research cuts the other way. Read this before scoring anyone's writing.

- **Plain is not AI.** Liang, Yuksekgonul, Mao, Wu and Zou (Patterns, 2023) ran 91 TOEFL essays through seven detectors: the average false-positive rate was about 61%, and about 98% were flagged by at least one. Simple, constrained phrasing from non-native writers reads as low-perplexity, which is what the detectors flag. Never score short sentences, limited vocabulary, or textbook grammar from a second-language writer as tells. The rhythm and lexical dimensions are the most exposed to this error.
- **Edited is not generated.** Shan, Lee and Hao (2026, preprint) found model-written text has a consistent stylometric footprint across eight models and five domains, but human text a model *edited* does not: it shifts only slightly, mostly in lexical density. A human draft polished by a model will not show the full catalog, and a low ai-smell score does not mean nobody used a model. The score measures how the prose reads, which is the only claim it should make.
- **Vocabulary lists expire.** Juzek and Ward (COLING 2025, and a 2025 follow-up) found neither architecture nor training data explains words like *delve*; human raters in feedback training prefer them, which is how they get in. Lists track a generation of models and its feedback data, so they age. Prefer the term-frequency method in this file over any fixed list, including this one.
- **Experts are the best detector, and they use the whole picture.** Russell, Karpinska and Iyyer (2025) found a majority vote of five frequent LLM users misclassified 1 of 300 articles, beating most commercial detectors, including on paraphrased text. Their stated reasons, by share of explanations: vocabulary (about 53%), predictable structure (about 36%), grammar too clean (about 25%), lack of originality (about 24%), and quotes (about 22%). No single tell carried the decision; clusters did.
- **Voice matching can erase culture.** Agarwal, Naaman and Vashistha (CHI 2025) found AI writing suggestions pulled Indian participants toward Western styles. When matching a writer's voice, keep their regional idiom, references, and register; do not "correct" them toward a neutral default.
- **The famous tells now under-fire on current models.** Graphite tracked eleven well-known tells (*delve*, formulaic closes, hedging, the em dash, and others) across model versions in 2026. Their average strength fell 21% to 53% from each family's earliest to latest model, and GPT-6 Astra used them 29% *less* often than the pre-ChatGPT human writers did. A reviewer scoring a 2026 draft against the 2024 checklist will rate current GPT output as more human than human. That is why the late-2026 entries (74 to 82) and the family table in entry 73 exist, and why the term-frequency method gets more useful with every release.
- **Most single indicators do not generalize.** El Attar, Dönmez, Maurer and Falenska (arXiv 2606.04177, 2026) tested 284 published stylometric indicators across 30 models and 10 domains and found most of them depend on the model or the domain; only lexical richness held across families. Rudnicka and Juzek (arXiv 2608.06589, 2026) found each model keeps a distinct profile, closer to a human idiolect than to one "AI language," with a clear generational break between 2024 and 2026 models. Score clusters, not single hits, and expect the cluster to differ by family.
- **Long words and academic vocabulary flag humans.** Karr, Khvatskii, Hua and Chawla (arXiv 2608.11256, 2026) found commercial detectors flagged 9% to 15% of unedited human abstracts from 2023 to 2025, more in non-STEM fields, and that the scores tracked long-token counts and Academic Word List density. A formal human writer looks like a model to a detector. The lexical dimension here inherits that risk, which is one more reason it is capped.
- **In flagged copy, check the facts.** Russell, Iyyer and colleagues (ACL 2026) estimated about 9% of 186,000 US newspaper articles from summer 2025 were partly or fully AI-generated, rarely disclosed, and concentrated in small outlets and in weather and tech coverage. The study used Pangram's detector and two authors are from Pangram, so read its numbers with that in mind. The editorial point stands either way: where prose reads as generated, verify claims, not just style.

---

## Writing in a language other than English

Every entry above is English. The tells do not translate, and running an English catalog against a Spanish or Korean draft will flag the wrong things and miss the real ones, because each language has its own pre-existing bad register that model output falls into.

What is known so far, and it is thin:

- **Korean, 번역투.** Translationese. English calques and stiff written-register forms in place of native discourse particles.
- **Russian, канцелярит.** Bureaucratic register: the copula `является`, split predicates like `осуществить` where a plain verb exists. Chukovsky named the disease; Ilyakhov's *Пиши, сокращай* is the standard guide against it.
- **Chinese, 公文腔.** Officialese: `进行` plus noun as padding, `予以`, stock openers such as `众所周知`.
- **Vietnamese.** Sino-Vietnamese vocabulary and calque openers (`thực hiện`, `trong trường hợp`) where plain Vietnamese is shorter.
- **Filipino.** Over-formal literary Tagalog and calque openers (`upang`, `sa pamamagitan ng`) where the editorial register is conversational.
- **Korean, measured.** Lee (2026, single-author preprint) ran a morphology-aware excess-vocabulary count over 398,000 Korean journal abstracts: 시사하다 ("suggest") appeared in about 21% of 2026 abstracts against about 5% expected, while the plain 알아보다 ("look into") fell to about a quarter of trend. The shift began in late 2024, a year after the English abstracts in the same papers, and translation does not explain it. The first frequency evidence for a non-English register shift; count morphemes, not words, in agglutinative languages.

- **Chinese, measured.** Peng and colleagues (arXiv 2610.22249, 2026) found five commercial models use 不是X而是Y ("not X but Y") 2.5 to 9.2 times as densely as human writers; 52.8% of 307 annotated uses were grammatical but unneeded, and reward models preferred the construction. Entry 1's context test applies unchanged.
- **Korean poetry, measured.** Park, Yu and Kim (arXiv 2608.28986, Findings of EMNLP 2026) separated model-written Korean poems from human ones on five form-level features, including structural variation, rhythmic irregularity, and how closely orthographic norms are followed, reaching an AUC of 83.6 on seven unseen models including GPT-5.2 and Gemini 3. Model poems are too regular and too correct, which is entry 64 in another language.

The pattern across all five is the same and it is worth naming, because it is the fastest way to build a list for a language not here: **model output lands in whichever register that language already reserves for institutions.** Bureaucratic Russian, official Chinese, translated Korean, formal Tagalog. Ask a native speaker what their language sounds like when a ministry writes it, and that is most of the catalog.

The structural entries transfer better than the lexical ones, which is what the fingerprint research would predict. X-not-Y, the rule of three, the rhetorical wrap-up, signposting, the restatement loop, and the substance failures in entries 58 to 63 are all recognizable in translation. The vocabulary, the punctuation profile, and the formatting tics are not.

For Korean and Chinese there are now community humanizer projects with real use behind them (`im-not-ai` for Korean, `shuorenhua` and `qu-ai-wei` for Chinese, the last of which reconciles three rule sets). Rule packs for the five languages above also exist in `slop-gate` (see the sources table). It is a one-author project rather than a research result, so treat the lists as a place to start and check them against a native speaker.

---

## Term-frequency analysis: how to find tells by counting

Every word list in this catalog is downstream of somebody counting. Kobak counted 14 million abstracts, Liang counted 1.1 million papers, Yakura counted 824,634 podcast episodes, and the *load-bearing* project counts a hundred pull requests a day. None of them started from a list of suspicious words. They measured a frequency against a baseline and read off whatever came out on top, which is how *delve* was found and how *load-bearing* was found.

A list compiled last year is already describing last year's models, while the counting procedure that produced it still works on whatever came out this month. So when a draft matters, run the count rather than only grepping the list.

### The formula

The one the *load-bearing* project publishes is the clearest, and it is the same shape Kobak's excess-vocabulary ratio and the Antislop framework use.

```
                 count_in(w) / N_in
    ratio(w) = ------------------------
               max(count_out(w), 1) / N_out
```

`count_in(w)` is how many times the word appears in the text under test and `N_in` is every word appearance in it. `count_out` and `N_out` are the same two numbers for the baseline. Report it as "N times more frequent than baseline."

Four rules travel with the formula, and each of them is a mistake somebody has already made.

**Rates, not counts.** Divide each side by its own size. The *load-bearing* project shipped the count version first: because the cluster held a fifth of the corpus, dividing its count of a word by the four fifths outside scaled every one of its words down by the same factor of 3.77, and a smaller cluster's by 40. The ranking inside one text survives that error, so it looks fine; the numbers are comparable to nothing.

**The baseline must exclude the text you are testing.** If the draft is inside the baseline, you are comparing it partly against itself, and the effect shrinks by however much of the pool it is.

**Floor the count, and know the floor is a choice.** A word appearing twice can post a huge ratio and mean nothing. The *load-bearing* project started with three floors (45 appearances, 25 documents, 20 distinct accounts) and said outright that the 45 was picked so its title word would clear it; it now uses a single rule, 50 distinct accounts, chosen as the loosest floor at which two fits agree on half their top twenty. Pick a floor, say what it is, and check what a different one would have dropped.

**No probability floor, though.** Do not discard rare words to clean up the list. Rare-but-concentrated is exactly what the count exists to find; *load-bearing* appeared 101 times in five million.

### The distinct-source floor is the good idea

The best rule in that project is the one about *who* used a word rather than how often it appeared:

| word | documents | distinct accounts |
|---|---|---|
| `pullrequest` | 201 | 17 |
| `load-bearing` | 93 | 92 |

Ninety-two people independently reaching for the same phrase is a fact about the language, whereas 201 documents from 17 accounts is one template pasted 201 times. Counting documents cannot separate those two; counting distinct sources does it at a glance.

For a single draft the analogue is dispersion. A word that appears eight times across six sections about six different things is part of the register. A word that appears eight times in one paragraph is one passage. Check where the hits fall before you count them.

### Where the baseline comes from, best first

1. **The writer's own earlier writing.** If a voice sample exists, that is the baseline, and it is better than any public corpus because it answers the question that actually matters: what is this draft doing that this person does not do? It finds the draft's borrowed vocabulary and it finds nothing for the writer's real tics, which is correct, since those are voice.
2. **Any human-written corpus in the same genre.** Their last ten posts, the team's existing docs, the repository's older commit messages.
3. **Published anchors, when there is nothing else.** Weaker, because the genre will not match. The usable one is the *load-bearing* project's live page, which draws any word's weekly history as a rate per million words (`?w=word` links straight to one) and publishes the counts behind it. Cite the date you read it, because the numbers move every week and the method has changed more than once.

### Running it on one draft

```bash
# rate per 1,000 words, draft against baseline, one word at a time
python3 - draft.md baseline.md <<'EOF'
import re, sys, collections
def tf(path):
    w = re.findall(r"[A-Za-z][A-Za-z0-9_/-]*", open(path).read().lower())
    return collections.Counter(w), len(w)
a, na = tf(sys.argv[1]); b, nb = tf(sys.argv[2])
rows = []
for w, c in a.items():
    if c < 3: continue                      # the floor. say what you used.
    r = (c / na) / (max(b[w], 1) / nb)
    rows.append((r, w, c, b[w]))
for r, w, c, o in sorted(rows, reverse=True)[:40]:
    print(f"{r:8.1f}x  {w:<24} {c:>3} in draft, {o:>4} in baseline")
EOF
```

Then read the top of the list and ask, for each word, whether the draft needed it. Do the same for two-word and three-word runs; the Slop Score weights overused trigrams at 15% of its verdict for a reason, and stock phrases show up in bigrams that hide inside ordinary unigrams.

### What it is good for, and what it is not

It finds tells that are on no list, which is the entire argument for running it. It finds the writer's own new tics, which no published list can contain. It is also cheap to run and it leaves an artifact somebody can disagree with, which a judgment call does not.

It does not detect authorship, and the contamination finding above is why: the vocabulary is entering ordinary speech, so a high ratio on a word means the draft leans on the word, not that a model wrote it. It is also blind to structure. A draft can be perfectly ordinary in its word frequencies and be built entirely out of X-not-Y and rule of three, which is the case the structural entries exist for and the reason those carry the most weight in the ai-smell score.

Treat the output as a list of places to look, in the same spirit as the counts below.

---

## Counting instead of guessing

Most of this catalog asks for judgment. These seventeen counts are mechanical, and running them first stops the audit from turning into vibes. They are rules of thumb calibrated by use, not thresholds from a study, so treat a failed count as a place to look rather than a verdict.

| Count | How | Look harder when |
|-------|-----|------------------|
| Term-frequency ratio | The formula in the section above, draft against the writer's own earlier writing or any same-genre human text | Any content word running more than about 5x baseline with at least three hits spread across the draft. Read the top forty and the bigrams, not just the flagged ones |
| Checkable specifics | Numbers, dates, proper nouns, quoted people, named mechanisms, per 100 words | Fewer than 2. Under 1 and the passage is pure abstraction. |
| Rhythm spread | Longest minus shortest sentence in each paragraph, in words | Under 8 words of spread across a whole paragraph. Spread matters; average sentence length does not (entry 54). |
| Mark variety | How many distinct punctuation types appear per 500 words | Three or fewer, or a page built only from periods and commas. |
| Words between marks | Median gap between consecutive punctuation marks, and the longest gap | Any run over about 25 words, or a median that never shifts across paragraphs. |
| Contraction rate | Contractions per 100 words, in anything conversational | Zero, or "it is" and "do not" where speech would contract (entry 64). Current Claude and GPT models contract freely, so a high rate proves nothing; only the zero is informative |
| Quoted voices | People quoted by name | Zero in a piece about what people did or said. |
| Zombie nouns | Words ending `-tion`, `-ment`, `-ance`, `-ity`, `-ness`, per 100 words | More than 4, or 2 in one sentence. |
| Be-verbs | *is, are, was, were, be, been, being*, per 100 words | More than 3, especially with an abstract subject. |
| Ad-words | Adjectives and adverbs, per 100 words | More than 6, or any `-ly` intensifier that can be deleted without changing meaning. |
| Cut-test loss | Delete every sentence that repeats a point already made, then measure | More than 15% of the draft went, which means it was padded. |
| Connective density | Count *because, so, but, unless, which means, even though* per paragraph of argument | Zero in a paragraph that is supposed to reason. |
| Hedge and booster balance | Count hedges (*may, might, appears*) against boosters (*clearly, obviously, undoubtedly, always, never*) | Boosters outnumber hedges in a piece making empirical claims. |
| Attribution | Count claims about the world against named sources | More claims than sources, or a paraphrase whose source has been dropped. |
| Salience and correction flags | Count *matters* (as a verb about importance), *does not establish*, *not simply*, *not automatically*, *should be treated as*, *rather than* | More than one per 500 words, or any "why X matters" heading (entries 74, 75). |
| Costless trade-offs | Count *without sacrificing*, *without losing*, *without compromising*, *without requiring* | Any instance with no cost named anywhere nearby (entry 76). |
| Interrupting punctuation | Count exclamation marks, parentheses, semicolons, and question marks together, per 1,000 words | Zero across a whole piece in a register where a person would use any of them (entry 54). |

The first five counts, in a similar shape, are the basis of Helen Sword's Writer's Diet test, which grades a passage on be-verbs, zombie nouns, prepositions, ad-words, and the waste words *it*, *this*, *that*, and *there*. Her thresholds are calibrated for academic prose and are worth checking against directly.

One trap worth naming: **lexical density is not the target.** Bao et al. found post-ChatGPT abstracts scored *higher* on lexical density (more content words per total words) while becoming *harder* to read, because the connective words went missing. Packing more content words in is how you get an unreadable paragraph. What you want is more checkable specifics and fewer wasted words, with the connective tissue of the argument left intact.

## The human-touch list

The counts above have a ceiling, and it is the ceiling of what a model can know. A pass that removes every tell and adds no substance produces prose that is clean, correct, and still not worth reading. So every audit should end with a short list of places where only the writer can raise the value of the piece, marked in the text or listed by location.

What to flag:

- **A number the writer has and the draft doesn't.** Latency, headcount, dollars, dates, how many times it happened.
- **A named person or a real quote.** The Economist's 2026 analysis found absent quotation is one of the stronger current markers of machine prose, and it is usually the fastest single fix.
- **A first-hand moment.** The meeting where it went wrong, the bug that took a week, what the writer thought at the time and was wrong about.
- **An opinion with a cost.** The place where the draft describes a tradeoff without saying which side the writer takes.
- **The objection with no good answer.** What the smartest skeptic would say, left unresolved on purpose.
- **The thing that is still broken.** Model prose resolves; real accounts leave something open.
- **A concrete example replacing a category.** One customer, one file, one incident, instead of "teams" or "organizations."
- **A joke, an aside, or a piece of local slang** that only this writer would use.
- **A take the default would not produce.** Where the main argument is the obvious one, the place the writer disagrees with it (entry 80).

Frame each one as a question the writer can answer in a sentence ("which two teams stopped holding standups?"), not as an instruction. This list is the part of an audit that most changes the finished piece, and it is the part a tool cannot do for anyone. See "Why Slop Matters" (arXiv 2601.06060) on why: what separates slop from writing is not surface competence but whether any of it required the effort of knowing something, and only the writer holds that.

---

## The final audit question

After any draft, ask honestly: "What would make this so obviously AI-generated?" Name the remaining tells using the vocabulary above. Then revise. If you cannot read a paragraph aloud without hearing the cadence of a model, it still reads as AI.

Then ask the three questions the tell list cannot answer, because a draft can pass every check above and still be empty:

- **What can I cut?** Which sentences repeat a point already made, and which words are load I could drop without losing meaning (entries 19, 58, 59).
- **What here could only have been written by someone who did the work?** Underline every number, name, date, quote, and mechanism. If a paragraph has none, it is decoration (entry 61, and the counts above).
- **Is every claim the size of its evidence?** Check hedges and attributions against the source, and check absolutes against what you have actually verified (entries 60, 61).

Finish with the human-touch list: the two to five places where only the writer can raise the value of the piece.

This is also where both scores get assigned (see the rubrics in `SKILL.md`): the tells named here are the evidence behind them. For ai-smell, structural tells (the top six plus entries 42 to 46, 48 to 50, 53, 55, 59, 74 to 77, and 81) carry the most weight, rhythm and voice next, lexical and formatting tells least. For the reader-value score, entries 58 to 63 and the counts above supply the evidence: 58, 59, and 19 for concision, 60 and 61 for calibration, and the specifics count and entry 80 for substance. Entry 79 is a reader-path failure. Cite the specific instances, then score and revise.

Provenance artifacts (entry 57) sit outside the score entirely. Report them separately.

---

## How the ai-smell score relates to the research

The rubric is a lightweight, prose-specific version of the LLM-as-a-judge methods now standard in NLG evaluation. A few findings shaped how it is scored.

**Reason before you rate, and score per dimension.** G-Eval (Liu et al. 2023) established that an LLM judge aligns with human ratings far better when it generates explicit evaluation steps first and fills in a per-criterion form, rather than emitting one holistic number. That is exactly the order the final pass uses: name the tells, then score each of the five dimensions. Rubric-based analytic scoring beats a single overall grade.

**Guard against judge bias.** Studies of LLM judges document three biases that would wreck an ai-smell score: self-preference or self-enhancement bias (Wataoka et al. 2024), where a model rates text in its own style more favorably; verbosity bias, where longer answers score higher; and position bias (Shi et al. 2024). Self-preference is the dangerous one here, because the judge and the writer are the same kind of model, so the judge is partly blind to its own tics. The scoring rules counter it directly: score as a hostile skeptic, and never reward length or fluency.

**The lexical dimension has an empirical backbone.** Kobak et al. (2024) measured "excess vocabulary" across 14 million PubMed abstracts and showed that words like *delve*, *underscore*, and *showcase* spiked after ChatGPT, an effect larger than the Covid pandemic left on scientific prose. Word-frequency tells are not folklore; they are measurable.

**Rhythm is real but never decisive.** Burstiness (variation in sentence-level surprise) underlies the classic detectors DetectGPT, Fast-DetectGPT, and Binoculars (Hans et al. 2024). But Pangram Labs and others show low burstiness alone misfires badly: it flags plain human prose, famous documents, and non-native English writers. So uniform rhythm is one dimension of five, never a verdict on its own. This is why the score stays inside the pass and is never presented as proof of authorship.

**What the punctuation research actually supports.** Punctuation is a real stylometric feature family, not folklore: Kumarage et al. (2023) build a detector on phraseology, punctuation, and linguistic diversity, where the punctuation features are total mark count and the mean count of specific marks (`!`, `'`, `,`, `:`, `;`, `?`, `"`, `-`, `@`, `#`), and report that adding them improves state-of-the-art classifiers. But the useful findings are about distributions rather than individual marks. Terčon and Dobrovoljc's survey reports that AI text draws on a narrower set of marks, with commas and periods dominating, and uses fewer commas, question marks, dashes, parentheses, semicolons, and colons than human text. It also reports that sentence-length *variation* is consistently lower in AI text while average sentence length shows no consensus across studies, which means variance is the signal and the mean is noise. Stanisz, Kwapień, and Drożdż add a third layer by measuring the gaps between consecutive marks in words, finding a discrete Weibull distribution with an always-increasing hazard function whose parameters separate languages, authors, and translations; that work is aimed at language universals rather than detection, so it belongs in an audit as a lens rather than a test.

The counterweight matters as much as the findings. The em dash was the most confident punctuation claim of 2025 and it did not survive contact with data (entry 23). Educators have started arguing that punctuation heuristics should be dropped entirely, because the cost falls on writers who punctuate carefully and on students whose polished work now draws suspicion, and because the heuristics survive on being easy to apply rather than on being accurate. That is why punctuation lives inside one capped dimension of the ai-smell score, is scored on variety and spread rather than on counts, and never functions as a verdict about authorship.

**Surface markers rotate; structure does not.** Two 2026 findings make this concrete. The Economist's comparison of 1.2 million words of its own prose against four frontier models found the em dash has stopped working as a marker (only Claude overuses it) and that punctuation *sparseness* now separates the sets better, because models write longer sentences, lean on "and," and do not quote people. Forbes's May 2026 roundup shows the vocabulary layer moving the same way: the delve-and-tapestry set has been scrubbed out of a lot of writing and replaced by plain words used abstractly (quietly, shift, matters, land, real, earn, compound, signal). Anything word-level or punctuation-level in this catalog should be treated as dated on arrival and rechecked. Sarvazyan et al. (2025) is the counterweight: structural and syntactic fingerprints persist across domains and survive paraphrase, which is why the rubric weights structural tics highest.

**The tells are now per family, and they are measured at scale.** Graphite's 2026 study (Druck, Paredes and Smith) is the largest current-model measurement there is: 10,000 pre-ChatGPT human web articles from Common Crawl, and 10,000 matched articles from each of nine models (GPT-4.1 through GPT-6 Astra, Claude Opus 4 through Opus 5, Gemini 2.5 and 3.1 Pro), each written from a summary of the human article at the same length, plus an October update adding Claude Opus 5.5. A tell is any word, phrase, or gapped frame used at least twice the human rate above a distinct-article floor, which is this catalog's term-frequency method with a bigger corpus. It found 12,877 of them. Four findings changed this catalog. 65% of tells belong to one family, and 55% to 72% to one version, so a single list cannot cover current text. The well-known tells are fading, to the point that GPT-6 Astra uses them less than humans did. What replaced them is consistent across families: salience flags (entry 75), corrective framing (74), costless trade-offs (76), synthesis transitions (77), and mannered prose (78). And em dashes have nearly vanished from two of the three families (entry 23). The study is from a company that sells content services and used a single prompt on web-article topics, and its authors say outright that the tells are not for classifying individual documents. Its data is published, which is what makes it usable.

**Ideas carry the signal after the words are gone.** Two 2026 papers from the same lab moved the measurement from prose to content. *Argument Collapse* (Kim, Chang, Pham and Iyyer) found model essays on public debates converge on the same few main arguments, 3.4% unique within a debate against 65.3% for humans. IdeaLens (Rajendhran, Iyyer and colleagues) detects AI-originated ideas from outlines with the wording stripped out, and it flagged 68% of stories that people wrote by hand from AI plans, against 8% for a prose detector. For an editing skill that is the hardest finding in this file: a humanizing pass can remove every tell in the prose and leave the piece reading as generated at the level of its ideas. Entry 80 carries it, and it is the reason the human-touch list asks for positions and downsides, not just numbers.

**Why the agent register exists, according to the people measuring readability.** Clark, Martin and Mahowald (2026) found all nine models they tested used more inanimate subjects with animate verbs and more rare word sequences than human writers, and most packed in longer dependencies and stacked nouns. Their hypothesis is that training for math, code, and reasoning rewards information density over communication. It is the first account of entry 67 that explains the mechanism behind the symptom, and it predicts the register will spread to whatever genre a reasoning-trained model writes next.

**The vocabulary can be watched in the open, in something other than abstracts.** The Kobak measurement above ran on PubMed; the *load-bearing* project runs the same idea on GitHub, and continuously. It samples newly opened pull request descriptions daily, drops accounts that are not people, and fits ten KL-divergence k-means clusters over word counts with no time parameter in the model at all, so the weekly curves are counts of documents rather than fitted trends. One cluster went from about 1% of the corpus in January 2025 to 39.5% of the four weeks ending 2026-11-02 and is still rising. Four things make it worth carrying here. It is a measurement of a *register* rather than of a word list, which is the level the catalog has been arguing matters. Its top word through the summer was already entry 48. It publishes its own arbitrary choices, which is the honesty the other word-frequency sources mostly skip. And it caught a model release in the act: in the week Claude Opus 5.5 shipped, the cluster kept growing while *load-bearing*, *genuinely*, and *deliberately* fell by 75% to 90%, which is the clearest evidence anywhere that a word list is a snapshot of one model version. Entry 67 carries the findings and the caveats.

**Narrative shape is its own signal.** StoryScope (Russell et al. 2026) analyzed 61,608 stories on discourse-level features rather than style and hit 93.2% separation between human and AI narratives, with about 30 features carrying most of it. AI stories over-explain their themes and run tidy single-track plots; human ones keep ambiguity and temporal mess. That result is why entry 55 exists and why the fix for a flat anecdote is structural, not lexical.

**The vocabulary is leaking into speech, which caps what any word list can prove.** Yakura et al. (arXiv 2409.01754) measured ChatGPT-preferred words in 737,083 hours of unscripted conversation across 824,634 podcast episodes and found an abrupt post-release rise in spontaneous speech, causally linked by synthetic control. Anderson, Galpin, and Juzek (arXiv 2508.00238) replicate the direction on 22.1 million words of unscripted speech but find the effect smaller and patchier, with *delve* not significantly up. Read together they say the same thing to an auditor: the words are entering the language, so a human writer using them is now an ordinary event rather than evidence. This is the strongest argument in the research for keeping the lexical dimension capped and structure weighted highest, and for never reporting a word-frequency hit as an authorship finding.

**Slop is a measurable construct, and it lands on the substance axis.** Shaib et al. (arXiv 2509.19163) built a taxonomy of slop from interviews with NLP researchers, writers, and philosophers, turned it into interpretable dimensions, and had annotators mark it at the span level rather than judging whole documents. Two results matter here. Binary slop judgments are somewhat subjective, so a single number should never be presented as fact, which is why both rubrics require cited instances. And those judgments correlate with latent dimensions like coherence and relevance rather than with surface polish, which is independent support for scoring reader-value separately from ai-smell. The span-level method is also the right one: mark the passage, then score, never the reverse.

**Voice loss is measured, not just asserted.** Abdulhai et al. (arXiv 2603.18161, March 2026) combined a user study, model-revised 2021 essays written before LLMs existed, and AI-generated conference peer reviews. Heavy LLM users produced essays about 70% more likely to stay neutral on the question they were answering; users reported losing creativity and voice; and models altered semantic meaning even when asked for grammar-only edits. That last finding is the operational one for this skill, because a humanizing pass is exactly a "surface only" edit, and it is evidence that no such edit stays on the surface. It is also the empirical backbone for the voice-and-stance dimension: refusing to land a position is not a matter of taste, it is the measured signature of heavy model involvement.

**The deeper mechanism is homogenization.** Work on shrinking linguistic diversity (arxiv 2502.11266) and on instruction-tuning reducing lexical variety shows LLMs converge toward a low-diversity mean. AI-smell is the surface of that convergence, which is why the fix is always the same: reintroduce specificity, variation, and a point of view.

**Padding is a trained behavior, so it can be trained out.** Reward models used in RLHF learn that longer answers score better, and LLM judges pick the longer response far more often than human raters do on open-ended tasks. YapBench turns that into a measurement by scoring each response against the shortest sufficient answer, and its result is the useful one for editing: GPT-3.5-Turbo is more concise than several newer frontier models, so verbosity tracks post-training choices rather than capability. Practically, this means padding is the most reliably removable defect in a draft. It is also the one an LLM judge is least likely to penalize on its own, which is why the cut test is mechanical here instead of left to judgment.

**Certainty is the newest measurable failure, and it runs opposite to the old one.** Belem et al. (2026) found that rewriting distorts expressed certainty in up to 75% of outputs, with a 1.5 to 2 times bias toward raising it, compounding across passes and worsening under greedy decoding. Hagar et al. (2025) name the three shapes it takes in summarization: attribution stripping, overinterpretation, and certainty inflation. This matters for a humanizing pass specifically, because every rewrite is another chance to inflate. An edit that removes hedges to tighten a sentence can make the sentence false while making it read better, so calibration has to be checked against the source rather than against the previous draft.

**Refresh the word lists by computation, not memory.** The Antislop framework (2025) builds its lists by profiling model output against human baselines and finds patterns appearing over 1,000 times more often in LLM text than in human writing, then suppresses more than 8,000 of them at inference; token banning alone breaks down past about 2,000. The related Slop Score weights its verdict 60% overused words, 25% not-X-but-Y constructions, and 15% overused trigrams, with the lists computed from ten models against human corpora. Two things follow. Any word list in this catalog is a snapshot, and the method that produced it is the durable part. And the independent weighting is a useful check on this one: a tool built from measurement, with no knowledge of this catalog, puts a quarter of its score on the same construction that sits at entry 1.

**What separates slop from writing is not surface quality.** "Why Slop Matters" (arXiv 2601.06060, ACM AI Letters) characterizes slop through three prototypical properties: superficial competence, where the veneer of quality hides an absence of substance; asymmetric effort, where the output took far less work than it appears to have taken; and mass producibility. The first property is the one that should shape an audit. Removing tells raises surface competence, which is exactly the axis that was never the problem. This is the argument for scoring substance separately from ai-smell, and for ending every pass with a list of the things only the writer can add.

---

## Reference

This catalog builds on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup), whose patterns come from observing thousands of instances of AI-generated text on Wikipedia. Key insight from that page: language models guess what should come next, and the result tends toward the most statistically likely phrasing that fits the widest range of cases. That is exactly what makes the output sound generic, and exactly what this skill works against.

### Other sources worth consulting

These are descriptive field guides, not detectors. No single pattern proves AI authorship; clusters of weak signals matter more than any one hit. Automated tools (GPTZero, Turnitin, Originality.ai) are unreliable on their own; Wikipedia's guide explicitly warns against relying on them.

| Source | URL | What it adds |
|--------|-----|--------------|
| Wikipedia: Signs of AI writing | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | Primary catalog: content inflation, formatting, negative parallelisms, AI vocabulary, challenges sections |
| WikiProject AI Cleanup / Guide | https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide | How editors find and fix AI content; sourcing and cleanup workflow |
| GPTZero AI Vocabulary | https://gptzero.me/news/most-common-ai-vocabulary/ | Statistical word-frequency list from millions of comparisons; updated periodically |
| Pangram Labs guide | https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns | Rhythm (low burstiness), em dashes, uniform paragraphs, "Overall"/"In conclusion" closers |
| Google Cloud statistical tells | https://medium.com/google-cloud/detecting-ai-generated-text-by-uncovering-its-statistical-tells-042c8d0e3a24 | Signposting, authoritative qualifiers, sycophantic openers; measured with log-likelihood ratios |
| VU Amsterdam ALP Guide | https://vu.nl/en/about-vu/more-about/alp-guide-spotting-ai-writing | Academic framing: boosters vs. hedges, bland style, overly poetic language, low perplexity |
| Sarvazyan et al. 2025 (ACL) | https://aclanthology.org/2025.genaidetect-1.6/ | LLMs leave persistent lexical/syntactic fingerprints; structural tells outlast individual words |
| OpenAI community thread | https://community.openai.com/t/what-are-your-strategies-for-spotting-ai-writing/1150515 | Practitioner discussion; emphasizes structural joints over word lists |
| Embryo cross-model word list | https://embryo.com/blog/list-words-ai-overuses/ | Aggregated overuse list across ChatGPT, Claude, Gemini, etc. |
| no-ai-slop (Peter Yang) | https://github.com/petergyang/no-ai-slop | Detect-vs-edit split, minimum-effective-edit principle, colon reveals, throat-clearing openers, banned intensifier list |
| deslop (Stephen Turner) | https://blog.stephenturner.us/p/deslop | Dramatic-pause directives ("let that sink in"), scoring rubric, calibrating edit aggressiveness to how voice-critical the piece is |
| G-Eval: NLG evaluation with GPT-4 (Liu et al. 2023) | https://arxiv.org/abs/2303.16634 | Rubric-based LLM-as-a-judge: reason via chain-of-thought first, then form-fill per-dimension scores. Basis for the score's reason-then-rate order |
| Self-Preference Bias in LLM-as-a-Judge (Wataoka et al. 2024) | https://arxiv.org/abs/2410.21819 | Judges favor text in their own style; grounds the "score as a skeptic" rule |
| Position bias in LLM-as-a-Judge (Shi et al. 2024) | https://arxiv.org/abs/2406.07791 | Systematic study of position and verbosity bias in LLM judges |
| Excess vocabulary in academic writing (Kobak et al. 2024) | https://arxiv.org/abs/2406.07016 | Data-driven measurement of LLM word overuse (*delve, underscore*) across 14M abstracts; empirical basis for the lexical dimension |
| Binoculars: zero-shot LLM detection (Hans et al. 2024) | https://arxiv.org/abs/2401.12070 | Perplexity/cross-perplexity detection; the burstiness signal behind the rhythm dimension |
| Why perplexity and burstiness fail (Pangram Labs) | https://www.pangram.com/blog/why-perplexity-and-burstiness-fail-to-detect-ai | Limits of statistical signals: false positives on plain and non-native prose; why rhythm is never decisive alone |
| Shrinking Landscape of Linguistic Diversity (2025) | https://arxiv.org/abs/2502.11266 | LLM adoption reduces stylistic diversity; the homogenization the whole skill works against |
| The Economist on spotting AI writing (2026) | https://www.fastcompany.com/91584243/how-to-identify-ai-generated-writing-viral-report-has-surprising-new-clues-economist | 55,940 sentences, 1.2M words vs. four frontier models. Em dashes no longer diagnostic (only Claude overuses); models use fewer commas, semicolons, parentheses, write longer sentences, overuse "and," don't quote people. Basis for entry 54 and the caveat in entry 23 |
| Forbes: 15 new giveaway signs of AI writing (May 2026) | https://www.forbes.com/sites/jodiecook/2026/05/21/15-new-giveaway-signs-of-ai-writing-may-2026-update/ | The post-delve vocabulary: quietly, shift, matters, shape, land, actually, real, earn, the work, hold, pull, compound, signal, built different. Feeds entries 10 and 47 |
| The load-bearing vocabulary of Claude (Louis Abraham, 2026) | https://louisabraham.github.io/load-bearing/ | 531,322 GitHub PR descriptions sampled daily since Jan 2025 (as of 2026-11-10), clustered by KL-divergence k-means with no time parameter. One way of writing grew from ~1% to 39.5% of the corpus; *load-bearing* led its vocabulary until the week Claude Opus 5.5 shipped, then fell to 249th as *refused*, *says*, and *nobody* rose. Code, data, and the arbitrary choices at https://github.com/louisabraham/load-bearing. Basis for entry 67, and the measurement behind entries 47 and 48 |
| StoryScope: idiosyncrasies in AI fiction (Russell et al. 2026) | https://arxiv.org/abs/2604.03136 | 61,608 stories scored on discourse-level narrative features; 93.2% human/AI separation from narrative shape alone. AI over-explains themes and favors tidy single-track plots. Basis for entry 55 |
| Linguistic Characteristics of AI-Generated Text: A Survey (Terčon & Dobrovoljc 2025) | https://arxiv.org/abs/2510.05136 | Synthesis of the measurement literature. AI text is more nominal and impersonal: more nouns, determiners, and prepositions, fewer adjectives and adverbs, lower lexical diversity. Basis for entry 58 |
| Linguistic shifts in academic writing after ChatGPT (Bao et al. 2025) | https://arxiv.org/abs/2505.12218 | 823,798 arXiv abstracts. More LLM-preferred words and higher lexical density, but simpler syntax, fewer connectives, more positive sentiment, and lower readability. Basis for entries 61 and 63, and for the warning that lexical density is not the target |
| From "May" to "Is": certainty distortion in LM rewriting (Belem et al. 2026) | https://arxiv.org/abs/2606.07951 | Rewriting shifts expressed certainty in up to 75% of outputs, biased 1.5 to 2 times toward more confidence, compounding across passes. Basis for entry 60 and the calibration dimension |
| Not Wrong, But Untrue (Hagar et al. 2025) | https://arxiv.org/abs/2509.25498 | Three named failure modes in document-grounded generation: attribution stripping, overinterpretation, certainty inflation. The editing vocabulary for entry 60 |
| Why Slop Matters (2026) | https://arxiv.org/abs/2601.06060 | Defines slop by superficial competence, asymmetric effort, and mass producibility. The argument for scoring substance separately from surface tells |
| Antislop framework (2025) | https://arxiv.org/abs/2510.15061 | Computes overused patterns against human baselines (some appear 1,000 times more often), suppresses 8,000+ at inference. The method for keeping word lists current |
| Slop Score and slop-forensics (Sam Paech) | https://eqbench.com/slop-score.html | Weights its score 60% overused words, 25% not-X-but-Y, 15% overused trigrams, all computed from ten models against human corpora. Independent confirmation of entry 1's weight |
| YapBench (2026) | https://arxiv.org/abs/2601.00624 | Scores responses against the shortest sufficient answer. Newer frontier models pad more than GPT-3.5-Turbo, so verbosity is a post-training behavior. Basis for entry 59 |
| ai-pattern-detection (halans) | https://github.com/halans/ai-pattern-detection | 46 regex patterns in six weighted severity tiers, summed and normalized to 0-100. A working example of the weighted-rubric approach, and a useful cross-check on tier weights |
| Stylometric detection of AI text (Kumarage et al. 2023) | https://arxiv.org/abs/2303.03697 | Punctuation as one of three stylometric feature families (with phraseology and lexical diversity); mark counts measurably improve SOTA detectors. Basis for entry 54 |
| Universal versus system-specific punctuation patterns (Stanisz, Kwapień & Drożdż) | https://arxiv.org/abs/2212.11182 | Gaps between punctuation marks, in words, follow a discrete Weibull distribution with increasing hazard; two parameters separate languages and authors. The words-between-marks rhythm in entry 54 |
| Punctuation patterns in Finnegans Wake are largely translation-invariant (2025) | https://arxiv.org/abs/2501.12954 | Same method applied to experimental literature and translations. Useful for how far a real human writer can sit from the norm without being an outlier |
| How well do LLMs imitate human writing style? (Jemama & Kumar 2025) | https://arxiv.org/abs/2509.24930 | Punctuation ranked among the most diagnostic style features; models under-use commas, apostrophes, hyphens, and exclamation marks. Feeds entries 54 and 64 |
| Comparing LLM and human news text with formal syntactic theory (2025) | https://arxiv.org/abs/2506.01407 | Humans use contractions, colloquialisms, and rarer constructions more; model output reads as an averaged grammatical profile. Basis for entry 64 |
| Stop policing punctuation (AARE 2026) | https://blog.aare.edu.au/stop-policing-punctuation-now-why-ai-detection-needs-a-rethink/ | The case against punctuation heuristics: they persist because they are easy, and the cost lands on careful writers. Why punctuation is scored but never decisive |
| The Writer's Diet (Helen Sword) | https://writersdiet.com | Grades prose on be-verbs, zombie nouns, prepositions, ad-words, and the waste words it/this/that/there. Source of the mechanical counts and the "zombie noun" name |
| Reuters Institute: how AI prose diverges from human writing | https://reutersinstitute.politics.ox.ac.uk/news/how-ai-generated-prose-diverges-human-writing-and-why-it-matters | Juzek & Ward on focal words, Rudnicka on formality, Mahadevan on "a lot of words that don't say anything" and show-don't-tell. Journalism framing for the substance dimension |
| AI's hyperbole is making abstracts harder to read (THE, on Bao et al.) | https://www.timeshighereducation.com/news/ais-hyperbole-making-journal-abstracts-harder-read | Plain-language account of the hyperbole and readability findings, with the specific adjectives that rose about 40% |
| Quantifying LLM usage in scientific papers (Liang et al. 2025) | https://www.nature.com/articles/s41562-025-02273-8 | *Nature Human Behaviour*. 1,121,912 papers and preprints, 2020 to 2024, estimating LLM-modified text from population-level word-frequency shifts: up to 22% in computer science, about 9% in mathematics and the Nature portfolio, and higher for short papers in crowded areas. The method companion to Kobak, and the reason entry 10 is framed as frequency rather than as a blacklist |
| LLM influence on human spoken communication (Yakura et al. 2024) | https://arxiv.org/abs/2409.01754 | 737,083 hours of conversation across 824,634 podcast episodes. ChatGPT-preferred words rose abruptly in *spontaneous speech* after release, tied to it by synthetic control. The contamination caveat on every word list in this catalog |
| Traces of AI-associated language in unscripted spoken English (Anderson, Galpin & Juzek 2025) | https://arxiv.org/abs/2508.00238 | 22.1M words of unscripted speech. Replicates the direction of the Yakura result but finds it smaller and uneven, with *delve* not significantly up. The counterweight that keeps the lexical dimension capped |
| Measuring AI "Slop" in Text (Shaib et al. 2025) | https://arxiv.org/abs/2509.19163 | Taxonomy of slop from expert interviews, turned into interpretable dimensions and annotated at the span level. Slop judgments are partly subjective but correlate with coherence and relevance rather than polish. Independent support for the reader-value score and for cite-the-span scoring |
| How LLMs Distort Our Written Language (Abdulhai et al. 2026) | https://arxiv.org/abs/2603.18161 | User study plus model-revised pre-LLM essays plus AI-written peer reviews. Heavy LLM users' essays were ~70% more likely to stay neutral; models changed meaning even under grammar-only instructions. Empirical basis for the voice-and-stance dimension, and a warning that no rewrite is surface-only |
| People who frequently use ChatGPT are accurate detectors (Russell et al. 2025) | https://arxiv.org/abs/2501.15654 | Expert detectors ranked by the tells they cite; stock names; quote placement. Entries 69 and 70 |
| LAMP corpus: Can AI writing be salvaged? (Chakrabarty et al., CHI 2025) | https://arxiv.org/abs/2409.14509 | Professional-writer edit taxonomy with shares per category. Entry 71 |
| Do LLMs write like humans? (Reinhart et al., PNAS 2025) | https://arxiv.org/abs/2410.16107 | Grammatical feature rates, participles and nominalizations. Entry 72 |
| ELEPHANT (Cheng et al. 2025) | https://arxiv.org/abs/2505.13995 | Measured sycophancy: validation, indirectness, premise acceptance. Entry 68 |
| Idiosyncrasies in LLMs (Sun et al., ICML 2025) | https://arxiv.org/abs/2502.12150 | Per-family openers and markdown fingerprints. Entry 73 |
| AI-modified peer reviews (Liang et al., ICML 2024) | https://arxiv.org/abs/2403.07183 | Peer-review vocabulary: commendable, meticulous, intricate. Entry 10 |
| GPT detectors biased against non-native writers (Liang et al. 2023) | https://arxiv.org/abs/2304.02819 | False-positive guardrail. When the tells mislead |
| AI editors have no consistent footprint (Shan et al. 2026) | https://arxiv.org/abs/2608.27855 | Edited text differs from generated text. When the tells mislead |
| Why does ChatGPT "delve" so much? (Juzek & Ward 2025) | https://arxiv.org/abs/2412.11385 | Feedback training explains overused words; lists age. When the tells mislead |
| AI use in American newspapers (Russell et al., ACL 2026) | https://arxiv.org/abs/2510.18774 | Journalism prevalence; check facts in flagged copy. Vendor co-authors. When the tells mislead |
| AI suggestions homogenize writing (Agarwal et al., CHI 2025) | https://arxiv.org/abs/2409.11360 | Cultural flattening; keep idiom when matching voice. When the tells mislead |
| Korean register shift (Lee 2026) | https://arxiv.org/abs/2609.07447 | Morphology-aware excess vocabulary for Korean. Non-English section |
| AI Tells (Graphite, Druck, Paredes & Smith, Sept 2026) | https://graphite.io/five-percent/research/ai-tells | 10,000 pre-ChatGPT human articles against 10,000 matched articles from each of nine models. 12,877 tells at 2x human or more; 65% unique to one family; per-family tables; em-dash and punctuation features; mannered-prose scores. Data downloadable. Basis for entries 74 to 78 and the family table in 73 |
| AI Tells: Opus 5.5 Update (Graphite, Oct 2026) | https://graphite.io/five-percent/research/ai-tells-opus-5-5-update | Opus 5.5 em dashes down 99% from Opus 5 (2.92 to 0.015 per 1,000 words), mannered prose down 37%, word distribution 19% closer to human, still 2,548 tells. *this matters* at 116x, *dependable* at 23x |
| Wikipedia: Signs of AI writing, 2026 revisions | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | Corrective framings dated to mid-2026 and GPT-5.6; identification-by-source phrasing; GPT-6 era vocabulary; em dashes moved to "Historical indicators" (2022 to September 2026); "preserved/retained" edit summaries. Entries 5, 10, 23, 30, 74, 79 |
| Anthropic says it fixed Claude's writing (Arize, Sept 2026) | https://arize.com/blog/anthropic-says-it-fixed-claudes-writing/ | 80 posts from 20 frozen briefs, Opus 5 against Opus 5.5, human-calibrated span judge. "Claudisms" halved (4.79 to 2.38 per 1,000 words); salience flags still the most common; bold lead-in bullets up 2.5x, three-part lists up 35%; "earns its counter space" survives. Entries 73, 75, 78 |
| Can Pangram detect GPT-6.1 Sol? (Pangram, Nov 2026) | https://www.pangram.com/blog/can-pangram-detect-gpt-6-1-sol | 2,215 Sol answers to LMSYS prompts. Curly apostrophes in 73.9% (Claude Haiku 5.5: 0%), em dash in 29.7%, en dash in 11.4%; Mara/Maya Vale and Daniel; "The first..." openers. Vendor blog. Entries 23, 28, 69 |
| Claudish (slhck, June 2026) | https://slhck.info/software/2026/06/22/claudish.html | Three levels of Claude's accent: stock phrasings, compressed jargon, and revisions written as diffs for a reader who saw v1. Practitioner observation, no counts. Entries 67, 79 |
| IdeaLens (Rajendhran, Iyyer et al. 2026) | https://arxiv.org/abs/2610.06778 | Detects AI-originated ideas from discourse-role outlines with the wording removed. Flags 68% of human-written stories built from AI plans, against 8% for a prose detector. Entry 80 |
| Argument Collapse (Kim, Chang, Pham & Iyyer 2026) | https://arxiv.org/abs/2606.01736 | 23,381 model essays against 1,487 human debate responses. Unique main arguments 3.4% against 65.3%; diversity prompting recovers about half. Entry 80 |
| Why is AI-generated language so hard to understand? (Clark, Martin & Mahowald 2026) | https://arxiv.org/abs/2610.29162 | Nine models all over-use inanimate subjects with animate verbs and rare n-grams; density training as the cause. Entry 67 |
| Not X, but When (Peng et al. 2026) | https://arxiv.org/abs/2610.22249 | Mandarin 不是X而是Y at 2.5 to 9.2 times human density; 52.8% of uses correct but unneeded; reward models prefer it. Entry 1, non-English section |
| Artificial Epanorthosis (Boggia 2026) | https://arxiv.org/abs/2607.21498 | "Not X but Y" over-used in oratory and abstracts, under-used in casual Q&A and narrative; small samples. Entry 1 |
| Beyond "AI Language" (Rudnicka & Juzek 2026) | https://arxiv.org/abs/2608.06589 | Same prompts, 2024 against 2026 model cohorts. Generational style break; negation contractions about 32 times as common in 2026; per-model idiolects. Entries 64, 73 |
| Most biomedical publications show signs of LLM-assisted writing (Holzwarth, González-Márquez & Kobak 2026) | https://arxiv.org/abs/2608.10715 | 1,194,287 PMC full texts; 89% show excess LLM vocabulary by December 2025. Entry 10 |
| Engineering writing after chat assistants (Cokyasar 2026) | https://arxiv.org/abs/2611.11174 | 1.8M engineering abstracts. LLM words up 82%, hedges down 13%, boosters up 20%. Entry 20 |
| The em-dash em-beds in Congress (Czuma 2026) | https://arxiv.org/abs/2608.05889 | 146,239 congressional press releases; em-dash density roughly doubled in 2025. Exploratory. Entry 23 |
| Generalizability of stylometric indicators (El Attar et al. 2026) | https://arxiv.org/abs/2606.04177 | 284 indicators, 30 models, 10 domains; most are model- or domain-dependent, only lexical richness holds. When the tells mislead |
| Why AI detection fails for academic integrity (Karr et al. 2026) | https://arxiv.org/abs/2608.11256 | Human abstracts flagged 9% to 15%; scores track long words and academic vocabulary. When the tells mislead |
| Form-level features of Korean LLM poetry (Park, Yu & Kim, EMNLP Findings 2026) | https://arxiv.org/abs/2608.28986 | Too-regular, too-correct form separates model poems. Non-English section |
| EQ-Bench Creative Writing slop scores | https://eqbench.com/creative_writing.html | Per-model slop scores and over-used fiction phrases, updated as models ship. Claude 5 family: "like a held breath," "for a long moment"; Gemini 3: "heart hammering against his ribs." Entry 71 |
| Reddit practitioner threads, July to November 2026 | https://old.reddit.com/r/ChatGPT/comments/1vlddcq/ (formats readers can no longer stand, 742 points), https://old.reddit.com/r/ChatGPT/comments/1xahk2m/ (reflexive pushback, 366 points), https://old.reddit.com/r/ClaudeAI/comments/1vrlrud/ (Claude-isms mined from transcripts, 811 points), https://old.reddit.com/r/ChatGPT/comments/1wd56qb/ (line breaks for dashes) | Anecdote, but heavily corroborated across threads. Line breaks replacing the dash, performed pushback, instant concession, the self-interview fragment, "No X. No Y. Just Z.", binary-choice closers. Entries 12, 29, 41, 67, 68, 81, 82 |
| Em dash vs 163M Reddit posts (KissMyPost, 2026) | https://old.reddit.com/r/ChatGPT/comments/1xe8ink/ | 10.9M long posts and 152M long comments, 2021 to 2026: em dash 7x the 2021 level in 2026 after a 30% dip; *quietly* up 3.7x; *delve* back to baseline. Posted by the developer of an analytics product; CSVs linked. Entries 10, 23 |
| vale-ai-tells (tbhb) | https://github.com/tbhb/vale-ai-tells | Vale style package with rules for the agent register: inanimate subjects with bare verbs, pseudo-clefts ("what changed is the direction"), shell-noun copulas ("the problem is that"), survival and motion metaphors, *earns*. The closest linter to entry 67 |
| avoid-ai-writing (conorbronsdon) | https://github.com/conorbronsdon/avoid-ai-writing | Audit-and-rewrite skill with a corpus-backed CI gate; "performed insight" and crowd-contrast teasers; flags negative parallelism only at density |
| awesome-slop (index) | https://github.com/hwajongpark/awesome-slop | Small but current index of slop research, linters, classifiers, humanizers, and word lists, organized by language. Useful as a survey of what exists; not itself a source |
| slop-gate | https://github.com/hwajongpark/slop-gate | Zero-dependency CLI that flags the em dash and about 40 English tells in CI, with opt-in translationese rule packs for Korean, Russian, Chinese, Vietnamese, and Filipino. The only pointer here for non-English tells; a one-author project, so treat the packs as a starting list |
