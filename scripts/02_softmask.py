#!/usr/bin/env python3
"""Soft-mask intervals from a BED file by writing those bases in lowercase.

Inputs:  --fa --bed --out-fa  optional --uppercase-first
Tested:  planted tiny genome; every FASTA record is processed, matched by
the first token of the header (chromosome name).
Production: RepeatMasker -xsmall with a trusted, gene-purged library only
(see the vitis-te README and gene-structure-annotation docs/TE_LIBRARY.md).
Do not hard-mask for BRAKER or GALBA. Do not use raw EDTA output as the library.
This script only lowercases BED intervals; it does not run RepeatMasker.

Hand-off notes:
- EDTA expects genome sequence names of at most 13 characters, using letters,
  digits and underscores. Keep a name map and map back before gene annotation.
- Before RepeatMasker -xsmall, convert the genome to uppercase so that
  lowercase afterwards means only the trusted-library mask. How RepeatMasker
  treats pre-existing lowercase is [待确认]. Use --uppercase-first here to
  do that conversion.
- RepeatMasker libraries use the name#Class/Family header form. Do not
  replace library sequence names with TEsorter labels.
- RepeatMasker .out coordinates are 1-based closed intervals; BED is 0-based
  half-open. Convert before passing a .out file to this script.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def read_fa(path: Path):
    recs = []
    name, seq = None, []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.startswith(">"):
                if name is not None:
                    recs.append((name, "".join(seq)))
                name = line[1:].strip()
                seq = []
            else:
                seq.append(line.strip())
    if name is not None:
        recs.append((name, "".join(seq)))
    return recs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fa", required=True)
    ap.add_argument("--bed", required=True)
    ap.add_argument("--out-fa", required=True)
    ap.add_argument("--uppercase-first", action="store_true",
                    help="convert every base to uppercase before applying the BED mask")
    args = ap.parse_args()
    recs = read_fa(Path(args.fa))
    seqs = {}
    order = []
    for name, seq in recs:
        chrom = name.split()[0]
        order.append((chrom, name))
        text = seq.upper() if args.uppercase_first else seq
        seqs[chrom] = list(text)
    n = 0
    skipped = 0
    with Path(args.bed).open(encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            chrom, start, end, *_ = line.rstrip("\n").split("\t")
            start, end = int(start), int(end)
            if chrom not in seqs:
                skipped += 1
                continue
            s = seqs[chrom]
            for i in range(start, min(end, len(s))):
                s[i] = s[i].lower()
                n += 1
    with Path(args.out_fa).open("x", encoding="utf-8") as f:
        for chrom, name in order:
            f.write(">" + name + "\n")
            text = "".join(seqs[chrom])
            for i in range(0, len(text), 80):
                f.write(text[i:i + 80] + "\n")
    print("lowercased_bases", n, "bed_chroms_not_in_fasta", skipped, "records", len(recs))


if __name__ == "__main__":
    main()
