#!/usr/bin/env python3
"""Build personal-voice artifacts in the shape each provider expects.

Sources of truth:
  SKILL.md                 the skill, with YAML frontmatter
  references/ai-tells.md   the catalog the skill loads by relative path
  PROMPT.md                the two condensed prompts, in its fenced blocks

Everything under dist/ is generated. Run with no arguments to build all targets.

  python3 scripts/build.py                     build everything
  python3 scripts/build.py --list              show the targets
  python3 scripts/build.py --target chatgpt    build one or more targets
  python3 scripts/build.py --check             run validation only, build nothing
"""

import argparse
import json
import os
import re
import shutil
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIST = os.path.join(ROOT, "dist")

SKILL_NAME = "personal-voice"

# Frontmatter caps enforced by claude.ai and the Skills API.
NAME_CAP = 64
DESCRIPTION_CAP = 1024

# Instruction-field caps, per provider documentation.
CAPS = {
    "chatgpt-custom-instructions-free": 1500,
    "chatgpt-custom-instructions-plus": 5000,
    "chatgpt-custom-gpt": 8000,
}

# Lines that legitimately contain an em or en dash because they document one.
DASH_ALLOWED = ("em dashes (—)", "en dashes (–)", "1990–2000", "pages 12–15")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as f:
        return f.read()


def write(rel, text):
    path = os.path.join(DIST, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def parse_frontmatter(skill):
    if not skill.startswith("---\n"):
        fail("SKILL.md does not start with YAML frontmatter")
    body = skill.split("---", 2)[1]
    name = re.search(r"^name:\s*(.+)$", body, re.M).group(1).strip()
    start = body.index("description: |\n") + len("description: |\n")
    lines = []
    for line in body[start:].split("\n"):
        if line and not line.startswith("  "):
            break
        lines.append(line[2:])
    return name, "\n".join(lines).strip()


def parse_prompts(prompt_md):
    """Pull the condensed prompts out of PROMPT.md by the heading above each."""
    out = {}
    for key, heading in (("short", "## Short version"), ("long", "## Long version")):
        i = prompt_md.find(heading)
        if i < 0:
            fail(f'PROMPT.md is missing a "{heading}" heading')
        block = re.search(r"```\n(.*?)```", prompt_md[i:], re.S)
        if not block:
            fail(f'PROMPT.md has no fenced block under "{heading}"')
        out[key] = block.group(1).strip() + "\n"
    return out


ERRORS = []


def fail(msg):
    ERRORS.append(msg)


def check_dashes(label, text):
    for n, line in enumerate(text.split("\n"), 1):
        if ("—" in line or "–" in line) and not any(a in line for a in DASH_ALLOWED):
            fail(f"{label}:{n} has an em or en dash: {line.strip()[:70]}")


def check_cap(label, text, cap):
    if cap and len(text) > cap:
        fail(f"{label} is {len(text)} characters, cap is {cap}")


def zip_tree(rel_out, entries):
    """entries: list of (arcname, absolute source path)."""
    path = os.path.join(DIST, rel_out)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for arcname, src in entries:
            z.write(src, arcname)
    return path


def flatten_refs(text, filename):
    """Rewrite the relative catalog path for bundles with no directories.

    Knowledge-file uploads flatten everything, so `references/ai-tells.md`
    resolves to nothing and the skill silently loses its catalog.
    """
    return text.replace("references/ai-tells.md", filename)


def demote_headings(md):
    return re.sub(r"^(#{1,5}) ", r"#\1 ", md, flags=re.M)


# ---------------------------------------------------------------- targets

def build_claude_code(ctx):
    """Filesystem skill for Claude Code. Flat layout, SKILL.md at the root."""
    base = os.path.join(DIST, "claude-code", SKILL_NAME)
    os.makedirs(os.path.join(base, "references"), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, "SKILL.md"), os.path.join(base, "SKILL.md"))
    shutil.copy2(
        os.path.join(ROOT, "references", "ai-tells.md"),
        os.path.join(base, "references", "ai-tells.md"),
    )
    zip_tree(
        f"claude-code/{SKILL_NAME}.skill",
        [
            ("SKILL.md", os.path.join(base, "SKILL.md")),
            ("references/ai-tells.md", os.path.join(base, "references", "ai-tells.md")),
        ],
    )
    return {
        "files": [
            f"claude-code/{SKILL_NAME}/SKILL.md",
            f"claude-code/{SKILL_NAME}/references/ai-tells.md",
            f"claude-code/{SKILL_NAME}.skill",
        ],
        "install": "Copy the personal-voice/ folder to ~/.claude/skills/ (personal) or "
                   ".claude/skills/ (project), or unzip the .skill into "
                   "~/.claude/skills/personal-voice/. Verify with /skills.",
    }


