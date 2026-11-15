# scripts

Toy demonstrations and command wrappers for this repository. None of the inputs are real *Vitis* data. Citations for production tools are in `catalog/CATALOG.tsv`. Paper years in that catalogue are print years.

Run the tested Python chain:

```bash
bash scripts/run_toy_pipeline.sh OUTDIR
```

| File | Purpose | Tested? |
|------|---------|---------|
| `00_make_tiny_genome.py` | Plant one LTR-like insertion in a tiny FASTA | Yes, 2026-11-15 CST |
| `01_ltr_insertion_age.py` | p-distance and K2P; years only if `--rate` is given (no default rate); T = K/(2r) | Yes (without `--rate`) |
| `02_softmask.py` | Lowercase BED intervals on every FASTA record; optional `--uppercase-first` | Yes |
| `03_run_edta.sh` | Document EDTA.pl; `--u` must be set explicitly (rice 1.3e-8 is not a grape default) | No, `--dry-run` exits 2 |
| `04_run_repeatmodeler_repeatmasker.sh` | Document RepeatModeler2 + RepeatMasker `-xsmall` | No, `--dry-run` exits 2 |
| `05_run_tesorter.sh` | Document TEsorter; do not replace working FASTA with all.cls.lib | No, `--dry-run` exits 2 |
| `run_toy_pipeline.sh` | Driver for the three Python scripts | Yes |

On the tested run (seed 5), the two planted LTRs differed at 10 of 200 sites (p = 0.05). The age script does not apply a default substitution rate.
