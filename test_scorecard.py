"""Table 1 tree reproduces published codes; independent pass agrees 21/22."""

from __future__ import annotations

import json
from pathlib import Path

from scorecard import Flags, score

HERE = Path(__file__).resolve().parent
ROWS = json.loads((HERE / "scorecard_rows.json").read_text())["rows"]


def test_tree_matches_published() -> None:
    mismatches: list[str] = []
    for row in ROWS:
        flags: Flags = row["flags"]
        got = score(flags)
        if got != row["published"]:
            mismatches.append(f"{row['id']}: tree={got} published={row['published']}")
    assert mismatches == [], mismatches


def test_independent_disagrees_only_on_row_9() -> None:
    independent = {row["id"]: row.get("independent") for row in ROWS}
    assert independent["9"] == "P"
    disagreed = [
        row["id"]
        for row in ROWS
        if row.get("independent") and row["independent"] != row["published"]
    ]
    assert disagreed == ["9"]


def test_contradiction_beats_same_event() -> None:
    flags: Flags = {
        "internals_only": False,
        "two_contradict": True,
        "two_independent_same_event": True,
        "uncontested_first_party_own": True,
        "metr_only_count": False,
        "single_uncorroborated": False,
        "assert_plus_scope_out": False,
    }
    assert score(flags) == "C"


def test_contradiction_beats_internals() -> None:
    flags: Flags = {
        "internals_only": True,
        "two_contradict": True,
        "two_independent_same_event": False,
        "uncontested_first_party_own": False,
        "metr_only_count": False,
        "single_uncorroborated": False,
        "assert_plus_scope_out": False,
    }
    assert score(flags) == "C"


def test_established_beats_internals() -> None:
    flags: Flags = {
        "internals_only": True,
        "two_contradict": False,
        "two_independent_same_event": True,
        "uncontested_first_party_own": False,
        "metr_only_count": False,
        "single_uncorroborated": False,
        "assert_plus_scope_out": False,
    }
    assert score(flags) == "E"


if __name__ == "__main__":
    test_tree_matches_published()
    test_independent_disagrees_only_on_row_9()
    test_contradiction_beats_same_event()
    test_contradiction_beats_internals()
    test_established_beats_internals()
    print(f"ok: {len(ROWS)} published rows match the tree")
