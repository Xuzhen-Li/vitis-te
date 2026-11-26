import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svgkit_v2 import SVG, PAL, tint, tw, wrap, INK, MUTED, ink_on

OUT, REPO = sys.argv[1], sys.argv[2]
B, O, G, R, P, S, GR = PAL["blue"], PAL["orange"], PAL["green"], PAL["red"], PAL["purple"], PAL["sky"], PAL["grey"]
BR = PAL["brown"]; MG = PAL["magenta"]; GO = PAL["gold"]
rows = list(csv.DictReader(open(os.path.join(REPO, "catalog/SOFTWARE_AUTHORITY.tsv"), encoding="utf-8"), delimiter="\t"))

def badge(s, x, y, n, color):
    s.raw("<circle cx=\"%.1f\" cy=\"%.1f\" r=\"11\" fill=\"%s\"/>" % (x, y, color))
    s.text(x, y + 4.6, str(n), 12.5, True, ink_on(color, 12.5), "middle")

def workflow():
    W, H = 1320, 470
    s = SVG(W, H, "Practical TE library workflow in vitis-te")
    steps = [
        ("EDTA per haplotype", ["--species others --sensitive 1 --anno 1", "set --u and record its source"], B, "raw EDTA TElib"),
        ("TEtrimmer per haplotype", ["keep Perfect + Good", "CD-HIT about 95% identity"], O, "working library"),
        ("TEsorter (rexdb-plant)", ["domains and labels only", "never swap in all.cls.lib"], P, "labelled working library"),
        ("Curation gate", ["CDS BLAST removes host genes", "TEsorter class-emit rules; record sha256"], G, "trusted gated library"),
        ("Soft-mask / --curatedlib", ["RepeatMasker -xsmall or EDTA --curatedlib", "trusted file only"], "#1D7CBB", "soft-masked genome, TE GFF"),
        ("panEDTA for a panel", ["combine panel results formally", "then re-annotate the panel"], BR, "curated pan TE GFFs"),
        ("Downstream", ["LTR age, LAI, PAV", "only after curated pan TE GFFs exist"], MG, "results"),
    ]
    n = len(steps); x0 = 20; gap = 18; bw = (W - 2 * x0 - gap * (n - 1)) / n; y0 = 70
    s.text(20, 36, "Default route: EDTA, TEtrimmer, TEsorter, a CDS-gated trusted library, soft-masking; panEDTA for a panel (README, Practical workflow)", 14, True, INK)
    hs = []
    for i, (t, ls, c, prod) in enumerate(steps):
        x = x0 + i * (bw + gap)
        h = s.node(x, y0, bw, t, ls, c, tsize=14, bsize=11.5, align="start", min_h=132)
        badge(s, x + bw - 14, y0 - 2, i + 1, c)
        hs.append(h)
    for i in range(n - 1):
        x = x0 + (i + 1) * (bw + gap) - gap + 1
        s.line([(x, y0 + 50), (x + gap - 4, y0 + 50)], "#333333", 2)
    # product strip
    py = y0 + max(hs) + 34
    s.text(20, py - 10, "Which product may be used as --curatedlib or for gene soft-masking (README product table)", 14, True, INK)
    prods = [("Raw EDTA TElib", "no", "not a trusted library; not --curatedlib"),
             ("Working library (after TEtrimmer + CD-HIT)", "no", "whole file is not a trusted library"),
             ("Trusted gated library", "yes", "the only file for --curatedlib and gene soft-masking"),
             ("cat + CD-HIT of many libraries", "no", "deduplication is not curation"),
             ("Non-TE repeats (TRF, telomeres, rDNA)", "no", "do not belong in --curatedlib")]
    cw = (W - 40 - 4 * 12) / 5
    for i, (t, ok, why) in enumerate(prods):
        x = 20 + i * (cw + 12); c = G if ok == "yes" else R
        s.rect(x, py, cw, 92, c, rx=8)
        s.text(x + 12, py + 22, ("Use: " + ok).upper() if False else ("Usable: " + ok), 13, True, INK)
        yy = py + 42
        for ln in wrap(t, 12.5, cw - 24, True):
            s.text(x + 12, yy, ln, 12.5, True, "#000000"); yy += 16
        for ln in wrap(why, 11.5, cw - 24):
            s.text(x + 12, yy, ln, 11.5, False, INK); yy += 15
    # notes
    ny = py + 120
    s.rect(20, ny, W - 40, 72, "#6B6B6B", rx=8, fill="#F7F7F7", shadow=False, dash="5 4")
    notes = ["If --u is omitted, EDTA silently uses a rice rate of 1.3e-8 per bp per year; never use it for grape without saying so.",
             "Soft-mask only: do not hard-mask for BRAKER or GALBA. Classifier-only tools name consensi; they do not replace trimmers or become the library."]
    for j, t in enumerate(notes):
        s.text(34, ny + 28 + j * 22, t, 12.5, False, INK)
    s.text(W - 20, H - 10, "Steps, options and rules quoted from README, Practical workflow.", 11, False, MUTED, "end")
    return s

