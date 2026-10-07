# AGENTS.md

Instructions for coding agents working with this repository. If a user points you
at this repo and asks you to install, set up, or add the skill, follow the
matching section below and then confirm what you did.

## What this repo is

`personal-voice` is an Agent Skill: prose instructions, no executable code. Three
files are the source of truth and everything else is generated from them.

| File | Role |
|------|------|
| `SKILL.md` | The skill. YAML frontmatter plus the full instructions. About 52,000 characters. |
| `references/ai-tells.md` | Progressive-disclosure reference. The catalog of 67 AI writing tells, the mechanical counts, the term-frequency method, and the research notes. Loaded only when the skill is doing real work. |
| `PROMPT.md` | The two condensed prompts, in its fenced blocks. The build extracts them for every provider that only has an instructions field. Not part of the skill package itself. |

`dist/` is build output and is gitignored. Do not commit it.

## Build first, then install

Every provider wants a different layout, and `scripts/build.py` generates all of
them from the same three sources. Run it before installing anywhere except Claude
Code, where a plain clone works.

```bash
python3 scripts/build.py --list      # targets and what each is for
python3 scripts/build.py             # all of them, into dist/
python3 scripts/build.py --target chatgpt --target copilot
python3 scripts/build.py --check     # validate sources, build nothing
```

`dist/manifest.json` lists every artifact with its byte size and a one-line
install note, so read that rather than guessing which file a user needs.
`dist/` is gitignored; never commit it.

| Target | Artifact | Goes where |
|--------|----------|------------|
| `claude-code` | `dist/claude-code/personal-voice/` and `.skill` | `~/.claude/skills/` or `.claude/skills/` |
| `claude-ai` | `dist/claude-ai/personal-voice.zip` | Browser upload, wrapped layout |
| `claude-api` | `dist/claude-api/personal-voice.zip` | `POST /v1/skills` |
| `cursor` | `dist/cursor/personal-voice.skill` | `~/.cursor/skills/personal-voice/` |
| `chatgpt` | three sized `.txt` files plus `knowledge/` | Instructions fields and Knowledge uploads |
| `gemini` | `gem-instructions.txt` plus `knowledge/` | Gem instructions and sources |
| `copilot` | a `.github/` tree | Copy into the target repository |
| `generic` | `personal-voice-single-file.md`, `rules.txt` | Single-file tools, small rules files |
| `release` | four assets | Published by CI |

## Install for Claude Code

Personal (available in every project):

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/rickcrawford-postman/personal-voice.git ~/.claude/skills/personal-voice
```

Project-scoped (checked in, shared with the team):

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/rickcrawford-postman/personal-voice.git .claude/skills/personal-voice
rm -rf .claude/skills/personal-voice/.git
```

If the user is already working inside a clone of this repo and wants it live,
symlink instead of copying so edits take effect immediately:

```bash
ln -s "$(pwd)" ~/.claude/skills/personal-voice
```

Verify with `/skills` inside a Claude Code session, or `claude --list-skills`.
The skill is discovered by its frontmatter `description`, so no registration
step exists and nothing needs to be added to settings.json.

## Install for claude.ai, the desktop app, and the Skills API

```bash
python3 scripts/build.py --target claude-ai --target claude-api
```

For claude.ai, tell the user to upload `dist/claude-ai/personal-voice.zip` at
Settings > Customize > Skills > + > Create skill > Upload a skill, with code
execution already on under Settings > Capabilities. You cannot do that upload for
them; it is a browser action. That zip wraps the skill folder at the archive root,
which claude.ai requires and the flat `.skill` does not do.

For the API, upload `dist/claude-api/personal-voice.zip` through `/v1/skills` with
the `skills-2025-10-02` beta header, then pass the returned `skill_id` in the
`container` parameter alongside the code execution tool.

Custom skills do not sync between surfaces, so each of these is separate from a
Claude Code install and from each other.

## Install for Cursor, opencode, and other skill-aware tools

