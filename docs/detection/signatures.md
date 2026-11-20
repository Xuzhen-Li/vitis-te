# Sequence signatures used to recognise each type

This page is a field card. The type chapters give the biology and the claim–source tables; this page is what you look at on a candidate sequence. Figure [F7](../../figures/F7_decision_tree.svg) is the same logic as a tree.

| Type | Termini | TSD | Protein domains that matter | Frequent genomic wreckage | First-line tools |
|------|---------|-----|-----------------------------|---------------------------|------------------|
| LTR Copia / Gypsy | Two direct LTRs; start 5′-TG-3′ and end 5′-CA-3′ (Wicker 2007 body, [待确认]) | 4–6 bp (Wicker Fig. 1, [待确认]); typically 5 bp (Witte et al. 2001 abstract) | *gag*, *pol*; INT-before-RT (Copia) vs RT-before-INT (Gypsy) (Wicker Fig. 1, [待确认]) | Solo LTR; nested insertions; truncated *pol* | LTR_FINDER / LTRharvest → LTR_retriever; DANTE_LTR; TEsorter/REXdb |
| TRIM / LARD | Two LTRs, PBS, PPT; unusual LTR:internal proportions | Typically 5 bp (Witte et al. 2001 abstract, for LTR insertion sites) | Little or no *pol* | Solo LTR | Same structural LTR tools, then a protein screen that finds "empty" internals |
| LINE | No LTR; 3' often A-rich in L1-like groups [待确认] | Variable [待确认] | EN + RT in ORF2 (Wells and Feschotte 2020) | 5′ truncation (Wells and Feschotte 2020) | RepeatModeler / HiTE homology; domain search |
| SINE | Short; often tRNA, 7SL or 5S derived (Wells and Feschotte 2020, full text, PMC8293684: “Most SINEs are derived from Pol III-transcribed noncoding RNA such as tRNA, 7SL or 5S RNA”) | Variable [待确认] | None (no RT) | Heavily degraded copies | Homology to a SINE library; do not use LTR tools |
| TIR DNA | Short inverted termini | Superfamily-typical, from Wicker Fig. 1 [待确认]: Tc1–Mariner TA; hAT 8 bp; Mutator 9–11 bp; Merlin 8–9 bp; Transib 5 bp; P 8 bp; PiggyBac TTAA; PIF–Harbinger 3 bp; CACTA 2–3 bp | DDE transposase in autonomous copies | Broken TIRs | TIR-Learner, GRF, EDTA TIR module |
| MITE | Short TIRs, almost no ORF | Same as the partner superfamily (Tourist–PIF, Zhang et al. 2001, doi:10.1073/pnas.211442198; Stowaway–Mariner, Wicker 2007 body [待确认]; Bureau and Wessler 1994, doi:10.1105/tpc.6.6.907, TA target site) | None | High copy, short | MITE-Hunter, detectMITE, TIR-Learner |
| Helitron | Often 5′-TC…CTRR-3′ and a short hairpin (Kapitonov and Jurka 2001 abstract); usually no TIR | TSD 0 (Wicker Fig. 1, [待确认]) | Wicker 2007: “Y2-type tyrosine recombinase” [待确认]. Wells and Feschotte 2020: HUH nuclease / Rep/Hel | Captured gene fragments (Morgante et al. 2005, doi:10.1038/ng1615); high false positives | HelitronScanner; DeepHel; then curation |
| Maverick/Polinton | Long TIRs | 6 bp (Kapitonov and Jurka 2006 abstract) or 5–6 bp (Pritham et al. 2007 abstract) | PolB + integrase-like | not detectable in plants (Pritham et al. 2007 abstract) | Domain search, not EDTA default |
| Crypton | Termini wording is [待确认]: Goodwin et al. 2003 abstract, doi:10.1099/mic.0.26529-0, “bordered by short direct repeats”; Wells and Feschotte 2020 group Crypton with short TIRs | TSD 0 (Wicker Fig. 1, [待确认]) | Tyrosine recombinase (Wells and Feschotte 2020, full text: “by YR (called Cryptons)”; Wicker Fig. 1 wording [待确认]) | Rare or absent in plants [待确认] | Domain search |
| Florendovirus / pararetrovirus | Not an LTR order. Geering et al. 2014: a genus of Caulimoviridae. Wells and Feschotte 2020 exclude typically non-integrating viral elements from the TE definition used here | not a simple TE TSD rule | Viral RT / movement-related domains | Intact vs degraded insertions; in *V. vinifera*, 9% of florendovirus loci are in introns (Geering et al. 2014) | TEsorter/virus HMMs; keep on a separate track |
| Non-TE repeat | Tandem monomers, rRNA, SSR; keep centromeric satellites off the TE track (CRTs stay on the TE track) | none as a TE TSD | Host proteins if a gene family leaked in | Inflated TE content if left in the library | TRF; rDNA BLAST; CDS gate |

Non-autonomous copies are usually kept as their own families and assigned to a superfamily by shared termini or homology, not merged into the autonomous consensus (this repository teaching practice [待确认]).

Maverick first-report: Pritham et al. 2007 is a survey (“We previously identified … Mavericks”), not the first report. Feschotte and Pritham 2005 (doi:10.1016/j.tig.2005.07.007) is a candidate first report; only the title was opened for these chapters, so that identification remains [待确认].

Chinese: [signatures.zh.md](signatures.zh.md).
