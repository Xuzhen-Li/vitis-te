# Knowledge map

[中文](KNOWLEDGE_MAP.zh.md)

This page indexes every part of this repository, by topic and by kind of page. TE-Lib is a general library of knowledge, software and workflows for transposable elements: the book (in Chinese) explains TE biology, the type and detection pages show how each kind of element is recognised, the software catalogue compares tools by analysis step, and the workflow page and scripts give one way to run the analysis. Grapevine (*Vitis*) is kept as the running example. The two gene annotation repositories use the same layout.

This repository was formerly named vitis-te. Older pages still use that name; GitHub redirects the old links.

- [Topics](#topics)
- [Learn](#learn)
- [Software by analysis step](#software)
- [Example scripts and test data](#example-code)
- [Figures](#figures)
- [Sources and checks](#sources)
- [Other repository files](#other-files)

<a id="topics"></a>
## Topics

Each topic lists the book chapters, the knowledge pages and the matching sections of the software catalogue on the home page.

### Discovery and core concepts

- Book: [Chapter 1. Discovery and core concepts](../book/chapters/01-discovery-and-core-concepts.md)

### Classification and nomenclature

- Book: [Chapter 2. Classification and nomenclature](../book/chapters/02-classification-and-nomenclature.md); [A type-by-type catalogue of transposable elements](../book/chapters/types-catalogue.md)
- Pages: [TE types: a teaching map](../docs/types/README.md)
- Software: [Classification](../README.md#classification)

### Class I retrotransposons

- Book: [Chapter 3. Class I retrotransposons: structure and life cycle](../book/chapters/03-class-I-retrotransposons.md)
- Pages: [LTR retrotransposons](../docs/types/class_I_ltr.md); [LINE and SINE](../docs/types/class_I_line_sine.md); [DIRS and Penelope-like elements (PLE)](../docs/types/class_I_dirs_ple.md); [TRIM and LARD](../docs/types/class_I_trim_lard.md); [Plant pararetroviruses and Florendovirus](../docs/types/pararetrovirus_florendovirus.md)
- Software: [LTR retrotransposon detection](../README.md#ltr-retrotransposon-detection)

### Class II DNA transposons

- Book: [Chapter 4. Class II DNA transposons: structure and life cycle](../book/chapters/04-class-II-dna-transposons.md)
- Pages: [TIR DNA transposons](../docs/types/class_II_tir.md); [MITEs](../docs/types/class_II_mite.md); [Helitrons](../docs/types/class_II_helitron.md); [Maverick / Polinton](../docs/types/class_II_maverick.md); [Crypton](../docs/types/class_II_crypton.md)
- Software: [TIR, MITE, Helitron and SINE detection](../README.md#tir-mite-helitron-and-sine-detection)

### Non-TE repeats

- Pages: [Non-TE repeats that contaminate TE libraries](../docs/types/non_te_repeats.md)
- Software: [Polyploid subgenomes and tandem repeats](../README.md#polyploid-subgenomes-and-tandem-repeats)

### TEs as they appear in genomes

- Book: [Chapter 13. TEs as they appear in genomes: complete, fragmentary, chimeric, and domesticated](../book/chapters/13-observed-forms.md)

### Host silencing and epigenetics

- Book: [Chapter 5. Host silencing and epigenetic regulation](../book/chapters/05-host-silencing-and-epigenetics.md)
- Pages: [TEs and the host](../docs/host/README.md)
- Software: [TE expression and small RNA](../README.md#te-expression-and-small-rna)

### Genome evolution and TE dynamics

- Book: [Chapter 6. Genome evolution and TE dynamics](../book/chapters/06-genome-evolution-and-te-dynamics.md)
- Software: [Insertion age, landscape and horizontal transfer](../README.md#insertion-age-landscape-and-horizontal-transfer)

### Detection, annotation and libraries

- Book: [Chapter 7. Detection, de novo annotation, and library construction](../book/chapters/07-detection-annotation-and-libraries.md)
- Pages: [Sequence signatures used to recognise each type](../docs/detection/signatures.md); [Tools, mainstream pipelines, and field difficulties](../docs/detection/tools_and_pipelines.md); [Soft-mask hand-off into gene annotation](../docs/detection/softmask_handoff.md)
- Software: [Complete pipelines and the steps they cover](../README.md#complete-pipelines-and-the-steps-they-cover); [Complete pipelines: paper, lab and authority](../README.md#complete-pipelines-paper-lab-and-authority); [Family finders and read-based repeat discovery](../README.md#family-finders-and-read-based-repeat-discovery); [Curation, redundancy reduction and library QC](../README.md#curation-redundancy-reduction-and-library-qc); [Masking, annotation and cleaning of annotations](../README.md#masking-annotation-and-cleaning-of-annotations); [Databases and libraries: general](../README.md#databases-and-libraries-general); [Databases and libraries: plants](../README.md#databases-and-libraries-plants); [Simulation and benchmarking](../README.md#simulation-and-benchmarking)

### Insertion polymorphisms (TIPs)

- Book: [Chapter 8. Population-level transposable-element insertion polymorphisms (TIPs)](../book/chapters/08-insertion-polymorphisms-tips.md)
- Software: [Insertion polymorphism: short reads](../README.md#insertion-polymorphism-short-reads); [Insertion polymorphism: long reads and call annotation](../README.md#insertion-polymorphism-long-reads-and-call-annotation); [Insertion polymorphism: assemblies, pangenomes and graphs](../README.md#insertion-polymorphism-assemblies-pangenomes-and-graphs); [Insertion polymorphism: plant resources and other inputs](../README.md#insertion-polymorphism-plant-resources-and-other-inputs)

### Phenotype and domestication

- Book: [Chapter 9. TEs, phenotypic variation, and crop domestication](../book/chapters/09-phenotype-and-domestication.md)

### Grapevine as the worked example

- Book: [Chapter 10. TEs in grapevine genomes: *Vitis* as a worked example](../book/chapters/10-vitis-as-worked-example.md)
- Pages: [TEs in grapevine genomes](../docs/vitis/README.md)
- Software: [Databases and libraries: grapevine (Vitis)](../README.md#databases-and-libraries-grapevine-vitis)

### Practical workflow

- Book: [Chapter 11. A practical workflow: analysing a grapevine genome from start to finish](../book/chapters/11-practical-workflow.md)
- Pages: [TE-Lib workflow](../docs/WORKFLOW.md)
- Home page: [Practical workflow](../README.md#practical-workflow)

### Visualization

- Software: [Visualization](../README.md#visualization)

### Open questions

- Book: [Chapter 12. Open questions and future directions](../book/chapters/12-open-questions.md)
- Software: [Community indexes and cross-links](../README.md#community-indexes-and-cross-links)

### Appendices

- Book: [Appendix A. Glossary of terms and abbreviations](../book/chapters/appendix-a-glossary.md); [Appendix B. Public databases and widely used tools](../book/chapters/appendix-b-databases-and-tools.md); [Appendix C. Further reading](../book/chapters/appendix-c-further-reading.md)

<a id="learn"></a>
## Learn

- Book: [《转座子从发现到实践，以葡萄为例》](../book/README.md); [转座子从发现到实践，以葡萄为例](../book/TE_BOOK_full.md); [全书文件索引](../book/INDEX.md); [Preface](../book/chapters/00-preface.md)
- Illustrated edition: [配图预览说明（非正式书稿，第2版 p2d）](../book/illustrated_v3_p2d/TE_BOOK_illustrated_v3_p2d.md); [配图合订本](../book/illustrated_v3_p2d/README.md)

<a id="software"></a>
## Software by analysis step

- [Software by analysis step](../README.md#software-by-analysis-step)
- [Guide to TE analysis software, by analysis step](../docs/software/README.md)
- [`SOFTWARE_AUTHORITY.tsv`](../catalog/SOFTWARE_AUTHORITY.tsv); [`CATALOG.tsv`](../catalog/CATALOG.tsv)

<a id="example-code"></a>
## Example scripts and test data

The example scripts are small and tested on a toy genome with one planted LTR-like insertion. They are not a maintained software package.

- [scripts](../scripts/README.md)
  - [`00_make_tiny_genome.py`](../scripts/00_make_tiny_genome.py)
  - [`01_ltr_insertion_age.py`](../scripts/01_ltr_insertion_age.py)
  - [`02_softmask.py`](../scripts/02_softmask.py)
  - [`03_run_edta.sh`](../scripts/03_run_edta.sh)
  - [`04_run_repeatmodeler_repeatmasker.sh`](../scripts/04_run_repeatmodeler_repeatmasker.sh)
  - [`05_run_tesorter.sh`](../scripts/05_run_tesorter.sh)
  - [`draw_te_schematics.v4.py`](../scripts/figures/draw_te_schematics.v4.py)
  - [`run_toy_pipeline.sh`](../scripts/run_toy_pipeline.sh)
- [testdata](../testdata/README.md); [testdata/EXAMPLES.md](../testdata/EXAMPLES.md)

<a id="figures"></a>
## Figures

- [Figures](../figures/README.md); [Figures for the guide](../figures/guide/README.md)
- Figures of the illustrated edition: `book/illustrated_v3_p2d/figures/`
- 213 files, including the drawing scripts in `figures/guide/src/`

<a id="sources"></a>
## Sources and checks

- [`DOI_CHECKS.tsv`](../DOI_CHECKS.tsv)
- [DOI_CHECKS year convention](../DOI_CHECKS.NOTES.md)
- [`SOURCES_READ.tsv`](../SOURCES_READ.tsv)
- [Changelog](../CHANGELOG.md)
- [`SHA256SUMS.v2`](../SHA256SUMS.v2)
- [`SHA256SUMS.txt`](../book/illustrated_v3_p2d/SHA256SUMS.txt)

<a id="other-files"></a>
## Other repository files

- `README.md`
- `README.zh.md`
- `LICENSE`
- `NOTICE.md`
