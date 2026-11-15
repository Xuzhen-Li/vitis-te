#!/usr/bin/env bash
# Document RepeatModeler2 + RepeatMasker as an alternative de novo + homology route.
# Untested on this box.

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "documented commands (install the tools first):"
  printf '%s\n' "BuildDatabase -name NAME assembly.fa"
  printf '%s\n' "RepeatModeler -database NAME -LTRStruct -threads N"
  printf '%s\n' "  -LTRStruct is the RepeatModeler2 LTR structural module; the exact option"
  printf '%s\n' "  name and thread flag can vary by version [待确认]."
  printf '%s\n' "Before RepeatMasker -xsmall, convert the genome to uppercase."
  printf '%s\n' "RepeatMasker -xsmall -lib trusted.fa assembly.fa"
  printf '%s\n' "Library headers should use the name#Class/Family form."
  printf '%s\n' "RepeatMasker .out is 1-based closed; BED is 0-based half-open."
  printf '%s\n' "Citations (verified): RepeatModeler2 Flynn et al. 2020 PNAS 10.1073/pnas.1921046117"
  printf '%s\n' "RepeatMasker: Smit, AFA, Hubley, R & Green, P. RepeatMasker Open-4.0. 2013-2015"
  printf '%s\n' "  http://www.repeatmasker.org"
  printf '%s\n' "Soft-mask only for BRAKER/GALBA; use a trusted gene-purged library, not raw consensi."
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
exit 3
