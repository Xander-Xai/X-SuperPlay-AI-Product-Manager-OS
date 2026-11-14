"""A deterministic tool-execution guard, NOT a model or real Agent framework."""
from dataclasses import dataclass
from enum import Enum

class Status(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

@dataclass
class WorkOrder:
    order_id: str
    tenant: str
    payload: str
    status: Status = Status.PENDING

class Guard:
    def __init__(self):
        self.orders: dict[str, WorkOrder] = {}
        self.results: dict[tuple[str, str], tuple[str, str]] = {}
        self.write_count = 0

    def submit(self, order: WorkOrder) -> None:
        if not order.order_id or not order.tenant:
            raise ValueError("missing identifiers")
        if order.order_id in self.orders:
            raise ValueError("duplicate order id")
        if order.status != Status.PENDING:
            raise ValueError("cannot bypass approval")
        self.orders[order.order_id] = order

    def decide(self, order_id: str, tenant: str, reviewer_role: str, approve: bool) -> None:
        order = self.orders[order_id]
        if order.tenant != tenant or reviewer_role != "approver":
            raise PermissionError("not authorized to approve")
        if order.status != Status.PENDING:
            raise ValueError("decision already made")
        order.status = Status.APPROVED if approve else Status.REJECTED

    def execute(self, order_id: str, tenant: str, operation_key: str) -> str:
        order = self.orders[order_id]
        if order.tenant != tenant:
            raise PermissionError("wrong tenant")
        if order.status != Status.APPROVED:
            raise PermissionError("approval required")
        if not operation_key:
            raise ValueError("idempotency key required")
        key = (tenant, operation_key)
        fingerprint = (order.order_id, order.payload)
        if key in self.results:
            prior_fingerprint, result = self.results[key]
            if prior_fingerprint != str(fingerprint):
                raise ValueError("idempotency key reused with different payload")
            return result
        result = f"FAKE_WRITTEN:{order.order_id}"
        self.results[key] = (str(fingerprint), result)
        self.write_count += 1
        return result
