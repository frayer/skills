#!/usr/bin/env python3
"""
Scaffold the work-journal directory structure.

This script creates a deterministic directory layout with template files
for using the work-journal skill.
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime


# Template content for knowledgebase files
OBJECTIVES_TEMPLATE = """<!-- DEMONSTRATION CONTENT: This file contains fictional sample data for illustration purposes only. It is not real. -->

> **Demonstration content:** This file contains fictional sample data for illustration purposes only. Replace with your own information before use.

# Objectives

Your strategic objectives — what you're trying to accomplish and how success is measured. Use language you actually use day-to-day. Keep it to 2–4 objectives with concrete key results.

## Strategic Objective Alpha

Brief description of the first major objective you're driving. Replace with your actual objective and use language you use in daily work.

**Key Results:**

- Specific measurable outcome 1
- Specific measurable outcome 2
- Specific measurable outcome 3

## Strategic Objective Beta

Brief description of the second major objective. Replace with your actual objective and use language you use in daily work.

**Key Results:**

- Specific measurable outcome 1
- Specific measurable outcome 2
- Specific measurable outcome 3
"""

PRINCIPLES_TEMPLATE = """<!-- DEMONSTRATION CONTENT: This file contains fictional sample data for illustration purposes only. It is not real. -->

> **Demonstration content:** This file contains fictional sample data for illustration purposes only. Replace with your own information before use.

# Principles

The principles that guide your work — technical standards, engineering practices, ways of working, or values that shape how you and your team operate. Keep it to 4–6 principles that reflect what actually shapes your decisions.

## Technical Principle Alpha

Description of a technical standard or engineering practice that guides your work. Replace with your actual principles using language from your day-to-day work.

## Technical Principle Beta

Description of another technical standard or engineering practice that guides your work. Replace with your actual principles using language from your day-to-day work.

## Working Method Principle

Description of a way of working or operational value that shapes how you and your team operate. Replace with your actual principles using language from your day-to-day work.

## Quality Standard Principle

Description of a quality standard or architectural constraint that guides your decisions. Replace with your actual principles using language from your day-to-day work.
"""

EFFORTS_TEMPLATE = """<!-- DEMONSTRATION CONTENT: This file contains fictional sample data for illustration purposes only. It is not real. -->

> **Demonstration content:** This file contains fictional sample data for illustration purposes only. Replace with your own information before use.

# {year} Efforts

Active initiatives and work streams for {year}. These are the tactical efforts that consume your time and attention right now — the "what" you're working on. While objectives describe the strategic "why" and principles describe the "how," efforts capture the concrete projects, initiatives, and work streams you're actively driving.

## Project Alpha

Brief description of the first active effort or initiative you're driving. Connect it to one of your strategic objectives. Replace with your actual project/effort name using language from your day-to-day work.

**Scope:** Brief scope description
**Timeline:** Q1-Q3 {year}
**Current phase:** Current status or phase

## Project Beta

Brief description of the second active effort or initiative you're driving. Connect it to one of your strategic objectives. Replace with your actual project/effort name using language from your day-to-day work.

**Scope:** Brief scope description
**Timeline:** Q1-Q2 {year}
**Current phase:** Current status or phase

## Initiative Gamma

Brief description of the third active effort or initiative you're driving. Connect it to one of your principles or objectives. Replace with your actual initiative name using language from your day-to-day work.

