# vitis-te

[English](README.md) | 中文

本仓库存放一部中文书稿、一份方法目录，以及若干用于葡萄属（*Vitis*）及其他植物转座元件（TE）的小脚本。要了解转座子是什么、如何分类、在葡萄里已知哪些事实，请看书的目录。要看分析怎么做，请看下面的软件、流程和脚本。基因软屏蔽所用的葡萄 TE 文库说明见 [gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)。

基因模型注释由 [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) 负责。功能注释属于 [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation)。PAV 图和较长的图工具列表见 [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome)。本仓库不是其他研究组原始 TE 识别结果的转存。尚未公开出现在 GitHub 上的私有实验草稿和讲义，不复制到这里。

## 书的目录

中文书稿《转座子从发现到实践，以葡萄为例》见 [`book/README.md`](book/README.md)。同一正文的合订本见 [`book/TE_BOOK_full.md`](book/TE_BOOK_full.md)。文件清单见 [`book/INDEX.md`](book/INDEX.md)。凡尚未对照已打开的来源核实的说法或文献，一律标为 [待确认]。

配图合订本（第1至4章、类型详解、第13章、第5至12章与附录）见 [`book/illustrated_v3_p2d/TE_BOOK_illustrated_v3_p2d.md`](book/illustrated_v3_p2d/TE_BOOK_illustrated_v3_p2d.md)。

