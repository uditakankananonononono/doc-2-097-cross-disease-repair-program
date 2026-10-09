# DOC-2-097 A1 RESULTS - independent gate verdict: SCOPED PASS as HONEST NEGATIVE

Label (set mechanically by analysis_097_A1.py): **HONEST NEGATIVE [post-floor-miss population change (A1); second look; platform-pooled]**.

Population: all 555 human CREEDS signatures (341 GSE, 44 platforms), 133 of 150 Hallmark DNA Repair genes in the universe. Floors met. G1 passed (false-positive rate 0.055, limit 0.10).

| item | value |
|---|---|
| primary: mean net-up of DNA Repair genes | observed 0.00596; matched-null mean 0.00037; effect 0.00559, GSE-bootstrap 95% CI [0.00264, 0.00855]; one-sided p = 0.0011 (10,000 draws) |
| G2 (p < 0.01 AND effect >= 0.02 AND CI lower > 0) | **fail**: p and CI pass, effect size threshold (0.02) not met by a factor of about 3.6 |
| reported only: non-neoplastic (420 sigs, 257 GSE, 127 genes) | effect 0.00314, CI [0.00003, 0.00621], p = 0.028 |
| reported only: G2-M Checkpoint reference set (179 genes) | effect 0.00572, CI [0.00139, 0.01003], p = 0.0001 |
| reported only: coverage-adjusted DNA Repair | effect 0.00185, p = 0.457. The CI printed in results.json for this row is NOT valid (the bootstrap inside run() does not use the adjusted denominator); ignore it. In results_A1.json this CI is set to null and flagged; the unaltered program output is in analysis_A1.log |
| reported only: GPL96-only (96 sigs, 74 GSE, 67 genes), GPL570-only (246 sigs, 129 GSE, 98 genes) | INSUFFICIENT-DATA (floor), as expected |

## What this shows and does not show
- Across pooled human disease signatures, DNA Repair genes show a small offset (0.0056) relative to promiscuity-matched random genes that is not specific to DNA Repair and is largely attributable to platform coverage (reported-only proxy). It is statistically distinguishable from the matched null but tiny and far under the pre-set effect floor. The label is HONEST NEGATIVE under the locked gates, not a finding that repair is uninvolved.
- The G2-M Checkpoint proliferation reference set shows a similar effect (0.0057), so the proliferation alternative explanation is not ruled out and the repair-specific reading is not supported.
- The effect shrinks to 0.0019 (p = 0.46) when the denominator is limited to signatures on platforms that cover the gene. This is consistent with a coverage contribution but does not establish that coverage explains the offset. The proxy is crude: the platform gene universe is inferred from genes that ever appear in that platform's signatures, so low-promiscuity genes get small denominators.
- Primary declared limit: GEO batch and platform confounding, plus pooling of 44 platforms. Heterogeneous studies and curation. No causal, mechanistic or therapeutic claim.

## Disclosures
- This is a post-floor-miss population change (A1); second look; platform-pooled. The lock-1 run (GPL570 only) was INSUFFICIENT-DATA at 98/150 genes. After that stop I counted overlap only (555/341/19,187/133 of 150); no outcome statistic was computed before AMENDMENT-2026-10-10-A1.md.
- Gate-derived: the independent gate reviewed the A1 amendment at 4cf15432 (SCOPED PASS, fixes landed at 144e2351) before the run. After the run it independently reproduced this result (same values at every field except 16th-digit float rounding) and gave SCOPED PASS as HONEST NEGATIVE with the two wording corrections applied here (relayed by the program owner's main agent).
- Run once from 144e235144868307bcf05b24ea2006bdef08afae, analysis_097_A1.py unchanged (md5 87fcf6bd3bba3b3dbc458fff0f206f1b), same data files as lock-1 run (md5 in run_log). 2026-10-09T20:07:22Z to 20:11:56Z, exit 0, Python 3.10.12, numpy 2.2.6.
- The 0.02 effect floor was my pre-lock choice and was not calibrated; the primary effect is 0.0056, so the label would not change at any plausible threshold between 0.006 and 0.02 but a lower floor (for example 0.005) would flip G2. It was not changed.
- Descriptive only; no multiplicity control across the reported-only rows.
