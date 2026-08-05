# Repository operating guide

Purpose: always-on instructions for Codex and other repo-aware agents working in this `open_mower_ros` fork. Keep this file concise; route durable detail to the linked source of truth.

## Start every task here

1. Read [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md) for the current branch, active workstreams, blockers, and the exact next actions.
2. Read the closest nested `AGENTS.md` for every path you may change.
3. For substantive change, fix, refactor, documentation, review, or release work, use the repo-scoped `project-operations` skill in `.agents/skills/project-operations/`.
4. For multi-session, cross-package, safety-sensitive, or ambiguous work, read [PLANS.md](PLANS.md) and create or resume one plan under `docs/exec-plans/active/`.
5. Inspect `git status --short --branch`, the relevant diff, `git worktree list`, remotes, and the linked issue/PR before editing.

Do not ask the user to restate facts already available in these sources. Verify current behavior from repository files rather than relying on memory.

## Sources of truth

- `AGENTS.md`: durable operating rules only; never task status.
- [docs/PROJECT_STATE.md](docs/PROJECT_STATE.md): compact startup snapshot and router; not the backlog.
- `docs/exec-plans/active/`: self-contained state, decisions, evidence, and next action for complex active work.
- [GitHub Issues](https://github.com/MartinHaghani/open_mower_ros/issues): canonical outstanding-work backlog. Do not create unlinked Markdown TODO lists.
- `scripts/agent/project-policy.json`: machine-readable canonical repository and integration-base routing used by local and CI policy.
- `docs/decisions/`: append-only architectural decision records. Supersede decisions; do not rewrite their history.
- Stable reference and operating docs under `docs/`: current system truth.
- Git commits and PRs: implementation and verification ledger.

Record decision-relevant rationale, alternatives, evidence, risks, and uncertainty. Do not record private chain-of-thought, full terminal transcripts, or activity diaries.

## Automatic task lifecycle

### Start and isolate

- Map the request to one issue. Create a linked issue automatically when authorized GitHub access is available and no suitable issue exists.
- A simple question, explanation, status report, read-only review, or diagnosis does not create an issue, branch, commit, or pull request unless the maintainer explicitly asks for tracking or a change.
- Use one short-lived branch per issue, normally `codex/<issue>-<description>`.
- Never mix unrelated dirty work. If the current checkout contains unrelated changes, preserve it and create an isolated worktree from the intended base.
- Mark the issue/workstream in progress and put branch, base SHA, scope, acceptance criteria, and verification plan in the active ExecPlan.

### Plan and delegate

- Keep requirements, shared decisions, integration, and final reporting in the main agent.
- Proactively delegate independent read-heavy exploration, tests/log analysis, documentation audit, and review when it materially improves speed or quality.
- Prefer two or three bounded subagents and nesting depth one. Require concise evidence-backed summaries rather than raw logs.
- Allow only one writer per file or shared worktree. Give independent write-heavy tasks separate worktrees and keep one parent integrator.

### Work and document

- Update the active ExecPlan at every meaningful stopping point: progress, discoveries, decisions, validation evidence, blockers, and exact next action.
- Update stable docs in the same change whenever behavior, interfaces, config, operations, or safety assumptions change.
- Put newly discovered out-of-scope work in a linked issue with evidence, risk, dependencies, acceptance criteria, and verification needs. If GitHub is unavailable, record it under the plan's temporary `Outstanding work` section and reconcile it before closeout.
- Keep generated artifacts and bulky run logs out of narrative docs. Link or summarize selected evidence with reproducible commands and artifact identifiers.

### Verify and close

- Run verification proportional to risk and record exact commands and outcomes. Never imply a command was run when it was not.
- Review the complete diff for scope, generated/vendor boundaries, secrets, debug artifacts, and documentation impact.
- Reconcile the issue, active plan, stable docs, ADRs, and `PROJECT_STATE` before stopping.
- Move a completed plan to `docs/exec-plans/completed/`; leave incomplete plans active with a precise resume point.
- Final reporting must state outcome, changed behavior, verification, safety/rollback concerns, unresolved issues, and exact next action.

## Git and GitHub autonomy

For an authorized change/build task, agents may act without another prompt to create issues, branches, and worktrees; edit and validate files; make coherent commits; push task branches; and open or update draft PRs.

- Use Conventional Commit subjects such as `fix(localization): ...` or `docs(agent-ops): ...`.
- Substantive commits require a body covering why, important constraints, and validation, plus `Refs: #<issue>`.
- For topic-branch pushes and pull requests, CI validates every non-merge commit in the event range. Only recognized Dependabot-generated subjects receive subject-only handling; other commits keep the normal evidence requirements. The exception registry is read from the immutable comparison base, with a known-empty registry for the first clean bootstrap, so a pull request cannot exempt itself.
- Stage intentional paths only; never use broad staging to absorb unrelated changes.
- Push an early recoverable checkpoint for multi-session work, then keep the draft PR and issue current.
- Put `Closes #<issue>` in the PR body only when merge into the target branch should close the issue.

Agents must obtain explicit user approval before merging, pushing directly to the default branch or configured integration/base branch, force-pushing, rewriting shared history, deleting branches or worktrees containing unique work, deploying, changing live mower/VESC configuration, or performing a physical mower test. Never use destructive Git commands to work around a dirty tree.

## Adopting this operating system in older tasks

Already-running agents do not retroactively receive newly landed repository instructions. Before claiming adoption, verify that the agent-OS landing commit recorded in `docs/PROJECT_STATE.md` is an ancestor of the task branch and that both `AGENTS.md` and `.agents/skills/project-operations/SKILL.md` exist in that checkout. If it is not adopted, create or link any missing issue, topic branch, and plan required by the task—or queue missing GitHub tracking when access is unavailable—then checkpoint unique work. Do not checkout, rebase, reset, or clean a dirty worktree merely to obtain the policy. Integrate the landed operating-system commit only from a clean, reviewable state, inspect and trust the hooks, then start a new Codex task so startup instructions load afresh.

The active project repository is `MartinHaghani/open_mower_ros`: push topic branches only to `origin`. `upstream` remains the read-only source fork at `ClemensElflein/open_mower_ros`; the local `alm` remote is parked and must not receive pushes unless the maintainer explicitly reactivates that migration.

## Repository map and safety boundaries

This is a ROS Noetic catkin workspace for OpenMower.

- `src/open_mower`: launch/orchestration, params, hardware presets, and RViz configuration.
- `src/mower_logic`: high-level state machine and monitoring. Safety-critical.
- `src/mower_hardware`: supported Mowrator direct hardware bridge. Safety-critical.
- `src/mower_comms_v1` and `src/mower_comms_v2`: legacy/simulation comms bridges. Safety-critical.
- `src/mower_map`, `src/mower_msgs`, `src/mower_simulation`, `src/mower_utils`: first-party map, interface, simulation, and utility packages.
- `src/lib` and `services`: mixed submodule, vendored, or external boundaries. Do not treat them as first-party by default.
- `config`: structured config. `config/mower_config.schema.json` is authoritative.
- `docker`: runtime images and entrypoints; entrypoints are safety-sensitive.
- `devenv` and `.devcontainer`: development-only container setup.
- `webui`: React/Vite source for `/next/`; `web/next/` is generated output. Treat all of `web/` as generated-first.
- `tools/coverage_lab`: laptop-only coverage-planner evaluation and V2 prototypes; read its nested guide first.

Treat motion, blade control, emergency handling, localization authority, launch wiring, hardware params, container entrypoints, and live ESC settings as safety-sensitive. Live VESC writes must refresh `docs/vesc_configs/` and `docs/VESC_MAINTENANCE.md` in the same change.

Preserve these boundaries:

- Keep ROS package boundaries and catkin conventions intact.
- Do not broadly format or clean `src/lib/`, `services/`, or `web/`.
- Keep `config/mower_config.sh.example` aligned while it exists, but it remains deprecated.
- `src/open_mower/config/mower_config.sh.example` is only a redirect stub.
- Keep upstream-sync work separate from fork-specific behavior; document intentional drift.

## Verified setup and run commands

These commands are verified from repository files but are not assumed to have run in the current environment:

```bash
rosdep update
git submodule update --init --recursive
rosdep install --from-paths src --ignore-src --default-yes
catkin_make
source devel/setup.bash
roslaunch open_mower open_mower.launch
```

Development container helpers:

```bash
./devenv/start_devenv.sh
./devenv/attach.sh
```

## Documentation and verification routing

- Start with [docs/README.md](docs/README.md), [docs/REPO_MAP.md](docs/REPO_MAP.md), and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
- Config changes: read [docs/CONFIGURATION.md](docs/CONFIGURATION.md) and [config/AGENTS.md](config/AGENTS.md); update schema, deprecated example, and docs together.
- Source or launch changes: read [src/AGENTS.md](src/AGENTS.md); update package/architecture/build docs as applicable.
- Docker changes: read [docs/DOCKER.md](docs/DOCKER.md) and [docker/AGENTS.md](docker/AGENTS.md).
- Generated Web changes: read [web/AGENTS.md](web/AGENTS.md); React source changes use [webui/AGENTS.md](webui/AGENTS.md).
- Coverage lab changes: read `tools/coverage_lab/AGENTS.md` and its linked roadmap/active plan.

Before closeout, run the repository policy command documented by the `project-operations` skill plus relevant package/build tests. Safety-sensitive changes require explicit risk, rollback, and controlled-validation evidence.

## Review guidelines

- Prioritize physical safety, control-authority regressions, silent config drift, generated/vendor edits, inadequate validation, and missing recovery behavior.
- Treat undocumented safety-sensitive behavior changes and weakened safety checks as high-priority findings.
- Treat a stale or non-resumable active ExecPlan as a blocking handoff defect for complex work.
