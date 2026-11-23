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

### Software by step

| Step | Use when | Tools in this catalogue |
|------|----------|-------------------------|
| De novo discovery | Starting from an assembly or haplotype | EDTA (default here), RepeatModeler2, Earl Grey; family finders RepeatScout, RECON, PILER |
| Structural detection | Seeking intact LTR, TIR, MITE or Helitron copies | LTR_FINDER, LTR_FINDER_parallel, LTRharvest, LTR_retriever; HelitronScanner; MITE-Hunter, detectMITE, TIR-Learner, GRF |
| Homology | Annotating or masking with a library | RepeatMasker; libraries Dfam and Repbase |
| Classification | Labelling a working library | TEsorter + REXdb (plant LTR lineages); DeepTE; TEclass |
| Curation and consensus | Turning raw consensi into a working or trusted library | TEtrimmer (default here), MCHelper, Goubert guide, CD-HIT |
| Library QC | Removing non-TE repeats and checking assembly quality | TRF (non-TE track); LAI after curated or pan annotation |
| Masking | Handing a genome to gene annotation | RepeatMasker `-xsmall` with the trusted library only; BEDTools for track checks |
| TE age / insertion time | Intact LTR pairs after curation | LTR_retriever; `scripts/01_ltr_insertion_age.py` for a toy demonstration |
| Polymorphic TE calling | Population or long-read insertion calling, not library construction | TEMP, RelocaTE2, xTea, Jitterbug |
| Pangenome TE | A panel of haplotypes or genomes | panEDTA (`panEDTA.sh` in the EDTA repository) |
| Visualization / defragmentation | Cleaning homology annotations | RepeatCraft, oneCodeToFindThemAll |

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

