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


| Command | Description | Output Artifact |
|---|---|---|
| `/sales prospect <url>` | Full 360° account audit launching 5 parallel agents. | `PROSPECT-ANALYSIS.md` |
| `/sales quick <url>` | Fast 60-second firmographic & visibility snapshot. | Terminal Output |
| `/sales research <url>` | Deep-dive deep web company research & metadata. | `COMPANY-RESEARCH.md` |
| `/sales qualify <url>` | Two-pass BANT + MEDDIC scoring optimization. | `LEAD-QUALIFICATION.md` |
| `/sales contacts <url>` | Maps decision-makers, buying roles, and contact gaps. | `DECISION-MAKERS.md` |
| `/sales outreach <name>` | Multi-step hyper-personalized messaging sequences. | `OUTREACH-SEQUENCE.md` |
| `/sales followup <name>` | Context-locked follow-ups synced to previous touchpoints. | `FOLLOWUP-SEQUENCE.md` |
| `/sales prep <url>` | Meeting briefing document with embedded tactical scripts. | `MEETING-PREP.md` |
| `/sales proposal <client>` | Comprehensive, ROI-benchmarked closing agreements. | `PROPOSAL-DOCUMENT.md` |
| `/sales report` | Scans OUTREACH-LOG.md to spit out dynamic pipeline health. | Terminal + PDF Option |

├── agents/
│   ├── sales-strategy.md       # Swarm Orchestrator & Data Quality Gate
│   ├── sales-competitive.md    # Continuous Threat Matrix Loop
│   ├── sales-company.md        # Firmographic Processing Core
│   ├── sales-contacts.md       # Identity & Target Committee Mapper
│   └── sales-opportunity.md    # Dynamic Intent Pipeline Agent
├── skills/
│   ├── sales-objections/      # LQS, MIC, AAR, FCA Psychological Engines
│   ├── sales-icp/             # Automated Analytics & Profile Diff Engine
│   ├── sales-prep/            # Playbook-Synced Briefing Generation
│   ├── sales-followup/        # Context-Locked Nurture Automation
│   └── [Other Skills]         # Core handlers (Prospect, Research, Qualify, etc.)
├── templates/
│   ├── COMPETITIVE-LIBRARY.md  # Long-term marketplace intelligence tracking
│   ├── OUTREACH-LOG.md         # Validated outreach state registry
│   ├── ROI-BENCHMARKS.md       # Economic justification milestones
│   ├── MARKET-CONTEXT.md       # Regional tool behavior & cultural overrides
│   └── OBJECTION-PLAYBOOK.md   # Script injection mapping asset
└── scripts/
    ├── lead_scorer.py         # Two-Pass Math Scoring Script
    ├── contact_finder.py      # Verification Mining Protocol
    └── generate_pdf_report.py # Automated Report Compilation Script

⚡ Quick Start & Installation
1. Provision Locally
Clone the repository to your local runtime environment:

Bash
git clone [https://github.com/Its-Leo-Space/ai-sales-forge.git](https://github.com/Its-Leo-Space/ai-sales-forge.git)
cd ai-sales-forge
2. Run the Environment Installer
Execute the setup wrapper to build project tracking directories and extract necessary dependencies:

Bash
chmod +x install.sh
./install.sh
3. Initialize Variables
Populate your newly generated local .env configuration file:

Plaintext
CLAUDE_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
4. Run Pre-Flight Diagnostics
Ensure your two-pass scoring layers and file tracking systems are perfectly calibrated before live deployment:

Bash
python scripts/lead_scorer.py