def build_claude_ai(ctx):
    """Upload zip for claude.ai and the desktop app. Folder at the archive root."""
    src = os.path.join(DIST, "claude-code", SKILL_NAME)
    zip_tree(
        f"claude-ai/{SKILL_NAME}.zip",
        [
            (f"{SKILL_NAME}/SKILL.md", os.path.join(src, "SKILL.md")),
            (f"{SKILL_NAME}/references/ai-tells.md",
             os.path.join(src, "references", "ai-tells.md")),
        ],
    )
    return {
        "files": [f"claude-ai/{SKILL_NAME}.zip"],
        "install": "Enable code execution under Settings > Capabilities, then "
                   "Settings > Customize > Skills > + > Create skill > Upload a skill.",
    }


def build_claude_api(ctx):
    """Same wrapped layout as claude.ai, uploaded through /v1/skills."""
    src = os.path.join(DIST, "claude-code", SKILL_NAME)
    zip_tree(
        f"claude-api/{SKILL_NAME}.zip",
        [
            (f"{SKILL_NAME}/SKILL.md", os.path.join(src, "SKILL.md")),
            (f"{SKILL_NAME}/references/ai-tells.md",
             os.path.join(src, "references", "ai-tells.md")),
        ],
    )
    return {
        "files": [f"claude-api/{SKILL_NAME}.zip"],
        "install": "POST to /v1/skills with the skills-2025-10-02 beta header, then pass "
                   "the returned skill_id in the container parameter alongside the code "
                   "execution tool. Workspace-wide once uploaded.",
    }


def build_cursor(ctx):
    """Cursor and other tools that read SKILL.md from a skills directory."""
    src = os.path.join(DIST, "claude-code", SKILL_NAME)
    zip_tree(
        f"cursor/{SKILL_NAME}.skill",
        [
            ("SKILL.md", os.path.join(src, "SKILL.md")),
            ("references/ai-tells.md", os.path.join(src, "references", "ai-tells.md")),
        ],
    )
    return {
        "files": [f"cursor/{SKILL_NAME}.skill"],
        "install": "unzip -o cursor/personal-voice.skill -d "
                   "~/.cursor/skills/personal-voice (or .cursor/skills/ for one project). "
                   "Same layout works for opencode.",
    }


def _knowledge_files(prefix):
    """Flat copies for knowledge-file uploads, with the catalog path rewritten."""
    skill_name = f"{SKILL_NAME}-skill.md"
    tells_name = f"{SKILL_NAME}-ai-tells.md"
    skill = flatten_refs(read("SKILL.md"), tells_name)
    tells = flatten_refs(read("references/ai-tells.md"), tells_name)
    write(f"{prefix}/knowledge/{skill_name}", skill)
    write(f"{prefix}/knowledge/{tells_name}", tells)
    stale = [f for f, t in ((skill_name, skill), (tells_name, tells))
             if "references/ai-tells.md" in t]
    if stale:
        fail(f"{prefix} knowledge files still reference a directory path: {stale}")
    return [f"{prefix}/knowledge/{skill_name}", f"{prefix}/knowledge/{tells_name}"]


KNOWLEDGE_NOTE = (
    "\n\nThe two attached files are the full version of these rules: "
    f"{SKILL_NAME}-skill.md is the skill and {SKILL_NAME}-ai-tells.md is the catalog of "
    "64 tells with examples, the mechanical counts, and the research. Read "
    f"{SKILL_NAME}-ai-tells.md before any substantial audit, and quote its entry names "
    "when you report findings.\n"
)


