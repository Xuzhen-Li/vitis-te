#!/usr/bin/env bash
# Document the public EDTA command already used in the vitis-te stub README.
# --species others --sensitive 1 --anno 1, and set --u explicitly.
# If --u is omitted, EDTA defaults to the rice rate 1.3e-8 substitutions per
# bp per year and writes LTR ages under that default. That rice default must
# not be used silently for grape. A grape value for --u is [待确认] and must
# be given with its source when used. Ages from raw EDTA are not a delivery.
# Genome sequence names should be at most 13 characters (letters, digits,
# underscores); keep a name map. Do not treat raw EDTA output as a trusted
# library. Untested on this box (EDTA is not installed).

set -Ceu
if [ "${1:-}" = "--help" ] || [ "${1:-}" = "--dry-run" ]; then
  printf '%s\n' "documented command (set --u yourself; there is no grape default here):"
  printf '%s\n' "EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --u RATE --threads N"
  printf '%s\n' "If --u is omitted, EDTA uses rice 1.3e-8 /bp/year. Do not use that default for grape."
  printf '%s\n' "A grape --u value is [待确认]. Record the source of whatever rate you set."
  printf '%s\n' "Do not pass raw TElib to --curatedlib or gene soft-mask."
  printf '%s\n' "Citation (verified): Ou et al. 2019 Genome Biology 10.1186/s13059-019-1905-y"
  if [ "${1:-}" = "--dry-run" ]; then exit 2; fi
  exit 0
fi
printf '%s\n' "EDTA.pl is not invoked automatically in this wrapper; see --help."
exit 3
