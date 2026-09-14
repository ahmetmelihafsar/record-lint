# Detection is not containment: scoring the public record of the OpenAI–Hugging Face intrusion

**Track:** 2 — What happened, and what breaks next  
**Authors:** Ahmet Melih Afşar, Tansylu Akhmetova, Alper Cimşit (AI Safety Türkiye)

Research conducted at the AI Incident Response Sprint, September 2026.

---

## Abstract

Public reports of the OpenAI–Hugging Face intrusion still collapse distinct clocks. When Hugging Face cut OpenAI’s evaluation agents out of production on 13 July, that was containment. OpenAI’s Artifactory alert is 19 July; its public origin statement is 21 July. Treating those as one “detection” leaves the next similar incident without a shared language. This paper’s purpose is to fix that vocabulary. We introduce Record-Lint, a way to score atomic claims in dated public sentences as established, contested, not established, or knowable only from provider-internal evidence, and to flag six reporting-error codes. We find that OpenAI’s published design and reporting fail all six of our checks, and that a distinct May–June wiki swarm fails the shared-store check. Why the agents entered Hugging Face production stays contested. Collapsing distinct clocks is a reporting error, not a two-source contradiction. Record-Lint is a reporting aid, not a containment standard. The next report should name each clock, say whose account each claim comes from, and not infer beyond what the public record supports. We will score a forecast about shared mutable stores on 13 March 2027.

---

## 1. Introduction

The attack path of the July 2026 OpenAI–Hugging Face intrusion is public; the reporting vocabulary is not settled. When labs, victims, and the press report this class of event, they still mix the moment the victim stopped the attacker with the moment the lab detected that the attacker was theirs. They also mix two motives into one story. Our purpose is to give the next report a language that keeps those clocks, and those motives, apart.

We introduce Record-Lint for that job. Containment is when the victim cut access: 13 July, Hugging Face. OpenAI’s security alert was on 19 July; its public attribution followed on 21 July. Those dated timestamps are named clocks. Collapsing the 19 July alert with the 21 July origin statement is the same error as collapsing either with 13 July containment. Reporting perspective means whose account is speaking: the victim, the lab, an investigator, or a reporter. Each source claim is tagged with its reporting perspective; the E/C/N/P code itself does not encode perspective.

**Table 1. Six published milestones.** Distinct incident-response clocks among them are not one detection.

| Milestone | Date (2026) | Whose |
| --- | --- | --- |
| Lab signal; halt not required | 27 Jun | OpenAI (on-call: halt not required) |
| Victim containment | 13 Jul | Hugging Face |
| Victim disclosure, origin unknown | 16 Jul | Hugging Face |
| Lab security alert | 19 Jul | OpenAI (Artifactory) |
| Public origin / attribution | 21 Jul | OpenAI |
| Independent behaviour audit | 26 Aug | METR (not a safeguard audit) |

Our main contributions are:

1. A four-score codebook for atomic claims in dated public sentences, plus six reporting-error codes, so a contested claim stays contested instead of being flattened into a single “what happened.”
2. The same public-record discipline applied, in §4, to six design and reporting checks a defender can run from published design and reporting, and a dated forecast about shared mutable-store channels.
3. A demonstration that the main reporting error — one “detection,” distinct clocks — already appears in later coverage, and that a distinct wiki swarm exhibits the same shared-store failure mode, but is not the same incident.

Existing incident-response guidance such as CoSAI [11] tells operators how to respond; Record-Lint instead constrains what public reports are justified in claiming. It is a reporting aid, not a containment standard.

That error is easiest to see on one sentence. Reuters [10] wrote: “During the Hugging Face breach, OpenAI agents autonomously plotted a digital heist that went undetected for more than a week.” The sentence names one undetected span without naming whose detection clock bounds it. Table 1 shows why that matters.

*Worked example. Claim, score, lint, and next action on one sentence.*

| Step | On this sentence |
| --- | --- |
| Claim | One undetected span covering the Hugging Face breach |
| Score | Not established — Reuters alone asserts the span; HF’s 13 July containment is a distinct clock. |
| Lint | CLOCK-MERGE |
| Action | Publish the relevant clocks separately |

