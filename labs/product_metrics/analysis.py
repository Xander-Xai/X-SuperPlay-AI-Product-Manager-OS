"""Reproducible task-level metrics; synthetic rows, no real user analytics."""
from collections import defaultdict
from dataclasses import dataclass

@dataclass(frozen=True)
class Event:
    task_id: str
    kind: str
    cost: float = 0.0
    verified: bool = False

def metrics(events: list[Event]) -> dict:
    if any(e.cost < 0 for e in events):
        raise ValueError("cost should be non-negative; refunds need explicit convention")
    started = {e.task_id for e in events if e.kind == "task_started" and e.task_id}
    if not started:
        return {"started": 0, "verified_success": 0, "completion_rate": None, "cost_per_success": None}
    verified = {e.task_id for e in events if e.kind == "task_completed" and e.verified and e.task_id in started}
    total_cost = sum(e.cost for e in events if e.task_id in started)
    return {
        "started": len(started),
        "verified_success": len(verified),
        "completion_rate": len(verified) / len(started),
        "cost_per_success": total_cost / len(verified) if verified else None,
    }

SYNTHETIC = [
    Event("t1", "task_started"), Event("t1", "model_call", cost=0.08),
    Event("t1", "task_completed", verified=True),
    Event("t2", "task_started"), Event("t2", "model_call", cost=0.10),
    Event("t2", "task_completed", verified=False),
    Event("t3", "task_started"), Event("t3", "model_call", cost=0.12),
    Event("t3", "task_completed", verified=True),
]
