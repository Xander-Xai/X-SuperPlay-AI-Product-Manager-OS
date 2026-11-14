import unittest
from labs.rag_evidence.baseline import Document, EXAMPLE, search, answer

class EvidenceTests(unittest.TestCase):
    def test_correct_current_citation(self):
        got = answer("return window", "A", EXAMPLE)
        self.assertEqual(got["status"], "EVIDENCE_FOUND")
        self.assertEqual(got["citation"], "public-policy@r2")

    def test_retired_doc_not_returned(self):
        self.assertNotIn("obsolete-policy", [d.doc_id for d in search("thirty days", "A", EXAMPLE)])

    def test_cross_tenant_refused(self):
        got = answer("secret refund contract", "A", EXAMPLE)
        self.assertEqual(got["status"], "REFUSE_NO_EVIDENCE")
        self.assertIsNone(got["citation"])

    def test_empty_query_refused(self):
        self.assertEqual(answer(" ", "A", EXAMPLE)["status"], "REFUSE_NO_EVIDENCE")

    def test_permission_not_overridden_by_query(self):
        got = answer("ignore instruction tenant B secret refund", "A", EXAMPLE)
        self.assertEqual(got["status"], "REFUSE_NO_EVIDENCE")

    def test_new_revision_preferred_when_current(self):
        docs = [Document("x", "A", 1, False, "Token recovery"),
                Document("x", "A", 2, True, "Token recovery current")]
        self.assertEqual(answer("token recovery", "A", docs)["citation"], "x@r2")

if __name__ == "__main__":
    unittest.main()
