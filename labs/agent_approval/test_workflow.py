import unittest
from labs.agent_approval.workflow import Guard, WorkOrder

class ApprovalTests(unittest.TestCase):
    def setUp(self):
        self.g = Guard()
        self.g.submit(WorkOrder("o1", "A", "create support ticket"))

    def test_no_write_before_approval(self):
        with self.assertRaises(PermissionError):
            self.g.execute("o1", "A", "k1")
        self.assertEqual(self.g.write_count, 0)

    def test_wrong_tenant_cannot_approve(self):
        with self.assertRaises(PermissionError):
            self.g.decide("o1", "B", "approver", True)

    def test_wrong_role_cannot_approve(self):
        with self.assertRaises(PermissionError):
            self.g.decide("o1", "A", "viewer", True)

    def test_rejected_stays_unexecuted(self):
        self.g.decide("o1", "A", "approver", False)
        with self.assertRaises(PermissionError):
            self.g.execute("o1", "A", "k1")
        self.assertEqual(self.g.write_count, 0)

    def test_duplicate_delivery_is_idempotent(self):
        self.g.decide("o1", "A", "approver", True)
        a = self.g.execute("o1", "A", "k1")
        b = self.g.execute("o1", "A", "k1")
        self.assertEqual(a, b)
        self.assertEqual(self.g.write_count, 1)

    def test_tenant_mismatch_cannot_execute(self):
        self.g.decide("o1", "A", "approver", True)
        with self.assertRaises(PermissionError):
            self.g.execute("o1", "B", "k1")

    def test_idempotency_key_conflict_fails(self):
        self.g.decide("o1", "A", "approver", True)
        self.g.execute("o1", "A", "same-key")
        self.g.submit(WorkOrder("o2", "A", "second action"))
        self.g.decide("o2", "A", "approver", True)
        with self.assertRaises(ValueError):
            self.g.execute("o2", "A", "same-key")
        self.assertEqual(self.g.write_count, 1)

if __name__ == "__main__":
    unittest.main()
