#!/usr/bin/env bash
# Document TEsorter with rexdb-plant. Labels only; never replace the working FASTA
# with all.cls.lib (existing vitis-te / TE_LIBRARY.md rule).
# TEsorter/REXdb is used here for plant LTR lineages. It can also emit domain
# labels for some TIR superfamilies and Helitrons; the finer lineage names
# (Ale, Tekay, and so on) apply to LTR elements. The exact class coverage
# for TIR and Helitron is [待确认]. Untested on this box.

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "documented command: TEsorter working_lib.fa -db rexdb-plant"
  printf '%s\n' "Use domain table and class labels only. Do not replace working FASTA with all.cls.lib."
  printf '%s\n' "Do not rewrite library sequence names into RepeatMasker name#Class/Family from these labels alone."
  printf '%s\n' "Citation (verified): Zhang et al. 2022 Hortic Res 10.1093/hr/uhac017"
  printf '%s\n' "REXdb: Neumann et al. 2019 Mobile DNA 10.1186/s13100-018-0144-1"
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
exit 3
