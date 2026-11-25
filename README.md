# vitis-te

English | [中文](README.zh.md)

This repository holds a Chinese book, a methods catalogue, and small scripts on transposable elements (TEs) in grapevine (*Vitis*) and other plants. The book is the place to learn what TEs are, how they are classified, and what is known in grapevine. The workflow, software catalogue, and scripts are the place to see how an analysis is done. This repository also points to a *Vitis* TE library used for gene soft-masking, documented in [gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md).

Gene-model annotation is handled by [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation). Functional annotation belongs to [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation). PAV graphs and the long graph-tool list are covered by [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome). This repository is not a dump of raw TE calls from other research groups. Private laboratory drafts and teaching notes that are not already public on GitHub are not copied here.

## Book contents

The book, 《转座子从发现到实践，以葡萄为例》 (Transposable elements from discovery to practice, with grapevine as the example), is in Chinese. Start from [`book/README.md`](book/README.md). The same text is in [`book/TE_BOOK_full.md`](book/TE_BOOK_full.md). The file list is in [`book/INDEX.md`](book/INDEX.md). Statements or citations that have not been checked against an opened source are marked [待确认].

An illustrated combined edition (chapters 1-4, the type catalogue, chapter 13, chapters 5-12, and the book appendices) is in [`book/illustrated_v3_p2d/TE_BOOK_illustrated_v3_p2d.md`](book/illustrated_v3_p2d/TE_BOOK_illustrated_v3_p2d.md).