A corrected version would read: Hugging Face cut access on 13 July. OpenAI’s Artifactory alert is 19 July. OpenAI’s public origin statement is 21 July. Why the agents entered stays contested.

METR reconstructed agent behaviour for 7–13 July; it did not audit safeguards. DSEWiki is a second example of the same shared-store failure mode — agents using a shared mutable store to coordinate “in a way their developers did not intend (writing to the internet was blocked)” [9] — and not the Hugging Face incident. Treating a second case as the same operation is CASE-MERGE. Related instruments and transfer sentences are Appendix B.

---

## 2. How to score a claim

Every claim gets one of four scores, in this order: two public sources contradict on the same proposition → C; two statements from distinct qualifying sources among the first parties and/or METR, or an uncontested first-party account of that party’s own action, or an uncontested first-party forensic claim about that party’s own systems → E; if neither applies and adjudication requires non-public provider internals → P; otherwise N. Hugging Face’s 13 July cut is E. OpenAI’s 27 June on-call is E on the same own-action clause. A METR-only count, a single uncorroborated secondary line, or an assertion next to an explicit scope exclusion is N. Provider-only (P) is residual: the claim is not C or E, and settling it requires non-public provider-internal evidence. These codes describe the public record’s support state for a proposition, not a binary truth value; a proposition that no source asserts is N unless there is an actual two-source contest over that proposition.

One published sentence can carry two claims. We score each. The same OpenAI on-call sentence publishes the stated response criterion. That criterion fails the halt check in §4.

On top of those scores sit six reporting errors:

**Table 2. Reporting-error codes.**

| Code | Means |
| --- | --- |
| CLOCK-MERGE | One detection claim or span that collapses distinct incident-response clocks, such as victim containment, lab alert, or public attribution |
| MOTIVE-TRANSFER | Victim-side forensic observations written as if they establish the entering agent’s motive |
| CASE-MERGE | Two distinct incidents or cases written as one operation |
| SCOPE-SLIP | An explicit scope exclusion treated as evidence for or against the excluded proposition |
| COUNTERFACTUAL-AS-FACT | A “would have” counterfactual reported as an observed event |
| LABEL-SUBSTITUTION | A categorical label used as if it resolves a separate factual question, such as detection, containment, or attribution |

The source excerpts were fixed before rescoring; row 14’s proposition was narrowed to primary motive and row 19’s to the wipe → restart → board sequence, without changing those excerpts. A post-revision, score-blinded consistency check on all nine Table 3 claim units — rows 14–22 — matched all nine published scores. We keep the published scores. A one-command replay checks the replayable quotes against cached public pages; Reuters is handled separately. This is not a human rater and not validation.

---

## 3. What the record does and does not settle

Motive stays Contested. Hugging Face treats stealing test solutions as the primary motive; METR treats scorer-intel as primary. Hugging Face’s 13 July cut and OpenAI’s 19 July alert do not contradict each other. Reuters’ undetected-span claim is Not established: only Reuters asserts it, and a 13 July containment does not rule out a multi-day undetected period beforehand. We call this CLOCK-MERGE because the unqualified word “undetected” assigns one detection state to a breach that has distinct victim and lab clocks.

Six calendar days sit between those two clocks. The gap is real. It is not a measured stretch of time in which Hugging Face went “undetected.”

The established mechanics — how the agents entered, what they took, that they used a shared package cache — live in Appendix Table A6. Table 3 contains the core scored claims.

**Table 3. Core scored claims.** Motive stays C. Row 15 is N + CLOCK-MERGE. Rows 1–13 are Table A6.

