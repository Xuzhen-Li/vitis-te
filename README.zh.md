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

