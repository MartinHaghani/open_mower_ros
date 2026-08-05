# Evaluation results

Store privacy-safe cohort summaries here as
`YYYY-MM-DD-<baseline>-vs-<candidate>.md`. Start from
[the baseline template](../BASELINE_TEMPLATE.md) and link individual scorecards or
private traces without copying secrets, private yard data, raw chain-of-thought, or
large terminal transcripts into the repository.

Every result must use immutable commit SHAs, preserve failed trials, and link
[issue #11](https://github.com/MartinHaghani/open_mower_ros/issues/11). If a result
is invalidated by a fixture, prompt, model, or telemetry problem, keep it and mark
the reason rather than deleting an inconvenient outcome.

Do not publish active holdout prompts, fixtures, expected behavior, scoring keys,
or fixture builders. Publish capability labels, version identifiers, hashes,
aggregate measurements, sanitized findings, and privacy-safe evidence references
only.

Preserve every invalidated trial with its immutable trial ID, cohort and commit,
invalidation reason, artifact hashes or private references, and
excluded-from-aggregate status. Never delete or overwrite a leaked, unsuccessful,
timed-out, or incomplete run. Retired holdout material may be disclosed only after
deliberate rotation and an issue #11 record that it is no longer active acceptance
material.
