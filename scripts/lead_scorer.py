#!/usr/bin/env python3
"""
Lead Scorer — AI Sales Team for Claude Code
Implements BANT + MEDDIC scoring algorithm for lead qualification.

Usage:
    python3 lead_scorer.py <input.json>
    cat input.json | python3 lead_scorer.py
    python3 lead_scorer.py --help
"""

import argparse
import json
import math
import sys

# ---------------------------------------------------------------------------
# BANT Scoring (each dimension 0-25, total 0-100)
# ---------------------------------------------------------------------------

def score_budget(signals):
    """Score budget signals (0-25)."""
    score = 0
    funding = signals.get("funding_amount", 0)
    if funding >= 50_000_000:
        score += 10
    elif funding >= 10_000_000:
        score += 8
    elif funding >= 5_000_000:
        score += 6
    elif funding >= 1_000_000:
        score += 4
    elif funding > 0:
        score += 2

    emp_count = signals.get("employee_count", 0)
    if emp_count >= 500:
        score += 5
    elif emp_count >= 100:
        score += 4
    elif emp_count >= 50:
        score += 3
    elif emp_count >= 10:
        score += 2
    elif emp_count > 0:
        score += 1

    if signals.get("pricing_visible"):
        score += 3

    tech_spend = signals.get("tech_spend_indicators", [])
    score += min(len(tech_spend) * 2, 7)

    return min(score, 25)


def score_authority(signals):
    """Score authority signals (0-25)."""
    score = 0
    dm_count = signals.get("decision_makers_found", 0)
    if dm_count >= 5:
        score += 10
    elif dm_count >= 3:
        score += 8
    elif dm_count >= 1:
        score += 5

    if signals.get("c_suite_identified"):
        score += 8

    if signals.get("org_chart_mapped"):
        score += 7
    elif dm_count > 1:
        score += 3

    return min(score, 25)


def score_need(signals):
    """Score need signals (0-25)."""
    score = 0
    pain_points = signals.get("pain_points_detected", 0)
    if pain_points >= 5:
        score += 8
    elif pain_points >= 3:
        score += 6
    elif pain_points >= 1:
        score += 3

    if signals.get("job_posts_relevant"):
        score += 6

    if signals.get("reviews_mention_pain"):
        score += 5

    complaints = signals.get("competitor_complaints", 0)
    if complaints >= 3:
        score += 6
    elif complaints >= 1:
        score += 4

    return min(score, 25)


def score_timeline(signals):
    """Score timeline signals (0-25)."""
    score = 0
    if signals.get("hiring_for_role"):
        score += 7

    if signals.get("recent_funding"):
        score += 7

    if signals.get("contract_renewal"):
        score += 6

    urgency = signals.get("urgency_mentions", 0)
    if urgency >= 3:
        score += 5
    elif urgency >= 1:
        score += 3

    return min(score, 25)


# ---------------------------------------------------------------------------
# MEDDIC Completeness Assessment
# ---------------------------------------------------------------------------

def assess_meddic(data):
    """
    Assess MEDDIC completeness as a percentage for each dimension.
    MEDDIC: Metrics, Economic Buyer, Decision Criteria, Decision Process,
             Identify Pain, Champion
    """
    budget = data.get("budget_signals", {})
    authority = data.get("authority_signals", {})
    need = data.get("need_signals", {})
    timeline = data.get("timeline_signals", {})

    metrics_signals = [
        budget.get("funding_amount", 0) > 0,
        budget.get("employee_count", 0) > 0,
        need.get("pain_points_detected", 0) > 0,
    ]
    metrics = int(sum(metrics_signals) / len(metrics_signals) * 100)

    econ_buyer_signals = [
        authority.get("c_suite_identified", False),
        authority.get("decision_makers_found", 0) >= 1,
    ]
    economic_buyer = int(sum(econ_buyer_signals) / len(econ_buyer_signals) * 100)

    decision_criteria_signals = [
        budget.get("pricing_visible", False),
        len(budget.get("tech_spend_indicators", [])) > 0,
        need.get("reviews_mention_pain", False),
    ]
    decision_criteria = int(sum(decision_criteria_signals) / len(decision_criteria_signals) * 100)

    decision_process_signals = [
        authority.get("org_chart_mapped", False),
        authority.get("decision_makers_found", 0) >= 2,
        timeline.get("contract_renewal", False),
    ]
    decision_process = int(sum(decision_process_signals) / len(decision_process_signals) * 100)

    pain_signals = [
        need.get("pain_points_detected", 0) >= 1,
        need.get("job_posts_relevant", False),
        need.get("competitor_complaints", 0) >= 1,
    ]
    identify_pain = int(sum(pain_signals) / len(pain_signals) * 100)

    champion_signals = [
        authority.get("decision_makers_found", 0) >= 1,
        need.get("reviews_mention_pain", False),
        timeline.get("hiring_for_role", False),
    ]
    champion = int(sum(champion_signals) / len(champion_signals) * 100)

    overall = int((metrics + economic_buyer + decision_criteria +
                   decision_process + identify_pain + champion) / 6)

    return {
        "metrics": metrics,
        "economic_buyer": economic_buyer,
        "decision_criteria": decision_criteria,
        "decision_process": decision_process,
        "identify_pain": identify_pain,
        "champion": champion,
        "overall": overall,
    }