def top_tools(section, k, skip=()):
    rs = [r for r in rows if r["step_section"] == section and r["name"] not in skip]
    d = [r["name"] for r in rs if r["role"] == "repository default"]
    o = sorted([r for r in rs if r["role"] != "repository default" and r["citations_openalex"]], key=lambda r: -int(r["citations_openalex"]))
    return d, [r["name"] for r in o[:k]]

def decision():
    W, H = 1320, 580
    s = SVG(W, H, "Which TE tools for which question")
    qs = [
        ("Build a TE library for one assembly", ["EDTA"], ["RepeatModeler2", "Earl Grey", "HiTE", "REPET"], B),
        ("Build one library for a panel of genomes", ["panEDTA"], ["panHiTE", "pantera", "panREPET"], BR),
        ("Find LTR retrotransposons", [], ["LTR_retriever", "LTRharvest", "LTR_FINDER", "DANTE and DANTE_LTR"], O),
        ("Find TIR, MITE, Helitron or SINE elements", [], ["TIR-Learner", "MITE-Hunter", "HelitronScanner", "AnnoSINE_v2"], O),
        ("Curate a raw library and check it", ["TEtrimmer", "CD-HIT"], ["MCHelper", "TE-Aid", "LTR Assembly Index (LAI)"], G),
        ("Classify consensus sequences", ["TEsorter"], ["REXdb", "DeepTE", "TEclass2"], P),
        ("Mask the genome for gene annotation", ["RepeatMasker"], ["BEDTools", "RepeatCraft"], "#1D7CBB"),
        ("Insertion age and repeat landscape", [], ["ParseRM", "RepeatLandscape", "TE_Density"], MG),
        ("Insertion polymorphisms from short reads", [], ["McClintock 2", "TEPID", "TEMP2", "RelocaTE2"], R),
        ("Insertion polymorphisms from long reads", [], ["TrEMOLO", "TELR", "PALMER"], R),
        ("Insertion polymorphisms from assemblies or graphs", [], ["GraffiTE", "PanGenie", "SyRI"], R),
        ("TE expression and small RNA", [], ["TEtranscripts", "TElocal", "Telescope", "SQuIRE", "ShortStack"], S),
    ]
    byname = {r["name"]: r for r in rows}
    cols = 3; cw = (W - 40 - (cols - 1) * 16) / cols; ch = 112
    s.text(20, 32, "Start from your question. Bold = repository default; others = examples from that catalogue section (README tables give paper, lab and tier).", 13.5, True, INK)
    for i, (qq, d, o, c) in enumerate(qs):
        for t in d + o:
            assert t in byname, t
        for t in d:
            assert byname[t]["role"] == "repository default", t
        secs = sorted(set(byname[t]["step_section"] for t in d + o))
        r_, c_ = divmod(i, cols)
        x = 20 + c_ * (cw + 16); y = 52 + r_ * (ch + 14)
        s.rect(x, y, cw, ch, c, rx=8)
        s.text(x + 12, y + 22, qq, 13.5, True, INK, maxw=cw - 24)
        yy = y + 46
        line_items = [(t, True) for t in d] + [(t, False) for t in o]
        xx = x + 12
        for t, bold in line_items:
            w = tw(t, 12, bold) + 16
            if xx + w > x + cw - 10:
                xx = x + 12; yy += 27
            s.rect(xx, yy - 14, w, 21, c, rx=10, fill=(tint(c, 0.75) if bold else "#FFFFFF"), shadow=False, stroke_w=1.0)
            s.text(xx + w / 2, yy + 1, t, 12, bold, "#000000", "middle"); xx += w + 6
        assert yy + 12 < y + ch - 22, qq
        for j, sec in enumerate(secs[:2]):
            s.text(x + 12, y + ch - 14 - 14 * (len(secs[:2]) - 1 - j), "section: " + sec, 10.5, False, INK, maxw=cw - 24)
    s.text(W - 20, H - 10, "Tool names, roles and sections checked against catalog/SOFTWARE_AUTHORITY.tsv.", 11, False, MUTED, "end")
    return s

