# vitis-te

[English](README.md) | 中文

<!-- PROSE:INTRO -->
本仓库是葡萄属（*Vitis*）及其他植物转座元件（TE）的方法目录。正文按阅读顺序展开：什么是 TE、它们是如何被发现的、如何移动、如何分类、各类型有哪些序列特征、与宿主基因组怎样相互作用、葡萄基因组里目前已知什么、现有方法卡在哪里，以及每一步使用哪些软件。这里也是把葡萄 TE 文库交给基因软屏蔽的公开交接处。实验室里的操作笔记留在私有目录中，不纳入 git。
<!-- /PROSE:INTRO -->
中文书稿《转座子从发现到实践，以葡萄为例》见 [`book/README.md`](book/README.md)。

结构注释的交接说明见 [gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)。与该仓库内容有所交叉是预期之中的；本页只提供交叉链接，不重复基因预测的操作手册。

<!-- PROSE:CATALOG_NOTE -->
**2026-11-15 目录。** 本轮不锁定工具版本，除被引用的论文年份外一律记为 `n/a`。论文年份按纸本年；Crossref 没有纸本日期的，改用发行或在线年，并在目录里注明。只在 Crossref 题名与目标论文一致时收录 DOI（核对于 2026-11-15，Asia/Shanghai，CST，UTC+8）。没有题名匹配 DOI 的条目只写网址，或标 [待确认]。带决策点的流程见 [`docs/WORKFLOW.zh.md`](docs/WORKFLOW.zh.md)。表格式目录见 [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv)（80 条）。
<!-- /PROSE:CATALOG_NOTE -->

## 不包含的内容

- 基因模型注释由 [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) 负责。
- 功能注释属于 [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation)。
- PAV 图和较长的图工具列表见 [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome)。
- 本仓库不是其他研究组原始 TE 识别结果的转存。
- 尚未公开出现在 GitHub 上的私有实验草稿和讲义，不复制到这里。

## 目录