- [前言](book/chapters/00-preface.md)
  - [编写定位](book/chapters/00-preface.md#编写定位)
  - [全书结构与阅读路径](book/chapters/00-preface.md#全书结构与阅读路径)
  - [术语规范、代码约定与可重复计算原则](book/chapters/00-preface.md#术语规范代码约定与可重复计算原则)
- [第1章 转座子的发现史与核心概念](book/chapters/01-discovery-and-core-concepts.md)
  - [1.1 玉米控制元件的发现与早期争议](book/chapters/01-discovery-and-core-concepts.md#11-玉米控制元件的发现与早期争议)
  - [1.2 从“垃圾DNA”到基因组动态组分：认知范式的演变](book/chapters/01-discovery-and-core-concepts.md#12-从垃圾dna到基因组动态组分认知范式的演变)
  - [1.3 转座子的基本定义、结构特征与宿主基因组背景](book/chapters/01-discovery-and-core-concepts.md#13-转座子的基本定义结构特征与宿主基因组背景)
- [第2章 转座子的分类体系与命名规范](book/chapters/02-classification-and-nomenclature.md)
  - [2.1 分类学的演进：从Finnegan到Wicker与Repbase体系](book/chapters/02-classification-and-nomenclature.md#21-分类学的演进从finnegan到wicker与repbase体系)
  - [2.2 统一分类框架中的层级与边界争议](book/chapters/02-classification-and-nomenclature.md#22-统一分类框架中的层级与边界争议)
  - [2.3 命名规则与公共数据库标准](book/chapters/02-classification-and-nomenclature.md#23-命名规则与公共数据库标准)
- [第3章 Ⅰ类转座子（反转录转座子）的结构与生活史](book/chapters/03-class-I-retrotransposons.md)
  - [3.1 LTR反转录转座子的结构与反转录机制](book/chapters/03-class-I-retrotransposons.md#31-ltr反转录转座子的结构与反转录机制)
  - [3.2 非LTR反转录转座子：LINE与SINE](book/chapters/03-class-I-retrotransposons.md#32-非ltr反转录转座子line与sine)
  - [3.3 DIRS、PLE及其他特殊反转录元件](book/chapters/03-class-I-retrotransposons.md#33-dirsple及其他特殊反转录元件)
- [第4章 Ⅱ类转座子（DNA转座子）的结构与生活史](book/chapters/04-class-II-dna-transposons.md)
  - [4.1 经典“剪切-粘贴”型TIR DNA转座子](book/chapters/04-class-II-dna-transposons.md#41-经典剪切-粘贴型tir-dna转座子)
  - [4.2 MITEs（微型反向重复转座元件）的起源与扩增](book/chapters/04-class-II-dna-transposons.md#42-mites微型反向重复转座元件的起源与扩增)
  - [4.3 Helitron与Maverick/Polinton：滚环复制与自合成元件](book/chapters/04-class-II-dna-transposons.md#43-helitron与maverickpolinton滚环复制与自合成元件)
- [第5章 宿主沉默机制与表观遗传调控](book/chapters/05-host-silencing-and-epigenetics.md)
  - [5.1 植物DNA甲基化与RdDM（RNA导向的DNA甲基化）通路](book/chapters/05-host-silencing-and-epigenetics.md#51-植物dna甲基化与rddmrna导向的dna甲基化通路)
  - [5.2 组蛋白修饰、染色质重塑与异染色质维持](book/chapters/05-host-silencing-and-epigenetics.md#52-组蛋白修饰染色质重塑与异染色质维持)
  - [5.3 转座子的逃逸、胁迫激活与表观遗传重编程](book/chapters/05-host-silencing-and-epigenetics.md#53-转座子的逃逸胁迫激活与表观遗传重编程)
- [第6章 基因组演化与转座子动力学](book/chapters/06-genome-evolution-and-te-dynamics.md)
  - [6.1 转座子爆发、清除与基因组大小演化](book/chapters/06-genome-evolution-and-te-dynamics.md#61-转座子爆发清除与基因组大小演化)
  - [6.2 基因组区室化分布与嵌套插入](book/chapters/06-genome-evolution-and-te-dynamics.md#62-基因组区室化分布与嵌套插入)
  - [6.3 结构变异、基因捕获与功能外适应（Exaptation）](book/chapters/06-genome-evolution-and-te-dynamics.md#63-结构变异基因捕获与功能外适应exaptation)
- [第7章 转座子的检测、从头注释与文库构建](book/chapters/07-detection-annotation-and-libraries.md)
  - [7.1 基于同源与基于结构的从头预测原理](book/chapters/07-detection-annotation-and-libraries.md#71-基于同源与基于结构的从头预测原理)
  - [7.2 整合注释流程与高质量一致性文库构建](book/chapters/07-detection-annotation-and-libraries.md#72-整合注释流程与高质量一致性文库构建)
  - [7.3 注释质量评估与跨基因组/泛基因组注释策略](book/chapters/07-detection-annotation-and-libraries.md#73-注释质量评估与跨基因组泛基因组注释策略)
- [第8章 群体水平的转座子插入多态性（TIPs）分析](book/chapters/08-insertion-polymorphisms-tips.md)
  - [8.1 短读长与长读长测序数据的TIPs检测原理](book/chapters/08-insertion-polymorphisms-tips.md#81-短读长与长读长测序数据的tips检测原理)
  - [8.2 群体遗传学统计量与中性检验在TIPs中的应用](book/chapters/08-insertion-polymorphisms-tips.md#82-群体遗传学统计量与中性检验在tips中的应用)
  - [8.3 TIPs在全基因组关联分析（TE-GWAS）中的应用](book/chapters/08-insertion-polymorphisms-tips.md#83-tips在全基因组关联分析te-gwas中的应用)
- [第9章 转座子、表型变异与作物驯化](book/chapters/09-phenotype-and-domestication.md)
  - [9.1 转座子影响基因表达的分子机制](book/chapters/09-phenotype-and-domestication.md#91-转座子影响基因表达的分子机制)
  - [9.2 模式植物与主要作物中的经典表型案例](book/chapters/09-phenotype-and-domestication.md#92-模式植物与主要作物中的经典表型案例)
  - [9.3 无性繁殖与多年生木本作物中的转座子与体细胞变异](book/chapters/09-phenotype-and-domestication.md#93-无性繁殖与多年生木本作物中的转座子与体细胞变异)
- [第10章 葡萄基因组中的转座子：以葡萄属（*Vitis*）为范例](book/chapters/10-vitis-as-worked-example.md)
  - [10.1 葡萄基因组特征与转座子组成概览](book/chapters/10-vitis-as-worked-example.md#101-葡萄基因组特征与转座子组成概览)
  - [10.2 经典案例：Gret1与葡萄果皮颜色的演化](book/chapters/10-vitis-as-worked-example.md#102-经典案例gret1与葡萄果皮颜色的演化)
  - [10.3 葡萄无性系变异、风土适应与性状改良中的转座子](book/chapters/10-vitis-as-worked-example.md#103-葡萄无性系变异风土适应与性状改良中的转座子)
- [第11章 实践工作流：以葡萄基因组为例的端到端分析](book/chapters/11-practical-workflow.md)
  - [11.1 数据准备、软件环境与单基因组转座子从头注释实战](book/chapters/11-practical-workflow.md#111-数据准备软件环境与单基因组转座子从头注释实战)
  - [11.2 转座子文库精修、插入时间估算与基因组分布可视化](book/chapters/11-practical-workflow.md#112-转座子文库精修插入时间估算与基因组分布可视化)
  - [11.3 葡萄群体重测序TIPs鉴定与候选功能位点筛选实战](book/chapters/11-practical-workflow.md#113-葡萄群体重测序tips鉴定与候选功能位点筛选实战)
- [第12章 开放问题与前沿方向](book/chapters/12-open-questions.md)
  - [12.1 T2T基因组与泛基因组时代的转座子解析新挑战](book/chapters/12-open-questions.md#121-t2t基因组与泛基因组时代的转座子解析新挑战)
  - [12.2 深度学习与长读长多组学在转座子研究中的应用](book/chapters/12-open-questions.md#122-深度学习与长读长多组学在转座子研究中的应用)
  - [12.3 转座子工程化应用与未来作物育种前景](book/chapters/12-open-questions.md#123-转座子工程化应用与未来作物育种前景)
- [第13章 基因组里实际看到的转座子：完整、残缺、嵌合与驯化](book/chapters/13-observed-forms.md)
  - [13.1 完整的自主元件](book/chapters/13-observed-forms.md#131-完整的自主元件)
  - [13.2 非自主元件](book/chapters/13-observed-forms.md#132-非自主元件)
  - [13.3 碎片与截短体](book/chapters/13-observed-forms.md#133-碎片与截短体)
  - [13.4 solo-LTR 与 LTR 间非等位重组](book/chapters/13-observed-forms.md#134-solo-ltr-与-ltr-间非等位重组)
  - [13.5 嵌套插入（nested insertion）](book/chapters/13-observed-forms.md#135-嵌套插入nested-insertion)
  - [13.6 嵌合元件与重组产物](book/chapters/13-observed-forms.md#136-嵌合元件与重组产物)
  - [13.7 被驯化成宿主基因的 TE](book/chapters/13-observed-forms.md#137-被驯化成宿主基因的-teexaptationdomestication)
  - [13.8 携带宿主基因片段的元件](book/chapters/13-observed-forms.md#138-携带宿主基因片段的元件)
  - [13.9 TE 衍生的串联重复与卫星](book/chapters/13-observed-forms.md#139-te-衍生的串联重复与卫星)
  - [13.10 Penelope 类元件（PLE）](book/chapters/13-observed-forms.md#1310-penelope-类元件ple)
  - [13.11 DIRS 类元件](book/chapters/13-observed-forms.md#1311-dirs-类元件)
  - [13.12 Crypton](book/chapters/13-observed-forms.md#1312-crypton)
  - [13.13 Maverick/Polinton](book/chapters/13-observed-forms.md#1313-maverickpolinton)
  - [13.14 Ngaro 及其他酪氨酸重组酶反转录元件](book/chapters/13-observed-forms.md#1314-ngaro-及其他酪氨酸重组酶反转录元件)
  - [13.15 其他少见超家族与 Helitron2/Helentron](book/chapters/13-observed-forms.md#1315-其他少见超家族与-helitron2helentron)
  - [13.16 植物（包括葡萄）中各稀有类别的存在与否汇总](book/chapters/13-observed-forms.md#1316-植物包括葡萄中各稀有类别的存在与否汇总)
  - [13.17 注释工具对稀有类别的常见误判和漏判，以及人工核查建议](book/chapters/13-observed-forms.md#1317-注释工具对稀有类别的常见误判和漏判以及人工核查建议)
  - [13.18 本章小结](book/chapters/13-observed-forms.md#1318-本章小结)
- [转座子类型逐类详解](book/chapters/types-catalogue.md)
  - [分类树与总表](book/chapters/types-catalogue.md#分类树与总表)
  - [第一部分　LTR 逆转录转座子](book/chapters/types-catalogue.md#第一部分ltr-逆转录转座子目超家族与非自主衍生物)
  - [第二部分　Copia 超家族谱系（一）](book/chapters/types-catalogue.md#第二部分copia-超家族谱系一)
  - [第三部分　Copia 超家族谱系（二）](book/chapters/types-catalogue.md#第三部分copia-超家族谱系二)
  - [第四部分　Gypsy 超家族：色质病毒样谱系](book/chapters/types-catalogue.md#第四部分gypsy-超家族色质病毒样谱系)
  - [第五部分　Gypsy 超家族：苔藓/石松特有谱系与 OTA 分支](book/chapters/types-catalogue.md#第五部分gypsy-超家族苔藓石松特有谱系与-ota-分支)
  - [第六部分　DIRS、PLE 与 LINE/SINE 目](book/chapters/types-catalogue.md#第六部分dirsple-与-linesine-目)
  - [第七部分　LINE 分支（一）](book/chapters/types-catalogue.md#第七部分line-分支一)
  - [第八部分　LINE 分支（二）与 SINE 类型](book/chapters/types-catalogue.md#第八部分line-分支二与-sine-类型)
  - [第九部分　TIR DNA 转座子：主要超家族](book/chapters/types-catalogue.md#第九部分tir-dna-转座子主要超家族)
  - [第十部分　TIR DNA 转座子：其他超家族（一）](book/chapters/types-catalogue.md#第十部分tir-dna-转座子其他超家族一)
  - [第十一部分　TIR DNA 转座子：其他超家族（二）与 Crypton](book/chapters/types-catalogue.md#第十一部分tir-dna-转座子其他超家族二与-crypton)
  - [第十二部分　Helitron、Maverick 与基因捕获形态](book/chapters/types-catalogue.md#第十二部分helitronmaverick-与基因捕获形态)
  - [第十三部分　基因组中实际看到的转座子形态](book/chapters/types-catalogue.md#第十三部分基因组中实际看到的转座子形态)
  - [类型详解附录　分类体系外与有争议的类型](book/chapters/types-catalogue.md#类型详解附录分类体系外与有争议的类型)
- [附录A 常用专业术语与缩略语对照表](book/chapters/appendix-a-glossary.md)
- [附录B 公共数据库与主流生物信息学工具清单](book/chapters/appendix-b-databases-and-tools.md)
  - [公共转座子与重复序列数据库](book/chapters/appendix-b-databases-and-tools.md#公共转座子与重复序列数据库)
  - [转座子注释、精修与评估核心工具](book/chapters/appendix-b-databases-and-tools.md#转座子注释精修与评估核心工具)
  - [群体TIPs检测与常规辅助分析工具](book/chapters/appendix-b-databases-and-tools.md#群体tips检测与常规辅助分析工具)
- [附录C 推荐进阶阅读文献](book/chapters/appendix-c-further-reading.md)
  - [一、基础理论、发现史与基因组演化](book/chapters/appendix-c-further-reading.md#一基础理论发现史与基因组演化)
  - [二、分类体系与生物信息学注释方法](book/chapters/appendix-c-further-reading.md#二分类体系与生物信息学注释方法)
  - [三、表观遗传调控与宿主沉默](book/chapters/appendix-c-further-reading.md#三表观遗传调控与宿主沉默)
  - [四、葡萄基因组与转座子范例研究](book/chapters/appendix-c-further-reading.md#四葡萄基因组与转座子范例研究)

按类型写的较短笔记和配图见 [`docs/types/README.zh.md`](docs/types/README.zh.md)（英文索引：[`docs/types/README.md`](docs/types/README.md)）。TE 与宿主的笔记见 [`docs/host/README.zh.md`](docs/host/README.zh.md)。葡萄基因组中的 TE 见 [`docs/vitis/README.zh.md`](docs/vitis/README.zh.md)。教学示意图见 [`figures/README.md`](figures/README.md)。

## 软件与流程

默认路线是 EDTA，再到 TEtrimmer，再到 TEsorter，再到经过 CDS 过滤的 trusted 文库，最后用于软屏蔽或 panEDTA。带判断节点的决策树见 [`docs/WORKFLOW.zh.md`](docs/WORKFLOW.zh.md)。按步骤划分的软件、行业难点，以及同一路线的更详细说明见 [`docs/detection/tools_and_pipelines.zh.md`](docs/detection/tools_and_pipelines.zh.md)。用于识别各类型的序列特征见 [`docs/detection/signatures.zh.md`](docs/detection/signatures.zh.md)。交给基因注释的软屏蔽说明见 [`docs/detection/softmask_handoff.zh.md`](docs/detection/softmask_handoff.zh.md)。每一行的链接、标题匹配的 DOI（如有）、输入、输出和适用场合见 [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv)。此处未锁定工具版本。只在 Crossref 题名与目标论文一致时收录 DOI（核对于 2026-11-15，Asia/Shanghai，CST，UTC+8）。没有题名匹配 DOI 的条目只写网址，或标 [待确认]。

与上面默认的 EDTA 路线并列、但不取代它的，是 Inpactor 这一组面向植物 LTR 反转录转座子的工具：[Inpactor](https://github.com/simonorozcoarias/Inpactor) 和 [Inpactor2](https://github.com/simonorozcoarias/Inpactor2) 用于完整 LTR 元件的分类（Inpactor2 还能做检测并分到谱系），[InpactorDB](https://inpactordb.github.io) 是谱系级的植物 LTR 参考集，[SENMAP](https://github.com/simonorozcoarias/SENMAP) 在整理文库时保留完整拷贝，[TIP_finder](https://github.com/simonorozcoarias/TIP_finder) 用短读长双端数据检测插入多态。题名核对过的 DOI 和代码仓库链接见下方，以及 [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv)。

### 按步骤划分的软件

| 步骤 | 适用场合 | 本目录中的工具 |
|------|----------|----------------|
| de novo 发现 | 从组装或单倍型出发 | [EDTA](https://github.com/oushujun/EDTA)（此处默认）、[RepeatModeler2](https://github.com/Dfam-consortium/RepeatModeler)、[Earl Grey](https://github.com/TobyBaril/EarlGrey)；家族发现还有 [RepeatScout](https://github.com/Dfam-consortium/RepeatScout)、[RECON](https://github.com/Dfam-consortium/RECON)、[PILER](https://www.drive5.com/piler/) |
| 结构检测 | 寻找完整的 LTR、TIR、MITE 或 Helitron | [LTR_FINDER](https://github.com/xzhub/LTR_FINDER)、[LTR_FINDER_parallel](https://github.com/oushujun/LTR_FINDER_parallel)、[LTRharvest](https://github.com/genometools/genometools)、[LTR_retriever](https://github.com/oushujun/LTR_retriever)；[HelitronScanner](https://sourceforge.net/projects/helitronscanner/)；MITE-Hunter、[detectMITE](https://sourceforge.net/projects/detectmite/)、[TIR-Learner](https://github.com/oushujun/TIR-Learner)、[GRF](https://github.com/bioinfolabmu/GenericRepeatFinder)、[Inpactor2](https://github.com/simonorozcoarias/Inpactor2) |
| 同源注释 | 用文库做注释或屏蔽 | [RepeatMasker](https://github.com/Dfam-consortium/RepeatMasker)（[网站](https://www.repeatmasker.org/)）；文库为 [Dfam](https://www.dfam.org/) 和 [Repbase](https://www.girinst.org/repbase/) |
| 分类 | 给 working 文库贴标签 | [TEsorter](https://github.com/zhangrengang/TEsorter) + [REXdb](https://bitbucket.org/petrnovak/repex_tarean)（植物 LTR 谱系）；[DeepTE](https://github.com/LiLabAtVT/DeepTE)；[TEclass](https://bioinformatics.uni-muenster.de/tools/teclass/index.hbi)；[Inpactor](https://github.com/simonorozcoarias/Inpactor)、[Inpactor2](https://github.com/simonorozcoarias/Inpactor2) |
| 整理与 consensus | 把原始 consensus 变成 working 或 trusted 文库 | [TEtrimmer](https://github.com/qjiangzhao/TEtrimmer)（此处默认）、[MCHelper](https://github.com/GonzalezLab/MCHelper)、[SENMAP](https://github.com/simonorozcoarias/SENMAP)、Goubert 指南（[doi:10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7)）、[CD-HIT](https://github.com/weizhongli/cdhit) |
| 文库质控 | 去掉非 TE 重复、检查组装质量 | [TRF](https://github.com/Benson-Genomics-Lab/TRF)（非 TE 轨道；[网站](https://tandem.bu.edu/trf/trf.html)）；在整理后或泛注释上计算 LAI（[LTR_retriever](https://github.com/oushujun/LTR_retriever)） |
| 屏蔽 | 把基因组交给基因注释 | 只用 trusted 文库做 [RepeatMasker](https://github.com/Dfam-consortium/RepeatMasker) `-xsmall`；用 [BEDTools](https://github.com/arq5x/bedtools2) 检查轨道 |
| TE 年龄 / 插入时间 | 整理后的完整 LTR 对 | [LTR_retriever](https://github.com/oushujun/LTR_retriever)；演示脚本 `scripts/01_ltr_insertion_age.py` |
| 多态 TE 检测 | 群体或长读插入检测，不是建库 | [TEMP](https://github.com/JialiUMassWengLab/TEMP)、[RelocaTE2](https://github.com/JinfengChen/RelocaTE2)、[xTea](https://github.com/parklab/xTea)、[Jitterbug](https://github.com/elzbth/jitterbug)、[TIP_finder](https://github.com/simonorozcoarias/TIP_finder) |
| 泛基因组 TE | 一组单倍型或基因组 | [panEDTA](https://github.com/oushujun/EDTA)（EDTA 仓库中的 `panEDTA.sh`） |
| 可视化 / 碎片合并 | 整理同源注释 | [RepeatCraft](https://github.com/niccw/repeatcraftp)、[oneCodeToFindThemAll](https://doua.prabi.fr/software/one-code-to-find-them-all) |

### Inpactor 系列（植物 LTR 反转录转座子）

下列工具是对默认 EDTA 路线的补充或备选，不能代替经过 CDS 门控的 trusted 文库。

| 名称 | 用途 | 代码或数据仓库 | DOI |
|------|------|----------------|-----|
| Inpactor | 在高性能计算环境下分类植物 LTR 反转录转座子，区分自主与非自主拷贝，并估算插入时间 | [github.com/simonorozcoarias/Inpactor](https://github.com/simonorozcoarias/Inpactor) | [10.3390/biology7020032](https://doi.org/10.3390/biology7020032) |
| Inpactor2 | 结合深度学习与结构特征，检测完整植物 LTR 反转录转座子、过滤碎片与嵌套拷贝，并分类到超家族和谱系；输入为组装基因组 | [github.com/simonorozcoarias/Inpactor2](https://github.com/simonorozcoarias/Inpactor2) | [10.1093/bib/bbac511](https://doi.org/10.1093/bib/bbac511) |
| InpactorDB | 谱系级植物 LTR 反转录转座子参考集（论文中为 195 个基因组、108 个物种；去冗余后 67,241 条） | [InpactorDB 检索页](https://inpactordb.github.io)；数据集 [10.5281/zenodo.4386317](https://doi.org/10.5281/zenodo.4386317)（其后快照见 [10.5281/zenodo.5816833](https://doi.org/10.5281/zenodo.5816833)） | [10.3390/genes12020190](https://doi.org/10.3390/genes12020190) |
| SENMAP | 用卷积网络在整理植物 LTR 文库时保留完整拷贝 | [github.com/simonorozcoarias/SENMAP](https://github.com/simonorozcoarias/SENMAP) | [10.1515/jib-2021-0036](https://doi.org/10.1515/jib-2021-0036)（期刊论文；会议摘要：[10.1109/ci-ibbi54220.2021.9626130](https://doi.org/10.1109/ci-ibbi54220.2021.9626130)） |
| TIP_finder | 用 Illumina 双端短读、染色体级别参考基因组和转座子一致性序列，在高性能计算环境下检测插入多态 | [github.com/simonorozcoarias/TIP_finder](https://github.com/simonorozcoarias/TIP_finder) | [10.3390/biology9090281](https://doi.org/10.3390/biology9090281) |
| YORO | 用卷积网络做基因组目标检测，用于转座子的检测与分类 | [github.com/simonorozcoarias/YORO](https://github.com/simonorozcoarias/YORO) | [10.1371/journal.pone.0291925](https://doi.org/10.1371/journal.pone.0291925) |
| PanTEon | 跨界的转座子分类器设计与比较框架及配套数据库（预印本） | [github.com/simonorozcoarias/PanTEon](https://github.com/simonorozcoarias/PanTEon) | [10.64898/2026.04.01.715927](https://doi.org/10.64898/2026.04.01.715927) |

同一工作线上的相关论文（不是独立软件）：植物反转录转座子结构、识别与分类的综述（[10.3390/ijms20153837](https://doi.org/10.3390/ijms20153837)）；机器学习用于转座子检测与分类的系统调查（[10.7717/peerj.8311](https://doi.org/10.7717/peerj.8311)）；基于 k-mer 的植物 LTR 分类方法（[10.7717/peerj.11456](https://doi.org/10.7717/peerj.11456)）；以及这些任务中性能指标的比较（[10.3390/pr8060638](https://doi.org/10.3390/pr8060638)）。配套实验仓库：[MLinTEs](https://github.com/simonorozcoarias/MLinTEs) 和 [MachineLearningInTEs](https://github.com/simonorozcoarias/MachineLearningInTEs)。

### 按分析步骤增补的软件与数据库

下面是对上文软件表的补充，不改变默认的 EDTA、TEtrimmer、TEsorter 路线。每一条都有已打开的论文 DOI，或已打开且返回成功的官方代码/数据入口。仍找不到可核验来源的候选没有写入。

| 步骤 | 名称 | 用途 | 代码或数据入口 | DOI |
|------|------|------|----------------|-----|
| 从头检测（含 LTR、TIR、MITE、Helitron、LINE/SINE，以及基于短读的发现） | **RepeatExplorer2** | 用短读做图聚类，在不必先组装基因组的情况下识别并定量重复序列，提供 Galaxy 界面。 | [repeatexplorer-elixir.cerit-sc.cz](https://repeatexplorer-elixir.cerit-sc.cz) | [10.1038/s41596-020-0400-y](https://doi.org/10.1038/s41596-020-0400-y) |
|  | **dnaPipeTE** | 从低覆盖度原始短读组装、注释并定量转座子，不需要基因组组装。 | [github.com/clemgoub/dnaPipeTE](https://github.com/clemgoub/dnaPipeTE) | [10.1093/gbe/evv050](https://doi.org/10.1093/gbe/evv050) |
|  | **REPET** | 包含 TEdenovo 与 TEannot 的流程包，用于在组装基因组中从头检测、聚类并注释转座子家族。 | [urgi.versailles.inrae.fr/Tools/REPET](https://urgi.versailles.inrae.fr/Tools/REPET) | [10.1371/journal.pone.0016526](https://doi.org/10.1371/journal.pone.0016526) |
|  | **EAHelitron** | 基于保守末端基序和富 GC 发夹的 Helitron 结构注释工具。论文摘要中给出软件名 EAHelitron。 | [github.com/dontkme/EAHelitron](https://github.com/dontkme/EAHelitron) | [10.1186/s12859-019-2945-8](https://doi.org/10.1186/s12859-019-2945-8) |
|  | **MITE Tracker** | 通过邻近反向重复、家族聚类和侧翼序列过滤，在大型基因组中寻找并分类 MITE。 | [github.com/INTABiotechMJ/MITE-Tracker](https://github.com/INTABiotechMJ/MITE-Tracker) | [10.1186/s12859-018-2376-y](https://doi.org/10.1186/s12859-018-2376-y) |
|  | **miteFinderII** | 在真核基因组中识别隐藏的 MITE。当前仓库由 screamer/miteFinder 重定向到 jhu99/miteFinder。 | [github.com/jhu99/miteFinder](https://github.com/jhu99/miteFinder) | [10.1186/s12920-018-0418-y](https://doi.org/10.1186/s12920-018-0418-y) |
|  | **AnnoSINE** | 面向植物基因组的 SINE 注释工具，结合同源与结构搜索并过滤假阳性，以构建 SINE 文库。 | [github.com/yangli557/AnnoSINE](https://github.com/yangli557/AnnoSINE) | [10.1093/plphys/kiab524](https://doi.org/10.1093/plphys/kiab524) |
|  | **AnnoSINE_v2** | 用于植物和动物基因组从头 SINE 注释的加速版本（预印本）。 | [github.com/oushujun/AnnoSINE_v2](https://github.com/oushujun/AnnoSINE_v2) | [10.1101/2024.03.01.582874](https://doi.org/10.1101/2024.03.01.582874) |
|  | **SINE_Scan** | 在大规模基因组数据中发现 SINE 家族。 | [github.com/maohlzj/SINE_Scan](https://github.com/maohlzj/SINE_Scan) | [10.1093/bioinformatics/btw718](https://doi.org/10.1093/bioinformatics/btw718) |
|  | **SINE-Finder** | 论文中给出的工具，用于定向发现植物基因组中源自 tRNA 的 SINE。本次未确认到仍可访问的官方代码仓库。 | — | [10.1105/tpc.111.088682](https://doi.org/10.1105/tpc.111.088682) |
|  | **LtrDetector** | LTR 反转录转座子的从头检测工具。当前仓库由 TulsaBioinformaticsToolsmith/LtrDetector 重定向而来。 | [github.com/BioinformaticsToolsmith/LtrDetector](https://github.com/BioinformaticsToolsmith/LtrDetector) | [10.1186/s12864-019-5796-9](https://doi.org/10.1186/s12864-019-5796-9) |
|  | **MUSTv2** | 改进的近期活跃 MITE 从头检测程序。本次未确认到仍可访问的官方代码仓库。 | — | [10.1515/jib-2017-0029](https://doi.org/10.1515/jib-2017-0029) |
|  | **LTRdigest** | 注释候选 LTR 反转录转座子的内部特征（蛋白结构域、PBS 和 PPT）。与 LTRharvest 同属 GenomeTools。 | [github.com/genometools/genometools](https://github.com/genometools/genometools) | [10.1093/nar/gkp759](https://doi.org/10.1093/nar/gkp759) |
|  | **LTRpred** | 用于完整 LTR 反转录转座子从头注释的 R 包。当前仓库由 HajkD/LTRpred 重定向到 drostlab/LTRpred。 | [github.com/drostlab/LTRpred](https://github.com/drostlab/LTRpred) | [10.21105/joss.02170](https://doi.org/10.21105/joss.02170) |
|  | **MGEScan** | 官方说明中介绍的 Galaxy 系统，用于识别 LTR 与非 LTR 反转录转座子。 | [github.com/MGEScan/mgescan](https://github.com/MGEScan/mgescan) | — |
|  | **Red** | 无需预先文库、在全基因组尺度上从头检测重复 DNA 的工具。 | [github.com/BioinformaticsToolsmith/Red](https://github.com/BioinformaticsToolsmith/Red) | [10.1186/s12859-015-0654-5](https://doi.org/10.1186/s12859-015-0654-5) |
|  | **EDTA-GUI** | 面向植物的 EDTA 图形界面实现，并提供谱系级分类。本次未确认到官方代码仓库。 | — | [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) |
|  | **Tephra** | 从基因组组装发现转座子家族并描述其结构与演化的命令行流程，不必预先提供参考文库。官方说明中的引用是该仓库本身；本次未使用题名匹配的期刊论文。 | [github.com/sestaton/tephra](https://github.com/sestaton/tephra) | — |
|  | **Transposome** | 从未组装的双端全基因组鸟枪法读段注释转座子家族。 | [github.com/sestaton/Transposome](https://github.com/sestaton/Transposome) | [10.1093/bioinformatics/btv059](https://doi.org/10.1093/bioinformatics/btv059) |
|  | **CARP** | 综合从头重复序列流程，用于在基因组组装中识别、聚类并注释转座子和片段重复。本次未找到返回 HTTP 200 的官方代码仓库。 | — | [10.1371/journal.pone.0193588](https://doi.org/10.1371/journal.pone.0193588) |
|  | **MegaLTR** | 用于在植物基因组中检测完整 LTR 反转录转座子并计算 LTR 组装指数的网页服务与本地流程。本次未能成功打开配套网页服务；GitHub 仓库已打开。 | [github.com/MoradMMokhtar/MegaLTR](https://github.com/MoradMMokhtar/MegaLTR) | [10.3389/fpls.2023.1237426](https://doi.org/10.3389/fpls.2023.1237426) |
|  | **TE-greedy-nester** | 基于结构检测 LTR 反转录转座子，并重建其嵌套顺序。 | [gitlab.fi.muni.cz/lexa/nested](https://gitlab.fi.muni.cz/lexa/nested) | [10.1093/bioinformatics/btaa632](https://doi.org/10.1093/bioinformatics/btaa632) |
|  | **PhyLTR** | 官方说明中用于 LTR 反转录转座子系统发育分析的流程。已确认 Zenodo 软件记录；本次未使用另外题名匹配的期刊论文。 | [github.com/mcsimenc/PhyLTR](https://github.com/mcsimenc/PhyLTR) | [10.5281/zenodo.4256534](https://doi.org/10.5281/zenodo.4256534) |
|  | **TAREAN** | 从未组装短读识别并刻画卫星 DNA 的工具，可通过 RepeatExplorer 的 Galaxy 服务使用。RepeatExplorer2 本身已单独列出。 | [repeatexplorer-elixir.cerit-sc.cz/galaxy/](https://repeatexplorer-elixir.cerit-sc.cz/galaxy/) | [10.1093/nar/gkx257](https://doi.org/10.1093/nar/gkx257) |
|  | **CLARI-TE** | 官方说明中用于小麦等复杂基因组转座子注释的脚本。本次未确认到题名匹配的期刊论文。 | [github.com/jdaron/CLARI-TE](https://github.com/jdaron/CLARI-TE) | — |
|  | **Dfam TETools** | Dfam 联盟维护的容器，提供可运行的 RepeatMasker 与 RepeatModeler 安装。它封装的是本目录中已有的工具，本身不是新的注释器。 | [github.com/Dfam-consortium/TETools](https://github.com/Dfam-consortium/TETools) | — |
|  | **PanTE** | 泛基因组转座子注释流程，按官方说明和题名匹配的预印本，把多条互补的从头检测路径合并为分类文库。 | [github.com/unavailable-2374/Pan_TE](https://github.com/unavailable-2374/Pan_TE) | [10.21203/rs.3.rs-5867196/v1](https://doi.org/10.21203/rs.3.rs-5867196/v1) |
|  | **ParTEA** | Earl Grey 泛基因组流程（ParTEA），用于在多个基因组间保持一致的转座子注释。Earl Grey 本身已单独列出。 | [github.com/TobyBaril/EarlGreyParTEA](https://github.com/TobyBaril/EarlGreyParTEA) | [10.64898/2026.11.04.764261](https://doi.org/10.64898/2026.11.04.764261) |
|  | **MAKER-P** | 植物基因注释工具包，不是转座子注释器。在注释植物基因组时可使用重复序列文库。本次未找到返回 HTTP 200 的 MAKER-P 官方页面；未把通用 MAKER 仓库当作 MAKER-P 主页。 | — | [10.1104/pp.113.230144](https://doi.org/10.1104/pp.113.230144) |
| 文库构建、精修与去冗余 | **VSEARCH** | 通用的开放源代码聚类与去重工具，有时用于降低转座子文库冗余。它本身不是转座子注释器。 | [github.com/torognes/vsearch](https://github.com/torognes/vsearch) | [10.7717/peerj.2584](https://doi.org/10.7717/peerj.2584) |
|  | **MMseqs2** | 通用序列搜索与聚类套件，有时用于大规模转座子家族聚类。它本身不是转座子注释器。 | [github.com/soedinglab/MMseqs2](https://github.com/soedinglab/MMseqs2) | [10.1038/nbt.3988](https://doi.org/10.1038/nbt.3988) |
|  | **TE-Aid** | 绘制覆盖度、分歧度、自点阵和开放读框图，辅助人工精修一致性序列。介绍见本目录中已有的入门精修指南论文。 | [github.com/clemgoub/TE-Aid](https://github.com/clemgoub/TE-Aid) | [10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7) |
| 分类（含深度学习） | **NeuralTE** | 利用多种序列特征对转座子超家族进行分类的深度学习工具。 | [github.com/CSU-KangHu/NeuralTE](https://github.com/CSU-KangHu/NeuralTE) | [10.1145/3698587.3701346](https://doi.org/10.1145/3698587.3701346) |
|  | **TERL** | 用卷积网络从原始序列分类转座子。 | [github.com/muriloHoracio/TERL](https://github.com/muriloHoracio/TERL) | [10.1093/bib/bbaa185](https://doi.org/10.1093/bib/bbaa185) |
|  | **ClassifyTE** | 基于 stacking 的转座子层级分类器。 | [github.com/manisa/ClassifyTE](https://github.com/manisa/ClassifyTE) | [10.1093/bioinformatics/btab146](https://doi.org/10.1093/bioinformatics/btab146) |
|  | **PASTEC** | 将转座子自动分类到目一级的工具，可作为 REPET 模块或独立程序使用。 | [urgi.versailles.inrae.fr/Tools/REPET](https://urgi.versailles.inrae.fr/Tools/REPET) | [10.1371/journal.pone.0091929](https://doi.org/10.1371/journal.pone.0091929) |
| 插入多态检测（短读、长读及相关工具） | **McClintock 2** | 可安装并运行多种短读转座子插入检测器的元流程，并带有模拟评估框架。 | [github.com/bergmanlab/mcclintock](https://github.com/bergmanlab/mcclintock) | [10.1186/s13100-023-00296-4](https://doi.org/10.1186/s13100-023-00296-4) |
|  | **TEMP2** | 用短读取检测生殖系转座子插入，并可估计新发单例插入频率。附录B中已有条目。 | [github.com/weng-lab/TEMP2](https://github.com/weng-lab/TEMP2) | [10.1093/nar/gkab010](https://doi.org/10.1093/nar/gkab010) |
|  | **MELT** | 面向群体规模的短读可移动元件插入检测工具。附录B中已有条目。 | [melt.igs.umaryland.edu](https://melt.igs.umaryland.edu) | [10.1101/gr.218032.116](https://doi.org/10.1101/gr.218032.116) |
|  | **TEPID** | 用短读绘制植物群体中的转座子插入多样性。附录B中已有条目。官方说明引用该 eLife 论文。 | [github.com/ListerLab/TEPID](https://github.com/ListerLab/TEPID) | [10.7554/eLife.20777](https://doi.org/10.7554/eLife.20777) |
|  | **PoPoolationTE2** | 用 Pool-Seq 数据比较转座子插入多态。本次未确认到仍可访问的官方仓库。 | — | [10.1093/molbev/msw137](https://doi.org/10.1093/molbev/msw137) |
|  | **RetroSeq** | 用 Illumina 双端全基因组测序检测非参考转座子插入。 | [github.com/tk2/RetroSeq](https://github.com/tk2/RetroSeq) | [10.1093/bioinformatics/bts697](https://doi.org/10.1093/bioinformatics/bts697) |
|  | **TEFLoN** | 用短读发现转座子插入与缺失并估计速率。官方说明引用该论文，但论文题名中不含工具名。 | [github.com/jradrion/TEFLoN](https://github.com/jradrion/TEFLoN) | [10.1093/gbe/evx050](https://doi.org/10.1093/gbe/evx050) |
|  | **T-lex3** | 用短读对参考转座子插入分型，并估计群体频率。 | [github.com/GonzalezLab/T-lex3](https://github.com/GonzalezLab/T-lex3) | [10.1093/bioinformatics/btz727](https://doi.org/10.1093/bioinformatics/btz727) |
|  | **ngs_te_mapper2** | 用短读取检测转座子插入，包含分裂读支持。官方说明称方法见该 Genetics 论文。 | [github.com/bergmanlab/ngs_te_mapper2](https://github.com/bergmanlab/ngs_te_mapper2) | [10.1093/genetics/iyab113](https://doi.org/10.1093/genetics/iyab113) |
|  | **Mobster** | 用不一致读对和分裂读从高通量测序数据中检测可移动元件插入。 | [github.com/jyhehir/mobster](https://github.com/jyhehir/mobster) | [10.1186/s13059-014-0488-x](https://doi.org/10.1186/s13059-014-0488-x) |
|  | **TE-locate** | 用双端短读定位非参考转座子插入。本次未匹配到方法论文 DOI。 | [sourceforge.net/projects/te-locate](https://sourceforge.net/projects/te-locate/) | — |
|  | **TRACKPOSON** | 官方说明中介绍的流程，用于检测转座子插入多态并生成有无矩阵。 | [github.com/Markestine/TRACKPOSON](https://github.com/Markestine/TRACKPOSON) | — |
|  | **TrEMOLO** | 结合组装与比对，用长读取估计转座子等位频率。 | [github.com/DrosophilaGenomeEvolution/TrEMOLO](https://github.com/DrosophilaGenomeEvolution/TrEMOLO) | [10.1186/s13059-023-02911-2](https://doi.org/10.1186/s13059-023-02911-2) |
|  | **PALMER** | 用长读取检测非参考可移动元件插入。官方说明将该论文列为一作方法文献。 | [github.com/WeichenZhou/PALMER](https://github.com/WeichenZhou/PALMER) | [10.1093/nar/gkz1173](https://doi.org/10.1093/nar/gkz1173) |
|  | **LoRTE** | 用低覆盖度 PacBio 长读取检测转座子引起的变异。本次未找到返回 HTTP 200 的官方代码仓库。 | — | [10.1186/s13100-017-0088-x](https://doi.org/10.1186/s13100-017-0088-x) |
|  | **rMETL** | 通过对长读重新比对来检测可移动元件插入。 | [github.com/tjiangHIT/rMETL](https://github.com/tjiangHIT/rMETL) | [10.1093/bioinformatics/btz106](https://doi.org/10.1093/bioinformatics/btz106) |
|  | **sTELLeR** | 从长读基因组快速检测转座子插入，并输出 VCF。 | [github.com/kristinebilgrav/sTELLeR](https://github.com/kristinebilgrav/sTELLeR) | [10.1093/bioinformatics/btae686](https://doi.org/10.1093/bioinformatics/btae686) |
|  | **TELR** | 用长读取检测非参考转座子插入，并对插入序列做局部组装。官方说明引用该论文。 | [github.com/bergmanlab/telr](https://github.com/bergmanlab/telr) | [10.1093/nar/gkac794](https://doi.org/10.1093/nar/gkac794) |
|  | **somrit** | 用于从长读取识别并分析体细胞反转录转座子插入的工具包。 | [github.com/adcosta17/somrit](https://github.com/adcosta17/somrit) | [10.1101/2023.08.06.552193](https://doi.org/10.1101/2023.08.06.552193) |
|  | **SVAN** | 按官方说明，对序列已解析的插入与缺失（包括可移动元件插入）做注释和分类。本次未挂接题名匹配的方法学 DOI。 | [github.com/REPBIO-LAB/SVAN](https://github.com/REPBIO-LAB/SVAN) | — |
|  | **MEIGA-PAV** | 按官方说明，在已解析序列的结构变异 VCF 中注释可移动元件插入。 | [github.com/MEIGA-tk/MEIGA-PAV](https://github.com/MEIGA-tk/MEIGA-PAV) | — |
|  | **panREPET** | 无需参考基因组即可检测泛基因组中共有转座子插入的流程，用于回溯一个物种内的插入动态。 | [forgemia.inra.fr/urgi-anagen/panREPET](https://forgemia.inra.fr/urgi-anagen/panREPET) | [10.1186/s13059-026-03984-5](https://doi.org/10.1186/s13059-026-03984-5) |
|  | **pantera** | 从泛基因组变异图中的多态性识别转座子家族。 | [github.com/piosierra/pantera](https://github.com/piosierra/pantera) | [10.1186/s13100-024-00323-y](https://doi.org/10.1186/s13100-024-00323-y) |
|  | **Pannagram** | 按题名匹配的预印本和官方说明，做泛基因组比对并呼叫活动组。是通用泛基因组工具，不只是转座子注释器。 | [github.com/iganna/pannagram](https://github.com/iganna/pannagram) | [10.1101/2025.02.07.637071](https://doi.org/10.1101/2025.02.07.637071) |
|  | **PanGenie** | 针对泛基因组图中各类变异的短读分型工具。通用工具，不是转座子注释器。 | [github.com/eblerjana/pangenie](https://github.com/eblerjana/pangenie) | [10.1038/s41588-022-01043-w](https://doi.org/10.1038/s41588-022-01043-w) |
|  | **Paragraph** | 面向短读数据的图结构变异分型工具。通用工具，不是转座子注释器。此处使用已发表 DOI。 | [github.com/Illumina/paragraph](https://github.com/Illumina/paragraph) | [10.1186/s13059-019-1909-7](https://doi.org/10.1186/s13059-019-1909-7) |
|  | **SyRI** | 从全基因组组装中识别共线与重排区域以及局部序列差异。通用工具，不是转座子注释器。此处使用已发表 DOI，而非预印本。 | [github.com/schneebergerlab/syri](https://github.com/schneebergerlab/syri) | [10.1186/s13059-019-1911-0](https://doi.org/10.1186/s13059-019-1911-0) |
|  | **MEGAnE** | Mobile Element Genotyping Analysis Environment：按官方说明，从短读全基因组数据识别并为多态可移动元件分型。官方说明引用该预印本；预印本题名未使用工具名。 | [github.com/shohei-kojima/MEGAnE](https://github.com/shohei-kojima/MEGAnE) | [10.1101/2022.03.25.485726](https://doi.org/10.1101/2022.03.25.485726) |
|  | **TEfinder** | 利用双端测序中的不一致读段检测新的转座子插入的流程。 | [github.com/VistaSohrab/TEfinder](https://github.com/VistaSohrab/TEfinder) | [10.3390/genes12020224](https://doi.org/10.3390/genes12020224) |
|  | **ITIS** | 从二代测序数据识别转座子插入位点的工具。本次未能成功打开论文中的网站。 | — | [10.1186/s12859-015-0507-2](https://doi.org/10.1186/s12859-015-0507-2) |
|  | **TE-Tracker** | 从全基因组重测序系统识别转座事件。本次未确认到官方代码仓库。 | — | [10.1186/s12859-014-0377-z](https://doi.org/10.1186/s12859-014-0377-z) |
|  | **ELITE** | Efficiently Locating Insertions of Transposable Elements，一篇 ACM 方法论文。本次未确认到官方代码仓库。 | — | [10.1145/3307339.3342182](https://doi.org/10.1145/3307339.3342182) |
| 转座子表达与小 RNA | **TEtranscripts** | 在批量 RNA-seq 差异表达分析中同时计入基因与转座子表达，并处理多重比对读段。 | [github.com/mhammell-laboratory/TEtranscripts](https://github.com/mhammell-laboratory/TEtranscripts) | [10.1093/bioinformatics/btv422](https://doi.org/10.1093/bioinformatics/btv422) |
|  | **TElocal** | 按座位定量转座子表达，与 TEtranscripts 出自同一实验室。 | [github.com/mhammell-laboratory/TElocal](https://github.com/mhammell-laboratory/TElocal) | — |
|  | **Telescope** | 用贝叶斯模型从 RNA-seq 按座位估计转座子表达。 | [github.com/mlbendall/telescope](https://github.com/mlbendall/telescope) | [10.1371/journal.pcbi.1006453](https://doi.org/10.1371/journal.pcbi.1006453) |
|  | **SQuIRE** | 用于分散重复序列座位级定量的 RNA-seq 端到端流程。 | [github.com/wyang17/SQuIRE](https://github.com/wyang17/SQuIRE) | [10.1093/nar/gky1301](https://doi.org/10.1093/nar/gky1301) |
|  | **SalmonTE** | 基于 Salmon 的准比对流程，用于从 RNA-seq 定量转座子表达。当前仓库重定向到 jeonglab-bcm/SalmonTE。 | [github.com/jeonglab-bcm/SalmonTE](https://github.com/jeonglab-bcm/SalmonTE) | [10.1142/9789813235533_0016](https://doi.org/10.1142/9789813235533_0016) |
|  | **scTE** | 官方说明中用于从单细胞 RNA-seq 等数据定量转座子表达。 | [github.com/JiekaiLab/scTE](https://github.com/JiekaiLab/scTE) | — |
|  | **SoloTE** | 在单细胞 RNA-seq 中按座位定量转座子表达。 | [github.com/bvaldebenitom/SoloTE](https://github.com/bvaldebenitom/SoloTE) | [10.1038/s42003-022-04020-5](https://doi.org/10.1038/s42003-022-04020-5) |
|  | **TEtools** | 统计并比较转座子表达（TEcount 与 TEdiff），并提供 Galaxy 封装。 | [github.com/l-modolo/TEtools](https://github.com/l-modolo/TEtools) | [10.1093/nar/gkw953](https://doi.org/10.1093/nar/gkw953) |
|  | **RepEnrich** | 结合唯一比对与多重比对读段，从 RNA-seq 或 ChIP-seq 估计重复序列亚家族的转录富集。本次未确认到官方仓库。 | — | [10.1186/1471-2164-15-583](https://doi.org/10.1186/1471-2164-15-583) |
|  | **ShortStack** | 注释并定量小 RNA 基因，包括植物转座子沉默研究中常用的多重比对 21–24 nt siRNA。 | [github.com/MikeAxtell/ShortStack](https://github.com/MikeAxtell/ShortStack) | [10.1261/rna.035279.112](https://doi.org/10.1261/rna.035279.112) |
|  | **piPipes** | 官方说明中介绍的一套流程，用于分析多种测序数据中的 piRNA 与转座子转录本。 | [github.com/bowhan/piPipes](https://github.com/bowhan/piPipes) | — |
| 年龄、分歧度与景观 | **ParseRM** | 解析 RepeatMasker 的 .out 或 .align 文件，汇总组成、分歧度与景观。本次未匹配到独立方法论文的题名。 | [github.com/4ureliek/Parsing-RepeatMasker-Outputs](https://github.com/4ureliek/Parsing-RepeatMasker-Outputs) | — |
|  | **VHICA** | Vertical and Horizontal Inheritance Consistence Analysis：通过比较转座子与宿主基因的分歧，区分垂直遗传与水平转移。 | [cran.r-project.org/package=vhica](https://cran.r-project.org/package=vhica) | [10.1093/molbev/msv341](https://doi.org/10.1093/molbev/msv341) |
|  | **REANNOTATE** | 用于重建插入历史的重复序列自动古生物学注释。本次未能成功打开论文中的网站。 | — | [10.1186/1471-2164-9-614](https://doi.org/10.1186/1471-2164-9-614) |
|  | **RepeatLandscape** | 解析 RepeatMasker 比对输出并绘制重复序列景观直方图或饼图的脚本。本次未匹配到独立方法论文的题名。 | [github.com/caballero/RepeatLandscape](https://github.com/caballero/RepeatLandscape) | — |
|  | **TE_Density** | 按窗口计算相对于基因的转座子密度，用于研究转座子与基因的空间关系。 | [github.com/sjteresi/TE_Density](https://github.com/sjteresi/TE_Density) | [10.1186/s13100-022-00264-4](https://doi.org/10.1186/s13100-022-00264-4) |
|  | **TEGRiP** | Transposable Elements Genes RelationshIps Pipeline：检测转座子与相邻基因的位置和方向关系。官方说明使用名称 TEGRiP。 | [github.com/marieBvr/TEs_genes_relationship_pipeline](https://github.com/marieBvr/TEs_genes_relationship_pipeline) | [10.24072/pcjournal.57](https://doi.org/10.24072/pcjournal.57) |
|  | **Repeattools** | 按官方说明，比较不同物种的转座子组成和拷贝分歧。仓库说明引用的是 TEsorter 论文，该 DOI 未用在本条目。 | [github.com/AgustinAmata/Repeattools](https://github.com/AgustinAmata/Repeattools) | — |
| 可视化 | **StainedGlass** | 为超大串联重复及其他高度重复区域生成交互式一致性热图。 | [github.com/vollgerlab/StainedGlass](https://github.com/vollgerlab/StainedGlass) | [10.1093/bioinformatics/btac018](https://doi.org/10.1093/bioinformatics/btac018) |
|  | **ModDotPlot** | 用于串联重复和大段重复区间的快速交互式点阵图工具。 | [github.com/marbl/ModDotPlot](https://github.com/marbl/ModDotPlot) | [10.1093/bioinformatics/btae493](https://doi.org/10.1093/bioinformatics/btae493) |
|  | **FlexiDot** | 可定制、能处理序列歧义的点阵图工具，可用于比较包含重复序列的序列。通用可视化工具，不是转座子注释器。 | [github.com/molbio-dresden/flexidot](https://github.com/molbio-dresden/flexidot) | [10.1093/bioinformatics/bty395](https://doi.org/10.1093/bioinformatics/bty395) |
|  | **RepeatOBserver** | 可视化串联重复，并可标出可能的着丝粒。主要针对串联重复，不是转座子注释器。 | [github.com/celphin/RepeatOBserverV1](https://github.com/celphin/RepeatOBserverV1) | [10.1111/1755-0998.14084](https://doi.org/10.1111/1755-0998.14084) |
|  | **LTRsift** | 用于对从头检测到的 LTR 反转录转座子做半自动分类和后处理的图形界面。 | [github.com/satta/ltrsift](https://github.com/satta/ltrsift) | [10.1186/1759-8753-3-18](https://doi.org/10.1186/1759-8753-3-18) |
|  | **plotsr** | 可视化多个基因组组装之间的结构相似与重排。通用工具，不是转座子注释器。 | [github.com/schneebergerlab/plotsr](https://github.com/schneebergerlab/plotsr) | [10.1093/bioinformatics/btac196](https://doi.org/10.1093/bioinformatics/btac196) |
| 模拟与评测 | **simuG** | 通用基因组模拟器，可引入 SNP、indel、结构变异和转座子插入，用于方法测试。 | [github.com/yjx1217/simuG](https://github.com/yjx1217/simuG) | [10.1093/bioinformatics/btz424](https://doi.org/10.1093/bioinformatics/btz424) |
|  | **TEgenomeSimulator** | 用于按可配置的转座子景观模拟基因组的框架，供方法测试使用。 | [github.com/Plant-Food-Research-Open/TEgenomeSimulator](https://github.com/Plant-Food-Research-Open/TEgenomeSimulator) | [10.64898/2026.03.09.710711](https://doi.org/10.64898/2026.03.09.710711) |
|  | **PrinTE** | 正向模拟框架，用于研究转座子如何导致基因组膨胀与收缩。 | [github.com/cwb14/PrinTE](https://github.com/cwb14/PrinTE) | [10.1101/2025.06.04.657780](https://doi.org/10.1101/2025.06.04.657780) |
|  | **TEvarSim** | 转座子插入与缺失的基因组模拟器，也可模拟短读和长读数据。 | [github.com/daweili-lab/TEvarSim](https://github.com/daweili-lab/TEvarSim) | [10.1371/journal.pcbi.1013933](https://doi.org/10.1371/journal.pcbi.1013933) |
|  | **TE_simu** | 按官方说明，模拟基因组序列中转座子插入、扩增与演化的脚本。本次未挂接题名匹配的方法论文。 | [github.com/unavailable-2374/TE_simu](https://github.com/unavailable-2374/TE_simu) | — |
|  | **Hoen et al. 2015** | 呼吁系统评测转座子注释方法的方法学论文。这是论文，不是软件工具。 | — | [10.1186/s13100-015-0044-6](https://doi.org/10.1186/s13100-015-0044-6) |
|  | **Rishishwar et al. 2016** | 针对多态转座子检测工具的评测论文。这是论文，不是软件工具。 | — | [10.1093/bib/bbw072](https://doi.org/10.1093/bib/bbw072) |
|  | **Saha et al. 2008** | 对从头重复序列发现程序的实证比较。这是论文，不是软件工具。 | — | [10.1093/nar/gkn064](https://doi.org/10.1093/nar/gkn064) |
| 多倍体亚基因组与串联重复 | **TRASH** | Tandem Repeat Annotation and Structural Hierarchy：注释串联重复，包括卫星阵列。不是转座子注释器。 | [github.com/vlothec/TRASH](https://github.com/vlothec/TRASH) | [10.1093/bioinformatics/btad308](https://doi.org/10.1093/bioinformatics/btad308) |
|  | **SubPhaser** | 利用亚基因组特异 k-mer（主要来自转座子等重复序列）划分异源多倍体亚基因组。不是转座子注释器。 | [github.com/zhangrengang/SubPhaser](https://github.com/zhangrengang/SubPhaser) | [10.1111/nph.18173](https://doi.org/10.1111/nph.18173) |
|  | **PolyCRACKER** | 利用重复序列演化信号，在无监督条件下划分多倍体亚基因组。见到过非官方代码镜像，未将其作为官方仓库。 | — | [10.1186/s12864-019-5828-5](https://doi.org/10.1186/s12864-019-5828-5) |
| 数据库与参考集 | **PlantRep** | 在数百个植物基因组中重新注释得到的植物重复序列一致性库。本次未能成功打开其公开网站。 | — | [10.1007/s00299-021-02817-y](https://doi.org/10.1007/s00299-021-02817-y) |
|  | **RiTE-db** | 稻属转座子资源库。当前页面由旧的 genome.arizona.edu 地址重定向而来。 | [ava.genome.arizona.edu/cgi-bin/rite/index.cgi](https://ava.genome.arizona.edu/cgi-bin/rite/index.cgi) | [10.1186/s12864-015-1762-3](https://doi.org/10.1186/s12864-015-1762-3) |
|  | **SINEBase** | 收录真核生物 SINE 一致性序列并提供结构分析的数据库与工具。 | [sines.eimb.ru](https://sines.eimb.ru/) | [10.1093/nar/gks1263](https://doi.org/10.1093/nar/gks1263) |
|  | **SoyTEdb** | 大豆基因组转座子数据库。原域名现重定向到 SoyBase 的旧版页面。 | [legacy.soybase.org/soytedb](https://legacy.soybase.org/soytedb/) | [10.1186/1471-2164-11-113](https://doi.org/10.1186/1471-2164-11-113) |
|  | **RepetDB** | 与 REPET 项目相关的转座子参考序列统一资源。 | [urgi.versailles.inrae.fr/repetdb](https://urgi.versailles.inrae.fr/repetdb) | [10.1186/s13100-019-0150-y](https://doi.org/10.1186/s13100-019-0150-y) |
|  | **TREP** | 面向植物的人工精修转座子平台，附录B已有条目；此处补入方法目录。 | [trep-db.uzh.ch](https://trep-db.uzh.ch) | — |
|  | **HTT-DB** | 水平转移转座子数据库，另有更新说明论文。本次尝试的公开网站未能成功打开。 | — | [10.1093/bioinformatics/btv281](https://doi.org/10.1093/bioinformatics/btv281) |
|  | **PlantLTRdb** | 收录 195 个植物物种完整 LTR 反转录转座子的交互式数据库。 | [bioinformatics.um6p.ma/PlantLTRdb/](https://bioinformatics.um6p.ma/PlantLTRdb/) | [10.3389/fpls.2023.1134627](https://doi.org/10.3389/fpls.2023.1134627) |
|  | **DPTEdb** | 雌雄异株植物转座子综合数据库。本次未能成功打开论文中的网站。 | — | [10.1093/database/baw078](https://doi.org/10.1093/database/baw078) |
|  | **SPTEdb** | 杨柳科植物转座子数据库。本次未能成功打开论文中的网站。 | — | [10.1093/database/bay024](https://doi.org/10.1093/database/bay024) |
|  | **RetrOryza** | 水稻 LTR 反转录转座子数据库。本次尝试的公开网站未能成功打开。 | — | [10.1093/nar/gkl780](https://doi.org/10.1093/nar/gkl780) |
|  | **TIGR Plant Repeat Databases** | 历史上用于识别植物重复序列的汇总资源。本次未能成功打开原来的 TIGR 网址。 | — | [10.1093/nar/gkh099](https://doi.org/10.1093/nar/gkh099) |
|  | **ConTEdb** | 针叶树转座子综合数据库。本次尝试的公开网站未能成功打开。 | — | [10.1093/database/bay131](https://doi.org/10.1093/database/bay131) |
|  | **AnnoTEP-DB** | 与 EDTA-GUI 论文相关的说明与预注释基因组资源。目录中已有 EDTA-GUI 软件条目，本次未改那一行。当前可用地址需要末尾斜杠。 | [plantgenomics.ncc.unesp.br/AnnoTEP-DB/](https://plantgenomics.ncc.unesp.br/AnnoTEP-DB/) | [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) |
|  | **MaizeGP** | 开放的玉米图泛基因组平台，含结构变异目录。这是物种泛基因组资源，不是专一的转座子数据库。 | [github.com/Jia-nianhua/Maize-Graph-Pangenome](https://github.com/Jia-nianhua/Maize-Graph-Pangenome) | [10.1111/jipb.70439](https://doi.org/10.1111/jipb.70439) |
|  | **TE Hub** | 用于分享并连接转座子注释工具、数据、资源和方法的社区站点。 | [tehub.org](https://tehub.org/) | [10.1186/s13100-021-00244-0](https://doi.org/10.1186/s13100-021-00244-0) |
|  | **awesome-transposable-elements** | 公开整理的转座子研究软件、数据库和其他资源清单。这是社区索引，不是原始数据库。 | [github.com/nixonlab/awesome-transposable-elements](https://github.com/nixonlab/awesome-transposable-elements) | — |

### 操作流程

1. 针对每个组装或单倍型运行 `EDTA`，使用 `--species others --sensitive 1 --anno 1`，并显式设定 `--u`、记录其来源。葡萄的 `--u` 仍为 [待确认]；若不设 `--u`，EDTA 会静默使用水稻的 1.3e-8 /bp/年，不能当作葡萄的默认值。
2. 针对每个单倍型运行 `TEtrimmer`，合并 Perfect 与 Good 序列，并用 `CD-HIT` 生成相似度约 95% 的 working 文库。可以按需生成 80-80 阈值的家族目录，但不要覆盖 working 文库。
3. 使用 `TEsorter`（如 `rexdb-plant`）只分配结构域和标签。不要用 `all.cls.lib` 替换 working FASTA。
4. 通过包含 CDS BLAST 和 TEsorter 分类输出规则的整理步骤，生成 trusted FASTA 并记录 sha256。
5. 仅使用 trusted 文件进行软屏蔽，或作为 EDTA 的 `--curatedlib` 传入。
6. 运行 `panEDTA` 做正式合并，而不是直接拼接 TE 文库，随后对面板重新注释。
7. 在生成经过整理的泛 TE GFF 之后，再做 LTR 插入时间、LAI 和 PAV。

| 产物 | 可否作为 `--curatedlib` / 基因软屏蔽？ |
|------|----------------------------------------|
| 原始 EDTA TElib | 否 |
| working 文库（TEtrimmer 后 CD-HIT） | 否（整份文件） |
| 经过门控的 trusted 文库 | 是 |
| 把许多文库 `cat` 后再 CD-HIT | 否（去冗余不是整理） |

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --u RATE --threads 32
```

- 不要把原始 EDTA 输出当作金标准 TE 文库。
- 不要把 `cat` 加 CD-HIT 的结果直接当作 `--curatedlib`。
- 只做分类的工具只给 consensus 命名，不能取代修剪，也不能直接作为最终文库。
- 不要在 BRAKER 或 GALBA 流程中硬屏蔽。必须使用经过宿主基因清洗的 trusted 文库做软屏蔽。
- 非 TE 重复序列（如 TRF、端粒、rDNA）不属于 `--curatedlib`。

### 示例脚本

用 Python 3 和 numpy 即可运行的演示脚本在 [`scripts/`](scripts/)。它们使用一条人工放入的 LTR 样插入，而非真实的 *Vitis* 数据。见 [`scripts/README.md`](scripts/README.md) 和 [`testdata/README.md`](testdata/README.md)。操作示例见 [`testdata/EXAMPLES.md`](testdata/EXAMPLES.md)。

| 脚本 | 作用 | 是否实测 |
|------|------|----------|
| `00_make_tiny_genome.py` | 写入带一条人工 LTR 样插入的小 FASTA 和 BED | 是，2026-11-15 CST |
| `01_ltr_insertion_age.py` | 计算两条 LTR 的 p 距离和 K2P；只有提供 `--rate` 时才给年份（无默认速率）；T = K/(2r) | 是，2026-11-15 CST（未给 `--rate`） |
| `02_softmask.py` | 把 BED 区间改成小写（软屏蔽演示） | 是，2026-11-15 CST |
| `03_run_edta.sh` | 记录上面的 EDTA 命令 | 否（仅 `--dry-run` / `--help`） |
| `04_run_repeatmodeler_repeatmasker.sh` | 记录 RepeatModeler2 和 RepeatMasker `-xsmall` | 否（仅 `--dry-run` / `--help`） |
| `05_run_tesorter.sh` | 记录 TEsorter（rexdb-plant）和 all.cls.lib 规则 | 否（仅 `--dry-run` / `--help`） |
| `run_toy_pipeline.sh` | 运行上面三个已实测的 Python 脚本 | 是，2026-11-15 CST |

```bash
bash scripts/run_toy_pipeline.sh OUTDIR
```

DOI 题名核对见 [`DOI_CHECKS.tsv`](DOI_CHECKS.tsv)，说明见 [`DOI_CHECKS.NOTES.md`](DOI_CHECKS.NOTES.md)。为目录论断打开过的来源见 [`SOURCES_READ.tsv`](SOURCES_READ.tsv)。变更记录见 [`CHANGELOG.md`](CHANGELOG.md)。

作者：李旭振，[ORCID](https://orcid.org/0000-0003-3670-6657)

