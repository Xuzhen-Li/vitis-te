# 附录B 公共数据库与主流生物信息学工具清单

## 公共转座子与重复序列数据库

| 名称 | 定位与核心特点 | 适用场景 | 官方入口 |
| :--- | :--- | :--- | :--- |
| **Dfam** | 开源开放获取的转座子数据库，基于轮廓隐马尔可夫模型（profile HMMs）表征家族，涵盖精修与社区提交条目，为RepeatMasker/RepeatModeler默认后端库。 | 全基因组同源屏蔽、古老退化拷贝高灵敏度搜索及跨物种分类参考。 | https://dfam.org |
| **Repbase** | 历史最悠久的专家人工精修真核转座子参考库（由GIRI维护，现采用订阅制），分类体系细致，涵盖大量非模式物种与经典超家族。 | 高精度人工精修参考比对与历史文献分类标签核对。 | https://www.girinst.org/repbase/ |
| **TREP** | 面向植物（最初聚焦小麦族并扩展至多类被子植物）的高质量人工精修转座子平台，严格贯彻Wicker三字母代码命名规范。 | 植物转座子分类学基准参考与手动精修对照。 | https://trep-db.uzh.ch |
| **PGSB Repeat Element Database** | 整合多种已测序植物重复序列的比较基因组学参考库（原MIPS-REdat）。 | 植物跨物种同源重复序列检索与初步屏蔽。 | [待确认] |
| **REXdb / GyDB** | 专注于植物反转录转座子（REXdb）或LTR/逆转录病毒（GyDB）保守蛋白质结构域系统发育的垂直数据库。 | 结合TEsorter或HMMER对未知转座子一致性序列进行亚谱系精细分类。 | REXdb: https://bitbucket.org/petrnovak/repex_tarean ；GyDB: https://gydb.org |
| **InpactorDB** | 谱系级植物LTR反转录转座子参考集，论文中包含195个基因组、108个物种，去冗余后67,241条完整元件（doi:10.3390/genes12020190）。 | 训练或比对植物LTR谱系分类器，或作为同源检索的补充参考。 | 检索页 https://inpactordb.github.io ；数据集 doi:10.5281/zenodo.4386317 |

## 转座子注释、精修与评估核心工具

