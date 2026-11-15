# vitis-te

English | [中文](README.zh.md)

<!-- PROSE:INTRO -->
This repository is a methods catalogue for transposable elements (TEs) in *Vitis* and other plants. It starts from the basics: what a TE is, how TEs were discovered, how they move, how they are classified, which sequence features define each type, how they interact with the host genome, what is known in grapevine, where current methods struggle, and which software is used at each step. It is also the public hand-off for a *Vitis* TE library used in gene soft-masking. The operational laboratory notebook stays in a private tree and is not tracked in git.
<!-- /PROSE:INTRO -->

The structure-annotation plug-in is documented in [gene-structure-annotation `docs/TE_LIBRARY.md`](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md). Overlap with that repository is expected; this page cross-links to it rather than repeating the gene-prediction playbook.

<!-- PROSE:CATALOG_NOTE -->
**2026-11-15 catalogue.** Tool versions are not pinned in this pass and are recorded as `n/a` unless a paper year is the object being cited. Paper years are print years, except where Crossref lists no print date (in which case the issued or online year is used and noted). DOIs are included only when the Crossref title matches the intended paper (checked 2026-11-15, Asia/Shanghai, CST, UTC+8). Items without a title-matched DOI are listed by URL only, or marked [待确认]. A workflow with decision points is in [`docs/WORKFLOW.md`](docs/WORKFLOW.md). The tabular form of the catalogue is [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv) (80 entries).
<!-- /PROSE:CATALOG_NOTE -->

## Out of scope