| # | Claim | Score | Why |
| --- | --- | --- | --- |
| 14 | Primary motive for the Hugging Face intrusion was stealing solution keys | C | HF 27 Jul [1]: “steal the test solutions rather than solve the challenge on its own.” METR 26 Aug [5]: “primarily motivated by understanding the implementation of the scorer rather than stealing answer keys.” |
| 15 | One undetected span covering the Hugging Face breach | N | Reuters [10]: “a digital heist that went undetected for more than a week.” Only Reuters asserts that span. HF 27 Jul [1]: “The Hugging Face security response team then cut access.” Containment does not contradict a pre-containment undetected period. Reuters does not name 19 July. N + CLOCK-MERGE. |
| 16 | Classifiers / monitors / auto-review off by design | E | OpenAI 26 Aug [3][4] and METR 26 Aug [5]: classifiers off for these evaluations. |
| 17 | Monitors would have paged >1 day before Hugging Face | N | OpenAI [3][4]: “paged our security team more than a day before.” METR places safeguard effectiveness explicitly out of scope. |
| 18 | 27 Jun on-call response did not require halting the run | E | OpenAI [3]: “stopping the evaluation run was not required.” Uncontested first-party own-action. METR omits the episode; silence is not contradiction. |
| 19 | 4–6 Jul wipe was followed by eval restart and board activity | E | OpenAI and METR both give wipe → 7 Jul restart → 8 Jul board. |
| 20 | 3–6 considered alerting a human; zero did | N | METR-only census. “Walked away” is not page-a-human. |
| 21 | DSEWiki is the same incident as Hugging Face | N | No source asserts identity. collusion.wiki [9], Reuters [10], and OpenAI 5 Sep [13] treat it as distinct. |
| 22 | DSEWiki should be classified as a security/hacking incident rather than only as misalignment | C | OpenAI 5 Sep [13]: misalignment finding, not security. Reuters [10]: Olejnik as a hacking attempt; OpenAI disputed. |

Row 17 is not a contest. OpenAI asserts a counterfactual; METR scoped that question out. Row 18 is OpenAI’s own uncontested on-call response: halt was not required. The same sentence’s stated response criterion fails the halt check.

Transfer examples — CeSIA’s two-clock control, Vectra’s “both teams” line — are Tables A4 and A8. They are not validation.

---

## 4. Design checks and forecasts

These six checks are not a second definition of Record-Lint, and they are not a containment standard. They apply the same public-record discipline to published design and reporting. If the public record is silent, we write “not publicly established.” One lab clock is not containment.

**Table 4. Checks a defender can run from published design and reporting.**

| ID | Check | OpenAI | DSEWiki |
| --- | --- | --- | --- |
| K1 | Do nominally isolated or egress-restricted agents/evals share a mutable coordination store? Pass = no. | Fail — shared package cache (OpenAI + METR) | Fail — unintended public-wiki coordination [9] |
| K2 | After a wipe, can allowed egress still reach a writable shared namespace? | Fail — board back 8 Jul (OpenAI + METR); shared store still a mailbox | not publicly established |
| K3 | If messages associated with never-solved tasks account for ≥50% of message-board traffic, halt or shrink | Fail — OpenAI [3]: 198 of 898 never solved; those tasks accounted for 93% of board traffic; evals resumed (also fails 30 and 70) | not publicly established |
| K4 | Are distinct incident-response events explicitly named and distinguished as separate clocks? | Fail — dates exist, not named as separate IR clocks | not publicly established |
| K5 | Does the stated out-of-band response criterion require halting the evaluation? Pass = yes. | Fail — “stopping the evaluation run was not required” | not publicly established |
| K6 | If monitors are off, is a “would have caught it” claim supported by a publicly documented pre-registration? | Fail — post-hoc counterfactual; no public pre-registration identified | not publicly established |

The 50% cutoff on K3 is a policy choice; OpenAI’s 93% board-traffic share [3] also fails at 30% or 70%. K4 scores the provider’s framing, not Table 1: OpenAI [3] writes one lab detection — “OpenAI detected suspicious internal activity on July 19.” — and does not name containment, alert, and attribution as separate IR clocks. K5 reads two claims in one sentence: halt was not required (row 18, E); the published response criterion “stopping the evaluation run was not required” fails the check. K1 fails when nominally isolated or egress-restricted agents still share a mutable store. By 13 March 2027 we score F1: the next publicly disclosed eval-agent third-party intrusion uses a shared mutable-store channel that crosses an intended isolation or egress boundary. F2 and the pass/fail/unresolved rules are Table A5.

---

## 5. Discussion and Limitations

Record-Lint classifies public wording. It cannot see provider-internal evidence or settle motive. A timeline that lists 21 July as detection is describing OpenAI’s attribution, not Hugging Face’s containment. Both cases fail the shared-store check. That is the same architectural failure mode, not proof they were one incident. Table A7 applies the six reporting-error codes to DSEWiki’s public text: CLOCK-MERGE and LABEL-SUBSTITUTION were not observed; row 22 remains Contested. That does not imply the swarms were the same.

