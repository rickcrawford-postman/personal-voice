# personal-voice

A skill that writes and edits prose so it reads like a person wrote it, not an AI agent.

It does three things:

1. Drafts new writing in a natural, personal voice (and can match a voice you give it from a sample).
2. Audits existing drafts and strips the patterns that make text read as AI-generated.
3. Does the part a tell-hunt misses: cuts the padding, checks that every claim is the size of its evidence, counts what is actually verifiable in the draft, and hands back a short list of the places where only you can make the piece better.

## What's in here

- `SKILL.md`: the skill itself. Personal voice, voice matching, two modes (detect the tells or edit them out), the six highest-signal AI tells, no em/en dash default, writing and editing workflow, the cut/claim/calibration tests, the ai-smell score (a 0 to 100 rating of how machine-generated the text reads), the reader-value score (0 to 100 for substance, concision, calibration, and reader path), the adversarial review (argue against the piece as its toughest readers would, then fix, concede, or ask), the human-touch list, and the final read-aloud audit.
- `references/ai-tells.md`: the full catalog of 73 AI writing patterns, each with a before-and-after example, plus fifteen mechanical counts you can run instead of guessing, a term-frequency method for finding tells that are on no list yet, a short section on writing in languages other than English, and the research notes behind both scores. The skill loads this when it's doing real drafting or auditing.
- `PROMPT.md`: condensed versions of the skill for products that only give you an instructions box. One fits 1,500 characters, the other fits 5,000.
- `AGENTS.md`: install instructions written for coding agents, so you can point one at the repo and say "install this."
- `llms.txt`: the machine-readable index of the above.
- `scripts/build.py`: generates a package per provider from those sources, and validates them. See [How the build works](#how-the-build-works).

## Install

The skill is two files with no executable code: `SKILL.md` and
`references/ai-tells.md`. Keep them together, because the skill reads the catalog
by relative path. Split them and it still runs, just without the examples,
counts, or research.

Every provider wants a different shape, so the build generates all of them:

```bash
python3 scripts/build.py --list     # see the targets
python3 scripts/build.py            # build them all into dist/
python3 scripts/build.py --target chatgpt
```

Each section below tells you which `dist/` artifact to use. Or skip the build and
grab a [release asset](#download-the-prebuilt-packages).

If you would rather not do any of this by hand, point a coding agent at the repo
and say "install this skill." `AGENTS.md` tells it what to do on every surface.

### Claude Code

Skills are filesystem-based here, so installing means putting the folder in the
right place. Nothing to register, no settings to edit.

```bash
# personal, available in every project
mkdir -p ~/.claude/skills
git clone https://github.com/rickcrawford-postman/personal-voice.git ~/.claude/skills/personal-voice
```

```bash
# project-scoped, checked in and shared with the team
mkdir -p .claude/skills
git clone --depth 1 https://github.com/rickcrawford-postman/personal-voice.git .claude/skills/personal-voice
rm -rf .claude/skills/personal-voice/.git
```

Working on the skill itself? Symlink your clone instead, so edits apply
immediately: `ln -s "$(pwd)" ~/.claude/skills/personal-voice`.

Check it landed with `/skills` in a session, or `claude --list-skills`. Claude
picks it up from the frontmatter description, so you don't have to invoke it by
name, though `/personal-voice` works if you want to force it.

To make it apply to everything you write rather than only when you ask, add a
line to `~/.claude/CLAUDE.md`:

```markdown
Use the `personal-voice` skill for all prose written for humans: posts, essays,
emails, READMEs, docs, PR descriptions, and commit messages. Invoke it before
drafting, not after. This does not apply to code, comments, or config.
```

### claude.ai and the Claude desktop app

These want a zip with the skill folder at the root of the archive, which is not the
same layout as the `.skill` file:

```bash
python3 scripts/build.py --target claude-ai
# dist/claude-ai/personal-voice.zip
```

Then, in the browser or the desktop app:

1. Turn on code execution first, under **Settings > Capabilities**. Skills are
   inert without it.
2. Go to **Settings > Customize > Skills**, click **+**, then **Create skill**,
   then **Upload a skill**.
3. Upload `dist/personal-voice.zip`.
4. Toggle it on. Claude uses it automatically when a request matches.

Two things worth knowing. Custom skills are per-user, so each teammate uploads
their own copy, and they don't sync between surfaces: a claude.ai upload is
invisible to Claude Code and vice versa. Skills you enable here also show up in
the Claude add-ins for Excel, PowerPoint, Word, and Outlook.

### Claude API

```bash
python3 scripts/build.py --target claude-api
# dist/claude-api/personal-voice.zip
```

Upload through the `/v1/skills` endpoints with the `skills-2025-10-02` beta
header, then reference the returned `skill_id` in the `container` parameter
alongside the code execution tool. API skills are workspace-wide, so one upload
covers everyone in it.

### Cursor, opencode, and other skill-aware tools

Same layout as Claude Code, different directory:

```bash
python3 scripts/build.py --target cursor
mkdir -p ~/.cursor/skills/personal-voice
unzip -o dist/cursor/personal-voice.skill -d ~/.cursor/skills/personal-voice
```

`SKILL.md` should end up at `~/.cursor/skills/personal-voice/SKILL.md`, with
`references/` beside it. Use `.cursor/skills/personal-voice/` for a project-local
install.

### ChatGPT

ChatGPT has no skills system, so the skill goes in as instructions. `SKILL.md` is
about 52,000 characters and every instructions field is smaller than that, so the
build emits a version sized for each one:

```bash
python3 scripts/build.py --target chatgpt
# dist/chatgpt/custom-instructions-free.txt   1,435 chars (cap 1,500)
# dist/chatgpt/custom-instructions-plus.txt   4,610 chars (cap 5,000)
# dist/chatgpt/custom-gpt-instructions.txt    4,936 chars (cap 8,000)
# dist/chatgpt/knowledge/personal-voice-skill.md
# dist/chatgpt/knowledge/personal-voice-ai-tells.md
```

**A custom GPT (best fidelity).** Create a GPT, paste
`custom-gpt-instructions.txt` into Instructions, then upload both `knowledge/`
files as Knowledge. That gets you the entire catalog, since knowledge files have
no practical size limit. The build rewrites the catalog's path inside those copies
(`references/ai-tells.md` becomes `personal-voice-ai-tells.md`), because knowledge
uploads flatten directories and the skill would otherwise point at a file that
isn't there.

**Custom instructions (applies to every chat).** Settings > Personalization >
Custom instructions. Paste `custom-instructions-free.txt` on Free or Go (1,500
character cap), or `custom-instructions-plus.txt` on Plus and above (5,000).

**A project.** Create a project, attach both `knowledge/` files, and paste
`custom-gpt-instructions.txt` into the project instructions.

### Gemini

```bash
python3 scripts/build.py --target gemini
# dist/gemini/gem-instructions.txt
# dist/gemini/knowledge/*.md
```

Create a Gem, paste `gem-instructions.txt` into the instructions box, and add both
`knowledge/` files as sources. Google doesn't document a character cap for that
box, so the build doesn't enforce one. If it truncates, fall back to
`dist/chatgpt/custom-instructions-free.txt`.

### GitHub Copilot

The build emits a `.github` tree you can drop into a repository as-is:

```bash
python3 scripts/build.py --target copilot
# dist/copilot/.github/copilot-instructions.md                        repo-wide
# dist/copilot/.github/instructions/personal-voice.instructions.md    prose files only
# dist/copilot/.github/personal-voice/ai-tells.md                     the catalog
```

Use `copilot-instructions.md` to apply the rules across the whole repository, or
`instructions/personal-voice.instructions.md` to scope them by glob (it carries
`applyTo: "**/*.md,**/*.mdx,**/*.txt"` so it only fires on prose). Keep one and
delete the other. Both `@`-include the catalog file, which is why it ships inside
the same tree. If the repo already has a `copilot-instructions.md`, append rather
than overwrite. The same files are read by Copilot in VS Code, on github.com, and
in the CLI.

### Cline, Windsurf, Zed, a raw system prompt, anything else

```bash
python3 scripts/build.py --target generic
# dist/generic/personal-voice-single-file.md   the skill and catalog in one document
# dist/generic/rules.txt                       the condensed version
```

`personal-voice-single-file.md` is everything in one file, with the catalog as an
appendix and the internal file references rewritten to point at it. Use it wherever
you can pass one instruction document. `rules.txt` is for small rules files such as
`.clinerules` or `.windsurfrules`.

### Download the prebuilt packages

CI validates and builds on every push to `main` and publishes four assets to the
[latest release](https://github.com/rickcrawford-postman/personal-voice/releases/latest):

```bash
base=https://github.com/rickcrawford-postman/personal-voice/releases/latest/download
curl -LO $base/personal-voice.skill              # Claude Code, Cursor, opencode
curl -LO $base/personal-voice.zip                # claude.ai, desktop app, Skills API
curl -LO $base/personal-voice-single-file.md     # single-file tools
curl -LO $base/personal-voice-prompts.zip        # ChatGPT, Gemini, Copilot artifacts
```

You can also run the **Package skill** workflow manually from the
[Actions tab](https://github.com/rickcrawford-postman/personal-voice/actions/workflows/package-skill.yml).

**Workflow not running?** Check **Settings > Actions > General** and confirm
Actions are enabled for this repository. If the repo lives in an organization, an
admin may also need to approve new or updated workflows under **Actions > General
> Fork pull request workflows** or the workflow approval policies. Pushes made by
GitHub Apps using `GITHUB_TOKEN` do not trigger workflows; push from your machine
with `git push` instead.

## How the build works

Three files are the source of truth. Everything under `dist/` is generated, and
`dist/` is gitignored.

| Source | Feeds |
|--------|-------|
| `SKILL.md` | Every skill package, the knowledge-file copies, the single-file build |
| `references/ai-tells.md` | The same, plus the Copilot catalog file |
| `PROMPT.md` | Every instruction-field artifact, extracted from its two fenced blocks |

So the condensed prompts live in exactly one place. Edit the fenced blocks in
`PROMPT.md` and every ChatGPT, Gemini, Copilot, and rules-file artifact changes
with them.

`scripts/build.py` also validates, and CI fails on any of it:

- The frontmatter `name` (64 characters, lowercase and hyphens, no reserved words)
  and `description` (1,024 characters). claude.ai and the Skills API reject
  anything over, and the error they return doesn't say why. The description was
  1,332 characters before this check existed.
- Every generated instruction artifact against its provider's field cap.
- Em and en dashes in the sources and in the generated output, with an exemption
  for the handful of lines that document the characters themselves.
- That no flat bundle still points at `references/ai-tells.md`, which would leave
  the skill silently without its catalog.

`dist/manifest.json` lists every artifact with its size and where it goes.
`scripts/package-skill.sh` still works and now wraps the build.

## How to use it

Point your assistant at the skill and ask it to write or clean something:

- "Rewrite this so it sounds like a person, not a bot."
- "This draft reads like AI. Fix it."
- "Write a short post about X in my voice. Here's a sample of how I write: ..."
- "Audit this before I publish it."

If you give it a writing sample, it will match your sentence rhythm, word choice, and habits rather than just removing tells. If you don't, it falls back to a natural, varied, opinionated default voice. By default it also strips em dashes and en dashes from output.

Every pass ends with two numbers and a list.

The **ai-smell score** runs 0 to 100 and lower is more human. It breaks down across structural tics, rhythm, voice, lexical tells, and formatting, with the specific lines that earned each point. On an edit it reports the before-and-after so you can see the drop. It is a self-check on how the writing reads, not an AI detector.

The **reader-value score** runs 0 to 100 and higher is better. It scores substance (numbers, names, dates, quotes, mechanisms), concision (what percentage of the draft survives the cut test), calibration (whether the hedges, attributions, and absolutes match the evidence), and reader path (order that serves a reader). The two scores exist separately because they come apart: a page can score 8 on ai-smell and 22 on reader-value, which means it is clean, readable, and says nothing. Reporting only the first number would call that a win.

The **adversarial review** argues against the piece before it ships. It names two or three readers with a reason to push back (the expert in the room, the skeptic of motive, the reader in a hurry), steelmans up to five objections against specific lines, and marks each one: fix it, concede it in the text, hand it to you because only you have the evidence, or stand by the line and say why. The scores tell you how a piece reads; this tells you whether it survives its audience.

The **human-touch list** is the last thing it hands back, and usually the most useful. Two to five places where only you can raise the value of the piece, each phrased as a question you can answer in a sentence: which two teams dropped standups, what the latency actually was, which side of the tradeoff you come down on, what is still broken. The skill will not invent that material to fill the gap. It marks the hole and asks.

You can also layer house style on top: ban specific words, forbid em dashes, cap the length, or require plain prose with no headers. State the constraint and the skill applies it throughout.

## The research behind it

The skill is a field guide plus a lightweight judge, and both halves are grounded in published work.

The pattern catalog started from [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup from thousands of flagged edits. That page's core insight drives everything here: a language model picks the most statistically likely next token, so its output converges on generic phrasing that fits the widest range of cases. Research on the [shrinking landscape of linguistic diversity](https://arxiv.org/abs/2502.11266) measures that convergence directly and finds LLM writing assistants reduce stylistic variety. AI-smell is the surface of it, which is why the fix is always more specificity, more variation, and a point of view.

The word-level tells are not folklore either. [Kobak et al. (2024)](https://arxiv.org/abs/2406.07016) tracked "excess vocabulary" across 14 million PubMed abstracts and found words like *delve*, *underscore*, and *showcase* spiked after ChatGPT, a larger shift than the Covid pandemic left on scientific writing. [Liang et al. (2025)](https://www.nature.com/articles/s41562-025-02273-8) ran the same idea over 1,121,912 papers in *Nature Human Behaviour* and estimated up to 22% of computer science papers carried LLM-modified text.

The newest entries come from measured studies rather than lists. Expert annotators who use ChatGPT heavily caught all but 1 of 300 AI articles and named the tells they relied on, including stock names like Emily and Sarah and quotes that sound like the narrator (Russell, Karpinska and Iyyer 2025). Professional writers editing 1,057 model paragraphs produced an edit taxonomy led by awkward word choice, sentence structure, redundant exposition, and cliché (Chakrabarty et al., CHI 2025). A PNAS study found instruction-tuned models use present participial clauses at up to five times the human rate (Reinhart et al. 2025). ELEPHANT measured sycophancy: models validated the asker about 76% of the time, against 22% for people (Cheng et al. 2025). The catalog also gained a section on when the tells mislead: detectors flagged about 61% of essays by non-native English writers as AI (Liang et al. 2023), and text a model only edited keeps most of its human fingerprint (Shan et al. 2026).

They also go stale, which is why the skill now carries the method rather than only the lists. Louis Abraham's [load-bearing](https://louisabraham.github.io/load-bearing/) project samples a hundred GitHub pull request descriptions a day, drops bot accounts, and clusters what is left by vocabulary alone. One way of writing went from about 1% of the corpus in January 2025 to 44.6% of the four weeks ending August 2026, and its most characteristic word, at 123 times the rate it appears anywhere else, is *load-bearing*, which was already in this catalog as entry 48. That register is now entry 67, and the ratio the project publishes is now a section of its own: how to compare a draft against the writer's own earlier writing and read off whatever comes out on top, instead of grepping a list somebody else compiled last year.

The lists come with a hard limit, too. [Yakura et al. (2024)](https://arxiv.org/abs/2409.01754) measured ChatGPT-preferred vocabulary across 824,634 podcast episodes and found the words rising in *spontaneous human speech* after the release, causally linked by synthetic control; a [smaller unscripted-speech corpus](https://arxiv.org/abs/2508.00238) finds the effect real but patchier. The vocabulary is entering the language. So a word-frequency hit says the draft leans on the word, never that a machine wrote it, and the lexical dimension stays capped for that reason.

The **ai-smell score** borrows from the LLM-as-a-judge literature:

- **Reason first, then score.** [G-Eval](https://arxiv.org/abs/2303.16634) showed an LLM judge matches human ratings far better when it reasons through the specifics and scores each dimension separately, instead of guessing one overall number. The score is built that way.
- **Score as a skeptic.** LLM judges suffer from [self-preference bias](https://arxiv.org/abs/2410.21819) (they rate text in their own style too kindly) and [verbosity bias](https://arxiv.org/abs/2406.07791) (they reward length). The scoring rules push against both, because the judge and the writer here are the same kind of model.
- **The score is not a detector.** Statistical signals like perplexity and burstiness [misfire on plain and non-native writing](https://www.pangram.com/blog/why-perplexity-and-burstiness-fail-to-detect-ai), so the number stays a self-check on how the text reads, never a claim about who or what wrote it.

### On punctuation, where most advice is wrong

Punctuation is a real stylometric feature family. [Kumarage et al. (2023)](https://arxiv.org/abs/2303.03697) build a detector on three of them (phraseology, punctuation, lexical diversity) and show that adding mark counts measurably improves state-of-the-art classifiers. But the findings that survive are about distributions, not individual marks, and the popular advice gets all three backwards.

- **Variety beats counts.** The [survey by Terčon and Dobrovoljc](https://arxiv.org/abs/2510.05136) collects the measurements: AI text draws on a narrower set of marks, with commas and periods doing almost all the work, and uses fewer commas, question marks, dashes, parentheses, semicolons, and colons than human writing. The Economist found the same thinning across 1.2 million words and traced part of it to models not quoting anyone, since quotation is what pulls attribution punctuation into a sentence.
- **Variance beats mean.** Sentence-length *spread* is consistently lower in AI text, while studies disagree entirely about whether models write longer sentences or shorter ones. So the skill scores the gap between the longest and shortest sentence in a paragraph and ignores the average. Getting this backwards is how you end up "fixing" prose by making every sentence short.
- **Rhythm has a second layer.** [Stanisz, Kwapień, and Drożdż](https://arxiv.org/abs/2212.11182) measured the gaps between consecutive punctuation marks, in words, across seven Western languages and found a discrete Weibull distribution whose two parameters separate languages, individual authors, and even the language a text was translated into. Their work targets language universals rather than detection, so the skill treats it as a lens: words-between-marks is a rhythm separate from sentence length, and any unpunctuated run past about 25 words reads as machine-made even when the grammar is fine.
- **Uniform correctness is its own tell.** Models under-use apostrophes and avoid contractions and colloquialisms, and a [formal syntactic comparison of LLM and human news writing](https://arxiv.org/abs/2506.01407) found human authors reaching for contractions and blunter phrasing more often, with model output reading as an averaged grammatical profile of many human styles. Hence the register check: contract where speech would contract, put a real aside in parentheses, let one sentence be a fragment. The first rule attached to it is that you never fake an error to sound human.

And the counterweight, which matters as much. The em dash was the most confident punctuation claim of 2025 and it did not survive contact with data. Educators now argue for [dropping punctuation heuristics entirely](https://blog.aare.edu.au/stop-policing-punctuation-now-why-ai-detection-needs-a-rethink/), because they persist on being easy to apply rather than accurate, and the cost of a false positive lands on writers who punctuate carefully. So punctuation sits inside one capped dimension of the ai-smell score, gets judged on variety and spread rather than counts, and never functions as a verdict about who wrote something.

The **reader-value score** and the substance checks come out of a different set of findings, mostly from 2025 and 2026:

- **Padding is trained in, so it can be cut out.** Reward models and LLM judges both prefer longer answers, and [YapBench](https://arxiv.org/abs/2601.00624) makes the result measurable by scoring responses against the shortest sufficient answer. GPT-3.5-Turbo beats several newer frontier models on conciseness, which means verbosity is a post-training choice rather than a limitation. That is why the cut test is mechanical here instead of left to taste.
- **Rewriting inflates certainty.** [Belem et al. (2026)](https://arxiv.org/abs/2606.07951) found language models shift the certainty of text they rewrite in up to 75% of cases, biased 1.5 to 2 times toward more confidence, and it compounds over repeated passes. [Hagar et al. (2025)](https://arxiv.org/abs/2509.25498) name the three shapes it takes: attribution stripping, overinterpretation, certainty inflation. A humanizing pass is a rewrite, so it is exactly where hedges and attributions get quietly deleted. The skill checks calibration against the source, not against the previous draft.
- **The drift is toward hyperbole.** [Bao et al. (2025)](https://arxiv.org/abs/2505.12218) analyzed 823,798 arXiv abstracts and found more positive sentiment and more inflation adjectives after ChatGPT, alongside simpler syntax, fewer connective words, and lower readability. Higher lexical density, harder to read. So packing in content words is not the goal; more checkable specifics and fewer wasted words is.
- **AI prose is nominal and impersonal.** The survey by [Terčon and Dobrovoljc (2025)](https://arxiv.org/abs/2510.05136) synthesizes the measurement literature: more nouns, determiners, and prepositions, fewer adjectives and adverbs, lower lexical diversity. That profile is what nominalization produces, which is why "the implementation of the optimization of" is now a tell in its own right.
- **Surface quality was never the problem.** [Why Slop Matters (2026)](https://arxiv.org/abs/2601.06060) defines slop through superficial competence, asymmetric effort, and mass producibility. Removing tells raises superficial competence, which is the one axis that was already fine. That argument is the reason substance is scored separately and the reason every pass ends by asking the writer for the things only they have.
- **Word lists should be computed, not remembered.** [Antislop](https://arxiv.org/abs/2510.15061) profiles model output against human baselines and finds patterns appearing over 1,000 times more often than in human text. The related [Slop Score](https://eqbench.com/slop-score.html) weights its verdict 60% overused words, 25% not-X-but-Y constructions, and 15% overused trigrams. That last number is a nice independent check: a tool built purely from measurement puts a quarter of its score on the same construction this skill lists first.

The fuller writeup, with every source, is in `references/ai-tells.md`.

## Credit

The pattern catalog builds on the humanizer approach and on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. It also borrows from [no-ai-slop](https://github.com/petergyang/no-ai-slop) (the detect-vs-edit split, the minimum-effective-edit principle, and tells like colon reveals and empty intensifiers) and [deslop](https://blog.stephenturner.us/p/deslop) (dramatic-pause directives and calibrating how hard to edit to how voice-critical the piece is). Additional patterns come from observing common tells in long-form drafting.

The substance and punctuation halves are built on published research rather than observation: the sources are linked above and catalogued in full, with what each one contributes, at the end of `references/ai-tells.md`.

## License

MIT. See `SKILL.md` frontmatter.