| 工具名称 | 核心定位与算法原理 | 适用场景 | 官方入口 |
| :--- | :--- | :--- | :--- |
| **RepeatMasker** | 基于同源比对（RMBlast、HMMER等）的全基因组重复序列屏蔽与注释引擎。 | 使用物种特异性精修文库或公共库进行全基因组转座子扫描与软/硬屏蔽。 | https://github.com/Dfam-consortium/RepeatMasker （网站 https://www.repeatmasker.org） |
| **RepeatModeler2** | 整合RECON、RepeatScout与LTR结构搜索的从头重复序列发现与一致性文库构建框架（doi:10.1073/pnas.1921046117）。 | 无先验参考库的新测序基因组从头重复序列打捞（尤其是LINE、SINE与古老家族）。 | https://www.repeatmasker.org ；https://github.com/Dfam-consortium/RepeatModeler |
| **LTR_FINDER / LTRharvest** | 基于精确种子与增强后缀数组的完整LTR反转录转座子从头结构搜索工具（doi:10.1093/nar/gkm286；doi:10.1186/1471-2105-9-18）。 | 全基因组高灵敏度搜寻候选完整LTR对，作为LTR_retriever的上游输入。 | LTR_FINDER: https://github.com/xzhub/LTR_FINDER ；LTRharvest: https://github.com/genometools/genometools |
| **LTR_retriever** | 融合末端基序、TSD、串联重复剔除与侧翼延伸比对过滤的高精度LTR鉴定与LAI计算引擎（doi:10.1104/pp.17.01310；doi:10.1093/nar/gky730）。 | 构建高置信度植物完整LTR文库、计算插入分歧度与评估基因组LAI指数。 | https://github.com/oushujun/LTR_retriever |
| **EDTA** | 串联LTR_retriever、TIR-Learner、HelitronScanner、RepeatModeler与RepeatMasker的植物整合注释流水线（doi:10.1186/s13059-019-1905-y），并衍生出面向泛基因组的panEDTA策略。 | 植物单基因组及多单倍型泛基因组的端到端从头转座子注释。 | https://github.com/oushujun/EDTA |
| **TEsorter** | 基于植物REXdb蛋白域数据库与HMMER的转座子编码域鉴定与精细亚谱系分类工具。 | 将`Unknown`一致性序列升级分类、区分*Copia*/*Gypsy*亚谱系并辅助排查宿主基因污染。 | https://github.com/zhangrengang/TEsorter |
| **TEtrimmer** | 自动化多拷贝抽提、侧翼延伸、多序列比对、边界修剪与报告生成的半自动转座子文库精修工具。 | 大幅降低大型植物基因组一致性文库手工精修的人力成本。 | https://github.com/qjiangzhao/TEtrimmer |
| **Inpactor** | 面向大型植物基因组的LTR反转录转座子并行分类与插入时间分析流程（doi:10.3390/biology7020032）。 | 在已检测的LTR候选集上做超家族/谱系分类、区分自主与非自主拷贝，并估算插入时间。 | https://github.com/simonorozcoarias/Inpactor |
| **Inpactor2** | 结合深度学习与结构特征，检测、过滤并分类完整植物LTR反转录转座子，可分到谱系（doi:10.1093/bib/bbac511）。 | 从组装基因组快速构建半整理的植物LTR参考文库，作为EDTA等流程之外的备选。 | https://github.com/simonorozcoarias/Inpactor2 |
| **SENMAP** | 用卷积网络区分完整与非完整植物LTR拷贝，用于文库整理（doi:10.1515/jib-2021-0036）。 | 在精修LTR文库时剔除碎片或嵌套拷贝。 | https://github.com/simonorozcoarias/SENMAP |

## 群体TIPs检测与常规辅助分析工具

| 工具名称 | 核心定位与算法原理 | 适用场景 | 官方入口 |
| :--- | :--- | :--- | :--- |
| **TEMP2 / MELT / TEPID** | 基于双端短读长DRP与SR信号的群体非参考转座子插入与参考缺失检测及分型工具。 | 大规模重测序群体（如葡萄、水稻、拟南芥群体）的TIPs鉴定与基因型矩阵构建。 | TEMP2: https://github.com/weng-lab/TEMP2 ；MELT: https://melt.igs.umaryland.edu ；TEPID: https://github.com/ListerLab/TEPID |
| **TIP_finder** | 用双端短读、染色体级别参考基因组和转座子一致性序列，在高性能计算环境下检测插入多态（doi:10.3390/biology9090281）。 | 大规模重测序数据集中的非参考转座子插入检测（与TEMP2等并列的备选工具）。 | https://github.com/simonorozcoarias/TIP_finder |
| **BWA-MEM / minimap2** | 分别面向短读长（Illumina）与长读长/基因组局部比对（PacBio HiFi、ONT、组装区段）的主流比对工具。 | 群体重测序比对、单倍型局部微共线性比对及长读长SV/TIPs上游比对。 | BWA: https://github.com/lh3/bwa ；minimap2: https://github.com/lh3/minimap2 |
| **SAMtools / BEDTools / SeqKit / VCFtools** | 分别用于BAM比对处理与去重、基因组区间交集与滑动窗口统计、FASTA清理以及VCF群体过滤与 $F_{ST}$ 计算的基础工具集。 | 贯穿第11章端到端实战工作流的数据预处理、质控与统计分析。 | SAMtools: https://github.com/samtools/samtools ；BEDTools: https://github.com/arq5x/bedtools2 ；SeqKit: https://github.com/shenwei356/seqkit ；VCFtools: https://github.com/vcftools/vcftools |
| **IGV** (Integrative Genomics Viewer) | 交互式桌面基因组浏览器，支持同步加载参考序列、GFF3注释与多样本BAM原始读长轨道。 | 候选TIPs位点的DRP夹击、SR软裁剪悬崖与TSD人工视觉核验排雷。 | https://igv.org ；https://github.com/igvteam/igv |


## 增补的数据库与工具

下列条目补充上文清单，不替换已有行。默认注释路线仍以 EDTA、TEtrimmer 与 TEsorter 为主。

### 增补的数据库

| 名称 | 定位与核心特点 | 适用场景 | 官方入口 |
| :--- | :--- | :--- | :--- |
| **PlantRep** | 在数百个植物基因组中重新注释得到的植物重复序列一致性库。截至 2026-11-24 CST 未能成功打开其公开网站。 | doi:10.1007/s00299-021-02817-y | — |
| **RiTE-db** | 稻属转座子资源库。当前页面由旧的 genome.arizona.edu 地址重定向而来。 | doi:10.1186/s12864-015-1762-3 | https://ava.genome.arizona.edu/cgi-bin/rite/index.cgi |
| **SINEBase** | 收录真核生物 SINE 一致性序列并提供结构分析的数据库与工具。 | doi:10.1093/nar/gks1263 | https://sines.eimb.ru/ |
| **SoyTEdb** | 大豆基因组转座子数据库。原域名现重定向到 SoyBase 的旧版页面。 | doi:10.1186/1471-2164-11-113 | https://legacy.soybase.org/soytedb/ |
| **RepetDB** | 与 REPET 项目相关的转座子参考序列统一资源。 | doi:10.1186/s13100-019-0150-y | https://urgi.versailles.inrae.fr/repetdb |
| **HTT-DB** | 水平转移转座子数据库，另有更新说明论文。截至 2026-11-25 CST，尝试的公开网站未能成功打开。 | doi:10.1093/bioinformatics/btv281 | https://web.archive.org/web/20220814084307/http://lpa.saogabriel.unipampa.edu.br:8080/httdatabase/ |
| **PlantLTRdb** | 收录 195 个植物物种完整 LTR 反转录转座子的交互式数据库。 | doi:10.3389/fpls.2023.1134627 | https://bioinformatics.um6p.ma/PlantLTRdb/ |
| **DPTEdb** | 雌雄异株植物转座子综合数据库。截至 2026-11-25 CST 未能成功打开论文中的网站。 | doi:10.1093/database/baw078 | https://web.archive.org/web/20180812090334/http://genedenovoweb.ticp.net:81/DPTEdb/index.php |
| **SPTEdb** | 杨柳科植物转座子数据库。截至 2026-11-25 CST 未能成功打开论文中的网站。 | doi:10.1093/database/bay024 | https://web.archive.org/web/20180730000921/http://genedenovoweb.ticp.net:81/SPTEdb/index.php |
| **RetrOryza** | 水稻 LTR 反转录转座子数据库。截至 2026-11-25 CST，尝试的公开网站未能成功打开。 | doi:10.1093/nar/gkl780 | — |
| **TIGR Plant Repeat Databases** | 历史上用于识别植物重复序列的汇总资源。截至 2026-11-25 CST 未能成功打开原来的 TIGR 网址。 | doi:10.1093/nar/gkh099 | https://rice.uga.edu/pub/data/TIGR_Plant_Repeats/ |
| **ConTEdb** | 针叶树转座子综合数据库。截至 2026-11-25 CST，尝试的公开网站未能成功打开。 | doi:10.1093/database/bay131 | https://web.archive.org/web/20210921143932/http://genedenovoweb.ticp.net:81/conTEdb/index.php |
| **AnnoTEP-DB** | 与 EDTA-GUI 论文相关的说明与预注释基因组资源。目录中已有 EDTA-GUI 软件条目，截至 2026-11-25 CST 未改那一行。当前可用地址需要末尾斜杠。 | doi:10.1186/s12864-026-12588-z | https://plantgenomics.ncc.unesp.br/AnnoTEP-DB/ |
| **MaizeGP** | 开放的玉米图泛基因组平台，含结构变异目录。这是物种泛基因组资源，不是专一的转座子数据库。 | doi:10.1111/jipb.70439 | https://github.com/Jia-nianhua/Maize-Graph-Pangenome |
| **TE Hub** | 用于分享并连接转座子注释工具、数据、资源和方法的社区站点。 | doi:10.1186/s13100-021-00244-0 | https://tehub.org/ |
| **awesome-transposable-elements** | 公开整理的转座子研究软件、数据库和其他资源清单。这是社区索引，不是原始数据库。 | — | https://github.com/nixonlab/awesome-transposable-elements |
| **GrapeGenomics Vitis RepeatMasker library** | 基于赤霞珠（Cabernet Sauvignon）的葡萄 RepeatMasker 自定义文库（Vitis_repeats.lib.gz），由 Cantu 实验室发布。这是可直接用于屏蔽的文库，不是可浏览检索的转座子数据库。未确认到正式的数据集 DOI。 | — | https://grapegenomics.com/pages/repeats.php |
| **PN40024 T2T TE annotations** | 随 PN40024 端粒到端粒基因组发布的转座子注释文件（PN_T2T_TE.gff3）。论文已在本目录中；本行只收录注释文件。 | doi:10.5281/zenodo.13741133 | https://zenodo.org/records/13741133 |

### 增补的检测、分类、表达与相关工具

| 工具名称 | 核心定位与算法原理 | 适用场景 | 官方入口 |
| :--- | :--- | :--- | :--- |
| **RepeatExplorer2** | 用短读做图聚类，在不必先组装基因组的情况下识别并定量重复序列，提供 Galaxy 界面。 | doi:10.1038/s41596-020-0400-y | https://repeatexplorer-elixir.cerit-sc.cz |
| **dnaPipeTE** | 从低覆盖度原始短读组装、注释并定量转座子，不需要基因组组装。 | doi:10.1093/gbe/evv050 | https://github.com/clemgoub/dnaPipeTE |
| **REPET** | 包含 TEdenovo 与 TEannot 的流程包，用于在组装基因组中从头检测、聚类并注释转座子家族。 | doi:10.1371/journal.pone.0016526 | https://urgi.versailles.inrae.fr/Tools/REPET |
| **EAHelitron** | 基于保守末端基序和富 GC 发夹的 Helitron 结构注释工具。论文摘要中给出软件名 EAHelitron。 | doi:10.1186/s12859-019-2945-8 | https://github.com/dontkme/EAHelitron |
| **MITE Tracker** | 通过邻近反向重复、家族聚类和侧翼序列过滤，在大型基因组中寻找并分类 MITE。 | doi:10.1186/s12859-018-2376-y | https://github.com/INTABiotechMJ/MITE-Tracker |
| **miteFinderII** | 在真核基因组中识别隐藏的 MITE。当前仓库由 screamer/miteFinder 重定向到 jhu99/miteFinder。 | doi:10.1186/s12920-018-0418-y | https://github.com/jhu99/miteFinder |
| **AnnoSINE** | 面向植物基因组的 SINE 注释工具，结合同源与结构搜索并过滤假阳性，以构建 SINE 文库。 | doi:10.1093/plphys/kiab524 | https://github.com/yangli557/AnnoSINE |
| **AnnoSINE_v2** | 用于植物和动物基因组从头 SINE 注释的加速版本（预印本）。 | doi:10.1101/2024.03.01.582874 | https://github.com/oushujun/AnnoSINE_v2 |
| **SINE_Scan** | 在大规模基因组数据中发现 SINE 家族。 | doi:10.1093/bioinformatics/btw718 | https://github.com/maohlzj/SINE_Scan |
| **SINE-Finder** | 论文中给出的工具，用于定向发现植物基因组中源自 tRNA 的 SINE。截至 2026-11-24 CST 未确认到仍可访问的官方代码仓库。 | doi:10.1105/tpc.111.088682 | — |
| **LtrDetector** | LTR 反转录转座子的从头检测工具。当前仓库由 TulsaBioinformaticsToolsmith/LtrDetector 重定向而来。 | doi:10.1186/s12864-019-5796-9 | https://github.com/BioinformaticsToolsmith/LtrDetector |
| **MUSTv2** | 改进的近期活跃 MITE 从头检测程序。截至 2026-11-24 CST 未确认到仍可访问的官方代码仓库。 | doi:10.1515/jib-2017-0029 | — |
| **LTRdigest** | 注释候选 LTR 反转录转座子的内部特征（蛋白结构域、PBS 和 PPT）。与 LTRharvest 同属 GenomeTools。 | doi:10.1093/nar/gkp759 | https://github.com/genometools/genometools |
| **LTRpred** | 用于完整 LTR 反转录转座子从头注释的 R 包。当前仓库由 HajkD/LTRpred 重定向到 drostlab/LTRpred。 | doi:10.21105/joss.02170 | https://github.com/drostlab/LTRpred |
| **MGEScan** | 官方说明中介绍的 Galaxy 系统，用于识别 LTR 与非 LTR 反转录转座子。 | 补充工具 | https://github.com/MGEScan/mgescan |
| **Red** | 无需预先文库、在全基因组尺度上从头检测重复 DNA 的工具。 | doi:10.1186/s12859-015-0654-5 | https://github.com/BioinformaticsToolsmith/Red |
| **EDTA-GUI** | 面向植物的 EDTA 图形界面实现，并提供谱系级分类。截至 2026-11-24 CST 未确认到官方代码仓库。 | doi:10.1186/s12864-026-12588-z | https://github.com/Marcos-Fernando/EDTA-GUI |
| **VSEARCH** | 通用的开放源代码聚类与去重工具，有时用于降低转座子文库冗余。它本身不是转座子注释器。 | doi:10.7717/peerj.2584 | https://github.com/torognes/vsearch |
| **MMseqs2** | 通用序列搜索与聚类套件，有时用于大规模转座子家族聚类。它本身不是转座子注释器。 | doi:10.1038/nbt.3988 | https://github.com/soedinglab/MMseqs2 |
| **TE-Aid** | 绘制覆盖度、分歧度、自点阵和开放读框图，辅助人工精修一致性序列。介绍见本目录中已有的入门精修指南论文。 | doi:10.1186/s13100-021-00259-7 | https://github.com/clemgoub/TE-Aid |
| **ParseRM** | 解析 RepeatMasker 的 .out 或 .align 文件，汇总组成、分歧度与景观。截至 2026-11-24 CST 未匹配到独立方法论文的题名。 | 补充工具 | https://github.com/4ureliek/Parsing-RepeatMasker-Outputs |
| **NeuralTE** | 利用多种序列特征对转座子超家族进行分类的深度学习工具。 | doi:10.1145/3698587.3701346 | https://github.com/CSU-KangHu/NeuralTE |
| **TERL** | 用卷积网络从原始序列分类转座子。 | doi:10.1093/bib/bbaa185 | https://github.com/muriloHoracio/TERL |
| **ClassifyTE** | 基于 stacking 的转座子层级分类器。 | doi:10.1093/bioinformatics/btab146 | https://github.com/manisa/ClassifyTE |
| **PASTEC** | 将转座子自动分类到目一级的工具，可作为 REPET 模块或独立程序使用。 | doi:10.1371/journal.pone.0091929 | https://urgi.versailles.inrae.fr/Tools/REPET |
| **McClintock 2** | 可安装并运行多种短读转座子插入检测器的元流程，并带有模拟评估框架。 | doi:10.1186/s13100-023-00296-4 | https://github.com/bergmanlab/mcclintock |
| **PoPoolationTE2** | 用 Pool-Seq 数据比较转座子插入多态。截至 2026-11-24 CST 未确认到仍可访问的官方仓库。 | doi:10.1093/molbev/msw137 | — |
| **RetroSeq** | 用 Illumina 双端全基因组测序检测非参考转座子插入。 | doi:10.1093/bioinformatics/bts697 | https://github.com/tk2/RetroSeq |
| **TEFLoN** | 用短读发现转座子插入与缺失并估计速率。官方说明引用该论文，但论文题名中不含工具名。 | doi:10.1093/gbe/evx050 | https://github.com/jradrion/TEFLoN |
| **T-lex3** | 用短读对参考转座子插入分型，并估计群体频率。 | doi:10.1093/bioinformatics/btz727 | https://github.com/GonzalezLab/T-lex3 |
| **ngs_te_mapper2** | 用短读取检测转座子插入，包含分裂读支持。官方说明称方法见该 Genetics 论文。 | doi:10.1093/genetics/iyab113 | https://github.com/bergmanlab/ngs_te_mapper2 |
| **Mobster** | 用不一致读对和分裂读从高通量测序数据中检测可移动元件插入。 | doi:10.1186/s13059-014-0488-x | https://github.com/jyhehir/mobster |
| **TE-locate** | 用双端短读定位非参考转座子插入。截至 2026-11-24 CST 未匹配到方法论文 DOI。 | 补充工具 | https://sourceforge.net/projects/te-locate/ |
| **TRACKPOSON** | 官方说明中介绍的流程，用于检测转座子插入多态并生成有无矩阵。 | 补充工具 | https://github.com/Markestine/TRACKPOSON |
| **TrEMOLO** | 结合组装与比对，用长读取估计转座子等位频率。 | doi:10.1186/s13059-023-02911-2 | https://github.com/DrosophilaGenomeEvolution/TrEMOLO |
| **PALMER** | 用长读取检测非参考可移动元件插入。官方说明将该论文列为一作方法文献。 | doi:10.1093/nar/gkz1173 | https://github.com/WeichenZhou/PALMER |
| **LoRTE** | 用低覆盖度 PacBio 长读取检测转座子引起的变异。截至 2026-11-24 CST 未找到返回 HTTP 200 的官方代码仓库。 | doi:10.1186/s13100-017-0088-x | — |
| **rMETL** | 通过对长读重新比对来检测可移动元件插入。 | doi:10.1093/bioinformatics/btz106 | https://github.com/tjiangHIT/rMETL |
| **sTELLeR** | 从长读基因组快速检测转座子插入，并输出 VCF。 | doi:10.1093/bioinformatics/btae686 | https://github.com/kristinebilgrav/sTELLeR |
| **TELR** | 用长读取检测非参考转座子插入，并对插入序列做局部组装。官方说明引用该论文。 | doi:10.1093/nar/gkac794 | https://github.com/bergmanlab/telr |
| **TEtranscripts** | 在批量 RNA-seq 差异表达分析中同时计入基因与转座子表达，并处理多重比对读段。 | doi:10.1093/bioinformatics/btv422 | https://github.com/mhammell-laboratory/TEtranscripts |
| **TElocal** | 按座位定量转座子表达，与 TEtranscripts 出自同一实验室。 | 补充工具 | https://github.com/mhammell-laboratory/TElocal |
| **Telescope** | 用贝叶斯模型从 RNA-seq 按座位估计转座子表达。 | doi:10.1371/journal.pcbi.1006453 | https://github.com/mlbendall/telescope |
| **SQuIRE** | 用于分散重复序列座位级定量的 RNA-seq 端到端流程。 | doi:10.1093/nar/gky1301 | https://github.com/wyang17/SQuIRE |
| **SalmonTE** | 基于 Salmon 的准比对流程，用于从 RNA-seq 定量转座子表达。当前仓库重定向到 jeonglab-bcm/SalmonTE。 | doi:10.1142/9789813235533_0016 | https://github.com/jeonglab-bcm/SalmonTE |
| **scTE** | 官方说明中用于从单细胞 RNA-seq 等数据定量转座子表达。 | 补充工具 | https://github.com/JiekaiLab/scTE |
| **SoloTE** | 在单细胞 RNA-seq 中按座位定量转座子表达。 | doi:10.1038/s42003-022-04020-5 | https://github.com/bvaldebenitom/SoloTE |
| **TEtools** | 统计并比较转座子表达（TEcount 与 TEdiff），并提供 Galaxy 封装。 | doi:10.1093/nar/gkw953 | https://github.com/l-modolo/TEtools |
| **RepEnrich** | 结合唯一比对与多重比对读段，从 RNA-seq 或 ChIP-seq 估计重复序列亚家族的转录富集。截至 2026-11-24 CST 未确认到官方仓库。 | doi:10.1186/1471-2164-15-583 | — |
| **ShortStack** | 注释并定量小 RNA 基因，包括植物转座子沉默研究中常用的多重比对 21–24 nt siRNA。 | doi:10.1261/rna.035279.112 | https://github.com/MikeAxtell/ShortStack |
| **piPipes** | 官方说明中介绍的一套流程，用于分析多种测序数据中的 piRNA 与转座子转录本。 | 补充工具 | https://github.com/bowhan/piPipes |
| **StainedGlass** | 为超大串联重复及其他高度重复区域生成交互式一致性热图。 | doi:10.1093/bioinformatics/btac018 | https://github.com/vollgerlab/StainedGlass |
| **ModDotPlot** | 用于串联重复和大段重复区间的快速交互式点阵图工具。 | doi:10.1093/bioinformatics/btae493 | https://github.com/marbl/ModDotPlot |
| **simuG** | 通用基因组模拟器，可引入 SNP、indel、结构变异和转座子插入，用于方法测试。 | doi:10.1093/bioinformatics/btz424 | https://github.com/yjx1217/simuG |
| **Tephra** | 从基因组组装发现转座子家族并描述其结构与演化的命令行流程，不必预先提供参考文库。官方说明中的引用是该仓库本身；截至 2026-11-25 CST 未使用题名匹配的期刊论文。 | — | https://github.com/sestaton/tephra |
| **Transposome** | 从未组装的双端全基因组鸟枪法读段注释转座子家族。 | doi:10.1093/bioinformatics/btv059 | https://github.com/sestaton/Transposome |
| **CARP** | 综合从头重复序列流程，用于在基因组组装中识别、聚类并注释转座子和片段重复。截至 2026-11-25 CST 未找到返回 HTTP 200 的官方代码仓库。 | doi:10.1371/journal.pone.0193588 | https://github.com/carp-te/carp-documentation |
| **MegaLTR** | 用于在植物基因组中检测完整 LTR 反转录转座子并计算 LTR 组装指数的网页服务与本地流程。截至 2026-11-25 CST 未能成功打开配套网页服务；GitHub 仓库已打开。 | doi:10.3389/fpls.2023.1237426 | https://github.com/MoradMMokhtar/MegaLTR |
| **TE-greedy-nester** | 基于结构检测 LTR 反转录转座子，并重建其嵌套顺序。 | doi:10.1093/bioinformatics/btaa632 | https://gitlab.fi.muni.cz/lexa/nested |
| **PhyLTR** | 官方说明中用于 LTR 反转录转座子系统发育分析的流程。已确认 Zenodo 软件记录；截至 2026-11-25 CST 未使用另外题名匹配的期刊论文。 | doi:10.5281/zenodo.4256534 | https://github.com/mcsimenc/PhyLTR |
| **TAREAN** | 从未组装短读识别并刻画卫星 DNA 的工具，可通过 RepeatExplorer 的 Galaxy 服务使用。RepeatExplorer2 本身已单独列出。 | doi:10.1093/nar/gkx257 | https://repeatexplorer-elixir.cerit-sc.cz/galaxy/ |
| **CLARI-TE** | 官方说明中用于小麦等复杂基因组转座子注释的脚本。截至 2026-11-25 CST 未确认到题名匹配的期刊论文。 | — | https://github.com/jdaron/CLARI-TE |
| **Dfam TETools** | Dfam 联盟维护的容器，提供可运行的 RepeatMasker 与 RepeatModeler 安装。它封装的是本目录中已有的工具，本身不是新的注释器。 | — | https://github.com/Dfam-consortium/TETools |
| **PanTE** | 泛基因组转座子注释流程，按官方说明和题名匹配的预印本，把多条互补的从头检测路径合并为分类文库。 | doi:10.21203/rs.3.rs-5867196/v1 | https://github.com/unavailable-2374/Pan_TE |
| **ParTEA** | Earl Grey 泛基因组流程（ParTEA），用于在多个基因组间保持一致的转座子注释。Earl Grey 本身已单独列出。 | doi:10.64898/2026.11.04.764261 | https://github.com/TobyBaril/EarlGreyParTEA |
| **MAKER-P** | 植物基因注释工具包，不是转座子注释器。在注释植物基因组时可使用重复序列文库。截至 2026-11-25 CST 未找到返回 HTTP 200 的 MAKER-P 官方页面；未把通用 MAKER 仓库当作 MAKER-P 主页。 | doi:10.1104/pp.113.230144 | https://yandell-lab.org/software/maker-p/ |
| **somrit** | 用于从长读取识别并分析体细胞反转录转座子插入的工具包。 | doi:10.1101/2023.08.06.552193 | https://github.com/adcosta17/somrit |
| **SVAN** | 按官方说明，对序列已解析的插入与缺失（包括可移动元件插入）做注释和分类。截至 2026-11-25 CST 未挂接题名匹配的方法学 DOI。 | — | https://github.com/REPBIO-LAB/SVAN |
| **MEIGA-PAV** | 按官方说明，在已解析序列的结构变异 VCF 中注释可移动元件插入。 | — | https://github.com/MEIGA-tk/MEIGA-PAV |
| **panREPET** | 无需参考基因组即可检测泛基因组中共有转座子插入的流程，用于回溯一个物种内的插入动态。 | doi:10.1186/s13059-026-03984-5 | https://forgemia.inra.fr/urgi-anagen/panREPET |
| **pantera** | 从泛基因组变异图中的多态性识别转座子家族。 | doi:10.1186/s13100-024-00323-y | https://github.com/piosierra/pantera |
| **Pannagram** | 按题名匹配的预印本和官方说明，做泛基因组比对并呼叫活动组。是通用泛基因组工具，不只是转座子注释器。 | doi:10.1101/2025.02.07.637071 | https://github.com/iganna/pannagram |
| **PanGenie** | 针对泛基因组图中各类变异的短读分型工具。通用工具，不是转座子注释器。 | doi:10.1038/s41588-022-01043-w | https://github.com/eblerjana/pangenie |
| **Paragraph** | 面向短读数据的图结构变异分型工具。通用工具，不是转座子注释器。此处使用已发表 DOI。 | doi:10.1186/s13059-019-1909-7 | https://github.com/Illumina/paragraph |
| **SyRI** | 从全基因组组装中识别共线与重排区域以及局部序列差异。通用工具，不是转座子注释器。此处使用已发表 DOI，而非预印本。 | doi:10.1186/s13059-019-1911-0 | https://github.com/schneebergerlab/syri |
| **MEGAnE** | Mobile Element Genotyping Analysis Environment：按官方说明，从短读全基因组数据识别并为多态可移动元件分型。官方说明引用该预印本；预印本题名未使用工具名。 | doi:10.1101/2022.03.25.485726 | https://github.com/shohei-kojima/MEGAnE |
| **TEfinder** | 利用双端测序中的不一致读段检测新的转座子插入的流程。 | doi:10.3390/genes12020224 | https://github.com/VistaSohrab/TEfinder |
| **ITIS** | 从二代测序数据识别转座子插入位点的工具。截至 2026-11-25 CST 未能成功打开论文中的网站。 | doi:10.1186/s12859-015-0507-2 | https://web.archive.org/web/20160825205722/http://bioinformatics.psc.ac.cn:80/software/ITIS/ |
| **TE-Tracker** | 从全基因组重测序系统识别转座事件。截至 2026-11-25 CST 未确认到官方代码仓库。 | doi:10.1186/s12859-014-0377-z | https://web.archive.org/web/20170813054646/http://www.genoscope.cns.fr:80/externe/tetracker/ |
| **ELITE** | Efficiently Locating Insertions of Transposable Elements，一篇 ACM 方法论文。截至 2026-11-25 CST 未确认到官方代码仓库。 | doi:10.1145/3307339.3342182 | https://github.com/Anwica/ELITE |
| **TIF** | Transposon Insertion Finder：从短读数据检测新生转座并报告插入位置的程序，不依赖已有的转座子文库。 | doi:10.1186/1471-2105-15-71 | https://github.com/akiomiyao/tif |
| **TEF** | Transposable Element Finder：通用的活性转座子检测程序，通过比较两个样本、或一个样本与参考基因组，利用接合读段或靶位点重复证据寻找活跃转座。 | doi:10.1186/s12859-022-05011-3 | https://github.com/akiomiyao/tef |
| **ITIPs** | 在白菜（Brassica rapa）泛基因组中检测转座子插入多态的流程，依赖 smartie-sv 和 bwa。 | doi:10.1111/pbi.13807 | https://github.com/caixu0518/ITIPs |
| **RTRIP** | 约 3,000 份水稻种质的转座子插入多态目录，并附有分析脚本。论文中的网站目前无法打开；已打开一份存档的官方页面。 | doi:10.1111/pbi.13425 | https://web.archive.org/web/20240226054850/http://ibi.zju.edu.cn/Rtrip/index.html |
| **panTEvo** | 用于在棉花泛基因组中追踪 LTR 反转录转座子动态与插入多态的流程。 | doi:10.1186/s13059-025-03837-7 | https://github.com/Lcamdom/panTEvo |
| **TEPEAK** | 用于在非模式物种群体中识别并刻画多态转座子的方法。不是植物专用工具。 | doi:10.1371/journal.pcbi.1013122 | https://github.com/ryanlayerlab/TEPEAK |
| **TypeSINE** | 从短读数据检测 SINE 插入多态。题名匹配的预印本研究对象是猪，不是植物。当前可用仓库为 github.com/mobilome/TypeSINE。 | doi:10.1101/2025.05.21.653756 | https://github.com/mobilome/TypeSINE |
| **AnchorWave** | 面向高序列多样性、广泛结构变异和全基因组复制的全基因组比对工具。不是转座子注释器；论文报告了玉米中转座子有无变异的召回情况。 | doi:10.1073/pnas.2113075119 | https://github.com/baoxingsong/AnchorWave |
| **SVIM-asm** | 面向单倍体和二倍体基因组组装的结构变异检测工具。不是转座子注释器。 | doi:10.1093/bioinformatics/btaa1034 | https://github.com/eldariont/svim-asm |
| **VHICA** | Vertical and Horizontal Inheritance Consistence Analysis：通过比较转座子与宿主基因的分歧，区分垂直遗传与水平转移。 | doi:10.1093/molbev/msv341 | https://cran.r-project.org/package=vhica |
| **REANNOTATE** | 用于重建插入历史的重复序列自动古生物学注释。截至 2026-11-25 CST 未能成功打开论文中的网站。 | doi:10.1186/1471-2164-9-614 | https://web.archive.org/web/20120208050248/http://www.bioinformatics.org/reannotate/ |
| **RepeatLandscape** | 解析 RepeatMasker 比对输出并绘制重复序列景观直方图或饼图的脚本。截至 2026-11-25 CST 未匹配到独立方法论文的题名。 | — | https://github.com/caballero/RepeatLandscape |
| **TE_Density** | 按窗口计算相对于基因的转座子密度，用于研究转座子与基因的空间关系。 | doi:10.1186/s13100-022-00264-4 | https://github.com/sjteresi/TE_Density |
| **TEGRiP** | Transposable Elements Genes RelationshIps Pipeline：检测转座子与相邻基因的位置和方向关系。官方说明使用名称 TEGRiP。 | doi:10.24072/pcjournal.57 | https://github.com/marieBvr/TEs_genes_relationship_pipeline |
| **Repeattools** | 按官方说明，比较不同物种的转座子组成和拷贝分歧。仓库说明引用的是 TEsorter 论文，该 DOI 未用在本条目。 | — | https://github.com/AgustinAmata/Repeattools |
| **FlexiDot** | 可定制、能处理序列歧义的点阵图工具，可用于比较包含重复序列的序列。通用可视化工具，不是转座子注释器。 | doi:10.1093/bioinformatics/bty395 | https://github.com/molbio-dresden/flexidot |
| **RepeatOBserver** | 可视化串联重复，并可标出可能的着丝粒。主要针对串联重复，不是转座子注释器。 | doi:10.1111/1755-0998.14084 | https://github.com/celphin/RepeatOBserverV1 |
| **LTRsift** | 用于对从头检测到的 LTR 反转录转座子做半自动分类和后处理的图形界面。 | doi:10.1186/1759-8753-3-18 | https://github.com/satta/ltrsift |
| **plotsr** | 可视化多个基因组组装之间的结构相似与重排。通用工具，不是转座子注释器。 | doi:10.1093/bioinformatics/btac196 | https://github.com/schneebergerlab/plotsr |
| **TEgenomeSimulator** | 用于按可配置的转座子景观模拟基因组的框架，供方法测试使用。 | doi:10.64898/2026.03.09.710711 | https://github.com/Plant-Food-Research-Open/TEgenomeSimulator |
| **PrinTE** | 正向模拟框架，用于研究转座子如何导致基因组膨胀与收缩。 | doi:10.1101/2025.06.04.657780 | https://github.com/cwb14/PrinTE |
| **TEvarSim** | 转座子插入与缺失的基因组模拟器，也可模拟短读和长读数据。 | doi:10.1371/journal.pcbi.1013933 | https://github.com/daweili-lab/TEvarSim |
| **TE_simu** | 按官方说明，模拟基因组序列中转座子插入、扩增与演化的脚本。截至 2026-11-25 CST 未挂接题名匹配的方法论文。 | — | https://github.com/unavailable-2374/TE_simu |
| **Hoen et al. 2015** | 呼吁系统评测转座子注释方法的方法学论文。这是论文，不是软件工具。 | doi:10.1186/s13100-015-0044-6 | — |
| **Rishishwar et al. 2016** | 针对多态转座子检测工具的评测论文。这是论文，不是软件工具。 | doi:10.1093/bib/bbw072 | — |
| **Saha et al. 2008** | 对从头重复序列发现程序的实证比较。这是论文，不是软件工具。 | doi:10.1093/nar/gkn064 | — |
| **TRASH** | Tandem Repeat Annotation and Structural Hierarchy：注释串联重复，包括卫星阵列。不是转座子注释器。 | doi:10.1093/bioinformatics/btad308 | https://github.com/vlothec/TRASH |
| **SubPhaser** | 利用亚基因组特异 k-mer（主要来自转座子等重复序列）划分异源多倍体亚基因组。不是转座子注释器。 | doi:10.1111/nph.18173 | https://github.com/zhangrengang/SubPhaser |
| **PolyCRACKER** | 利用重复序列演化信号，在无监督条件下划分多倍体亚基因组。见到过非官方代码镜像，未将其作为官方仓库。 | doi:10.1186/s12864-019-5828-5 | https://bitbucket.org/berkeleylab/jgi-polycracker/ |