- Gene-model annotation is handled by [gene-structure-annotation](https://github.com/Xuzhen-Li/gene-structure-annotation).
- Functional annotation belongs to [gene-function-annotation](https://github.com/Xuzhen-Li/gene-function-annotation).
- PAV graphs and the long graph-tool list are covered by [vitis-pangenome](https://github.com/Xuzhen-Li/vitis-pangenome).
- This repository is not a dump of raw TE calls from other research groups.
- Private laboratory drafts and teaching notes that are not already public on GitHub are not copied here.

## Contents

0. [What a transposable element is](#section-0)
1. [How TEs were discovered](#section-1)
2. [How TEs move](#section-2)
3. [Classification](#section-3)
4. [Sequence features](#section-4)
5. [TEs and the host](#section-5)
6. [TEs in grapevine genomes](#section-6)
7. [Field difficulties](#section-7)
8. [Software by step](#section-8)
9. [Practical workflow, red lines, and example scripts](#section-9)
10. [Glossary](#section-10)

<a id="section-0"></a>
## 0. What a transposable element is

<!-- PROSE:SECTION:T00A -->
In plain words, a transposable element is a stretch of DNA that can move or copy itself to a new place in the genome. Some elements are cut out of one site and pasted into another. Others are copied through an RNA intermediate, so the original copy stays in place while a new copy appears elsewhere. Helitrons move by a rolling-circle mechanism (see [section 2](#section-2)). Over time, many copies lose the ability to move and remain as inactive remnants.

TEs make up a large part of many plant genomes. They can land near or inside genes and alter how those genes are used, and they can also be silenced by the host and remain inactive for long periods. The later sections cover this in order: the history of their discovery, the ways TEs move, the names used to classify them, the sequence features that identify each type, their effects on the host, what is known in grapevine, and finally the practical difficulties and software.

Introductory reviews include Feschotte, Jiang and Wessler (2002, [doi:10.1038/nrg793](https://doi.org/10.1038/nrg793)), Lisch (2013, [doi:10.1038/nrg3374](https://doi.org/10.1038/nrg3374)) and Wells and Feschotte (2020, [doi:10.1146/annurev-genet-040620-022145](https://doi.org/10.1146/annurev-genet-040620-022145)). The classification used throughout this repository is Wicker et al. (2007, [doi:10.1038/nrg2165](https://doi.org/10.1038/nrg2165)).
<!-- /PROSE:SECTION:T00A -->

<a id="section-1"></a>
## 1. How TEs were discovered

<!-- PROSE:SECTION:T00B -->
This section is a reading path, not a complete history of every paper. Claims below are limited to papers whose Crossref title was matched on 2026-11-15 (CST). A number, a gene name, or a first use of a phrase is marked [待确认] when the original wording was not re-read.

**Maize, and the idea that DNA can move.** McClintock (1950, [doi:10.1073/pnas.36.6.344](https://doi.org/10.1073/pnas.36.6.344)) described the origin and behaviour of mutable loci in maize. A subsequent report (McClintock 1953, [doi:10.1093/genetics/38.6.579](https://doi.org/10.1093/genetics/38.6.579)) described the induction of instability at selected maize loci. That work forms the basis of what later literature calls the Activator/Dissociation (Ac/Ds) system; the first paper in which she used those exact names was not re-read here [待确认]. In 1983 she received the Nobel Prize in Physiology or Medicine for the discovery of mobile genetic elements. Her Nobel lecture was published as McClintock (1984, [doi:10.1126/science.15739260](https://doi.org/10.1126/science.15739260)).

**Bacteria.** Jordan, Saedler and Starlinger (1968, [doi:10.1007/bf00433726](https://doi.org/10.1007/bf00433726)) showed that certain strong-polar mutations in the *Escherichia coli* gal operon were insertions. Insertion sequences (IS elements) are now a well-described class of bacterial mobile DNA (Mahillon and Chandler 1998, [doi:10.1128/mmbr.62.3.725-774.1998](https://doi.org/10.1128/mmbr.62.3.725-774.1998)). Shapiro (1979, [doi:10.1073/pnas.76.4.1933](https://doi.org/10.1073/pnas.76.4.1933)) proposed a general molecular model for the transposition and replication of bacteriophage Mu and other transposable elements.

**Yeast, and movement through RNA.** Boeke, Garfinkel, Styles and Fink (1985, [doi:10.1016/0092-8674(85)90197-7](https://doi.org/10.1016/0092-8674(85)90197-7)) showed that Ty elements in yeast transpose through an RNA intermediate. That experiment provided a key direct demonstration behind the later Class I / retrotransposon picture: the element is transcribed, reverse-transcribed, and a new DNA copy is inserted.

**Fruit fly, and hybrid dysgenesis.** Kidwell, Kidwell and Sved (1977, [doi:10.1093/genetics/86.4.813](https://doi.org/10.1093/genetics/86.4.813)) described hybrid dysgenesis in *Drosophila melanogaster*: a syndrome of aberrant traits, including mutation, sterility and male recombination, in the offspring of certain crosses. Bingham, Kidwell and Rubin (1982, [doi:10.1016/0092-8674(82)90463-9](https://doi.org/10.1016/0092-8674(82)90463-9)) reported results strongly supporting the P-factor hypothesis: that the molecular basis of P-M hybrid dysgenesis is the P element, a transposon family present in P strains.

**Genome size, and DNA that spreads because it can.** Organisms that do not differ correspondingly in apparent complexity can still carry very different amounts of DNA per haploid genome (the C-value). Thomas (1971, [doi:10.1146/annurev.ge.05.120171.001321](https://doi.org/10.1146/annurev.ge.05.120171.001321)) discussed the genetic organisation of chromosomes in this context. Secondary sources attribute the phrase "C-value paradox" to that paper; the Thomas text itself was not re-read here [待确认]. Doolittle and Sapienza (1980, Nature 284:601–603, [doi:10.1038/284601a0](https://doi.org/10.1038/284601a0)) and Orgel and Crick (1980, Nature 284:604–607, [doi:10.1038/284604a0](https://doi.org/10.1038/284604a0)) argued that much DNA can spread simply because it can replicate within the genome, without needing to serve a function for the organism — "selfish DNA". These are the April 1980 essays in volume 284 (title-matched on Crossref). A later reply by Orgel, Crick and Sapienza (1980, Nature 288:645–646, [doi:10.1038/288645a0](https://doi.org/10.1038/288645a0)) is a separate item and is not a substitute for the April essays. The DOI 10.1038/288604a0 is a different paper and is not used.

**A shared classification, then the genome era.** Finnegan (1989) split eukaryotic TEs into two classes; Wicker et al. (2007) added the hierarchy used in this repository (see [section 3](#section-3)). Once whole genomes could be sequenced, the scale of TEs became obvious. Schnable et al. (2009, [doi:10.1126/science.1178534](https://doi.org/10.1126/science.1178534)) reported, for the maize B73 genome, that "Nearly 85% of the genome is composed of hundreds of families of transposable elements", and that these elements captured and amplified numerous gene fragments.

**Grapevine milestones** are developed further in [sections 5 and 6](#section-5). In brief: Kobayashi, Goto-Yamamoto and Hirochika (2004, [doi:10.1126/science.1095011](https://doi.org/10.1126/science.1095011)) reported retrotransposon-induced mutations in grape skin color (the body of that short paper was not re-read here). This et al. (2007, [doi:10.1007/s00122-006-0472-2](https://doi.org/10.1007/s00122-006-0472-2)), in an abstract we did read, found that insertion of the retroelement Gret1 in the promoter of *VvmybA1* was strongly associated with the white-fruited phenotype in *Vitis vinifera*. Jaillon et al. (2007) published the first grapevine genome sequence and reported a combined repetitive/transposable-element fraction (see [section 3](#section-3) and [section 6](#section-6)). Later pangenome work catalogues structural variation across many assemblies (Liu et al. 2024; see section 6); that paper reported that, on average, 88.6% of the SVs overlapped TEs (overlap, not a count of SVs that are TE insertions).
<!-- /PROSE:SECTION:T00B -->

<a id="section-2"></a>
## 2. How TEs move

<!-- PROSE:SECTION:T00C -->
The movement mechanism forms the basis of the two-class system in [section 3](#section-3).

**Copy-and-paste (Class I, retrotransposons).** The element is transcribed into RNA, reverse-transcribed into DNA, and a new copy is inserted while the original copy remains. Boeke et al. (1985) demonstrated this RNA intermediate for yeast Ty elements. Plant genomes are rich in LTR retrotransposons (Copia/Ty1 and Gypsy/Ty3) and also contain non-LTR elements (LINEs and the non-autonomous SINEs that depend on them).

**Cut-and-paste (many Class II TIR elements).** A transposase excises the element from one site and inserts it at another. These elements are typically bordered by terminal inverted repeats (TIRs) and leave a short target-site duplication (TSD). Short non-autonomous MITEs are derived from TIR elements and do not encode their own transposase.

**Rolling-circle, and Mavericks.** Helitrons transpose by a rolling-circle mechanism (Kapitonov and Jurka 2001, [doi:10.1073/pnas.151269298](https://doi.org/10.1073/pnas.151269298)). In the Wicker system, Helitrons and Mavericks (Polintons) form Class II subclass 2 because they transpose without double-strand cleavage. Helitrons typically lack both TIRs and a TSD. Mavericks have long TIRs and are thought to replicate using a self-encoded DNA polymerase. A Maverick TSD length is [待确认] until the Wicker table is checked in full.

**Autonomous and non-autonomous copies.** An autonomous element encodes the proteins it needs to move. A non-autonomous element does not, and can move only when those proteins are supplied in trans — for example SINEs relying on LINE machinery, or MITEs relying on a related transposase. Because non-autonomous copies lack coding domains, domain-based classifiers often leave them as Unknown. They are usually kept as separate families and assigned to a superfamily through shared termini or homology to an autonomous partner, rather than merged into the autonomous consensus (see [section 7](#section-7)). Separately, host-gene fragments accidentally placed in a library are dangerous because they can soft-mask real genes (see [section 9](#section-9)).
<!-- /PROSE:SECTION:T00C -->

<a id="section-3"></a>
## 3. Classification

<!-- PROSE:SECTION:T01 -->
Finnegan (1989, [doi:10.1016/0168-9525(89)90039-5](https://doi.org/10.1016/0168-9525(89)90039-5)) divided eukaryotic TEs into Class I, which replicate through an RNA intermediate, and Class II, which move through a DNA intermediate. Wicker et al. (2007, [doi:10.1038/nrg2165](https://doi.org/10.1038/nrg2165)) retained that class split and added a hierarchy of order, superfamily and family. Two elements are placed in the same family when they share at least 80 percent identity over at least 80 percent of their coding or internal region, or of their terminal repeats, and at least 80 bp (the 80-80-80 rule in Wicker et al. 2007).

Orders that matter in plant genomes include:

- LTR retrotransposons, mainly the Ty1/Copia and Ty3/Gypsy superfamilies (some systems also list Bel-Pao, retrovirus and caulimovirus / pararetrovirus groups).
- Non-LTR retrotransposons: LINE and SINE.
- TIR DNA transposons, and the short non-autonomous MITEs that derive from them.
- Helitrons, which transpose by a rolling-circle mechanism (Kapitonov and Jurka 2001, [doi:10.1073/pnas.151269298](https://doi.org/10.1073/pnas.151269298)). In the Wicker system, Helitrons and Mavericks (Polintons) form Class II subclass 2 because they transpose without double-strand cleavage. Helitrons typically lack both TIRs and a TSD. Mavericks have long TIRs and are thought to replicate using a self-encoded DNA polymerase. A Maverick TSD length is [待确认] until the Wicker table is checked in full.

These systems do not always agree on names.

- Kapitonov and Jurka (2008, [doi:10.1038/nrg2165-c1](https://doi.org/10.1038/nrg2165-c1)) argued for a "universal classification" implemented in Repbase. Repbase names and Wicker names are related but not identical.
- RepeatMasker and Dfam assign a sequence by homology to a consensus or HMM library. The string in a RepeatMasker output is a library hit, not a fresh structural classification on its own. Dfam is the open library ([doi:10.1186/s13100-020-00230-y](https://doi.org/10.1186/s13100-020-00230-y)); Repbase is a separate, historically central database ([doi:10.1159/000084979](https://doi.org/10.1159/000084979)). Libraries enriched in animal families can leave plant-specific lineages as `Unknown` or under a generic `LTR/Gypsy` or `LTR/Copia` label.
- TEsorter with REXdb classifies plant LTR elements from conserved protein domains into lineages (for example Copia lineages such as Ale or SIRE, and Gypsy lineages such as Tekay or CRM; Neumann et al. 2019, [doi:10.1186/s13100-018-0144-1](https://doi.org/10.1186/s13100-018-0144-1); Zhang et al. 2022, [doi:10.1093/hr/uhac017](https://doi.org/10.1093/hr/uhac017)). Those lineage names are more resolved than a RepeatMasker superfamily hit, and they apply to LTR elements with detectable coding domains. TEsorter can also emit domain labels for some TIR superfamilies and Helitrons; the exact class coverage is [待确认]. Classifier output names consensus sequences; it does not replace trimming, and `all.cls.lib` must not replace the working FASTA.

Jaillon et al. (2007, [doi:10.1038/nature06148](https://doi.org/10.1038/nature06148)) is the first grapevine genome paper and is listed for context. They report that "41.4% (average value) of the grapevine genome is composed of repetitive/transposable elements", the average of three approaches, as a combined repetitive and transposable-element fraction, not a TE-only proportion and not a current annotation.
<!-- /PROSE:SECTION:T01 -->
<a id="section-4"></a>
## 4. Sequence features

<!-- PROSE:SECTION:T02 -->
Typical values below follow Wicker et al. 2007 and, for Helitrons, Kapitonov and Jurka 2001 and 2007. Exceptions are common. Use these rows as a checklist when inspecting a consensus, not as a substitute for a curated alignment.

| Type | Typical TSD | Termini and ends | Internal hallmarks |
|------|-------------|------------------|--------------------|
| LTR Copia (Ty1) | Often 5 bp | LTRs, typically with 5-prime TG and 3-prime CA ends (typical, not absolute); PBS complementary to a tRNA just inside the 5-prime LTR; PPT just before the 3-prime LTR | Gag, protease, integrase, reverse transcriptase, RNase H; integrase is usually encoded before RT |
| LTR Gypsy (Ty3) | Often 5 bp | Same LTR, PBS and PPT logic, including typical TG…CA ends | Same domain set; integrase is usually encoded after RT |
| LINE | Variable (often several to tens of bp) | No LTR; many families end in a polyA or another 3-prime tail | Autonomous copies encode an endonuclease and RT |
| SINE | Variable | Internal RNA polymerase III promoters; often a 3-prime polyA; no protein-coding ORFs | Non-autonomous; mobilisation depends on LINE machinery |
| TIR Tc1/Mariner | TA | Terminal inverted repeats | Transposase when autonomous |
| TIR hAT | 8 bp | Terminal inverted repeats | Transposase when autonomous |
| TIR Mutator (MuDR) | 9–11 bp [待确认] | Terminal inverted repeats | Transposase when autonomous |
| TIR CACTA | 2–3 bp | Terminal inverted repeats; CACTA-like termini | Transposase when autonomous |
| TIR PIF/Harbinger | 3 bp | Terminal inverted repeats | Transposase when autonomous |
| MITE | Same as the parent TIR superfamily | Short elements with TIRs; no transposase | Non-autonomous DNA TE |
| Helitron | Typically none (often at AT) | 5-prime TC; 3-prime CTRR plus a short hairpin | Rolling-circle Rep/helicase when autonomous |

PBS is the primer-binding site. PPT is the polypurine tract. TSD length and terminus motifs should be treated as typical rather than exclusive, and remain open to revision if a primary table in Wicker 2007 is checked against a specific family and disagrees [待确认] for rare superfamilies not listed here.
<!-- /PROSE:SECTION:T02 -->

<a id="section-5"></a>
## 5. TEs and the host

<!-- PROSE:SECTION:T00D -->
**Effects on genes.** A new insertion can disrupt a coding sequence, alter splicing, or land near a gene and change when or where that gene is expressed. TEs can also donate regulatory sequence. Feschotte et al. (2002) and Lisch (2013) review these outcomes in plants. Not every insertion matters; many land in already repetitive DNA and remain silent.

**Silencing.** Eukaryotic hosts use overlapping epigenetic mechanisms to silence TE expression and mobility, including small RNAs and DNA methylation (Slotkin and Martienssen 2007, [doi:10.1038/nrg2072](https://doi.org/10.1038/nrg2072)). In plants, RNA-directed DNA methylation (RdDM) is a major pathway of this kind (Matzke and Mosher 2014, [doi:10.1038/nrg3683](https://doi.org/10.1038/nrg3683)). Silencing protects the genome, and because TEs recruit the silencing machinery, they can also shape epigenetic states at single genes and across larger chromosomal regions (Slotkin and Martienssen 2007).

**A grapevine trait example: berry skin colour.** Kobayashi, Goto-Yamamoto and Hirochika (2004, [doi:10.1126/science.1095011](https://doi.org/10.1126/science.1095011)) reported retrotransposon-induced mutations in grape skin color; the body of that short paper was not re-read in this pass, so gene and element names are not taken from it. This et al. (2007, [doi:10.1007/s00122-006-0472-2](https://doi.org/10.1007/s00122-006-0472-2)) found, across over 200 *V. vinifera* accessions, that insertion of the retroelement Gret1 in the promoter of *VvmybA1*, a regulator of anthocyanin biosynthesis, was strongly associated with the white-fruited phenotype. That association alone does not establish that the insertion caused the colour change. The same abstract reports that some pigmented alleles are consistent with later “excision” of Gret1 (the authors' word). Because Gret1 is an LTR retrotransposon, it moves by copy-and-paste rather than transposase-mediated excision; loss of such an element usually occurs through recombination between the two LTRs, leaving a solo LTR. Whether the coloured alleles in that study actually carry a solo LTR is [待确认]. The abstract also notes that the association of Gret1 with the white-fruited phenotype was rarely absent, suggesting that a white phenotype can also arise through mutation in additional genes. *VvmybA1* is discussed there in the context of a trait under human selection after domestication, rather than as proof of the insertion's role in the original domestication event.

**Somatic variation in a clonal crop.** Because grapevine is usually propagated by cuttings, a somatic change in one bud can be maintained as a new clone. Azuma et al. (2009, [doi:10.1016/j.plantsci.2008.12.015](https://doi.org/10.1016/j.plantsci.2008.12.015)) studied bud sports of white-skinned 'Italia'. For colour recovery in 'Ruby Okuyama', they wrote that it "may have occurred as a result of intra-LTR recombination within a retrotransposon, Gret1". In plain words, the two long terminal repeats of a single element can recombine with each other, deleting the internal sequence and leaving behind a single LTR. That sentence in Azuma 2009 restates earlier work; a candidate source is Kobayashi et al. 2005 ([doi:10.2503/jjshs.74.196](https://doi.org/10.2503/jjshs.74.196); title-matched, body not opened here) [待确认]. The same Azuma paper's own result for 'Benitaka' is different: a novel *VvmybA1*(BEN) allele attributed to recombination between *VvmybA1a* and *VvmybA3*, not to a TE insertion or excision. How often TEs cause somatic change in vineyards more generally, and how that should be weighed against other mutation classes, is [待确认].

**Other crops.** The maize B73 genome (Schnable et al. 2009) serves as a scale example: TEs make up nearly 85% of that genome and have captured gene fragments. Further crop-trait examples are not listed here unless a title-matched paper was read for this catalogue.
<!-- /PROSE:SECTION:T00D -->

<a id="section-6"></a>
## 6. TEs in grapevine genomes

<!-- PROSE:SECTION:T00E -->
**The first genome papers.** Jaillon et al. (2007, [doi:10.1038/nature06148](https://doi.org/10.1038/nature06148)), using a nearly homozygous Pinot-derived genotype (PN40024), reported that "41.4% (average value) of the grapevine genome is composed of repetitive/transposable elements", the average of three approaches, as a combined repetitive and transposable-element fraction rather than a TE-only proportion or a current annotation (see also [section 3](#section-3)). Velasco et al. (2007, [doi:10.1371/journal.pone.0001326](https://doi.org/10.1371/journal.pone.0001326)) assembled a heterozygous Pinot Noir clone, estimated the genome size at 504.6 Mb, and reported that "Homologous chromosomes of Pinot Noir differ by 11.2% of their DNA (hemizygous DNA plus chromosomal gaps)". A TE fraction was not taken from the Velasco abstract, as it does not state one.

**Heterozygosity and haplotypes.** Because the two haplotypes of a grapevine can differ substantially, a TE may be present on one haplotype and absent on the other. A collapsed haploid representation can hide that presence or absence, and a library built from only one haplotype will miss some families. This is one reason later work moved to haplotype-resolved assemblies and pangenome methods (see also the field-difficulty note in [section 7](#section-7)).

**Pangenomes and presence/absence.** Liu et al. (2024, [doi:10.1038/s41588-024-01967-5](https://doi.org/10.1038/s41588-024-01967-5)) built a graph-based grapevine pangenome (Grapepan v.1.0) from 18 new phased telomere-to-telomere assemblies and 11 published assemblies, along with a variation map containing 9,105,787 short variants and 236,449 structural variants from 466 cultivars. They reported that, on average, 88.6% of the SVs overlapped TEs (overlap with TEs, not a count of SVs that are TE insertions). For TE presence/absence across a panel, this repository points to panEDTA (Ou et al. 2024, [doi:10.1101/gr.278131.123](https://doi.org/10.1101/gr.278131.123)), rather than a simple concatenation of raw EDTA libraries (see [section 9](#section-9)).
<!-- /PROSE:SECTION:T00E -->
<a id="section-7"></a>
## 7. Field difficulties

<!-- PROSE:SECTION:T03 -->
- **Nested and fragmented copies.** New insertions into older elements, along with decayed fragments, cause structural detectors to miss copies and homology annotators to split a single element into many hits. Defragment after RepeatMasker (RepeatCraft, oneCodeToFindThemAll) and inspect nested structure during curation.
- **Recent versus old copies.** Insertion age from LTR-LTR divergence is meaningful for intact young copies after curation. The two LTRs of a new insertion are copies of the same template and are identical at insertion; later divergence is what T = K / (2r) measures, because the two LTRs accumulate substitutions independently. Canonical LTR ends are often 5′-TG…CA-3′ (typical, not absolute; LTR_retriever also reports non-canonical ends). After insertion, recombination between the two LTRs can delete the internal region and leave a single LTR (a solo LTR), which cannot be dated by this formula. If r is in substitutions per site per year, no generation time is needed; a per-generation rate must be converted first. In a clonal crop the sexual generation interval is long and uncertain. Gene conversion between the two LTRs makes the estimated age too young. Do not treat ages from raw EDTA output as a final deliverable, and do not convert divergence to years without an explicit substitution rate (and a generation time only if the rate is per generation). If EDTA is run without `--u`, it silently uses a rice rate of 1.3e-8 /bp/year; that default is not a grape value and must not be used without stating it explicitly. A grape `--u` is [待确认].
- **Curation is still the bottleneck.** TEtrimmer, MCHelper and Earl Grey automate parts of consensus cleaning, but a trusted library still requires a documented CDS gate and class-emit rules. Goubert et al. 2022 ([doi:10.1186/s13100-021-00259-7](https://doi.org/10.1186/s13100-021-00259-7)) is a beginner's guide to manual curation, not the methods paper for those tools.
- **False positives from gene families and tandem repeats.** NLR clusters, other gene families, SSRs and tandem repeats can enter a de novo library. Keep TRF, telomere and rDNA on a separate non-TE track; they do not belong in `--curatedlib`.
- **Soft-mask hand-off.** If the genome is left unmasked, BRAKER and GALBA call TE-encoded ORFs as genes (over-prediction). If it is hard-masked to `N`, genes that overlap repeats are truncated or lost (under-prediction). If it is soft-masked with a library that still contains host genes, those genes are masked and can be missed (under-prediction). The only file accepted for gene soft-mask or EDTA `--curatedlib` is the current trusted library, named with its version and sha256 (see [TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md)). EDTA genome sequence names should be at most 13 characters (letters, digits, underscores), with a name map back to the original headers. Convert the genome to uppercase before RepeatMasker `-xsmall`. Library headers should follow the `name#Class/Family` format. RepeatMasker `.out` coordinates are 1-based closed intervals; BED is 0-based half-open.
- **Pangenome TE presence or absence.** In grape, an insertion may be haplotype-specific. Combine panel libraries with panEDTA once a trusted file exists; concatenating raw TElibs and running CD-HIT does not produce a pan library.
- **Heterozygous, haplotype-resolved genomes.** Run discovery per assembly or haplotype rather than collapsing haplotypes before TE discovery.
<!-- /PROSE:SECTION:T03 -->
<a id="section-8"></a>
## 8. Software by step

<!-- PROSE:SECTION:T04 -->
Each row is expanded in [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv), with a link, a title-matched DOI where one exists, inputs, outputs and when to use the tool. Tool versions are not pinned here.

Three tools are worth a brief explanation, using only what the method papers' abstracts support and leaving unchecked module lists as [待确认]. EDTA (Ou et al. 2019) is a pipeline that compares existing annotators for LTR retrotransposons, TIR transposons (including MITEs) and Helitrons, then combines the more robust programs into a filtered, non-redundant library of intact and fragmented elements, and can resolve nested insertions. The exact programs called inside a given EDTA release are [待确认] against that paper's methods and the EDTA documentation; in this repository LTR_retriever is the intact-LTR filter documented alongside EDTA. RepeatModeler2 (Flynn et al. 2020) is a de novo family finder; this version adds a module for structural discovery of complete LTR retroelements. This repository's wrapper records the LTR structural step (`-LTRStruct`; the option name by version remains [待确认]). The catalogue lists RepeatScout and RECON as RepeatModeler2's internal de novo engines. In this repository's catalogue, LTR_retriever (Ou and Jiang 2018) is recorded as taking structural LTR candidates and building a high-quality LTR library (that input step comes from the catalogue, not from the paper abstract). It identifies canonical elements with 5′-TG…CA-3′ termini and also reports non-canonical (non-TGCA) LTR retrotransposons. Further filter features used inside the program are [待确认] pending a methods-section re-read.

| Step | Use when | Tools in this catalogue |
|------|----------|-------------------------|
| De novo discovery | Starting from an assembly or haplotype | EDTA (default here), RepeatModeler2, Earl Grey; family finders RepeatScout, RECON, PILER |
| Structural detection | Seeking intact LTR, TIR, MITE or Helitron copies | LTR_FINDER, LTR_FINDER_parallel, LTRharvest, LTR_retriever; HelitronScanner; MITE-Hunter, detectMITE, TIR-Learner, GRF |
| Homology | Annotating or masking with a library | RepeatMasker; libraries Dfam and Repbase |
| Classification | Labelling a working library | TEsorter + REXdb (plant LTR lineages); DeepTE; TEclass |
| Curation and consensus | Turning raw consensi into a working or trusted library | TEtrimmer (default here), MCHelper, Goubert guide, CD-HIT |
| Library QC | Removing non-TE repeats and checking assembly quality | TRF (non-TE track); LAI after curated or pan annotation |
| Masking | Handing a genome to gene annotation | RepeatMasker `-xsmall` with the trusted library only; BEDTools for track checks |
| TE age / insertion time | Intact LTR pairs after curation | LTR_retriever; `scripts/01_ltr_insertion_age.py` for a toy demonstration |
| Polymorphic TE calling | Population or long-read insertion calling, not library construction | TEMP, RelocaTE2, xTea, Jitterbug |
| Pangenome TE | A panel of haplotypes or genomes | panEDTA (`panEDTA.sh` in the EDTA repository) |
| Visualization / defragmentation | Cleaning homology annotations | RepeatCraft, oneCodeToFindThemAll |
<!-- /PROSE:SECTION:T04 -->
<a id="section-9"></a>
## 9. Practical workflow, red lines, and example scripts

The public workflow runs from `EDTA` to `TEtrimmer` to `TEsorter` to a CDS-gated trusted library, and from there to soft-masking or `panEDTA`. The `R1` numbers, such as a trusted count of `~240`, are archive and teaching examples; the panel gold standard may move to a newer trusted file. The gene soft-mask step designated as `A0` accepts only the current trusted file along with its version and sha256, not raw EDTA output and not the entire working library.

1. Run `EDTA` per assembly or haplotype using `--species others --sensitive 1 --anno 1`. Set `--u` explicitly and record its source. A grape value for `--u` is [待确认]; if `--u` is omitted, EDTA silently uses a rice rate of 1.3e-8 /bp/year, which must not be used for grape without stating it explicitly.
2. Run `TEtrimmer` per haplotype, merge the Perfect and Good outputs, and use `CD-HIT` to generate a working library at about 95 percent identity. An optional 80-80 family catalog can also be built, provided it does not overwrite the working library.
3. Run `TEsorter` with a resource such as `rexdb-plant` to assign domains and labels only. Never replace the working FASTA with `all.cls.lib`.
4. Apply a curation gate using CDS BLAST and TEsorter class-emit rules to produce a trusted FASTA and record its sha256.
5. Run soft-masking or EDTA `--curatedlib` with the trusted file only.
6. Run `panEDTA` to combine panel results formally rather than concatenating TE libraries, then reannotate the panel.
7. Calculate LTR age, LAI and PAV only after curated pan TE GFFs are generated.

| Product | Use as `--curatedlib` / gene soft-mask? |
|---------|----------------------------------------|
| Raw EDTA TElib | No |
| Working lib (post-TEtrimmer CD-HIT) | No (whole file) |
| Trusted gated lib | Yes |
| `cat` + CD-HIT of many libs | No (dedup is not curation) |

```bash
EDTA.pl --genome assembly.fa --species others --sensitive 1 --anno 1 --u RATE --threads 32
```

- Do not treat raw EDTA output as a gold-standard TE library.
- Do not treat `cat` and CD-HIT output as `--curatedlib`.
- Classifier-only tools name consensi; they do not replace trimmers and do not become the library itself.
- Do not hard-mask for BRAKER or GALBA. Soft-mask with a trusted library that has been purged of host genes.
- Non-TE repeats such as TRF, telomeres and rDNA do not belong in `--curatedlib`.
### Example scripts

Toy demonstrations that run with Python 3 and numpy are in [`scripts/`](scripts/). They use a planted LTR-like insertion rather than real *Vitis* data. See [`scripts/README.md`](scripts/README.md) and [`testdata/README.md`](testdata/README.md).

| Script | Role | Status on the build box (2026-11-15 CST) |
|--------|------|------------------------------------------|
| `00_make_tiny_genome.py` | Write a tiny FASTA and BED with one planted LTR-like insertion | Tested |
| `01_ltr_insertion_age.py` | p-distance and K2P between the two LTRs; years only with `--rate` (no default); T = K/(2r) | Tested |
| `02_softmask.py` | Lowercase BED intervals (soft-mask demonstration) | Tested |
| `03_run_edta.sh` | Documents the EDTA command used above | Untested (`--dry-run` / `--help` only) |
| `04_run_repeatmodeler_repeatmasker.sh` | Documents RepeatModeler2 + RepeatMasker `-xsmall` | Untested (`--dry-run` / `--help` only) |
| `05_run_tesorter.sh` | Documents TEsorter with rexdb-plant and the all.cls.lib rule | Untested (`--dry-run` / `--help` only) |
| `run_toy_pipeline.sh` | Runs the three tested Python scripts | Tested |

```bash
bash scripts/run_toy_pipeline.sh OUTDIR
```

<a id="section-10"></a>
## 10. Glossary

<!-- PROSE:SECTION:T00F -->
- **Transposable element (TE).** A DNA sequence that can move or copy itself to a new genomic site; many copies later lose that ability.
- **Class I / retrotransposon.** An element that moves through an RNA intermediate (copy-and-paste).
- **Class II / DNA transposon.** An element that moves through a DNA intermediate. Many use cut-and-paste, while Helitrons and Mavericks are grouped separately (subclass 2).
- **LTR.** Long terminal repeat, the direct repeats that flank LTR retrotransposons.
- **Solo LTR.** A single LTR left behind after recombination between the two LTRs of one element deletes the internal region. Solo LTRs cannot be dated by T = K/(2r).
- **TIR.** Terminal inverted repeat, characteristic of cut-and-paste DNA transposons.
- **TSD.** Target-site duplication, a short sequence duplicated at the insertion site.
- **PBS / PPT.** Primer-binding site and polypurine tract, sequence hallmarks located just inside the LTR ends.
- **MITE.** A short, non-autonomous TIR element.
- **Autonomous / non-autonomous.** Whether an element encodes the proteins it needs to move, or relies on another element to supply them.
- **80-80-80 rule.** Wicker family criterion: at least 80% identity over at least 80% of the coding or internal region, or of the terminal repeats, and at least 80 bp.
- **Soft-mask / hard-mask.** Soft-masking writes repeats in lowercase while leaving the bases readable; hard-masking replaces them with N. This repository uses soft-masking for gene annotation.
- **RdDM.** RNA-directed DNA methylation, a plant pathway that can silence TEs.
- **C-value.** The amount of DNA in a haploid genome, which varies widely among organisms.
- **Selfish DNA.** The idea that some DNA spreads simply because it can replicate within the genome, rather than because it benefits the organism (Doolittle and Sapienza 1980; Orgel and Crick 1980). A later reply is Orgel, Crick and Sapienza 1980.
- **Hybrid dysgenesis.** A syndrome of sterility and mutation in the offspring of certain *Drosophila* crosses, caused in the P-M system by P elements.
- **Gret1 / VvmybA1.** A retrotransposon insertion in the promoter of the anthocyanin regulator *VvmybA1*, associated with white grape berries (This et al. 2007).
- **PAV.** Presence/absence variation, including TE insertions that differ among haplotypes or cultivars.
<!-- /PROSE:SECTION:T00F -->

## References

Catalogue rows and DOIs are in [`catalog/CATALOG.tsv`](catalog/CATALOG.tsv). The gene-annotation hand-off is [TE_LIBRARY.md](https://github.com/Xuzhen-Li/gene-structure-annotation/blob/main/docs/TE_LIBRARY.md).

Author: Xuzhen Li, [ORCID](https://orcid.org/0000-0003-3670-6657)
