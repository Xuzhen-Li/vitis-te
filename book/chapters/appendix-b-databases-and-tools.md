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

