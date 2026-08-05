# ExecPlan: Establish the repository agent operating system

- Status: Active
- Owner: coordinating Codex agent
- Created: 2026-07-15
- Last updated: 2026-08-04
- Issue: [#1](https://github.com/MartinHaghani/open_mower_ros/issues/1)
- Branch/worktree: `codex/open-mower-agent-os` at `/Users/martinhaghani/Code/open_mower_ros_agent_os_rescope`
- Baseline commit: `329726f`
- Related ADRs: [ADR 0001](../../decisions/0001-agent-documentation-and-context-model.md), [ADR 0002](../../decisions/0002-git-autonomy-and-safety-boundary.md)

This plan follows [PLANS.md](../../../PLANS.md). It is the self-contained handoff for
implementing the documentation, context, tracking, subagent, and Git automation
requested by the maintainer.

## Purpose and Intended Outcome

A newly started agent should orient itself, select or create the correct workstream,
use subagents appropriately, preserve decisions and evidence, update outstanding
work, perform safe routine Git operations, and leave a reviewable handoff without
the maintainer repeating workflow prompts.

The outcome is a repository-enforced workflow, not merely more prose. Checked-in
instructions and skills define agent behavior; state, plans, ADRs, and issues have
separate sources of truth; deterministic local and CI checks detect omissions; Git
rules preserve human control over merge, destructive history, deployment, and live
hardware operations.

## Progress

- [x] (2026-07-15) Audited existing documentation, Git history, dirty state, and
  parallel worktrees; identified strong domain docs but no universal current-state,
  decision, or handoff layer.
- [x] (2026-07-15) Created an isolated agent-OS branch and
  worktree from baseline `329726f` so unrelated source-worktree changes remain
  untouched.
- [x] (2026-07-15) Added the documentation foundation: planning policy, project
  state router, ADR index and initial decisions, templates, and plan lifecycle.
- [x] (2026-07-15) Added concise repository operating instructions and a project operations skill
  that automatically performs startup, planning, documentation, subagent, tracking,
  Git, and closeout duties.
- [x] (2026-07-15) Added bounded custom subagent roles and project hooks for context injection and
  deterministic stop-time hygiene checks.
- [x] (2026-07-15) Completed validators and their self-tests, then executed the
  changed-file pre-commit/CI path for links, state, ExecPlans, ADRs, documentation
  impact, and commit/PR policy. Full-tree debt is tracked in issue #21.
- [x] (2026-07-15) Added issue/PR templates, CODEOWNERS, pinned workflow actions,
  least-privilege workflow permissions, and policy CI without weakening the Docker
  build or Release Drafter.
- [x] (2026-07-16) Re-scoped the reusable OpenMower operating-system commits onto
  `codex/open-mower-agent-os` from exact baseline `329726f`; excluded the deferred
  standalone-repository identity work, stale PR handoff, and unrelated Docker fix.
- [x] (2026-07-16) Added actual event-range commit validation with an immutable-base
  exception registry and a known-empty clean bootstrap, so a PR cannot exempt its
  own commits. No historical migration exceptions are carried.
- [x] (2026-07-16) Added machine-readable canonical-repository and integration-base
  routing for small/no-ExecPlan first pushes, hardened Dependabot waivers to verified
  bot-authored bump commits, preserved literal committed subjects, and accepted only
  fully validated PR handoffs for reviewed squash commits.
- [x] (2026-07-16) Added the current integration branch to the four-way Docker PR
  validation trigger; remove that temporary trigger only when integration returns
  to `main`.
- [x] (2026-07-15) Enabled Issues, created labels and issues #1–#12, configured
  squash-only merging and branch cleanup, and protected `main` with PR-only linear
  history, resolved conversations, and force-push/deletion blocks.
- [x] (2026-07-15) Added isolated Codex automations for weekly project hygiene and
  four-week rotating fresh-agent regression sampling.
- [x] (2026-07-16) Paused both jobs after confirming their saved prompts still
  targeted the deferred standalone migration; issue #10 owns safe OpenMower
  retargeting and reactivation after this operating system lands.
- [x] (2026-07-16) Verified the source worktree remained byte-for-byte unchanged
  during the rescope: tracked-diff SHA-256 `ef9395675adf27c2773dcd8d2ce18719a91030d004eb38d6bc52d6d195957c30`
  and status SHA-256 `8d2cc6f9743b519000fe1551320f337a2a688eff96cfe3f6e64d8e17df5f5de9`
  match the pre-edit snapshot; the two untracked-file hashes also match.
- [x] (2026-07-17) Re-ran the complete local policy matrix and independent scope,
  policy, and documentation reviews after hardening repository routing, commit-range
  evidence, and older-agent adoption guidance.
- [x] (2026-07-21) Published replacement draft PR
  [#24](https://github.com/MartinHaghani/open_mower_ros/pull/24), confirmed its
  project-policy check passed, and closed the superseded OpenMower PR #22 without
  deleting its branch or history.
- [x] (2026-07-21) Diagnosed PR #24's first four-way validation attempt: the ARM64
  default image failed because the Focal base lacks the `input` group, while the
  other three matrix jobs were cancelled by fail-fast. Created immediate issue
  [#25](https://github.com/MartinHaghani/open_mower_ros/issues/25), portability and
  least-privilege follow-up [#26](https://github.com/MartinHaghani/open_mower_ros/issues/26),
  and focused draft PR [#27](https://github.com/MartinHaghani/open_mower_ros/pull/27).
  Commit `ea82f06` carries the reviewed correction on this validation branch without
  merging either PR or publishing an image.
- [x] (2026-07-21) Obtained a fresh green, non-publishing default/legacy by
  amd64/arm64 matrix on corrected head `b14d647` in
  [run 29793647884](https://github.com/MartinHaghani/open_mower_ros/actions/runs/29793647884).
  Both policy checks passed, all four validation jobs passed, and the publishing
  `build` and `merge` jobs remained skipped. Neither PR was merged or deployed.
- [x] (2026-08-04) Reconciled the rollout tracking to replacement PR #24, current
  candidate head `b6a39f3`, issue #11's candidate-cohort protocol, the paused
  automation state, and the parked ALM migration. Head `b6a39f3` passed project
  policy and all four non-publishing Docker jobs in
  [run 29794246511](https://github.com/MartinHaghani/open_mower_ros/actions/runs/29794246511);
  publishing remained skipped, and no merge, deployment, or live-hardware operation
  was performed.
- [x] (2026-08-04) Reconciled current state and external tracking at `24cad13`;
  project policy and all four non-publishing Docker jobs passed in
  [run 30954272378](https://github.com/MartinHaghani/open_mower_ros/actions/runs/30954272378).
  Publishing remained skipped and the PR remained draft and unmerged.
- [ ] (Pre-merge, issue #10) Protect the temporary integration ref as PR-only or
  decide to retire it into `main`, and resolve the Projects v2 OAuth/board decision.
- [ ] (Post-merge, issue #10) After an approved merge lands and the policy workflow
  passes on its target ref, make the stable policy check required, then retarget,
  dry-run, and reactivate the two paused gardening automations.
- [x] (2026-07-15) Validated deterministic fresh-agent orientation, hooks, skill
  structure, configuration parsing, documentation-only/code/safety documentation
  impact, PR policy, and changed-file pre-commit behavior in the isolated clean
  worktree.
- [x] (2026-07-15) Reconciled migration artifacts and assigned every legacy
  first-party source TODO/FIXME marker through an exact-content validated register;
  issues #13–#20 capture the newly discovered work.
- [x] (2026-08-04) Invalidated the initial public-case cohort as pre-merge
  acceptance evidence after traces showed evaluated sessions could inspect exact
  prompts, expected sources, and success criteria. Preserved the raw artifacts and
  diagnostic scoring; none count toward acceptance.
- [ ] (2026-08-04) Create and seal a materially different private rotating holdout,
  record prompt, fixture, and scoring-key hashes, prove session blindness, and run
  at least three valid baseline and candidate trials per applicable capability.
- [ ] After current-head CI, the candidate cohort, and issue #10's pre-merge gates
  pass, obtain human merge approval. After an approved merge, complete issue #10's
  post-merge activation steps and move this plan to `completed/` in the completion
  change.

Exact next action: seal and hash the private acceptance holdout, pass its blindness
preflight, and run the baseline and candidate cohorts under issue #11. The resume
fixture must provide a synthetic landed policy commit and a state page consistent
with that landing before measuring adoption or restart behavior. Then complete
issue #10's pre-merge integration-boundary and Projects decision.
Any head change after validated head `24cad13` must repeat project policy and all
four non-publishing Docker jobs. Keep PRs #24 and #27 draft and unmerged; perform no
deployment or live-hardware operation without explicit human approval.

## Surprises & Discoveries

- The repository already contains detailed architecture, hardware, planner, and
  maintenance documentation. The primary gap is state ownership and enforcement,
  not lack of domain prose.
- The source worktree contains 33 unrelated dirty paths spanning multiple
  workstreams: 31 modified and two untracked, with nothing staged. The agent-OS
  foundation overlaps only `docs/COVERAGE_PLANNER_ROADMAP.md` and `docs/README.md`.
  An isolated worktree is required; those two paths must be checkpointed and
  reconciled deliberately before eventual integration.
- Several local worktrees and unmerged slope branches exist. A branch name is not
  completion evidence; every agent must inspect worktree state and branch-local
  handoffs before integration or cleanup.
- Coverage Planner V2 status is internally inconsistent: the newer prototype plan
  points beyond classification, while the older algorithm plan still calls M1 the
  immediate next step. The migration must track reconciliation rather than silently
  selecting one claim.
- Recent commits often have concise subjects without explanatory bodies, reducing
  the usefulness of Git history as a handoff ledger. Commit policy must preserve
  problem, decision, validation, risk, and follow-up context for substantive work.
- The fork had Issues disabled and no branch protection. Both are now enabled; the
  sole-collaborator setup makes a mandatory independent approval impossible until a
  second trusted reviewer is added.
- GitHub Projects v2 uses a separate OAuth scope not present on the current `gh`
  token. Repository administration access does not imply Projects access.
- The repository contained 15 legacy source TODO/FIXME sites without ownership.
  Eight focused issues (#13–#20) now own them; the navigation-completion marker was
  linked to the already related issue #6.
- The former pre-commit exclusion regex effectively skipped the repository. A true
  all-files run exposed inherited formatter and executable-bit debt and attempted
  broad unrelated rewrites. Those side effects were removed, CI now ratchets
  added/modified files, and issue #21 owns deliberate full-tree cleanup.
- The ARM64 `ros:noetic-ros-base-focal` image does not provide an `input` group, so
  the default Dockerfile's existing `adduser openmower input` step failed. The
  focused correction creates GID `996` explicitly as the current OSv2 assumption;
  issue #26 owns a host-aware, least-privilege design.
- A focused PR targeting `codex/remove-lowlevel-board` does not trigger the baseline
  four-way build, while that workflow's manual-dispatch path publishes images. The
  safe pre-merge evidence path is PR #24's PR-only, non-publishing validation job.
- Issue #10 originally mixed work that can happen before merge with required-check
  and automation activation that depends on the workflow already being landed.
  Treating all of it as a pre-merge gate would be circular, so the rollout is now
  explicitly divided into pre-merge governance decisions and immediate post-merge
  activation.
- The first candidate cohort was not blind: `docs/agent-evals/CASES.md` exposed the
  exact prompts, expected sources, and success criteria, and several sessions read
  their own case specifications. One resume fixture also expected adoption without
  providing a genuinely landed policy commit. These runs remain useful calibration
  and harness evidence but cannot support a pre-merge acceptance decision.

## Decision Log

- 2026-07-15 — Separate instructions, current state, plans, decisions, stable docs,
  backlog, and Git history into purpose-specific artifacts. This reduces stale
  duplication and startup context. See ADR 0001.
- 2026-07-15 — Make GitHub Issues/Projects the target authoritative backlog; retain
  existing roadmaps as design and sequencing references during deliberate migration.
- 2026-07-15 — Permit routine branch, worktree, commit, push, issue, Project, and
  draft-PR actions while reserving merge, history rewriting, deployment, and live
  hardware changes for explicit human approval. See ADR 0002.
- 2026-07-15 — Use deterministic hooks and CI to validate structure and required
  evidence. Automation may flag missing semantic documentation but must not invent
  decisions or rewrite prose automatically.
- 2026-07-15 — Parallelize bounded read-heavy exploration, testing, and review;
  assign one write owner per file/workstream and use isolated worktrees for
  concurrent implementation.
- 2026-07-16 — Keep `MartinHaghani/open_mower_ros` authoritative for current work,
  park the `alm` remote, and publish a clean replacement PR rather than rewriting
  shared PR #22 history. Retarget scheduled jobs only after the clean policy lands.
- 2026-07-16 — Route range checks through a versioned integration-base config rather
  than stale default-branch inference. Human-gate direct pushes to both default and
  integration refs; let reviewed squash commits use the already validated PR
  handoff body while keeping ordinary commits on labeled evidence rules.
- 2026-07-21 — Keep the ARM64 Docker correction separately reviewable in PR #27,
  carry the same reviewed change on PR #24 only to obtain fresh non-publishing
  four-way evidence, and reject manual dispatch, merge, or deployment until that
  matrix is green.
- 2026-08-04 — Split issue #10's rollout into pre-merge governance and post-merge
  activation. The integration-boundary and Projects decision remain pre-merge;
  requiring the policy check and retargeting paused automations occur only after an
  approved merge lands and the workflow passes on its target ref.
- 2026-08-04 — Classify checked-in cases as public calibration only. Pre-merge
  acceptance requires a materially different private rotating holdout outside the
  evaluated repository, sealed hashes, a blindness preflight, and invalidation of
  any trial exposed to its exact specification. Resume testing must model a truly
  landed policy state rather than asking an agent to adopt an unmerged candidate.

## Outcomes & Retrospective

The local operating system is complete and internally consistent in this worktree:
layered documentation, the behavioral skill, bounded custom agents, hooks,
validators, policy CI, GitHub templates, evaluation cases, and Git conventions all
have deterministic coverage. The migration also exposed and assigned every legacy
first-party source TODO instead of silently carrying it forward.

Local verification passes 37 agent-policy tests, nine PR-policy tests, 15/15
fresh-agent context assertions, strict all-scope and changed-scope hygiene,
commit-range validation, Actionlint 1.7.12, Python compilation, JSON/TOML parsing,
the pinned changed-file pre-commit hooks, and whitespace checks. The separately
reviewed Docker correction also passes focused pre-commit, whitespace, and a
disposable ARM64 ROS-base user/group test. Prior validated head `24cad13` passed
all four non-publishing Docker jobs and project policy in
[run 30954272378](https://github.com/MartinHaghani/open_mower_ros/actions/runs/30954272378);
any later head must repeat those checks. No ROS, merge, deployment, or live-hardware
operation was performed.

The remaining rollout is staged. The first public-case cohort was invalidated for
acceptance after answer-key exposure and a semantically incomplete resume fixture;
no acceptance conclusion is drawn from it. A corrected private holdout cohort in
issue #11 remains required before merge. Issue #10 owns the pre-merge
integration-boundary and Projects decision; its required-check and gardening-job
activation steps follow only after an approved merge because they depend on the
landed workflow. Full-tree formatting cleanup remains separate in issue #21. This
plan remains active through PR review, approved merge, and immediate post-merge
activation, then moves to `completed/`.

## Context and Orientation

This repository is a ROS Noetic catkin workspace. Root `AGENTS.md` and nested agent
guides define repository boundaries; [docs/README.md](../../README.md) indexes stable
documentation. Safety-sensitive areas include `src/mower_logic`,
`src/mower_comms_v1`, `src/mower_comms_v2`, hardware-specific parameters, launch
wiring, container entrypoints, and live VESC settings.

The operating-system implementation belongs on `codex/open-mower-agent-os` in
the isolated worktree named above. Do not stage or clean files in the source
worktree. Before editing, inspect `git status --short --branch`, all worktrees, the
active plan, and file ownership assigned to parallel agents.

The documentation sources of truth are defined by ADR 0001. The autonomy boundary
is defined by ADR 0002. Existing build workflows under `.github/workflows/` must be
preserved; new policy checks should call the same deterministic validation entrypoint
as local hooks and pre-commit.

## Plan of Work

First, establish the documentation foundation and routing contract without moving
existing domain docs. Then encode the lifecycle in concise agent instructions and a
focused repository skill so it triggers automatically for implementation work.

Next, add custom subagents for exploration, testing, review, and documentation
audit. Add project hooks only for context routing and deterministic hygiene checks;
the owning agent remains responsible for semantic decisions and edits.

Add one reusable validator that checks internal links, required ExecPlan and ADR
structure, project-state freshness fields, documentation impact declarations, and
prohibited tracking patterns. Run it from pre-commit and a required GitHub Actions
workflow. Add issue and PR templates, CODEOWNERS for safety-sensitive paths, and
document the repository settings that cannot be enforced by checked-in files alone.

Finally, test onboarding and closeout behavior in clean baseline and candidate
checkouts through the issue #11 cohort. Maintain draft PR #24 through that cohort,
issue #10's pre-merge governance, and corrected four-way Docker validation. Keep the
prerequisite Docker correction separately reviewable in draft PR #27. After every
pre-merge gate passes, obtain human merge authorization; complete issue #10's
post-merge activation before archiving this plan.

## Concrete Steps

Work only in the isolated worktree:

```bash
cd /Users/martinhaghani/Code/open_mower_ros_agent_os_rescope
git status --short --branch
git worktree list --porcelain
```

Inspect documentation and policy references before modifying them:

```bash
sed -n '1,240p' AGENTS.md
sed -n '1,240p' docs/PROJECT_STATE.md
sed -n '1,260p' PLANS.md
```

After implementation, run the repository-provided policy validator and existing
relevant checks:

```bash
python3 scripts/agent/check_project_hygiene.py --root . --scope all
python3 -m unittest discover -s scripts/agent/tests -p 'test_*.py'
python3 scripts/agent/evaluate_agent_context.py
python3 .github/scripts/test_validate_pr.py
python3 scripts/agent/validate_commit_message.py \
  --range 329726f..HEAD \
  --exceptions scripts/agent/commit-message-exceptions.json
# After staging only the intended paths:
pre-commit run
git diff --check
git status --short
```

Expected success is a zero exit status, no broken repository-local links, no missing
required sections, and a diff containing only the intended operating-system files.

For the current non-publishing validation gate:

```bash
gh pr view 24 --repo MartinHaghani/open_mower_ros \
  --json headRefOid,isDraft,mergeable,statusCheckRollup
git push origin codex/open-mower-agent-os
gh pr checks 24 --repo MartinHaghani/open_mower_ros --watch --interval 30
```

The expected result is a successful `policy-gate` plus four successful
`validate-pr-build` jobs covering default/legacy on amd64/arm64. The publishing
`build` and `merge` jobs must remain skipped for the pull-request event. Do not use
the baseline workflow's manual-dispatch path because that event publishes images.

## Validation and Acceptance

The migration is accepted only when all of the following are demonstrated:

- A fresh agent can identify the repository baseline, active workstream, exact next
  action, safety boundary, and validation commands from checked-in sources without
  access to the originating conversation.
- Implementation tasks automatically invoke the project workflow, while simple
  questions do not create unnecessary plans, branches, or issues.
- Independent read-heavy tasks are delegated; concurrent agents cannot silently
  write the same workstream.
- A discovered out-of-scope item is created or queued as a structured issue and is
  included in the final outstanding-work report.
- A substantive change missing its required plan, documentation-impact record,
  validation evidence, or PR linkage fails locally and in CI with an actionable
  message.
- Topic-branch commit, push, and draft-PR preparation can run without repeated user
  prompts, while merge, force-push, direct default- or configured integration-branch
  push, deployment, and live hardware operations remain human-gated.
- Existing repository build workflows still parse and the new checks run on pull
  requests. Documentation links and templates validate on a clean checkout.
- `git diff --check` and all added automated tests pass. Any environment-dependent
  check that cannot run is identified with exact reason and follow-up issue.

## Idempotence and Recovery

All new files are additive or narrow policy updates, so the migration can be rerun
and reviewed without touching source work. Validators must be read-only and
idempotent. Hooks may stop a task with an actionable diagnostic but may not modify
prose, stage files, commit, push, merge, or delete worktrees.

If interrupted, start from this plan's `Progress` and verify Git/worktree state
before editing. Preserve partial commits on the topic branch. If parallel edits
overlap, stop the losing writer, inspect both diffs, and integrate deliberately
instead of resetting user work. Do not remove the isolated worktree or branch until
the draft PR is merged or the maintainer explicitly abandons it after confirming no
unique commits remain.

External GitHub configuration should be applied only after the checked-in workflow
is reviewable. If API access or permissions are unavailable, record the exact
settings and pending action in this plan and an issue rather than treating the
migration as complete.

## Artifacts and Interfaces

- Planning policy: `PLANS.md`.
- Current-state router: `docs/PROJECT_STATE.md`.
- Active/completed plan lifecycle: `docs/exec-plans/`.
- Templates: `docs/templates/exec-plan.md` and `docs/templates/adr.md`.
- Durable decisions: `docs/decisions/`.
- Agent behavior: root/nested `AGENTS.md` and the repository operations skill added
  by this migration.
- Agent roles and hooks: `.codex/agents/` and project hook configuration added by
  this migration.
- Deterministic checks: repository validation scripts, pre-commit, and GitHub Actions
  added by this migration.
- Machine authority: `scripts/agent/project-policy.json`.
- Tracking/review: GitHub Issues, Project items, pull-request template, CODEOWNERS,
  draft PR, and protected-branch settings.
- Current review and validation: Agent OS draft PR
  [#24](https://github.com/MartinHaghani/open_mower_ros/pull/24), immediate Docker
  issue [#25](https://github.com/MartinHaghani/open_mower_ros/issues/25), focused
  fix draft PR [#27](https://github.com/MartinHaghani/open_mower_ros/pull/27), and
  host-aware device-access follow-up
  [#26](https://github.com/MartinHaghani/open_mower_ros/issues/26).

## Plan Change Log

- 2026-07-15 — Created the self-contained migration plan and recorded the initial
  documentation foundation, decisions, evidence, and remaining milestones.
- 2026-07-15 — Completed the local automation and governance layers, applied
  repository settings, migrated backlog/TODO ownership to issues #1–#20, recorded
  the Projects OAuth boundary in issue #10, and captured verification evidence.
- 2026-07-15 — Replaced attempted full-tree formatting with a changed-file ratchet,
  tracked inherited debt in issue #21, added the exact legacy-marker register, and
  incorporated independent correctness and documentation review findings.
- 2026-07-16 — Re-scoped the implementation to a new OpenMower-only branch, added
  clean commit-range enforcement and repository-authority regression checks, and
  paused the two incorrectly targeted scheduled jobs pending post-merge retargeting.
- 2026-07-17 — Recorded the final 37-test policy matrix and independent review
  results before publishing the clean replacement draft PR.
- 2026-07-21 — Recorded draft PR #24 publication, the ARM64 default-image failure,
  focused issues #25/#26 and draft PR #27, the non-publishing validation route, and
  the explicit no-merge/no-deploy gate.
- 2026-07-21 — Recorded fresh green policy and default/legacy by amd64/arm64
  validation on corrected head `b14d647`; publishing remained skipped and both PRs
  remained draft and unmerged.
- 2026-08-04 — Reconciled tracking to current validated head `b6a39f3` and run
  `29794246511`, marked the issue #11 candidate cohort in progress, and split issue
  #10 into pre-merge governance and post-merge activation. No merge, deployment, or
  live-hardware operation was performed.
- 2026-08-04 — Invalidated the public-case cohort for acceptance, preserved it as
  calibration evidence, separated public calibration from a blind private holdout,
  and corrected the resume-fixture requirement to use a synthetic landed policy
  state. No merge, deployment, or live-hardware operation was performed.
