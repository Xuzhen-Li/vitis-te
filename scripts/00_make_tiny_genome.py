#!/usr/bin/env python3
"""Write a tiny DNA FASTA with one planted LTR retrotransposon-like insertion.

Inputs:  --out-fa --out-bed --seed
Outputs: FASTA and a BED of the 5-prime LTR, internal region, and 3-prime LTR.
The 3-prime LTR is a diverged copy of the 5-prime LTR (known substitutions).
Tested:  Python 3.13 + numpy. This is not a real Vitis TE.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out-fa", required=True)
    ap.add_argument("--out-bed", required=True)
    ap.add_argument("--seed", type=int, default=5)
    args = ap.parse_args()
    rng = np.random.default_rng(args.seed)
    bases = np.array(list("ACGT"))
    flank_l = "".join(rng.choice(bases, size=500))
    ltr5 = "".join(rng.choice(bases, size=200))
    internal = "".join(rng.choice(bases, size=400))
    ltr3 = list(ltr5)
    # introduce 10 substitutions in the 3-prime LTR (5% of 200 bp)
    idx = rng.choice(200, size=10, replace=False)
    for i in idx:
        alt = [b for b in "ACGT" if b != ltr3[i]]
        ltr3[i] = str(rng.choice(np.array(alt)))
    ltr3 = "".join(ltr3)
    flank_r = "".join(rng.choice(bases, size=500))
    seq = flank_l + ltr5 + internal + ltr3 + flank_r
    start5 = len(flank_l)
    start_i = start5 + len(ltr5)
    start3 = start_i + len(internal)
    with Path(args.out_fa).open("x", encoding="utf-8") as f:
        f.write(">chrToy TE-demo planted LTR-like insertion; not Vitis data\n")
        for i in range(0, len(seq), 80):
            f.write(seq[i:i + 80] + "\n")
    with Path(args.out_bed).open("x", encoding="utf-8") as f:
        f.write("#chrom\tstart\tend\tname\n")
        f.write(f"chrToy\t{start5}\t{start_i}\tLTR5\n")
        f.write(f"chrToy\t{start_i}\t{start3}\tINTERNAL\n")
        f.write(f"chrToy\t{start3}\t{start3 + len(ltr3)}\tLTR3\n")
    print("length", len(seq), "LTR5", start5, start_i, "LTR3", start3, start3 + 200)


if __name__ == "__main__":
    main()