def build_chatgpt(ctx):
    """Instruction fields plus knowledge files. No skills system to install into."""
    short, long = ctx["prompts"]["short"], ctx["prompts"]["long"]
    files = []

    free = short
    check_cap("chatgpt/custom-instructions-free.txt", free,
              CAPS["chatgpt-custom-instructions-free"])
    files.append(write("chatgpt/custom-instructions-free.txt", free))

    plus = long
    check_cap("chatgpt/custom-instructions-plus.txt", plus,
              CAPS["chatgpt-custom-instructions-plus"])
    files.append(write("chatgpt/custom-instructions-plus.txt", plus))

    gpt = long.rstrip("\n") + KNOWLEDGE_NOTE
    check_cap("chatgpt/custom-gpt-instructions.txt", gpt, CAPS["chatgpt-custom-gpt"])
    files.append(write("chatgpt/custom-gpt-instructions.txt", gpt))

    files += [os.path.join(DIST, f) for f in _knowledge_files("chatgpt")]
    return {
        "files": [os.path.relpath(f, DIST) for f in files],
        "install": "Custom GPT: paste custom-gpt-instructions.txt into Instructions and "
                   "upload both knowledge/ files as Knowledge. Account-wide: paste "
                   "custom-instructions-free.txt (Free, Go) or custom-instructions-plus.txt "
                   "(Plus and above) into Settings > Personalization > Custom instructions. "
                   "Project: attach both knowledge/ files and paste the plus version into "
                   "the project instructions.",
    }


def build_gemini(ctx):
    """Gemini Gems: instructions box plus knowledge files."""
    text = ctx["prompts"]["long"].rstrip("\n") + KNOWLEDGE_NOTE
    files = [write("gemini/gem-instructions.txt", text)]
    files += [os.path.join(DIST, f) for f in _knowledge_files("gemini")]
    return {
        "files": [os.path.relpath(f, DIST) for f in files],
        "install": "Create a Gem, paste gem-instructions.txt into the instructions box, "
                   "and add both knowledge/ files as sources. Google does not document a "
                   "character cap for the instructions box, so nothing is enforced here; "
                   "if it truncates, fall back to the ChatGPT free version.",
    }


COPILOT_HEADER = """# Writing prose in this repository

These rules cover prose written for humans: READMEs, docs, PR descriptions, commit
messages, issue comments, changelogs, and code comments meant to explain rather
than annotate. They do not apply to code, configuration, or generated output.

"""


def build_copilot(ctx):
    """A .github tree that can be dropped into a repository as-is."""
    long = ctx["prompts"]["long"].rstrip("\n")
    tells_rel = f"{SKILL_NAME}/ai-tells.md"

    repo_wide = (
        COPILOT_HEADER
        + long
        + "\n\nThe full catalog of 64 tells, with examples and the mechanical counts, "
        + f"is at `.github/{tells_rel}`. Read it before any substantial audit: "
        + f"@.github/{tells_rel}\n"
    )
    path_specific = (
        "---\n"
        'applyTo: "**/*.md,**/*.mdx,**/*.txt"\n'
        "---\n\n"
        + COPILOT_HEADER
        + long
        + f"\n\nFull catalog: @.github/{tells_rel}\n"
    )

    files = [
        write("copilot/.github/copilot-instructions.md", repo_wide),
        write("copilot/.github/instructions/personal-voice.instructions.md", path_specific),
        write(f"copilot/.github/{tells_rel}", read("references/ai-tells.md")),
    ]
    return {
        "files": [os.path.relpath(f, DIST) for f in files],
        "install": "Copy the copilot/.github/ tree into your repository. Use "
                   "copilot-instructions.md for repository-wide instructions, or "
                   "instructions/personal-voice.instructions.md to scope them to prose "
                   "files by glob. Delete whichever one you do not want. If the repo "
                   "already has a copilot-instructions.md, append rather than overwrite. "
                   "The same files are read by Copilot in VS Code, on github.com, and in "
                   "the CLI.",
    }


