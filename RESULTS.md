# DOC-2-097 RESULTS - review pending (independent gate has not cleared)

Label (set mechanically by analysis_097.py under the lock-1 floor): **INSUFFICIENT-DATA**. No effect size, p-value or gate G1/G2 was computed. This is a protocol stop, not a negative finding about DNA repair.

| item | value |
|---|---|
| primary population | human GPL570 signatures: 246 signatures from 129 distinct GSE series (GSE floor of 100 met) |
| target set | Hallmark 2020 "DNA Repair": 150 listed genes, **98 found in the GPL570 signature gene universe** |
| floor | >= 100 target genes: **not met (98 < 100)** |
| outcome | analysis stopped at the floor; results.json holds only the counts above and the label |

## Disclosures
- The floor was fixed at lock-1 and was not loosened. The pre-lock grounding counted signatures (246 GPL570) but did not check how many Hallmark genes appear in the universe; that count was first seen at the run. The shortfall is 2 genes.
- Run once: acquire_097.py then analysis_097.py, unchanged from tag lock-1 (8afeec5d). Python run on this sandbox; exit code 0. Start 2026-10-09T20:00:11Z, end 2026-10-09T20:00:14Z (see run_log.txt for md5s).
- The G1 calibration, matched-null test, G2-M reference set, non-neoplastic subset and GPL96 replicate were not run (they follow the primary).
- Any follow-up (for example a different target set, or counting genes across all human platforms) is a new, dated amendment committed before its outcome, and needs its own review. It is not part of this result.
