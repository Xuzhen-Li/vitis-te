# 识别各类型所用的序列特征

本页是现场卡片。类型各章给出生物学和论断—出处表；本页是对着一条候选序列时看什么。图 [F7](../../figures/F7_decision_tree.svg) 是同一套逻辑的树形写法。

| 类型 | 末端 | TSD | 关键蛋白结构域 | 常见基因组残迹 | 一线工具 |
|------|---------|-----|-----------------------------|---------------------------|------------------|
| LTR Copia / Gypsy | 两条正向 LTR；以 5′-TG-3′ 起始、5′-CA-3′ 结束（Wicker 2007 正文，[待确认]） | 4–6 bp（Wicker 图 1，[待确认]）；通常 5 bp（Witte 等 2001 摘要） | *gag*、*pol*；Copia 为 INT 在 RT 前，Gypsy 为 RT 在 INT 前（Wicker 图 1，[待确认]） | Solo LTR；嵌套插入；截短的 *pol* | LTR_FINDER / LTRharvest → LTR_retriever；DANTE_LTR；TEsorter/REXdb |
| TRIM / LARD | 两条 LTR，PBS、PPT；LTR 与内部区比例不寻常 | 插入位点通常 5 bp（Witte 等 2001 摘要） | 几乎没有 *pol* | Solo LTR | 同一套结构 LTR 工具，再用蛋白筛选找“空”内部 |
| LINE | 无 LTR；L1 样类群 3′ 常富含 A [待确认] | 可变 [待确认] | ORF2 中的 EN + RT（Wells 与 Feschotte 2020） | 5′ 截短（Wells 与 Feschotte 2020） | RepeatModeler / HiTE 同源；结构域搜索 |
| SINE | 短；常来自 tRNA、7SL 或 5S（Wells 与 Feschotte 2020 全文，PMC8293684：“Most SINEs are derived from Pol III-transcribed noncoding RNA such as tRNA, 7SL or 5S RNA”） | 可变 [待确认] | 无（无 RT） | 严重降解的拷贝 | 对 SINE 文库做同源；不用 LTR 工具 |
| TIR DNA | 短的反向末端 | 超家族特异，取自 Wicker 图 1 [待确认]：Tc1–Mariner TA；hAT 8 bp；Mutator 9–11 bp；Merlin 8–9 bp；Transib 5 bp；P 8 bp；PiggyBac TTAA；PIF–Harbinger 3 bp；CACTA 2–3 bp | 自主拷贝中的 DDE 转座酶 | 断裂的 TIR | TIR-Learner、GRF、EDTA 的 TIR 模块 |
| MITE | 短 TIR，几乎无 ORF | 与配对超家族相同（Tourist–PIF，Zhang 等 2001，doi:10.1073/pnas.211442198；Stowaway–Mariner，Wicker 2007 正文 [待确认]；Bureau 与 Wessler 1994，doi:10.1105/tpc.6.6.907，靶位点 TA） | 无 | 高拷贝、短 | MITE-Hunter、detectMITE、TIR-Learner |
| Helitron | 常为 5′-TC…CTRR-3′ 和短发夹（Kapitonov 与 Jurka 2001 摘要）；通常无 TIR | TSD 为 0（Wicker 图 1，[待确认]） | Wicker 2007：“Y2-type tyrosine recombinase”[待确认]。Wells 与 Feschotte 2020：HUH 核酸酶 / Rep/Hel | 捕获的基因片段（Morgante 等 2005，doi:10.1038/ng1615）；假阳性高 | HelitronScanner；DeepHel；再整理 |
| Maverick/Polinton | 长 TIR | 6 bp（Kapitonov 与 Jurka 2006 摘要）或 5–6 bp（Pritham 等 2007 摘要） | PolB + 整合酶样蛋白 | 2007 年调查中 not detectable in plants（Pritham 等 2007 摘要） | 结构域搜索，不是 EDTA 默认模块 |
| Crypton | 末端措辞 [待确认]：Goodwin 等 2003 摘要，doi:10.1099/mic.0.26529-0，“bordered by short direct repeats”；Wells 与 Feschotte 2020 把 Crypton 与短 TIR 放在一起 | TSD 为 0（Wicker 图 1，[待确认]） | 酪氨酸重组酶（Wells 与 Feschotte 2020 全文：“by YR (called Cryptons)”；Wicker 图 1 的写法 [待确认]） | 植物中罕见或缺失 [待确认] | 结构域搜索 |
| Florendovirus / 副反转录病毒 | 不是 LTR 目。Geering 等 2014：Caulimoviridae 的一个属。Wells 与 Feschotte 2020 把通常不整合的病毒元件排除在此处所用的 TE 定义之外 | 不是简单的 TE TSD 规则 | 病毒 RT / 运动相关结构域 | 完整或降解的插入；葡萄中 9% 的 florendovirus 位点在内含子里（Geering 等 2014） | TEsorter/病毒 HMM；单独一条轨道 |
| 非 TE 重复 | 串联单体、rRNA、SSR；着丝粒卫星走非 TE 轨道（CRT 走 TE 轨道） | 不是 TE 的 TSD | 若漏进基因家族，则是宿主蛋白 | 留在文库里会抬高 TE 含量 | TRF；rDNA BLAST；CDS 门控 |

非自主拷贝通常自成家族，靠末端或同源性归到超家族，不并进自主元件的共识序列（本仓库的教学做法 [待确认]）。

Maverick 的首报：Pritham 等 2007 是综述式调查（“We previously identified … Mavericks”），不是首篇报道。Feschotte 与 Pritham 2005（doi:10.1016/j.tig.2005.07.007）是候选首报；本组教学章节打开的来源中只打开了题名，这一鉴定仍为 [待确认]。

英文见 [signatures.md](signatures.md)。