```bash
python3 scripts/build.py --target cursor
mkdir -p ~/.cursor/skills/personal-voice
unzip -o dist/cursor/personal-voice.skill -d ~/.cursor/skills/personal-voice
```

Use `.cursor/skills/personal-voice/` for a project-local install. Any tool that
reads `SKILL.md` from a skills directory takes the same layout.

Keep `references/` next to `SKILL.md`. The skill reads `references/ai-tells.md` by
relative path, so splitting them breaks the catalog silently: the skill still runs,
just without the examples, counts, or research.

## Install for ChatGPT

```bash
python3 scripts/build.py --target chatgpt
```

Pick by field:

- Custom GPT: `dist/chatgpt/custom-gpt-instructions.txt` into Instructions (8,000
  character cap), then upload both files in `dist/chatgpt/knowledge/` as Knowledge.
  Highest fidelity, because the knowledge files carry the whole catalog.
- Account-wide custom instructions: `custom-instructions-free.txt` on Free or Go
  (1,500 cap), `custom-instructions-plus.txt` on Plus and above (5,000 cap).
- Project: attach both `knowledge/` files and paste
  `custom-gpt-instructions.txt` into the project instructions.

The build rewrites the catalog path inside the knowledge copies, because knowledge
uploads flatten directories. Do not hand-edit those files; regenerate them.

## Install for Gemini

```bash
python3 scripts/build.py --target gemini
```

`dist/gemini/gem-instructions.txt` goes in the Gem instructions box, and both files
in `dist/gemini/knowledge/` go in as sources. Google does not document a character
cap for that box, so the build enforces none. If it truncates, fall back to
`dist/chatgpt/custom-instructions-free.txt`.

## Install for GitHub Copilot

```bash
python3 scripts/build.py --target copilot
cp -R dist/copilot/.github/. /path/to/repo/.github/
```

Two entry points ship in that tree, and the user should keep one:

- `.github/copilot-instructions.md` applies repository-wide.
- `.github/instructions/personal-voice.instructions.md` carries
  `applyTo: "**/*.md,**/*.mdx,**/*.txt"` and fires only on prose files.

Both `@`-include `.github/personal-voice/ai-tells.md`, which is why the catalog
ships in the same tree. If the repository already has a `copilot-instructions.md`,
append rather than overwrite, and say that you did.

## Install anywhere else

```bash
python3 scripts/build.py --target generic
```

`dist/generic/personal-voice-single-file.md` is the skill and the full catalog in
one document with the internal path references rewritten, for Cline, Windsurf, Zed,
a system prompt, or an API call. `dist/generic/rules.txt` is the condensed version
for small rules files such as `.clinerules` or `.windsurfrules`.

## If you are editing this repo

- Run `python3 scripts/build.py` after changing `SKILL.md`, `references/`, or
  `PROMPT.md`. It validates as it goes and exits non-zero on any problem, and CI
  runs the same thing.
- The condensed prompts live only in the fenced blocks of `PROMPT.md`. The build
  extracts them, so never edit a generated prompt under `dist/`.
- The frontmatter `description` has a hard cap of 1,024 characters and the `name`
  a cap of 64. Uploads to claude.ai and the Skills API reject anything longer and
  the failure message is not obvious. The build checks both; it currently reports
  1,020 of 1,024.
- `name` must be lowercase letters, numbers, and hyphens only, and cannot contain
  "claude" or "anthropic".
- Write everything in this repo the way the skill says to write. No em dashes or
  en dashes, and that includes commit messages and PR descriptions.
- When you add a tell to `references/ai-tells.md`, update the contents list, the
  entry count in `README.md` and `llms.txt`, and the dimension it maps to in the
  ai-smell rubric in `SKILL.md`. Those go stale first.
- If you add a provider, add a `build_*` function and a row to `TARGETS` in
  `scripts/build.py`, plus its field cap in `CAPS` if it has one. The install note
  you return lands in `dist/manifest.json` and `dist/README.md`.
