# Project state

Purpose: give a newly started agent a compact, evidence-based snapshot and route it
to the active source for each workstream.

This file is **not the backlog**, an architecture reference, or a history log.
Outstanding work belongs in GitHub Issues; Project views may organize those issues;
implementation detail belongs in an active ExecPlan; stable behavior belongs in
the relevant reference documentation. Keep this page short enough to read at every
task start.

## Current Baseline

- Last verified: 2026-07-21.
- Branch used for this migration: `codex/open-mower-agent-os`.
- Inspected baseline commit: `329726f` (`webui: compact map selector controls`).
- Canonical repository: `MartinHaghani/open_mower_ros`; use the `origin` remote for
  topic-branch publication. The current integration ref is
  `origin/codex/remove-lowlevel-board`, not the stale default-branch baseline. The
  machine-readable authority is `scripts/agent/project-policy.json`.
- Upstream source: `ClemensElflein/open_mower_ros` through the `upstream` remote.
  The local `alm` remote is parked and must not receive pushes unless the maintainer
  explicitly reactivates the deferred standalone-repository migration in
  [issue #23](https://github.com/MartinHaghani/open_mower_ros/issues/23).
- Adoption status: this operating system is not active on the integration ref until
  its replacement PR merges. Tasks based on `329726f` must follow the checkpoint,
  ancestry, hook-review, and new-task process in
  [AGENT_OPERATIONS.md](AGENT_OPERATIONS.md#adoption-by-older-agents).
- Runtime baseline: the launch-composed ROS Noetic workspace described in
  [ARCHITECTURE.md](ARCHITECTURE.md); the laptop coverage lab does not replace the
  runtime `slic3r_coverage_planner`.
- Safety boundary: mower logic, low-level communications, hardware configuration,
  launch wiring, live VESC settings, and container entrypoints require
  risk-proportional validation and explicit review.

Always verify `git status`, `git branch --show-current`, `git worktree list`, and
`git rev-parse --short HEAD` before relying on this snapshot. A checked-in state
page cannot see uncommitted changes in another worktree.

## Active Workstreams

| Workstream | Status | Snapshot | Authoritative next-step source |
|---|---|---|---|
| Agent documentation, context, and Git operating system | active | Draft PR [#24](https://github.com/MartinHaghani/open_mower_ros/pull/24) is open; its previous head passed project policy, while fresh policy and corrected four-way Docker validation are pending on the head that includes the reviewed change from draft PR [#27](https://github.com/MartinHaghani/open_mower_ros/pull/27) | [issue #1](https://github.com/MartinHaghani/open_mower_ros/issues/1) and the [active migration ExecPlan](exec-plans/active/agent-operating-system-migration.md) |
| Existing coverage planner lab | planned | P0, P1, P3, P10, P11, P12, and P13 are recorded as landed; P5 is the next sequence item | [roadmap](COVERAGE_PLANNER_ROADMAP.md) and [issue #3](https://github.com/MartinHaghani/open_mower_ros/issues/3) |
| Coverage Planner V2 exploration | planned | M1 evidence and substantial M2.x local prototypes exist; M2 acceptance reconciliation and M3 candidate routing are outstanding | [algorithm status](COVERAGE_PLANNER_V2_ALGORITHM_PLAN.md#current-implementation-status) and [issue #8](https://github.com/MartinHaghani/open_mower_ros/issues/8) |
| Passive SLAM confidence weighting | planned | No active implementation plan | [issue #2](https://github.com/MartinHaghani/open_mower_ros/issues/2) |
| Parallel Mowrator slope branches | planned | Audit required before integration or worktree cleanup | [issue #12](https://github.com/MartinHaghani/open_mower_ros/issues/12) |

## Blockers and Risks

The original `/Users/martinhaghani/Code/open_mower_ros` worktree had 33 dirty paths
at the 2026-07-17 verification: 31 modified and two untracked, with nothing staged.
They contain active planner, localization, RTCM, controller-safety, and WebUI work;
they are not cleanup debris. This migration uses a separate clean worktree and must
not stage, reset, stash, or rewrite that state. The agent-OS foundation overlaps
only `docs/COVERAGE_PLANNER_ROADMAP.md` and `docs/README.md`; checkpoint and reconcile
those paths deliberately before eventual integration.

The inspection also found additional unmerged worktrees for Mowrator slope
reliability at commits `f56dd9a` and `bb84e454`, plus three Claude worktrees. Branch
names and commits prove that parallel state exists; they do not prove completion or
integration. Inspect `git worktree list --porcelain`, each worktree's status, and its
branch-local handoff before using or deleting any of them. Do not treat results on
those branches as part of the baseline until they are reviewed and merged.

Tracked rollout gaps are:

- GitHub Issues are now authoritative and issues #1–#21 seed the migrated backlog.
  Every legacy first-party source TODO/FIXME marker has exact-content ownership in
  the machine-validated [legacy register](legacy-todos.json); new markers require
  inline issue references. The Projects v2 board still requires separate OAuth
  `project` scope and is tracked
  by [issue #10](https://github.com/MartinHaghani/open_mower_ros/issues/10).
- The two Codex desktop gardening jobs are paused because their saved prompts still
  target the parked migration. Retarget and reactivate them only after this policy
  lands, under issue #10 and the authority checks in
  [AGENT_OPERATIONS.md](AGENT_OPERATIONS.md#scheduled-gardening).
- Main protection is active without required CI checks; add the stable policy gate
  only after the workflow lands and passes, also under issue #10.
- Direct pushes to the temporary integration branch are human-gated by policy but
  not yet proven blocked by live GitHub settings. Issue #10 must protect that ref
  PR-only or retire it into `main` before required governance relies on it.
- The manual fresh-agent candidate cohort required before merge is outstanding in
  [issue #11](https://github.com/MartinHaghani/open_mower_ros/issues/11); stochastic
  trials are evidence, not a required per-PR CI check.
- Full-tree pre-commit debt is ratcheted to added/modified files and tracked by
  [issue #21](https://github.com/MartinHaghani/open_mower_ros/issues/21).
- Parallel slope branches require the branch-by-branch audit in issue #12.
- PR #24's first four-way build exposed a pre-existing ARM64 default-image failure:
  the base image omits the `input` group. Immediate issue
  [#25](https://github.com/MartinHaghani/open_mower_ros/issues/25), focused draft PR
  [#27](https://github.com/MartinHaghani/open_mower_ros/pull/27), and portability
  follow-up [#26](https://github.com/MartinHaghani/open_mower_ros/issues/26) own the
  work. Do not merge or deploy until PR #24's corrected, non-publishing
  default/legacy by amd64/arm64 matrix is green; do not use the publishing manual
  dispatch path as a substitute.

These are migration gaps, not a replacement backlog. Remove a bullet when its
linked issue is completed; do not add implementation checklists here.

## Next Actions

1. Wait for and record a fresh green four-way Docker validation on draft PR #24
   with the reviewed correction from draft PR #27; keep both PRs unmerged and
   perform no deployment.
2. Run and record the pre-merge candidate cohort under issue #11.
3. Complete the external Project/required-check rollout in issue #10 after the
   workflow lands.
4. Resume planner and slope work only through their linked issues and active plans;
   preserve every unmerged worktree until issue #12 proves it is safe to clean.

## Routing

- Repository layout and ownership: [REPO_MAP.md](REPO_MAP.md) and
  [PACKAGES.md](PACKAGES.md).
- Runtime composition: [ARCHITECTURE.md](ARCHITECTURE.md).
- Build and launch commands: [BUILD_AND_RUN.md](BUILD_AND_RUN.md).
- Mowrator bench and live-hardware safety:
  [MOWRATOR_BENCH_BRINGUP.md](MOWRATOR_BENCH_BRINGUP.md) and
  [VESC_MAINTENANCE.md](VESC_MAINTENANCE.md).
- Agent planning policy: [../PLANS.md](../PLANS.md).
- Durable decisions: [decisions/README.md](decisions/README.md).
- Documentation update rules: [DOCS_MAINTENANCE.md](DOCS_MAINTENANCE.md).

## Refresh Contract

Update this file in the same change whenever an active workstream starts, finishes,
becomes blocked, changes its authoritative plan, or establishes a new baseline that
would change a fresh agent's first action. Each row must link to evidence. Remove
finished work instead of turning this page into a changelog.
