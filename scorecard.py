"""Executable Table 1 decision tree.

Given recorded evidence flags for a claim, return exactly one of E, C, N, P.
The flags are human (or second-coder) judgments; the tree is mechanical.

Order matches the codebook: C, then E, then P, then N.
"""

from __future__ import annotations

from typing import Literal, TypedDict

Score = Literal["E", "C", "N", "P"]


class Flags(TypedDict):
    internals_only: bool
    two_contradict: bool
    two_independent_same_event: bool
    uncontested_first_party_own: bool  # uncontested first-party account of that party's own action
    metr_only_count: bool
    single_uncorroborated: bool
    assert_plus_scope_out: bool


def score(flags: Flags) -> Score:
    """Apply Table 1. C wins over E and P; E wins over P; P is residual internals."""
    if flags["two_contradict"]:
        return "C"
    if flags["two_independent_same_event"] or flags["uncontested_first_party_own"]:
        return "E"
    if flags["internals_only"]:
        return "P"
    return "N"


def empty_flags() -> Flags:
    return {
        "internals_only": False,
        "two_contradict": False,
        "two_independent_same_event": False,
        "uncontested_first_party_own": False,
        "metr_only_count": False,
        "single_uncorroborated": False,
        "assert_plus_scope_out": False,
    }