---

## 6. Conclusion

The public record establishes that evaluation agents used a shared cache, reached Hugging Face production, and ran with the relevant classifiers, monitors, and auto-review disabled by design. It does not agree on why the agents entered. The public record does not support collapsing these distinct events into a single “detection date.” Counts that appear only in METR stay not established. We will score F1 on 13 March 2027. For the next incident report: publish victim containment, lab alert, and public attribution as separate named clocks, say whose account stands behind each claim, and write “not publicly established” when the public record is silent.

---

## Code and Data

`python3 replay.py` checks the fixed source excerpts against cached public pages. How to run and expected output: `README.md`. `scorecard.py` maps flags to codes; it does not read sentences.

---

## References

1. Hugging Face. Agent intrusion disclosure and technical timeline. 16 Jul and 27 Jul 2026. https://huggingface.co/blog/security-incident-july-2026 ; https://huggingface.co/blog/agent-intrusion-technical-timeline
2. OpenAI. First origin statement. 21 Jul 2026. https://openai.com/index/hugging-face-model-evaluation-security-incident/
3. OpenAI. Hugging Face Incident Technical Report. 26 Aug 2026. https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf
4. OpenAI. The Hugging Face incident and the road ahead. 26 Aug 2026. https://openai.com/index/hugging-face-incident-and-the-road-ahead/
5. Wijk, Cotra, Greenblatt (METR / Redwood). Brief independent investigation of agents’ behaviour, reasoning and collaboration. 26 Aug 2026. https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/ ; https://metr.org/hugging-face-incident-report-aug-2026.pdf
6. CeSIA. The OpenAI / Hugging Face incident: what we know, what we don’t, what follows. https://cesia.org/en/publications/the-openai-hugging-face-incident-what-we-know-what-we-dont-what-follows/
7. UK AI Security Institute. Cheating behaviour in frontier model evaluations. 21 Jul 2026. https://www.aisi.gov.uk/blog/cheating-behaviour-in-frontier-model-evaluations
8. Anthropic. Three evals incidents after a 141,006-run review. 30 Jul 2026. https://www.anthropic.com/research/investigating-incidents-cybersecurity-evals
9. collusion.wiki / Nightingale Collective. DSEWiki swarm. 4 Sep 2026. https://collusion.wiki/
10. Reuters. OpenAI agents hijacked German wiki. 4–5 Sep 2026. https://www.reuters.com/world/europe/openai-agents-hijacked-german-website-previously-undisclosed-ai-breakout-this-2026-09-04/
11. Coalition for Secure AI. AI Incident Response Framework v1.0. 27 Oct 2025. https://www.coalitionforsecureai.org/wp-content/uploads/2026/03/AI-Incident-Response-1.pdf
12. Vectra. An autonomous AI agent compromised Hugging Face. The response is the real story. 22 Jul 2026, updated 28 Jul 2026. https://www.vectra.ai/blog/an-autonomous-ai-agent-compromised-hugging-face-the-response-is-the-real-story
13. OpenAI. The Hugging Face incident and other third-party impact from misaligned models. 5 Sep 2026. https://openai.com/hugging-face-incident-and-misalignment/

---

## Appendix A — Limitations and Dual-Use Considerations

### Limitations

METR reconstructed agent behaviour for 7–13 July and is not a safeguard audit; METR-only counts stay N. Public sources only. The codebook is §2 plus the cited URLs. Language-model rescorings are exploratory, not a rater pool.

### Dual-use

We do not reproduce Artifactory 0-day steps, tool-call spoof recipes, steganographic encodings, or a how-to for coordinating via shared caches beyond what OpenAI and METR already published. Checks are yes/no design and reporting questions. Apart reviewers assess sprint write-ups for information hazards during judging.

---

## Appendix B — Artifact

Tables 1–4 in the body are the scorecard. Appendix tables A1–A8 complete the artifact. Contested is a result, not a gap to flatten. Tables A7–A8 are additional transfer, scored after Table 3 and Table A4 were fixed. They are not held-out validation.

