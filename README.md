# personal-voice

A skill that writes and edits prose so it reads like a person wrote it, not an AI agent.

It does two things:

1. Drafts new writing in a natural, personal voice (and can match a voice you give it from a sample).
2. Audits existing drafts and strips the patterns that make text read as AI-generated.

## What's in here

- `SKILL.md`: the skill itself. Personal voice, voice matching, the six highest-signal AI tells, no em/en dash default, writing and editing workflow, and the final read-aloud audit.
- `references/ai-tells.md`: the full catalog of AI writing patterns, each with a before-and-after example. The skill loads this when it's doing real drafting or auditing.

## Install from `.skill` package

CI builds `personal-voice.skill` on every push to `main` and publishes it to the [latest release](https://github.com/rickcrawford-postman/personal-voice/releases/latest). The file is a zip of `SKILL.md` and `references/`.

Download:

```bash
curl -LO https://github.com/rickcrawford-postman/personal-voice/releases/latest/download/personal-voice.skill
```

Install into Cursor:

```bash
mkdir -p ~/.cursor/skills/personal-voice
curl -LO https://github.com/rickcrawford-postman/personal-voice/releases/latest/download/personal-voice.skill
unzip -o personal-voice.skill -d ~/.cursor/skills/personal-voice
rm personal-voice.skill
```

`SKILL.md` should end up at `~/.cursor/skills/personal-voice/SKILL.md`. Use `.cursor/skills/personal-voice/` instead for a project-local install.

To build locally: `./scripts/package-skill.sh`

## How to use it

Point your assistant at the skill and ask it to write or clean something:

- "Rewrite this so it sounds like a person, not a bot."
- "This draft reads like AI. Fix it."
- "Write a short post about X in my voice. Here's a sample of how I write: ..."
- "Audit this before I publish it."

If you give it a writing sample, it will match your sentence rhythm, word choice, and habits rather than just removing tells. If you don't, it falls back to a natural, varied, opinionated default voice. By default it also strips em dashes and en dashes from output.

You can also layer house style on top: ban specific words, forbid em dashes, cap the length, or require plain prose with no headers. State the constraint and the skill applies it throughout.

## Credit

The pattern catalog builds on the [humanizer](https://github.com/) approach and on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. Additional patterns come from observing common tells in long-form drafting.

## License

MIT. See `SKILL.md` frontmatter.
