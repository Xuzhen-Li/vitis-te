# vitis-te
[English](README.md)

## 概述

本仓库提供 Vitis 转座子（TE）文库及进入基因注释阶段之前的软屏蔽（soft-mask）交接数据。实验操作记录存放在私有实验室 TE 树中，未包含在 git 中。

分析流程设计为 `EDTA` 至 `TEtrimmer`，至 `TEsorter`，再至基于 CDS 过滤的 trusted 结果，最终用于软屏蔽或 `panEDTA`。诸如 trusted `~240` 这样的 `R1` 编号属于归档和教学示例。最终的高质量参考数据可能会更新为新版的 trusted 结果。

基因软屏蔽步骤（`A0`）仅接受当前的 trusted 文件及其 version 或 `sha256` 值，不接受原始的 `EDTA` 输出或整个 working 文库。结构指南插件见于 [gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)。

## 不包含的内容

- 本项目不包含基因模型注释，相关内容见 [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation)。
- 本项目不包含基因功能注释，相关内容见 [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation)。
- 本项目不包含 PAV 图谱分析，相关内容见 [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome)。
- 本项目不是其他课题组原始 TE 预测结果的堆砌。

## 流程

1. 针对每个组装或单倍型运行 `EDTA`，使用 `--species others --sensitive 1 --anno 1` 参数，并记录 `--u` 参数。
2. 针对每个单倍型运行 `TEtrimmer`，合并 Perfect 与 Good 序列，并使用 `CD-HIT` 生成相似度约 `~95%` 的 working 文库。可以按需生成 `80-80` 阈值的 family 目录，但不要覆盖 working 文库。
3. 使用 `TEsorter`（如 `rexdb-plant`）仅用于分配结构域和标签。不要用 `all.cls.lib` 文件替换 working FASTA。
4. 通过包含 CDS BLAST 和 `TEsorter` 分类过滤规则的 curation 步骤，生成 trusted FASTA 并记录 `sha256` 值。
5. 仅使用 trusted 文件进行软屏蔽或作为 `EDTA` 的 `--curatedlib` 传入。
6. 运行 `panEDTA` 进行官方数据合并，而不是直接对 TE 文库使用 `cat` 命令，随后进行泛基因组重注释。
7. 在生成经过整理（curated）的 pan TE GFF 文件后，再进行 LTR 插入时间估计、LAI 计算和 PAV 分析。

## 区分

| Product | Use as `--curatedlib` / gene soft-mask? |
|---------|----------------------------------------|
| Raw EDTA TElib | No |
| Working lib (post-TEtrimmer CD-HIT) | No (whole file) |
| Trusted gated lib | Yes |
| `cat` + CD-HIT of many libs | No (dedup ≠ curation) |

## 用法

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --threads 32
```

## 注意事项

- 不要将 `EDTA` 原始输出作为金标准 TE 文库。
- 不要将 `cat` 加 `CD-HIT` 的结果直接作为 `--curatedlib`。
- 仅用于分类的工具只给 consensus 序列分类命名，它们不能取代序列修剪，也不能直接作为最终文库。
- 不要在 `BRAKER` 或 `GALBA` 流程中进行硬屏蔽（hard-mask）。必须使用经过宿主基因清洗的 trusted 文库进行软屏蔽。
- 非 TE 重复序列（如 `TRF`、端粒、rDNA）不属于 `--curatedlib` 的范畴。

## 参考

- [gene-structure-annotation `TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)
- [bioinfo-agent-skills](https://github.com/Xuzhen-Li/bioinfo-agent-skills)

作者：李旭真，[ORCID](https://orcid.org/0000-0003-3670-6657)
