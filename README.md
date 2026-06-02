# AI-SalesForge
A full-suite AI Sales Agents that handle your entire pipeline, combining auto prospecting, personalized email outreach, and psy-ops sales objection handling. Equipped with specialized subagents and advanced skills, scripts and workflows with dynamic hand-on agent interactions and context awareness for the entire funnel. 

# AI Sales Forge 🛠️💼

An advanced, enterprise-grade Multi-Agent Sales Engine running inside Claude Code. Optimized to dynamically orchestrate 5 specialized parallel agents alongside deterministic data quality gates and psychological objection defusal frameworks. 

AI Sales Forge transforms raw intent signals and domain URLs into deeply contextualized, high-conversion B2B outreach, structured qualifying scoring, and playbook-aligned meeting frameworks—entirely driving your enterprise revenue pipeline from the command line.

---

## 🚀 Key Overhauls & Architectural Enhancements

This repository represents a complete production hardening of the baseline CLI sales script engine, introducing strict state-management safeguards, psychological framing systems, and analytical tracking algorithms:

### 🧠 1. Psychological Objection Dominance (`skills/sales-objections/`)
Replaced basic narrative pushback guidelines with a comprehensive, 895-line operational matrix detailing four core high-resistance defense architectures:
*   **LQS (Label → Question → Silence):** Tactical labeling to lower cognitive barriers and defuse pressure.
*   **MIC (Mirror → Implication Chain → Permission Close):** Structural framing that leverages behavioral loss aversion to isolate the economic cost of inaction.
*   **AAR (Accusation Audit → Reversal):** Preemptive defense mechanisms engineered to neutralize baseline skepticism in cold accounts.
*   **FCA (Future Pace → Cost Anchor → Autonomy Return):** Long-term valuation anchoring balanced with immediate preservation of prospect agency.
*   *Enforced with pattern interrupts, explicit timed conversational silences, and binary disqualification gates across 15 enterprise-level buying objections.*

### 🛡️ 2. Autonomous Initialization & Data Quality Gates (`agents/sales-strategy.md`)
*   **Initialization Gate:** `Agent 5 (sales-strategy)` executes an integrated validation pass over incoming payloads before spinning up the sub-agent cluster.
*   **Fallback Vectors:** Structural data gaps dynamically redirect execution paths. Missing data points trigger immediate identity extraction steps; unverified intent vectors run localized hypothesis testing; low firmographic certainty degrades lead tier mapping automatically to protect your downstream deliverability.

### 📊 3. Two-Pass Math Weighting Engine (`scripts/lead_scorer.py`)
Upgraded lead qualification mathematics from simple keyword tracking into a two-tiered analytics pipeline:
*   **Pass 1 (Surface Mining):** Extracts open-web firmographics and standard digital intent signals.
*   **Pass 2 (Agent Enrichment):** Reads, maps, and merges specialized agent-written behavioral data (`SIGNAL-DATA.json`).
*   **Delta Metric:** Directly surfaces the performance delta between surface data and deep agent context to mathematically track your actual pipeline enrichment leverage.

### 🔄 4. Closed-Loop Context Alignment & Continuous Intel
*   **`sales-competitive.md` & `COMPETITIVE-LIBRARY.md`:** The competitive intelligence agent continuously tracks adversary patterns, loop-referencing historical logs on every runtime path and updating a persistent library to scale tactical edge.
*   **`sales-prep.md` & `OBJECTION-PLAYBOOK.md`:** If an objection playbook is present, Rule 7 forces the preparation agent to extract word-for-word tactical scripts directly into Section 8 of your generated meeting briefs.
*   **`sales-icp.md`:** The `/sales icp refine` sub-command parses your historical outreach logs, detects behavioral commonalities among top-tier prospects, and adjusts the core ICP structure with a clean markdown `before/after` diff.

---

## 📊 Terminal Interface & Command Suite

Type a command inside Claude Code to launch the specialized multi-agent pipeline:

```bash
> /sales prospect [https://target-prospect.com](https://target-prospect.com)
