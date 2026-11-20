# Soft-mask hand-off into gene annotation

This repository builds and curates TE libraries. [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) consumes a **trusted** library and soft-masks the genome before it predicts gene models. That consumption step is their A0. Library building is not done in the gene-annotation repository.

The public product layers and red lines below restated what was already public in vitis-te (2026-11-15) and in the public teaching pages of gene-structure-annotation. They do **not** copy private laboratory notebooks.

## Four products (do not crush into one FASTA)

1. **Raw EDTA TElib** — a discovery output. Not `--curatedlib`. Not a gene soft-mask library.
2. **Working library** — after TEtrimmer (Perfect + Good) and a ~95% CD-HIT collapse. Still not `--curatedlib` as a whole file.
3. **Classifier labels** — TEsorter (for example `rexdb-plant`) adds domains and names. Do not replace the working FASTA with `all.cls.lib` (`all.cls.lib` in this repository is the name used when TEsorter is run on `all.fa`; the official README output is `<input>.rexdb.cls.lib`).
4. **Trusted library** — after a recorded CDS BLAST / host-gene purge and documented classification rules. ProtExcluder, as used in this repository, is a library-edit step that overlaps the CDS gate taught here. A mechanistic claim that it “removes protein-matching fragments and flanking 50 bp” is **[待确认]** until a ProtExcluder README or methods section is opened. DOI 10.1111/tpj.12340 was checked and is a plant-hemoglobin paper, not MAKER-P; it is not used. The opened MAKER-P abstract (Campbell et al., doi:10.1104/pp.113.230144) does not mention ProtExcluder. Treating NLR and F-box families as a default exclusion list is **this repository’s rule**, not a sentence copied from an opened grape paper. This trusted file, with its version and sha256, is the only library that may be used for gene soft-mask or as EDTA `--curatedlib`. Do not add Dfam as a second default library beside it unless a later methods decision says otherwise (that conflict is recorded in the 2026-11-15 methods notes).

`cat` plus CD-HIT of many libraries is not curation.

## Soft-mask, not hard-mask

The BRAKER README says: “In order to predict genes accurately in a novel genome, the genome should be masked for repeats. This will avoid the prediction of false positive gene structures in repetitive and low complexitiy regions.” It also says that for GeneMark and AUGUSTUS, “softmasking (i.e. putting repeat regions into lower case letters and all other regions into upper case letters) leads to better results than hardmasking (i.e. replacing letters in repetitive regions by the letter `N` for unknown nucleotide).” A further claim that hard-masking to `N` truncates or loses overlapping real genes is this repository’s inference **[待确认]**; it is not a BRAKER sentence. Soft-mask with RepeatMasker `-xsmall` (RepeatMasker help: “When the option -xsmall is used … repeat regions are in lower case”) and a trusted library only. `EDTA.pl` calls `make_masked.pl` with `-hardmask 1` (EDTA.pl source lines that invoke make_masked.pl, not a user-facing default documented in the EDTA README). This repository does not teach EDTA `make_masked.pl` as the A0 soft-mask step.

Practical checks that stay with the annotation repo: uppercase the genome before RepeatMasker (a defensive convention in this repository, because `-xsmall` uses lowercase for the mask; RepeatMasker help does not itself require a prior uppercase step); use `name#Class/Family` in the library; EDTA genome names no longer than 13 characters (letters, numbers, underscore) with a lookup table (EDTA README); This repository currently treats RepeatMasker `.out` as 1-based closed intervals and BED as 0-based half-open; the RepeatMasker help page does not state that coordinate convention, so it remains **[待确认]**.

## What moves where in the sources opened for these chapters

Deep teaching of types, tools and library building lives here. gene-structure-annotation should keep only a short A0 consumption hook and gene-model QC that measures overlap with TEs (`qa08_te_overlap.py`). See the `REMOVALS.md` list shipped with this teaching package for the proposed gene-structure-annotation PR. That list is not applied until a PR is merged.

R1 trusted ~240 is an archive/teaching example, not a universal target. A grape EDTA `--u` remains [待确认].