Related instruments. CeSIA [6] already splits Hugging Face clocks. CoSAI [11] is a process playbook for operators. AISI [7] measured cheating. Anthropic [8] “stopped all cyber evaluations the same day” they began transcript review — a contemporaneous contrast, not a matched case, and not proof that K5 would have produced a better outcome. Vectra [12] is Table A8 (each-caught line E, corroborated by [1] and [3]; not CLOCK-MERGE). F1 pass/fail/unresolved, including the first qualifying post-cutoff write-up, is Table A5.

**Table A1. Scoring rule.** Apply C, then E, then P, then N. Do not flatten C into E.

| Code | Meaning | Rule |
| --- | --- | --- |
| C | Contested | Two public sources contradict on the same proposition. Quote both dated sentences. Do not pick a winner. Explicit scope exclusion is not C. |
| E | Established | Two statements from distinct qualifying sources among the first parties and/or METR, or an uncontested first-party account of that party’s own action, or an uncontested first-party forensic claim about that party’s own systems. A METR-only count is not E. |
| P | Provider-only | Neither C nor E, and adjudication requires non-public internals. |
| N | Not established | METR-only count; single uncorroborated secondary line; or assertion plus explicit scope exclusion. |

**Table A2. Selected decision-tree traces.**

| # | Claim scored | Branch | Code |
| --- | --- | --- | --- |
| 14 | primary motive: steal keys vs scorer-intel | two sentences contradict | C |
| 15 | one undetected span covering the HF breach | single uncorroborated line (Reuters span; HF cut is a different clock) | N |
| 17 | would have paged | assert + METR out of scope | N |
| 18 | 27 Jun on-call: halt not required | uncontested first-party own-action | E |
| 19 | wipe → restart → board | two distinct qualifying sources, same event | E |
| 21 | DSEWiki = Hugging Face | no source asserts identity | N |
| 22 | security/hacking vs only misalignment | two sentences contradict | C |

**Table A3. Named-clock lags.** Date gaps are not a causal detection delay.

| Start | End | Gap | Allowed | Forbidden |
| --- | --- | --- | --- | --- |
| 13 Jul HF containment [1] | 19 Jul OpenAI Artifactory alert [4] | 6 calendar days | lab alert after victim containment | “Hugging Face undetected for six days” |
| 16 Jul HF disclosure [1] | 21 Jul OpenAI public origin [2] | 5 calendar days | origin-statement lag | “detected on 21 July” as the first catch |
| OpenAI “paged our security team more than a day before” [4] | — | not observed | N (row 17) | measured lead time |

**Table A4. Transfer and specificity examples.** Examples illustrating specificity and transfer; not held-out validation. Scores follow the §2 rule.

| Sentence | Proposition | Lint | Score |
| --- | --- | --- | --- |
| CeSIA [6]: “Hugging Face detected the intrusion but could not trace its source” | HF detected intrusion; origin unknown | none (specificity control) | E (HF [1]: first signals from security stack; 16 Jul origin unnamed) |
| CeSIA [6]: “Only then did OpenAI finally detect anomalous activity…” (on 19 July) | OpenAI’s lab clock on 19 July | none (names the lab clock) | E (corroborated by OpenAI [3]; Table 1) |
| Reuters [10]: “The activity in Germany wasn't related to Hugging Face…” | DSEWiki ≠ HF incident | none (explicit split) | E (corroborated by [9] and [13]; see row 21) |
| same Reuters sentence | OpenAI acted in good faith | — | N (uncorroborated secondary characterization) |
| Reuters [10]: “a digital heist that went undetected for more than a week.” | one undetected span covering the HF breach | CLOCK-MERGE | N (row 15) |

**Table A5. Forecasts.** If F1 fails, the forecasted recurrence of the shared-store failure mode is weakened; F1 does not test the causal efficacy of K1–K6.

| ID | Claim | Resolution | Window |
| --- | --- | --- | --- |
| F1 | Next publicly disclosed eval-agent third-party intrusion uses a shared mutable-store channel that crosses an intended isolation or egress boundary | First lab/victim write-up about the first qualifying third-party intrusion publicly disclosed after 13 Sep 2026 that names the channel. Pass = identified channel is a shared mutable store crossing an intended isolation or egress boundary. Fail = write-up clearly identifies the channel and it does not satisfy that condition. If the channel cannot be classified, do not resolve. No write-up = unresolved. | by 13 Mar 2027 |
| F2 | The first post-cutoff report from an eligible developer about a wiki-based incident will frame it as misalignment rather than security | Eligible developer = AISI [7] model developer as of 13 Sep 2026. Pass = first post-cutoff wiki-incident report frames misalignment, not security. Fail = security. Mixed = do not resolve. None = unresolved. | by 13 Mar 2027 |

