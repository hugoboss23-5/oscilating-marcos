# Change ID: PROP-002

## What changes
Reset interaction protocol:
- Remove chat-based approval loop
- Replace with terminal-only approval via file flag APPROVED=yes in proposal

## Why it helps
Prevents deadlock between chat input vs terminal execution.
Keeps everything inspectable and terminal-driven.

## Risk level
LOW

## Rollback plan
git revert HEAD

## Exact files impacted
- proposals workflow only (no code yet)

## Test / verification plan
cat proposals/PROP-002-control-loop-reset.md

## Approval Status
APPROVED=no