# ---------------------------------------------------------------------------
# Grading + Recommendations
# ---------------------------------------------------------------------------

def compute_grade(score):
    """Return letter grade based on total score."""
    if score >= 75:
        return "A"
    elif score >= 50:
        return "B"
    elif score >= 25:
        return "C"
    return "D"


def compute_confidence(data):
    """Compute a confidence level based on data completeness."""
    total_fields = 0
    filled_fields = 0
    for section in ("budget_signals", "authority_signals", "need_signals", "timeline_signals"):
        signals = data.get(section, {})
        for key, val in signals.items():
            total_fields += 1
            if isinstance(val, bool) and val:
                filled_fields += 1
            elif isinstance(val, (int, float)) and val > 0:
                filled_fields += 1
            elif isinstance(val, list) and len(val) > 0:
                filled_fields += 1
            elif isinstance(val, str) and val:
                filled_fields += 1
    if total_fields == 0:
        return "low"
    ratio = filled_fields / total_fields
    if ratio >= 0.7:
        return "high"
    elif ratio >= 0.4:
        return "medium"
    return "low"


def recommend_action(grade, meddic):
    """Recommend next action based on grade and MEDDIC gaps."""
    if grade == "A":
        return "Schedule discovery call — high-priority prospect. Focus on confirming budget and timeline."
    elif grade == "B":
        weakest = min(meddic.items(), key=lambda x: x[1] if x[0] != "overall" else 999)
        return f"Nurture with targeted content — strengthen {weakest[0].replace('_', ' ')} ({weakest[1]}% complete). Build champion relationship."
    elif grade == "C":
        gaps = [k for k, v in meddic.items() if v < 50 and k != "overall"]
        gap_str = ", ".join(g.replace("_", " ") for g in gaps[:3])
        return f"Research needed — fill gaps in: {gap_str}. Consider multi-threaded outreach."
    return "Low priority — add to long-term nurture sequence. Revisit in 90 days."


# ---------------------------------------------------------------------------
# Main scoring pipeline
# ---------------------------------------------------------------------------

