"""DOC-2-097 frozen analysis (PROTOCOL.md lock-1). Run once. Needs creeds.json, hallmark.gmt."""
import json, re, numpy as np
rng = np.random.default_rng(12345)
D = json.load(open("creeds.json")); H = {l.split("\t")[0]: [g for g in l.rstrip("\n").split("\t")[2:] if g] for l in open("hallmark.gmt")}
NEO = re.compile(r"cancer|carcinoma|leukemia|leukaemia|lymphoma|tumou?r|neoplas|melanoma|sarcoma|glioma|glioblastoma|myeloma|adenoma|blastoma", re.I)
def build(platform, nonneo=False):
    S = [s for s in D if s["organism"] == "human" and s["platform"] == platform and not (nonneo and NEO.search(s["disease_name"] or ""))]
    genes = sorted({g[0].upper() for s in S for g in s["up_genes"] + s["down_genes"]}); gi = {g: i for i, g in enumerate(genes)}
    U = np.zeros((len(S), len(genes)), dtype=np.float32); Dn = np.zeros_like(U)
    for k, s in enumerate(S):
        for g in s["up_genes"]: U[k, gi[g[0].upper()]] = 1
        for g in s["down_genes"]: Dn[k, gi[g[0].upper()]] = 1
    return S, genes, gi, U, Dn
def run(platform, setname, nonneo=False, nnull=10000, boot=True, target=None):
    S, genes, gi, U, Dn = build(platform, nonneo); N = len(S); gse = np.array([s["geo_id"] for s in S])
    T = target if target is not None else sorted({gi[g] for g in H[setname] if g in gi}); out = dict(platform=platform, set=setname, n_signatures=N, n_gse=int(len(set(gse))), n_target_genes=len(T))
    if N == 0 or len(T) < 100: out["insufficient"] = True; return out
    net = (U.sum(0) - Dn.sum(0)) / N; tot = U.sum(0) + Dn.sum(0); G = len(genes)
    edges = np.unique(np.quantile(tot, np.linspace(0, 1, 11))); b = np.clip(np.searchsorted(edges, tot, side="right") - 1, 0, len(edges) - 2); nb = len(edges) - 1
    isT = np.zeros(G, bool); isT[T] = True; need = np.bincount(b[isT], minlength=nb); pools = [np.where((b == k) & ~isT)[0] for k in range(nb)]
    obs = net[T].mean(); nulls = np.zeros(nnull)
    for i in range(nnull): nulls[i] = np.mean(np.concatenate([net[rng.choice(pools[k], need[k], replace=False)] for k in range(nb) if need[k] > 0]))
    out.update(obs_net_up=float(obs), null_mean=float(nulls.mean()), effect=float(obs - nulls.mean()), p_one_sided=float((1 + (nulls >= obs).sum()) / (1 + nnull)))
    if boot:
        ug = sorted(set(gse)); idx = {g: np.where(gse == g)[0] for g in ug}; eff = []
        for _ in range(2000):
            w = np.zeros(N)
            for g in rng.choice(ug, len(ug)): w[idx[g]] += 1
            nb_ = (w @ U - w @ Dn) / w.sum(); eff.append(nb_[T].mean() - sum(need[k] * nb_[pools[k]].mean() for k in range(nb) if need[k] > 0) / need.sum())
        out["effect_ci95"] = [float(x) for x in np.percentile(eff, [2.5, 97.5])]
    return out
res = {}; prim = run("GPL570", "DNA Repair"); res["primary"] = prim
if prim.get("insufficient") or prim["n_gse"] < 100:
    res["LABEL"] = "INSUFFICIENT-DATA"
else:
    S, genes, gi, U, Dn = build("GPL570"); N = len(S); net = (U.sum(0) - Dn.sum(0)) / N; tot = U.sum(0) + Dn.sum(0); G = len(genes); k0 = prim["n_target_genes"]
    rej = 0; ncal = 200
    for _ in range(ncal):  # G1 calibration: random size-matched pseudo-target sets through the same test (1,000 null draws, no bootstrap)
        T = sorted(rng.choice(G, k0, replace=False)); r = run("GPL570", "DNA Repair", nnull=1000, boot=False, target=T); rej += r["p_one_sided"] < 0.05
    res["G1"] = dict(false_positive_rate=rej / ncal, pass_=bool(rej / ncal <= 0.10))
    res["G2"] = dict(effect=prim["effect"], ci=prim["effect_ci95"], p=prim["p_one_sided"], pass_=bool(prim["p_one_sided"] < 0.01 and prim["effect"] >= 0.02 and prim["effect_ci95"][0] > 0))
    res["LABEL"] = "INVALID" if not res["G1"]["pass_"] else ("REPAIR-SET-UP-BIASED-CROSS-DISEASE" if res["G2"]["pass_"] else "HONEST NEGATIVE")
    res["reported_only"] = dict(non_neoplastic=run("GPL570", "DNA Repair", nonneo=True), G2M_reference_set=run("GPL570", "G2-M Checkpoint"), GPL96_replicate=run("GPL96", "DNA Repair"))
print("RESULT_JSON", json.dumps(res, default=float)); open("results.json", "w").write(json.dumps(res, default=float, indent=1))