- [Preface](book/chapters/00-preface.md)
  - [Aim of the book](book/chapters/00-preface.md#编写定位)
  - [How the book is organised](book/chapters/00-preface.md#全书结构与阅读路径)
  - [Terms, code conventions, and reproducibility](book/chapters/00-preface.md#术语规范代码约定与可重复计算原则)
- [Chapter 1. Discovery and core concepts](book/chapters/01-discovery-and-core-concepts.md)
  - [1.1 Discovery of maize controlling elements, and early disputes](book/chapters/01-discovery-and-core-concepts.md#11-玉米控制元件的发现与早期争议)
  - [1.2 From junk DNA to a dynamic component of the genome](book/chapters/01-discovery-and-core-concepts.md#12-从垃圾dna到基因组动态组分认知范式的演变)
  - [1.3 Basic definition, structure, and the host-genome setting](book/chapters/01-discovery-and-core-concepts.md#13-转座子的基本定义结构特征与宿主基因组背景)
- [Chapter 2. Classification and nomenclature](book/chapters/02-classification-and-nomenclature.md)
  - [2.1 From Finnegan to Wicker and Repbase](book/chapters/02-classification-and-nomenclature.md#21-分类学的演进从finnegan到wicker与repbase体系)
  - [2.2 Hierarchy and boundary disputes in the unified framework](book/chapters/02-classification-and-nomenclature.md#22-统一分类框架中的层级与边界争议)
  - [2.3 Naming rules and public-database standards](book/chapters/02-classification-and-nomenclature.md#23-命名规则与公共数据库标准)
- [Chapter 3. Class I retrotransposons: structure and life cycle](book/chapters/03-class-I-retrotransposons.md)
  - [3.1 Structure and reverse transcription of LTR retrotransposons](book/chapters/03-class-I-retrotransposons.md#31-ltr反转录转座子的结构与反转录机制)
  - [3.2 Non-LTR retrotransposons: LINEs and SINEs](book/chapters/03-class-I-retrotransposons.md#32-非ltr反转录转座子line与sine)
  - [3.3 DIRS, PLE, and other unusual retroelements](book/chapters/03-class-I-retrotransposons.md#33-dirsple及其他特殊反转录元件)
- [Chapter 4. Class II DNA transposons: structure and life cycle](book/chapters/04-class-II-dna-transposons.md)
  - [4.1 Classical cut-and-paste TIR DNA transposons](book/chapters/04-class-II-dna-transposons.md#41-经典剪切-粘贴型tir-dna转座子)
  - [4.2 Origin and amplification of MITEs](book/chapters/04-class-II-dna-transposons.md#42-mites微型反向重复转座元件的起源与扩增)
  - [4.3 Helitrons and Maverick/Polinton: rolling-circle and self-synthesizing elements](book/chapters/04-class-II-dna-transposons.md#43-helitron与maverickpolinton滚环复制与自合成元件)
- [Chapter 5. Host silencing and epigenetic regulation](book/chapters/05-host-silencing-and-epigenetics.md)
  - [5.1 Plant DNA methylation and the RdDM pathway](book/chapters/05-host-silencing-and-epigenetics.md#51-植物dna甲基化与rddmrna导向的dna甲基化通路)
  - [5.2 Histone modification, chromatin remodeling, and heterochromatin](book/chapters/05-host-silencing-and-epigenetics.md#52-组蛋白修饰染色质重塑与异染色质维持)
  - [5.3 TE escape, stress activation, and epigenetic reprogramming](book/chapters/05-host-silencing-and-epigenetics.md#53-转座子的逃逸胁迫激活与表观遗传重编程)
- [Chapter 6. Genome evolution and TE dynamics](book/chapters/06-genome-evolution-and-te-dynamics.md)
  - [6.1 TE bursts, removal, and genome-size evolution](book/chapters/06-genome-evolution-and-te-dynamics.md#61-转座子爆发清除与基因组大小演化)
  - [6.2 Compartmentalized distribution and nested insertions](book/chapters/06-genome-evolution-and-te-dynamics.md#62-基因组区室化分布与嵌套插入)
  - [6.3 Structural variation, gene capture, and exaptation](book/chapters/06-genome-evolution-and-te-dynamics.md#63-结构变异基因捕获与功能外适应exaptation)
- [Chapter 7. Detection, de novo annotation, and library construction](book/chapters/07-detection-annotation-and-libraries.md)
  - [7.1 Homology-based and structure-based de novo detection](book/chapters/07-detection-annotation-and-libraries.md#71-基于同源与基于结构的从头预测原理)
  - [7.2 Combined annotation pipelines and high-quality consensus libraries](book/chapters/07-detection-annotation-and-libraries.md#72-整合注释流程与高质量一致性文库构建)
  - [7.3 Quality assessment and cross-genome or pangenome annotation](book/chapters/07-detection-annotation-and-libraries.md#73-注释质量评估与跨基因组泛基因组注释策略)
- [Chapter 8. Population-level transposable-element insertion polymorphisms (TIPs)](book/chapters/08-insertion-polymorphisms-tips.md)
  - [8.1 TIP detection from short and long reads](book/chapters/08-insertion-polymorphisms-tips.md#81-短读长与长读长测序数据的tips检测原理)
  - [8.2 Population-genetic statistics and neutrality tests for TIPs](book/chapters/08-insertion-polymorphisms-tips.md#82-群体遗传学统计量与中性检验在tips中的应用)
  - [8.3 TIPs in genome-wide association (TE-GWAS)](book/chapters/08-insertion-polymorphisms-tips.md#83-tips在全基因组关联分析te-gwas中的应用)
- [Chapter 9. TEs, phenotypic variation, and crop domestication](book/chapters/09-phenotype-and-domestication.md)
  - [9.1 How TEs affect gene expression](book/chapters/09-phenotype-and-domestication.md#91-转座子影响基因表达的分子机制)
  - [9.2 Classic phenotypic cases in model plants and major crops](book/chapters/09-phenotype-and-domestication.md#92-模式植物与主要作物中的经典表型案例)
  - [9.3 TEs and somatic variation in clonally propagated and perennial woody crops](book/chapters/09-phenotype-and-domestication.md#93-无性繁殖与多年生木本作物中的转座子与体细胞变异)
- [Chapter 10. TEs in grapevine genomes: *Vitis* as a worked example](book/chapters/10-vitis-as-worked-example.md)
  - [10.1 Grapevine genome features and TE composition](book/chapters/10-vitis-as-worked-example.md#101-葡萄基因组特征与转座子组成概览)
  - [10.2 A classic case: Gret1 and berry skin colour](book/chapters/10-vitis-as-worked-example.md#102-经典案例gret1与葡萄果皮颜色的演化)
  - [10.3 TEs in grapevine clonal variation, local adaptation, and trait improvement](book/chapters/10-vitis-as-worked-example.md#103-葡萄无性系变异风土适应与性状改良中的转座子)
- [Chapter 11. A practical workflow: analysing a grapevine genome from start to finish](book/chapters/11-practical-workflow.md)
  - [11.1 Data, software environment, and de novo annotation of a single genome](book/chapters/11-practical-workflow.md#111-数据准备软件环境与单基因组转座子从头注释实战)
  - [11.2 Library curation, insertion-time estimates, and genome-wide distribution](book/chapters/11-practical-workflow.md#112-转座子文库精修插入时间估算与基因组分布可视化)
  - [11.3 TIP calling from grapevine population resequencing, and screening of candidate sites](book/chapters/11-practical-workflow.md#113-葡萄群体重测序tips鉴定与候选功能位点筛选实战)
- [Chapter 12. Open questions and future directions](book/chapters/12-open-questions.md)
  - [12.1 New challenges in the T2T and pangenome era](book/chapters/12-open-questions.md#121-t2t基因组与泛基因组时代的转座子解析新挑战)
  - [12.2 Deep learning and long-read multi-omics](book/chapters/12-open-questions.md#122-深度学习与长读长多组学在转座子研究中的应用)
  - [12.3 TE engineering and crop breeding](book/chapters/12-open-questions.md#123-转座子工程化应用与未来作物育种前景)
- [Chapter 13. TEs as they appear in genomes: complete, fragmentary, chimeric, and domesticated](book/chapters/13-observed-forms.md)
- [A type-by-type catalogue of transposable elements](book/chapters/types-catalogue.md)
  - [Appendix to the catalogue: types outside the classification, and disputed types](book/chapters/types-catalogue.md#类型详解附录分类体系外与有争议的类型)
- [Appendix A. Glossary of terms and abbreviations](book/chapters/appendix-a-glossary.md)
- [Appendix B. Public databases and widely used tools](book/chapters/appendix-b-databases-and-tools.md)
  - [Public TE and repeat databases](book/chapters/appendix-b-databases-and-tools.md#公共转座子与重复序列数据库)
  - [Core tools for TE annotation, curation, and evaluation](book/chapters/appendix-b-databases-and-tools.md#转座子注释精修与评估核心工具)
  - [Population TIP detection and routine helper tools](book/chapters/appendix-b-databases-and-tools.md#群体tips检测与常规辅助分析工具)
- [Appendix C. Further reading](book/chapters/appendix-c-further-reading.md)
  - [Basic theory, discovery, and genome evolution](book/chapters/appendix-c-further-reading.md#一基础理论发现史与基因组演化)
  - [Classification systems and bioinformatic annotation](book/chapters/appendix-c-further-reading.md#二分类体系与生物信息学注释方法)
  - [Epigenetic regulation and host silencing](book/chapters/appendix-c-further-reading.md#三表观遗传调控与宿主沉默)
  - [Grapevine genomes and worked TE examples](book/chapters/appendix-c-further-reading.md#四葡萄基因组与转座子范例研究)

Shorter type-by-type notes, with figures, are in [`docs/types/README.md`](docs/types/README.md) (Chinese index: [`docs/types/README.zh.md`](docs/types/README.zh.md)). Notes on TEs and the host are in [`docs/host/README.md`](docs/host/README.md) (Chinese: [`docs/host/README.zh.md`](docs/host/README.zh.md)). Notes on TEs in grapevine genomes are in [`docs/vitis/README.md`](docs/vitis/README.md) (Chinese: [`docs/vitis/README.zh.md`](docs/vitis/README.zh.md)). Teaching schematics are in [`figures/README.md`](figures/README.md).

## Software and workflow

The default route is EDTA, then TEtrimmer, then TEsorter, then a CDS-gated trusted library, then soft-masking or panEDTA. The decision tree is in [`docs/WORKFLOW.md`](docs/WORKFLOW.md). Software by step, field difficulties, and the same route in more detail are in [`docs/detection/tools_and_pipelines.md`](docs/detection/tools_and_pipelines.md). Sequence signatures used to recognise each type are in [`docs/detection/signatures.md`](docs/detection/signatures.md). The soft-mask hand-off into gene annotation is in [`docs/detection/softmask_handoff.md`](docs/detection/softmask_handoff.md). Each catalogue row, with a link, a title-matched DOI where one exists, inputs, outputs, and when to use the tool, is in [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv). Tool versions are not pinned. A DOI is listed only when the Crossref title matches the intended paper (checked 2026-11-15, Asia/Shanghai, CST, UTC+8). Items without a title-matched DOI are listed by URL only, or marked [待确认].

### Software by analysis step

Contents of this section: links to each step are below. The number in parentheses is the number of entries in that table. The tier rule and the pipeline coverage table are included. This section has 198 entries.

- [Tier rule](#tier-rule)
- [Complete pipelines and the steps they cover](#complete-pipelines-and-the-steps-they-cover) (14)
- [Complete pipelines: paper, lab and authority](#complete-pipelines-paper-lab-and-authority) (14)
- [Family finders and read-based repeat discovery](#family-finders-and-read-based-repeat-discovery) (8)
- [LTR retrotransposon detection](#ltr-retrotransposon-detection) (13)
- [TIR, MITE, Helitron and SINE detection](#tir-mite-helitron-and-sine-detection) (14)
- [Curation, redundancy reduction and library QC](#curation-redundancy-reduction-and-library-qc) (10)
- [Classification](#classification) (14)
- [Masking, annotation and cleaning of annotations](#masking-annotation-and-cleaning-of-annotations) (6)
- [Insertion age, landscape and horizontal transfer](#insertion-age-landscape-and-horizontal-transfer) (8)
- [Insertion polymorphism: short reads](#insertion-polymorphism-short-reads) (25)
- [Insertion polymorphism: long reads and call annotation](#insertion-polymorphism-long-reads-and-call-annotation) (9)
- [Insertion polymorphism: assemblies, pangenomes and graphs](#insertion-polymorphism-assemblies-pangenomes-and-graphs) (11)
- [Insertion polymorphism: plant resources and other inputs](#insertion-polymorphism-plant-resources-and-other-inputs) (2)
- [TE expression and small RNA](#te-expression-and-small-rna) (11)
- [Visualization](#visualization) (22)
  - [TE-specific views, landscapes and nesting diagrams](#te-specific-views-landscapes-and-nesting-diagrams) (6)
  - [Dotplots and identity heatmaps for repeats](#dotplots-and-identity-heatmaps-for-repeats) (3)
  - [Density and karyotype (ideogram) plots](#density-and-karyotype-ideogram-plots) (3)
  - [Circos-style circular plots](#circos-style-circular-plots) (2)
  - [Genome-browser tracks](#genome-browser-tracks) (4)
  - [Synteny, assembly-alignment and pangenome-graph views](#synteny-assembly-alignment-and-pangenome-graph-views) (4)
- [Polyploid subgenomes and tandem repeats](#polyploid-subgenomes-and-tandem-repeats) (3)
- [Databases and libraries: general](#databases-and-libraries-general) (5)
- [Databases and libraries: plants](#databases-and-libraries-plants) (11)
- [Databases and libraries: grapevine (Vitis)](#databases-and-libraries-grapevine-vitis) (2)
- [Simulation and benchmarking](#simulation-and-benchmarking) (6)
- [Community indexes and cross-links](#community-indexes-and-cross-links) (3)

The 198 software tools, databases and workflows in this catalogue are listed below by analysis step. Each entry gives its original paper, lab and authority; the tool link goes to the official repository or site. Longer notes are in [`docs/software/README.md`](docs/software/README.md), per-entry data in [`catalog/SOFTWARE_AUTHORITY.tsv`](catalog/SOFTWARE_AUTHORITY.tsv), and the check notes for each row in [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv).

**Default route:** [EDTA](https://github.com/oushujun/EDTA) → [TEtrimmer](https://github.com/qjiangzhao/TEtrimmer) → [TEsorter](https://github.com/zhangrengang/TEsorter) → a CDS-gated trusted library → soft-masking with [RepeatMasker](https://github.com/Dfam-consortium/RepeatMasker), or panEDTA for a panel of genomes. Only tools on this route are marked **default** in the tables. Where a step has no default, rows are ordered by paper citation count, which does not say which tool suits your genome.

#### Tier rule

> **Tier rule (stated once):** the indicator is the OpenAlex citation count of the paper (retrieved 2026-11-25). standard: 500 or more; established: 100–499; newer: fewer than 100 and the paper is from 2023 or later; niche: fewer than 100 and from before 2023; no paper: the catalogue has no title-matched paper. General-purpose tools such as BEDTools and IGV have counts from every field. Lab is the corresponding author named in the paper metadata with the institution (first one shown, +N for further corresponding authors; the last author when none is flagged). DOIs were checked against Crossref; the exceptions are in the `doi_check` column of `catalog/SOFTWARE_AUTHORITY.tsv`. This section has 198 entries: standard 28, established 47, newer 42, niche 58, no paper 23.

#### Complete pipelines and the steps they cover

yes means the documentation of the pipeline, or its catalogue entry, states the step; a dash only means it is not stated. Paper and lab for each pipeline are in the first table after this one.

| Pipeline | Library | Curation | Classification | Masking / annotation | Age / divergence | Panel of genomes | Tier · citations |
|---|---|---|---|---|---|---|---|
| **[EDTA](https://github.com/oushujun/EDTA)** (default route) | yes | yes | yes | yes | — | via panEDTA | standard · 1683 |
| **[panEDTA](https://github.com/oushujun/EDTA/blob/master/panEDTA.sh)** (default route) | — | yes | — | yes | — | yes | newer · 84 |
| [EDTA-GUI](https://github.com/Marcos-Fernando/EDTA-GUI) | as EDTA | as EDTA | yes | as EDTA | — | — | newer · 2 |
| [RepeatModeler2](https://github.com/Dfam-consortium/RepeatModeler) | yes | yes | yes | — | — | — | standard · 4333 |
| [Dfam TETools](https://github.com/Dfam-consortium/TETools) | via RepeatModeler | — | via RepeatModeler | via RepeatMasker | — | — | no paper |
| [Earl Grey](https://github.com/TobyBaril/EarlGrey) | yes | yes | yes | yes | yes | ParTEA | established · 292 |
| [ParTEA](https://github.com/TobyBaril/EarlGreyParTEA) | — | — | — | yes | — | yes | newer · 0, preprint |
| [HiTE](https://github.com/CSU-KangHu/HiTE) | yes | — | yes | yes | — | panHiTE | newer · 71 |
| [panHiTE](https://github.com/CSU-KangHu/HiTE) | yes | — | — | — | — | yes | newer · 5 |
| [REPET](https://urgi.versailles.inrae.fr/Tools/REPET) | yes | yes | — | yes | — | — | standard · 589 |
| [Tephra](https://github.com/sestaton/tephra) | yes | — | yes | yes | yes | — | no paper |
| [CARP](https://github.com/carp-te/carp-documentation) | yes | yes | — | yes | — | — | niche · 36 |
| [CLARI-TE](https://github.com/jdaron/CLARI-TE) | — | — | — | yes | — | — | no paper |
| [PanTE](https://github.com/unavailable-2374/Pan_TE) | yes | — | yes | — | — | yes | newer · 2, preprint |

#### Complete pipelines: paper, lab and authority

| Tool | Role | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|---|
| [EDTA](https://github.com/oushujun/EDTA) | **default** | *Genome biology* 2019 · [10.1186/s13059-019-1905-y](https://doi.org/10.1186/s13059-019-1905-y) | Ning Jiang, Michigan State University +2 | standard · 1683 |
| [panEDTA](https://github.com/oushujun/EDTA/blob/master/panEDTA.sh) | **default** | *Genome Research* 2024 · [10.1101/gr.278131.123](https://doi.org/10.1101/gr.278131.123) | Matthew B. Hufford, Iowa State University +1 | newer · 84 |
| [RepeatModeler2](https://github.com/Dfam-consortium/RepeatModeler) | alternative | *Proceedings of the National Academy of Sciences* 2020 · [10.1073/pnas.1921046117](https://doi.org/10.1073/pnas.1921046117) | Arian F. A. Smit, Institute for Systems Biology (last author) | standard · 4333 |
| [REPET](https://urgi.versailles.inrae.fr/Tools/REPET) | alternative | *PLoS ONE* 2011 · [10.1371/journal.pone.0016526](https://doi.org/10.1371/journal.pone.0016526) | Hadi Quesneville, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement | standard · 589 |
| [Earl Grey](https://github.com/TobyBaril/EarlGrey) | alternative | *Molecular Biology and Evolution* 2024 · [10.1093/molbev/msae068](https://doi.org/10.1093/molbev/msae068) | Tobias Baril, University of Exeter +1 | established · 292 |
| [HiTE](https://github.com/CSU-KangHu/HiTE) | alternative | *Nature Communications* 2024 · [10.1038/s41467-024-49912-8](https://doi.org/10.1038/s41467-024-49912-8) | Bin Hu, Beijing Institute of Technology +1 | newer · 71 |
| [CARP](https://github.com/carp-te/carp-documentation) | alternative | *PLoS ONE* 2018 · [10.1371/journal.pone.0193588](https://doi.org/10.1371/journal.pone.0193588) | David L. Adelson, The University of Adelaide | niche · 36 |
| [panHiTE](https://github.com/CSU-KangHu/HiTE) | alternative | *Plant Communications* 2025 · [10.1016/j.xplc.2025.101669](https://doi.org/10.1016/j.xplc.2025.101669) | Jianxin Wang, Central South University | newer · 5 |
| [EDTA-GUI](https://github.com/Marcos-Fernando/EDTA-GUI) | alternative | *BMC Genomics* 2026 · [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) | Alessandro M. Varani, Universidade Estadual Paulista (Unesp) +1 | newer · 2 |
| [PanTE](https://github.com/unavailable-2374/Pan_TE) | alternative | *Research Square* 2025 · [10.21203/rs.3.rs-5867196/v1](https://doi.org/10.21203/rs.3.rs-5867196/v1) | Yiwen Wang, The University of Melbourne | newer · 2, preprint |
| [ParTEA](https://github.com/TobyBaril/EarlGreyParTEA) | alternative | *bioRxiv (Cold Spring Harbor Laboratory)* 2026 · [10.64898/2026.11.04.764261](https://doi.org/10.64898/2026.11.04.764261) | Tobias Baril, Swedish Museum of Natural History | newer · 0, preprint |
| [CLARI-TE](https://github.com/jdaron/CLARI-TE) | alternative | — | — | no paper |
| [Dfam TETools](https://github.com/Dfam-consortium/TETools) | alternative | — | — | no paper |
| [Tephra](https://github.com/sestaton/tephra) | alternative | — | — | no paper |

#### Family finders and read-based repeat discovery

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [RepeatScout](https://github.com/Dfam-consortium/RepeatScout) | *Bioinformatics* 2005 · [10.1093/bioinformatics/bti1018](https://doi.org/10.1093/bioinformatics/bti1018) | Alkes L. Price, University of California San Diego | standard · 2427 |
| [RECON](https://github.com/Dfam-consortium/RECON) | *Genome Research* 2002 · [10.1101/gr.88502](https://doi.org/10.1101/gr.88502) | Sean R. Eddy, Howard Hughes Medical Institute | standard · 1126 |
| [PILER](https://www.drive5.com/piler/) | *Bioinformatics* 2005 · [10.1093/bioinformatics/bti1003](https://doi.org/10.1093/bioinformatics/bti1003) | R. C. Edgar, bob@drive5.com | standard · 807 |
| [TAREAN](https://repeatexplorer-elixir.cerit-sc.cz/galaxy/) | *Nucleic Acids Research* 2017 · [10.1093/nar/gkx257](https://doi.org/10.1093/nar/gkx257) | Jir̆í Macas, Institute of Plant Molecular Biology | established · 368 |
| [RepeatExplorer2](https://repeatexplorer-elixir.cerit-sc.cz) | *Nature Protocols* 2020 · [10.1038/s41596-020-0400-y](https://doi.org/10.1038/s41596-020-0400-y) | Jir̆í Macas, Czech Academy of Sciences | established · 320 |
| [Red](https://github.com/BioinformaticsToolsmith/Red) | *BMC Bioinformatics* 2015 · [10.1186/s12859-015-0654-5](https://doi.org/10.1186/s12859-015-0654-5) | Hani Z. Girgis, National Institutes of Health | established · 275 |
| [dnaPipeTE](https://github.com/clemgoub/dnaPipeTE) | *Genome Biology and Evolution* 2015 · [10.1093/gbe/evv050](https://doi.org/10.1093/gbe/evv050) | Matthieu Boulesteix, Lyon 1 Université | established · 240 |
| [Transposome](https://github.com/sestaton/Transposome) | *Bioinformatics* 2015 · [10.1093/bioinformatics/btv059](https://doi.org/10.1093/bioinformatics/btv059) | S. Evan Staton, University of Georgia | niche · 22 |

#### LTR retrotransposon detection

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [LTR_FINDER](https://github.com/xzhub/LTR_FINDER) | *Nucleic Acids Research* 2007 · [10.1093/nar/gkm286](https://doi.org/10.1093/nar/gkm286) | Hao Wang, Fudan University | standard · 2933 |
| [LTRharvest](https://github.com/genometools/genometools) | *BMC Bioinformatics* 2008 · [10.1186/1471-2105-9-18](https://doi.org/10.1186/1471-2105-9-18) | Ute Willhoeft, Universität Hamburg | standard · 1855 |
| [LTR_retriever](https://github.com/oushujun/LTR_retriever) | *Plant Physiology* 2017 · [10.1104/pp.17.01310](https://doi.org/10.1104/pp.17.01310) | Ning Jiang, Michigan State University | standard · 1703 |
| [LTRdigest](https://github.com/genometools/genometools) | *Nucleic Acids Research* 2009 · [10.1093/nar/gkp759](https://doi.org/10.1093/nar/gkp759) | Sascha Steinbiss, Universität Hamburg | established · 310 |
| [LTR_FINDER_parallel](https://github.com/oushujun/LTR_FINDER_parallel) | *Mobile DNA* 2019 · [10.1186/s13100-019-0193-0](https://doi.org/10.1186/s13100-019-0193-0) | Ning Jiang, Michigan State University | established · 291 |
| [DANTE and DANTE_LTR](https://github.com/kavonrtep/dante_ltr) | *NAR Genomics and Bioinformatics* 2024 · [10.1093/nargab/lqae113](https://doi.org/10.1093/nargab/lqae113) | Jir̆í Macas, Czech Academy of Sciences | newer · 42 |
| [Inpactor2](https://github.com/simonorozcoarias/Inpactor2) | *Briefings in Bioinformatics* 2022 · [10.1093/bib/bbac511](https://doi.org/10.1093/bib/bbac511) | Simón Orozco-Arias, Universidad de Caldas +3 | niche · 38 |
| [LTRpred](https://github.com/drostlab/LTRpred) | *The Journal of Open Source Software* 2020 · [10.21105/joss.02170](https://doi.org/10.21105/joss.02170) | Hajk‐Georg Drost, University of Cambridge | niche · 28 |
| [LtrDetector](https://github.com/BioinformaticsToolsmith/LtrDetector) | *BMC Genomics* 2019 · [10.1186/s12864-019-5796-9](https://doi.org/10.1186/s12864-019-5796-9) | Hani Z. Girgis, University of Tulsa | niche · 27 |
| [TE-greedy-nester](https://gitlab.fi.muni.cz/lexa/nested) | *Bioinformatics* 2020 · [10.1093/bioinformatics/btaa632](https://doi.org/10.1093/bioinformatics/btaa632) | Matej Lexa, Czech Academy of Sciences | niche · 24 |
| [MegaLTR](https://github.com/MoradMMokhtar/MegaLTR) | *Frontiers in Plant Science* 2023 · [10.3389/fpls.2023.1237426](https://doi.org/10.3389/fpls.2023.1237426) | Morad M. Mokhtar, Université Mohammed VI Polytechnique +1 | newer · 9 |
| [PhyLTR](https://github.com/mcsimenc/PhyLTR) | *Zenodo (CERN European Organization for Nuclear Research)* 2020 · [10.5281/zenodo.4256534](https://doi.org/10.5281/zenodo.4256534) | Der, JP. (last author) | niche · 0 |
| [MGEScan](https://github.com/MGEScan/mgescan) | — | — | no paper |

#### TIR, MITE, Helitron and SINE detection

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [MITE-Hunter](https://doi.org/10.1093/nar/gkq862) | *Nucleic Acids Research* 2010 · [10.1093/nar/gkq862](https://doi.org/10.1093/nar/gkq862) | S. R. Wessler, University of Georgia | standard · 759 |
| [HelitronScanner](https://sourceforge.net/projects/helitronscanner/) | *Proceedings of the National Academy of Sciences* 2014 · [10.1073/pnas.1410068111](https://doi.org/10.1073/pnas.1410068111) | Chunguang Du, Montclair State University (last author) | established · 307 |
| [TIR-Learner](https://github.com/oushujun/TIR-Learner) | *Molecular Plant* 2019 · [10.1016/j.molp.2019.02.008](https://doi.org/10.1016/j.molp.2019.02.008) | Thomas Peterson, Iowa State University | established · 175 |
| [MITE Tracker](https://github.com/INTABiotechMJ/MITE-Tracker) | *BMC Bioinformatics* 2018 · [10.1186/s12859-018-2376-y](https://doi.org/10.1186/s12859-018-2376-y) | Leonardo Sebastian Vanzetti, Consejo Nacional de Investigaciones Científicas y Técnicas | established · 144 |
| [Generic Repeat Finder (GRF)](https://github.com/bioinfolabmu/GenericRepeatFinder) | *Plant Physiology* 2019 · [10.1104/pp.19.00386](https://doi.org/10.1104/pp.19.00386) | Chun Liang, Miami University (last author) | established · 138 |
| [SINE-Finder](https://doi.org/10.1105/tpc.111.088682) | *The Plant Cell* 2011 · [10.1105/tpc.111.088682](https://doi.org/10.1105/tpc.111.088682) | Thomas Schmidt, Technische Universität Dresden (last author) | established · 128 |
| [detectMITE](https://sourceforge.net/projects/detectmite/) | *Scientific Reports* 2016 · [10.1038/srep19688](https://doi.org/10.1038/srep19688) | Guoli Ji, Xiamen University +1 | niche · 70 |
| [SINE_Scan](https://github.com/maohlzj/SINE_Scan) | *Bioinformatics* 2016 · [10.1093/bioinformatics/btw718](https://doi.org/10.1093/bioinformatics/btw718) | Hao Wang, University of Georgia | niche · 57 |
| [EAHelitron](https://github.com/dontkme/EAHelitron) | *BMC Bioinformatics* 2019 · [10.1186/s12859-019-2945-8](https://doi.org/10.1186/s12859-019-2945-8) | Yidan Ouyang, Huazhong Agricultural University +1 | niche · 50 |
| [miteFinderII](https://github.com/jhu99/miteFinder) | *BMC Medical Genomics* 2018 · [10.1186/s12920-018-0418-y](https://doi.org/10.1186/s12920-018-0418-y) | Xuequn Shang, Northwestern Polytechnical University | niche · 49 |
| [AnnoSINE](https://github.com/yangli557/AnnoSINE) | *Plant Physiology* 2021 · [10.1093/plphys/kiab524](https://doi.org/10.1093/plphys/kiab524) | Yanni Sun, City University of Hong Kong | niche · 23 |
| [MUSTv2](https://doi.org/10.1515/jib-2017-0029) | *Berichte aus der medizinischen Informatik und Bioinformatik/Journal of integrative bioinformatics* 2017 · [10.1515/jib-2017-0029](https://doi.org/10.1515/jib-2017-0029) | Qing Wu, Hangzhou Dianzi University +1 | niche · 20 |
| [AnnoSINE_v2](https://github.com/oushujun/AnnoSINE_v2) | *Mobile DNA* 2024 · [10.1101/2024.03.01.582874](https://doi.org/10.1101/2024.03.01.582874) | Yanni Sun, City University of Hong Kong +1 | newer · 4 |
| [DeepHel](https://github.com/lyysxb/DeepHel) | *Bioinformatics* 2026 · [10.1093/bioinformatics/btag817](https://doi.org/10.1093/bioinformatics/btag817) | Jianxin Wang, Central South University | newer · 0 |

#### Curation, redundancy reduction and library QC

| Tool | Role | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|---|
| [CD-HIT](https://github.com/weizhongli/cdhit) | **default** | *Bioinformatics* 2012 · [10.1093/bioinformatics/bts565](https://doi.org/10.1093/bioinformatics/bts565) | LiMin Fu, University of California San Diego +3 | standard · 12430 |
| [TEtrimmer](https://github.com/qjiangzhao/TEtrimmer) | **default** | *Nature Communications* 2025 · [10.1038/s41467-025-63889-y](https://doi.org/10.1038/s41467-025-63889-y) | Stefan Kusch, Forschungszentrum Jülich +1 | newer · 37 |
| [VSEARCH](https://github.com/torognes/vsearch) | alternative | *PeerJ* 2016 · [10.7717/peerj.2584](https://doi.org/10.7717/peerj.2584) | Frédéric Mahé, Centre de Coopération Internationale en Recherche Agronomique pour le Développement (last author) | standard · 12129 |
| [Tandem Repeats Finder (TRF)](https://tandem.bu.edu/trf/trf.html) | alternative | *Nucleic Acids Research* 1999 · [10.1093/nar/27.2.573](https://doi.org/10.1093/nar/27.2.573) | Gary Benson, Icahn School of Medicine at Mount Sinai | standard · 10371 |
| [MMseqs2](https://github.com/soedinglab/MMseqs2) | alternative | *Nature Biotechnology* 2017 · [10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) | Johannes Söding, Max Planck Institute for Biophysical Chemistry | standard · 5716 |
| [LTR Assembly Index (LAI)](https://github.com/oushujun/LTR_retriever) | alternative | *Nucleic Acids Research* 2018 · [10.1093/nar/gky730](https://doi.org/10.1093/nar/gky730) | Shujun Ou, Michigan State University | standard · 947 |
| [TE-Aid](https://github.com/clemgoub/TE-Aid) | alternative | *Mobile DNA* 2022 · [10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7) | Anna Victoria Protasio, University of Cambridge | established · 196 |
| [MCHelper](https://github.com/GonzalezLab/MCHelper) | alternative | *Genome Research* 2024 · [10.1101/gr.278821.123](https://doi.org/10.1101/gr.278821.123) | Josefa González, Consejo Superior de Investigaciones Científicas | newer · 51 |
| [SENMAP](https://github.com/simonorozcoarias/SENMAP) | alternative | *Berichte aus der medizinischen Informatik und Bioinformatik/Journal of integrative bioinformatics* 2022 · [10.1515/jib-2021-0036](https://doi.org/10.1515/jib-2021-0036) | Simón Orozco-Arias, Universidad de Caldas +6 | niche · 6 |
| [ColabCuraTE](https://github.com/Ellison-Lab/ColabCuraTE) | alternative | *Mobile DNA* 2025 · [10.1186/s13100-025-00389-2](https://doi.org/10.1186/s13100-025-00389-2) | Christopher E. Ellison, Rutgers, The State University of New Jersey | newer · 2 |

#### Classification

| Tool | Role | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|---|
| [TEsorter](https://github.com/zhangrengang/TEsorter) | **default** | *Horticulture Research* 2022 · [10.1093/hr/uhac017](https://doi.org/10.1093/hr/uhac017) | Rengang Zhang, Kunming Institute of Botany +2 | established · 376 |
| [REXdb](https://bitbucket.org/petrnovak/repex_tarean) | alternative | *Mobile DNA* 2019 · [10.1186/s13100-018-0144-1](https://doi.org/10.1186/s13100-018-0144-1) | Pavel Neumann, Czech Academy of Sciences | established · 478 |
| [TEclass](https://bioinformatics.uni-muenster.de/tools/teclass/index.hbi) | alternative | *Bioinformatics* 2009 · [10.1093/bioinformatics/btp084](https://doi.org/10.1093/bioinformatics/btp084) | György Abrusán, University of Münster | established · 443 |
| [PASTEC](https://urgi.versailles.inrae.fr/Tools/REPET) | alternative | *PLoS ONE* 2014 · [10.1371/journal.pone.0091929](https://doi.org/10.1371/journal.pone.0091929) | Hadi Quesneville, Ressources génomique-info | established · 350 |
| [DeepTE](https://github.com/LiLabAtVT/DeepTE) | alternative | *Bioinformatics* 2020 · [10.1093/bioinformatics/btaa519](https://doi.org/10.1093/bioinformatics/btaa519) | Song Li, Virginia Tech | established · 239 |
| [TERL](https://github.com/muriloHoracio/TERL) | alternative | *Briefings in Bioinformatics* 2020 · [10.1093/bib/bbaa185](https://doi.org/10.1093/bib/bbaa185) | Murilo Horacio Pereira da Cruz, Universidade Tecnológica Federal do Paraná +1 | niche · 64 |
| [Inpactor](https://github.com/simonorozcoarias/Inpactor) | alternative | *Biology* 2018 · [10.3390/biology7020032](https://doi.org/10.3390/biology7020032) | Romain Guyot, Centre de Coopération Internationale en Recherche Agronomique pour le Développement | niche · 34 |
| [ClassifyTE](https://github.com/manisa/ClassifyTE) | alternative | *Bioinformatics* 2021 · [10.1093/bioinformatics/btab146](https://doi.org/10.1093/bioinformatics/btab146) | Md Tamjidul Hoque, LSU New Orleans +1 | niche · 25 |
| [TEclass2](https://github.com/IOB-Muenster/TEclass2) | alternative | *Biology* 2025 · [10.3390/biology15010059](https://doi.org/10.3390/biology15010059) | Wojciech Makałowski, University of Münster | newer · 23 |
| [CREATE](https://doi.org/10.1093/bib/bbaf608) | alternative | *Briefings in Bioinformatics* 2025 · [10.1093/bib/bbaf608](https://doi.org/10.1093/bib/bbaf608) | Xingyu Liao, Northwestern Polytechnical University +1 | newer · 11 |
| [Terrier](https://doi.org/10.1093/bib/bbaf442) | alternative | *Briefings in Bioinformatics* 2025 · [10.1093/bib/bbaf442](https://doi.org/10.1093/bib/bbaf442) | Robert Turnbull, The University of Melbourne | newer · 10 |
| [NeuralTE](https://github.com/CSU-KangHu/NeuralTE) | alternative | *ACM International Conference on Bioinformatics, Computational Biology, and Health Informatics (ACM-BCB)* 2024 · [10.1145/3698587.3701346](https://doi.org/10.1145/3698587.3701346) | Jianxin Wang, Central South University | newer · 9 |
| [YORO](https://github.com/simonorozcoarias/YORO) | alternative | *PLoS ONE* 2023 · [10.1371/journal.pone.0291925](https://doi.org/10.1371/journal.pone.0291925) | Romain Guyot, Centre de Coopération Internationale en Recherche Agronomique pour le Développement | newer · 5 |
| [PanTEon](https://github.com/simonorozcoarias/PanTEon) | alternative | *bioRxiv (Cold Spring Harbor Laboratory)* 2026 · [10.64898/2026.04.01.715927](https://doi.org/10.64898/2026.04.01.715927) | Simón Orozco-Arias, Barcelona Supercomputing Center | newer · 1, preprint |

#### Masking, annotation and cleaning of annotations

| Tool | Role | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|---|
| [RepeatMasker](https://www.repeatmasker.org/) | **default** | — | — | no paper |
| [BEDTools](https://github.com/arq5x/bedtools2) | alternative | *Bioinformatics* 2010 · [10.1093/bioinformatics/btq033](https://doi.org/10.1093/bioinformatics/btq033) | Aaron R. Quinlan, University of Virginia +1 | standard · 30267 |
| [MAKER-P](https://yandell-lab.org/software/maker-p/) | alternative | *Plant Physiology* 2013 · [10.1104/pp.113.230144](https://doi.org/10.1104/pp.113.230144) | Mark D. Yandell, Eccles Institute of Human Genetics (M.S.C., M.L., M.Y.) and (last author) | established · 451 |
| [oneCodeToFindThemAll](https://doua.prabi.fr/software/one-code-to-find-them-all) | alternative | *Mobile DNA* 2014 · [10.1186/1759-8753-5-13](https://doi.org/10.1186/1759-8753-5-13) | Emmanuelle Lerat, Lyon 1 Université | established · 213 |
| [RepeatCraft](https://github.com/niccw/repeatcraftp) | alternative | *Bioinformatics* 2018 · [10.1093/bioinformatics/bty745](https://doi.org/10.1093/bioinformatics/bty745) | Wai Yee Wong, University of Vienna | niche · 51 |
| [Soft-mask hand-off (this repository)](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md) | alternative | — | — | no paper |

#### Insertion age, landscape and horizontal transfer

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [VHICA](https://cran.r-project.org/package=vhica) | *Molecular Biology and Evolution* 2015 · [10.1093/molbev/msv341](https://doi.org/10.1093/molbev/msv341) | Gabriel Luz Wallau, Universidade Federal de Santa Maria | niche · 78 |
| [HTT-DB](https://web.archive.org/web/20220814084307/http://lpa.saogabriel.unipampa.edu.br:8080/httdatabase/) | *Bioinformatics* 2015 · [10.1093/bioinformatics/btv281](https://doi.org/10.1093/bioinformatics/btv281) | Bruno Reis Dotto, Universidade Federal do Pampa +1 | niche · 62 |
| [REANNOTATE](https://web.archive.org/web/20120208050248/http://www.bioinformatics.org/reannotate/) | *BMC Genomics* 2008 · [10.1186/1471-2164-9-614](https://doi.org/10.1186/1471-2164-9-614) | Vini Pereira, Quadram Institute | niche · 37 |
| [TE_Density](https://github.com/sjteresi/TE_Density) | *Mobile DNA* 2022 · [10.1186/s13100-022-00264-4](https://doi.org/10.1186/s13100-022-00264-4) | Patrick P. Edger, Michigan State University | niche · 17 |
| [TEGRiP](https://github.com/marieBvr/TEs_genes_relationship_pipeline) | *Peer Community Journal* 2021 · [10.24072/pcjournal.57](https://doi.org/10.24072/pcjournal.57) | Quynh-Trang Bui, Université de Bordeaux (last author) | niche · 7 |
| [ParseRM](https://github.com/4ureliek/Parsing-RepeatMasker-Outputs) | — | — | no paper |
| [RepeatLandscape](https://github.com/caballero/RepeatLandscape) | — | — | no paper |
| [Repeattools](https://github.com/AgustinAmata/Repeattools) | — | — | no paper |

#### Insertion polymorphism: short reads

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [MELT](https://melt.igs.umaryland.edu) | *Genome Research* 2017 · [10.1101/gr.218032.116](https://doi.org/10.1101/gr.218032.116) | Scott E. Devine, University of Maryland, Baltimore | established · 411 |
| [TEPID](https://github.com/ListerLab/TEPID) | *eLife* 2016 · [10.7554/eLife.20777](https://doi.org/10.7554/eLife.20777) | Ryan Lister, The University of Western Australia | established · 261 |
| [RetroSeq](https://github.com/tk2/RetroSeq) | *Bioinformatics* 2012 · [10.1093/bioinformatics/bts697](https://doi.org/10.1093/bioinformatics/bts697) | Thomas Keane, Wellcome Sanger Institute | established · 229 |
| [TEMP](https://github.com/JialiUMassWengLab/TEMP) | *Nucleic Acids Research* 2014 · [10.1093/nar/gku323](https://doi.org/10.1093/nar/gku323) | William E. Theurkauf, University of Massachusetts Chan Medical School +1 | established · 146 |
| [xTea](https://github.com/parklab/xTea) | *Nature Communications* 2021 · [10.1038/s41467-021-24041-8](https://doi.org/10.1038/s41467-021-24041-8) | Eunjung Alice Lee, Broad Institute +1 | established · 131 |
| [PoPoolationTE2](https://doi.org/10.1093/molbev/msw137) | *Molecular Biology and Evolution* 2016 · [10.1093/molbev/msw137](https://doi.org/10.1093/molbev/msw137) | Christian Schlötterer, University of Veterinary Medicine Vienna | established · 129 |
| [Mobster](https://github.com/jyhehir/mobster) | *Genome biology* 2014 · [10.1186/s13059-014-0488-x](https://doi.org/10.1186/s13059-014-0488-x) | Jayne Y. Hehir‐Kwa, Radboud University Medical Center | established · 118 |
| [TEFLoN](https://github.com/jradrion/TEFLoN) | *Genome Biology and Evolution* 2017 · [10.1093/gbe/evx050](https://doi.org/10.1093/gbe/evx050) | Sarah Schaack, Reed College | niche · 91 |
| [ITIS](https://web.archive.org/web/20160825205722/http://bioinformatics.psc.ac.cn:80/software/ITIS/) | *BMC Bioinformatics* 2015 · [10.1186/s12859-015-0507-2](https://doi.org/10.1186/s12859-015-0507-2) | Renyi Liu, Chinese Academy of Sciences +1 | niche · 66 |
| [TEMP2](https://github.com/weng-lab/TEMP2) | *Nucleic Acids Research* 2021 · [10.1093/nar/gkab010](https://doi.org/10.1093/nar/gkab010) | William E. Theurkauf, University of Massachusetts Chan Medical School +2 | niche · 66 |
| [MEGAnE](https://github.com/shohei-kojima/MEGAnE) | *Nature Genetics* 2023 · [10.1101/2022.03.25.485726](https://doi.org/10.1101/2022.03.25.485726) | Shohei Kojima, RIKEN +1 | newer · 64 |
| [RelocaTE2](https://github.com/JinfengChen/RelocaTE2) | *PeerJ* 2017 · [10.7717/peerj.2942](https://doi.org/10.7717/peerj.2942) | J. Stajich, University of California, Riverside (last author) | niche · 56 |
| [Jitterbug](https://github.com/elzbth/jitterbug) | *BMC Genomics* 2015 · [10.1186/s12864-015-1975-5](https://doi.org/10.1186/s12864-015-1975-5) | Josep Casacuberta, Center for Research in Agricultural Genomics +1 | niche · 53 |
| [TIF](https://github.com/akiomiyao/tif) | *BMC Bioinformatics* 2014 · [10.1186/1471-2105-15-71](https://doi.org/10.1186/1471-2105-15-71) | Akio Miyao, Institute of Agrobiological Sciences | niche · 45 |
| [TE-Tracker](https://web.archive.org/web/20170813054646/http://www.genoscope.cns.fr:80/externe/tetracker/) | *BMC Bioinformatics* 2014 · [10.1186/s12859-014-0377-z](https://doi.org/10.1186/s12859-014-0377-z) | Vincent Colot, Centre National de la Recherche Scientifique +1 | niche · 36 |
| [ngs_te_mapper2](https://github.com/bergmanlab/ngs_te_mapper2) | *Genetics* 2021 · [10.1093/genetics/iyab113](https://doi.org/10.1093/genetics/iyab113) | Casey Bergman, University of Georgia | niche · 27 |
| [T-lex3](https://github.com/GonzalezLab/T-lex3) | *Bioinformatics* 2019 · [10.1093/bioinformatics/btz727](https://doi.org/10.1093/bioinformatics/btz727) | Josefa González, Universitat Pompeu Fabra | niche · 27 |
| [McClintock 2](https://github.com/bergmanlab/mcclintock) | *Mobile DNA* 2023 · [10.1186/s13100-023-00296-4](https://doi.org/10.1186/s13100-023-00296-4) | Casey Bergman, University of Georgia | newer · 21 |
| [TEfinder](https://github.com/VistaSohrab/TEfinder) | *Genes* 2021 · [10.3390/genes12020224](https://doi.org/10.3390/genes12020224) | Li‐Jun Ma, University of Massachusetts Amherst +1 | niche · 19 |
| [TIP_finder](https://github.com/simonorozcoarias/TIP_finder) | *Biology* 2020 · [10.3390/biology9090281](https://doi.org/10.3390/biology9090281) | Simón Orozco-Arias, Universidad de Caldas +1 | niche · 11 |
| [TEF](https://github.com/akiomiyao/tef) | *BMC Bioinformatics* 2022 · [10.1186/s12859-022-05011-3](https://doi.org/10.1186/s12859-022-05011-3) | Akio Miyao, National Agriculture and Food Research Organization | niche · 6 |
| [TypeSINE](https://github.com/mobilome/TypeSINE) | *bioRxiv (Cold Spring Harbor Laboratory)* 2025 · [10.1101/2025.05.21.653756](https://doi.org/10.1101/2025.05.21.653756) | Chengyi Song, Yangzhou University | newer · 2, preprint |
| [ELITE](https://github.com/Anwica/ELITE) | *ACM International Conference on Bioinformatics, Computational Biology, and Health Informatics (ACM-BCB)* 2019 · [10.1145/3307339.3342182](https://doi.org/10.1145/3307339.3342182) | Leonard McMillan, University of North Carolina at Chapel Hill (last author) | niche · 1 |
| [TE-locate](https://sourceforge.net/projects/te-locate/) | — | — | no paper |
| [TRACKPOSON](https://github.com/Markestine/TRACKPOSON) | — | — | no paper |

#### Insertion polymorphism: long reads and call annotation

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [PALMER](https://github.com/WeichenZhou/PALMER) | *Nucleic Acids Research* 2019 · [10.1093/nar/gkz1173](https://doi.org/10.1093/nar/gkz1173) | Ryan E. Mills, University of Michigan | established · 104 |
| [LoRTE](https://doi.org/10.1186/s13100-017-0088-x) | *Mobile DNA* 2017 · [10.1186/s13100-017-0088-x](https://doi.org/10.1186/s13100-017-0088-x) | Jonathan Filée, Centre National de la Recherche Scientifique (last author) | niche · 38 |
| [TrEMOLO](https://github.com/DrosophilaGenomeEvolution/TrEMOLO) | *Genome biology* 2023 · [10.1186/s13059-023-02911-2](https://doi.org/10.1186/s13059-023-02911-2) | Anna-Sophie Fiston-Lavier, Centre National de la Recherche Scientifique +1 | newer · 34 |
| [TELR](https://github.com/bergmanlab/telr) | *Nucleic Acids Research* 2022 · [10.1093/nar/gkac794](https://doi.org/10.1093/nar/gkac794) | Casey Bergman, University of Georgia | niche · 28 |
| [rMETL](https://github.com/tjiangHIT/rMETL) | *Bioinformatics* 2019 · [10.1093/bioinformatics/btz106](https://doi.org/10.1093/bioinformatics/btz106) | Yadong Wang, Harbin Institute of Technology | niche · 25 |
| [sTELLeR](https://github.com/kristinebilgrav/sTELLeR) | *Bioinformatics* 2024 · [10.1093/bioinformatics/btae686](https://doi.org/10.1093/bioinformatics/btae686) | Kristine Bilgrav Sæther, Science for Life Laboratory | newer · 12 |
| [somrit](https://github.com/adcosta17/somrit) | *bioRxiv (Cold Spring Harbor Laboratory)* 2023 · [10.1101/2023.08.06.552193](https://doi.org/10.1101/2023.08.06.552193) | Jared T. Simpson, Ontario Institute for Cancer Research | newer · 3, preprint |
| [MEIGA-PAV](https://github.com/MEIGA-tk/MEIGA-PAV) | — | — | no paper |
| [SVAN](https://github.com/REPBIO-LAB/SVAN) | — | — | no paper |

#### Insertion polymorphism: assemblies, pangenomes and graphs

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [SyRI](https://github.com/schneebergerlab/syri) | *Genome biology* 2019 · [10.1186/s13059-019-1911-0](https://doi.org/10.1186/s13059-019-1911-0) | Korbinian Schneeberger, Max Planck Institute for Plant Breeding Research | standard · 1256 |
| [PanGenie](https://github.com/eblerjana/pangenie) | *Nature Genetics* 2022 · [10.1038/s41588-022-01043-w](https://doi.org/10.1038/s41588-022-01043-w) | Tobias Marschall, Heinrich Heine University Düsseldorf | established · 349 |
| [Paragraph](https://github.com/Illumina/paragraph) | *Genome biology* 2019 · [10.1186/s13059-019-1909-7](https://doi.org/10.1186/s13059-019-1909-7) | Michael A. Eberle, Illumina (United States) | established · 246 |
| [SVIM-asm](https://github.com/eldariont/svim-asm) | *Bioinformatics* 2020 · [10.1093/bioinformatics/btaa1034](https://doi.org/10.1093/bioinformatics/btaa1034) | Martin Vingron, Max Planck Institute for Molecular Genetics | established · 232 |
| [AnchorWave](https://github.com/baoxingsong/AnchorWave) | *Proceedings of the National Academy of Sciences* 2021 · [10.1073/pnas.2113075119](https://doi.org/10.1073/pnas.2113075119) | Baoxing Song, Cornell University +2 | established · 120 |
| [ITIPs](https://github.com/caixu0518/ITIPs) | *Plant Biotechnology Journal* 2022 · [10.1111/pbi.13807](https://doi.org/10.1111/pbi.13807) | Jian Wu, Institute of Vegetables and Flowers +1 | niche · 87 |
| [GraffiTE](https://github.com/cgroza/GraffiTE) | *Nature Communications* 2024 · [10.1038/s41467-024-53294-2](https://doi.org/10.1038/s41467-024-53294-2) | Clément Goubert, University of Arizona | newer · 54 |
| [pantera](https://github.com/piosierra/pantera) | *Mobile DNA* 2024 · [10.1186/s13100-024-00323-y](https://doi.org/10.1186/s13100-024-00323-y) | Richard Michael Durbin, University of Cambridge | newer · 31 |
| [panREPET](https://forgemia.inra.fr/urgi-anagen/panREPET) | *Genome biology* 2026 · [10.1186/s13059-026-03984-5](https://doi.org/10.1186/s13059-026-03984-5) | Hadi Quesneville, Institut National de Recherche pour l'Agriculture, l'Alimentation et l'Environnement | newer · 9 |
| [panTEvo](https://github.com/Lcamdom/panTEvo) | *Genome biology* 2025 · [10.1186/s13059-025-03837-7](https://doi.org/10.1186/s13059-025-03837-7) | Lucía Campos, Universitat Autònoma de Barcelona +1 | newer · 9 |
| [Pannagram](https://github.com/iganna/pannagram) | *bioRxiv (Cold Spring Harbor Laboratory)* 2025 · [10.1101/2025.02.07.637071](https://doi.org/10.1101/2025.02.07.637071) | Anna A. Igolkina, Gregor Mendel Institute of Molecular Plant Biology | newer · 6, preprint |

#### Insertion polymorphism: plant resources and other inputs

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [RTRIP](https://web.archive.org/web/20240226054850/http://ibi.zju.edu.cn/Rtrip/index.html) | *Plant Biotechnology Journal* 2020 · [10.1111/pbi.13425](https://doi.org/10.1111/pbi.13425) | Jian‐Hong Xu, Zhejiang University | niche · 20 |
| [TEPEAK](https://github.com/ryanlayerlab/TEPEAK) | *PLoS Computational Biology* 2026 · [10.1371/journal.pcbi.1013122](https://doi.org/10.1371/journal.pcbi.1013122) | Devin Burke, University of Colorado Boulder | newer · 1 |

#### TE expression and small RNA

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [TEtranscripts](https://github.com/mhammell-laboratory/TEtranscripts) | *Bioinformatics* 2015 · [10.1093/bioinformatics/btv422](https://doi.org/10.1093/bioinformatics/btv422) | Molly Hammell, Cold Spring Harbor Laboratory | standard · 822 |
| [ShortStack](https://github.com/MikeAxtell/ShortStack) | *Rna* 2013 · [10.1261/rna.035279.112](https://doi.org/10.1261/rna.035279.112) | Michael J. Axtell, Pennsylvania State University | standard · 579 |
| [RepEnrich](https://doi.org/10.1186/1471-2164-15-583) | *BMC Genomics* 2014 · [10.1186/1471-2164-15-583](https://doi.org/10.1186/1471-2164-15-583) | Nicola Neretti, Brown University | established · 360 |
| [SQuIRE](https://github.com/wyang17/SQuIRE) | *Nucleic Acids Research* 2019 · [10.1093/nar/gky1301](https://doi.org/10.1093/nar/gky1301) | Lindsay M. Payer, Johns Hopkins University +1 | established · 232 |
| [Telescope](https://github.com/mlbendall/telescope) | *PLoS Computational Biology* 2019 · [10.1371/journal.pcbi.1006453](https://doi.org/10.1371/journal.pcbi.1006453) | Douglas F. Nixon, Weill Cornell Medicine | established · 227 |
| [TEtools](https://github.com/l-modolo/TEtools) | *Nucleic Acids Research* 2016 · [10.1093/nar/gkw953](https://doi.org/10.1093/nar/gkw953) | Emmanuelle Lerat, Lyon 1 Université +3 | established · 149 |
| [SalmonTE](https://github.com/jeonglab-bcm/SalmonTE) | *Pacific Symposium on Biocomputing (PSB)* 2017 · [10.1142/9789813235533_0016](https://doi.org/10.1142/9789813235533_0016) | Zhandong Liu, Baylor College of Medicine (last author) | established · 109 |
| [SoloTE](https://github.com/bvaldebenitom/SoloTE) | *Communications Biology* 2022 · [10.1038/s42003-022-04020-5](https://doi.org/10.1038/s42003-022-04020-5) | Braulio Valdebenito‐Maturana, Icahn School of Medicine at Mount Sinai | niche · 76 |
| [piPipes](https://github.com/bowhan/piPipes) | — | — | no paper |
| [scTE](https://github.com/JiekaiLab/scTE) | — | — | no paper |
| [TElocal](https://github.com/mhammell-laboratory/TElocal) | — | — | no paper |

#### Visualization

Grouped by purpose. General-purpose entries are not limited to transposable elements; the TE use is that you supply the TE coordinates or track.

##### TE-specific views, landscapes and nesting diagrams

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [TEnest](https://github.com/cmdcolin/TEnest) | *Plant Physiology* 2007 · [10.1104/pp.107.110353](https://doi.org/10.1104/pp.107.110353) | Roger P. Wise, Agricultural Research Service | niche · 81 |
| [UCSC Repeat Browser](https://repeatbrowser.ucsc.edu) | *Mobile DNA* 2020 · [10.1186/s13100-020-00208-w](https://doi.org/10.1186/s13100-020-00208-w) | Sofie R. Salama, Howard Hughes Medical Institute +1 | niche · 53 |
| [RepeatOBserver](https://github.com/celphin/RepeatOBserverV1) | *Molecular Ecology Resources* 2025 · [10.1111/1755-0998.14084](https://doi.org/10.1111/1755-0998.14084) | Cassandra Elphinstone, University of British Columbia | newer · 32 |
| [LTRsift](https://github.com/satta/ltrsift) | *Mobile DNA* 2012 · [10.1186/1759-8753-3-18](https://doi.org/10.1186/1759-8753-3-18) | Stefan Kurtz, Universität Hamburg | niche · 13 |
| [DfamTEBrowser](https://github.com/Dfam-consortium/DfamTEBrowser) | — | — | no paper |
| [RepeatMasker landscape utilities (calcDivergenceFromAlign.pl, createRepeatLandscape.pl)](https://github.com/Dfam-consortium/RepeatMasker/blob/master/util/createRepeatLandscape.pl) | — | R. M. Hubley, J. Caballero, Institute for Systems Biology (script headers) | no paper |

##### Dotplots and identity heatmaps for repeats

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [StainedGlass](https://github.com/vollgerlab/StainedGlass) | *Bioinformatics* 2022 · [10.1093/bioinformatics/btac018](https://doi.org/10.1093/bioinformatics/btac018) | Mitchell Robert Vollger, University of Washington +1 | established · 177 |
| [FlexiDot](https://github.com/molbio-dresden/flexidot) | *Bioinformatics* 2018 · [10.1093/bioinformatics/bty395](https://doi.org/10.1093/bioinformatics/bty395) | Tony Heitkam, Technische Universität Dresden | niche · 95 |
| [ModDotPlot](https://github.com/marbl/ModDotPlot) | *Bioinformatics* 2024 · [10.1093/bioinformatics/btae493](https://doi.org/10.1093/bioinformatics/btae493) | Alexander P. Sweeten, National Institutes of Health +1 | newer · 86 |

##### Density and karyotype (ideogram) plots

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [karyoploteR](https://github.com/bernatgel/karyoploteR) | *Bioinformatics* 2017 · [10.1093/bioinformatics/btx346](https://doi.org/10.1093/bioinformatics/btx346) | Bernat Gel, Institut d'Investigació en Ciències de la Salut Germans Trias i Pujol | standard · 845 |
| [RIdeogram](https://github.com/TickingClock1992/RIdeogram) | *PeerJ Computer Science* 2020 · [10.7717/peerj-cs.251](https://doi.org/10.7717/peerj-cs.251) | Guangchuang Yu, Southern Medical University +1 | standard · 633 |
| [chromoMap](https://github.com/lakshay-anand/chromoMap) | *BMC Bioinformatics* 2022 · [10.1186/s12859-021-04556-z](https://doi.org/10.1186/s12859-021-04556-z) | Lakshay Anand, University of Kentucky | established · 261 |

##### Circos-style circular plots

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [circlize](https://github.com/jokergoo/circlize) | *Bioinformatics* 2014 · [10.1093/bioinformatics/btu393](https://doi.org/10.1093/bioinformatics/btu393) | Benedikt Brors, German Cancer Research Center | standard · 4971 |
| [interacCircos](https://github.com/mrcuizhe/interacCircos) | *Bioinformatics* 2021 · [10.1093/bioinformatics/btab232](https://doi.org/10.1093/bioinformatics/btab232) | Tianyi Zang, Harbin Institute of Technology +1 | niche · 19 |

##### Genome-browser tracks

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [IGV](https://github.com/igvteam/igv) | *Briefings in Bioinformatics* 2012 · [10.1093/bib/bbs017](https://doi.org/10.1093/bib/bbs017) | J. T. Robinson, Broad Institute | standard · 10150 |
| [JBrowse 2](https://github.com/GMOD/jbrowse-components) | *Genome biology* 2023 · [10.1186/s13059-023-02914-z](https://doi.org/10.1186/s13059-023-02914-z) | Ian H Holmes, University of California, Berkeley | standard · 907 |
| [igv.js](https://github.com/igvteam/igv.js) | *Bioinformatics* 2022 · [10.1093/bioinformatics/btac830](https://doi.org/10.1093/bioinformatics/btac830) | James T Robinson, University of California San Diego | standard · 648 |
| [pyGenomeTracks](https://github.com/deeptools/pyGenomeTracks) | *Bioinformatics* 2020 · [10.1093/bioinformatics/btaa692](https://doi.org/10.1093/bioinformatics/btaa692) | Fidel Ramírez, Max Planck Institute of Immunobiology and Epigenetics | standard · 575 |

##### Synteny, assembly-alignment and pangenome-graph views

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [plotsr](https://github.com/schneebergerlab/plotsr) | *Bioinformatics* 2022 · [10.1093/bioinformatics/btac196](https://doi.org/10.1093/bioinformatics/btac196) | Korbinian Schneeberger, Ludwig-Maximilians-Universität München | established · 383 |
| [ODGI](https://github.com/pangenome/odgi) | *Bioinformatics* 2022 · [10.1093/bioinformatics/btac308](https://doi.org/10.1093/bioinformatics/btac308) | Erik P. Garrison, University of Tennessee Health Science Center | established · 233 |
| [NGenomeSyn](https://github.com/hewm2008/NGenomeSyn) | *Bioinformatics* 2023 · [10.1093/bioinformatics/btad121](https://doi.org/10.1093/bioinformatics/btad121) | Xiaodong Fang, BGI Group (China) | established · 195 |
| [SVbyEye](https://github.com/daewoooo/SVbyEye) | *Bioinformatics* 2025 · [10.1093/bioinformatics/btaf332](https://doi.org/10.1093/bioinformatics/btaf332) | David Porubskỳ, University of Washington | newer · 71 |

Related entries in other steps: ParseRM, RepeatLandscape, Repeattools, TE_Density, TE-Aid.

#### Polyploid subgenomes and tandem repeats

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [SubPhaser](https://github.com/zhangrengang/SubPhaser) | *New Phytologist* 2022 · [10.1111/nph.18173](https://doi.org/10.1111/nph.18173) | Jian‐Feng Mao, Beijing Forestry University (last author) | established · 179 |
| [TRASH](https://github.com/vlothec/TRASH) | *Bioinformatics* 2023 · [10.1093/bioinformatics/btad308](https://doi.org/10.1093/bioinformatics/btad308) | Ian R. Henderson, University of Cambridge | established · 115 |
| [PolyCRACKER](https://bitbucket.org/berkeleylab/jgi-polycracker/) | *BMC Genomics* 2019 · [10.1186/s12864-019-5828-5](https://doi.org/10.1186/s12864-019-5828-5) | Sean Gordon, Joint Genome Institute +1 | niche · 20 |

#### Databases and libraries: general

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [Repbase Update](https://www.girinst.org/repbase/) | *Cytogenetic and Genome Research* 2005 · [10.1159/000084979](https://doi.org/10.1159/000084979) | Jolanta Walichiewicz, Genetic Information Research Institute (last author) | standard · 3782 |
| [Dfam (Storer et al. 2021)](https://www.dfam.org/) | *Mobile DNA* 2021 · [10.1186/s13100-020-00230-y](https://doi.org/10.1186/s13100-020-00230-y) | Jessica M. Storer, Institute for Systems Biology +2 | standard · 838 |
| [SINEBase](https://sines.eimb.ru/) | *Nucleic Acids Research* 2012 · [10.1093/nar/gks1263](https://doi.org/10.1093/nar/gks1263) | Dmitri A. Kramerov, Engelhardt Institute of Molecular Biology | established · 229 |
| [RepetDB](https://urgi.versailles.inrae.fr/repetdb) | *Mobile DNA* 2019 · [10.1186/s13100-019-0150-y](https://doi.org/10.1186/s13100-019-0150-y) | Joëlle Amselem, Université Paris-Saclay | niche · 72 |
| [TREP](https://trep-db.uzh.ch) | — | — | no paper |

#### Databases and libraries: plants

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [TIGR Plant Repeat Databases](https://rice.uga.edu/pub/data/TIGR_Plant_Repeats/) | *Nucleic Acids Research* 2003 · [10.1093/nar/gkh099](https://doi.org/10.1093/nar/gkh099) | Shu Ouyang, The Institute for Genomic Research, 9712 Medical Center Drive, Rockville, MD 20850, USA | established · 335 |
| [SoyTEdb](https://legacy.soybase.org/soytedb/) | *BMC Genomics* 2010 · [10.1186/1471-2164-11-113](https://doi.org/10.1186/1471-2164-11-113) | Randy C. Shoemaker, Agricultural Research Service +1 | established · 157 |
| [RiTE-db](https://ava.genome.arizona.edu/cgi-bin/rite/index.cgi) | *BMC Genomics* 2015 · [10.1186/s12864-015-1762-3](https://doi.org/10.1186/s12864-015-1762-3) | Rod A. Wing, University of Arizona | niche · 84 |
| RetrOryza | *Nucleic Acids Research* 2006 · [10.1093/nar/gkl780](https://doi.org/10.1093/nar/gkl780) | Olivier Panaud, University of Arizona | niche · 66 |
| [PlantRep](https://doi.org/10.1007/s00299-021-02817-y) | *Plant Cell Reports* 2022 · [10.1007/s00299-021-02817-y](https://doi.org/10.1007/s00299-021-02817-y) | Yu Zhang, Sun Yat-sen University | niche · 47 |
| [DPTEdb](https://web.archive.org/web/20180812090334/http://genedenovoweb.ticp.net:81/DPTEdb/index.php) | *Database* 2016 · [10.1093/database/baw078](https://doi.org/10.1093/database/baw078) | Lianfeng Gu, Fujian Agriculture and Forestry University +1 | niche · 24 |
| [InpactorDB](https://inpactordb.github.io) | *Genes* 2021 · [10.3390/genes12020190](https://doi.org/10.3390/genes12020190) | Simón Orozco-Arias, Universidad de Caldas +1 | niche · 24 |
| [SPTEdb](https://web.archive.org/web/20180730000921/http://genedenovoweb.ticp.net:81/SPTEdb/index.php) | *Database* 2018 · [10.1093/database/bay024](https://doi.org/10.1093/database/bay024) | Wenjun Ma, Chinese Academy of Forestry +1 | niche · 22 |
| [PlantLTRdb](https://bioinformatics.um6p.ma/PlantLTRdb/) | *Frontiers in Plant Science* 2023 · [10.3389/fpls.2023.1134627](https://doi.org/10.3389/fpls.2023.1134627) | Morad M. Mokhtar, Université Mohammed VI Polytechnique +1 | newer · 21 |
| [ConTEdb](https://web.archive.org/web/20210921143932/http://genedenovoweb.ticp.net:81/conTEdb/index.php) | *Database* 2018 · [10.1093/database/bay131](https://doi.org/10.1093/database/bay131) | Fangqun Ouyang, Chinese Academy of Forestry +1 | niche · 20 |
| [AnnoTEP-DB](https://plantgenomics.ncc.unesp.br/AnnoTEP-DB/) | *BMC Genomics* 2026 · [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) | Alessandro M. Varani, Universidade Estadual Paulista (Unesp) +1 | newer · 2 |
| [MaizeGP](https://github.com/Jia-nianhua/Maize-Graph-Pangenome) | *Journal of Integrative Plant Biology* 2026 · [10.1111/jipb.70439](https://doi.org/10.1111/jipb.70439) | Shaojiang Chen, China Agricultural University +2 | newer · 0 |

#### Databases and libraries: grapevine (Vitis)

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [PN40024 T2T TE annotations](https://zenodo.org/records/13741133) | *DIGITAL.CSIC (Spanish National Research Council (CSIC))* 2023 · [10.5281/zenodo.13741133](https://doi.org/10.5281/zenodo.13741133) | ShiXiaoya | newer · 1 |
| [GrapeGenomics Vitis RepeatMasker library](https://grapegenomics.com/pages/repeats.php) | — | — | no paper |

#### Simulation and benchmarking

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [simuG](https://github.com/yjx1217/simuG) | *Bioinformatics* 2019 · [10.1093/bioinformatics/btz424](https://doi.org/10.1093/bioinformatics/btz424) | Jia‐Xing Yue, Centre National de la Recherche Scientifique +1 | niche · 61 |
| [PrinTE](https://github.com/cwb14/PrinTE) | *Nature Communications* 2026 · [10.1101/2025.06.04.657780](https://doi.org/10.1101/2025.06.04.657780) | Shujun Ou, The Ohio State University | newer · 2 |
| [TEgenomeSimulator](https://github.com/Plant-Food-Research-Open/TEgenomeSimulator) | *bioRxiv (Cold Spring Harbor Laboratory)* 2026 · [10.64898/2026.03.09.710711](https://doi.org/10.64898/2026.03.09.710711) | Ting-Hsuan Chen, Bioeconomy Science Institute | newer · 2, preprint |
| [TEvarSim](https://github.com/daweili-lab/TEvarSim) | *PLoS Computational Biology* 2026 · [10.1371/journal.pcbi.1013933](https://doi.org/10.1371/journal.pcbi.1013933) | Dawei Li, Texas Tech University | newer · 2 |
| [TE_Bench](https://doi.org/10.1186/s13100-026-00405-z) | *Mobile DNA* 2026 · [10.1186/s13100-026-00405-z](https://doi.org/10.1186/s13100-026-00405-z) | Hannah Kania, Duke University | newer · 1 |
| [TE_simu](https://github.com/unavailable-2374/TE_simu) | — | — | no paper |

#### Community indexes and cross-links

| Tool | Paper (journal year, DOI) | Lab (corresponding author, institution) | Tier · citations |
|---|---|---|---|
| [TE Hub](https://tehub.org/) | *Mobile DNA* 2021 · [10.1186/s13100-021-00244-0](https://doi.org/10.1186/s13100-021-00244-0) | Travis J. Wheeler, University of Montana | niche · 42 |
| [awesome-transposable-elements](https://github.com/nixonlab/awesome-transposable-elements) | — | — | no paper |
| [gene-structure-annotation TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md) | — | — | no paper |

Related publications in the same line of work (not standalone tools): a survey of plant retrotransposon structure, identification and classification ([10.3390/ijms20153837](https://doi.org/10.3390/ijms20153837)); a systematic survey of machine-learning methods for transposable-element detection and classification ([10.7717/peerj.8311](https://doi.org/10.7717/peerj.8311)); a k-mer machine-learning method to classify plant LTR retrotransposons ([10.7717/peerj.11456](https://doi.org/10.7717/peerj.11456)); and a comparison of performance metrics for those tasks ([10.3390/pr8060638](https://doi.org/10.3390/pr8060638)). Companion experiment repositories: [MLinTEs](https://github.com/simonorozcoarias/MLinTEs) and [MachineLearningInTEs](https://github.com/simonorozcoarias/MachineLearningInTEs).

Benchmark papers listed in the old tables (papers, not software tools): Hoen et al. 2015, on systematic benchmarking of transposable-element annotation methods ([10.1186/s13100-015-0044-6](https://doi.org/10.1186/s13100-015-0044-6)); Rishishwar et al. 2016, a benchmark of tools for polymorphic transposable-element detection ([10.1093/bib/bbw072](https://doi.org/10.1093/bib/bbw072)); and Saha et al. 2008, an empirical comparison of ab initio repeat-finding programs ([10.1093/nar/gkn064](https://doi.org/10.1093/nar/gkn064)).

### Practical workflow

1. Run `EDTA` per assembly or haplotype using `--species others --sensitive 1 --anno 1`. Set `--u` explicitly and record its source. A grape value for `--u` is [待确认]; if `--u` is omitted, EDTA silently uses a rice rate of 1.3e-8 /bp/year, which must not be used for grape without stating it explicitly.
2. Run `TEtrimmer` per haplotype, merge the Perfect and Good outputs, and use `CD-HIT` to generate a working library at about 95 percent identity. An optional 80-80 family catalog can also be built, provided it does not overwrite the working library.
3. Run `TEsorter` with a resource such as `rexdb-plant` to assign domains and labels only. Never replace the working FASTA with `all.cls.lib`.
4. Apply a curation gate using CDS BLAST and TEsorter class-emit rules to produce a trusted FASTA and record its sha256.
5. Run soft-masking or EDTA `--curatedlib` with the trusted file only.
6. Run `panEDTA` to combine panel results formally rather than concatenating TE libraries, then reannotate the panel.
7. Calculate LTR age, LAI and PAV only after curated pan TE GFFs are generated.

| Product | Use as `--curatedlib` / gene soft-mask? |
|---------|----------------------------------------|
| Raw EDTA TElib | No |
| Working lib (post-TEtrimmer CD-HIT) | No (whole file) |
| Trusted gated lib | Yes |
| `cat` + CD-HIT of many libs | No (dedup is not curation) |

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --u RATE --threads 32
```

- Do not treat raw EDTA output as a gold-standard TE library.
- Do not treat `cat` and CD-HIT output as `--curatedlib`.
- Classifier-only tools name consensi; they do not replace trimmers and do not become the library itself.
- Do not hard-mask for BRAKER or GALBA. Soft-mask with a trusted library that has been purged of host genes.
- Non-TE repeats such as TRF, telomeres and rDNA do not belong in `--curatedlib`.

### Example scripts

Toy demonstrations that run with Python 3 and numpy are in [`scripts/`](scripts/). They use a planted LTR-like insertion rather than real *Vitis* data. See [`scripts/README.md`](scripts/README.md) and [`testdata/README.md`](testdata/README.md). Worked examples are in [`testdata/EXAMPLES.md`](testdata/EXAMPLES.md).

| Script | Role | Tested? |
|--------|------|---------|
| `00_make_tiny_genome.py` | Write a tiny FASTA and BED with one planted LTR-like insertion | Yes, 2026-11-15 CST |
| `01_ltr_insertion_age.py` | p-distance and K2P between the two LTRs; years only with `--rate` (no default); T = K/(2r) | Yes, 2026-11-15 CST (without `--rate`) |
| `02_softmask.py` | Lowercase BED intervals (soft-mask demonstration) | Yes, 2026-11-15 CST |
| `03_run_edta.sh` | Documents the EDTA command used above | No (`--dry-run` / `--help` only) |
| `04_run_repeatmodeler_repeatmasker.sh` | Documents RepeatModeler2 + RepeatMasker `-xsmall` | No (`--dry-run` / `--help` only) |
| `05_run_tesorter.sh` | Documents TEsorter with rexdb-plant and the all.cls.lib rule | No (`--dry-run` / `--help` only) |
| `run_toy_pipeline.sh` | Runs the three tested Python scripts | Yes, 2026-11-15 CST |

```bash
bash scripts/run_toy_pipeline.sh OUTDIR
```

DOI title-match checks are in [`DOI_CHECKS.tsv`](DOI_CHECKS.tsv), with a short note in [`DOI_CHECKS.NOTES.md`](DOI_CHECKS.NOTES.md). Sources opened for catalogue claims are in [`SOURCES_READ.tsv`](SOURCES_READ.tsv). The change log is [`CHANGELOG.md`](CHANGELOG.md).

Author: Xuzhen Li, [ORCID](https://orcid.org/0000-0003-3670-6657)

