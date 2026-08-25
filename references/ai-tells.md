# AI writing tells: the full catalog

This is the working catalog of patterns that flag prose as AI-generated. It merges the humanizer skill (drawn from Wikipedia's "Signs of AI writing," maintained by WikiProject AI Cleanup) with additional patterns observed in long-form drafting. Each entry has the pattern, why it reads as AI, and how to fix it. The list is a living artifact. If you find a new tell, add it.

The first six are the ones that show up most. Hunt them first.

## Hunt these first (top six)

1. **The X-not-Y construction**: contrast through negation
2. **The contrast-flip couplet**: two short sentences, second inverts the first
3. **The rhetorical wrap-up**: fake mic-drop closer
4. **Dead metaphor stacks**: travel (journey, arc, path), structural (load-bearing, foundation, thread, levers), doors (opens the door, unlocks, paves the way)
5. **Signposting and announcements**: "Let's dive in," "Here's what you need to know"
6. **Rule of three**: forced triplets

Scan next: significance inflation, superficial `-ing` endings, fragmented headers, structural and door metaphors (load-bearing, threads, opens the door), imperative closers, AI vocabulary clusters.

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

---

## 1. The X-not-Y construction

*Top-six tell (#1).*

**Looks like.** A declarative sentence followed by a contrasting negation. "Good writing is a habit, not a talent." "It's not a checklist. It's a way of thinking."

**Why it reads as AI.** The pattern adds emphasis through opposition rather than substance. Once it lands. Three times in a piece it is a rhetorical tic. The contrast is doing the work of conviction.

**Variants.** "It's not just X, it's Y." "Not X. Y." "It's not about X. It's about Y." "Rather than X, Y" when X and Y aren't actually being weighed. Tailing negations: "The form fills itself in, no guessing." See also the "it was never X, it is Y" false-depth reveal (entry 42).

**Fix.** Say what the thing is. Trust the reader to register the contrast. If the contrast is essential, give the opposing case its own sentence and develop it.

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

**Fix.** Replace the list with one specific, sourced instance. "In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods."

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

**Why it reads as AI.** Frequency. Each word in isolation is fine. A cluster of them in one piece is the giveaway. They co-occur. The vocabulary also rotates as models change and as writers learn to avoid the flagged words, so treat any watch-list as dated and check the current one.

**Fix.** Use the plain word. Delve becomes look at. Navigate becomes work through. Intricate becomes detailed. Underscore becomes show. Robust becomes reliable or thorough. Leverage becomes use.

## 11. Copula avoidance

**Looks like.** Substituting elaborate verbs for is/are/has. "The gallery serves as the city's main exhibition space." "The report represents a summary of the findings." "The team boasts twelve engineers."

**Why it reads as AI.** The model has a learned aversion to plain copulas because they feel weak. They are the most honest verbs in English.

**Fix.** Use is, are, has. "The gallery is the city's main exhibition space." "The team has twelve engineers."

## 12. Negative parallelisms and tailing negations

**Looks like.** "Not only X but also Y." "It's not just about the beat; it's the atmosphere." Clipped tailing negations tacked onto a sentence: "The options come from the selected item, no guessing."

**Why it reads as AI.** Overused construction that signals emphasis without earning it. Closely related to entry 1.

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

**Fix.** Make the claim or cut the sentence. "The policy may affect outcomes" is enough. One hedge at most.

## 21. Generic positive conclusions

**Looks like.** "The future looks bright." "Exciting times lie ahead." "This represents a major step in the right direction."

**Why it reads as AI.** The model closes with vague optimism because closing is hard.

**Fix.** End with a fact, a number, or a concrete next step. "The company plans to open two more locations next year."

## 22. Conjunctive adverbs as transition crutches

**Looks like.** "However," "therefore," "additionally," "furthermore," "moreover," "thus," "consequently," "specifically," "importantly" used as openers, often where no real logical connection exists.

**Why it reads as AI.** The connective tissue does the work of pretending there's an argument.

**Fix.** Drop the adverb and let the sentence stand. If the connection is real, show it through substance rather than announcing it.

## 23. Em and en dashes

*Default skill behavior: remove all em dashes (—) and en dashes (–) from output.*

**Looks like.** Em dashes in place of commas, periods, or parentheses, used as a default punchy connector. En dashes for ranges (*1990–2000*, *pages 12–15*) or as a weaker stand-in for an em dash.

**Why it reads as AI.** The dash stack reads like punchy sales copy, and models misuse hyphens and en dashes inconsistently.

**Caveat, and it is a real one.** The em dash is no longer good evidence of AI authorship. The Economist's 2026 comparison of its own prose against ChatGPT, Claude, Gemini, and Grok (55,940 sentences, 1.2 million words) found that only Claude used em dashes more often than human writers did; the others used them less. Meanwhile the same study found models use *fewer* commas, semicolons, and parentheses overall (entry 54). So treat a pile of em dashes as a style problem rather than a fingerprint, and do not raise a score on dash count alone. This skill still strips them by default, but that is a house-style choice about how the writing should read, not a detection claim.

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

**Why it reads as AI.** ChatGPT in particular defaults to curly quotes.

**Fix.** Match whatever the target context uses. In plain-text and code contexts, use straight quotes throughout.

## 29. Collaborative communication artifacts

**Looks like.** "I hope this helps," "Of course," "Certainly," "Would you like me to," "here is a," "let me know."

**Why it reads as AI.** Chatbot correspondence pasted in as content.

**Fix.** Cut it and start with the answer.

## 30. Knowledge-cutoff disclaimers

**Looks like.** "As of my last training update." "While specific details are limited based on available information." "Up to my knowledge cutoff."

**Why it reads as AI.** Model self-disclosures that don't belong in published content.

**Fix.** Find the fact and cite it, or don't make the claim.

## 31. Sycophantic openings

**Looks like.** "Great question!" "You're absolutely right." "What a thoughtful observation." "That's an excellent point."

**Why it reads as AI.** Conversational artifacts from chatbot training leaking into prose.

**Fix.** Cut. Start with the answer.

## 32. Signposting and announcements

*Top-six tell (#5).*

**Looks like.** "Let's dive into." "Let's explore." "Let's break this down." "Here's what you need to know." "Without further ado." "In this section, we will discuss."

**Why it reads as AI.** The model announces what it's about to do instead of doing it. The meta-commentary gives the piece a tutorial-script feel.

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

**Why it reads as AI.** The words perform emphasis or candor while carrying no information. "Honestly" and "actually" imply a contrast with some unstated dishonest or expected version that never appears. "Simply" and "just" wave away difficulty the reader may not share. "Genuinely" and "meaningfully" try to certify that this instance is the real one, which only raises the question of the others. "Arguably" hedges and boosts at the same time, so the sentence commits to nothing. "Quietly" is the current standout: it manufactures drama by implying the writer noticed something others missed ("quietly became the default," "quietly shipping"), and it topped Forbes's May 2026 list of new AI giveaways. Delete any of them and the sentence usually means exactly the same thing, which is the test.

**Fix.** Cut the word and check the sentence still stands. It almost always does. Keep an intensifier only when it marks a real contrast the sentence needs ("the build is slow, but the tests are *very* slow" earns it). One survivor per paragraph at most.

---

## 48. Load-bearing and structural metaphors

**Looks like.** Structural engineering applied to arguments, teams, and decisions that are not buildings.

*Load and structure.* "That assumption is load-bearing." "That word is doing a lot of work." "The heavy lifting happens in the second step." "Scaffolding for the team." "The foundation everything rests on." "The cornerstone." "Bedrock." "The pillars of the program." "Building blocks." "The whole thing collapses without it."

*Connective tissue.* "The thread between the two teams." "The thread running through all of this." "The connective tissue between the systems." "The spine of the argument." "The backbone of the platform." "The seams where they meet." "The fabric of the organization." "The glue holding it together."

*Mechanical cousins.* "The levers you can pull." "The dials worth turning." "That moves the needle." "The plumbing underneath." "Putting it on rails." "Under the hood." "The surface area of the problem." Same move, different workshop.

**Why it reads as AI.** The metaphor claims something matters structurally without naming what depends on it. "Load-bearing" asserts that removing the thing breaks something, and then never says what breaks. "Doing a lot of work" asserts hidden importance and skips the demonstration. The connective-tissue words are the worst of the set, because they name a relationship the sentence never specifies, which is the same move as the false-depth reveal (entry 42, "the space between them"). They also cluster: once a paragraph has a foundation it tends to grow a spine, then some scaffolding. Travel metaphors (entry 16) behave the same way and often show up in the same paragraph.

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

## Counting instead of guessing

Most of this catalog asks for judgment. These fourteen counts are mechanical, and running them first stops the audit from turning into vibes. They are rules of thumb calibrated by use, not thresholds from a study, so treat a failed count as a place to look rather than a verdict.

| Count | How | Look harder when |
|-------|-----|------------------|
| Checkable specifics | Numbers, dates, proper nouns, quoted people, named mechanisms, per 100 words | Fewer than 2. Under 1 and the passage is pure abstraction. |
| Rhythm spread | Longest minus shortest sentence in each paragraph, in words | Under 8 words of spread across a whole paragraph. Spread matters; average sentence length does not (entry 54). |
| Mark variety | How many distinct punctuation types appear per 500 words | Three or fewer, or a page built only from periods and commas. |
| Words between marks | Median gap between consecutive punctuation marks, and the longest gap | Any run over about 25 words, or a median that never shifts across paragraphs. |
| Contraction rate | Contractions per 100 words, in anything conversational | Zero, or "it is" and "do not" where speech would contract (entry 64). |
| Quoted voices | People quoted by name | Zero in a piece about what people did or said. |
| Zombie nouns | Words ending `-tion`, `-ment`, `-ance`, `-ity`, `-ness`, per 100 words | More than 4, or 2 in one sentence. |
| Be-verbs | *is, are, was, were, be, been, being*, per 100 words | More than 3, especially with an abstract subject. |
| Ad-words | Adjectives and adverbs, per 100 words | More than 6, or any `-ly` intensifier that can be deleted without changing meaning. |
| Cut-test loss | Delete every sentence that repeats a point already made, then measure | More than 15% of the draft went, which means it was padded. |
| Connective density | Count *because, so, but, unless, which means, even though* per paragraph of argument | Zero in a paragraph that is supposed to reason. |
| Hedge and booster balance | Count hedges (*may, might, appears*) against boosters (*clearly, obviously, undoubtedly, always, never*) | Boosters outnumber hedges in a piece making empirical claims. |
| Attribution | Count claims about the world against named sources | More claims than sources, or a paraphrase whose source has been dropped. |

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

Frame each one as a question the writer can answer in a sentence ("which two teams stopped holding standups?"), not as an instruction. This list is the part of an audit that most changes the finished piece, and it is the part a tool cannot do for anyone. See "Why Slop Matters" (arXiv 2601.06060) on why: what separates slop from writing is not surface competence but whether any of it required the effort of knowing something, and only the writer holds that.

---

## The final audit question

After any draft, ask honestly: "What would make this so obviously AI-generated?" Name the remaining tells using the vocabulary above. Then revise. If you cannot read a paragraph aloud without hearing the cadence of a model, it still reads as AI.

Then ask the three questions the tell list cannot answer, because a draft can pass every check above and still be empty:

- **What can I cut?** Which sentences repeat a point already made, and which words are load I could drop without losing meaning (entries 19, 58, 59).
- **What here could only have been written by someone who did the work?** Underline every number, name, date, quote, and mechanism. If a paragraph has none, it is decoration (entry 61, and the counts above).
- **Is every claim the size of its evidence?** Check hedges and attributions against the source, and check absolutes against what you have actually verified (entries 60, 61).

Finish with the human-touch list: the two to five places where only the writer can raise the value of the piece.

This is also where both scores get assigned (see the rubrics in `SKILL.md`): the tells named here are the evidence behind them. For ai-smell, structural tells (the top six plus entries 42 to 46, 48 to 50, 53, 55, and 59) carry the most weight, rhythm and voice next, lexical and formatting tells least. For the reader-value score, entries 58 to 63 and the counts above supply the evidence: 58, 59, and 19 for concision, 60 and 61 for calibration, and the specifics count for substance. Cite the specific instances, then score and revise.

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

**Narrative shape is its own signal.** StoryScope (Russell et al. 2026) analyzed 61,608 stories on discourse-level features rather than style and hit 93.2% separation between human and AI narratives, with about 30 features carrying most of it. AI stories over-explain their themes and run tidy single-track plots; human ones keep ambiguity and temporal mess. That result is why entry 55 exists and why the fix for a flat anecdote is structural, not lexical.

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
