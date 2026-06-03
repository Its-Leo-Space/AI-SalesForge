<!-- HTML Code for README.md -->
<p align="center">
  <img src="repo banner.png" alt="AI Sales Forge - Claude Code Project Banner" width="1000px">
</p>

> **A full AI-powered sales system running inside Claude Code.**
> Research any company, score leads with BANT + MEDDIC, map buying committees, generate personalized outreach, handle objections with FBI negotiation tactics, prepare for meetings, and produce professional PDF pipeline reports — all from the command line.

---

## What This Does

Type a command in Claude Code and get instant, actionable sales intelligence:

```
> /sales prospect https://acme.com

ICP Pre-Flight: ✓ IDEAL-CUSTOMER-PROFILE.md found

Phase 1: Discovering company information...
  ✓ Homepage fetched — SaaS / B2B detected
  ✓ 6 subpages extracted (about, team, pricing, careers, blog, contact)
  ✓ analyze_prospect.py — 23 data points extracted
  ✓ MARKET-CONTEXT.md loaded

Phase 2: Running parallel analysis (5 agents)...
  ✓ Company Research      — Fit Score: 82/100
  ✓ Contact Discovery     — 4 contacts found
  ✓ Opportunity Scoring   — BANT: 78/100
  ✓ Competitive Intel     — 3 competitors mapped, library updated
  ✓ Outreach Strategy     — 5-email sequence ready
    └─ Data Quality Gate  — all signals confirmed

Phase 3: Synthesizing results (two-pass scoring)...
  ✓ Pass 1 Score: 74/100 (website signals)
  ✓ Pass 2 Score: 85/100 (agent-enriched)
  ✓ Intelligence delta: +11 points from parallel agents

┌─────────────────────────────────────────────────┐
│  PROSPECT SCORE                                 │
│                                                 │
│  ██████████████████████████████████░░░░  85/100  │
│                                                 │
│  Grade: A  —  Strong Prospect                   │
│  Action: Invest significant effort              │
└─────────────────────────────────────────────────┘

Full analysis saved to PROSPECT-ANALYSIS.md
```

---

## Quick Start

Prerequisites: Make sure you have Claude Code and Git installed before proceeding.


Windows (VS Code Terminal)
powershellgit clone https://github.com/Its-Leo-Space/AI-SalesForge.git
cd AI-SalesForge
bash install.sh

Note: This requires Git Bash to be installed (it comes with Git for Windows). If you get an error on the bash line, open the terminal dropdown in VS Code, select Git Bash as your shell, and run the 3 lines again.


Mac / Linux
One-line install in your terminal:
bashcurl -fsSL https://raw.githubusercontent.com/Its-Leo-Space/AI-SalesForge/main/install.sh | bash

Or manually:
bashgit clone https://github.com/Its-Leo-Space/AI-SalesForge.git
cd AI-SalesForge
./install.sh

### Optional: PDF Reports & Enhanced Parsing

```bash
pip install -r requirements.txt
```

<details>
<summary><strong>What the installer does</strong></summary>

```
╔══════════════════════════════════════════════════════════╗
║  AI Sales Forge — Claude Code Skills                    ║
║  14 Skills · 5 Agents · 4 Scripts · PDF                 ║
╚══════════════════════════════════════════════════════════╝

Installing skills...
  ✓ sales (orchestrator)
  ✓ sales-prospect
  ✓ sales-research
  ✓ sales-qualify
  ✓ sales-contacts
  ✓ sales-outreach
  ✓ sales-followup
  ✓ sales-prep
  ✓ sales-proposal
  ✓ sales-objections
  ✓ sales-icp
  ✓ sales-competitors
  ✓ sales-report
  ✓ sales-report-pdf

Installing agents...
  ✓ sales-company
  ✓ sales-contacts
  ✓ sales-opportunity
  ✓ sales-competitive
  ✓ sales-strategy

Installing scripts...
  ✓ analyze_prospect.py
  ✓ lead_scorer.py
  ✓ contact_finder.py
  ✓ generate_pdf_report.py

Installing templates...
  ✓ outreach-cold.md
  ✓ outreach-warm.md
  ✓ outreach-referral.md
  ✓ meeting-prep.md
  ✓ proposal-template.md
  ✓ OBJECTION-PLAYBOOK.md
  ✓ COMPETITIVE-LIBRARY.md
  ✓ OUTREACH-LOG.md
  ✓ ROI-BENCHMARKS.md
  ✓ MARKET-CONTEXT.md
```

</details>

---

## Commands

