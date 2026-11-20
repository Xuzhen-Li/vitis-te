#!/usr/bin/env python3
"""Draw original TE teaching schematics as SVG. No input data from papers.

Usage: python3 draw_te_schematics.v4.py OUTDIR
Writes F1-F8 SVG files. F1 and F5 use versioned names
(F1_hierarchy.v2.svg, F5_helitron_maverick.v2.svg) because their labels
were updated in an earlier version. Colours are decorative only; labels carry the meaning.
This file does not overwrite draw_te_schematics.py or draw_te_schematics.v2.py. F3 and F4 use versioned names in this version.
"""
from __future__ import annotations

import sys
sys.dont_write_bytecode = True
from pathlib import Path


def svg(w, h, body, title):
    return (
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-label="{title}">\n'
        f'<title>{title}</title>\n'
        f'<rect width="{w}" height="{h}" fill="#ffffff"/>\n'
        f'{body}\n</svg>\n'
    )


def text(x, y, s, size=13, anchor="start", weight="normal", fill="#111"):
    s = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
    return (
        f'<text x="{x}" y="{y}" font-family="DejaVu Sans, Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">{s}</text>'
    )


def rect(x, y, w, h, fill, stroke="#222", sw=1, rx=2):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    )


def line(x1, y1, x2, y2, stroke="#333", sw=1.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"/>'


def f1_hierarchy():
    parts = [text(20, 28, "F1. Wicker-style hierarchy of eukaryotic TEs (simplified)", 16, weight="bold")]
    parts.append(text(20, 50, "Class I  retrotransposons (copy-and-paste, RNA intermediate)", 13, weight="bold"))
    y = 70
    class1 = [
        "Order LTR: Copia (RLC); Gypsy (RLG); Bel-Pao (RLB; Wicker Fig. 1 occurrence M only, [待确认]); Retrovirus; ERV.",
        "Florendovirus / plant pararetroviruses (Caulimoviridae; Geering 2014) sit OUTSIDE Order LTR. Wells and Feschotte 2020 exclude typically non-integrating viral elements.",
        "Order DIRS (YR, Wells 2020; TSD 0, Wicker Fig. 1 [待确认]).  Order PLE (TSD variable, Wicker Fig. 1 [待确认]).",
        "Order LINE (superfamilies R2, RTE, Jockey, L1, I; Wicker Fig. 1 [待确认]).  Order SINE (tRNA, 7SL, 5S derived; Wells 2020).",
        "Non-autonomous LTR derivatives: TRIM, LARD, TR-GAG (need a partner element for proteins).",
    ]
    for row in class1:
        parts.append(text(28, y, row, 12))
        y += 20
    y += 8
    parts.append(text(20, y, "Class II  DNA transposons", 13, weight="bold"))
    y += 22
    class2 = [
        "Subclass 1, order TIR (usually DDE transposase, cut-and-paste, TSD): Tc1/Mariner, hAT, Mutator, CACTA, PIF/Harbinger, PiggyBac, P, Merlin, Transib (Wicker Fig. 1 [待确认]).",
        "Subclass 1, order Crypton (tyrosine recombinase, TSD 0; Wicker 2007 Fig. 1, [待确认]). MITEs are short non-autonomous TIR elements (Tourist-PIF; Stowaway-Mariner).",
        "Subclass 2 (transposition by replication without double-strand cleavage; Wicker 2007 body, [待确认]): Helitron (rolling circle); Maverick / Polinton (DNA polymerase B).",
        "Nomenclature also exists in Repbase/Dfam and REXdb; they do not always agree.",
    ]
    for row in class2:
        parts.append(text(28, y, row, 12))
        y += 20
    parts.append(text(20, 330, "Source of the framework: Wicker et al. 2007, doi:10.1038/nrg2165 (abstract only; body and Fig. 1 [待确认]). This figure is an original schematic, not a journal reprint.", 11, fill="#444"))
    return svg(1180, 360, "\n".join(parts), "Wicker-style TE hierarchy")


def bar_row(x, y, segments, labels, title):
    parts = [text(x, y - 8, title, 13, weight="bold")]
    X = x
    for (w, fill, lab) in segments:
        parts.append(rect(X, y, w, 28, fill))
        parts.append(text(X + w / 2, y + 19, lab, 11, anchor="middle"))
        X += w
    return parts, X


def f2_ltr():
    parts = [text(20, 28, "F2. Anatomy of an intact LTR retrotransposon, and pol domain order", 16, weight="bold")]
    segs = [
        (70, "#f4c27a", "LTR"),
        (40, "#eeeeee", "PBS"),
        (90, "#8fbf7f", "gag"),
        (280, "#6ea8d8", "pol"),
        (40, "#eeeeee", "PPT"),
        (70, "#f4c27a", "LTR"),
    ]
    row, end = bar_row(40, 70, segs, None, "Intact element (not to scale). Flanking TSD is 4-6 bp (Wicker Fig. 1, [待确认]), typically 5 bp (Witte et al. 2001 abstract); not drawn.")
    parts += row
    parts.append(text(40, 130, "Copia (Ty1) pol domain order, typical:  PR — INT — RT — RH   (Wicker Fig. 1, [待确认])", 13))
    segs_c = [(70, "#d0e4f7", "PR"), (70, "#9cc4e8", "INT"), (70, "#6ea8d8", "RT"), (70, "#3d7fb0", "RH")]
    row, _ = bar_row(40, 145, segs_c, None, "")
    parts += row
    parts.append(text(40, 205, "Gypsy (Ty3) pol domain order, typical:  PR — RT — RH — INT   (a named chromovirus / chromodomain clade is [待确认]; not in the opened Wicker text)", 13))
    segs_g = [(70, "#d0e4f7", "PR"), (70, "#6ea8d8", "RT"), (70, "#3d7fb0", "RH"), (70, "#9cc4e8", "INT"), (90, "#c9b6e0", "chromo?")]
    row, _ = bar_row(40, 220, segs_g, None, "")
    parts += row
    notes = [
        "LTR: long terminal repeat, identical at insertion (Neumann et al. 2019). PBS: primer-binding site. PPT: polypurine tract.",
        "gag: capsid-related. pol: protease (PR), integrase (INT), reverse transcriptase (RT), RNase H (RH).",
        "The INT-before-RT versus RT-before-INT order is a practical way to tell Copia from Gypsy in a protein hit (Wicker Fig. 1, [待确认]).",
        "At insertion the two LTRs are the same sequence (Neumann et al. 2019). Solo LTRs form later by recombination. A solo LTR has only one LTR, so LTR-LTR divergence cannot be calculated (a conclusion from the definition).",
    ]
    y = 280
    for n in notes:
        parts.append(text(40, y, n, 12))
        y += 18
    return svg(1100, 370, "\n".join(parts), "LTR retrotransposon anatomy")


def f3_line_sine():
    parts = [text(20, 28, "F3. LINE (autonomous non-LTR) versus SINE (non-autonomous)", 16, weight="bold")]
    parts.append(text(40, 60, "LINE (e.g. L1-like): 5' UTR — ORF1 — ORF2 (EN + RT) — 3' UTR / poly(A) [待确认]. Often 5'-truncated in the genome (Wells 2020).", 13))
    segs = [(70, "#f0f0f0", "5'"), (110, "#8fbf7f", "ORF1"), (80, "#f2b5b5", "EN"), (110, "#6ea8d8", "RT (ORF2)"), (80, "#f0f0f0", "3'/A [待确认]")]
    row, _ = bar_row(40, 75, segs, None, "")
    parts += row
    parts.append(text(40, 140, "SINE: short, no RT of its own. Usually derived from tRNA, 7SL or 5S RNA and trans-mobilized by LINE machinery (Wells 2020).", 13))
    segs = [(90, "#f7e3a0", "tRNA/7SL/5S-like"), (100, "#f0f0f0", "body"), (90, "#f4c27a", "3'")]
    row, _ = bar_row(40, 155, segs, None, "")
    parts += row
    notes = [
        "Wells 2020: ORF2 encodes EN and RT; TPRT often terminates early, leaving 5-prime-truncated copies.",
        "Wells 2020: most SINEs derive from tRNA, 7SL or 5S RNA and are trans-mobilized by LINE machinery.",
        "Wells 2020: a hallmark of TPRT is frequent 5-prime truncation. The 3' UTR / poly(A) label and a variable TSD are [待确认]; they are not in the opened Wells 2020 full text.",
        "Plant genomes have LINEs and SINEs. A grape-specific claim that LTR elements dominate assembled sequence is not taught here (it was not in the opened Jaillon or Velasco abstracts). Exact Vitis lineage lists are [待确认] until a cited annotation is opened.",
    ]
    y = 220
    for n in notes:
        parts.append(text(40, y, n, 12))
        y += 18
    return svg(1100, 320, "\n".join(parts), "LINE versus SINE anatomy")


def f4_tir_mite():
    parts = [text(20, 28, "F4. TIR DNA transposon versus a MITE", 16, weight="bold")]
    parts.append(text(40, 60, "Autonomous TIR element: TIR — transposase (DDE or variant) — TIR. Cut-and-paste. TSD length is superfamily-typical [待确认].", 13))
    segs = [(80, "#f4c27a", "TIR"), (260, "#8fbf7f", "transposase and other ORFs"), (80, "#f4c27a", "TIR")]
    row, _ = bar_row(40, 75, segs, None, "")
    parts += row
    parts.append(text(40, 140, "MITE: short TIR element with little or no transposase ORF. Needs an autonomous partner that shares termini.", 13))
    segs = [(80, "#f4c27a", "TIR"), (80, "#f0f0f0", "short"), (80, "#f4c27a", "TIR")]
    row, _ = bar_row(40, 155, segs, None, "")
    parts += row
    notes = [
        "TSD lengths previously taken from Wicker 2007 Fig. 1 [待确认]: Tc1-Mariner TA; hAT 8 bp; Mutator 9-11 bp; Merlin 8-9 bp; Transib 5 bp; P 8 bp; PiggyBac TTAA; PIF-Harbinger 3 bp; CACTA 2-3 bp.",
        "Tourist MITEs are related to PIF (Zhang et al. 2001). Stowaway MITEs are plant Mariner elements with a TA TSD (Wicker 2007 body, [待确认]). Keep them as their own families.",
        "Do not merge non-autonomous copies into the autonomous consensus sequence. Assign them to a superfamily by shared termini or homology (this repository teaching practice [待确认]).",
        "Structural tools (TIR-Learner, MITE-Hunter, detectMITE, GRF) look for TIR + TSD. Homology tools need a library that already contains the family.",
    ]
    y = 220
    for n in notes:
        parts.append(text(40, y, n, 12))
        y += 18
    return svg(1100, 320, "\n".join(parts), "TIR DNA transposon versus MITE")


def f5_helitron_maverick():
    parts = [text(20, 28, "F5. Helitron versus Maverick / Polinton (Class II, subclass 2; Wicker 2007 body, [待确认])", 16, weight="bold")]
    parts.append(text(40, 60, "Helitron: rolling-circle. Usually no TIR and no TSD. Typical plant ends are often 5'-TC...CTRR-3' (typical, not absolute) [待确认].", 13))
    segs = [(60, "#f7e3a0", "5'TC"), (300, "#c9b6e0", "Rep/Hel (Wells: HUH + helicase); Wicker Y2 [待确认]"), (70, "#f7e3a0", "CTRR 3'")]
    row, _ = bar_row(40, 75, segs, None, "")
    parts += row
    parts.append(text(40, 140, "Maverick / Polinton: large, long TIRs, self-encoded DNA polymerase B and integrase-like protein. TSD 6 bp (Kapitonov and Jurka 2006) or 5-6 bp (Pritham et al. 2007).", 13))
    segs = [(70, "#f4c27a", "long TIR"), (140, "#6ea8d8", "PolB"), (140, "#8fbf7f", "INT-like"), (70, "#f4c27a", "long TIR")]
    row, _ = bar_row(40, 155, segs, None, "")
    parts += row
    notes = [
        "Helitrons were described as rolling-circle transposons by Kapitonov and Jurka 2001 (doi:10.1073/pnas.151269298).",
        "Polintons: Kapitonov and Jurka 2006 (doi:10.1073/pnas.0600833103). Mavericks: Pritham, Putliwala and Feschotte 2007 (doi:10.1016/j.gene.2006.08.008) is a survey (\"We previously identified ... Mavericks\"), not the first report.",
        "The two names refer to the same broad class of giant self-synthesizing DNA transposons; say which paper you follow. A candidate first report is Feschotte and Pritham 2005 (title only opened; [待确认]).",
        "Pritham et al. 2007 did not detect Mavericks in plants in that survey. Whether later plant reports exist is [待确认].",
        "DeepHel abstract: existing Helitron methods often have high false-positive rates. Not treating raw calls as a trusted library is this repository's rule.",
    ]
    y = 220
    for n in notes:
        parts.append(text(40, y, n, 12))
        y += 18
    return svg(1200, 340, "\n".join(parts), "Helitron versus Maverick anatomy")


def f6_trim_lard():
    parts = [text(20, 28, "F6. Autonomous LTR element versus TRIM and LARD", 16, weight="bold")]
    parts.append(text(40, 58, "Autonomous LTR: long LTRs + internal gag/pol (and sometimes other ORFs).", 13))
    segs = [(80, "#f4c27a", "LTR"), (260, "#6ea8d8", "internal coding (gag, pol, ...)"), (80, "#f4c27a", "LTR")]
    row, _ = bar_row(40, 72, segs, None, "")
    parts += row
    parts.append(text(40, 132, "TRIM (Witte et al. 2001): very short LTRs (~100-250 bp) and a short internal domain with PBS and PPT, no mobility ORFs.", 13))
    segs = [(70, "#f4c27a", "LTR"), (90, "#eeeeee", "PBS/PPT"), (70, "#f4c27a", "LTR")]
    row, _ = bar_row(40, 146, segs, None, "")
    parts += row
    parts.append(text(40, 206, "LARD (Kalendar et al. 2004): unusually long LTRs and a conserved but non-coding internal domain; described as Gypsy-related, non-autonomous.", 13))
    segs = [(120, "#f4c27a", "long LTR"), (160, "#e8e0f0", "non-coding internal"), (120, "#f4c27a", "long LTR")]
    row, _ = bar_row(40, 220, segs, None, "")
    parts += row
    parts.append(text(40, 280, "Both have LTR-like ends and can leave solo LTRs. They are kept as their own families, not merged into an autonomous consensus. TR-GAG is another reduced form (gag retained). Vitis counts [待确认].", 12))
    return svg(1100, 320, "\n".join(parts), "TRIM and LARD versus autonomous LTR")


def f7_decision():
    parts = [text(20, 28, "F7. How to recognise a TE: a decision tree for one candidate", 16, weight="bold")]
    boxes = [
        (40, 50, 320, 46, "Does it have two LTRs, PBS and PPT?"),
        (40, 120, 320, 46, "TIR plus a superfamily-typical TSD? [待确认]"),
        (40, 190, 320, 46, "Helitron-like ends, no TIR/TSD?"),
        (40, 260, 320, 46, "LINE/SINE signatures, or only a repeat?"),
        (420, 50, 360, 46, "LTR order: check pol domain order; date only intact pairs."),
        (420, 120, 360, 46, "TIR superfamily or MITE partner; keep families separate."),
        (420, 190, 360, 46, "Treat as Helitron only after curation; high FP risk."),
        (420, 260, 360, 46, "LINE/SINE vs satellite, rDNA, SSR, or a gene family."),
    ]
    for x, y, w, h, lab in boxes:
        parts.append(rect(x, y, w, h, "#f7f7f7"))
        parts.append(text(x + 10, y + 28, lab, 12))
    for y in (73, 143, 213, 283):
        parts.append(line(360, y, 420, y))
    parts.append(text(40, 330, "Structural evidence and protein domains beat a raw RepeatMasker name. Nested or fragmented copies need defragmentation before you trust a type call.", 12))
    return svg(820, 360, "\n".join(parts), "TE detection decision tree")


def f8_pipeline():
    parts = [text(20, 28, "F8. One mainstream plant library route (recommended here, not the only route)", 16, weight="bold")]
    steps = [
        (30, "EDTA de novo"),
        (170, "TEtrimmer"),
        (310, "TEsorter labels"),
        (470, "CDS-gated trusted"),
        (640, "soft-mask / panEDTA"),
    ]
    for i, (x, lab) in enumerate(steps):
        parts.append(rect(x, 70, 130, 48, "#e8f1fa"))
        parts.append(text(x + 65, 98, lab, 12, anchor="middle"))
        if i < len(steps) - 1:
            parts.append(line(x + 130, 94, steps[i + 1][0], 94))
    notes = [
        "Raw EDTA TElib is not a trusted library and is not --curatedlib.",
        "TEsorter (e.g. rexdb-plant) names domains; do not replace the working FASTA with all.cls.lib.",
        "Soft-mask only (RepeatMasker -xsmall) for gene annotation. Hard-masking hides real genes.",
        "panEDTA (Ou et al. 2024 maize pangenome paper, doi:10.1101/gr.278131.123) merges a panel; do not cat raw libraries.",
        "Peer pipelines exist: RepeatModeler2, Earl Grey, HiTE, DANTE/DANTE_LTR for lineage-centric LTR work. See the tools chapter.",
        "R1 trusted ~240 is an archive/teaching example, not a universal target number.",
    ]
    y = 150
    for n in notes:
        parts.append(text(30, y, n, 12))
        y += 20
    return svg(820, 290, "\n".join(parts), "Mainstream plant TE library route")


FIGURES = {
    "F1_hierarchy.v2.svg": f1_hierarchy,
    "F2_ltr_anatomy.svg": f2_ltr,
    "F3_line_sine.v2.svg": f3_line_sine,
    "F4_tir_mite.v2.svg": f4_tir_mite,
    "F5_helitron_maverick.v2.svg": f5_helitron_maverick,
    "F6_trim_lard.svg": f6_trim_lard,
    "F7_decision_tree.svg": f7_decision,
    "F8_pipeline.svg": f8_pipeline,
}


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 draw_te_schematics.v4.py OUTDIR", file=sys.stderr)
        return 2
    out = Path(sys.argv[1])
    # The output directory must already exist, or be creatable as a single new
    # folder (no parents=True, no exist_ok). Preflight all eight targets
    # before writing any file, so a mid-loop collision cannot leave a partial set.
    if not out.exists():
        out.mkdir()
    elif not out.is_dir():
        raise SystemExit(f"not a directory: {out}")
    paths = [out / name for name in FIGURES]
    existing = [p for p in paths if p.exists()]
    if existing:
        raise SystemExit("preflight: already exists: " + ", ".join(str(p) for p in existing))
    for name, fn in FIGURES.items():
        path = out / name
        data = fn()
        with path.open("x", encoding="utf-8") as f:
            f.write(data)
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
