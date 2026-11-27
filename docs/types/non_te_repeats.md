# Non-TE repeats that contaminate TE libraries

A de novo TE library is a collection of sequences that look repetitive. Not all of them are transposable elements. If they stay in a library used as `--curatedlib` or for gene soft-mask, real genes can be masked. That LAI and TE-content figures can then be inflated is this repository’s caution **[待确认]**, not a sentence copied from the opened Ou 2018 catalogue entry.

## What to keep off the trusted TE library

- **Tandem repeats and satellites**, including those found by Tandem Repeats Finder (Benson 1999, [doi:10.1093/nar/27.2.573](https://doi.org/10.1093/nar/27.2.573)). Put them on a **separate non-TE track**.
- **Telomeric and centromeric satellite repeats** are tandem, non-TE sequences and belong on that non-TE track. **Centromeric retrotransposons (CRTs)** are TEs; they belong on the TE track, not in this non-TE list. This chapter separates the two. A named *Vitis* CRT family is **[待确认]** until a cited annotation is opened.
- **rDNA arrays** (45S, 5S) are tandem gene arrays, not TEs. vitis-open-directions has a project on rDNA arrays; do not absorb that work as a TE family.
- **Low-complexity sequence and simple sequence repeats (SSRs).**
- **Host gene families** that occur in clusters and look “repetitive” to RepeatModeler, especially NLR (disease-resistance) genes and F-box genes. ProtExcluder is a library-edit tool kept on the gene-annotation side of this hand-off; a mechanistic description of how it purges protein-coding host genes is **[待确认]** until a ProtExcluder README or methods section is opened. DOI 10.1111/tpj.12340 was checked and is not MAKER-P; the opened MAKER-P abstract ([doi:10.1104/pp.113.230144](https://doi.org/10.1104/pp.113.230144)) does not mention ProtExcluder. Treating NLR and F-box families as a default exclusion list in the trusted-library gate is **this repository’s rule** (see [../detection/softmask_handoff.md](../detection/softmask_handoff.md)), not a sentence copied from an opened grape paper.
- **Organelle insertions** (NUMTs, NUPTs) if they were assembled into the nuclear sequence and then built into a “TE” model. Flag them; do not treat them as a new TE superfamily. This, too, is **this repository’s rule** until a *Vitis*-specific study is cited. Whether a given NUMT filter is sufficient on a given *Vitis* dataset is **[待确认]**.

## How to recognise them

TRF and tandem-repeat tools; rDNA HMMs or BLAST to known rRNA; CDS BLAST of the library against a trusted protein set; manual inspection of models that are only tandem monomers. LAI (Ou et al. 2018, [doi:10.1093/nar/gky730](https://doi.org/10.1093/nar/gky730)) is an assembly-quality index based on intact LTR content, not a licence to leave non-TE repeats in `--curatedlib`.

The core rule stands: non-TE repeats such as TRF, telomeres and rDNA do not belong in `--curatedlib`.

## Claim–source table

| Claim | Source | Quoted sentence or figure/table | What was read |
|---|---|---|---|
| TRF finds tandem repeats | doi:10.1093/nar/27.2.573 | Title/abstract (catalogue) | Catalogue entry |
| LAI is an intact-LTR assembly index | doi:10.1093/nar/gky730 | Title (catalogue) | Catalogue entry |
| ProtExcluder mechanism (protein hits and 50 bp flanks) | — | — | **[待确认]**; DOI 10.1111/tpj.12340 is not used |
| NLR/F-box as a default trusted-library exclusion; NUMT/NUPT flagging | this repository’s rule | softmask_handoff.md | Repository rule, not a grape paper |
| A named *Vitis* CRT family; sufficiency of a NUMT filter on a given dataset | — | — | **[待确认]** |
