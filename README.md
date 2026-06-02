# AI-SalesForge

AI-SalesForge is a full-suite, enterprise-grade **Multi-Agent Sales Engine** built inside Claude Code. It autonomously drives your entire B2B revenue pipeline—from raw intent signals and domain URLs to psychological objection handling, competitive positioning, and closed-loop deal acceleration.

Powered by 5 dynamically orchestrated parallel agents, it combines automated prospecting, hyper-personalized email outreach, and psychological objection-handling frameworks. Specialized subagents orchestrate lead qualification, competitive intelligence gathering, and real-time sales strategy adaptation across your entire pipeline.

---

## 🚀 Key Overhauls & Architectural Enhancements

This repository represents a complete production hardening of the baseline CLI sales script engine, introducing strict state-management safeguards, psychological framing systems, and analytical tracking across your entire go-to-market motion.

### 🧠 1. Psychological Objection Dominance (`skills/sales-objections/`)

Replaced basic narrative pushback guidelines with a comprehensive, 895-line operational matrix detailing four core high-resistance defense architectures:

- **LQS (Label → Question → Silence):** Tactical labeling to lower cognitive barriers and defuse pressure.
- **MIC (Mirror → Implication Chain → Permission Close):** Structural framing that leverages behavioral loss aversion to isolate the economic cost of inaction.
- **AAR (Accusation Audit → Reversal):** Preemptive defense mechanisms engineered to neutralize baseline skepticism in cold accounts.
- **FCA (Future Pace → Cost Anchor → Autonomy Return):** Long-term valuation anchoring balanced with immediate preservation of prospect agency.
- **Enforced with pattern interrupts, explicit timed conversational silences, and binary disqualification gates across 15 enterprise-level buying objections.**

### 🛡️ 2. Autonomous Initialization & Data Quality Gates (`agents/sales-strategy.md`)

- **Initialization Gate:** `Agent 5 (sales-strategy)` executes an integrated validation pass over incoming payloads before spinning up the sub-agent cluster.
- **Fallback Vectors:** Structural data gaps dynamically redirect execution paths. Missing data points trigger immediate identity extraction steps; unverified intent vectors run localized hypothesis testing against closed-loop email signatures.
- **State Management:** All operational state is persisted in locked YAML registry files to prevent mid-pipeline desynchronization.

### 📊 3. Two-Pass Math Weighting Engine (`scripts/lead_scorer.py`)

Upgraded lead qualification mathematics from simple keyword tracking into a two-tiered analytics pipeline:

- **Pass 1 (Surface Mining):** Extracts open-web firmographics and standard digital intent signals.
- **Pass 2 (Agent Enrichment):** Reads, maps, and merges specialized agent-written behavioral data (`SIGNAL-DATA.json`).
- **Delta Metric:** Directly surfaces the performance delta between surface data and deep agent context to mathematically track your actual pipeline enrichment leverage.

### 🔄 4. Closed-Loop Context Alignment & Continuous Intel

- **`sales-competitive.md` & `COMPETITIVE-LIBRARY.md`:** The competitive intelligence agent continuously tracks adversary patterns, loop-referencing historical logs on every runtime path and updating market context with weaponized positioning frameworks.
- **`sales-prep.md` & `OBJECTION-PLAYBOOK.md`:** If an objection playbook is present, Rule 7 forces the preparation agent to extract word-for-word tactical scripts directly into Section 8 of your outreach email, ensuring message consistency at scale.
- **`sales-icp.md`:** The `/sales icp refine` sub-command parses your historical outreach logs, detects behavioral commonalities among top-tier prospects, and adjusts the core ICP structure with statistical confidence intervals.

---

## 📊 Terminal Interface & Command Suite

Type a command inside Claude Code to launch the specialized multi-agent pipeline:

```bash
> /sales prospect https://target-prospect.com

Phase 1: Discovering company information...
 ✓ Homepage fetched — SaaS / B2B Enterprise detected
 ✓ 6 core subpages extracted (about, solution, pricing, careers, blog, contact)
 ✓ analyze_prospect.py — 23 core data points mapped to disk

Phase 2: Running parallel analysis (5 specialized agents)...
  [Agent 1] Company Research  ──> Fit Score: 91/100
  [Agent 2] Contact Discovery ──> 6 decision makers mapped (Buying Committee)
  [Agent 3] Opportunity Core  ──> BANT + MEDDIC validation complete
  [Agent 4] Competitive Intel ──> 4 market adversaries isolated & logged
  [Agent 5] Swarm Strategy    ──> Passed Data Quality Gate; structural check OK

Phase 3: Synthesizing results...
 ✓ Prospect Score: 88/100 (Grade A)
 ✓ Top Target Located: [VP of Infrastructure] — Strong proxy signal detected
 ✓ Core Opening Angle: Active engineering hiring surge + legacy platform friction
 💾 Output Saved: PROSPECT-ANALYSIS.md
```

---

## 📁 Repository Structure

```
.
├── agents/
│   ├── sales-strategy.md       # Swarm Orchestrator & Data Quality Gate
│   ├── sales-competitive.md    # Continuous Threat Matrix Loop
│   ├── sales-company.md        # Firmographic Processing Core
│   ├── sales-contacts.md       # Identity & Target Committee Mapper
│   └── sales-opportunity.md    # Dynamic Intent Pipeline Agent
├── skills/
│   ├── sales-objections/       # LQS, MIC, AAR, FCA Psychological Engines
│   ├── sales-icp/              # Automated Analytics & Profile Diff Engine
│   ├── sales-prep/             # Playbook-Synced Briefing Generation
│   ├── sales-followup/         # Context-Locked Nurture Automation
│   └── [Other Skills]          # Core handlers (Prospect, Research, Qualify, etc.)
├── templates/
│   ├── COMPETITIVE-LIBRARY.md  # Long-term marketplace intelligence tracking
│   ├── OUTREACH-LOG.md         # Validated outreach state registry
│   ├── ROI-BENCHMARKS.md       # Economic justification milestones
│   ├── MARKET-CONTEXT.md       # Regional tool behavior & cultural overrides
│   └── OBJECTION-PLAYBOOK.md   # Script injection mapping asset
└── scripts/
    ├── lead_scorer.py          # Two-Pass Math Scoring Script
    ├── contact_finder.py       # Verification Mining Protocol
    └── generate_pdf_report.py  # Automated Report Compilation Script
```

---

## 🎯 Core Features

### Automated Prospecting
- Intent signal detection and domain analysis
- Firmographic extraction and enrichment
- Buying committee identification and mapping

### Hyper-Personalized Outreach
- Dynamic email generation based on prospect context
- Playbook-synced messaging frameworks
- Multi-touch nurture sequences

### Psychological Objection Handling
- LQS, MIC, AAR, FCA tactical frameworks
- Pattern interrupt deployment
- Binary disqualification gates

### Competitive Intelligence
- Continuous threat matrix monitoring
- Market positioning weaponization
- Historical pattern referencing

### Closed-Loop Analytics
- Two-pass lead scoring (surface + agent enrichment)
- Delta metric tracking
- Performance benchmarking

---

## 🔧 Getting Started

1. Clone this repository
2. Configure your sales ICP and market context in `templates/`
3. Load the specialized sales agents into Claude Code
4. Use `/sales prospect [URL]` to begin autonomous pipeline analysis

---

## 📝 License

[Add your license information here]

## 👤 Author

Created by [Your Name/Organization]

---

**AI-SalesForge** — Your enterprise-grade, psychology-driven sales acceleration engine.