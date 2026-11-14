import unittest
from labs.product_metrics.analysis import Event, SYNTHETIC, metrics

class ProductMetricsTests(unittest.TestCase):
    def test_success_denominator(self):
        got = metrics(SYNTHETIC)
        self.assertEqual(got["started"], 3)
        self.assertEqual(got["verified_success"], 2)
        self.assertAlmostEqual(got["completion_rate"], 2 / 3)
        self.assertAlmostEqual(got["cost_per_success"], 0.15)

    def test_duplicate_complete_not_double_counted(self):
        data = SYNTHETIC + [Event("t1", "task_completed", verified=True)]
        self.assertEqual(metrics(data)["verified_success"], 2)

    def test_unstarted_completion_not_counted(self):
        data = [Event("x", "task_completed", verified=True), Event("t1", "task_started")]
        self.assertEqual(metrics(data)["verified_success"], 0)

    def test_zero_denominator_not_misreported(self):
        got = metrics([Event("ghost", "model_call", cost=0.1)])
        self.assertIsNone(got["completion_rate"])
        self.assertIsNone(got["cost_per_success"])

    def test_negative_cost_explicitly_rejected(self):
        with self.assertRaises(ValueError):
            metrics([Event("t1", "task_started", cost=-1)])

if __name__ == "__main__":
    unittest.main()
