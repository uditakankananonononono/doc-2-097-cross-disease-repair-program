# DOC-2-097 AMENDMENT A1 (dated 2026-10-10, committed before any A1 outcome; unfrozen until gate review)

Background: the lock-1 run (tag lock-1, RESULTS.md at tip fda8d59d) stopped at the floor: GPL570 had 246 signatures / 129 GSE but only 98 of 150 Hallmark DNA Repair genes in its universe (floor >= 100). That result stands as INSUFFICIENT-DATA and is not edited.

## Change (new unit, not a floor relaxation)
- Population: ALL 555 human CREEDS disease signatures, all platforms (analysis_097_A1.py; "ALL"). Mouse and rat remain excluded.
- Floors unchanged: >= 100 distinct GSE and >= 100 target genes.
- Statistic, matched null (decile promiscuity, 10,000 draws), GSE-clustered bootstrap (2,000), G1 (200 pseudo-targets, FPR <= 0.10 else INVALID), G2 (p < 0.01, effect >= 0.02, CI lower > 0), and labels are identical to PROTOCOL.md.
- Reported only (no gate role): non-neoplastic subset, G2-M Checkpoint reference set, GPL96-only (expected INSUFFICIENT-DATA), GPL570-only (expected INSUFFICIENT-DATA; already known, 98 genes), and a coverage-adjusted descriptive (net_up denominator = signatures on platforms whose signatures ever contain the gene, a proxy for platform gene coverage; same matched null and bootstrap). Added after gate review (fix 1 and gate's limits note); script and amendment now agree.
- Label rule: any A1 result label, in RESULTS.md and any summary, carries the text "post-floor-miss population change (A1); second look; platform-pooled". The script appends it to the label line.

## Pre-amendment counts (disclosed; no outcome statistic was computed)
All human: 555 signatures, 341 GSE, 19,187 genes in the universe, 133 of 150 Hallmark DNA Repair genes present. Floors would be met. These counts were looked at after the lock-1 stop and before writing this amendment; that is the only data-dependent input to this choice. Note that lock-1 PROTOCOL.md already listed the 555 human signatures before locking; the new data-dependent fact is gene coverage (133/150), not the signature count.

## Added declared limits
- Pooling platforms and probe-to-symbol mappings raises the platform/batch confound relative to the GPL570-only design. Platform is not modelled; matched nulls control gene promiscuity only. This remains the primary declared limit.
- Because the population was changed after a floor miss, this is a second look at the same question and must be reported as such; a positive result would carry that caveat.
- 44 platforms are pooled. Differences in gene coverage across platforms dilute net_up toward zero, which the promiscuity-matched null only partly handles; the coverage-adjusted descriptive is reported to show this, and no claim is made before it is read alongside the primary. 98 of 341 GSE contribute more than one signature; the GSE-clustered bootstrap addresses this.
- GPL570 is a subset of this population, so GPL570-only is not independent.

## Release
Not to be run until the independent gate reviews this amendment and the owner releases it.
