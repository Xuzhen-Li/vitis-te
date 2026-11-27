# Changelog

This is the public summary of changes to the teaching files in TE-Lib (formerly `vitis-te`). Detailed logs are not part of this repository.

## 2026-11-26 — A general TE library, and licence

- The repository is now named TE-Lib (formerly vitis-te); GitHub redirects the old links. The home page title, opening paragraph and About line describe a general library of TE knowledge, software and workflows. Grapevine stays as the worked example, and no grapevine page was removed.
- The home page has a new table on how the repository is organised. New [`docs/KNOWLEDGE_MAP.md`](docs/KNOWLEDGE_MAP.md) and its Chinese version index every page by topic.
- Code is under the MIT License; text, tables and figures made for this repository are under CC BY 4.0; figures reproduced from papers keep their own licence. See [`NOTICE.md`](NOTICE.md).

## 2026-11-15 — Wicker markers

- The detection signatures card now marks every Wicker 2007 body or Figure 1 item as [待确认], except two statements sourced to Wells and Feschotte 2020, opened in full (PMC8293684): SINE origin from tRNA, 7SL or 5S RNA, and Cryptons as YR elements.
- Inline [待确认] markers were added in the Helitron and LTR type chapters so they match the claim–source tables. The LTR anatomy figure and its drawing script now mark the Copia/Gypsy domain-order captions the same way.
- SOURCES_READ cites the direct opens of the EDTA README and Wells and Feschotte 2020, and records earlier opens by URL and sha only.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — hierarchy figures

Unmarked Wicker 2007 body / Fig. 1 claims, plus further suggestions, are worked through, together with a 388-line keyword sweep, and a fresh "Wicker" / nrg2165 string sweep is recorded in the change log.

- J1–J3. New `figures/F1_hierarchy.v2.svg` and `scripts/figures/draw_te_schematics.v2.py`: DIRS TSD 0 and PLE variable TSD, the LINE superfamily list (R2, RTE, Jockey, L1, I), and Subclass 1 TIR plus its superfamily list are marked [待确认] (Wicker Fig. 1). DIRS YR and SINE tRNA/7SL/5S follow Wells and Feschotte 2020 (PMC8293684, sha256 52de993f…). The previous F1 SVG and script are left byte-identical and are superseded by these updated figures.
- J4. `docs/types/README.md` index rows for LINE superfamilies and DIRS/PLE TSD values now carry the same [待确认] (or Wells) wording.
- J5. Helitron “Class II, subclass 2” and “Y2-type” are marked [待确认] in the English and Chinese chapters and in `figures/F5_helitron_maverick.v2.svg`. Wells 2020 uses “four major groups” and does not use “Y2”.
- K1. CACTA 2–3 bp and Mutator 9–11 bp in `class_II_tir.md` / `.zh.md` line 17: “(Fig. 1 values [待确认])”.
- K2. `catalog/CATALOG.tsv` Wicker row: 80-80-80 is cited from the Wells 2020 full-text sentence “TE families are usually defined using the “80-80-80” rule…”, which Wells attributes to Wicker et al. 2007 (their ref. 160). The Wicker entry itself is labelled abstract only; body and Fig. 1 [待确认].
- K3. “not separate Wicker orders” in `class_I_trim_lard.md` / `.zh.md` and the same class of wording in `class_II_mite.md` / `.zh.md` is marked [待确认].

A "Wicker" / nrg2165 sweep of that teaching tree found 141 hits: 123 already carry [待确认] on the same line; the other 18 are framework titles, bibliographic DOI rows, source-register rows, naming-system contrasts, historical earlier figure/script files, or Florendovirus placement against this repo’s F1 (Wells + Geering). Status of each hit is listed in the build-side change log.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — figures and signature sources

