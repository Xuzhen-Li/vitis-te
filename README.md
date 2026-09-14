# vitis-te

Public stub for *Vitis* TE libraries and the soft-mask hand-off into gene annotation.

**Operational notebook:** private lab TE tree (not in git).  
Pipeline idea: EDTA → TEtrimmer → TEsorter → CDS-gated **trusted** → soft-mask / panEDTA.  
**R1 numbers (e.g. trusted ~240) are archive/teaching examples**; panel gold may move to a newer trusted emit.  

**Structure playbook plug-in:**  
[gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md).

## This is not

- Not gene-model annotation — [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)
- Not functional annotation — [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation)
- Not PAV graphs — [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome)
- Not a dump of another group’s raw TE calls

## Lab order (summary)

1. **EDTA** per assembly/haplotype (`--species others --sensitive 1 --anno 1`; document `--u`)
2. **TEtrimmer** per hap → merge Perfect/Good → CD-HIT ~95% **working** lib  
   (optional 80-80 **family** catalog; do not overwrite working)
3. **TEsorter** (e.g. rexdb-plant) — domains/labels only; **never** replace working FASTA with `all.cls.lib`
4. **Curation gate** (CDS BLAST + TEsorter class emit rules) → **trusted** FASTA (record sha256)
5. Soft-mask / EDTA `--curatedlib` with **trusted only**
6. **panEDTA** combine (official; not `cat` of TElibs) → panel reannotate
7. LTR age / LAI / PAV after curated pan TE GFFs

### Critical distinctions

| Product | Use as `--curatedlib` / gene soft-mask? |
|---------|----------------------------------------|
| Raw EDTA TElib | No |
| Working lib (post-TEtrimmer CD-HIT) | No (whole file) |
| Trusted gated lib | **Yes** |
| `cat` + CD-HIT of many libs | No (dedup ≠ curation) |

### EDTA starter

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --threads 32
```

## Red lines

- Do not treat EDTA raw output as a gold-standard TE library.
- Do not treat `cat`+CD-HIT as curatedlib.
- Classifier-only tools name consensi; they do not replace trim or become the library.
- Do not hard-mask for BRAKER/GALBA; soft-mask with a **trusted**, host-gene-purged lib.
- Non-TE repeats (TRF / telomere / rDNA) are not curatedlib material.

## See also

- [gene-structure-annotation TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)
- [bioinfo-agent-skills](https://github.com/Xuzhen-Li/bioinfo-agent-skills)

**Author:** Xuzhen Li · [ORCID](https://orcid.org/0000-0003-3670-6657)