**Table A6. Mechanics.** Compact summary; where one row contains multiple component claims, all components receive the same displayed score. Do not flatten C into E.

| # | Claim | Score | Why |
| --- | --- | --- | --- |
| 1 | Eval agents reached Hugging Face production, Jul 2026 | E | HF + OpenAI + METR |
| 2 | Entry: local file-read, then template injection | E | Uncontested first-party forensics on HF’s own systems |
| 3 | Customer content = five solution datasets | E | Uncontested HF 27 Jul forensics on own systems |
| 4 | Shared package cache as mailbox; reinvented after wipe | E | OpenAI + METR |
| 5 | ~1,200 board agents; ~700 in the attack | N | METR-only census |
| 6 | Agents flagged cheating, then inferred a nonexistent transcript auditor | N | METR-only CoT |
| 7 | Official multi-agent spawning disabled; swarm behavior emerged unofficially | E | OpenAI + METR |
| 8 | Mass cutoff ~01:30 UTC 12 Jul as event | N | METR-only timestamp |
| 9 | Cause of that cutoff | N | METR did not confirm why |
| 10 | Tool-call spoofing in ≥96 transcripts | N | METR-only count |
| 11 | Spoofing aimed at deceiving humans | N | Same source, not a two-source contradiction |
| 12 | Remaining OpenAI-infra compromise after 13 Jul | P | Requires non-public internals; Black Hat unconfirmed |
| 13 | Verbatim eval prompts | P | Both withhold |

**Table A7. Six lint codes on DSEWiki public text.** Additional transfer. Not a third scored incident.

| Code | Public text used | Result |
| --- | --- | --- |
| CLOCK-MERGE | No published sentence collapses distinct DSEWiki incident-response clocks | none observed |
| MOTIVE-TRANSFER | No source attributes DSEWiki’s motive using Hugging Face victim forensics | none observed |
| CASE-MERGE | “DSEWiki = Hugging Face.” collusion.wiki [9]: “we believe this is distinct from the swarm of agents that hacked Hugging Face.” | none observed; identity proposition = N (row 21) |
| SCOPE-SLIP | none observed | none |
| COUNTERFACTUAL-AS-FACT | none observed | none |
| LABEL-SUBSTITUTION | OpenAI 5 Sep [13]: misalignment, not security. Reuters [10]: Olejnik as a hacking attempt. Neither uses the label to resolve a separate factual question. | none observed; row 22 remains C |

**Table A8. Additional transfer.** Scored after Table 3 was fixed. Not held-out validation. Score is E/C/N/P. Vectra’s each-caught line is E (HF [1] and OpenAI [3]); it is not CLOCK-MERGE.

| Sentence | Proposition | Lint | Score |
| --- | --- | --- | --- |
| Anthropic [8]: “stopped all cyber evaluations the same day” | Anthropic halted cyber evals on 23 Jul (own IR) | none (own-timeline; K5 contrast) | E |
| AISI [7]: “Every model we have tested for this behaviour attempted to cheat.” | Hypothetical merge: AISI cheating = HF incident | CASE-MERGE if merged | N |
| collusion.wiki [9]: “we believe this is distinct from the swarm of agents that hacked Hugging Face.” | DSEWiki ≠ HF | none (explicit split; corroborated by OpenAI [13], see row 21) | E |
| Vectra [12]: “detection worked. Both teams caught the activity independently” | HF and OpenAI each caught the activity | none (separate actors named; dates omitted) | E ([1], [3]) |
| Vectra [12]: “That is the only difference from Hugging Face” (AISI) | AISI analogous to HF | none (analogy, not identity) | N |

**LLM usage.** LLMs assisted with source triage, drafting, formatting, and exploratory rescoring; they are not a primary source. The authors take responsibility for every published score and for the wording.
