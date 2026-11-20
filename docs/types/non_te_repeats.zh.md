# 会混入 TE 文库的非 TE 重复

从头构建的 TE 文库收集的是“看起来重复”的序列，并不都是转座因子。若它们留在 `--curatedlib` 或用于基因软屏蔽，可能把真基因屏蔽掉，至于 LAI 和 TE 含量数字会被抬高，是本仓库的提醒 **[待确认]**，不是从已打开的 Ou 2018 目录条目里抄来的原句。

串联重复和卫星（含 Tandem Repeats Finder，Benson 1999，[doi:10.1093/nar/27.2.573](https://doi.org/10.1093/nar/27.2.573)）放在**单独的非 TE 轨道**。端粒和着丝粒**卫星**是串联的非 TE 序列，走这条非 TE 轨道；**着丝粒反转录转座子（CRT）是 TE**，走 TE 轨道，不进本清单。两者要分开。具名的葡萄 CRT 家族在打开相应注释之前标为 **[待确认]**。

rDNA 阵列（45S、5S）是串联基因阵列，不是 TE。低复杂度序列和 SSR 同样不进 trusted 文库。成簇的宿主基因家族（尤其是 NLR、F-box）在 RepeatModeler 里也常被当成“重复”。ProtExcluder 是交接里留在基因注释一侧的改库工具；它如何剔除宿主蛋白编码片段，在打开其 README 或方法部分之前标为 **[待确认]**。DOI 10.1111/tpj.12340 不是 MAKER-P，不用。已打开的 MAKER-P 摘要（[doi:10.1104/pp.113.230144](https://doi.org/10.1104/pp.113.230144)）没有提到 ProtExcluder。把 NLR/F-box 作为 trusted 文库默认剔除对象、以及把核基因组中的 NUMT/NUPT 标出来而不当成新的 TE 超家族，是**本仓库规则**（见 [../detection/softmask_handoff.zh.md](../detection/softmask_handoff.zh.md)），不是从已打开的葡萄论文里抄来的句子。某一套 NUMT 过滤在给定葡萄数据集上是否够用，标为 **[待确认]**。

LAI（Ou 等 2018，[doi:10.1093/nar/gky730](https://doi.org/10.1093/nar/gky730)）是基于完整 LTR 的组装质量指数，不是把非 TE 重复留在 `--curatedlib` 里的许可。论断—出处表见 [non_te_repeats.md](non_te_repeats.md)。