| Command | Description | Output |
|:--------|:------------|:-------|
| `/sales prospect <url>` | Full prospect audit — **5 parallel agents** | `PROSPECT-ANALYSIS.md` |
| `/sales quick <url>` | 60-second prospect snapshot | Terminal output |
| `/sales research <url>` | Company research & firmographics | `COMPANY-RESEARCH.md` |
| `/sales qualify <url>` | BANT + MEDDIC lead scoring | `LEAD-QUALIFICATION.md` |
| `/sales contacts <url>` | Decision maker identification | `DECISION-MAKERS.md` |
| `/sales outreach <prospect>` | Cold outreach email sequence | `OUTREACH-SEQUENCE.md` |
| `/sales followup <prospect>` | Follow-up sequence (anchored to meeting prep) | `FOLLOWUP-SEQUENCE.md` |
| `/sales prep <url>` | Meeting preparation brief | `MEETING-PREP.md` |
| `/sales proposal <client>` | Client proposal with ROI benchmarks | `CLIENT-PROPOSAL.md` |
| `/sales objections <topic>` | Objection handling — LQS / MIC / AAR / FCA | `OBJECTION-PLAYBOOK.md` |
| `/sales icp <description>` | Ideal Customer Profile builder | `IDEAL-CUSTOMER-PROFILE.md` |
| `/sales icp refine` | Refine ICP from existing prospect files | `IDEAL-CUSTOMER-PROFILE.md` |
| `/sales competitors <url>` | Competitive intelligence (persistent library) | `COMPETITIVE-INTEL.md` |
| `/sales report` | Pipeline report (reads outreach logs) | `SALES-REPORT.md` |
| `/sales report-pdf` | Pipeline report (PDF) | `SALES-REPORT-*.pdf` |

---

## How It Works

### Architecture

The system uses a three-layer architecture — one orchestrator skill routes commands to 13 sub-skills, with the flagship `/sales prospect` command launching 5 specialized agents in parallel:

```
                         ┌──────────────────────────┐
                         │     /sales prospect       │
                         │      (Orchestrator)       │
                         │   + ICP Pre-Flight Check  │
                         └────────────┬─────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    ▼                 ▼                  ▼
          ┌─────────────┐   ┌─────────────────┐   ┌──────────────┐
          │   PHASE 1    │   │     PHASE 2      │   │   PHASE 3    │
          │  Discovery   │   │ Parallel Analysis│   │  Synthesis   │
          └──────┬──────┘   └────────┬─────────┘   └──────┬───────┘
                 │                   │                     │
                 ▼                   ▼                     ▼
          ┌─────────────┐   ┌───────────────┐      ┌──────────────┐
          │ Fetch site   │   │ 5 agents run  │      │ Two-pass     │
          │ Extract data │   │ simultaneously│      │ score (0-100)│
          │ Detect type  │   │ + Data Quality│      │ Action plan  │
          │ Run scripts  │   │   Gate (Ag.5) │      │ First email  │
          └─────────────┘   └───────┬───────┘      └──────────────┘
                                    │
                 ┌──────────────────┼──────────────────┐
                 │                  │                   │
        ┌────────────────┐  ┌──────────────┐  ┌───────────────┐
        │   Company      │  │   Contacts   │  │  Opportunity  │
        │   Research     │  │   Finder     │  │  Scoring      │
        │   Fit: 25%     │  │   Access:20% │  │  Quality: 20% │
        └────────────────┘  └──────────────┘  └───────────────┘
        ┌────────────────┐  ┌──────────────┐
        │   Competitive  │  │   Outreach   │
        │   Analysis     │  │   Strategy   │
        │ + Persistent   │  │ + Data       │
        │   Library      │  │   Quality    │
        │   Position:15% │  │   Gate: 20%  │
        └────────────────┘  └──────────────┘
```

### Cross-Skill Intelligence

Skills automatically detect and build on each other's output — nothing is generated in isolation:

```
/sales prospect  ──►  PROSPECT-ANALYSIS.md
                            │
       ┌────────────────────┼─────────────────────┐
       ▼                    ▼                      ▼
/sales outreach      /sales prep             /sales proposal
 (reads contacts,    (reads objection        (reads ROI
  research data)      playbook → Sec. 8)      benchmarks)
       │                    │                      │
       ▼                    ▼                      ▼
 OUTREACH-             MEETING-               CLIENT-
 SEQUENCE.md  ──►      PREP.md    ──►         PROPOSAL.md
 OUTREACH-LOG.md       (anchors follow-up)    (⚠️ flags estimates)
       │
       ▼
/sales report
 (reads OUTREACH-LOG for
  actual pipeline reality)

/sales competitors  ──►  COMPETITIVE-INTEL.md
                               │
                               ▼
                         COMPETITIVE-LIBRARY.md
                         (persists across all runs)
                               │
                               ▼
                    next /sales prospect reads
                    prior competitive intel
```

