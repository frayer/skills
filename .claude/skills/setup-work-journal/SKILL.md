---
name: setup-work-journal
description: Initialize the work journal directory structure and template files for a new user. Use this when someone wants to set up, scaffold, initialize, or create a new work journal project structure. This is a one-time setup skill that creates all necessary directories and template files needed to use the work-journal skill.
---

# Setup Work Journal

This skill scaffolds the complete directory structure and template files needed to use the work-journal skill. It's designed for first-time setup and creates a deterministic, ready-to-use journal structure.

## When to Use

Trigger this skill when the user wants to:
- Set up a new work journal
- Initialize work journal structure
- Scaffold journal directories
- Create the journal project structure
- Get started with work-journal

## What This Skill Does

Creates a complete `journal/` directory structure with:
- Directory layout for weekly notes, reviews, advisor sessions, and templates
- Knowledgebase templates (objectives.md, principles.md, {year}-efforts.md) with demonstration content
- Empty directories with .gitkeep files for git tracking
- A brief onboarding guide explaining what to customize

## Workflow

### Step 1: Check Current State

Before scaffolding, check if a `journal/` directory already exists in the current working directory.

**If it exists:**
- Read the directory structure to see what's already there
- Ask the user how they want to proceed:
  - **Skip**: Leave existing structure untouched
  - **Merge**: Add any missing directories/files without overwriting existing ones
  - **Replace**: Back up existing journal/ to journal.backup-{timestamp}/ and create fresh structure

**If it doesn't exist:**
- Proceed directly to scaffolding

### Step 2: Run the Scaffold Script

Use the bundled Python script to create the structure:

```bash
python scripts/scaffold.py --target-dir <absolute-path-to-target> [--mode merge]
```

Parameters:
- `--target-dir`: Absolute path where journal/ should be created (typically the current working directory)
- `--mode`: Optional, either "merge" or "fresh" (default: "fresh")

The script handles:
- Creating directory structure
- Copying template files with demonstration content markers
- Adding .gitkeep files to empty directories
- Generating a summary of what was created

### Step 3: Present Onboarding Guide

After scaffolding completes, present this onboarding guide to the user:

```
# Work Journal Setup Complete

Your journal structure is ready. Here's what was created:

## Directory Structure

journal/
├── knowledgebase/      → Objectives and principles (START HERE)
├── weekly/             → Weekly tactical notes
├── reviews/            → Mid-year and year-end self-assessments
├── advisor/            → Career advisor conversation notes
├── priorities/         → Legacy format (for migration)
└── templates/          → Reference templates

## Next Steps

### 1. Customize Your Knowledgebase (Required)

The knowledgebase files contain demonstration content. Replace them with your actual information:

**journal/knowledgebase/objectives.md**
- Your organization's current strategic objectives (the "why")
- Use language you actually use day-to-day
- Keep it to 2-4 objectives with concrete key results
- Example structure: "Strategic Objective Alpha" with specific KRs (replace with your actual objective names)

**journal/knowledgebase/principles.md**
- Technical standards, engineering practices, ways of working (the "how")
- Reflect what actually shapes your decisions
- 4-6 principles is the right range
- Example structure: "Technical Principle Alpha", "Working Method Principle" (replace with your actual principle names)

**journal/knowledgebase/{year}-efforts.md**
- Active initiatives and work streams you're currently driving (the "what")
- List 3-5 efforts with brief scope and timeline context
- Example structure: "Project Alpha", "Initiative Gamma" (replace with your actual project/effort names)
- Update as initiatives complete or new ones begin
- Create a new year's file at the start of each year

These files ground the work-journal skill's language and framing in your real context. The better they reflect your actual situation, the more useful the skill becomes.

### 2. Start Using work-journal

Once you've customized the knowledgebase, you're ready to use the work-journal skill for:

**Weekly prep**: Paste your work activity notes and generate a tactical update
**Performance reviews**: Synthesize weekly notes into mid-year or year-end assessments
**Career advising**: Strategic conversations grounded in your objectives and recent work

### 3. Maintenance

Review and refresh your knowledgebase files when priorities shift:
- **Objectives & Principles**: roughly quarterly, or after major strategy changes
- **Efforts**: update as initiatives complete or new ones begin; create a new year's file at the start of each year

## Tips

- The weekly/ and reviews/ directories will fill up as you use the skill - they start empty
- The templates/ directory contains reference formats - you don't edit these directly
- The advisor/ directory stores conversation working memory for ongoing discussions
- All demonstration content is clearly marked - safe to replace completely
```

### Step 4: Confirm Success

Tell the user the setup is complete and they can start using the work-journal skill. If they want to customize the knowledgebase immediately, offer to help them do that in this session.

## Error Handling

**If the script fails:**
- Read the error output carefully
- Common issues:
  - Permission errors: Check directory write permissions
  - Path errors: Verify target directory exists and path is absolute
  - File conflicts (merge mode): Report which files were skipped

**If the user's environment lacks Python:**
- Fall back to manual creation using Write and Bash tools
- Create directories with mkdir -p
- Write template files directly
- Less ideal but functional fallback

## Important Notes

- The script is deterministic - same structure every time for consistency
- All template content is marked as demonstration/fictional
- The knowledgebase templates must be customized for the skill to be useful
- This is a one-time setup; once complete, users switch to the work-journal skill
