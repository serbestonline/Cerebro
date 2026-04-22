#!/bin/bash
# Cerebro — Setup Script
# Creates .claude/commands/ symlinks and courses/ directory

set -e

echo "Setting up Cerebro..."

# Create directories
mkdir -p .claude/commands
mkdir -p courses

# Create symlinks for slash commands
ln -sf ../../skills/lecture-ingest.md .claude/commands/lecture-ingest.md
ln -sf ../../skills/lecture-summary.md .claude/commands/lecture-summary.md
ln -sf ../../skills/flashcard-coverage-checker.md .claude/commands/flashcard-coverage.md
ln -sf ../../skills/mindmap-generator.md .claude/commands/mindmap.md
ln -sf ../../skills/lecture-mastery-tester.md .claude/commands/mastery-test.md
ln -sf ../../skills/essay-scaffolder.md .claude/commands/essay-scaffold.md
ln -sf ../../skills/weak-spot-hunter.md .claude/commands/weak-spots.md

echo ""
echo "Done. Created:"
echo "  .claude/commands/  — 7 slash commands linked"
echo "  courses/           — add your course folders here"
echo ""
echo "Next steps:"
echo "  1. Add course folders under courses/"
echo "  2. Create a flashcard skill in skills/flashcard-generators/"
echo "  3. Open Claude Code in this directory"
echo "  4. Type /lecture-ingest to process your first lecture"