---

## Prospect Scoring

Every prospect gets a **weighted composite score (0-100)** calculated across 5 dimensions, with two scoring passes to measure how much the agents added beyond raw website data:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   PROSPECT SCORE FORMULA                                            │
│                                                                     │
│   Company Fit ............ 25%   ████████████░░░░░░░░  Size,        │
│                                                        industry,    │
│                                                        growth       │
│                                                                     │
│   Contact Access ......... 20%   █████████░░░░░░░░░░░  Decision     │
│                                                        makers,      │
│                                                        warm paths   │
│                                                                     │
│   Opportunity Quality .... 20%   █████████░░░░░░░░░░░  BANT score,  │
│                                                        pain points  │
│                                                                     │
│   Competitive Position ... 15%   ███████░░░░░░░░░░░░░  Current      │
│                                                        solutions,   │
│                                                        switching    │
│                                                                     │
│   Outreach Readiness ..... 20%   █████████░░░░░░░░░░░  Channels,    │
│                                                        messaging,   │
│                                                        anchors      │
│                                                                     │
│   Pass 1: website signals only                                      │
│   Pass 2: agent-enriched (SIGNAL-DATA.json merged)                  │
│   Delta:  intelligence gap surfaced explicitly                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Grade Interpretation

```
  Score    Grade    Action
 ───────────────────────────────────────────────────────────
  90-100    A+      🔥  Hot Lead — prioritize immediately
  75-89     A       ✅  Strong Prospect — invest significant effort
  60-74     B       📊  Qualified Lead — pursue with standard approach
  40-59     C       🔄  Lukewarm — nurture, don't hard sell
   0-39     D       ⏸️   Poor Fit — deprioritize or disqualify
```

### Qualification Frameworks

<details>
<summary><strong>BANT Scoring (0-100)</strong></summary>

Each dimension scored 0-25 from publicly available signals:

| Dimension | Max | Signals |
|-----------|-----|---------|
| **Budget** | 25 | Funding, employee count, pricing pages, tech spend |
| **Authority** | 25 | Decision makers found, C-suite identified, org chart |
| **Need** | 25 | Pain points, job posts, reviews, competitor gaps |
| **Timeline** | 25 | Recent funding, hiring, contract cycles, urgency |

</details>

<details>
<summary><strong>MEDDIC Assessment (0-100%)</strong></summary>

Each dimension assessed for completeness:

- **M**etrics — Can we quantify the business impact?
- **E**conomic Buyer — Who controls the budget?
- **D**ecision Criteria — How will they evaluate solutions?
- **D**ecision Process — What's their buying process?
- **I**dentify Pain — Are pain points confirmed?
- **C**hampion — Is there an internal advocate?

</details>

---

## Objection Handling

Four response architectures grounded in FBI negotiation tactics (Chris Voss) and cognitive psychology (Kahneman). Each is selected automatically based on the type of resistance detected.

```
┌────────────────────────────────────────────────────────────────┐
│  OBJECTION RESPONSE ARCHITECTURES                              │
├────────────────┬───────────────────────────────────────────────┤
│  LQS           │  Label → Question → Silence                   │
│                │  Use: emotional / vague objections            │
│                │  Foundation: Voss labeling, silence technique │
├────────────────┼───────────────────────────────────────────────┤
│  MIC           │  Mirror → Implication Chain → Permission Close│
│                │  Use: price / budget objections               │
│                │  Foundation: Kahneman loss aversion (2:1)     │
├────────────────┼───────────────────────────────────────────────┤
│  AAR           │  Accusation Audit → Reversal                  │
│                │  Use: high-resistance / hostile prospects     │
│                │  Foundation: pre-empt the attack              │
├────────────────┼───────────────────────────────────────────────┤
│  FCA           │  Future Pace → Cost Anchor → Autonomy Return  │
│                │  Use: "not right now" / timing objections     │
│                │  Foundation: autonomy preservation            │
└────────────────┴───────────────────────────────────────────────┘
```

All 15 universal objections include: a diagnostic tree, pattern interrupt, power move, silence instruction with exact seconds, implication chain, explicit loss framing, and disqualification criteria.

---

## Key Capabilities

### ICP Pre-Flight Check
The orchestrator checks for an ICP file before routing any command. No ICP on file means you get an explicit prompt rather than silently producing output calibrated for nobody.

