---
name: csv-budget-cli
description: Use when working on this CSV-based Python CLI budget app, especially for tests-first implementation, refactoring, and quality checks.
---

# CSV Budget CLI

## When to use
Use this skill for changes in this repository's CSV-driven budgeting workflow, CLI commands, parsing, reporting, or test coverage.

## Working rules
- Write tests before implementation.
- Keep functions small and typed.
- Prefer simple, explicit control flow over clever abstractions.
- Watch cyclomatic complexity and keep it at 10 or below.

## Quality gate
Before finalizing a change:
- Run `pytest`.
- Run `radon cc`.
- Ask `qa_engineer` to review the change set.

## Change shape
- Keep behavior focused on CSV input/output and CLI actions.
- Refactor into helper functions when a function approaches 50 lines.
