# DOC-2-097 Cross-Disease Repair Program - PROTOCOL (lock-1)

Status: frozen before any real-data scoring. Results label: review pending until the independent gate clears.

## Question
Do DNA-repair genes (MSigDB Hallmark 2020 "DNA Repair") show a net up-regulated direction across many disease expression signatures, beyond matched random gene sets? Descriptive, public-data only. No clinical or causal claim.

## Data (public, no secrets)
- CREEDS disease signatures v1.0 (Gundersen/Ma'ayan lab), https://maayanlab.cloud/CREEDS/download/disease_signatures-v1.0.json. Site states all contents are CC BY 4.0. Underlying data are from NCBI GEO, whose data are public; GEO terms: https://www.ncbi.nlm.nih.gov/geo/info/disclaimer.html. Cite CREEDS (Wang et al., Nat Commun 2016) and GEO.
- MSigDB Hallmark 2020 via Enrichr library text endpoint. Enrichr library terms not separately verified; the gene set is used as a list of symbols only and is cited, not redistributed in this repo.
- Files are downloaded by acquire_097.py and hashed (DATA_HASHES.tsv). Raw data are not committed.
- Pre-lock grounding (not scoring): CREEDS has 828 signatures (555 human, 215 mouse, 58 rat); human GPL570 n=246, GPL96 n=96. Counts only, no outcome looked at.

## Unit and primary analysis
- Primary population: human signatures on platform GPL570 (single platform, removes cross-platform and cross-species mixing). Symbols upper-cased.
- Per gene: net_up = (fraction of signatures where gene is in the up list) - (fraction where in the down list).
- Statistic: mean net_up over Hallmark DNA Repair genes found in the signature universe.
- Null: matched random gene sets. Genes are binned into deciles of promiscuity (total appearances in up+down lists). Each null set draws the same number per decile from non-target genes. 10,000 draws. One-sided p = (1 + #null >= obs)/(1 + 10,000). Effect = obs - null mean.
- Uncertainty: bootstrap over GEO series (GSE) as clusters, 2,000 resamples; 95% percentile CI on effect. Signatures from the same GSE are not independent.

## Floor
If fewer than 100 distinct GSE series or fewer than 100 target genes in the primary population: label INSUFFICIENT-DATA, stop, report. No loosening.

## Gates
- G1 (calibration, must pass first): 200 random size-matched pseudo-target sets through the same matched-null test (1,000 draws each, no bootstrap); false-positive rate at p<0.05 must be <= 0.10. Fail: label INVALID.
- G2 (effect): p < 0.01 AND effect >= 0.02 AND bootstrap CI lower bound > 0.
- Labels: INSUFFICIENT-DATA; INVALID (G1 fail); REPAIR-SET-UP-BIASED-CROSS-DISEASE (G1 and G2 pass); HONEST NEGATIVE (otherwise).
- Reported only, no gate role: non-neoplastic subset (regex on disease name, in analysis_097.py); Hallmark G2-M Checkpoint as a proliferation reference set; GPL96 replicate.

## Declared primary limit
GEO batch and platform confounding. Signatures come from heterogeneous studies, tissues, case/control designs and curation choices. Matched random sets control gene promiscuity, not batch, tissue, proliferation or study design. A positive result would show a pattern of direction across these signatures, not that repair is a disease mechanism. Proliferation (many repair genes are cell-cycle genes) is a named alternative explanation, hence the G2-M reference set. Species/platform other than GPL570 are out of the primary claim.

## Not claimed
No causation, no therapeutic claim, no cross-species claim, no gene-level claims.

## Receipts
Raw logs, results.json, run_log (command, UTC times, versions, md5s), tag-tree check, repo plus Drive mirror. Amendments are new dated files committed before outcomes.

## Release
No real-data run until the lock-1 release by the program owner.
