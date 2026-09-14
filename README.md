# Record-Lint

Track **2** artifact for the [Apart Research × CeSIA AI Incident Response Sprint](https://apartresearch.com/sprints/ai-incident-response-sprint-2026-09-11-to-2026-09-13) (September 2026).

**Paper:** [Detection-is-not-containment.pdf](Detection-is-not-containment.pdf)  
**Authors:** Ahmet Melih Afşar, Tansylu Akhmetova, Alper Cimşit (AI Safety Türkiye)

Record-Lint scores atomic claims in dated public sentences (E / C / N / P) and flags reporting-error codes. This repo is the runnable check: the decision tree, frozen flags, and quote replay. It does not score new sentences.

## Run

Python 3.11+. No extra packages.

```bash
python3 test_scorecard.py
python3 replay.py
```

Expected:

```
ok: 22 published rows match the tree
  reuters: captcha-gated (no fake hit)
replay: frozen quotes, Table 1B, published codes
  scorecard rows     22
  Table 1B traces    7
  manifest units     14
  recode core        9/9
ok
```

`scorecard.py` maps flags to codes. It does not read source sentences. Reuters is CAPTCHA-gated; `quote_cache/reuters.txt` is a stub, not a fake hit.

## Dual-use

This repo does not reproduce Artifactory 0-day steps, tool-call spoof recipes, or a how-to for coordinating via shared caches. `quote_cache/` holds only the frozen public sentences used by `replay.py`.
