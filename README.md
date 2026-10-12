# vitis-te
[中文](README.zh.md)

## Overview

This repository provides a public stub for *Vitis* transposable element (TE) libraries and the soft-mask hand-off into gene annotation. The operational notebook is maintained in a private lab TE tree and is not tracked in git.

The pipeline progression is `EDTA` to `TEtrimmer` to `TEsorter` to CDS-gated trusted output, and finally to soft-masking or `panEDTA`. The `R1` numbers such as trusted `~240` are archive and teaching examples. The panel gold standard may shift to a newer trusted output.

The gene soft-mask step designated as `A0` only accepts the current trusted file with its version and `sha256` hash, not raw `EDTA` output or the entire working library. The structure playbook plug-in is documented in [gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md).

## Out of Scope

- This project is not for gene-model annotation, which is handled by [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation).
- It is not for functional annotation, which belongs to [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation).
- It is not for PAV graphs, which are covered by [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome).
- It is not a dump of raw TE calls from other research groups.

## Pipeline

1. Run `EDTA` per assembly or haplotype using `--species others --sensitive 1 --anno 1` and document the `--u` parameter.
2. Run `TEtrimmer` per haplotype, merge the Perfect and Good outputs, and use `CD-HIT` to generate a `~95%` working library. An optional `80-80` family catalog can be made, but do not overwrite the working library.
3. Run `TEsorter` with resources like `rexdb-plant` to assign domains and labels only. Never replace the working FASTA with the `all.cls.lib` file.
4. Use a curation gate with CDS BLAST and `TEsorter` class emit rules to generate a trusted FASTA and record its `sha256`.
5. Use soft-mask or `EDTA` `--curatedlib` with the trusted file only.
6. Run `panEDTA` to combine results officially, rather than just using `cat` on TE libraries, to reannotate the panel.
7. Calculate LTR age, LAI, and PAV after generating curated pan TE GFFs.

## Distinctions

| Product | Use as `--curatedlib` / gene soft-mask? |
|---------|----------------------------------------|
| Raw EDTA TElib | No |
| Working lib (post-TEtrimmer CD-HIT) | No (whole file) |
| Trusted gated lib | Yes |
| `cat` + CD-HIT of many libs | No (dedup ≠ curation) |

## Usage

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --threads 32
```

## Guidelines

- Do not treat `EDTA` raw output as a gold-standard TE library.
- Do not treat `cat` and `CD-HIT` output as `--curatedlib`.
- Classifier-only tools name consensi but do not replace trimming tools or become the library itself.
- Do not hard-mask for `BRAKER` or `GALBA`. You must soft-mask using a trusted library that has been purged of host genes.
- Non-TE repeats like `TRF`, telomeres, and rDNA are not appropriate for `--curatedlib`.

## References

- [gene-structure-annotation `TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)

Author: Xuzhen Li, [ORCID](https://orcid.org/0000-0003-3670-6657)