def build_generic(ctx):
    """One self-contained markdown file, and a plain rules file."""
    skill = read("SKILL.md")
    body = skill.split("---", 2)[2].lstrip("\n")
    # The skill points at the catalog by path. In a single file, point at the appendix.
    for old, new in (
        ("- `references/ai-tells.md`: the full catalog",
         "- The appendix at the end of this file: the full catalog"),
        ("Read that file when drafting", "Read it when drafting"),
        ("`references/ai-tells.md`", "the appendix at the end of this file"),
        ("references/ai-tells.md", "the appendix at the end of this file"),
    ):
        body = body.replace(old, new)
    body = body.replace(". the appendix at the end", ". The appendix at the end")
    catalog = read("references/ai-tells.md")
    # Drop the catalog's own title so it does not sit under the appendix heading.
    catalog = catalog.split("\n", 1)[1].lstrip("\n") if catalog.startswith("# ") else catalog
    catalog = demote_headings(catalog)
    single = (
        f"# {SKILL_NAME}\n\n"
        + f"> {' '.join(ctx['description'].split())}\n\n"
        + "This file is generated. It is `SKILL.md` and `references/ai-tells.md` in one "
        + "document, for tools that take a single instruction file.\n\n---\n\n"
        + body.rstrip("\n")
        + "\n\n---\n\n# Appendix: the full catalog\n\n"
        + catalog.rstrip("\n")
        + "\n"
    )
    files = [
        write(f"generic/{SKILL_NAME}-single-file.md", single),
        write("generic/rules.txt", ctx["prompts"]["long"]),
    ]
    return {
        "files": [os.path.relpath(f, DIST) for f in files],
        "install": "personal-voice-single-file.md is the whole skill in one document, for "
                   "any tool that accepts one instruction file (Cline, Windsurf, Zed, a "
                   "system prompt, an API call). rules.txt is the condensed version for "
                   "small rules files such as .clinerules or .windsurfrules.",
    }


def build_release(ctx):
    """The four assets published to the GitHub release."""
    pairs = [
        (f"claude-code/{SKILL_NAME}.skill", f"{SKILL_NAME}.skill"),
        (f"claude-ai/{SKILL_NAME}.zip", f"{SKILL_NAME}.zip"),
        (f"generic/{SKILL_NAME}-single-file.md", f"{SKILL_NAME}-single-file.md"),
    ]
    files = []
    for src, out in pairs:
        dst = os.path.join(DIST, "release", out)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(os.path.join(DIST, src), dst)
        files.append(f"release/{out}")

    # One copy of each instruction field artifact, plus one copy of the knowledge
    # files. Walking the target directories would pack the 90KB catalog five times.
    packed = [
        ("chatgpt/custom-instructions-free.txt", "chatgpt/custom-instructions-free.txt"),
        ("chatgpt/custom-instructions-plus.txt", "chatgpt/custom-instructions-plus.txt"),
        ("chatgpt/custom-gpt-instructions.txt", "chatgpt/custom-gpt-instructions.txt"),
        ("gemini/gem-instructions.txt", "gemini/gem-instructions.txt"),
        ("copilot/.github/copilot-instructions.md", "copilot/copilot-instructions.md"),
        ("copilot/.github/instructions/personal-voice.instructions.md",
         "copilot/personal-voice.instructions.md"),
        ("generic/rules.txt", "generic/rules.txt"),
        (f"chatgpt/knowledge/{SKILL_NAME}-skill.md",
         f"knowledge/{SKILL_NAME}-skill.md"),
        (f"chatgpt/knowledge/{SKILL_NAME}-ai-tells.md",
         f"knowledge/{SKILL_NAME}-ai-tells.md"),
    ]
    zip_tree(f"release/{SKILL_NAME}-prompts.zip",
             [(arc, os.path.join(DIST, src)) for src, arc in packed])
    files.append(f"release/{SKILL_NAME}-prompts.zip")
    return {
        "files": files,
        "install": "Published as release assets. personal-voice.skill for Claude Code and "
                   "Cursor, personal-voice.zip for claude.ai and the Skills API, "
                   "personal-voice-single-file.md for single-file tools, and "
                   "personal-voice-prompts.zip for the instruction-field artifacts.",
    }


TARGETS = [
    ("claude-code", "Claude Code, opencode, any filesystem skill loader", build_claude_code),
    ("claude-ai", "claude.ai and the Claude desktop app", build_claude_ai),
    ("claude-api", "The Claude Skills API", build_claude_api),
    ("cursor", "Cursor", build_cursor),
    ("chatgpt", "ChatGPT: custom GPTs, custom instructions, projects", build_chatgpt),
    ("gemini", "Gemini Gems", build_gemini),
    ("copilot", "GitHub Copilot: repository and path-specific instructions", build_copilot),
    ("generic", "Single-file tools and small rules files", build_generic),
    ("release", "Assets published to the GitHub release", build_release),
]

