#!/usr/bin/env bash
# Tested Python TE toy chain (genome, LTR age, soft-mask). Does not call EDTA.
# LTR age is run without --rate, so years stay NA.
set -Ceu
if [ "${1:-}" = "--help" ] || [ $# -lt 1 ]; then
  printf '%s\n' "usage: run_toy_pipeline.sh OUTDIR"
  exit 0
fi
OUT=$1
HERE=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$OUT"
python3 "$HERE/00_make_tiny_genome.py" --out-fa "$OUT/tiny.fa" --out-bed "$OUT/tiny.bed" --seed 5
python3 "$HERE/01_ltr_insertion_age.py" --fa "$OUT/tiny.fa" --bed "$OUT/tiny.bed" --out-tsv "$OUT/ltr_age.tsv"
python3 "$HERE/02_softmask.py" --uppercase-first --fa "$OUT/tiny.fa" --bed "$OUT/tiny.bed" --out-fa "$OUT/tiny.softmasked.fa"
printf '%s\n' "toy TE pipeline finished in $OUT"
