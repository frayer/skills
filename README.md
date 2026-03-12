# Work Journal Scaffold

**Work Journal** is a Claude Code skill that helps senior technical leaders capture, organize, and reflect on their work. This repository is a scaffold you clone, customize with your own organizational context, and use immediately.

## What Work Journal Does

Work Journal operates as a persistent professional advisor grounded in *your* objectives and principles — not generic corporate-speak. It supports three workflows:

1. **Weekly Tactical Prep** — Paste or point to notes about your week's work activity. Work Journal cleans them up, aligns language to your objectives, and writes a polished weekly note ready to drop into your team meeting doc.

2. **Performance Reviews** — At mid-year or year-end, Work Journal reads your accumulated weekly notes and drafts a self-assessment against your actual review template or a standard format organized by objective.

3. **Strategic Advisor** — Talk through a work challenge, org dynamic, or career question. Work Journal surfaces blind spots, suggests framings, and grounds advice in your real context (objectives, principles, recent journal entries).

## Directory Structure

```
journal/
  knowledgebase/           # Your objectives and principles
    objectives.md
    principles.md
  weekly/                  # Weekly tactical notes (YYYY-MM-DD.md)
  reviews/                 # Mid-year and year-end outputs
  advisor/                 # Working memory from advisor conversations
  priorities/              # Legacy effort entries (historical context)
```

## Prerequisites

- **Claude Code CLI** — the agent framework that runs Work Journal
- **Git 2.30+** — for change tracking
- **zsh 5.x+** — default on macOS; works on Linux with zsh installed

## Quick Start

### 1. Clone This Repository

```bash
git clone <repository-url>
cd work-ledger
```

### 2. Customize Your Knowledge Base

This is the most important setup step. Edit the two files in `journal/knowledgebase/` to reflect your actual organizational context:

**`objectives.md`** — Replace the sample objectives with your organization's real strategic goals. Use the language your leadership actually uses. Keep it to 2–4 objectives with concrete key results.

**`principles.md`** — Replace the sample principles with your team's actual technical standards, preferred patterns, and technology choices.

Work Journal reads these files before every response. The quality of alignment language it uses — in weekly notes, reviews, and advice — depends directly on the quality of what you put here.

### 3. Start Using Work Journal

Use the examples in the "Usage Examples" section below.

## Workflow Reference

### Weekly Tactical Prep

Provide notes about your week's work activity (pasted inline or as a file path). Work Journal will:

- Read your knowledgebase and recent weekly notes for continuity
- Parse the activity notes and organize them by category
- Write a weekly note to `journal/weekly/YYYY-MM-DD.md` (Monday-dated)
- Produce 3–5 outcome-oriented tactical bullets aligned to your objectives, ready to paste into your team meeting doc

### Performance Reviews

Ask Work Journal to draft your mid-year or year-end review. It will:

- Read all weekly notes within the review period
- Synthesize accomplishments by objective alignment
- Fill in your company's review template or use a standard format
- Save the draft to `journal/reviews/YYYY-midyear.md` or `journal/reviews/YYYY-yearend.md`

### Strategic Advisor

Have a freeform conversation about any work challenge or career question. Work Journal:

- Reads your knowledgebase and recent weekly notes for context
- Checks `journal/advisor/` for prior sessions on related topics and offers to continue them
- Asks 1–2 clarifying questions before advising
- Saves a working memory file (`journal/advisor/YYYY-MM-DD-<topic>.md`) and updates it as the conversation develops

## Usage Examples

Invoke the skill conversationally in Claude Code:

```
work-journal: Here are my notes from this week: [paste activity notes or file path]
```

```
work-journal: I need to write my mid-year review. Here's the template my company uses: [paste template]
```

```
work-journal: I'm trying to figure out how to scope an SRE role on my team. Can you help me think through it?
```

## Customization Tips

- **Keep knowledgebase files concise.** Work Journal reads them in full on every invocation. 2–4 objectives and 4–6 principles is the right range.
- **Use your organization's actual language.** If your company calls it "Platform Modernization," use that phrase — Work Journal will echo it back in your weekly notes and reviews.
- **Update quarterly.** Review and refresh your knowledgebase when organizational priorities or technical direction shifts.
- **Quantify where you can.** Specific metrics in your objectives ("reduce MTTR to under 15 minutes") give Work Journal better material to work with when writing reviews.

## Troubleshooting

**Work Journal gives generic advice not aligned to my context**
- Verify that `journal/knowledgebase/objectives.md` and `principles.md` exist and contain your actual content, not the sample placeholder text.

**No weekly notes are picked up for review drafting**
- Confirm files exist in `journal/weekly/` with the `YYYY-MM-DD.md` naming format.

**Advisor doesn't continue a prior session**
- Check that the prior session file in `journal/advisor/` has `Status: open` and was created within the last two weeks.
