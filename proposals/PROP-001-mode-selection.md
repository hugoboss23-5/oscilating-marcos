# Change ID: PROP-001

## What changes
Add explicit runtime mode selection via environment variable (MARCOS_MODE)
without altering default behavior.

## Why it helps
Allows deterministic external configuration while keeping code inspectable
and defaults unchanged.

## Risk level
LOW

## Rollback plan (exact commands)
git revert HEAD

## Exact files impacted
- marcos.py

## Test / verification plan (exact commands)
python marcos.py
MARCOS_MODE=yang python marcos.py
