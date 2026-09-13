# vitis-te

EDTA-based transposable-element annotation and **curated** TE libraries for *Vitis* (and the same order for other plants).

Gene-structure soft-mask consumes this scheme here:  
[`gene-structure-annotation` `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md).

## This is not

- Not gene-model annotation — [`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation) (BRAKER / GALBA / …)
- Not functional annotation — [`gene-function-annotation`](https://github.com/Xuzhen-Li/gene-function-annotation)
- Not PAV graphs — [`vitis-pangenome`](https://github.com/Xuzhen-Li/vitis-pangenome)
- Not synteny — [`vitis-synteny`](https://github.com/Xuzhen-Li/vitis-synteny)
- Not a dump of another group’s raw TE calls

## Lab order (do not skip curation)

1. **EDTA** per assembly (`--species others` unless rice/maize; prefer `--cds` when available)
2. **TEtrimmer** for boundaries
3. **TEsorter** for lineage (**naming**, not a genome-wide scanner)
4. Manual spot-check (LTR false positives, LINE/SINE misses, CDS contamination)
5. Curated lib: drop CDS → CD-HIT ~85% → 80-80 collapse
6. Re-annotate with `--curatedlib` and/or **RepeatMasker** (soft-mask `-xsmall` for gene prediction)
7. LTR age + **LAI** only after the lib is curated

### EDTA starter

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --threads 32
```

## Red lines

- Do not treat EDTA raw output as a gold-standard TE library.
- Classifier-only tools are for naming, not for scanning a genome or replacing trim.
- Do not publish another group's raw TE calls as yours.
- Do not hard-mask genomes for BRAKER/GALBA; soft-mask with a **host-gene-purged** lib (ProtExcluder).

## Soft-mask hand-off

After curated + purged lib → RepeatMasker `-xsmall` → `GENOME_SOFT` for  
[`gene-structure-annotation`](https://github.com/Xuzhen-Li/gene-structure-annotation) A0.  
Full plug-in notes: [TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md).

## See also

- [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)
- [bioinfo-agent-skills](https://github.com/Xuzhen-Li/bioinfo-agent-skills)

**Author:** Xuzhen Li · [ORCID](https://orcid.org/0000-0003-3670-6657)