0. [什么是转座元件](#section-0)
1. [TE 是怎样被发现的](#section-1)
2. [TE 怎样移动](#section-2)
3. [分类](#section-3)
4. [序列特征](#section-4)
5. [TE 与宿主](#section-5)
6. [葡萄基因组中的 TE](#section-6)
7. [行业难点](#section-7)
8. [按步骤划分的软件](#section-8)
9. [操作流程、红线和示例脚本](#section-9)
10. [术语表](#section-10)

<a id="section-0"></a>
## 0. 什么是转座元件

<!-- PROSE:SECTION:T00A -->
简单来说，转座元件是一段能够在基因组里变换位置，或者把自己复制到新位置的 DNA。有的元件会从一处切下来，再贴到另一处；有的会先抄成 RNA，再反转录成新的 DNA 拷贝，原来的拷贝仍留在原地。Helitron 以滚环方式移动（见[第 2 节](#section-2)）。随着时间推移，许多拷贝会失去移动能力，只剩下失活的残留。

在许多植物基因组里，TE 占了很大比例。它们可能落在基因附近或内部，改变基因的使用方式；也可能被宿主沉默，长时间处于不活跃状态。后面的章节按以下顺序展开：发现史、移动方式、分类名称、识别各类型的序列特征、对宿主的影响、葡萄里已知的事实，最后是实践中的难点和软件。

入门综述包括 Feschotte、Jiang 和 Wessler（2002，[doi:10.1038/nrg793](https://doi.org/10.1038/nrg793)）、Lisch（2013，[doi:10.1038/nrg3374](https://doi.org/10.1038/nrg3374)）以及 Wells 和 Feschotte（2020，[doi:10.1146/annurev-genet-040620-022145](https://doi.org/10.1146/annurev-genet-040620-022145)）。本仓库统一采用 Wicker 等人（2007，[doi:10.1038/nrg2165](https://doi.org/10.1038/nrg2165)）的分类。
<!-- /PROSE:SECTION:T00A -->

<a id="section-1"></a>
## 1. TE 是怎样被发现的

<!-- PROSE:SECTION:T00B -->
这一节提供一条阅读路径，并非列出所有相关论文的完整历史。下文陈述仅限于 2026-11-15（CST）已在 Crossref 上题名匹配的论文。数字、基因名或某个短语的首次使用，若原句未经重读，一律标 [待确认]。

**玉米，以及“DNA 可以移动”这一认识。** McClintock（1950，[doi:10.1073/pnas.36.6.344](https://doi.org/10.1073/pnas.36.6.344)）描述了玉米中可变位点的起源和行为。随后的报告（McClintock 1953，[doi:10.1093/genetics/38.6.579](https://doi.org/10.1093/genetics/38.6.579)）描写了在选定玉米位点上诱导不稳定性。后来文献所称的 Activator/Dissociation（Ac/Ds）系统，正是建立在这项工作之上；她最早在哪一篇里使用这两个名称，这里没有重读原文 [待确认]。1983 年，她因发现可移动遗传元件获得诺贝尔生理学或医学奖，讲演稿发表为 McClintock（1984，[doi:10.1126/science.15739260](https://doi.org/10.1126/science.15739260)）。

**细菌。** Jordan、Saedler 和 Starlinger（1968，[doi:10.1007/bf00433726](https://doi.org/10.1007/bf00433726)）表明，大肠杆菌 gal 操纵子中某些强极性突变是由插入引起的。插入序列（IS 元件）现在是一类记述清楚的细菌可移动 DNA（Mahillon 和 Chandler 1998，[doi:10.1128/mmbr.62.3.725-774.1998](https://doi.org/10.1128/mmbr.62.3.725-774.1998)）。Shapiro（1979，[doi:10.1073/pnas.76.4.1933](https://doi.org/10.1073/pnas.76.4.1933)）为噬菌体 Mu 及其他转座元件的转座和复制提出了一般性的分子模型。

**酵母，以及经由 RNA 的移动。** Boeke、Garfinkel、Styles 和 Fink（1985，[doi:10.1016/0092-8674(85)90197-7](https://doi.org/10.1016/0092-8674(85)90197-7)）证明，酵母的 Ty 元件通过 RNA 中间体转座。这一实验为后来的第 I 类 / 反转录转座子图景提供了关键的直接证明：元件先被转录，再反转录，随后新的 DNA 拷贝插入基因组。

**果蝇与 hybrid dysgenesis（杂交衰退，中文定名 [待确认]）。** Kidwell、Kidwell 和 Sved（1977，[doi:10.1093/genetics/86.4.813](https://doi.org/10.1093/genetics/86.4.813)）描述了黑腹果蝇的 hybrid dysgenesis：某些杂交组合的后代出现突变、不育和雄性重组等异常性状。Bingham、Kidwell 和 Rubin（1982，[doi:10.1016/0092-8674(82)90463-9](https://doi.org/10.1016/0092-8674(82)90463-9)）的结果有力支持 P 因子假说：P-M hybrid dysgenesis 的分子基础是 P 元件，这是一类存在于 P 品系中的转座子。

**基因组大小，以及“因为能复制而扩散”的 DNA。** 表观复杂度并不相应增加的生物，单倍基因组的 DNA 量（C 值）仍可能差异很大。Thomas（1971，[doi:10.1146/annurev.ge.05.120171.001321](https://doi.org/10.1146/annurev.ge.05.120171.001321)）在这一背景下讨论了染色体的遗传组织。二手文献把“C-value paradox”这一用语归于该文；Thomas 原文本身本轮没有重读 [待确认]。Doolittle 和 Sapienza（1980，Nature 284:601–603，[doi:10.1038/284601a0](https://doi.org/10.1038/284601a0)）以及 Orgel 和 Crick（1980，Nature 284:604–607，[doi:10.1038/284604a0](https://doi.org/10.1038/284604a0)）提出，许多 DNA 仅凭在基因组内复制的能力就能扩散，不必对生物体本身具有功能——即“自私 DNA”。这两篇是 1980 年 4 月 Nature 第 284 卷的文章（Crossref 题名已匹配）。后来 Orgel、Crick 和 Sapienza（1980，Nature 288:645–646，[doi:10.1038/288645a0](https://doi.org/10.1038/288645a0)）的回复属于另一条目，不能替代 4 月的两篇文章。DOI 10.1038/288604a0 是另一篇论文，此处不用。

**统一分类，然后进入基因组时代。** Finnegan（1989）把真核 TE 分成两类；Wicker 等人（2007）补上了本仓库采用的层级（见[第 3 节](#section-3)）。进入全基因组测序时代后，TE 的规模变得一目了然。Schnable 等人（2009，[doi:10.1126/science.1178534](https://doi.org/10.1126/science.1178534)）在玉米 B73 基因组中写到：“Nearly 85% of the genome is composed of hundreds of families of transposable elements”，并指出这些元件捕获并扩增了大量基因片段。

**葡萄上的节点**将在[第 5、6 节](#section-5)展开。简而言之：Kobayashi、Goto-Yamamoto 和 Hirochika（2004，[doi:10.1126/science.1095011](https://doi.org/10.1126/science.1095011)）报道了反转录转座子诱导的葡萄果皮颜色突变（这篇短文的正文本轮没有重读）。This 等人（2007，[doi:10.1007/s00122-006-0472-2](https://doi.org/10.1007/s00122-006-0472-2)）的摘要表明，Gret1 反转录元件插入 *VvmybA1* 启动子，与欧亚葡萄的白果表型密切相关。Jaillon 等人（2007）发表了第一份葡萄基因组序列，并给出了重复序列与转座元件的合计比例（见[第 3 节](#section-3)和[第 6 节](#section-6)）。后来的泛基因组工作汇总了许多组装中的结构变异（Liu 等人 2024；见第 6 节）；该文报道平均 88.6% 的结构变异与 TE 重叠（是重叠，不是这些变异中 TE 插入所占的比例）。
<!-- /PROSE:SECTION:T00B -->

<a id="section-2"></a>
## 2. TE 怎样移动

<!-- PROSE:SECTION:T00C -->
移动机制是[第 3 节](#section-3)两类分类系统的基础。

**复制粘贴（第 I 类，反转录转座子）。** 元件先被转录成 RNA，再反转录成 DNA，新拷贝插入基因组，而原来的拷贝留在原地。Boeke 等人（1985）在酵母 Ty 元件上证明了这一 RNA 中间体。植物基因组富含 LTR 反转录转座子（Copia/Ty1 和 Gypsy/Ty3），也含有非 LTR 元件（LINE，以及依赖它们的非自主 SINE）。

**剪切粘贴（许多第 II 类 TIR 元件）。** 转座酶把元件从一处切出，插入另一处。这类元件两端通常是末端反向重复（TIR），插入时会留下短的靶位点重复（TSD）。短的非自主 MITE 来源于 TIR 元件，自身不编码转座酶。

**滚环，以及 Maverick。** Helitron 以滚环方式转座（Kapitonov 和 Jurka 2001，[doi:10.1073/pnas.151269298](https://doi.org/10.1073/pnas.151269298)）。在 Wicker 体系中，Helitron 和 Maverick（Polinton）同属第 II 类的 subclass 2，因为它们转座时不发生双链切断。Helitron 通常既没有 TIR 也没有 TSD。Maverick 具有很长的 TIR，被认为靠自身编码的 DNA 聚合酶复制。Maverick 的 TSD 长度在对照 Wicker 原表之前标为 [待确认]。

**自主与非自主拷贝。** 自主元件编码自己移动所需的蛋白；非自主元件不编码这些蛋白，只能在有其他元件提供蛋白时移动——例如 SINE 依赖 LINE 的机制，MITE 依赖相关的转座酶。由于非自主拷贝缺乏编码结构域，按结构域分类的工具常把它们标成 Unknown。它们通常独立保留为各自的家族，依靠共有的末端或与自主元件的同源性归入超家族，而不并入自主家族的共有序列（见[第 7 节](#section-7)）。此外，误入文库的宿主基因片段很危险，因为它们会把真基因软屏蔽掉（见[第 9 节](#section-9)）。
<!-- /PROSE:SECTION:T00C -->

<a id="section-3"></a>
## 3. 分类

<!-- PROSE:SECTION:T01 -->
Finnegan（1989，[doi:10.1016/0168-9525(89)90039-5](https://doi.org/10.1016/0168-9525(89)90039-5)）把真核转座子分为第 I 类（经由 RNA 中间体复制）和第 II 类（经由 DNA 中间体移动）。Wicker 等人（2007，[doi:10.1038/nrg2165](https://doi.org/10.1038/nrg2165)）保留这一划分，并增加了目、超家族和家族的层级。当两条序列在编码区或内部区，或在末端重复区上，至少 80% 的长度达到至少 80% 一致性，并且覆盖至少 80 bp 时，归为同一家族（Wicker 等人 2007 的 80-80-80 规则）。

植物基因组中常见的目包括：

- LTR 反转录转座子，主要是 Ty1/Copia 和 Ty3/Gypsy 超家族（有的体系还列入 Bel-Pao、反转录病毒和花椰菜花叶病毒 / 副反转录病毒类群）。
- 非 LTR 反转录转座子：LINE 和 SINE。
- 带 TIR 的 DNA 转座子，以及由它们衍生的短的非自主 MITE。
- 以滚环方式转座的 Helitron（Kapitonov 和 Jurka 2001，[doi:10.1073/pnas.151269298](https://doi.org/10.1073/pnas.151269298)）。在 Wicker 体系中，Helitron 和 Maverick（Polinton）同属第 II 类的 subclass 2，因为它们转座时不发生双链切断。Helitron 通常既没有 TIR 也没有 TSD。Maverick 具有很长的 TIR，被认为靠自身编码的 DNA 聚合酶复制。Maverick 的 TSD 长度在对照 Wicker 原表之前标为 [待确认]。

不同命名体系并不总是一致。

- Kapitonov 和 Jurka（2008，[doi:10.1038/nrg2165-c1](https://doi.org/10.1038/nrg2165-c1)）主张一套在 Repbase 中实现的“通用分类”。Repbase 名称与 Wicker 名称相关，但并非同一套标签。
- RepeatMasker 和 Dfam 是按与 consensus 或 HMM 文库的同源性来命名的。RepeatMasker 输出里的字符串只是文库命中结果，本身并不是一次新的结构分类。Dfam 是开放文库（[doi:10.1186/s13100-020-00230-y](https://doi.org/10.1186/s13100-020-00230-y)）；Repbase 是另一套历史上很常用的数据库（[doi:10.1159/000084979](https://doi.org/10.1159/000084979)）。动物家族更丰富的文库，可能把植物特有谱系标成 `Unknown`，或只给出一个笼统的 `LTR/Gypsy`、`LTR/Copia`。
- TEsorter 结合 REXdb，根据保守蛋白结构域把植物 LTR 划分到谱系（例如 Copia 的 Ale、SIRE，Gypsy 的 Tekay、CRM；Neumann 等人 2019，[doi:10.1186/s13100-018-0144-1](https://doi.org/10.1186/s13100-018-0144-1)；Zhang 等人 2022，[doi:10.1093/hr/uhac017](https://doi.org/10.1093/hr/uhac017)）。这些谱系名称比 RepeatMasker 的超家族命中更精细，适用于能够检测到编码结构域的 LTR。TEsorter 也可给部分 TIR 超家族和 Helitron 打上结构域标签，具体覆盖范围仍为 [待确认]。分类器只给 consensus 命名，不能代替修剪，也不能用 `all.cls.lib` 替换 working FASTA。

Jaillon 等人（2007，[doi:10.1038/nature06148](https://doi.org/10.1038/nature06148)）是首篇葡萄基因组论文，此处仅作背景引用。原文写的是 “41.4% (average value) of the grapevine genome is composed of repetitive/transposable elements”，这是三种方法的平均值，也是重复序列与转座元件的合计，不是单纯的 TE 占比，也不是当前注释的数值。
<!-- /PROSE:SECTION:T01 -->
<a id="section-4"></a>
## 4. 序列特征

<!-- PROSE:SECTION:T02 -->
下表的典型值依据 Wicker 等人 2007，以及 Helitron 方面的 Kapitonov 和 Jurka 2001、2007。例外情况很常见。这些行用于检查 consensus，不能代替经过整理的比对。

| 类型 | 典型 TSD | 末端与边界 | 内部特征 |
|------|----------|------------|----------|
| LTR Copia（Ty1） | 常见 5 bp | LTR，末端常见 5 端 TG、3 端 CA（典型值，不是绝对的）；5 端 LTR 内侧有与 tRNA 互补的 PBS；3 端 LTR 前有 PPT | Gag、蛋白酶、整合酶、反转录酶、RNase H；整合酶通常位于 RT 之前 |
| LTR Gypsy（Ty3） | 常见 5 bp | 同样的 LTR、PBS 和 PPT 逻辑，也包括典型的 TG…CA 末端 | 同一套结构域；整合酶通常位于 RT 之后 |
| LINE | 不固定（常为数个到数十个碱基） | 无 LTR；许多家族以 polyA 或其他 3 端结尾 | 自主拷贝编码核酸内切酶和 RT |
| SINE | 不固定 | 内部有 RNA 聚合酶 III 启动子；常有 3 端 polyA；无蛋白编码框 | 非自主，依赖 LINE 机制移动 |
| TIR Tc1/Mariner | TA | 末端反向重复 | 自主拷贝有转座酶 |
| TIR hAT | 8 bp | 末端反向重复 | 自主拷贝有转座酶 |
| TIR Mutator（MuDR） | 9–11 bp [待确认] | 末端反向重复 | 自主拷贝有转座酶 |
| TIR CACTA | 2–3 bp | 末端反向重复；CACTA 一类末端 | 自主拷贝有转座酶 |
| TIR PIF/Harbinger | 3 bp | 末端反向重复 | 自主拷贝有转座酶 |
| MITE | 与其来源的 TIR 超家族相同 | 短元件，带 TIR；无转座酶 | 非自主 DNA 转座子 |
| Helitron | 通常无（常插入 AT） | 5 端 TC；3 端 CTRR 加一段短发夹 | 自主拷贝有滚环 Rep/解旋酶 |

PBS 是引物结合位点，PPT 是多嘌呤区。TSD 长度和末端基序应视为典型值而不是唯一值。若与 Wicker 2007 原表中某一少见超家族核对后不一致，相应条目仍可标为 [待确认]。
<!-- /PROSE:SECTION:T02 -->

<a id="section-5"></a>
## 5. TE 与宿主

<!-- PROSE:SECTION:T00D -->
**对基因的影响。** 新的插入可能打断编码序列、改变剪接，或落在基因旁边，影响基因何时、在何处表达。TE 也可以提供调控序列。Feschotte 等人（2002）和 Lisch（2013）综述了植物中的这些结果。并非每次插入都有影响；许多落在已经重复的区域里，并保持沉默。

**沉默。** 真核宿主拥有多层表观遗传机制来抑制 TE 的表达和移动，包括小 RNA 和 DNA 甲基化（Slotkin 和 Martienssen 2007，[doi:10.1038/nrg2072](https://doi.org/10.1038/nrg2072)）。在植物中，RNA 介导的 DNA 甲基化（RdDM）是其中的一条主要途径（Matzke 和 Mosher 2014，[doi:10.1038/nrg3683](https://doi.org/10.1038/nrg3683)）。沉默机制保护了基因组；由于 TE 会招募沉默机制，它们也会影响单个基因乃至更大染色体区域的表观遗传状态（Slotkin 和 Martienssen 2007）。

**葡萄性状的例子：果皮颜色。** Kobayashi、Goto-Yamamoto 和 Hirochika（2004，[doi:10.1126/science.1095011](https://doi.org/10.1126/science.1095011)）报道了反转录转座子诱导的葡萄果皮颜色突变；这篇短文的正文本轮没有重读，因此不从中摘取基因和元件名称。This 等人（2007，[doi:10.1007/s00122-006-0472-2](https://doi.org/10.1007/s00122-006-0472-2)）在 200 余份欧亚葡萄材料中发现，反转录元件 Gret1 插入花青素合成调控基因 *VvmybA1* 的启动子，与白果表型密切相关。仅凭这一关联，还不能证明插入本身造成了颜色变化。同一篇摘要还写到，部分有色等位基因与后来 Gret1 的“excision”（作者原词，常译作切出）相符。由于 Gret1 是 LTR 反转录转座子，它以复制粘贴方式移动，不会被转座酶切下来；这类元件的丢失通常源于两条 LTR 之间发生重组，留下一条 solo LTR。那些有色等位基因是否确实带有 solo LTR，标为 [待确认]。摘要还指出，少数情况下看不到 Gret1 与白果表型的关联，提示白果表型也可以由其他基因的突变产生。文中是在驯化后人工选择性状的背景下讨论 *VvmybA1* 的，而不是将其作为插入参与最初驯化事件的证据。

**无性繁殖作物中的体细胞变异。** 由于葡萄通常靠扦插繁殖，单个芽上的体细胞变化可以被保存成新的无性系。Azuma 等人（2009，[doi:10.1016/j.plantsci.2008.12.015](https://doi.org/10.1016/j.plantsci.2008.12.015)）研究了白果‘Italia’的芽变。关于 'Ruby Okuyama' 的颜色恢复，他们写到这“may have occurred as a result of intra-LTR recombination within a retrotransposon, Gret1”。用直白的话说，就是同一个元件的两条长末端重复之间发生重组，导致内部序列丢失，只留下一条 LTR。Azuma 2009 里的这句是在复述先前的研究；一个候选出处是 Kobayashi 等人 2005（[doi:10.2503/jjshs.74.196](https://doi.org/10.2503/jjshs.74.196)；题名已匹配，正文本轮未打开）[待确认]。同一篇 Azuma 论文自己关于 'Benitaka' 的结果则不同：一个新的 *VvmybA1*(BEN) 等位基因，被归因于 *VvmybA1a* 与 *VvmybA3* 之间的重组，而非 TE 的插入或切出。果园里 TE 造成体细胞变异的频率，以及应如何与其他突变类型一并权衡，仍标为 [待确认]。

**其他作物。** 玉米 B73 基因组（Schnable 等人 2009）是规模上的典型例子：TE 占该基因组的近 85%，并捕获了基因片段。除非本目录为此读过题名匹配的论文，这里不再列举其他作物性状的例子。
<!-- /PROSE:SECTION:T00D -->

<a id="section-6"></a>
## 6. 葡萄基因组中的 TE

<!-- PROSE:SECTION:T00E -->
**第一批基因组论文。** Jaillon 等人（2007，[doi:10.1038/nature06148](https://doi.org/10.1038/nature06148)）用接近纯合的 PN40024（由黑皮诺经多代自交选育而来）报道：“41.4% (average value) of the grapevine genome is composed of repetitive/transposable elements”。这是三种方法的平均值，属于重复序列与转座元件的合计，不是单纯的 TE 占比，也不是当前注释的数值（另见[第 3 节](#section-3)）。Velasco 等人（2007，[doi:10.1371/journal.pone.0001326](https://doi.org/10.1371/journal.pone.0001326)）组装了杂合的黑皮诺克隆，估计基因组大小为 504.6 Mb，并写到：“Homologous chromosomes of Pinot Noir differ by 11.2% of their DNA (hemizygous DNA plus chromosomal gaps)”。Velasco 的摘要里没有给出 TE 占比，这里也不另填数字。

**杂合性与单倍型。** 葡萄的两条单倍型之间可以存在较大差异，因此同一个 TE 可能只出现在其中一条单倍型上。折叠成单倍的参考基因组会掩盖这种有无差异，只从一条单倍型建库也会漏掉部分家族。这也是后来转向单倍型组装和泛基因组方法的原因之一（另见[第 7 节](#section-7)的难点说明）。

**泛基因组与有无变异。** Liu 等人（2024，[doi:10.1038/s41588-024-01967-5](https://doi.org/10.1038/s41588-024-01967-5)）用 18 套新的端粒到端粒分相组装和 11 套已发表组装，构建了图泛基因组 Grapepan v.1.0，并在 466 个品种的重测序中得到 9,105,787 个短变异和 236,449 个结构变异。他们报道平均 88.6% 的结构变异与 TE 重叠（指与 TE 重叠，而非这些变异中 TE 插入所占的比例）。要做一组材料中的 TE 有无分析，本仓库指向 panEDTA（Ou 等人 2024，[doi:10.1101/gr.278131.123](https://doi.org/10.1101/gr.278131.123)），而不是把各样本原始 EDTA 库简单拼接（见[第 9 节](#section-9)）。
<!-- /PROSE:SECTION:T00E -->
<a id="section-7"></a>
## 7. 行业难点

<!-- PROSE:SECTION:T03 -->
- **嵌套和破碎拷贝。** 新插入套进旧元件，以及退化破碎的片段，会让结构检测漏掉拷贝，也会让同源注释把一个元件拆成许多命中片段。RepeatMasker 之后可用 RepeatCraft、oneCodeToFindThemAll 做碎片合并，并在整理时检查嵌套结构。
- **新拷贝与旧拷贝。** 用 LTR-LTR 分歧度估计插入时间，只对整理之后仍然完整的年轻拷贝有意义。新插入时，两条 LTR 复制自同一模板，因此完全相同；随后的分歧度才是 T = K / (2r) 所度量的量，因为两条 LTR 各自独立积累突变。典型的 LTR 末端常为 5′-TG…CA-3′（典型特征，并非绝对；LTR_retriever 也会报告非典型末端）。插入之后，两条 LTR 之间的重组可以删掉内部区，只留下一条 LTR（solo LTR），这类元件无法用该公式定年。如果 r 的单位是每年每个位点，就不需要世代时间；若 r 是每代速率，则需先作换算。克隆作物的有性世代间隔很长，且不易确定。两条 LTR 之间的基因转换会使估出的年龄偏年轻。不要把原始 EDTA 输出里的年龄当作最终交付结果；没有明确的替换率时（若速率按代计，还需明确世代时间），不要把分歧度换算成年代。EDTA 若不设 `--u`，会静默使用水稻的 1.3e-8 /bp/年，不能当作葡萄的默认值。葡萄的 `--u` 仍为 [待确认]。
- **整理仍然是瓶颈。** TEtrimmer、MCHelper 和 Earl Grey 能自动完成部分 consensus 清理，但 trusted 文库仍需要有记录的 CDS 门控和分类输出规则。Goubert 等人 2022（[doi:10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7)）是手工整理的入门指南，不是这些工具的方法论文。
- **基因家族和串联重复造成的假阳性。** NLR 簇、其他基因家族、简单重复和串联重复可能混入 de novo 文库。TRF、端粒和 rDNA 应放在单独的非 TE 轨道，它们不属于 `--curatedlib`。
- **软屏蔽交接。** 如果基因组未屏蔽，BRAKER 和 GALBA 会把 TE 编码的 ORF 预测为基因（过度预测）。如果被硬屏蔽成 `N`，与重复区重叠的真基因会被截断或丢失（漏报）。如果用仍含宿主基因的文库做软屏蔽，这些真基因会被屏蔽，从而被漏掉（漏报）。基因软屏蔽或 EDTA `--curatedlib` 只接受当前 trusted 文库，并需注明版本和 sha256（见 [TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)）。EDTA 要求基因组序列名不超过 13 个字符（字母、数字和下划线），并保留与原名的对照表。交给 RepeatMasker `-xsmall` 之前先把基因组转成大写。文库序列名应使用 `name#Class/Family` 格式。RepeatMasker 的 `.out` 坐标是 1 起始闭区间，BED 是 0 起始半开区间。
- **泛基因组中的 TE 有无。** 在葡萄中，一次插入可能只出现在某一条单倍型上。得到 trusted 文件之后，应使用 panEDTA 合并一组文库；把原始 TElib 拼接后再跑 CD-HIT，并不能得到泛文库。
- **杂合、单倍型分相的基因组。** 按每个组装或单倍型分别做发现，不要在发现之前把单倍型塌缩。
<!-- /PROSE:SECTION:T03 -->
<a id="section-8"></a>
## 8. 按步骤划分的软件

<!-- PROSE:SECTION:T04 -->
每一行的链接、标题匹配的 DOI（如有）、输入、输出和适用场合见 [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv)。此处未锁定工具版本。

下面仅依据方法论文摘要中写明的内容，对三个工具作简短说明；尚未核对的模块名单标为 [待确认]。EDTA（Ou 等人 2019）会比较已有的 LTR 反转录转座子、TIR 转座子（包括 MITE）和 Helitron 注释程序，再把较稳健的程序组合起来，生成经过过滤、去冗余的完整与破碎元件文库，并能拆开嵌套插入。某一版 EDTA 内部具体调用哪些程序，仍需对照该论文方法部分和 EDTA 文档 [待确认]；本仓库把 LTR_retriever 作为与 EDTA 一并记录的完整 LTR 过滤器。RepeatModeler2（Flynn 等人 2020）用于 de novo 发现家族；这一版增加了完整 LTR 反转录元件的结构发现模块。本仓库的封装记录了 LTR 结构步骤（`-LTRStruct`；选项名随版本的变化仍为 [待确认]）。目录里把 RepeatScout 和 RECON 列为 RepeatModeler2 内部的 de novo 引擎。本仓库的目录记载，LTR_retriever（Ou 和 Jiang 2018）接收结构法得到的 LTR 候选并生成高质量 LTR 文库（这一输入步骤出自目录，而非出自该论文摘要）。它识别带 5′-TG…CA-3′ 末端的典型元件，也报告非典型（non-TGCA）LTR 反转录转座子。程序内部还有哪些过滤特征，在重读方法部分之前标为 [待确认]。

| 步骤 | 适用场合 | 本目录中的工具 |
|------|----------|----------------|
| de novo 发现 | 从组装或单倍型出发 | EDTA（此处默认）、RepeatModeler2、Earl Grey；家族发现还有 RepeatScout、RECON、PILER |
| 结构检测 | 寻找完整的 LTR、TIR、MITE 或 Helitron | LTR_FINDER、LTR_FINDER_parallel、LTRharvest、LTR_retriever；HelitronScanner；MITE-Hunter、detectMITE、TIR-Learner、GRF |
| 同源注释 | 用文库做注释或屏蔽 | RepeatMasker；文库为 Dfam 和 Repbase |
| 分类 | 给 working 文库贴标签 | TEsorter + REXdb（植物 LTR 谱系）；DeepTE；TEclass |
| 整理与 consensus | 把原始 consensus 变成 working 或 trusted 文库 | TEtrimmer（此处默认）、MCHelper、Goubert 指南、CD-HIT |
| 文库质控 | 去掉非 TE 重复、检查组装质量 | TRF（非 TE 轨道）；在整理后或泛注释上计算 LAI |
| 屏蔽 | 把基因组交给基因注释 | 只用 trusted 文库做 RepeatMasker `-xsmall`；用 BEDTools 检查轨道 |
| TE 年龄 / 插入时间 | 整理后的完整 LTR 对 | LTR_retriever；演示脚本 `scripts/01_ltr_insertion_age.py` |
| 多态 TE 检测 | 群体或长读插入检测，不是建库 | TEMP、RelocaTE2、xTea、Jitterbug |
| 泛基因组 TE | 一组单倍型或基因组 | panEDTA（EDTA 仓库中的 `panEDTA.sh`） |
| 可视化 / 碎片合并 | 整理同源注释 | RepeatCraft、oneCodeToFindThemAll |
<!-- /PROSE:SECTION:T04 -->
<a id="section-9"></a>
## 9. 操作流程、红线和示例脚本

公开流程仍是 `EDTA` 至 `TEtrimmer`，至 `TEsorter`，再至基于 CDS 过滤的 trusted 文库，最后用于软屏蔽或 `panEDTA`。诸如 trusted `~240` 这样的 `R1` 数字属于归档和教学示例；最终的高质量参考数据可能会更新为新版 trusted 文件。基因软屏蔽步骤（`A0`）只接受当前的 trusted 文件及其版本和 sha256，不接受原始 EDTA 输出，也不接受整个 working 文库。

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

用 Python 3 和 numpy 即可运行的演示脚本在 [`scripts/`](scripts/)。它们使用一条人工放入的 LTR 样插入，而非真实的 *Vitis* 数据。见 [`scripts/README.md`](scripts/README.md) 和 [`testdata/README.md`](testdata/README.md)。

| 脚本 | 作用 | 在构建机上的状态（2026-11-15 CST） |
|------|------|-------------------------------------|
| `00_make_tiny_genome.py` | 写入带一条人工 LTR 样插入的小 FASTA 和 BED | 已实测 |
| `01_ltr_insertion_age.py` | 计算两条 LTR 的 p 距离和 K2P；只有提供 `--rate` 时才给年份（无默认速率）；T = K/(2r) | 已实测 |
| `02_softmask.py` | 把 BED 区间改成小写（软屏蔽演示） | 已实测 |
| `03_run_edta.sh` | 记录上面的 EDTA 命令 | 未实测（仅 `--dry-run` / `--help`） |
| `04_run_repeatmodeler_repeatmasker.sh` | 记录 RepeatModeler2 和 RepeatMasker `-xsmall` | 未实测（仅 `--dry-run` / `--help`） |
| `05_run_tesorter.sh` | 记录 TEsorter（rexdb-plant）和 all.cls.lib 规则 | 未实测（仅 `--dry-run` / `--help`） |
| `run_toy_pipeline.sh` | 运行上面三个已实测的 Python 脚本 | 已实测 |

```bash
bash scripts/run_toy_pipeline.sh OUTDIR
```

<a id="section-10"></a>
## 10. 术语表

<!-- PROSE:SECTION:T00F -->
- **转座元件（TE）。** 能够移动或把自己复制到基因组新位置的 DNA 序列；许多拷贝后来会失去这种能力。
- **第 I 类 / 反转录转座子。** 通过 RNA 中间体移动的元件（复制粘贴）。
- **第 II 类 / DNA 转座子。** 通过 DNA 中间体移动的元件。许多采用剪切粘贴；Helitron 和 Maverick 另归为 subclass 2。
- **LTR。** 长末端重复，LTR 反转录转座子两端的正向重复。
- **Solo LTR。** 同一个元件的两条 LTR 之间发生重组、内部区被删掉后留下的单条 LTR。Solo LTR 不能用 T = K/(2r) 定年。
- **TIR。** 末端反向重复，剪切粘贴 DNA 转座子的典型结构。
- **TSD。** 靶位点重复，插入位点两侧复制出的短序列。
- **PBS / PPT。** 引物结合位点和多嘌呤区，位于 LTR 内侧的标志结构。
- **MITE。** 短的、非自主的 TIR 元件。
- **自主 / 非自主。** 元件是否自己编码移动所需的蛋白，或依赖其他元件提供。
- **80-80-80 规则。** Wicker 的家族标准：在编码区或内部区，或末端重复区，至少 80% 一致、覆盖至少 80%，并且至少 80 bp。
- **软屏蔽 / 硬屏蔽。** 软屏蔽把重复区写成小写，碱基仍可读；硬屏蔽替换成 N。本仓库在基因注释中只用软屏蔽。
- **RdDM。** RNA 介导的 DNA 甲基化，植物中沉默 TE 的一条途径。
- **C 值。** 单倍基因组的 DNA 量，在不同生物之间差异很大。
- **自私 DNA。** 有些 DNA 仅凭在基因组里复制的能力就能扩散，不必对生物体有利（Doolittle 和 Sapienza 1980；Orgel 和 Crick 1980）。后来的回复见 Orgel、Crick 和 Sapienza 1980。
- **杂交衰退（hybrid dysgenesis，中文定名 [待确认]）。** 某些果蝇杂交后代出现不育和突变的综合征，在 P-M 系统中由 P 元件引起。
- **Gret1 / VvmybA1。** 花青素调控基因 *VvmybA1* 启动子中的反转录转座子插入，与葡萄白果相关（This 等人 2007）。
- **PAV。** 有无变异，包括在不同单倍型或品种之间有无的 TE 插入。
<!-- /PROSE:SECTION:T00F -->

## 参考

目录条目和 DOI 见 [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv)。基因注释交接见 [TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)。

作者：李旭振，[ORCID](https://orcid.org/0000-0003-3670-6657)
