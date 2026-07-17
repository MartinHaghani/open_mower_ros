#!/usr/bin/env python3
"""Tests for the repository commit-message policy."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "validate_commit_message.py"
SPEC = importlib.util.spec_from_file_location("validate_commit_message", SCRIPT)
assert SPEC and SPEC.loader
POLICY = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = POLICY
SPEC.loader.exec_module(POLICY)


class CommitMessageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def git(self, *args: str, env=None) -> str:
        result = subprocess.run(
            ["git", *args],
            cwd=str(self.root),
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        return result.stdout.strip()

    def init_repo(self) -> None:
        self.git("init")
        self.git("config", "user.name", "Policy Test")
        self.git("config", "user.email", "policy@example.invalid")
        self.git("config", "commit.gpgsign", "false")

    def commit(
        self,
        message: str,
        index: int,
        author_name: str = "Policy Test",
        author_email: str = "policy@example.invalid",
        verbatim: bool = False,
    ) -> str:
        (self.root / "file-{}.txt".format(index)).write_text("{}\n".format(index), encoding="utf-8")
        self.git("add", ".")
        env = os.environ.copy()
        env["GIT_AUTHOR_NAME"] = author_name
        env["GIT_AUTHOR_EMAIL"] = author_email
        commit_args = ["commit"]
        if verbatim:
            commit_args.append("--cleanup=verbatim")
        commit_args.extend(("-m", message))
        self.git(*commit_args, env=env)
        return self.git("rev-parse", "HEAD")

    def write_exceptions(self, entries) -> Path:
        path = self.root / "exceptions.json"
        path.write_text(json.dumps({"version": 1, "exceptions": entries}), encoding="utf-8")
        return path

    def install_pr_validator(self) -> None:
        source = SCRIPT.parents[2] / ".github" / "scripts" / "validate_pr.py"
        destination = self.root / ".github" / "scripts" / "validate_pr.py"
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")

    @staticmethod
    def valid_pr_handoff() -> str:
        return """feat(test): land reviewed change

## Outcome

The reviewed behavior is now available on the integration branch.

## Tracking

- **Issue:** Closes #1
- **ExecPlan:** N/A because this fixture is intentionally self-contained.

## Key decisions

Preserve the reviewed implementation and its exact validation evidence.

## Documentation impact

- **Documentation updated:** This synthetic handoff is the complete test fixture.

## Safety and rollback

- **Safety impact:** None because the fixture changes no runtime behavior.
- **Rollback:** Revert this synthetic squash commit.

## Verification

- `python3 -m unittest` — Pass: the focused policy tests completed.

## Known limitations and follow-ups

