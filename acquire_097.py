"""DOC-2-097: download CREEDS disease signatures (CC BY 4.0) and the Enrichr MSigDB Hallmark 2020 library. Writes creeds.json, hallmark.gmt, DATA_HASHES.tsv."""
import hashlib, requests
out = ["file\tmd5\tbytes\turl"]
for name, url in [("creeds.json", "https://maayanlab.cloud/CREEDS/download/disease_signatures-v1.0.json"), ("hallmark.gmt", "https://maayanlab.cloud/Enrichr/geneSetLibrary?mode=text&libraryName=MSigDB_Hallmark_2020")]:
    r = requests.get(url, timeout=300); r.raise_for_status(); open(name, "wb").write(r.content); out.append(f"{name}\t{hashlib.md5(r.content).hexdigest()}\t{len(r.content)}\t{url}")
open("DATA_HASHES.tsv", "w").write("\n".join(out) + "\n"); print("ACQ_DONE")