### ICP Refinement
`/sales icp refine` reads all existing prospect files, identifies what your highest and lowest scoring prospects have in common, and produces an updated ICP with a visible before/after diff. Your targeting sharpens automatically as your pipeline grows.

### Persistent Competitive Memory
Every `/sales competitors` run reads from and writes back to `COMPETITIVE-LIBRARY.md`. Competitive intelligence compounds across sessions rather than resetting each time.

### Data Quality Gate
The strategy agent assesses incoming data quality before writing a single word of outreach. Low contact data triggers a research checklist. Unconfirmed needs shift the framework to hypothesis mode. Poor company fit caps the score and surfaces a warning.

### ROI-Honest Proposals
`/sales proposal` reads `ROI-BENCHMARKS.md` and either cites real evidence or flags estimates with `⚠️`. No invented numbers.

### Market Context Awareness
`MARKET-CONTEXT.md` feeds into both the prospect and competitive agents — local tool signatures, relationship norms, and regional funding signals pass through to every analysis that touches geography or buying behaviour.

---

## Examples

### Full Prospect Audit

```
> /sales prospect https://stripe.com

ICP Pre-Flight: ✓ IDEAL-CUSTOMER-PROFILE.md found

Phase 1: Discovering company information...
  ✓ Homepage fetched — SaaS / Fintech detected
  ✓ 6 subpages extracted (about, team, pricing, careers, blog, contact)
  ✓ analyze_prospect.py — 23 data points extracted

Phase 2: Running parallel analysis (5 agents)...
  ✓ Company Research      — Fit Score: 88/100
  ✓ Contact Discovery     — 6 decision makers found
  ✓ Opportunity Scoring   — BANT: 82/100
  ✓ Competitive Intel     — 4 competitors mapped, library updated
  ✓ Outreach Strategy     — 5-email sequence drafted
    └─ Data Quality Gate  — all signals confirmed

Phase 3: Synthesizing results...
  ✓ Pass 1 Score: 76/100 (website signals)
  ✓ Pass 2 Score: 85/100 (agent-enriched)
  ✓ Intelligence delta: +9 points
  ✓ Grade: A — Strong Prospect

Output: PROSPECT-ANALYSIS.md
```

### Objection Handling

```
> /sales objections "enterprise SaaS"

Generating objection playbook for enterprise SaaS...
  Architecture selected: MIC for price objections
  Architecture selected: LQS for vague/emotional resistance
  Architecture selected: AAR for legal/procurement pushback

  "It's too expensive"      → MIC: Implication Chain + Loss Frame
  "We need to think"        → LQS: Label + Calibrated Question
  "We already have a tool"  → FCA: Future Pace + Cost Anchor
  "Not right now"           → FCA: Autonomy Return
  "Send me some info"       → AAR: Accusation Audit
  ... 10 more objections

Output: OBJECTION-PLAYBOOK.md
```

### ICP Refinement

```
> /sales icp refine

Reading all prospect files...
  ✓ 12 PROSPECT-ANALYSIS files found
  ✓ High scorers (A+/A): 5 prospects
  ✓ Low scorers (C/D):   4 prospects

Pattern analysis:
  High-fit signals: Series B+, 50-200 employees, VP Engineering titles
  Low-fit signals:  Pre-revenue, single founder, consumer-facing

Before → After diff:
  Company size:  "any" → "50-200 employees"
  Funding stage: "any" → "Series A or later"
  Champion role: "any" → "VP/Director Engineering or Product"

Output: IDEAL-CUSTOMER-PROFILE.md (updated)
```

### Lead Qualification

```
> /sales qualify https://notion.so

  BANT Score: 78/100 (Grade A)
  ┌────────────────────────────────────┐
  │ Budget:    ██████████████████░░ 22  │
  │ Authority: ████████████████░░░░ 18  │
  │ Need:      ██████████████████░░ 20  │
  │ Timeline:  ████████████████░░░░ 18  │
  └────────────────────────────────────┘
  MEDDIC Completeness: 72%

Action: Schedule discovery call — high-priority prospect.
Output: LEAD-QUALIFICATION.md
```

---

## Project Structure