- The unversioned F1 and F5 drawings, and the original drawing script, are not in this tree. They were never on the live main branch. They remain in earlier copies of these teaching files and have not been deleted. This tree ships the updated F1 and F5 figures, a new `draw_te_schematics.v3.py`, and new `F3_line_sine.v2.svg` and `F4_tir_mite.v2.svg`.
- LINE and SINE feature wording that was not in the opened Wells 2020 full text is marked [待确认]: the 3-prime A-rich / poly(A) / 3-prime UTR labels, and a variable TSD, in the signatures card (English and Chinese) and in F3. The F3 footnote no longer says a variable TSD is not taught while the signatures card stated Variable as fact.
- The sentence that non-autonomous copies are kept as their own families and assigned to a superfamily by shared termini or homology is labelled as a teaching practice of this repository [待确认], in the types index, the signatures card (English and Chinese), and F4.
- A sweep of factual TE-feature claims (TSD lengths, terminal motifs, enzyme or domain names, superfamily lists, structural features) is summarized in the build-side change log. Claims without an opened source remain cut or marked [待确认].


## 2026-11-15 — source checks for TE feature claims

- F2, F3, F4 and F7 were redrawn from `scripts/figures/draw_te_schematics.v4.py`. The earlier drawing script is not in this tree; it remains in earlier copies of these teaching files and has not been deleted. F1, F6 and F8 are byte-identical to the previous drawings of those figures. F5 is the same drawing with one added [待确认] on the typical plant Helitron end wording, which had no opened source on that line.
- SINE wording in F3 now follows Wells and Feschotte 2020 (full text): SINEs are usually derived from tRNA, 7SL or 5S RNA and are trans-mobilized by LINE machinery. The unsourced wording that a SINE 3-prime end often resembles a LINE was removed.
- The LINE "3'/A" box, and the superfamily-typical TSD wording in F4 and F7, are marked [待确认] (the Wicker 2007 body and Fig. 1 were not opened on 2026-11-15).
- Identical LTRs at insertion are cited from Neumann et al. 2019 (full text). The idea that gene conversion makes LTR ages too young remains [待确认].
- Liu et al. 2024 was opened in full text: the 88.6% SV-TE overlap sentence is quoted from that paper. PN40024 is described there as highly homozygous after nine generations of selfing. The Jaillon 2007 abstract says only "a highly homozygous genotype" and does not name Pinot or PN40024; the 41.4% figure remains [待确认].
- Small RNA / RdDM teaching now cites the Matzke and Mosher 2014 abstract as the source for that pathway, and the Slotkin and Martienssen 2007 abstract for overlapping eukaryotic silencing mechanisms.
- Maverick / Polinton as two names for one broad class is cited from the Wells and Feschotte 2020 full-text phrase "known as Mavericks or Polintons".
- The signatures card uses the Pritham et al. 2007 abstract wording "not detectable in plants".
- Body-cited papers that were missing from SOURCES_READ were added after the 2026-11-15 reading opened each one. Each new row is labelled full text, abstract-only, or title-only. Truncated or punctuated DOI fragments were not registered as identifiers.
- The live catalogue rows for Jaillon 2007, Finnegan 1989, and other live records were left byte-identical; errata describing the opened read levels were appended.

Claims without an opened source remain cut or marked [待确认].

## 2026-11-15 — catalogue restore and wording

- The live catalogue row for Wicker et al. 2007 (T01, catalogue line 24) is restored so that it is byte-identical to the live repository. The Wells and Feschotte 2020 wording of the 80-80-80 rule, and the note that the Wicker body and Fig. 1 were not opened, are kept as appended erratum E005.
- Four new lines that had named a private laboratory notebook were rewritten to say only private laboratory notebooks, with no notebook name.
- Process wording on non-live lines was replaced with neutral teaching wording, such as this addition, in the sources opened for these chapters, and the 2026-11-15 methods notes. The live Liu 2024 catalogue row (line 23) is unchanged.

Claims without an opened source remain cut or marked [待确认].
