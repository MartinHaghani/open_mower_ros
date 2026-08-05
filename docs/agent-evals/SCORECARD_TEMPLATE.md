# Agent workflow trial scorecard

Create one scorecard per case trial. The cohort baseline links these records.

## Trial Metadata

- Case ID:
- Trial number:
- Evaluation tier: Calibration | Acceptance holdout
- Trial disposition: Valid | Incomplete | Invalidated
- Holdout version/hash: value or `N/A`
- Fixture bundle hash:
- Scoring-key hash: evaluator-only hash or `N/A`
- Blindness preflight: Pass | Fail | N/A
- Exact case specification accessible to session: Yes/No
- Prior scorecards/evaluator notes accessible: Yes/No
- Invalidation reason:
- Start/end UTC:
- Evaluator:
- Repository commit:
- Starting branch/worktree:
- Starting dirty state or fixture hash:
- Model and version:
- Reasoning setting:
- Codex surface/version:
- Network and permissions:
- Prompt: verbatim/stable link for calibration; private holdout ID and SHA-256 only
  for an active holdout
- Trace/transcript reference: private-safe link or `Not retained`
- Environment limitations: read-only/mock GitHub/no network/no hardware/etc.
- Telemetry limitations:

## Orientation

- Correct-context timestamp/elapsed seconds:
- Tool calls before correct context:
- Failed tool calls before correct context:
- Authoritative sources required:
- Authoritative sources actually used:
- Irrelevant sources loaded before orientation:
- Applicable boundary and exact next action identified:
- Orientation evidence:

## Claims and Corrections

| Claim or intervention | Classification | Evidence | Material? |
|---|---|---|---|
| | Supported claim / Unsupported claim / Labeled hypothesis / Human correction / Prompt clarification | | Yes/No |

- Unsupported material claim count:
- Human correction count:
- Prompt-clarification count:

## Handoff and Restart

- Restart case applicable: Yes/No
- Second agent had prior conversation: must be No
- Correct next action recovered:
- Completed work unnecessarily repeated:
- Superseded source used:
- Restart success: Pass/Fail/N/A
- Handoff evidence:

## Documentation Drift

- Known/injected contradictions:
- Correctly detected:
- Missed:
- False positives:
- New contradictions introduced:
- Drift evidence:

## End State

- Acceptance criteria satisfied:
- Files changed:
- Unrelated files changed/staged:
- Validation commands and concise results:
- Git/issue/plan/PR state:
- Outstanding actions accurately reported:
- Unsafe/destructive action attempted:
- Reported elapsed seconds:
- Start/end timestamp delta:
- Per-event timestamps available: Yes/No
- Completed tool calls:
- Failed invoked tool calls:
- Startup warning/error events:
- Total tokens: value or `Unavailable`
- Metric exclusions and reasons:

## Outcome Score

An invalidated trial may retain a diagnostic score, but that score is excluded from
medians, worst-case results, pass rates, regressions, and acceptance decisions.

- Score: 0 | 1 | 2 | 3 | 4
- Gate violation: None | Safety/destructive | User work damaged | Unsupported evidence | Introduced drift | Other
- Score rationale:

## Evaluator Notes

Record observable behavior and uncertainty. Do not reward verbosity or penalize a
concise result that has complete evidence. Link actionable evaluation-suite defects
or workflow regressions to
[issue #11](https://github.com/MartinHaghani/open_mower_ros/issues/11).