# claude-ai, claude-api, and cursor reuse what claude-code writes; release reuses
# everything. Keep this order when building a subset.
DEPENDS = {
    "claude-ai": ["claude-code"],
    "claude-api": ["claude-code"],
    "cursor": ["claude-code"],
    "release": ["claude-code", "claude-ai", "generic", "chatgpt", "gemini", "copilot"],
}

DIST_README = """# dist/

Generated by `scripts/build.py`. Do not edit anything in here and do not commit it.
Every artifact comes from `SKILL.md`, `references/ai-tells.md`, and the condensed
prompts in `PROMPT.md`.

| Target | Where it goes | Artifacts |
|--------|---------------|-----------|
{rows}

Sizes and the exact file list are in `manifest.json`.
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--target", action="append", default=[],
                    help="build one target (repeatable); default is all")
    ap.add_argument("--list", action="store_true", help="list targets and exit")
    ap.add_argument("--check", action="store_true", help="validate only, build nothing")
    args = ap.parse_args()

    if args.list:
        width = max(len(n) for n, _, _ in TARGETS)
        for name, desc, _ in TARGETS:
            print(f"{name.ljust(width)}  {desc}")
        return 0

    skill = read("SKILL.md")
    name, description = parse_frontmatter(skill)
    prompts = parse_prompts(read("PROMPT.md"))

    if len(name) > NAME_CAP:
        fail(f"frontmatter name is {len(name)} characters, cap is {NAME_CAP}")
    if not re.fullmatch(r"[a-z0-9-]+", name):
        fail(f'frontmatter name "{name}" must be lowercase letters, numbers, and hyphens')
    if any(w in name for w in ("claude", "anthropic")):
        fail(f'frontmatter name "{name}" contains a reserved word')
    if not description:
        fail("frontmatter description is empty")
    if len(description) > DESCRIPTION_CAP:
        fail(f"frontmatter description is {len(description)} characters, "
             f"cap is {DESCRIPTION_CAP}")

    for label in ("SKILL.md", "references/ai-tells.md", "README.md", "AGENTS.md",
                  "PROMPT.md", "llms.txt"):
        check_dashes(label, read(label))

    print(f"source: name={name}, description {len(description)}/{DESCRIPTION_CAP} chars, "
          f"short prompt {len(prompts['short'])}, long prompt {len(prompts['long'])}")

    if args.check:
        return report()

    wanted = args.target or [n for n, _, _ in TARGETS]
    unknown = [t for t in wanted if t not in {n for n, _, _ in TARGETS}]
    if unknown:
        print(f"unknown target(s): {', '.join(unknown)}", file=sys.stderr)
        return 2
    for t in list(wanted):
        for dep in DEPENDS.get(t, []):
            if dep not in wanted:
                wanted.append(dep)
    order = [n for n, _, _ in TARGETS if n in wanted]

    if not args.target and os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)

    ctx = {"prompts": prompts, "description": description, "name": name}
    manifest, rows = {}, []
    for target in order:
        fn = dict((n, f) for n, _, f in TARGETS)[target]
        result = fn(ctx)
        desc = dict((n, d) for n, d, _ in TARGETS)[target]
        entries = []
        for rel in result["files"]:
            full = os.path.join(DIST, rel)
            entries.append({"path": rel, "bytes": os.path.getsize(full)})
            if rel.endswith((".md", ".txt")):
                check_dashes(f"dist/{rel}", open(full, encoding="utf-8").read())
        manifest[target] = {"description": desc, "install": result["install"],
                            "files": entries}
        rows.append(f"| `{target}` | {desc} | " +
                    ", ".join(f"`{e['path']}`" for e in entries) + " |")
        print(f"  {target}: {len(entries)} file(s)")

    write("manifest.json", json.dumps(manifest, indent=2) + "\n")
    write("README.md", DIST_README.format(rows="\n".join(rows)))
    return report()


def report():
    if ERRORS:
        print("\n".join("FAIL: " + e for e in ERRORS), file=sys.stderr)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