**Scope:** Brief scope description
**Timeline:** Q1-Q4 {year}
**Current phase:** Current status or phase
"""

def create_directory_structure(target_dir: Path, mode: str = "fresh") -> dict:
    """
    Create the journal directory structure.

    Args:
        target_dir: Root directory where journal/ should be created
        mode: Either "fresh" (create new) or "merge" (add missing only)

    Returns:
        Dictionary with summary of what was created/skipped
    """
    journal_dir = target_dir / "journal"

    summary = {
        "directories_created": [],
        "directories_skipped": [],
        "files_created": [],
        "files_skipped": [],
    }

    # Define directory structure
    directories = [
        "knowledgebase",
        "weekly",
        "reviews",
        "advisor",
        "templates",
    ]

    # Create main journal directory
    if not journal_dir.exists():
        journal_dir.mkdir(parents=True)
        summary["directories_created"].append("journal/")
    elif mode == "fresh":
        summary["directories_skipped"].append("journal/ (already exists)")

    # Create subdirectories
    for subdir in directories:
        dir_path = journal_dir / subdir
        if not dir_path.exists():
            dir_path.mkdir(parents=True)
            summary["directories_created"].append(f"journal/{subdir}/")
        else:
            summary["directories_skipped"].append(f"journal/{subdir}/ (already exists)")

    return summary


def create_knowledgebase_files(target_dir: Path, mode: str, summary: dict):
    """Create knowledgebase template files."""
    kb_dir = target_dir / "journal" / "knowledgebase"

    # Get current year for efforts file
    current_year = datetime.now().year

    files = {
        "objectives.md": OBJECTIVES_TEMPLATE,
        "principles.md": PRINCIPLES_TEMPLATE,
        f"{current_year}-efforts.md": EFFORTS_TEMPLATE.format(year=current_year),
    }

    for filename, content in files.items():
        file_path = kb_dir / filename
        if not file_path.exists() or mode == "fresh":
            file_path.write_text(content)
            summary["files_created"].append(f"journal/knowledgebase/{filename}")
        else:
            summary["files_skipped"].append(f"journal/knowledgebase/{filename} (already exists)")


def create_gitkeep_files(target_dir: Path, summary: dict):
    """Create .gitkeep files in empty directories."""
    journal_dir = target_dir / "journal"

    empty_dirs = ["weekly", "reviews", "advisor", "templates"]

    for subdir in empty_dirs:
        gitkeep_path = journal_dir / subdir / ".gitkeep"
        if not gitkeep_path.exists():
            gitkeep_path.touch()
            summary["files_created"].append(f"journal/{subdir}/.gitkeep")


def print_summary(summary: dict):
    """Print a summary of what was created."""
    print("\n" + "=" * 60)
    print("Work Journal Scaffold Complete")
    print("=" * 60)

    if summary["directories_created"]:
        print("\n✓ Directories Created:")
        for dir_name in summary["directories_created"]:
            print(f"  - {dir_name}")

    if summary["directories_skipped"]:
        print("\n⊘ Directories Skipped:")
        for dir_name in summary["directories_skipped"]:
            print(f"  - {dir_name}")

    if summary["files_created"]:
        print("\n✓ Files Created:")
        for file_name in summary["files_created"]:
            print(f"  - {file_name}")

    if summary["files_skipped"]:
        print("\n⊘ Files Skipped:")
        for file_name in summary["files_skipped"]:
            print(f"  - {file_name}")

    print("\n" + "=" * 60)
    print("Next Steps:")
    print("  1. Customize journal/knowledgebase/objectives.md")
    print("  2. Customize journal/knowledgebase/principles.md")
    print("  3. Customize journal/knowledgebase/{year}-efforts.md")
    print("  4. Start using the work-journal skill")
    print("=" * 60 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold work-journal directory structure"
    )
    parser.add_argument(
        "--target-dir",
        type=str,
        required=True,
        help="Target directory where journal/ should be created (absolute path)"
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["fresh", "merge"],
        default="fresh",
        help="Mode: fresh (create new) or merge (add missing only)"
    )

    args = parser.parse_args()

    target_dir = Path(args.target_dir).resolve()

    # Validate target directory exists
    if not target_dir.exists():
        print(f"Error: Target directory does not exist: {target_dir}", file=sys.stderr)
        sys.exit(1)

    if not target_dir.is_dir():
        print(f"Error: Target path is not a directory: {target_dir}", file=sys.stderr)
        sys.exit(1)

    # Check if journal already exists
    journal_dir = target_dir / "journal"
    if journal_dir.exists() and args.mode == "fresh":
        print(f"Warning: journal/ already exists at {journal_dir}")
        print("Use --mode merge to add missing files without overwriting.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != "y":
            print("Aborted.")
            sys.exit(0)

    try:
        # Create structure
        summary = create_directory_structure(target_dir, args.mode)

        # Create knowledgebase files
        create_knowledgebase_files(target_dir, args.mode, summary)

        # Create .gitkeep files
        create_gitkeep_files(target_dir, summary)

        # Print summary
        print_summary(summary)

    except Exception as e:
        print(f"Error during scaffolding: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