```
AI-SalesForge/
│
├── sales/SKILL.md                     ← Main orchestrator (ICP pre-flight check)
│
├── skills/                            ← 13 sub-skills
│   ├── sales-prospect/SKILL.md           Full prospect audit (5 agents + market context)
│   ├── sales-research/SKILL.md           Company research & firmographics
│   ├── sales-qualify/SKILL.md            Lead qualification (BANT + MEDDIC)
│   ├── sales-contacts/SKILL.md           Decision maker identification
│   ├── sales-outreach/SKILL.md           Cold outreach email sequences
│   ├── sales-followup/SKILL.md           Follow-up (reads MEETING-PREP.md)
│   ├── sales-prep/SKILL.md               Meeting prep (reads OBJECTION-PLAYBOOK.md)
│   ├── sales-proposal/SKILL.md           Client proposal (reads ROI-BENCHMARKS.md)
│   ├── sales-objections/SKILL.md         Objection engine — LQS / MIC / AAR / FCA
│   ├── sales-icp/SKILL.md                ICP builder + /refine sub-command
│   ├── sales-competitors/SKILL.md        Competitive intel (persistent library)
│   ├── sales-report/SKILL.md             Pipeline report (reads OUTREACH-LOG files)
│   └── sales-report-pdf/SKILL.md         Pipeline report (PDF)
│
├── agents/                            ← 5 parallel subagents
│   ├── sales-company.md                  Company fit & firmographics (25%)
│   ├── sales-contacts.md                 Decision maker mapping (20%)
│   ├── sales-opportunity.md              Opportunity & BANT scoring (20%)
│   ├── sales-competitive.md              Competitive positioning + library (15%)
│   └── sales-strategy.md                 Outreach strategy + data quality gate (20%)
│
├── scripts/                           ← Python utilities
│   ├── analyze_prospect.py               Website scraping & data extraction
│   ├── lead_scorer.py                    BANT/MEDDIC + two-pass scoring engine
│   ├── contact_finder.py                 Team & leadership extraction
│   └── generate_pdf_report.py            ReportLab PDF generator
│
├── templates/                         ← Output templates
│   ├── outreach-cold.md                  5-email cold sequence
│   ├── outreach-warm.md                  3-email warm intro sequence
│   ├── outreach-referral.md              3-email referral sequence
│   ├── meeting-prep.md                   Meeting prep brief
│   ├── proposal-template.md              11-section client proposal
│   ├── OBJECTION-PLAYBOOK.md             15 objections — LQS / MIC / AAR / FCA
│   ├── COMPETITIVE-LIBRARY.md            Persistent competitive intel store
│   ├── OUTREACH-LOG.md                   Actual send/response tracking
│   ├── ROI-BENCHMARKS.md                 Evidence base for proposal ROI claims
│   └── MARKET-CONTEXT.md                 Regional/local market signals
│
├── install.sh                         ← One-command installer
├── uninstall.sh                       ← Cleanup script
├── requirements.txt                   ← Python deps (reportlab, bs4, requests)
└── LICENSE                            ← MIT
```

---

## Use Cases

<table>
<tr>
<td width="33%">

### Founders & Solopreneurs

```bash
# Full prospect intelligence
/sales prospect https://target.com

# Ready-to-send email sequence
/sales outreach "Target Company"

# Prep before the call
/sales prep https://target.com

# Sharpen targeting over time
/sales icp refine
```

</td>
<td width="33%">

### Sales Teams

```bash
# Qualify inbound leads
/sales qualify https://lead.com

# Map the buying committee
/sales contacts https://lead.com

# Handle objections with
# FBI negotiation tactics
/sales objections "enterprise SaaS"
```

</td>
<td width="33%">

### Agency Owners

```bash
# Client proposal with real ROI
/sales proposal "Client Name"

# Competitive positioning
# (builds persistent library)
/sales competitors https://client.com

# Define ideal customer
/sales icp "B2B SaaS, 50-200 emp"
```

</td>
</tr>
</table>

---

## Requirements

| Requirement | Status | Notes |
|:------------|:------:|:------|
| **Claude Code** | Required | [Install Claude Code](https://docs.anthropic.com/en/docs/claude-code) |
| **Python 3.8+** | Optional | For scripts and PDF generation |
| **reportlab** | Optional | `pip install reportlab` — PDF reports |
| **beautifulsoup4** | Optional | `pip install beautifulsoup4` — enhanced parsing |
| **requests** | Optional | `pip install requests` — fallback URL fetching |

---

## Uninstall

```bash
# From the repo directory
./uninstall.sh

# Or remotely
curl -fsSL https://raw.githubusercontent.com/Its-Leo-Space/AI-SalesForge/main/uninstall.sh | bash
```

Removes all skills, agents, scripts, and templates from `~/.claude/`. Python packages are not removed.

---

<p align="center">
  <strong>MIT License</strong> · <a href="https://github.com/Its-Leo-Space">Its-Leo-Space</a>
  <br><br>
  <a href="https://github.com/Its-Leo-Space/AI-SalesForge/issues">Report Bug</a> ·
  <a href="https://github.com/Its-Leo-Space/AI-SalesForge/issues">Request Feature</a>
</p>
