# 葡萄基因组中的 TE

下面各段从 2026-11-15 README 的第 6 节原文挪来。

## 6. 葡萄基因组中的 TE

<!-- PROSE:SECTION:T00E -->
**最早的基因组论文。** Jaillon 等人（2007，[doi:10.1038/nature06148](https://doi.org/10.1038/nature06148)）的摘要写该组装 “obtained from a highly homozygous genotype”（Jaillon 2007 摘要）。该摘要没有写出 PN40024 或黑皮诺，截至 2026-11-15 CST 也未获得 Jaillon 2007 全文。Liu 等人（2024，[doi:10.1038/s41588-024-01967-5](https://doi.org/10.1038/s41588-024-01967-5)，PMC11631756，全文）写到：“Although the commonly used reference genome from PN40024 was highly homozygous after nine generations of selfing, it is missing >10% of genes compared with heterozygous cultivars.” PN40024 这一名称以及九代自交，引自该句，而不是 Jaillon 摘要。Jaillon 等人 2007 被用作 “41.4% (average value) of the grapevine genome is composed of repetitive/transposable elements” 一句的出处。该句不在已打开的 Jaillon 摘要里，因此 41.4% 这一数字仍标 **[待确认]**。若日后核上，它是重复序列与转座元件的合计，不是单纯的 TE 占比，也不是当前注释的数值（类型教学见 [../types/README.zh.md](../types/README.zh.md)）。Velasco 等人（2007，[doi:10.1371/journal.pone.0001326](https://doi.org/10.1371/journal.pone.0001326)）组装了杂合的黑皮诺克隆，估计基因组大小为 504.6 Mb，并写到：“Homologous chromosomes of Pinot Noir differ by 11.2% of their DNA (hemizygous DNA plus chromosomal gaps)”。Velasco 的摘要里没有给出 TE 占比，这里也不另填数字。

**杂合性与单倍型。** 葡萄的两条单倍型之间可以存在较大差异，因此同一个 TE 可能只出现在其中一条单倍型上。折叠成单倍的参考基因组会掩盖这种有无差异，只从一条单倍型建库也会漏掉部分家族。这也是后来转向单倍型组装和泛基因组方法的原因之一（另见 [../detection/tools_and_pipelines.zh.md](../detection/tools_and_pipelines.zh.md) 的难点说明）。

**泛基因组与有无变异。** Liu 等人（2024，[doi:10.1038/s41588-024-01967-5](https://doi.org/10.1038/s41588-024-01967-5)）用 18 套新的端粒到端粒分相组装和 11 套已发表组装，构建了图泛基因组 Grapepan v.1.0，并在 466 个品种的重测序中得到 9,105,787 个短变异和 236,449 个结构变异。他们报道平均 88.6% 的结构变异与 TE 重叠（Liu 2024 全文：“On average, 88.6% of the SVs overlapped TEs, whereas 30.9% intersected gene structures (Supplementary Fig. 7c,d ).”；指与 TE 重叠，而非这些变异中 TE 插入所占的比例）。要做一组材料中的 TE 有无分析，本仓库指向 panEDTA（Ou 等人 2024，[doi:10.1101/gr.278131.123](https://doi.org/10.1101/gr.278131.123)），而不是把各样本原始 EDTA 库简单拼接（见 [../detection/tools_and_pipelines.zh.md](../detection/tools_and_pipelines.zh.md) 的操作路线）。
<!-- /PROSE:SECTION:T00E -->

影响葡萄注释的行业难点（嵌套、定年限制、葡萄 `--u` 仍为 [待确认]、软屏蔽交接、单倍型）放在 [../detection/tools_and_pipelines.zh.md](../detection/tools_and_pipelines.zh.md)，同样从第 7 节搬来，不改科学表述。
