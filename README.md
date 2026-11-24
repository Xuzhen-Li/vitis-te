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

A separate line of plant LTR-retrotransposon software, not part of the default EDTA route, is the Inpactor series: [Inpactor](https://github.com/simonorozcoarias/Inpactor) and [Inpactor2](https://github.com/simonorozcoarias/Inpactor2) classify intact LTR retrotransposons (Inpactor2 also detects them and assigns lineages), [InpactorDB](https://inpactordb.github.io) is a lineage-level plant LTR reference set, [SENMAP](https://github.com/simonorozcoarias/SENMAP) keeps intact LTR copies when curating a library, and [TIP_finder](https://github.com/simonorozcoarias/TIP_finder) calls insertion polymorphisms from short paired reads. Title-matched DOIs and repository links are listed below and in [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv).

### Software by step

| Step | Use when | Tools in this catalogue |
|------|----------|-------------------------|
| De novo discovery | Starting from an assembly or haplotype | [EDTA](https://github.com/oushujun/EDTA) (default here), [RepeatModeler2](https://github.com/Dfam-consortium/RepeatModeler), [Earl Grey](https://github.com/TobyBaril/EarlGrey); family finders [RepeatScout](https://github.com/Dfam-consortium/RepeatScout), [RECON](https://github.com/Dfam-consortium/RECON), [PILER](https://www.drive5.com/piler/) |
| Structural detection | Seeking intact LTR, TIR, MITE or Helitron copies | [LTR_FINDER](https://github.com/xzhub/LTR_FINDER), [LTR_FINDER_parallel](https://github.com/oushujun/LTR_FINDER_parallel), [LTRharvest](https://github.com/genometools/genometools), [LTR_retriever](https://github.com/oushujun/LTR_retriever); [HelitronScanner](https://sourceforge.net/projects/helitronscanner/); MITE-Hunter, [detectMITE](https://sourceforge.net/projects/detectmite/), [TIR-Learner](https://github.com/oushujun/TIR-Learner), [GRF](https://github.com/bioinfolabmu/GenericRepeatFinder), [Inpactor2](https://github.com/simonorozcoarias/Inpactor2) |
| Homology | Annotating or masking with a library | [RepeatMasker](https://github.com/Dfam-consortium/RepeatMasker) ([website](https://www.repeatmasker.org/)); libraries [Dfam](https://www.dfam.org/) and [Repbase](https://www.girinst.org/repbase/) |
| Classification | Labelling a working library | [TEsorter](https://github.com/zhangrengang/TEsorter) + [REXdb](https://bitbucket.org/petrnovak/repex_tarean) (plant LTR lineages); [DeepTE](https://github.com/LiLabAtVT/DeepTE); [TEclass](https://bioinformatics.uni-muenster.de/tools/teclass/index.hbi); [Inpactor](https://github.com/simonorozcoarias/Inpactor), [Inpactor2](https://github.com/simonorozcoarias/Inpactor2) |
| Curation and consensus | Turning raw consensi into a working or trusted library | [TEtrimmer](https://github.com/qjiangzhao/TEtrimmer) (default here), [MCHelper](https://github.com/GonzalezLab/MCHelper), [SENMAP](https://github.com/simonorozcoarias/SENMAP), Goubert guide ([doi:10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7)), [CD-HIT](https://github.com/weizhongli/cdhit) |
| Library QC | Removing non-TE repeats and checking assembly quality | [TRF](https://github.com/Benson-Genomics-Lab/TRF) (non-TE track; [website](https://tandem.bu.edu/trf/trf.html)); LAI after curated or pan annotation ([LTR_retriever](https://github.com/oushujun/LTR_retriever)) |
| Masking | Handing a genome to gene annotation | [RepeatMasker](https://github.com/Dfam-consortium/RepeatMasker) `-xsmall` with the trusted library only; [BEDTools](https://github.com/arq5x/bedtools2) for track checks |
| TE age / insertion time | Intact LTR pairs after curation | [LTR_retriever](https://github.com/oushujun/LTR_retriever); `scripts/01_ltr_insertion_age.py` for a toy demonstration |
| Polymorphic TE calling | Population or long-read insertion calling, not library construction | [TEMP](https://github.com/JialiUMassWengLab/TEMP), [RelocaTE2](https://github.com/JinfengChen/RelocaTE2), [xTea](https://github.com/parklab/xTea), [Jitterbug](https://github.com/elzbth/jitterbug), [TIP_finder](https://github.com/simonorozcoarias/TIP_finder) |
| Pangenome TE | A panel of haplotypes or genomes | [panEDTA](https://github.com/oushujun/EDTA) (`panEDTA.sh` in the EDTA repository) |
| Visualization / defragmentation | Cleaning homology annotations | [RepeatCraft](https://github.com/niccw/repeatcraftp), [oneCodeToFindThemAll](https://doua.prabi.fr/software/one-code-to-find-them-all) |

### Inpactor series (plant LTR retrotransposons)

These entries are an alternative or complement to the default EDTA route. They are not a replacement for a CDS-gated trusted library.

| Name | Role | Repository | DOI |
|------|------|------------|-----|
| Inpactor | HPC pipeline to classify plant LTR retrotransposons, mark autonomous and non-autonomous copies, and estimate insertion time | [github.com/simonorozcoarias/Inpactor](https://github.com/simonorozcoarias/Inpactor) | [10.3390/biology7020032](https://doi.org/10.3390/biology7020032) |
| Inpactor2 | Deep-learning and structure-based detection, filtering of fragments and nested copies, and classification of intact plant LTR retrotransposons to superfamily and lineage; input is an assembled genome | [github.com/simonorozcoarias/Inpactor2](https://github.com/simonorozcoarias/Inpactor2) | [10.1093/bib/bbac511](https://doi.org/10.1093/bib/bbac511) |
| InpactorDB | Lineage-level plant LTR retrotransposon reference set (195 genomes, 108 species; 67,241 non-redundant elements in the published set) | [InpactorDB search page](https://inpactordb.github.io); dataset [10.5281/zenodo.4386317](https://doi.org/10.5281/zenodo.4386317) (a later snapshot is [10.5281/zenodo.5816833](https://doi.org/10.5281/zenodo.5816833)) | [10.3390/genes12020190](https://doi.org/10.3390/genes12020190) |
| SENMAP | Convolutional network to keep intact LTR retrotransposon copies when curating a plant library | [github.com/simonorozcoarias/SENMAP](https://github.com/simonorozcoarias/SENMAP) | [10.1515/jib-2021-0036](https://doi.org/10.1515/jib-2021-0036) (journal article; conference report: [10.1109/ci-ibbi54220.2021.9626130](https://doi.org/10.1109/ci-ibbi54220.2021.9626130)) |
| TIP_finder | HPC caller of transposable-element insertion polymorphisms from Illumina paired reads, a chromosome-level reference, and a TE consensus set | [github.com/simonorozcoarias/TIP_finder](https://github.com/simonorozcoarias/TIP_finder) | [10.3390/biology9090281](https://doi.org/10.3390/biology9090281) |
| YORO | Convolutional genomic-object detector for transposable-element detection and classification | [github.com/simonorozcoarias/YORO](https://github.com/simonorozcoarias/YORO) | [10.1371/journal.pone.0291925](https://doi.org/10.1371/journal.pone.0291925) |
| PanTEon | Cross-kingdom framework and database for designing and comparing transposable-element classifiers (preprint) | [github.com/simonorozcoarias/PanTEon](https://github.com/simonorozcoarias/PanTEon) | [10.64898/2026.04.01.715927](https://doi.org/10.64898/2026.04.01.715927) |

Related publications in the same line of work (not standalone tools): a survey of plant retrotransposon structure, identification and classification ([10.3390/ijms20153837](https://doi.org/10.3390/ijms20153837)); a systematic survey of machine-learning methods for transposable-element detection and classification ([10.7717/peerj.8311](https://doi.org/10.7717/peerj.8311)); a k-mer machine-learning method to classify plant LTR retrotransposons ([10.7717/peerj.11456](https://doi.org/10.7717/peerj.11456)); and a comparison of performance metrics for those tasks ([10.3390/pr8060638](https://doi.org/10.3390/pr8060638)). Companion experiment repositories: [MLinTEs](https://github.com/simonorozcoarias/MLinTEs) and [MachineLearningInTEs](https://github.com/simonorozcoarias/MachineLearningInTEs).

### Additional software and databases by analysis step

These entries supplement the software table above. They do not change the default EDTA, TEtrimmer and TEsorter route. Each row has a paper DOI that was opened, or an official code or data site that returned a successful response. Candidates without a verifiable source were left out.

| Step | Name | Role | Repository or site | DOI |
|------|------|------|-------------------|-----|
| De novo detection (including LTR, TIR, MITE, Helitron, LINE/SINE, and read-based discovery) | **RepeatExplorer2** | Graph-based clustering of short reads to identify and quantify repetitive DNA without a genome assembly, with a Galaxy interface. | [repeatexplorer-elixir.cerit-sc.cz](https://repeatexplorer-elixir.cerit-sc.cz) | [10.1038/s41596-020-0400-y](https://doi.org/10.1038/s41596-020-0400-y) |
|  | **dnaPipeTE** | Assembles, annotates and quantifies transposable elements from low-coverage raw short reads, without a genome assembly. | [github.com/clemgoub/dnaPipeTE](https://github.com/clemgoub/dnaPipeTE) | [10.1093/gbe/evv050](https://doi.org/10.1093/gbe/evv050) |
|  | **REPET** | Package containing the TEdenovo and TEannot pipelines for de novo detection, clustering and annotation of transposable-element families in assembled genomes. | [urgi.versailles.inrae.fr/Tools/REPET](https://urgi.versailles.inrae.fr/Tools/REPET) | [10.1371/journal.pone.0016526](https://doi.org/10.1371/journal.pone.0016526) |
|  | **EAHelitron** | Structural Helitron annotator that uses conserved terminal motifs and a GC-rich hairpin. The paper abstract names the software EAHelitron. | [github.com/dontkme/EAHelitron](https://github.com/dontkme/EAHelitron) | [10.1186/s12859-019-2945-8](https://doi.org/10.1186/s12859-019-2945-8) |
|  | **MITE Tracker** | Finds and classifies MITEs in large genomes by nearby inverted repeats, family clustering and flanking-sequence filters. | [github.com/INTABiotechMJ/MITE-Tracker](https://github.com/INTABiotechMJ/MITE-Tracker) | [10.1186/s12859-018-2376-y](https://doi.org/10.1186/s12859-018-2376-y) |
|  | **miteFinderII** | Identifies MITEs hidden in eukaryotic genomes. The live repository redirects from screamer/miteFinder to jhu99/miteFinder. | [github.com/jhu99/miteFinder](https://github.com/jhu99/miteFinder) | [10.1186/s12920-018-0418-y](https://doi.org/10.1186/s12920-018-0418-y) |
|  | **AnnoSINE** | SINE annotation tool for plant genomes that combines homology and structure, then filters false positives to build a SINE library. | [github.com/yangli557/AnnoSINE](https://github.com/yangli557/AnnoSINE) | [10.1093/plphys/kiab524](https://doi.org/10.1093/plphys/kiab524) |
|  | **AnnoSINE_v2** | Faster successor for de novo SINE annotation in plant and animal genomes (preprint). | [github.com/oushujun/AnnoSINE_v2](https://github.com/oushujun/AnnoSINE_v2) | [10.1101/2024.03.01.582874](https://doi.org/10.1101/2024.03.01.582874) |
|  | **SINE_Scan** | Discovers SINE families in large genomic data sets. | [github.com/maohlzj/SINE_Scan](https://github.com/maohlzj/SINE_Scan) | [10.1093/bioinformatics/btw718](https://doi.org/10.1093/bioinformatics/btw718) |
|  | **SINE-Finder** | Tool named in the paper for targeted discovery of tRNA-derived SINEs in plant genomes. No live official code repository was confirmed in this pass. | — | [10.1105/tpc.111.088682](https://doi.org/10.1105/tpc.111.088682) |
|  | **LtrDetector** | De novo detector of LTR retrotransposons. The live repository redirects from TulsaBioinformaticsToolsmith/LtrDetector. | [github.com/BioinformaticsToolsmith/LtrDetector](https://github.com/BioinformaticsToolsmith/LtrDetector) | [10.1186/s12864-019-5796-9](https://doi.org/10.1186/s12864-019-5796-9) |
|  | **MUSTv2** | Improved de novo detector of recently active MITEs. No live official code repository was confirmed in this pass. | — | [10.1515/jib-2017-0029](https://doi.org/10.1515/jib-2017-0029) |
|  | **LTRdigest** | Annotates protein domains, primer-binding sites and polypurine tracts of putative LTR retrotransposons. Distributed with GenomeTools, the same package as LTRharvest. | [github.com/genometools/genometools](https://github.com/genometools/genometools) | [10.1093/nar/gkp759](https://doi.org/10.1093/nar/gkp759) |
|  | **LTRpred** | R package for de novo annotation of intact LTR retrotransposons. The live repository redirects from HajkD/LTRpred to drostlab/LTRpred. | [github.com/drostlab/LTRpred](https://github.com/drostlab/LTRpred) | [10.21105/joss.02170](https://doi.org/10.21105/joss.02170) |
|  | **MGEScan** | Galaxy-based system, described in the official README, for identifying LTR and non-LTR retrotransposons. | [github.com/MGEScan/mgescan](https://github.com/MGEScan/mgescan) | — |
|  | **Red** | Library-free de novo detector of repetitive DNA on a genomic scale. | [github.com/BioinformaticsToolsmith/Red](https://github.com/BioinformaticsToolsmith/Red) | [10.1186/s12859-015-0654-5](https://doi.org/10.1186/s12859-015-0654-5) |
|  | **EDTA-GUI** | Graphical, plant-oriented implementation of the EDTA pipeline, with lineage-level classification. No official code repository was confirmed in this pass. | — | [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) |
|  | **Tephra** | Command-line pipeline to discover transposable-element families from a genome assembly and describe their structure and evolution, without requiring a reference library. The official citation on the README is the repository itself; no title-matched journal article was used. | [github.com/sestaton/tephra](https://github.com/sestaton/tephra) | — |
|  | **Transposome** | Annotates transposable-element families from unassembled paired-end whole-genome shotgun reads. | [github.com/sestaton/Transposome](https://github.com/sestaton/Transposome) | [10.1093/bioinformatics/btv059](https://doi.org/10.1093/bioinformatics/btv059) |
|  | **CARP** | Comprehensive ab initio Repeat Pipeline for identifying, clustering and annotating transposable elements and segmental duplications from genome assemblies. No official code repository returned HTTP 200 in this pass. | — | [10.1371/journal.pone.0193588](https://doi.org/10.1371/journal.pone.0193588) |
|  | **MegaLTR** | Web server and standalone pipeline for detecting intact LTR retrotransposons and calculating the LTR Assembly Index in plant genomes. The companion web server did not respond successfully in this pass; the GitHub repository did. | [github.com/MoradMMokhtar/MegaLTR](https://github.com/MoradMMokhtar/MegaLTR) | [10.3389/fpls.2023.1237426](https://doi.org/10.3389/fpls.2023.1237426) |
|  | **TE-greedy-nester** | Structure-based detection of LTR retrotransposons and reconstruction of their nesting order. | [gitlab.fi.muni.cz/lexa/nested](https://gitlab.fi.muni.cz/lexa/nested) | [10.1093/bioinformatics/btaa632](https://doi.org/10.1093/bioinformatics/btaa632) |
|  | **PhyLTR** | Pipeline for phylogenetic analysis of LTR retrotransposons, as described in the official README. A Zenodo software record was confirmed; no separately title-matched journal article was used. | [github.com/mcsimenc/PhyLTR](https://github.com/mcsimenc/PhyLTR) | [10.5281/zenodo.4256534](https://doi.org/10.5281/zenodo.4256534) |
|  | **TAREAN** | Computational tool for identification and characterization of satellite DNA from unassembled short reads. It is available through the RepeatExplorer Galaxy service. RepeatExplorer2 itself is already listed separately. | [repeatexplorer-elixir.cerit-sc.cz/galaxy/](https://repeatexplorer-elixir.cerit-sc.cz/galaxy/) | [10.1093/nar/gkx257](https://doi.org/10.1093/nar/gkx257) |
|  | **CLARI-TE** | Script for transposable-element annotation in complex genomes such as wheat, as described in the official README. No title-matched journal article was confirmed in this pass. | [github.com/jdaron/CLARI-TE](https://github.com/jdaron/CLARI-TE) | — |
|  | **Dfam TETools** | Container that provides a working RepeatMasker and RepeatModeler installation maintained by the Dfam consortium. It packages tools already listed in this catalogue; it is not a new annotator. | [github.com/Dfam-consortium/TETools](https://github.com/Dfam-consortium/TETools) | — |
|  | **PanTE** | Pan-genome transposable-element annotation pipeline that combines complementary de novo tracks into a classified library, as described in the official README and in the title-matched preprint. | [github.com/unavailable-2374/Pan_TE](https://github.com/unavailable-2374/Pan_TE) | [10.21203/rs.3.rs-5867196/v1](https://doi.org/10.21203/rs.3.rs-5867196/v1) |
|  | **ParTEA** | Earl Grey pangenome pipeline (ParTEA) for consistent transposable-element annotation across many genomes. Earl Grey itself is already listed separately. | [github.com/TobyBaril/EarlGreyParTEA](https://github.com/TobyBaril/EarlGreyParTEA) | [10.64898/2026.11.04.764261](https://doi.org/10.64898/2026.11.04.764261) |
|  | **MAKER-P** | Plant gene-annotation toolkit, not a transposable-element annotator. It can use repeat libraries when annotating plant genomes. No official MAKER-P page returned HTTP 200 in this pass; the general MAKER repository was not treated as a MAKER-P homepage. | — | [10.1104/pp.113.230144](https://doi.org/10.1104/pp.113.230144) |
| Library building, curation and redundancy reduction | **VSEARCH** | General-purpose open-source tool for sequence clustering and dereplication; sometimes used to reduce redundancy in a TE library. It is not a TE annotator. | [github.com/torognes/vsearch](https://github.com/torognes/vsearch) | [10.7717/peerj.2584](https://doi.org/10.7717/peerj.2584) |
|  | **MMseqs2** | General-purpose sequence search and clustering suite; sometimes used for large TE-family clustering. It is not a TE annotator. | [github.com/soedinglab/MMseqs2](https://github.com/soedinglab/MMseqs2) | [10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) |
|  | **TE-Aid** | Helper that draws coverage, divergence, self-dotplot and ORF panels to support manual consensus curation. Presented in the beginner curation guide already listed as a paper in this catalogue. | [github.com/clemgoub/TE-Aid](https://github.com/clemgoub/TE-Aid) | [10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7) |
| Classification (including deep learning) | **NeuralTE** | Deep-learning classifier of transposable-element superfamilies using multiple sequence features. | [github.com/CSU-KangHu/NeuralTE](https://github.com/CSU-KangHu/NeuralTE) | [10.1145/3698587.3701346](https://doi.org/10.1145/3698587.3701346) |
|  | **TERL** | Convolutional-network classifier of transposable elements from raw sequences. | [github.com/muriloHoracio/TERL](https://github.com/muriloHoracio/TERL) | [10.1093/bib/bbaa185](https://doi.org/10.1093/bib/bbaa185) |
|  | **ClassifyTE** | Stacking-based hierarchical classifier of transposable elements. | [github.com/manisa/ClassifyTE](https://github.com/manisa/ClassifyTE) | [10.1093/bioinformatics/btab146](https://doi.org/10.1093/bioinformatics/btab146) |
|  | **PASTEC** | Automatic classifier of transposable elements to the order level, distributed as a REPET module or standalone program. | [urgi.versailles.inrae.fr/Tools/REPET](https://urgi.versailles.inrae.fr/Tools/REPET) | [10.1371/journal.pone.0091929](https://doi.org/10.1371/journal.pone.0091929) |
| Insertion polymorphism (short-read, long-read and related callers) | **McClintock 2** | Meta-pipeline that installs and runs multiple short-read transposable-element insertion detectors and includes a simulation framework. | [github.com/bergmanlab/mcclintock](https://github.com/bergmanlab/mcclintock) | [10.1186/s13100-023-00296-4](https://doi.org/10.1186/s13100-023-00296-4) |
|  | **TEMP2** | Detects germline transposon insertions from short reads and can estimate frequencies of de novo singleton insertions. Already listed in appendix B. | [github.com/weng-lab/TEMP2](https://github.com/weng-lab/TEMP2) | [10.1093/nar/gkab010](https://doi.org/10.1093/nar/gkab010) |
|  | **MELT** | Population-scale mobile-element insertion discovery from short-read data. Already listed in appendix B. | [melt.igs.umaryland.edu](https://melt.igs.umaryland.edu) | [10.1101/gr.218032.116](https://doi.org/10.1101/gr.218032.116) |
|  | **TEPID** | Maps transposable-element insertion diversity in plant populations from short reads. Already listed in appendix B. The official README cites this eLife paper. | [github.com/ListerLab/TEPID](https://github.com/ListerLab/TEPID) | [10.7554/eLife.20777](https://doi.org/10.7554/eLife.20777) |
|  | **PoPoolationTE2** | Compares transposable-element insertion polymorphism from Pool-Seq data. No live official repository was confirmed in this pass. | — | [10.1093/molbev/msw137](https://doi.org/10.1093/molbev/msw137) |
|  | **RetroSeq** | Detects non-reference transposable-element insertions from Illumina paired-end whole-genome sequencing. | [github.com/tk2/RetroSeq](https://github.com/tk2/RetroSeq) | [10.1093/bioinformatics/bts697](https://doi.org/10.1093/bioinformatics/bts697) |
|  | **TEFLoN** | Short-read caller used to discover transposable-element insertions and deletions and to estimate rates. The official README cites this paper; the paper title does not contain the tool name. | [github.com/jradrion/TEFLoN](https://github.com/jradrion/TEFLoN) | [10.1093/gbe/evx050](https://doi.org/10.1093/gbe/evx050) |
|  | **T-lex3** | Genotypes reference transposable-element insertions and estimates population frequencies from short-read data. | [github.com/GonzalezLab/T-lex3](https://github.com/GonzalezLab/T-lex3) | [10.1093/bioinformatics/btz727](https://doi.org/10.1093/bioinformatics/btz727) |
|  | **ngs_te_mapper2** | Detects transposable-element insertions from short-read data, including split-read support. The official README says the method is described in this Genetics paper. | [github.com/bergmanlab/ngs_te_mapper2](https://github.com/bergmanlab/ngs_te_mapper2) | [10.1093/genetics/iyab113](https://doi.org/10.1093/genetics/iyab113) |
|  | **Mobster** | Detects mobile-element insertions from next-generation sequencing data using discordant pairs and split reads. | [github.com/jyhehir/mobster](https://github.com/jyhehir/mobster) | [10.1186/s13059-014-0488-x](https://doi.org/10.1186/s13059-014-0488-x) |
|  | **TE-locate** | Paired-end short-read tool for locating non-reference transposable-element insertions. No methods DOI was title-matched in this pass. | [sourceforge.net/projects/te-locate](https://sourceforge.net/projects/te-locate/) | — |
|  | **TRACKPOSON** | Pipeline, described in its official README, for detecting transposable-element insertion polymorphisms and building a presence-absence matrix. | [github.com/Markestine/TRACKPOSON](https://github.com/Markestine/TRACKPOSON) | — |
|  | **TrEMOLO** | Estimates transposable-element allele frequencies from long-read data by combining assembly and mapping. | [github.com/DrosophilaGenomeEvolution/TrEMOLO](https://github.com/DrosophilaGenomeEvolution/TrEMOLO) | [10.1186/s13059-023-02911-2](https://doi.org/10.1186/s13059-023-02911-2) |
|  | **PALMER** | Long-read caller of non-reference mobile-element insertions. The official README cites this paper as the primary methods citation. | [github.com/WeichenZhou/PALMER](https://github.com/WeichenZhou/PALMER) | [10.1093/nar/gkz1173](https://doi.org/10.1093/nar/gkz1173) |
|  | **LoRTE** | Detects transposon-induced variants from low-coverage PacBio long reads. No official code repository returned HTTP 200 in this pass. | — | [10.1186/s13100-017-0088-x](https://doi.org/10.1186/s13100-017-0088-x) |
|  | **rMETL** | Detects mobile-element insertions from long reads by realignment. | [github.com/tjiangHIT/rMETL](https://github.com/tjiangHIT/rMETL) | [10.1093/bioinformatics/btz106](https://doi.org/10.1093/bioinformatics/btz106) |
|  | **sTELLeR** | Fast caller of transposable-element insertions from long-read genomes, with VCF output. | [github.com/kristinebilgrav/sTELLeR](https://github.com/kristinebilgrav/sTELLeR) | [10.1093/bioinformatics/btae686](https://doi.org/10.1093/bioinformatics/btae686) |
|  | **TELR** | Detects non-reference transposable-element insertions from long reads, with local assembly of insertion sequences. The official README cites this paper. | [github.com/bergmanlab/telr](https://github.com/bergmanlab/telr) | [10.1093/nar/gkac794](https://doi.org/10.1093/nar/gkac794) |
|  | **somrit** | Toolkit for identifying and analysing somatic retrotransposon insertions from long reads. | [github.com/adcosta17/somrit](https://github.com/adcosta17/somrit) | [10.1101/2023.08.06.552193](https://doi.org/10.1101/2023.08.06.552193) |
|  | **SVAN** | Annotates and classifies sequence-resolved insertions and deletions, including mobile-element insertions, as described in the official README. No title-matched methods DOI was attached in this pass. | [github.com/REPBIO-LAB/SVAN](https://github.com/REPBIO-LAB/SVAN) | — |
|  | **MEIGA-PAV** | Annotates mobile-element insertions in a VCF of sequence-resolved structural-variant calls, as described in the official README. | [github.com/MEIGA-tk/MEIGA-PAV](https://github.com/MEIGA-tk/MEIGA-PAV) | — |
|  | **panREPET** | Reference-free pipeline for detecting transposable-element insertions shared across a pan-genome, so their dynamics can be retraced within a species. | [forgemia.inra.fr/urgi-anagen/panREPET](https://forgemia.inra.fr/urgi-anagen/panREPET) | [10.1186/s13059-026-03984-5](https://doi.org/10.1186/s13059-026-03984-5) |
|  | **pantera** | Identifies transposable-element families from polymorphisms stored in a pangenome variation graph. | [github.com/piosierra/pantera](https://github.com/piosierra/pantera) | [10.1186/s13100-024-00323-y](https://doi.org/10.1186/s13100-024-00323-y) |
|  | **Pannagram** | Pangenome alignment and mobilome calling, as described in the title-matched preprint and the official README. General pangenome machinery; not only a transposable-element annotator. | [github.com/iganna/pannagram](https://github.com/iganna/pannagram) | [10.1101/2025.02.07.637071](https://doi.org/10.1101/2025.02.07.637071) |
|  | **PanGenie** | Short-read genotyper for variants represented in a pangenome graph. General-purpose; not a transposable-element annotator. | [github.com/eblerjana/pangenie](https://github.com/eblerjana/pangenie) | [10.1038/s41588-022-01043-w](https://doi.org/10.1038/s41588-022-01043-w) |
|  | **Paragraph** | Graph-based structural-variant genotyper for short-read data. General-purpose; not a transposable-element annotator. The published DOI was used. | [github.com/Illumina/paragraph](https://github.com/Illumina/paragraph) | [10.1186/s13059-019-1909-7](https://doi.org/10.1186/s13059-019-1909-7) |
|  | **SyRI** | Finds syntenic and rearranged regions, and local sequence differences, from whole-genome assemblies. General-purpose; not a transposable-element annotator. The published DOI was used rather than the preprint. | [github.com/schneebergerlab/syri](https://github.com/schneebergerlab/syri) | [10.1186/s13059-019-1911-0](https://doi.org/10.1186/s13059-019-1911-0) |
|  | **MEGAnE** | Mobile Element Genotyping Analysis Environment: identifies and genotypes polymorphic mobile elements from short-read whole-genome data, as described in the official README. The official README cites this preprint; the preprint title does not use the tool name. | [github.com/shohei-kojima/MEGAnE](https://github.com/shohei-kojima/MEGAnE) | [10.1101/2022.03.25.485726](https://doi.org/10.1101/2022.03.25.485726) |
|  | **TEfinder** | Pipeline for detecting novel transposable-element insertions from discordant reads in paired-end sequencing data. | [github.com/VistaSohrab/TEfinder](https://github.com/VistaSohrab/TEfinder) | [10.3390/genes12020224](https://doi.org/10.3390/genes12020224) |
|  | **ITIS** | Tool for identifying transposon insertion sites from next-generation sequencing data. The published site did not respond successfully in this pass. | — | [10.1186/s12859-015-0507-2](https://doi.org/10.1186/s12859-015-0507-2) |
|  | **TE-Tracker** | Systematic identification of transposition events from whole-genome resequencing. No official code repository was confirmed in this pass. | — | [10.1186/s12859-014-0377-z](https://doi.org/10.1186/s12859-014-0377-z) |
|  | **ELITE** | Efficiently Locating Insertions of Transposable Elements, an ACM methods paper. No official code repository was confirmed in this pass. | — | [10.1145/3307339.3342182](https://doi.org/10.1145/3307339.3342182) |
| Transposable-element expression and small RNA | **TEtranscripts** | Includes gene and transposable-element expression, with multi-mapping reads, in differential expression analysis of bulk RNA-seq. | [github.com/mhammell-laboratory/TEtranscripts](https://github.com/mhammell-laboratory/TEtranscripts) | [10.1093/bioinformatics/btv422](https://doi.org/10.1093/bioinformatics/btv422) |
|  | **TElocal** | Locus-specific quantification of transposable-element expression, from the same laboratory as TEtranscripts. | [github.com/mhammell-laboratory/TElocal](https://github.com/mhammell-laboratory/TElocal) | — |
|  | **Telescope** | Bayesian locus-specific estimation of transposable-element expression from RNA-seq. | [github.com/mlbendall/telescope](https://github.com/mlbendall/telescope) | [10.1371/journal.pcbi.1006453](https://doi.org/10.1371/journal.pcbi.1006453) |
|  | **SQuIRE** | End-to-end RNA-seq workflow for locus-specific quantification of interspersed repeat expression. | [github.com/wyang17/SQuIRE](https://github.com/wyang17/SQuIRE) | [10.1093/nar/gky1301](https://doi.org/10.1093/nar/gky1301) |
|  | **SalmonTE** | Quasi-mapping pipeline, based on Salmon, for quantifying transposable-element expression from RNA-seq. The live repository redirects to jeonglab-bcm/SalmonTE. | [github.com/jeonglab-bcm/SalmonTE](https://github.com/jeonglab-bcm/SalmonTE) | [10.1142/9789813235533_0016](https://doi.org/10.1142/9789813235533_0016) |
|  | **scTE** | Quantifies transposable-element expression from single-cell RNA-seq and related assays, as described in the official README. | [github.com/JiekaiLab/scTE](https://github.com/JiekaiLab/scTE) | — |
|  | **SoloTE** | Locus-specific quantification of transposable-element expression in single-cell RNA-seq. | [github.com/bvaldebenitom/SoloTE](https://github.com/bvaldebenitom/SoloTE) | [10.1038/s42003-022-04020-5](https://doi.org/10.1038/s42003-022-04020-5) |
|  | **TEtools** | Counts and compares transposable-element expression (TEcount and TEdiff), including a Galaxy wrapper. | [github.com/l-modolo/TEtools](https://github.com/l-modolo/TEtools) | [10.1093/nar/gkw953](https://doi.org/10.1093/nar/gkw953) |
|  | **RepEnrich** | Estimates transcriptional enrichment of repetitive-element subfamilies from RNA-seq or ChIP-seq by using uniquely mapping and multi-mapping reads. No official repository was confirmed in this pass. | — | [10.1186/1471-2164-15-583](https://doi.org/10.1186/1471-2164-15-583) |
|  | **ShortStack** | Annotates and quantifies small RNA genes, including multi-mapping 21-24 nt siRNAs often used in plant transposable-element silencing studies. | [github.com/MikeAxtell/ShortStack](https://github.com/MikeAxtell/ShortStack) | [10.1261/rna.035279.112](https://doi.org/10.1261/rna.035279.112) |
|  | **piPipes** | Set of pipelines, described in the official README, for analysing piRNAs and transposon transcripts across several sequencing assays. | [github.com/bowhan/piPipes](https://github.com/bowhan/piPipes) | — |
| Age, divergence and landscape | **ParseRM** | Perl scripts that parse RepeatMasker .out or .align files to summarise composition, divergence and landscape. No standalone methods paper was title-matched in this pass. | [github.com/4ureliek/Parsing-RepeatMasker-Outputs](https://github.com/4ureliek/Parsing-RepeatMasker-Outputs) | — |
|  | **VHICA** | Vertical and Horizontal Inheritance Consistence Analysis: discriminates vertical and horizontal transposon transfer by contrasting transposable-element divergence with that of host genes. | [cran.r-project.org/package=vhica](https://cran.r-project.org/package=vhica) | [10.1093/molbev/msv341](https://doi.org/10.1093/molbev/msv341) |
|  | **REANNOTATE** | Automated paleontology of repetitive DNA, used to reconstruct insertion history. The published site did not respond successfully in this pass. | — | [10.1186/1471-2164-9-614](https://doi.org/10.1186/1471-2164-9-614) |
|  | **RepeatLandscape** | Scripts that parse RepeatMasker alignment output and plot repeat-landscape histograms or charts. No standalone methods paper was title-matched in this pass. | [github.com/caballero/RepeatLandscape](https://github.com/caballero/RepeatLandscape) | — |
|  | **TE_Density** | Calculates transposable-element density in windows relative to genes, for studies of TE-gene spatial biology. | [github.com/sjteresi/TE_Density](https://github.com/sjteresi/TE_Density) | [10.1186/s13100-022-00264-4](https://doi.org/10.1186/s13100-022-00264-4) |
|  | **TEGRiP** | Transposable Elements Genes RelationshIps Pipeline: detects positional and directional relationships between transposable elements and adjacent genes. The official README uses the name TEGRiP. | [github.com/marieBvr/TEs_genes_relationship_pipeline](https://github.com/marieBvr/TEs_genes_relationship_pipeline) | [10.24072/pcjournal.57](https://doi.org/10.24072/pcjournal.57) |
|  | **Repeattools** | Compares transposable-element profiles and copy divergence across species, as described in the official README. The README cites a TEsorter paper; that DOI was not used here. | [github.com/AgustinAmata/Repeattools](https://github.com/AgustinAmata/Repeattools) | — |
| Visualization | **StainedGlass** | Builds interactive identity heatmaps of massive tandem-repeat and other highly repetitive regions. | [github.com/vollgerlab/StainedGlass](https://github.com/vollgerlab/StainedGlass) | [10.1093/bioinformatics/btac018](https://doi.org/10.1093/bioinformatics/btac018) |
|  | **ModDotPlot** | Fast interactive dot-plot viewer for tandem repeats and large repetitive intervals. | [github.com/marbl/ModDotPlot](https://github.com/marbl/ModDotPlot) | [10.1093/bioinformatics/btae493](https://doi.org/10.1093/bioinformatics/btae493) |
|  | **FlexiDot** | Customizable, ambiguity-aware dot plots for visual sequence comparison, including repetitive sequences. General-purpose visualization; not a transposable-element annotator. | [github.com/molbio-dresden/flexidot](https://github.com/molbio-dresden/flexidot) | [10.1093/bioinformatics/bty395](https://doi.org/10.1093/bioinformatics/bty395) |
|  | **RepeatOBserver** | Visualises tandem repeats and can highlight putative centromeres. Focused on tandem repeats rather than transposable-element annotation. | [github.com/celphin/RepeatOBserverV1](https://github.com/celphin/RepeatOBserverV1) | [10.1111/1755-0998.14084](https://doi.org/10.1111/1755-0998.14084) |
|  | **LTRsift** | Graphical interface for semi-automatic classification and post-processing of de novo detected LTR retrotransposons. | [github.com/satta/ltrsift](https://github.com/satta/ltrsift) | [10.1186/1759-8753-3-18](https://doi.org/10.1186/1759-8753-3-18) |
|  | **plotsr** | Visualizes structural similarities and rearrangements between multiple genome assemblies. General-purpose; not a transposable-element annotator. | [github.com/schneebergerlab/plotsr](https://github.com/schneebergerlab/plotsr) | [10.1093/bioinformatics/btac196](https://doi.org/10.1093/bioinformatics/btac196) |
| Simulation and benchmarking | **simuG** | General-purpose genome simulator that can introduce SNPs, indels, structural variants and transposable-element insertions for method testing. | [github.com/yjx1217/simuG](https://github.com/yjx1217/simuG) | [10.1093/bioinformatics/btz424](https://doi.org/10.1093/bioinformatics/btz424) |
|  | **TEgenomeSimulator** | Framework for simulating genomes with configurable transposable-element landscapes, for method testing. | [github.com/Plant-Food-Research-Open/TEgenomeSimulator](https://github.com/Plant-Food-Research-Open/TEgenomeSimulator) | [10.64898/2026.03.09.710711](https://doi.org/10.64898/2026.03.09.710711) |
|  | **PrinTE** | Forward simulation framework for studying how transposable elements contribute to genome expansion and contraction. | [github.com/cwb14/PrinTE](https://github.com/cwb14/PrinTE) | [10.1101/2025.06.04.657780](https://doi.org/10.1101/2025.06.04.657780) |
|  | **TEvarSim** | Genome simulator for transposable-element insertions and deletions, including simulated short-read and long-read data. | [github.com/daweili-lab/TEvarSim](https://github.com/daweili-lab/TEvarSim) | [10.1371/journal.pcbi.1013933](https://doi.org/10.1371/journal.pcbi.1013933) |
|  | **TE_simu** | Scripts for simulating insertion, amplification and evolution of transposable elements in genomic sequences, as described in the official README. No title-matched methods paper was attached in this pass. | [github.com/unavailable-2374/TE_simu](https://github.com/unavailable-2374/TE_simu) | — |
|  | **Hoen et al. 2015** | Methods paper calling for systematic benchmarking of transposable-element annotation methods. It is a paper, not a software tool. | — | [10.1186/s13100-015-0044-6](https://doi.org/10.1186/s13100-015-0044-6) |
|  | **Rishishwar et al. 2016** | Benchmark of computational tools for polymorphic transposable-element detection. It is a paper, not a software tool. | — | [10.1093/bib/bbw072](https://doi.org/10.1093/bib/bbw072) |
|  | **Saha et al. 2008** | Empirical comparison of ab initio repeat-finding programs. It is a paper, not a software tool. | — | [10.1093/nar/gkn064](https://doi.org/10.1093/nar/gkn064) |
| Polyploid subgenomes and tandem repeats | **TRASH** | Tandem Repeat Annotation and Structural Hierarchy: annotates tandem repeats, including satellite arrays. Not a transposable-element annotator. | [github.com/vlothec/TRASH](https://github.com/vlothec/TRASH) | [10.1093/bioinformatics/btad308](https://doi.org/10.1093/bioinformatics/btad308) |
|  | **SubPhaser** | Phases allopolyploid subgenomes using subgenome-specific k-mers, mainly from repetitive sequences such as transposable elements. Not a transposable-element annotator. | [github.com/zhangrengang/SubPhaser](https://github.com/zhangrengang/SubPhaser) | [10.1111/nph.18173](https://doi.org/10.1111/nph.18173) |
|  | **PolyCRACKER** | Unsupervised partitioning of polyploid subgenomes by signatures of repetitive-DNA evolution. An unofficial code mirror was seen and was not used as the official repository. | — | [10.1186/s12864-019-5828-5](https://doi.org/10.1186/s12864-019-5828-5) |
| Databases and reference sets | **PlantRep** | Database of plant repetitive-element consensus sequences re-annotated across hundreds of plant genomes. The public website did not respond successfully in this pass. | — | [10.1007/s00299-021-02817-y](https://doi.org/10.1007/s00299-021-02817-y) |
|  | **RiTE-db** | Resource database of Oryza transposable elements. The live page redirects from the older genome.arizona.edu address. | [ava.genome.arizona.edu/cgi-bin/rite/index.cgi](https://ava.genome.arizona.edu/cgi-bin/rite/index.cgi) | [10.1186/s12864-015-1762-3](https://doi.org/10.1186/s12864-015-1762-3) |
|  | **SINEBase** | Database and tool for SINE consensus sequences and structural analysis across eukaryotes. | [sines.eimb.ru](https://sines.eimb.ru/) | [10.1093/nar/gks1263](https://doi.org/10.1093/nar/gks1263) |
|  | **SoyTEdb** | Database of transposable elements in the soybean genome. The published hostname now redirects to this SoyBase legacy page. | [legacy.soybase.org/soytedb](https://legacy.soybase.org/soytedb/) | [10.1186/1471-2164-11-113](https://doi.org/10.1186/1471-2164-11-113) |
|  | **RepetDB** | Unified resource for transposable-element reference sequences associated with the REPET project. | [urgi.versailles.inrae.fr/repetdb](https://urgi.versailles.inrae.fr/repetdb) | [10.1186/s13100-019-0150-y](https://doi.org/10.1186/s13100-019-0150-y) |
|  | **TREP** | Plant-oriented curated transposable-element platform already listed in appendix B; added here so the methods catalogue has a matching resource row. | [trep-db.uzh.ch](https://trep-db.uzh.ch) | — |
|  | **HTT-DB** | Database of horizontally transferred transposable elements, with a later update paper. Public sites tried in this pass did not respond successfully. | — | [10.1093/bioinformatics/btv281](https://doi.org/10.1093/bioinformatics/btv281) |
|  | **PlantLTRdb** | Interactive database of intact LTR retrotransposons across 195 plant species. | [bioinformatics.um6p.ma/PlantLTRdb/](https://bioinformatics.um6p.ma/PlantLTRdb/) | [10.3389/fpls.2023.1134627](https://doi.org/10.3389/fpls.2023.1134627) |
|  | **DPTEdb** | Integrative database of transposable elements in dioecious plants. The published site did not respond successfully in this pass. | — | [10.1093/database/baw078](https://doi.org/10.1093/database/baw078) |
|  | **SPTEdb** | Database of transposable elements in salicaceous plants. The published site did not respond successfully in this pass. | — | [10.1093/database/bay024](https://doi.org/10.1093/database/bay024) |
|  | **RetrOryza** | Database of rice LTR retrotransposons. Public sites tried in this pass did not respond successfully. | — | [10.1093/nar/gkl780](https://doi.org/10.1093/nar/gkl780) |
|  | **TIGR Plant Repeat Databases** | Historical collective resource for identifying repetitive sequences in plants. The original TIGR URL did not respond successfully in this pass. | — | [10.1093/nar/gkh099](https://doi.org/10.1093/nar/gkh099) |
|  | **ConTEdb** | Comprehensive database of transposable elements in conifers. Public sites tried in this pass did not respond successfully. | — | [10.1093/database/bay131](https://doi.org/10.1093/database/bay131) |
|  | **AnnoTEP-DB** | Documentation and pre-processed genome resource associated with the EDTA-GUI paper. The software row for EDTA-GUI is already in this catalogue and was not edited. The live address requires a trailing slash. | [plantgenomics.ncc.unesp.br/AnnoTEP-DB/](https://plantgenomics.ncc.unesp.br/AnnoTEP-DB/) | [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) |
|  | **MaizeGP** | Open graph-based maize pangenome platform, including a structural-variant catalogue. It is a species pangenome resource, not a transposable-element-only database. | [github.com/Jia-nianhua/Maize-Graph-Pangenome](https://github.com/Jia-nianhua/Maize-Graph-Pangenome) | [10.1111/jipb.70439](https://doi.org/10.1111/jipb.70439) |
|  | **TE Hub** | Community site for sharing and connecting tools, data, resources and methods for transposable-element annotation. | [tehub.org](https://tehub.org/) | [10.1186/s13100-021-00244-0](https://doi.org/10.1186/s13100-021-00244-0) |
|  | **awesome-transposable-elements** | Curated public list of software, databases and other resources for transposable-element research. It is a community index, not a primary database. | [github.com/nixonlab/awesome-transposable-elements](https://github.com/nixonlab/awesome-transposable-elements) | — |

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

