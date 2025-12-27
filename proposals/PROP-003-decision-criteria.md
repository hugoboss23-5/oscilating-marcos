# Change ID: PROP-003

## What changes
Add explicit decision criteria and constraints so no architectural move happens
without a measurable reason.

This proposal does NOT change code. It defines the rule-set for deciding:
A) why we freeze before risky changes,
B) when an API surface is justified vs direct model invocation,
C) how we evaluate "best" vs "good enough".

## Why it helps
Prevents low-quality decisions by forcing:
- objective constraints
- measurable verification
- explicit tradeoffs
- rollback plans
before any implementation step.

## Risk level
LOW

## Rollback plan (exact commands)
git revert HEAD

## Exact files impacted
- proposals/PROP-003-decision-criteria.md (new)

## Decision Criteria (binding)
1) Determinism: given same inputs => same outputs (no hidden time/random/net)
2) Inspectability: state transitions traceable via explicit events
3) Minimal surface area: fewer moving parts unless justified by tests
4) Reproducibility: clean boot on Codespaces via terminal-only commands
5) Safety: changes gated by git clean/branch/commit and rollback commands

## Questions this answers (with constraints)

### Q1: "Why freeze repo?"
Allowed reasons:
- prevent irreversible drift when adding files/structure
- enable clean rollback via commits
Not allowed:
- "cleanup", "refactor", aesthetics

### Q2: "Why add an API if open-source llama exists?"
API is allowed ONLY if one of these is true:
- we need a stable interface between nucleus/modes and any model runner
- we need deterministic testing of the system without invoking a model
- we need separation so model invocation is an optional bond, not the core
Otherwise: reject API changes.

### Q3: "Stop making decisions without best-criteria"
From now on, any architecture/tooling move must be preceded by a proposal that includes:
- decision being made
- at least 2 alternatives
- measurable acceptance tests
- risk + rollback
- exact files touched

## Approval Status
APPROVED=no