def score_lead(data):
    """Run full BANT + MEDDIC scoring on input data."""
    budget = data.get("budget_signals", {})
    authority = data.get("authority_signals", {})
    need = data.get("need_signals", {})
    timeline = data.get("timeline_signals", {})

    b_score = score_budget(budget)
    a_score = score_authority(authority)
    n_score = score_need(need)
    t_score = score_timeline(timeline)
    total = b_score + a_score + n_score + t_score

    grade = compute_grade(total)
    meddic = assess_meddic(data)
    confidence = compute_confidence(data)
    action = recommend_action(grade, meddic)

    return {
        "company": data.get("company", "Unknown"),
        "bant_score": total,
        "bant_breakdown": {
            "budget": {"score": b_score, "max": 25},
            "authority": {"score": a_score, "max": 25},
            "need": {"score": n_score, "max": 25},
            "timeline": {"score": t_score, "max": 25},
        },
        "meddic_completeness": meddic,
        "lead_grade": grade,
        "confidence_level": confidence,
        "recommended_action": action,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Lead Scorer — BANT + MEDDIC scoring algorithm for lead qualification.",
        epilog="Example: python3 lead_scorer.py input.json",
    )
    parser.add_argument("input_file", nargs="?", help="Path to input JSON file (reads stdin if omitted)")
    args = parser.parse_args()

    if args.input_file:
        try:
            with open(args.input_file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found: {args.input_file}", file=sys.stderr)
            sys.exit(1)
        except json.JSONDecodeError as exc:
            print(f"Error: Invalid JSON in {args.input_file}: {exc}", file=sys.stderr)
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            print("Error: No input file provided and no stdin data.", file=sys.stderr)
            print("Usage: python3 lead_scorer.py <input.json>", file=sys.stderr)
            sys.exit(1)
        try:
            data = json.load(sys.stdin)
        except json.JSONDecodeError as exc:
            print(f"Error: Invalid JSON from stdin: {exc}", file=sys.stderr)
            sys.exit(1)

    result = score_lead(data)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------------
# Second-Pass Scoring — Agent Intelligence Integration (Gap 3 fix)
# ---------------------------------------------------------------------------
# When agents complete their analysis, they write SIGNAL-DATA.json to the
# working directory. This function reads that file and re-scores the lead
# with the richer signal set, producing a before/after comparison that
# shows how much intelligence the agents added.

import os

def load_agent_signals(signal_file="SIGNAL-DATA.json"):
    """Load agent-derived signals from the working directory if available."""
    if not os.path.exists(signal_file):
        return None
    try:
        with open(signal_file, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def merge_signals(base_data, agent_signals):
    """
    Merge agent-derived signals into the base scoring data.
    Agent signals override or supplement Python-script-only signals.
    """
    if not agent_signals:
        return base_data

    merged = {
        "company": base_data.get("company", agent_signals.get("company", "Unknown")),
        "budget_signals": {**base_data.get("budget_signals", {}), **agent_signals.get("budget_signals", {})},
        "authority_signals": {**base_data.get("authority_signals", {}), **agent_signals.get("authority_signals", {})},
        "need_signals": {**base_data.get("need_signals", {}), **agent_signals.get("need_signals", {})},
        "timeline_signals": {**base_data.get("timeline_signals", {}), **agent_signals.get("timeline_signals", {})},
    }
    return merged


def score_lead_with_agent_intelligence(base_data, signal_file="SIGNAL-DATA.json"):
    """
    Run two-pass scoring:
    Pass 1 — Python script data only (pre-agent baseline)
    Pass 2 — Python + agent research merged (post-agent with full intelligence)

    Returns both scores so the founder can see the intelligence gap:
    - Low gap = Python scripts captured most of the signal
    - High gap = agents found significant intelligence the scripts missed
    """
    # Pass 1 — baseline from script data alone
    pass1 = score_lead(base_data)
    pass1["scoring_pass"] = "baseline (script data only)"
    pass1["confidence_note"] = "Score based on publicly extractable website data alone."

    # Pass 2 — load agent signals if available
    agent_signals = load_agent_signals(signal_file)
    if not agent_signals:
        pass1["second_pass_available"] = False
        pass1["second_pass_note"] = (
            "No SIGNAL-DATA.json found. "
            "Agents write this file after completing analysis. "
            "Run /sales prospect to generate agent-enriched scoring."
        )
        return pass1

    merged = merge_signals(base_data, agent_signals)
    pass2 = score_lead(merged)
    pass2["scoring_pass"] = "enriched (script + agent intelligence)"
    pass2["confidence_note"] = "Score based on website data PLUS agent research (news, reviews, LinkedIn, job posts)."
    pass2["second_pass_available"] = True

    # Intelligence gap analysis
    bant_delta = pass2["bant_score"] - pass1["bant_score"]
    gap_interpretation = (
        "Minimal" if abs(bant_delta) <= 5 else
        "Moderate" if abs(bant_delta) <= 15 else
        "Significant"
    )

    return {
        "company": pass2["company"],
        "baseline_score": pass1["bant_score"],
        "enriched_score": pass2["bant_score"],
        "intelligence_gap": bant_delta,
        "gap_interpretation": f"{gap_interpretation} — agents added {abs(bant_delta)} points of BANT signal",
        "final_score": pass2["bant_score"],
        "bant_breakdown": pass2["bant_breakdown"],
        "meddic_completeness": pass2["meddic_completeness"],
        "lead_grade": pass2["lead_grade"],
        "confidence_level": pass2["confidence_level"],
        "recommended_action": pass2["recommended_action"],
        "baseline_detail": pass1,
        "enriched_detail": pass2,
        "scoring_methodology": (
            "Two-pass scoring: Pass 1 uses website data only. "
            "Pass 2 incorporates agent research findings. "
            f"Intelligence gap of {bant_delta} points reflects what agents found "
            "beyond publicly extractable website data."
        )
    }


def write_signal_data_template(output_file="SIGNAL-DATA.json"):
    """
    Write an empty SIGNAL-DATA.json template.
    Agents populate this file after completing their analysis.
    The lead scorer reads it on second-pass scoring.
    """
    template = {
        "company": "",
        "budget_signals": {
            "funding_amount": 0,
            "funding_round": "",
            "funding_date": "",
            "employee_count": 0,
            "pricing_visible": False,
            "tech_spend_indicators": [],
            "reviews_mention_pain": False,
            "hiring_budget_signals": []
        },
        "authority_signals": {
            "decision_makers_found": 0,
            "c_suite_identified": False,
            "org_chart_mapped": False,
            "economic_buyer_name": "",
            "economic_buyer_title": "",
            "champion_identified": False,
            "procurement_complexity": "unknown"
        },
        "need_signals": {
            "pain_points_detected": 0,
            "pain_point_list": [],
            "job_posts_relevant": False,
            "reviews_mention_pain": False,
            "competitor_complaints": 0,
            "blog_discusses_problem": False,
            "social_mentions_pain": False
        },
        "timeline_signals": {
            "hiring_for_role": False,
            "recent_funding": False,
            "funding_within_months": 0,
            "contract_renewal": False,
            "urgency_mentions": 0,
            "trigger_events": [],
            "leadership_change": False,
            "rapid_growth": False
        },
        "_meta": {
            "generated_by": "agent_analysis",
            "timestamp": "",
            "confidence": "medium",
            "notes": ""
        }
    }
    with open(output_file, "w") as f:
        json.dump(template, f, indent=2)
    return output_file
