# Figures

This tree ships `F1_hierarchy.v2.svg`, `F5_helitron_maverick.v2.svg`, `F3_line_sine.v2.svg`, `F4_tir_mite.v2.svg`, and the unversioned F2, F6, F7 and F8 drawings. F1 was drawn by `scripts/figures/draw_te_schematics.v4.py` and is unchanged in label content from the previous versioned drawing of that figure. F2, F3, F4, F5 and F7 were redrawn by the same v4 script (F5 adds a [待确认] marker on the typical plant Helitron end wording). F6 and F8 are unchanged in label content from the earlier drawings of those figures.

The earlier unversioned files `F1_hierarchy.svg`, `F5_helitron_maverick.svg`, `F3_line_sine.svg` and `F4_tir_mite.svg`, and the scripts `draw_te_schematics.py`, `draw_te_schematics.v2.py` and `draw_te_schematics.v3.py`, are not included here. They were never on the live main branch of this repository. They remain in earlier copies of these teaching files and have not been deleted. The unversioned F1 and F5 files, and the original script, still carry unmarked Wicker 2007 body / Fig. 1 wording; do not teach from them.

They are original teaching schematics, not copies of journal figures.

Run (from a new empty output directory, with bytecode writing disabled):

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/figures/draw_te_schematics.v4.py OUTDIR
```

The script refuses to overwrite an existing file.
