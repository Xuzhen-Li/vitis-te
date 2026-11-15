#!/usr/bin/env python3
"""Estimate LTR pairwise divergence (p-distance and K2P) from two equal-length sequences.

Inputs:  --fa --bed (LTR5 and LTR3 rows) OR --ltr5 and --ltr3 FASTA
         --rate optional, substitutions per site per year, no default
         --rate-source optional free text recorded in the output
Outputs: --out-tsv with n, substitutions, p_distance, k2p, years, rate, rate_source.
Tested:  planted tiny genome from 00_make_tiny_genome.py.
Production: use LTR_retriever / equivalent on curated annotations
(docs/WORKFLOW.md). Age in years uses T = K / (2r), because the two LTRs
accumulate substitutions independently. This script never applies a default
rate. Years are written only when --rate is given; otherwise they are NA.
If r is already in substitutions per site per year, no generation time is
needed. A per-generation rate would have to be converted first; in a clonal
crop the sexual generation interval is long and uncertain (see vitis-popgen
WORKFLOW decision 7). Gene conversion between the two LTRs makes the
estimated age too young. Real LTRs often differ in length; align them before
computing K, which this script does not do (it requires equal length).
When --fa and --bed are used, sequences are read by chromosome name (the
first token of each FASTA header) and sliced with the BED chrom, start and
end (0-based, half-open). Records are never concatenated.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path


def read_fa_records(path: Path) -> dict[str, str]:
    recs = {}
    name, seq = None, []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith(">"):
                if name is not None:
                    recs[name] = "".join(seq).upper()
                name = line[1:].strip().split()[0]
                seq = []
            else:
                seq.append(line.strip())
    if name is not None:
        recs[name] = "".join(seq).upper()
    if not recs:
        raise SystemExit(f"no FASTA records in {path}")
    return recs


def one_seq(path: Path) -> str:
    recs = read_fa_records(path)
    if len(recs) != 1:
        raise SystemExit(f"{path} must contain exactly one record when used as --ltr5 or --ltr3")
    return next(iter(recs.values()))


def slice_by_bed(recs: dict[str, str], chrom: str, start: int, end: int, label: str) -> str:
    if chrom not in recs:
        raise SystemExit(f"{label}: chromosome {chrom} not in FASTA")
    s = recs[chrom]
    if start < 0 or end < start or end > len(s):
        raise SystemExit(f"{label}: BED {chrom}:{start}-{end} is outside sequence length {len(s)}")
    return s[start:end]


def parse_bed(path: Path):
    rows = {}
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            chrom, start, end, name = line.rstrip("\n").split("\t")[:4]
            rows[name] = (chrom, int(start), int(end))
    return rows


def k2p(s1: str, s2: str):
    n = 0
    ts = tv = 0
    trans = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
    for a, b in zip(s1, s2):
        if a not in "ACGT" or b not in "ACGT":
            continue
        n += 1
        if a == b:
            continue
        if (a, b) in trans:
            ts += 1
        else:
            tv += 1
    if n == 0:
        return 0, 0, math.nan, math.nan
    p = (ts + tv) / n
    P = ts / n
    Q = tv / n
    try:
        d = -0.5 * math.log(1 - 2 * P - Q) - 0.25 * math.log(1 - 2 * Q)
    except ValueError:
        d = math.nan
    return n, ts + tv, p, d


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fa")
    ap.add_argument("--bed")
    ap.add_argument("--ltr5")
    ap.add_argument("--ltr3")
    ap.add_argument("--out-tsv", required=True)
    ap.add_argument("--rate", type=float, default=None,
                    help="substitutions per site per year; no default; required for years")
    ap.add_argument("--rate-source", default="",
                    help="free-text source for --rate, recorded in the output")
    args = ap.parse_args()
    if args.fa and args.bed:
        recs = read_fa_records(Path(args.fa))
        bed = parse_bed(Path(args.bed))
        for label in ("LTR5", "LTR3"):
            if label not in bed:
                raise SystemExit(f"BED is missing a {label} row")
        chrom5, a, b = bed["LTR5"]
        chrom3, c, d = bed["LTR3"]
        s1 = slice_by_bed(recs, chrom5, a, b, "LTR5")
        s2 = slice_by_bed(recs, chrom3, c, d, "LTR3")
    elif args.ltr5 and args.ltr3:
        s1, s2 = one_seq(Path(args.ltr5)), one_seq(Path(args.ltr3))
    else:
        raise SystemExit("provide --fa and --bed, or --ltr5 and --ltr3")
    if len(s1) != len(s2):
        raise SystemExit(f"LTR lengths differ: {len(s1)} vs {len(s2)}; align first")
    n, subs, p, d = k2p(s1, s2)
    if args.rate is not None:
        if args.rate <= 0:
            raise SystemExit("--rate must be positive")
        years = d / (2.0 * args.rate) if d == d else math.nan
        rate_s = f"{args.rate}"
        src = args.rate_source if args.rate_source else "user-supplied --rate"
    else:
        years = math.nan
        rate_s = "NA"
        src = "NA"
    def fmt(x):
        return f"{x:.8f}" if x == x else "NA"
    with Path(args.out_tsv).open("x", encoding="utf-8") as f:
        f.write("n_sites\tsubstitutions\tp_distance\tk2p\tyears\trate_per_site_per_year\trate_source\n")
        f.write(f"{n}\t{subs}\t{p:.8f}\t{fmt(d)}\t{fmt(years)}\t{rate_s}\t{src}\n")
    print("n", n, "subs", subs, "p", p, "k2p", d,
          "years" + ("=" + fmt(years) if args.rate is not None else "=NA (no --rate)"))


if __name__ == "__main__":
    main()
