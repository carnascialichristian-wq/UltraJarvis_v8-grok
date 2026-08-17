"""Task planner for UltraJarvis.

Turns a free-form task description into a structured Plan.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List
import json

from core.utils import slugify


@dataclass
class Plan:
    title: str
    summary: str
    steps: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    success_criteria: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


def plan(prompt: str) -> Plan:
    """Create a basic plan from a natural-language prompt."""
    title = prompt.strip()[:80] or "Untitled task"
    summary = f"Plan for: {title}"
    steps = [
        "Analyze the request and constraints",
        "Design a minimal safe implementation",
        "Write code / files under guarded I/O",
        "Run gates (lint/tests) and verify",
    ]
    risks = ["Over-writing protected files", "Incomplete tests"]
    success = ["Gates pass", "Behavior matches the prompt"]
    return Plan(title=title, summary=summary, steps=steps, risks=risks, success_criteria=success)


def write_plan_md(plan_obj: Plan, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# {plan_obj.title}",
        "",
        plan_obj.summary,
        "",
        "## Steps",
    ]
    for i, s in enumerate(plan_obj.steps, 1):
        lines.append(f"{i}. {s}")
    lines += ["", "## Risks"]
    for r in plan_obj.risks:
        lines.append(f"- {r}")
    lines += ["", "## Success criteria"]
    for c in plan_obj.success_criteria:
        lines.append(f"- {c}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path