- **Known limitations:** None because this is a bounded policy fixture.
- **Follow-up issues:** None because the fixture is complete.
"""

    def test_conventional_subject_passes(self) -> None:
        self.assertEqual([], POLICY.validate("docs(agent): add context router\n", "never", self.root))

    def test_nonconventional_subject_fails(self) -> None:
        errors = POLICY.validate("update everything\n", "never", self.root)
        self.assertTrue(any("type(scope): subject" in error for error in errors))

    def test_generated_and_rebase_subjects_pass(self) -> None:
        for message in ('Merge branch \'main\'\n', 'Revert "fix: bad change"\n\nThis reverts commit abc.\n', "fixup! old historical subject\n"):
            self.assertEqual([], POLICY.validate(message, "always", self.root))

    def test_required_body_needs_rationale_and_validation(self) -> None:
        errors = POLICY.validate("fix(comms): reconnect safely\n", "always", self.root)
        self.assertEqual(3, len(errors))
        message = "fix(comms): reconnect safely\n\nRationale: preserve RTCM delivery.\nValidation: focused reconnect test passes.\nRefs: #123\n"
        self.assertEqual([], POLICY.validate(message, "always", self.root))

    def test_substantive_body_requires_issue_reference(self) -> None:
        message = "docs(agent): explain state\n\nRationale: preserve context.\nValidation: links pass.\n"
        errors = POLICY.validate(message, "always", self.root)
        self.assertTrue(any("Refs: #123" in error for error in errors))

    def test_staged_change_inspection_fails_closed(self) -> None:
        errors = POLICY.validate("chore(agent): update policy\n", "auto", self.root)
        self.assertTrue(any("cannot inspect staged changes" in error for error in errors))

    def test_body_requires_blank_separator(self) -> None:
        errors = POLICY.validate("feat(map): add route\nRationale: needed\nValidation: tested\nRefs: #123\n", "always", self.root)
        self.assertTrue(any("blank line" in error for error in errors))

    def test_commit_range_enforces_substantive_body(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("fix(test): expose missing range check", 2)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any("needs Rationale" in error for error in errors))
        self.assertTrue(any(head[:12] in error for error in errors))

    def test_commit_range_accepts_documented_body_exception(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("fix(test): preserve published history", 2)
        exceptions = self.write_exceptions(
            [
                {
                    "sha": head,
                    "reason": "Published before range enforcement and retained without rewriting history.",
                    "issue": "#1",
                }
            ]
        )
        self.assertEqual([], POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions))

    def test_body_exception_does_not_waive_subject_policy(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("update everything", 2)
        exceptions = self.write_exceptions(
            [
                {
                    "sha": head,
                    "reason": "Only evidence-body requirements may be waived for a published commit.",
                    "issue": "#1",
                }
            ]
        )
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any("type(scope): subject" in error for error in errors))

    def test_commit_range_rejects_autosquash_subject(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("fixup! fix(test): earlier change", 2)
        exceptions = self.write_exceptions(
            [
                {
                    "sha": head,
                    "reason": "Body exceptions must not waive review-range subject integrity.",
                    "issue": "#1",
                }
            ]
        )
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any("must be squashed" in error for error in errors))

    def test_commit_range_rejects_fake_merge_subject(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("Merge branch 'main'", 2)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any("non-merge commit" in error for error in errors))

    def test_generated_revert_requires_evidence_in_commit_range(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit('Revert "fix(test): unsafe change"', 2)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any("needs Rationale" in error for error in errors))

    def test_subject_only_range_policy_supports_generated_bot_commits(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("ci(deps): bump generated lock data", 2)
        exceptions = self.write_exceptions([])
        self.assertEqual(
            [],
            POLICY.validate_range(
                self.root,
                "{}..{}".format(base, head),
                exceptions,
                body_policy="never",
            ),
        )

    def test_dependabot_mode_accepts_canonical_bump_subject(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit(
            "Bump vite from 8.0.14 to 8.1.4 in /webui",
            2,
            author_name="dependabot[bot]",
            author_email="49699333+dependabot[bot]@users.noreply.github.com",
        )
        exceptions = self.write_exceptions([])
        self.assertEqual(
            [],
            POLICY.validate_range(
                self.root,
                "{}..{}".format(base, head),
                exceptions,
                allow_dependabot_subjects=True,
            ),
        )

    def test_dependabot_mode_accepts_configured_dependency_subject(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        self.commit(
            "ci(deps): bump actions/checkout from 4 to 5",
            2,
            author_name="dependabot[bot]",
            author_email="49699333+dependabot[bot]@users.noreply.github.com",
        )
        head = self.commit(
            "ci(deps): bump generated dependency metadata from 1 to 2",
            3,
            author_name="dependabot[bot]",
            author_email="49699333+dependabot[bot]@users.noreply.github.com",
        )
        exceptions = self.write_exceptions([])
        self.assertEqual(
            [],
            POLICY.validate_range(
                self.root,
                "{}..{}".format(base, head),
                exceptions,
                allow_dependabot_subjects=True,
            ),
        )

    def test_dependabot_mode_does_not_exempt_ordinary_human_commit(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        self.commit(
            "Bump vite from 8.0.14 to 8.1.4 in /webui",
            2,
            author_name="dependabot[bot]",
            author_email="49699333+dependabot[bot]@users.noreply.github.com",
        )
        head = self.commit("fix(test): add human follow-up without evidence", 3)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(
            self.root,
            "{}..{}".format(base, head),
            exceptions,
            allow_dependabot_subjects=True,
        )
        self.assertTrue(any(head[:12] in error and "needs Rationale" in error for error in errors))

    def test_dependabot_mode_does_not_exempt_human_dependency_subject(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        (self.root / "second-policy-file.txt").write_text("substantive\n", encoding="utf-8")
        head = self.commit("ci(deps): bump safety policy from strict to disabled", 2)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(
            self.root,
            "{}..{}".format(base, head),
            exceptions,
            allow_dependabot_subjects=True,
        )
        self.assertTrue(any(head[:12] in error and "needs Rationale" in error for error in errors))

    def test_reviewed_squash_handoff_satisfies_substantive_evidence(self) -> None:
        self.init_repo()
        self.install_pr_validator()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit(self.valid_pr_handoff(), 2)
        exceptions = self.write_exceptions([])
        self.assertEqual([], POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions))

    def test_incomplete_squash_handoff_does_not_bypass_evidence(self) -> None:
        self.init_repo()
        self.install_pr_validator()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit(
            "feat(test): incomplete squash handoff\n\n## Outcome\n\n<!-- placeholder -->\n",
            2,
        )
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any(head[:12] in error and "needs Rationale" in error for error in errors))

    def test_valid_squash_handoff_does_not_waive_long_subject(self) -> None:
        self.init_repo()
        self.install_pr_validator()
        base = self.commit("docs(test): seed repository", 1)
        message = self.valid_pr_handoff().replace(
            "feat(test): land reviewed change",
            "feat(test): {}".format("x" * 70),
            1,
        )
        head = self.commit(message, 2)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any(head[:12] in error and "exceeds 72" in error for error in errors))

    def test_range_preserves_committed_hash_prefixed_subject(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit(
            "# invalid committed subject\n\nfix(test): misleading second line\n\nRationale: no.\nValidation: no.\nRefs: #1",
            2,
            verbatim=True,
        )
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any(head[:12] in error and "type(scope): subject" in error for error in errors))

    def test_canonical_bump_subject_is_not_allowed_for_human_range(self) -> None:
        self.init_repo()
        base = self.commit("docs(test): seed repository", 1)
        head = self.commit("Bump vite from 8.0.14 to 8.1.4 in /webui", 2)
        exceptions = self.write_exceptions([])
        errors = POLICY.validate_range(self.root, "{}..{}".format(base, head), exceptions)
        self.assertTrue(any("type(scope): subject" in error for error in errors))

    def test_exception_registry_fails_closed(self) -> None:
        path = self.write_exceptions(
            [{"sha": "deadbeef", "reason": "too short", "issue": "issue 23"}]
        )
        _, errors = POLICY._load_exception_shas(path)
        self.assertTrue(any("full 40-character" in error for error in errors))

    def test_repository_bootstrap_registry_is_empty(self) -> None:
        path = SCRIPT.parent / "commit-message-exceptions.json"
        shas, errors = POLICY._load_exception_shas(path)
        self.assertEqual([], errors)
        self.assertEqual(set(), shas)


if __name__ == "__main__":
    unittest.main()
