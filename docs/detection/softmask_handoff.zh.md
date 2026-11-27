# 交给基因注释的软屏蔽交接

本仓库负责建设和整理 TE 文库。[gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation) 使用**当前 trusted** 文库，在预测基因模型之前对基因组做软屏蔽。那一步是他们的 A0。基因注释仓库里不建 TE 库。

下面的产品分层和红线，复述的是 vitis-te（2026-11-15）以及 gene-structure-annotation 里已经公开的教学内容。这里**不**复制私有实验室笔记。

## 四层产物（不要压成一个 FASTA）

1. **原始 EDTA TElib** — 发现阶段的输出。不是 `--curatedlib`，也不能用于基因软屏蔽。
2. **working 文库** — TEtrimmer（Perfect + Good）之后，再按约 95% 做 CD-HIT。整份文件仍然不是 `--curatedlib`。
3. **分类标签** — TEsorter（例如 `rexdb-plant`）只加结构域和名称。不要用 `all.cls.lib` 替换 working FASTA（本仓库的 `all.cls.lib` 指对 `all.fa` 运行 TEsorter 时的文件名；官方 README 的输出是 `<input>.rexdb.cls.lib`）。
4. **trusted 文库** — 经过有记录的 CDS BLAST / 宿主基因清理，并有成文的分类规则。本仓库里的 ProtExcluder 是与这里所讲 CDS 门控有重叠的改库步骤。至于它是否“剔除与蛋白匹配的片段及两侧 50 bp”，在打开 ProtExcluder 的 README 或方法部分之前标为 **[待确认]**。DOI 10.1111/tpj.12340 经核是植物血红蛋白论文，不是 MAKER-P，不用。已打开的 MAKER-P 摘要（Campbell 等，doi:10.1104/pp.113.230144）没有提到 ProtExcluder。把 NLR、F-box 作为默认剔除对象是**本仓库规则**，不是从已打开的葡萄论文里抄来的句子。只有这份注明版本和 sha256 的 trusted 文件，才可用于基因软屏蔽或作为 EDTA `--curatedlib`。除非以后的方法决定另有说明，不要把 Dfam 当作默认的第二份库（这一口径冲突已记在 2026-11-15 的方法说明里）。

把许多文库 `cat` 后再 CD-HIT，并不是整理。

## 只做软屏蔽，不做硬屏蔽

BRAKER 的 README（已打开）写：为了在新基因组上准确预测基因，基因组应当做重复序列屏蔽，以免在重复和低复杂度区域预测出假阳性基因结构。对 GeneMark 和 AUGUSTUS，softmasking（重复区小写、其余大写）“leads to better results than hardmasking”（硬屏蔽是把重复区写成 `N`）。至于硬屏蔽成 `N` 会使重叠的真基因被截断或丢失，是本仓库的推断 **[待确认]**，不是 BRAKER 原句。只使用 RepeatMasker `-xsmall`（帮助页：使用 `-xsmall` 时重复区为小写）和 trusted 文库做软屏蔽。`EDTA.pl` 调用 `make_masked.pl` 时写的是 `-hardmask 1`（来自 EDTA.pl 源码，不是 EDTA README 里面向用户的默认项说明）。本仓库不把 EDTA `make_masked.pl` 当作 A0 软屏蔽步骤来教。

仍留在注释仓库里的操作检查包括：交给 RepeatMasker 之前先把基因组转成大写（本仓库的防御性约定，因为 `-xsmall` 用小写表示屏蔽；RepeatMasker 帮助页并不要求事先转大写）；文库序列名用 `name#Class/Family`；EDTA 要求基因组序列名不超过 13 个字符（字母、数字和下划线），并保留对照表（EDTA README）；本仓库目前把 RepeatMasker 的 `.out` 当作 1 起始闭区间、把 BED 当作 0 起始半开区间；已打开的 RepeatMasker 帮助页并没有写这一坐标约定，因此标为 **[待确认]**。

## 这部分内容如何迁移

类型、工具和建库的深入讲解放在本仓库。gene-structure-annotation 只保留简短的 A0 使用说明，以及检查基因模型与 TE 重叠的质控（`qa08_te_overlap.py`）。拟议的删除和替换清单见随本教学包提供的 `REMOVALS.md`。该清单在经过审阅并合并 PR 之前不会执行。

R1 trusted ~240 是归档和教学例子，不是通用目标。葡萄 EDTA 的 `--u` 仍为 [待确认]。