def ltr_age():
    W, H = 1320, 470
    s = SVG(W, H, "Dating an LTR retrotransposon insertion from its two LTRs")
    def element(x, y, w, muts5=(), muts3=(), label=""):
        ltr = 150
        s.raw("<rect x=\"%.1f\" y=\"%.1f\" width=\"28\" height=\"16\" fill=\"#BFBFBF\"/>" % (x - 30, y + 7))
        s.raw("<rect x=\"%.1f\" y=\"%.1f\" width=\"28\" height=\"16\" fill=\"#BFBFBF\"/>" % (x + w + 2, y + 7))
        s.text(x - 16, y + 44, "TSD", 11, False, MUTED, "middle"); s.text(x + w + 16, y + 44, "TSD", 11, False, MUTED, "middle")
        for lx in (x, x + w - ltr):
            s.raw("<polygon points=\"%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f\" fill=\"%s\" stroke=\"%s\" stroke-width=\"1\"/>" % (lx, y, lx + ltr - 14, y, lx + ltr, y + 15, lx + ltr - 14, y + 30, lx, y + 30, tint(B, 0.55), B))
        s.raw("<rect x=\"%.1f\" y=\"%.1f\" width=\"%.1f\" height=\"18\" fill=\"%s\" stroke=\"%s\" stroke-width=\"1\"/>" % (x + ltr + 4, y + 6, w - 2 * ltr - 8, tint(O, 0.6), O))
        s.text(x + w / 2, y + 20, "internal region (gag, pol)", 11.5, False, "#000000", "middle")
        s.text(x + ltr / 2, y - 8, "5\u2032 LTR", 12, True, INK, "middle"); s.text(x + w - ltr / 2, y - 8, "3\u2032 LTR", 12, True, INK, "middle")
        for m in muts5:
            s.raw("<line x1=\"%.1f\" y1=\"%.1f\" x2=\"%.1f\" y2=\"%.1f\" stroke=\"%s\" stroke-width=\"2.4\"/>" % (x + m, y + 2, x + m, y + 28, R))
        for m in muts3:
            s.raw("<line x1=\"%.1f\" y1=\"%.1f\" x2=\"%.1f\" y2=\"%.1f\" stroke=\"%s\" stroke-width=\"2.4\"/>" % (x + w - ltr + m, y + 2, x + w - ltr + m, y + 28, R))
    s.text(20, 34, "a  At insertion (T = 0)", 14, True, "#000000")
    s.text(20, 54, "both LTRs are copied from the same RNA region, so they start identical", 12, False, MUTED)
    element(80, 84, 520)
    s.text(20, 184, "b  After time T", 14, True, "#000000")
    s.text(20, 204, "each LTR gains about rT neutral substitutions on its own (red marks)", 12, False, MUTED)
    element(80, 234, 520, muts5=(22, 61, 95, 128), muts3=(15, 49, 80, 117, 139))
    # formula panel
    fx = 680
    s.rect(fx, 20, 620, 250, B, rx=10, fill="#FFFFFF")
    s.text(fx + 16, 48, "c  From divergence to age", 14, True, "#000000")
    s.raw("<text x=\"%d\" y=\"92\" font-family=\"Arial, Liberation Sans, sans-serif\" font-size=\"22\" fill=\"#000000\"><tspan font-style=\"italic\">K</tspan> = 2<tspan font-style=\"italic\">rT</tspan>   so   <tspan font-style=\"italic\">T</tspan> = <tspan font-style=\"italic\">K</tspan> / (2<tspan font-style=\"italic\">r</tspan>)</text>" % (fx + 16))
    lines = ["K: substitutions per site between the two LTRs, corrected for multiple hits (Kimura 2-parameter, K2P)",
             "r: neutral substitution rate per site per year; it sets the time scale"]
    yy = 124
    for ln in lines:
        for w_ in wrap(ln, 12.5, 588):
            s.text(fx + 16, yy, w_, 12.5, False, INK); yy += 18
        yy += 4
    tsv = list(csv.DictReader(open(os.path.join(REPO, "testdata/ltr_age.tsv"), encoding="utf-8"), delimiter="\t"))[0]
    s.text(fx + 16, yy + 10, "Toy example (scripts/01_ltr_insertion_age.py, testdata/ltr_age.tsv):", 12.5, True, INK)
    s.text(fx + 16, yy + 30, "%s sites, %s differences: p-distance %.3f, K2P %.4f; years: %s (no --rate given)" % (tsv["n_sites"], tsv["substitutions"], float(tsv["p_distance"]), float(tsv["k2p"]), tsv["years"]), 12.5, False, "#000000")
    # caveats
    cy = 300
    s.rect(20, cy, W - 40, 140, R, rx=10, fill=tint(R, 0.96), shadow=False, dash="5 4")
    s.text(36, cy + 26, "Why one copy\u2019s age is not a date", 14, True, INK)
    cav = ["Rate choice: the script has no default rate; EDTA falls back to a rice rate of 1.3e-8 per bp per year if --u is not set, which must not be used for grape silently.",
           "Gene conversion between the two LTRs erases differences and makes old copies look young; recombination with other copies can do the opposite.",
           "Use the distribution over many intact copies of a family, not a single value (book chapter 6.1.1)."]
    yy = cy + 52
    for c_ in cav:
        for w_ in wrap(c_, 12.5, W - 90):
            s.text(50, yy, w_, 12.5, False, INK); yy += 18
        yy += 6
    s.text(W - 20, H - 10, "Schematic. Formula and caveats from book chapter 6.1.1 and README; toy numbers from the repository test data.", 11, False, MUTED, "end")
    return s

figs = {"te_workflow_v2": workflow, "te_question_to_tools_v2": decision, "te_ltr_age_concept_v2": ltr_age}
for name, fn in figs.items():
    s = fn()
    ov = s.save(os.path.join(OUT, name + ".svg"))
    print(name, s.w, s.h, "overflow:", ov)
