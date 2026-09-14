"""One-command replay of frozen quotes, Table 1B traces, and published codes.

Does not score source sentences. Does not claim validation.
Run: python3 replay.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from scorecard import score


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower()

HERE = Path(__file__).resolve().parent
REPORT = HERE / "report.md"
VERBATIM = [
    "steal the test solutions rather than solve the challenge on its own.",
    "The Hugging Face security response team then cut access.",
    "paged our security team more than a day before",
    "stopping the evaluation run was not required",
    "OpenAI detected suspicious internal activity on July 19.",
    "in a way their developers did not intend (writing to the internet was blocked)",
]

# Frozen quotes checked against cached public fetches (whitespace-normalized).
# Reuters is captcha-gated here; do not fake a hit.
SOURCE_QUOTES = [
    ("hf_timeline.txt", "steal the test solutions rather than solve the challenge on its own"),
    ("hf_timeline.txt", "The Hugging Face security response team then cut access"),
    ("openai_tech.txt", "stopping the evaluation run was not required"),
    ("openai_tech.txt", "paged our security team more than a day before"),
    ("openai_tech.txt", "OpenAI detected suspicious internal activity on July 19"),
    ("metr_local.txt", "primarily motivated by understanding the implementation of the scorer rather than stealing answer keys"),
    ("cesia.txt", "Hugging Face detected the intrusion but could not trace its source"),
    ("anthropic.txt", "stopped all cyber evaluations the same day"),
    ("aisi.txt", "Every model we have tested for this behaviour attempted to cheat"),
    ("collusion.txt", "we believe this is distinct from the swarm of agents that hacked Hugging Face"),
    ("collusion.txt", "in a way their developers did not intend (writing to the internet was blocked)"),
    ("vectra.txt", "detection worked"),
    ("vectra.txt", "Both teams caught the activity independently"),
    ("vectra.txt", "That is the only difference from Hugging Face"),
]


def main() -> int:
    rows = json.loads((HERE / "scorecard_rows.json").read_text())["rows"]
    traces = json.loads((HERE / "table1b_traces.json").read_text())["rows"]
    recode = json.loads((HERE / "recode_results.json").read_text())
    manifest = json.loads((HERE / "source_sentence_manifest.json").read_text())
    report = REPORT.read_text()

    errors: list[str] = []

    for row in rows:
        got = score(row["flags"])
        if got != row["published"]:
            errors.append(f"tree {row['id']}: {got} != {row['published']}")

    by_id = {row["id"]: row for row in rows}
    for tr in traces:
        pub = by_id[tr["id"]]["published"]
        if tr["code"] != pub:
            errors.append(f"trace {tr['id']}: {tr['code']} != published {pub}")
        flags = by_id[tr["id"]]["flags"]
        if tr["branch"] in flags and not flags[tr["branch"]] and tr["branch"] != "no_identity_asserted":
            errors.append(f"trace {tr['id']}: branch {tr['branch']} not set on flags")

    agree = recode["core_table_3"]["agree"]
    disagree = [d["id"] for d in recode["core_table_3"]["disagree"]]
    n_core = len(agree) + len(disagree)
    expected = f"{len(agree)}/{n_core}"
    if recode["core_table_3"]["raw_agreement"] != expected:
        errors.append(
            f"recode raw_agreement {recode['core_table_3']['raw_agreement']} != {expected}"
        )
    if n_core != 9:
        errors.append(f"recode core must cover 9 rows, got {n_core}")
    if disagree:
        errors.append(f"recode disagree ids drifted: {disagree}")

    for quote in VERBATIM:
        if quote not in report:
            errors.append(f"verbatim missing from report.md: {quote[:40]}")

    cache = HERE / "quote_cache"
    for fname, quote in SOURCE_QUOTES:
        path = cache / fname
        if not path.exists():
            errors.append(f"cache missing {fname}")
            continue
        blob = _norm(path.read_text(errors="replace"))
        if _norm(quote) not in blob:
            errors.append(f"source miss {fname}: {quote[:50]}")
    reuters = cache / "reuters.txt"
    if reuters.exists() and "Please enable JS" in reuters.read_text(errors="replace"):
        print("  reuters: captcha-gated (no fake hit)")

    unit_ids = {u["id"] for u in manifest["units"]}
    for need in ["14", "15", "H5"]:
        if need not in unit_ids:
            errors.append(f"manifest missing unit {need}")
    u15 = next(u for u in manifest["units"] if u["id"] == "15")
    srcs = {s["src"] for s in u15["sentences"]}
    if srcs != {"Reuters", "Hugging Face"}:
        errors.append(f"unit 15 sources {srcs} (want Reuters vs Hugging Face)")

    print("replay: frozen quotes, Table 1B, published codes")
    print(f"  scorecard rows     {len(rows)}")
    print(f"  Table 1B traces    {len(traces)}")
    print(f"  manifest units     {len(manifest['units'])}")
    print(f"  recode core        {recode['core_table_3']['raw_agreement']}")
    if errors:
        print("FAIL")
        for e in errors:
            print(" ", e)
        return 1
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
