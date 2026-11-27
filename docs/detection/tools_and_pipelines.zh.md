# 工具、主流流程和行业难点

这一章扩展 2026-11-15 那版 README 里较短的软件表，并补上 2024–2026 年的工具。已经审过的 EDTA、RepeatModeler2 和 LTR_retriever 说明放在前面，新工具另表列出。

![F8 流程](../../figures/F8_pipeline.svg)

## 公认的行业难点

从 2026-11-15 README 第 7 节搬来，科学表述不改。软屏蔽交接的链接改为指向 [softmask_handoff.zh.md](softmask_handoff.zh.md)，而不再指向计划从 gene-structure-annotation 撤下的 `TE_LIBRARY.md`。

<!-- PROSE:SECTION:T03 -->
- **嵌套和破碎拷贝。** 新插入套进旧元件，以及退化破碎的片段，会让结构检测漏掉拷贝，也会让同源注释把一个元件拆成许多命中片段。RepeatMasker 之后可用 [RepeatCraft](https://github.com/niccw/repeatcraftp)、[oneCodeToFindThemAll](https://doua.prabi.fr/software/one-code-to-find-them-all) 做碎片合并，并在整理时检查嵌套结构。
- **新拷贝与旧拷贝。** 用 LTR-LTR 分歧度估计插入时间，只对整理之后仍然完整的年轻拷贝有意义。新插入时，两条 LTR 复制自同一模板，因此完全相同（Neumann 等 2019，[doi:10.1186/s13100-018-0144-1](https://doi.org/10.1186/s13100-018-0144-1)，全文：“Since the 5′ LTR and 3′ LTR are identical at the time of insertion of a new element copy to the genome the level of their divergence which is caused by mutations acquired over time is proportional to the insertion age.”）；随后的分歧度才是 T = K / (2r) 所度量的量，因为两条 LTR 各自独立积累突变。典型的 LTR 末端常为 5′-TG…CA-3′（典型特征，并非绝对；LTR_retriever 也会报告非典型末端）。插入之后，两条 LTR 之间的重组可以删掉内部区，只留下一条 LTR（solo LTR），这类元件无法用该公式定年。如果 r 的单位是每年每个位点，就不需要世代时间；若 r 是每代速率，则需先作换算。克隆作物的有性世代间隔很长，且不易确定。两条 LTR 之间的基因转换会使估出的年龄偏年轻，这一说法仍标 **[待确认]**（已打开的 Neumann 2019 全文和 SanMiguel 1998 摘要中未见）。不要把原始 EDTA 输出里的年龄当作最终交付结果；没有明确的替换率时（若速率按代计，还需明确世代时间），不要把分歧度换算成年代。EDTA 若不设 `--u`，会静默使用水稻的 1.3e-8 /bp/年，不能当作葡萄的默认值。葡萄的 `--u` 仍为 [待确认]。
- **整理仍然是瓶颈。** TEtrimmer、MCHelper 和 Earl Grey 能自动完成部分 consensus 清理，但 trusted 文库仍需要有记录的 CDS 门控和分类输出规则。Goubert 等人 2022（[doi:10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7)）是手工整理的入门指南，不是这些工具的方法论文。
- **基因家族和串联重复造成的假阳性。** NLR 簇、其他基因家族、简单重复和串联重复可能混入 de novo 文库。TRF、端粒和 rDNA 应放在单独的非 TE 轨道，它们不属于 `--curatedlib`。
- **软屏蔽交接。** BRAKER 的 README 写：基因组应当做重复序列屏蔽，并原话说 “This will avoid the prediction of false positive gene structures in repetitive and low complexitiy regions.”；对 GeneMark 和 AUGUSTUS，softmasking “leads to better results than hardmasking”。硬屏蔽成 `N` 会使重叠基因被截断或丢失，是本仓库的推断 **[待确认]**。基因软屏蔽或 EDTA `--curatedlib` 只接受当前 trusted 文库，并需注明版本和 sha256（见 [softmask_handoff.zh.md](softmask_handoff.zh.md)）。EDTA 要求基因组序列名不超过 13 个字符（字母、数字和下划线），并保留与原名的对照表。交给 RepeatMasker `-xsmall` 之前先把基因组转成大写（本仓库的防御性约定：`-xsmall` 把被屏蔽碱基写成小写，不能把原有小写误当成屏蔽；RepeatMasker 帮助页说明了 `-xsmall`，但并不要求事先转大写）。文库序列名应使用 `name#Class/Family` 格式。本仓库目前把 RepeatMasker 的 `.out` 当作 1 起始闭区间、把 BED 当作 0 起始半开区间；已打开的帮助页未写明该约定，标 **[待确认]**。
- **泛基因组中的 TE 有无。** 在葡萄中，一次插入可能只出现在某一条单倍型上。得到 trusted 文件之后，应使用 panEDTA 合并一组文库；把原始 TElib 拼接后再跑 CD-HIT，并不能得到泛文库。
- **杂合、单倍型分相的基因组。** 按每个组装或单倍型分别做发现，不要在发现之前把单倍型塌缩。

## EDTA、RepeatModeler2 和 LTR_retriever 说明

从同一 README 的第 8 节搬来：

<!-- PROSE:SECTION:T04 -->
每一行的链接、标题匹配的 DOI（如有）、输入、输出和适用场合见 [`catalog/CATALOG.tsv`](../../catalog/CATALOG.tsv)。此处未锁定工具版本。

下面依据已打开的全文或官方 README，对三个工具作简短说明。EDTA（Ou 等 2019，全文，[doi:10.1186/s13059-019-1905-y](https://doi.org/10.1186/s13059-019-1905-y)）“incorporates LTRharvest, the parallel version of LTR_FINDER, LTR_retriever, GRF, TIR-Learner, HelitronScanner，”再把较稳健的结果组合成经过过滤、去冗余的完整与破碎元件文库，并能拆开嵌套插入。RepeatModeler2（Flynn 等 2020）用于 de novo 发现家族；官方 README 写明内部有 RECON、RepeatScout 和 LtrHarvest/Ltr_retriever，并记录 `-LTRStruct` 开关。LTR_retriever（Ou 与 Jiang 2018；官方 README）接收来自 LTRharvest 或 LTR_FINDER 的结构 LTR-RT 候选，构建高质量 LTR 文库；识别典型的 5′-TG…CA-3′ 末端，也报告非典型（非 TGCA）LTR 反转录转座子。

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
<!-- /PROSE:SECTION:T04 -->

## 操作流程和红线

从第 9 节搬来。推荐路线仍然是 EDTA → TEtrimmer → TEsorter → 经 CDS 门控的 trusted 文库 → 软屏蔽或 panEDTA。R1 trusted ~240 仍属于归档和教学。

公开流程仍是 `EDTA` 至 `TEtrimmer`，至 `TEsorter`，再至基于 CDS 过滤的 trusted 文库，最后用于软屏蔽或 `panEDTA`。诸如 trusted `~240` 这样的 `R1` 数字属于归档和教学示例；最终的高质量参考数据可能会更新为新版 trusted 文件。基因软屏蔽步骤（`A0`）只接受当前的 trusted 文件及其版本和 sha256，不接受原始 EDTA 输出，也不接受整个 working 文库。

1. 针对每个组装或单倍型运行 `EDTA`，使用 `--species others --sensitive 1 --anno 1`，并显式设定 `--u`、记录其来源。葡萄的 `--u` 仍为 [待确认]；若不设 `--u`，EDTA 会静默使用水稻的 1.3e-8 /bp/年，不能当作葡萄的默认值。
2. 针对每个单倍型运行 `TEtrimmer`，合并 Perfect 与 Good 序列，并用 `CD-HIT` 生成相似度约 95% 的 working 文库。可以按需生成 80-80 阈值的家族目录，但不要覆盖 working 文库。
3. 使用 `TEsorter`（如 `rexdb-plant`）只分配结构域和标签。不要用 `all.cls.lib` 替换 working FASTA（本仓库的 `all.cls.lib` 指对 `all.fa` 运行 TEsorter 时的文件名；官方 README 的输出是 `<input>.rexdb.cls.lib`）。
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

## 较新的流程和分类器（2024–2026，题名已匹配）

这些工具没有写进那版短 README。下面每个 DOI 都在新增的 Crossref 题名匹配中核对过（见目录中的 `DOI_CHECKS.tsv`）。它们是替代或补充，不是悄悄替换红线流程。

| 工具 | 论文（官方题名，年份） | DOI | 用途 | 和上面路线的关系 |
|------|------------------------|-----|------|------------------|
| [HiTE](https://github.com/CSU-KangHu/HiTE) | *HiTE: a fast and accurate dynamic boundary adjustment approach for full-length transposable element detection and annotation*（2024） | [10.1038/s41467-024-49912-8](https://doi.org/10.1038/s41467-024-49912-8) | 全长 TE 检测；HiTE README 的输出列出 confident TIR、Helitron 和 non-LTR 鉴定结果（以及 LTR 相关输出） | 并列的 de novo 建库工具；2026-11-15 记录的检查中未测 |
| Earl Grey | 已在旧目录中 | [10.1093/molbev/msae068](https://doi.org/10.1093/molbev/msae068) | 自动注释和整理，并给出论文风格的汇总图 | 并列流程。软屏蔽基因组 FASTA 是 Earl Grey 的可选项（README 里 `-d` / soft-mask，默认 no），没有 CDS 门控时不能代替 trusted 文库 |
| TEtrimmer | 已在旧目录中 | [10.1038/s41467-025-63889-y](https://doi.org/10.1038/s41467-025-63889-y) | 自动完成手工整理 consensus 的若干步骤 | 上面路线里的默认修剪工具 |
| [DANTE](https://github.com/kavonrtep/dante) / [DANTE_LTR](https://github.com/kavonrtep/dante_ltr) | *DANTE and DANTE_LTR: lineage-centric annotation pipelines for long terminal repeat retrotransposons in plant genomes*（2024） | [10.1093/nargab/lqae113](https://doi.org/10.1093/nargab/lqae113) | 植物 LTR 的谱系注释 | 补充 TEsorter/REXdb；不代替 trusted 门控 |
| [GraffiTE](https://github.com/cgroza/GraffiTE) | *A unified framework to analyze transposable element insertion polymorphisms using graph genomes*（2024） | [10.1038/s41467-024-53294-2](https://doi.org/10.1038/s41467-024-53294-2) | 在图上分析 TE 插入多态，可从组装或长读出发再分型 | 文库之后的下游分析，不是建库工具。2024 年论文描述的是 v1.0；当前 README 默认是 1.1（标志、默认值和输出文件有改动；`--reads` 已改名为 `--genotype_with`）。要复现论文，README 指向 `-r v1.0.0.0`。交叉见 vitis-pangenome 和 VOD 项目 14 |
| panEDTA | Crossref 官方题名为 *Differences in activity and stability drive transposable element variation in tropical and temperate maize*（2024）。该文介绍了 panEDTA。 | [10.1101/gr.278131.123](https://doi.org/10.1101/gr.278131.123) | 在泛基因组面板上做一致的 TE 注释 | 已是上面路线里的面板合并步骤 |
| [TEclass2](https://github.com/IOB-Muenster/TEclass2) | *Transformer-Based Classification of Transposable Element Consensus Sequences with TEclass2*（2025） | [10.3390/biology15010059](https://doi.org/10.3390/biology15010059) | 用 Transformer 给 consensus 分类 | 只贴标签 |
| Terrier | *Terrier: a deep learning repeat classifier*（2025） | [10.1093/bib/bbaf442](https://doi.org/10.1093/bib/bbaf442) | 深度学习重复分类器 | 只贴标签 |
| CREATE | *CREATE: a novel attention-based framework for efficient classification of transposable elements*（2025） | [10.1093/bib/bbaf608](https://doi.org/10.1093/bib/bbaf608) | 基于注意力机制的 TE 分类 | 只贴标签 |
| [DeepHel](https://github.com/lyysxb/DeepHel) | *DeepHel: improving the accuracy and completeness of Helitron annotation with a multi-stage deep learning framework*（2026） | [10.1093/bioinformatics/btag817](https://doi.org/10.1093/bioinformatics/btag817) | Helitron 注释 | 与 HelitronScanner 并列；仍要整理 |
| [ColabCuraTE](https://github.com/Ellison-Lab/ColabCuraTE) | *ColabCuraTE: an easy-to-use, web-based pipeline for the manual curation of transposable elements*（2025） | [10.1186/s13100-025-00389-2](https://doi.org/10.1186/s13100-025-00389-2) | 浏览器里做手工整理 | 补充 TEtrimmer 和 Goubert 2022 指南 |
| TE_Bench | *TE_Bench: a foundational benchmarking workflow for transposable element annotation pipelines*（2026） | [10.1186/s13100-026-00405-z](https://doi.org/10.1186/s13100-026-00405-z) | 比较 EDTA、RepeatModeler2 和 Earl Grey | 在默认配置下，RepeatModeler2 与 Earl Grey 表现相近，并优于默认 EDTA（摘要）。用来比较工具；不要复制其插图。若重绘，只能用表中数字，并注明出处 |
| [panHiTE](https://github.com/CSU-KangHu/HiTE) | *panHiTE: A comprehensive and accurate pipeline for TE detection in large-scale population genomes*（2026） | [10.1016/j.xplc.2025.101669](https://doi.org/10.1016/j.xplc.2025.101669) | 在群体基因组上检测 TE（Plant Commun 2026，doi:10.1016/j.xplc.2025.101669；HiTE README 同时列出预印本 doi:10.1101/2025.02.15.638472） | 与 panEDTA 并列；此处未运行 |

只做分类的工具只给 consensus 命名，不能取代修剪，也不能直接作为最终文库。

## 2026-11-15 记录的检查中仍未实测的软件

`scripts/` 里已有的封装（`03_run_edta.sh`、`04_run_repeatmodeler_repeatmasker.sh`、`05_run_tesorter.sh`）只记录命令，并且仍像 2026-11-15 那次合并一样，只做了 `--dry-run` / `--help`。上表新工具没有安装，也没有运行。不要把本章当成基准测试。

## 新增七个工具的摘要依据

这七行的题名已经按官方题名写出。对应的摘要原句见英文版同一节，摘要于 2026-11-15 CST 在 EuropePMC 打开。它们都不是上面默认路线里的步骤。英文版同节每条摘要后的短评是本仓库判断，不是摘要原句。ColabCuraTE 在英文版改引了摘要里描述功能的一句（基于 EuropePMC 摘要于 2026-11-15 CST 重读）。


## 按分析步骤增补的软件与数据库

本节是对上文表格的补充，不改变默认的 EDTA 路线。每一条都有已打开的论文 DOI，或已打开且返回成功的官方代码/数据入口。

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
|  | **SINE-Finder** | 论文中给出的工具，用于定向发现植物基因组中源自 tRNA 的 SINE。截至 2026-11-24 CST 未确认到仍可访问的官方代码仓库。 | — | [10.1105/tpc.111.088682](https://doi.org/10.1105/tpc.111.088682) |
|  | **LtrDetector** | LTR 反转录转座子的从头检测工具。当前仓库由 TulsaBioinformaticsToolsmith/LtrDetector 重定向而来。 | [github.com/BioinformaticsToolsmith/LtrDetector](https://github.com/BioinformaticsToolsmith/LtrDetector) | [10.1186/s12864-019-5796-9](https://doi.org/10.1186/s12864-019-5796-9) |
|  | **MUSTv2** | 改进的近期活跃 MITE 从头检测程序。截至 2026-11-24 CST 未确认到仍可访问的官方代码仓库。 | — | [10.1515/jib-2017-0029](https://doi.org/10.1515/jib-2017-0029) |
|  | **LTRdigest** | 注释候选 LTR 反转录转座子的内部特征（蛋白结构域、PBS 和 PPT）。与 LTRharvest 同属 GenomeTools。 | [github.com/genometools/genometools](https://github.com/genometools/genometools) | [10.1093/nar/gkp759](https://doi.org/10.1093/nar/gkp759) |
|  | **LTRpred** | 用于完整 LTR 反转录转座子从头注释的 R 包。当前仓库由 HajkD/LTRpred 重定向到 drostlab/LTRpred。 | [github.com/drostlab/LTRpred](https://github.com/drostlab/LTRpred) | [10.21105/joss.02170](https://doi.org/10.21105/joss.02170) |
|  | **MGEScan** | 官方说明中介绍的 Galaxy 系统，用于识别 LTR 与非 LTR 反转录转座子。 | [github.com/MGEScan/mgescan](https://github.com/MGEScan/mgescan) | — |
|  | **Red** | 无需预先文库、在全基因组尺度上从头检测重复 DNA 的工具。 | [github.com/BioinformaticsToolsmith/Red](https://github.com/BioinformaticsToolsmith/Red) | [10.1186/s12859-015-0654-5](https://doi.org/10.1186/s12859-015-0654-5) |
|  | **EDTA-GUI** | 面向植物的 EDTA 图形界面实现，并提供谱系级分类。截至 2026-11-24 CST 未确认到官方代码仓库。 | [github.com/Marcos-Fernando/EDTA-GUI](https://github.com/Marcos-Fernando/EDTA-GUI) | [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) |
|  | **Tephra** | 从基因组组装发现转座子家族并描述其结构与演化的命令行流程，不必预先提供参考文库。官方说明中的引用是该仓库本身；截至 2026-11-25 CST 未使用题名匹配的期刊论文。 | [github.com/sestaton/tephra](https://github.com/sestaton/tephra) | — |
|  | **Transposome** | 从未组装的双端全基因组鸟枪法读段注释转座子家族。 | [github.com/sestaton/Transposome](https://github.com/sestaton/Transposome) | [10.1093/bioinformatics/btv059](https://doi.org/10.1093/bioinformatics/btv059) |
|  | **CARP** | 综合从头重复序列流程，用于在基因组组装中识别、聚类并注释转座子和片段重复。截至 2026-11-25 CST 未找到返回 HTTP 200 的官方代码仓库。 | [github.com/carp-te/carp-documentation](https://github.com/carp-te/carp-documentation) | [10.1371/journal.pone.0193588](https://doi.org/10.1371/journal.pone.0193588) |
|  | **MegaLTR** | 用于在植物基因组中检测完整 LTR 反转录转座子并计算 LTR 组装指数的网页服务与本地流程。截至 2026-11-25 CST 未能成功打开配套网页服务；GitHub 仓库已打开。 | [github.com/MoradMMokhtar/MegaLTR](https://github.com/MoradMMokhtar/MegaLTR) | [10.3389/fpls.2023.1237426](https://doi.org/10.3389/fpls.2023.1237426) |
|  | **TE-greedy-nester** | 基于结构检测 LTR 反转录转座子，并重建其嵌套顺序。 | [gitlab.fi.muni.cz/lexa/nested](https://gitlab.fi.muni.cz/lexa/nested) | [10.1093/bioinformatics/btaa632](https://doi.org/10.1093/bioinformatics/btaa632) |
|  | **PhyLTR** | 官方说明中用于 LTR 反转录转座子系统发育分析的流程。已确认 Zenodo 软件记录；截至 2026-11-25 CST 未使用另外题名匹配的期刊论文。 | [github.com/mcsimenc/PhyLTR](https://github.com/mcsimenc/PhyLTR) | [10.5281/zenodo.4256534](https://doi.org/10.5281/zenodo.4256534) |
|  | **TAREAN** | 从未组装短读识别并刻画卫星 DNA 的工具，可通过 RepeatExplorer 的 Galaxy 服务使用。RepeatExplorer2 本身已单独列出。 | [repeatexplorer-elixir.cerit-sc.cz/galaxy/](https://repeatexplorer-elixir.cerit-sc.cz/galaxy/) | [10.1093/nar/gkx257](https://doi.org/10.1093/nar/gkx257) |
|  | **CLARI-TE** | 官方说明中用于小麦等复杂基因组转座子注释的脚本。截至 2026-11-25 CST 未确认到题名匹配的期刊论文。 | [github.com/jdaron/CLARI-TE](https://github.com/jdaron/CLARI-TE) | — |
|  | **Dfam TETools** | Dfam 联盟维护的容器，提供可运行的 RepeatMasker 与 RepeatModeler 安装。它封装的是本目录中已有的工具，本身不是新的注释器。 | [github.com/Dfam-consortium/TETools](https://github.com/Dfam-consortium/TETools) | — |
|  | **PanTE** | 泛基因组转座子注释流程，按官方说明和题名匹配的预印本，把多条互补的从头检测路径合并为分类文库。 | [github.com/unavailable-2374/Pan_TE](https://github.com/unavailable-2374/Pan_TE) | [10.21203/rs.3.rs-5867196/v1](https://doi.org/10.21203/rs.3.rs-5867196/v1) |
|  | **ParTEA** | Earl Grey 泛基因组流程（ParTEA），用于在多个基因组间保持一致的转座子注释。Earl Grey 本身已单独列出。 | [github.com/TobyBaril/EarlGreyParTEA](https://github.com/TobyBaril/EarlGreyParTEA) | [10.64898/2026.11.04.764261](https://doi.org/10.64898/2026.11.04.764261) |
|  | **MAKER-P** | 植物基因注释工具包，不是转座子注释器。在注释植物基因组时可使用重复序列文库。截至 2026-11-25 CST 未找到返回 HTTP 200 的 MAKER-P 官方页面；未把通用 MAKER 仓库当作 MAKER-P 主页。 | [yandell-lab.org/software/maker-p/](https://yandell-lab.org/software/maker-p/) | [10.1104/pp.113.230144](https://doi.org/10.1104/pp.113.230144) |
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
|  | **PoPoolationTE2** | 用 Pool-Seq 数据比较转座子插入多态。截至 2026-11-24 CST 未确认到仍可访问的官方仓库。 | — | [10.1093/molbev/msw137](https://doi.org/10.1093/molbev/msw137) |
|  | **RetroSeq** | 用 Illumina 双端全基因组测序检测非参考转座子插入。 | [github.com/tk2/RetroSeq](https://github.com/tk2/RetroSeq) | [10.1093/bioinformatics/bts697](https://doi.org/10.1093/bioinformatics/bts697) |
|  | **TEFLoN** | 用短读发现转座子插入与缺失并估计速率。官方说明引用该论文，但论文题名中不含工具名。 | [github.com/jradrion/TEFLoN](https://github.com/jradrion/TEFLoN) | [10.1093/gbe/evx050](https://doi.org/10.1093/gbe/evx050) |
|  | **T-lex3** | 用短读对参考转座子插入分型，并估计群体频率。 | [github.com/GonzalezLab/T-lex3](https://github.com/GonzalezLab/T-lex3) | [10.1093/bioinformatics/btz727](https://doi.org/10.1093/bioinformatics/btz727) |
|  | **ngs_te_mapper2** | 用短读取检测转座子插入，包含分裂读支持。官方说明称方法见该 Genetics 论文。 | [github.com/bergmanlab/ngs_te_mapper2](https://github.com/bergmanlab/ngs_te_mapper2) | [10.1093/genetics/iyab113](https://doi.org/10.1093/genetics/iyab113) |
|  | **Mobster** | 用不一致读对和分裂读从高通量测序数据中检测可移动元件插入。 | [github.com/jyhehir/mobster](https://github.com/jyhehir/mobster) | [10.1186/s13059-014-0488-x](https://doi.org/10.1186/s13059-014-0488-x) |
|  | **TE-locate** | 用双端短读定位非参考转座子插入。截至 2026-11-24 CST 未匹配到方法论文 DOI。 | [sourceforge.net/projects/te-locate](https://sourceforge.net/projects/te-locate/) | — |
|  | **TRACKPOSON** | 官方说明中介绍的流程，用于检测转座子插入多态并生成有无矩阵。 | [github.com/Markestine/TRACKPOSON](https://github.com/Markestine/TRACKPOSON) | — |
|  | **TrEMOLO** | 结合组装与比对，用长读取估计转座子等位频率。 | [github.com/DrosophilaGenomeEvolution/TrEMOLO](https://github.com/DrosophilaGenomeEvolution/TrEMOLO) | [10.1186/s13059-023-02911-2](https://doi.org/10.1186/s13059-023-02911-2) |
|  | **PALMER** | 用长读取检测非参考可移动元件插入。官方说明将该论文列为一作方法文献。 | [github.com/WeichenZhou/PALMER](https://github.com/WeichenZhou/PALMER) | [10.1093/nar/gkz1173](https://doi.org/10.1093/nar/gkz1173) |
|  | **LoRTE** | 用低覆盖度 PacBio 长读取检测转座子引起的变异。截至 2026-11-24 CST 未找到返回 HTTP 200 的官方代码仓库。 | — | [10.1186/s13100-017-0088-x](https://doi.org/10.1186/s13100-017-0088-x) |
|  | **rMETL** | 通过对长读重新比对来检测可移动元件插入。 | [github.com/tjiangHIT/rMETL](https://github.com/tjiangHIT/rMETL) | [10.1093/bioinformatics/btz106](https://doi.org/10.1093/bioinformatics/btz106) |
|  | **sTELLeR** | 从长读基因组快速检测转座子插入，并输出 VCF。 | [github.com/kristinebilgrav/sTELLeR](https://github.com/kristinebilgrav/sTELLeR) | [10.1093/bioinformatics/btae686](https://doi.org/10.1093/bioinformatics/btae686) |
|  | **TELR** | 用长读取检测非参考转座子插入，并对插入序列做局部组装。官方说明引用该论文。 | [github.com/bergmanlab/telr](https://github.com/bergmanlab/telr) | [10.1093/nar/gkac794](https://doi.org/10.1093/nar/gkac794) |
|  | **somrit** | 用于从长读取识别并分析体细胞反转录转座子插入的工具包。 | [github.com/adcosta17/somrit](https://github.com/adcosta17/somrit) | [10.1101/2023.08.06.552193](https://doi.org/10.1101/2023.08.06.552193) |
|  | **SVAN** | 按官方说明，对序列已解析的插入与缺失（包括可移动元件插入）做注释和分类。截至 2026-11-25 CST 未挂接题名匹配的方法学 DOI。 | [github.com/REPBIO-LAB/SVAN](https://github.com/REPBIO-LAB/SVAN) | — |
|  | **MEIGA-PAV** | 按官方说明，在已解析序列的结构变异 VCF 中注释可移动元件插入。 | [github.com/MEIGA-tk/MEIGA-PAV](https://github.com/MEIGA-tk/MEIGA-PAV) | — |
|  | **panREPET** | 无需参考基因组即可检测泛基因组中共有转座子插入的流程，用于回溯一个物种内的插入动态。 | [forgemia.inra.fr/urgi-anagen/panREPET](https://forgemia.inra.fr/urgi-anagen/panREPET) | [10.1186/s13059-026-03984-5](https://doi.org/10.1186/s13059-026-03984-5) |
|  | **pantera** | 从泛基因组变异图中的多态性识别转座子家族。 | [github.com/piosierra/pantera](https://github.com/piosierra/pantera) | [10.1186/s13100-024-00323-y](https://doi.org/10.1186/s13100-024-00323-y) |
|  | **Pannagram** | 按题名匹配的预印本和官方说明，做泛基因组比对并呼叫活动组。是通用泛基因组工具，不只是转座子注释器。 | [github.com/iganna/pannagram](https://github.com/iganna/pannagram) | [10.1101/2025.02.07.637071](https://doi.org/10.1101/2025.02.07.637071) |
|  | **PanGenie** | 针对泛基因组图中各类变异的短读分型工具。通用工具，不是转座子注释器。 | [github.com/eblerjana/pangenie](https://github.com/eblerjana/pangenie) | [10.1038/s41588-022-01043-w](https://doi.org/10.1038/s41588-022-01043-w) |
|  | **Paragraph** | 面向短读数据的图结构变异分型工具。通用工具，不是转座子注释器。此处使用已发表 DOI。 | [github.com/Illumina/paragraph](https://github.com/Illumina/paragraph) | [10.1186/s13059-019-1909-7](https://doi.org/10.1186/s13059-019-1909-7) |
|  | **SyRI** | 从全基因组组装中识别共线与重排区域以及局部序列差异。通用工具，不是转座子注释器。此处使用已发表 DOI，而非预印本。 | [github.com/schneebergerlab/syri](https://github.com/schneebergerlab/syri) | [10.1186/s13059-019-1911-0](https://doi.org/10.1186/s13059-019-1911-0) |
|  | **MEGAnE** | Mobile Element Genotyping Analysis Environment：按官方说明，从短读全基因组数据识别并为多态可移动元件分型。官方说明引用该预印本；预印本题名未使用工具名。 | [github.com/shohei-kojima/MEGAnE](https://github.com/shohei-kojima/MEGAnE) | [10.1101/2022.03.25.485726](https://doi.org/10.1101/2022.03.25.485726) |
|  | **TEfinder** | 利用双端测序中的不一致读段检测新的转座子插入的流程。 | [github.com/VistaSohrab/TEfinder](https://github.com/VistaSohrab/TEfinder) | [10.3390/genes12020224](https://doi.org/10.3390/genes12020224) |
|  | **ITIS** | 从二代测序数据识别转座子插入位点的工具。截至 2026-11-25 CST 未能成功打开论文中的网站。 | [web.archive.org snapshot of bioinformatics.psc.ac.cn/software/ITIS](https://web.archive.org/web/20160825205722/http://bioinformatics.psc.ac.cn:80/software/ITIS/) | [10.1186/s12859-015-0507-2](https://doi.org/10.1186/s12859-015-0507-2) |
|  | **TE-Tracker** | 从全基因组重测序系统识别转座事件。截至 2026-11-25 CST 未确认到官方代码仓库。 | [web.archive.org snapshot of genoscope.cns.fr/externe/tetracker](https://web.archive.org/web/20170813054646/http://www.genoscope.cns.fr:80/externe/tetracker/) | [10.1186/s12859-014-0377-z](https://doi.org/10.1186/s12859-014-0377-z) |
|  | **ELITE** | Efficiently Locating Insertions of Transposable Elements，一篇 ACM 方法论文。截至 2026-11-25 CST 未确认到官方代码仓库。 | [github.com/Anwica/ELITE](https://github.com/Anwica/ELITE) | [10.1145/3307339.3342182](https://doi.org/10.1145/3307339.3342182) |
|  | **TIF** | Transposon Insertion Finder：从短读数据检测新生转座并报告插入位置的程序，不依赖已有的转座子文库。 | [github.com/akiomiyao/tif](https://github.com/akiomiyao/tif) | [10.1186/1471-2105-15-71](https://doi.org/10.1186/1471-2105-15-71) |
|  | **TEF** | Transposable Element Finder：通用的活性转座子检测程序，通过比较两个样本、或一个样本与参考基因组，利用接合读段或靶位点重复证据寻找活跃转座。 | [github.com/akiomiyao/tef](https://github.com/akiomiyao/tef) | [10.1186/s12859-022-05011-3](https://doi.org/10.1186/s12859-022-05011-3) |
|  | **ITIPs** | 在白菜（Brassica rapa）泛基因组中检测转座子插入多态的流程，依赖 smartie-sv 和 bwa。 | [github.com/caixu0518/ITIPs](https://github.com/caixu0518/ITIPs) | [10.1111/pbi.13807](https://doi.org/10.1111/pbi.13807) |
|  | **RTRIP** | 约 3,000 份水稻种质的转座子插入多态目录，并附有分析脚本。论文中的网站目前无法打开；已打开一份存档的官方页面。 | [web.archive.org snapshot of RTRIP](https://web.archive.org/web/20240226054850/http://ibi.zju.edu.cn/Rtrip/index.html) | [10.1111/pbi.13425](https://doi.org/10.1111/pbi.13425) |
|  | **panTEvo** | 用于在棉花泛基因组中追踪 LTR 反转录转座子动态与插入多态的流程。 | [github.com/Lcamdom/panTEvo](https://github.com/Lcamdom/panTEvo) | [10.1186/s13059-025-03837-7](https://doi.org/10.1186/s13059-025-03837-7) |
|  | **TEPEAK** | 用于在非模式物种群体中识别并刻画多态转座子的方法。不是植物专用工具。 | [github.com/ryanlayerlab/TEPEAK](https://github.com/ryanlayerlab/TEPEAK) | [10.1371/journal.pcbi.1013122](https://doi.org/10.1371/journal.pcbi.1013122) |
|  | **TypeSINE** | 从短读数据检测 SINE 插入多态。题名匹配的预印本研究对象是猪，不是植物。当前可用仓库为 github.com/mobilome/TypeSINE。 | [github.com/mobilome/TypeSINE](https://github.com/mobilome/TypeSINE) | [10.1101/2025.05.21.653756](https://doi.org/10.1101/2025.05.21.653756) |
|  | **AnchorWave** | 面向高序列多样性、广泛结构变异和全基因组复制的全基因组比对工具。不是转座子注释器；论文报告了玉米中转座子有无变异的召回情况。 | [github.com/baoxingsong/AnchorWave](https://github.com/baoxingsong/AnchorWave) | [10.1073/pnas.2113075119](https://doi.org/10.1073/pnas.2113075119) |
|  | **SVIM-asm** | 面向单倍体和二倍体基因组组装的结构变异检测工具。不是转座子注释器。 | [github.com/eldariont/svim-asm](https://github.com/eldariont/svim-asm) | [10.1093/bioinformatics/btaa1034](https://doi.org/10.1093/bioinformatics/btaa1034) |
| 转座子表达与小 RNA | **TEtranscripts** | 在批量 RNA-seq 差异表达分析中同时计入基因与转座子表达，并处理多重比对读段。 | [github.com/mhammell-laboratory/TEtranscripts](https://github.com/mhammell-laboratory/TEtranscripts) | [10.1093/bioinformatics/btv422](https://doi.org/10.1093/bioinformatics/btv422) |
|  | **TElocal** | 按座位定量转座子表达，与 TEtranscripts 出自同一实验室。 | [github.com/mhammell-laboratory/TElocal](https://github.com/mhammell-laboratory/TElocal) | — |
|  | **Telescope** | 用贝叶斯模型从 RNA-seq 按座位估计转座子表达。 | [github.com/mlbendall/telescope](https://github.com/mlbendall/telescope) | [10.1371/journal.pcbi.1006453](https://doi.org/10.1371/journal.pcbi.1006453) |
|  | **SQuIRE** | 用于分散重复序列座位级定量的 RNA-seq 端到端流程。 | [github.com/wyang17/SQuIRE](https://github.com/wyang17/SQuIRE) | [10.1093/nar/gky1301](https://doi.org/10.1093/nar/gky1301) |
|  | **SalmonTE** | 基于 Salmon 的准比对流程，用于从 RNA-seq 定量转座子表达。当前仓库重定向到 jeonglab-bcm/SalmonTE。 | [github.com/jeonglab-bcm/SalmonTE](https://github.com/jeonglab-bcm/SalmonTE) | [10.1142/9789813235533_0016](https://doi.org/10.1142/9789813235533_0016) |
|  | **scTE** | 官方说明中用于从单细胞 RNA-seq 等数据定量转座子表达。 | [github.com/JiekaiLab/scTE](https://github.com/JiekaiLab/scTE) | — |
|  | **SoloTE** | 在单细胞 RNA-seq 中按座位定量转座子表达。 | [github.com/bvaldebenitom/SoloTE](https://github.com/bvaldebenitom/SoloTE) | [10.1038/s42003-022-04020-5](https://doi.org/10.1038/s42003-022-04020-5) |
|  | **TEtools** | 统计并比较转座子表达（TEcount 与 TEdiff），并提供 Galaxy 封装。 | [github.com/l-modolo/TEtools](https://github.com/l-modolo/TEtools) | [10.1093/nar/gkw953](https://doi.org/10.1093/nar/gkw953) |
|  | **RepEnrich** | 结合唯一比对与多重比对读段，从 RNA-seq 或 ChIP-seq 估计重复序列亚家族的转录富集。截至 2026-11-24 CST 未确认到官方仓库。 | — | [10.1186/1471-2164-15-583](https://doi.org/10.1186/1471-2164-15-583) |
|  | **ShortStack** | 注释并定量小 RNA 基因，包括植物转座子沉默研究中常用的多重比对 21–24 nt siRNA。 | [github.com/MikeAxtell/ShortStack](https://github.com/MikeAxtell/ShortStack) | [10.1261/rna.035279.112](https://doi.org/10.1261/rna.035279.112) |
|  | **piPipes** | 官方说明中介绍的一套流程，用于分析多种测序数据中的 piRNA 与转座子转录本。 | [github.com/bowhan/piPipes](https://github.com/bowhan/piPipes) | — |
| 年龄、分歧度与景观 | **ParseRM** | 解析 RepeatMasker 的 .out 或 .align 文件，汇总组成、分歧度与景观。截至 2026-11-24 CST 未匹配到独立方法论文的题名。 | [github.com/4ureliek/Parsing-RepeatMasker-Outputs](https://github.com/4ureliek/Parsing-RepeatMasker-Outputs) | — |
|  | **VHICA** | Vertical and Horizontal Inheritance Consistence Analysis：通过比较转座子与宿主基因的分歧，区分垂直遗传与水平转移。 | [cran.r-project.org/package=vhica](https://cran.r-project.org/package=vhica) | [10.1093/molbev/msv341](https://doi.org/10.1093/molbev/msv341) |
|  | **REANNOTATE** | 用于重建插入历史的重复序列自动古生物学注释。截至 2026-11-25 CST 未能成功打开论文中的网站。 | [web.archive.org snapshot of bioinformatics.org/reannotate](https://web.archive.org/web/20120208050248/http://www.bioinformatics.org/reannotate/) | [10.1186/1471-2164-9-614](https://doi.org/10.1186/1471-2164-9-614) |
|  | **RepeatLandscape** | 解析 RepeatMasker 比对输出并绘制重复序列景观直方图或饼图的脚本。截至 2026-11-25 CST 未匹配到独立方法论文的题名。 | [github.com/caballero/RepeatLandscape](https://github.com/caballero/RepeatLandscape) | — |
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
|  | **TE_simu** | 按官方说明，模拟基因组序列中转座子插入、扩增与演化的脚本。截至 2026-11-25 CST 未挂接题名匹配的方法论文。 | [github.com/unavailable-2374/TE_simu](https://github.com/unavailable-2374/TE_simu) | — |
|  | **Hoen et al. 2015** | 呼吁系统评测转座子注释方法的方法学论文。这是论文，不是软件工具。 | — | [10.1186/s13100-015-0044-6](https://doi.org/10.1186/s13100-015-0044-6) |
|  | **Rishishwar et al. 2016** | 针对多态转座子检测工具的评测论文。这是论文，不是软件工具。 | — | [10.1093/bib/bbw072](https://doi.org/10.1093/bib/bbw072) |
|  | **Saha et al. 2008** | 对从头重复序列发现程序的实证比较。这是论文，不是软件工具。 | — | [10.1093/nar/gkn064](https://doi.org/10.1093/nar/gkn064) |
| 多倍体亚基因组与串联重复 | **TRASH** | Tandem Repeat Annotation and Structural Hierarchy：注释串联重复，包括卫星阵列。不是转座子注释器。 | [github.com/vlothec/TRASH](https://github.com/vlothec/TRASH) | [10.1093/bioinformatics/btad308](https://doi.org/10.1093/bioinformatics/btad308) |
|  | **SubPhaser** | 利用亚基因组特异 k-mer（主要来自转座子等重复序列）划分异源多倍体亚基因组。不是转座子注释器。 | [github.com/zhangrengang/SubPhaser](https://github.com/zhangrengang/SubPhaser) | [10.1111/nph.18173](https://doi.org/10.1111/nph.18173) |
|  | **PolyCRACKER** | 利用重复序列演化信号，在无监督条件下划分多倍体亚基因组。见到过非官方代码镜像，未将其作为官方仓库。 | [bitbucket.org/berkeleylab/jgi-polycracker](https://bitbucket.org/berkeleylab/jgi-polycracker/) | [10.1186/s12864-019-5828-5](https://doi.org/10.1186/s12864-019-5828-5) |
| 数据库与参考集 | **PlantRep** | 在数百个植物基因组中重新注释得到的植物重复序列一致性库。截至 2026-11-24 CST 未能成功打开其公开网站。 | — | [10.1007/s00299-021-02817-y](https://doi.org/10.1007/s00299-021-02817-y) |
|  | **RiTE-db** | 稻属转座子资源库。当前页面由旧的 genome.arizona.edu 地址重定向而来。 | [ava.genome.arizona.edu/cgi-bin/rite/index.cgi](https://ava.genome.arizona.edu/cgi-bin/rite/index.cgi) | [10.1186/s12864-015-1762-3](https://doi.org/10.1186/s12864-015-1762-3) |
|  | **SINEBase** | 收录真核生物 SINE 一致性序列并提供结构分析的数据库与工具。 | [sines.eimb.ru](https://sines.eimb.ru/) | [10.1093/nar/gks1263](https://doi.org/10.1093/nar/gks1263) |
|  | **SoyTEdb** | 大豆基因组转座子数据库。原域名现重定向到 SoyBase 的旧版页面。 | [legacy.soybase.org/soytedb](https://legacy.soybase.org/soytedb/) | [10.1186/1471-2164-11-113](https://doi.org/10.1186/1471-2164-11-113) |
|  | **RepetDB** | 与 REPET 项目相关的转座子参考序列统一资源。 | [urgi.versailles.inrae.fr/repetdb](https://urgi.versailles.inrae.fr/repetdb) | [10.1186/s13100-019-0150-y](https://doi.org/10.1186/s13100-019-0150-y) |
|  | **TREP** | 面向植物的人工精修转座子平台，附录B已有条目；此处补入方法目录。 | [trep-db.uzh.ch](https://trep-db.uzh.ch) | — |
|  | **HTT-DB** | 水平转移转座子数据库，另有更新说明论文。截至 2026-11-25 CST，尝试的公开网站未能成功打开。 | [web.archive.org snapshot of HTT-DB](https://web.archive.org/web/20220814084307/http://lpa.saogabriel.unipampa.edu.br:8080/httdatabase/) | [10.1093/bioinformatics/btv281](https://doi.org/10.1093/bioinformatics/btv281) |
|  | **PlantLTRdb** | 收录 195 个植物物种完整 LTR 反转录转座子的交互式数据库。 | [bioinformatics.um6p.ma/PlantLTRdb/](https://bioinformatics.um6p.ma/PlantLTRdb/) | [10.3389/fpls.2023.1134627](https://doi.org/10.3389/fpls.2023.1134627) |
|  | **DPTEdb** | 雌雄异株植物转座子综合数据库。截至 2026-11-25 CST 未能成功打开论文中的网站。 | [web.archive.org snapshot of DPTEdb](https://web.archive.org/web/20180812090334/http://genedenovoweb.ticp.net:81/DPTEdb/index.php) | [10.1093/database/baw078](https://doi.org/10.1093/database/baw078) |
|  | **SPTEdb** | 杨柳科植物转座子数据库。截至 2026-11-25 CST 未能成功打开论文中的网站。 | [web.archive.org snapshot of SPTEdb](https://web.archive.org/web/20180730000921/http://genedenovoweb.ticp.net:81/SPTEdb/index.php) | [10.1093/database/bay024](https://doi.org/10.1093/database/bay024) |
|  | **RetrOryza** | 水稻 LTR 反转录转座子数据库。截至 2026-11-25 CST，尝试的公开网站未能成功打开。 | — | [10.1093/nar/gkl780](https://doi.org/10.1093/nar/gkl780) |
|  | **TIGR Plant Repeat Databases** | 历史上用于识别植物重复序列的汇总资源。截至 2026-11-25 CST 未能成功打开原来的 TIGR 网址。 | [rice.uga.edu/pub/data/TIGR_Plant_Repeats/](https://rice.uga.edu/pub/data/TIGR_Plant_Repeats/) | [10.1093/nar/gkh099](https://doi.org/10.1093/nar/gkh099) |
|  | **ConTEdb** | 针叶树转座子综合数据库。截至 2026-11-25 CST，尝试的公开网站未能成功打开。 | [web.archive.org snapshot of ConTEdb](https://web.archive.org/web/20210921143932/http://genedenovoweb.ticp.net:81/conTEdb/index.php) | [10.1093/database/bay131](https://doi.org/10.1093/database/bay131) |
|  | **AnnoTEP-DB** | 与 EDTA-GUI 论文相关的说明与预注释基因组资源。目录中已有 EDTA-GUI 软件条目，截至 2026-11-25 CST 未改那一行。当前可用地址需要末尾斜杠。 | [plantgenomics.ncc.unesp.br/AnnoTEP-DB/](https://plantgenomics.ncc.unesp.br/AnnoTEP-DB/) | [10.1186/s12864-026-12588-z](https://doi.org/10.1186/s12864-026-12588-z) |
|  | **MaizeGP** | 开放的玉米图泛基因组平台，含结构变异目录。这是物种泛基因组资源，不是专一的转座子数据库。 | [github.com/Jia-nianhua/Maize-Graph-Pangenome](https://github.com/Jia-nianhua/Maize-Graph-Pangenome) | [10.1111/jipb.70439](https://doi.org/10.1111/jipb.70439) |
|  | **TE Hub** | 用于分享并连接转座子注释工具、数据、资源和方法的社区站点。 | [tehub.org](https://tehub.org/) | [10.1186/s13100-021-00244-0](https://doi.org/10.1186/s13100-021-00244-0) |
|  | **awesome-transposable-elements** | 公开整理的转座子研究软件、数据库和其他资源清单。这是社区索引，不是原始数据库。 | [github.com/nixonlab/awesome-transposable-elements](https://github.com/nixonlab/awesome-transposable-elements) | — |
|  | **GrapeGenomics Vitis RepeatMasker library** | 基于赤霞珠（Cabernet Sauvignon）的葡萄 RepeatMasker 自定义文库（Vitis_repeats.lib.gz），由 Cantu 实验室发布。这是可直接用于屏蔽的文库，不是可浏览检索的转座子数据库。未确认到正式的数据集 DOI。 | [grapegenomics.com/pages/repeats.php](https://grapegenomics.com/pages/repeats.php) | — |
|  | **PN40024 T2T TE annotations** | 随 PN40024 端粒到端粒基因组发布的转座子注释文件（PN_T2T_TE.gff3）。论文已在本目录中；本行只收录注释文件。 | [zenodo.org/records/13741133](https://zenodo.org/records/13741133) | [10.5281/zenodo.13741133](https://doi.org/10.5281/zenodo.13741133) |
