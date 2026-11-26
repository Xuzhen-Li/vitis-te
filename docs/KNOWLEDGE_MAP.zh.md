# 知识地图

[English](KNOWLEDGE_MAP.md)

本页按主题和页面类型列出本仓库的全部内容。TE-Lib 是一个通用的转座子知识、软件与流程库：书讲转座子本身，类型页和识别页讲各类元件怎么认，软件目录按分析步骤比较工具，流程页和脚本给出一条跑法。葡萄（*Vitis*）作为贯穿全书的例子保留。两个基因注释仓库按同样的结构组织。

本仓库原名 vitis-te。较早的页面仍用旧名，GitHub 会把旧链接转到新地址。

- [主题](#topics)
- [学习](#learn)
- [按分析步骤的软件](#software)
- [示例脚本与测试数据](#example-code)
- [图](#figures)
- [来源与核对](#sources)
- [其他文件](#other-files)

<a id="topics"></a>
## 主题

每个主题列出书章、知识页和首页软件目录里的对应小节。

### 发现史与核心概念

- 书：[第1章 转座子的发现史与核心概念](../book/chapters/01-discovery-and-core-concepts.md)

### 分类与命名

- 书：[第2章 转座子的分类体系与命名规范](../book/chapters/02-classification-and-nomenclature.md); [转座子类型逐类详解](../book/chapters/types-catalogue.md)
- 知识页：[TE 类型：教学地图](../docs/types/README.zh.md)
- 软件目录：[分类](../README.zh.md#分类)

### Ⅰ类反转录转座子

- 书：[第3章 Ⅰ类转座子（反转录转座子）的结构与生活史](../book/chapters/03-class-I-retrotransposons.md)
- 知识页：[LTR 反转录转座子](../docs/types/class_I_ltr.zh.md); [LINE 与 SINE](../docs/types/class_I_line_sine.zh.md); [DIRS 与 Penelope 样元件（PLE）](../docs/types/class_I_dirs_ple.zh.md); [TRIM 与 LARD](../docs/types/class_I_trim_lard.zh.md); [植物副反转录病毒与 Florendovirus](../docs/types/pararetrovirus_florendovirus.zh.md)
- 软件目录：[LTR 反转录转座子检测](../README.zh.md#ltr-反转录转座子检测)

### Ⅱ类 DNA 转座子

- 书：[第4章 Ⅱ类转座子（DNA转座子）的结构与生活史](../book/chapters/04-class-II-dna-transposons.md)
- 知识页：[TIR DNA 转座子](../docs/types/class_II_tir.zh.md); [MITE](../docs/types/class_II_mite.zh.md); [Helitron](../docs/types/class_II_helitron.zh.md); [Maverick / Polinton](../docs/types/class_II_maverick.zh.md); [Crypton](../docs/types/class_II_crypton.zh.md)
- 软件目录：[TIR、MITE、Helitron 与 SINE 检测](../README.zh.md#tirmitehelitron-与-sine-检测)

### 非转座子重复

- 知识页：[会混入 TE 文库的非 TE 重复](../docs/types/non_te_repeats.zh.md)
- 软件目录：[多倍体亚基因组与串联重复](../README.zh.md#多倍体亚基因组与串联重复)

### 基因组里实际看到的转座子

- 书：[第13章 基因组里实际看到的转座子：完整、残缺、嵌合与驯化](../book/chapters/13-observed-forms.md)

### 宿主沉默与表观遗传

- 书：[第5章 宿主沉默机制与表观遗传调控](../book/chapters/05-host-silencing-and-epigenetics.md)
- 知识页：[TE 与宿主](../docs/host/README.zh.md)
- 软件目录：[转座子表达与小 RNA](../README.zh.md#转座子表达与小-rna)

### 基因组演化与转座子动力学

- 书：[第6章 基因组演化与转座子动力学](../book/chapters/06-genome-evolution-and-te-dynamics.md)
- 软件目录：[插入年龄、景观与水平转移](../README.zh.md#插入年龄景观与水平转移)

### 识别、注释与建库

- 书：[第7章 转座子的检测、从头注释与文库构建](../book/chapters/07-detection-annotation-and-libraries.md)
- 知识页：[识别各类型所用的序列特征](../docs/detection/signatures.zh.md); [工具、主流流程和行业难点](../docs/detection/tools_and_pipelines.zh.md); [交给基因注释的软屏蔽交接](../docs/detection/softmask_handoff.zh.md)
- 软件目录：[整套流程及其覆盖的步骤](../README.zh.md#整套流程及其覆盖的步骤); [整套流程：论文、实验室与权威度](../README.zh.md#整套流程论文实验室与权威度); [重复家族发现工具与基于读段的发现](../README.zh.md#重复家族发现工具与基于读段的发现); [精修、去冗余与文库质控](../README.zh.md#精修去冗余与文库质控); [屏蔽、注释与注释结果整理](../README.zh.md#屏蔽注释与注释结果整理); [数据库与文库：通用](../README.zh.md#数据库与文库通用); [数据库与文库：植物](../README.zh.md#数据库与文库植物); [模拟与评测](../README.zh.md#模拟与评测)

### 插入多态（TIP）

- 书：[第8章 群体水平的转座子插入多态性（TIPs）分析](../book/chapters/08-insertion-polymorphisms-tips.md)
- 软件目录：[插入多态：短读长](../README.zh.md#插入多态短读长); [插入多态：长读长与结果注释](../README.zh.md#插入多态长读长与结果注释); [插入多态：组装、泛基因组与图基因组](../README.zh.md#插入多态组装泛基因组与图基因组); [插入多态：植物资源与其他输入](../README.zh.md#插入多态植物资源与其他输入)

### 表型与驯化

- 书：[第9章 转座子、表型变异与作物驯化](../book/chapters/09-phenotype-and-domestication.md)

### 以葡萄为例

- 书：[第10章 葡萄基因组中的转座子：以葡萄属（*Vitis*）为范例](../book/chapters/10-vitis-as-worked-example.md)
- 知识页：[葡萄基因组中的 TE](../docs/vitis/README.zh.md)
- 软件目录：[数据库与文库：葡萄（Vitis）](../README.zh.md#数据库与文库葡萄vitis)

### 操作流程

- 书：[第11章 实践工作流：以葡萄基因组为例的端到端分析](../book/chapters/11-practical-workflow.md)
- 知识页：[TE-Lib 流程](../docs/WORKFLOW.zh.md)
- 首页：[操作流程](../README.zh.md#操作流程)

### 可视化

- 软件目录：[可视化](../README.zh.md#可视化)

### 开放问题

- 书：[第12章 开放问题与前沿方向](../book/chapters/12-open-questions.md)
- 软件目录：[社区索引与交叉链接](../README.zh.md#社区索引与交叉链接)

### 附录

- 书：[附录A 常用专业术语与缩略语对照表](../book/chapters/appendix-a-glossary.md); [附录B 公共数据库与主流生物信息学工具清单](../book/chapters/appendix-b-databases-and-tools.md); [附录C 推荐进阶阅读文献](../book/chapters/appendix-c-further-reading.md)

<a id="learn"></a>
## 学习

- 书：[《转座子从发现到实践，以葡萄为例》](../book/README.md); [转座子从发现到实践，以葡萄为例](../book/TE_BOOK_full.md); [全书文件索引](../book/INDEX.md); [前言](../book/chapters/00-preface.md)
- 配图合订本：[配图预览说明（非正式书稿，第2版 p2d）](../book/illustrated_v3_p2d/TE_BOOK_illustrated_v3_p2d.md); [配图合订本](../book/illustrated_v3_p2d/README.md)

<a id="software"></a>
## 按分析步骤的软件

- [按分析步骤划分的软件](../README.zh.md#按分析步骤划分的软件)
- [转座子分析软件指南（按分析步骤）](../docs/software/README.zh.md)
- [`SOFTWARE_AUTHORITY.tsv`](../catalog/SOFTWARE_AUTHORITY.tsv); [`CATALOG.tsv`](../catalog/CATALOG.tsv)

<a id="example-code"></a>
## 示例脚本与测试数据

示例脚本很小，在植入了一个 LTR 样插入的玩具基因组上测试过，不是维护中的软件。

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
## 图

- [Figures](../figures/README.md); [Figures for the guide](../figures/guide/README.md)
- 配图合订本的图：`book/illustrated_v3_p2d/figures/`
- 213 个文件，含绘图脚本 `figures/guide/src/`

<a id="sources"></a>
## 来源与核对

- [`DOI_CHECKS.tsv`](../DOI_CHECKS.tsv)
- [DOI_CHECKS year convention](../DOI_CHECKS.NOTES.md)
- [`SOURCES_READ.tsv`](../SOURCES_READ.tsv)
- [Changelog](../CHANGELOG.md)
- [`SHA256SUMS.v2`](../SHA256SUMS.v2)
- [`SHA256SUMS.txt`](../book/illustrated_v3_p2d/SHA256SUMS.txt)

<a id="other-files"></a>
## 其他文件

- `README.md`
- `README.zh.md`
- `LICENSE`
- `NOTICE.md`
