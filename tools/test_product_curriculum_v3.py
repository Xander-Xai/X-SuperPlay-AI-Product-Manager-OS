"""V3 product/manager/founder knowledge completeness and upstream provenance tests."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ProductV3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c = json.loads((ROOT / "docs/atlas/knowledge-catalog.json").read_text(encoding="utf-8"))
        cls.s = json.loads((ROOT / "resources/authorities.json").read_text(encoding="utf-8"))
        cls.u = json.loads((ROOT / "resources/upstream-pm-knowledge-index.json").read_text(encoding="utf-8"))

    def test_cross_domain_coverage(self):
        ids = {x["id"] for x in self.c["topics"]}
        self.assertGreaterEqual(len(ids), 80)
        for domain in ["product", "ai", "engineering", "operations", "data", "business", "management", "cognition", "governance"]:
            self.assertTrue(any(x["domain"] == domain for x in self.c["topics"]), domain)

    def test_new_nodes_have_plain_formal_exercise(self):
        for x in self.c["topics"]:
            if x["id"].startswith(("MGT","COG","GO")) or x["id"] in {"PM13","PM14","PM15","BIZ06","BIZ07","BIZ08","BIZ09","BIZ10","BIZ11","BIZ12","DATA04"}:
                for field in ["definition","plain","exercise","evidence","trigger","resources"]:
                    self.assertTrue(x.get(field), f"{x['id']} missing {field}")

    def test_sources_and_private_paths(self):
        ids = {x["id"] for x in self.c["topics"]}
        sources = {x["id"] for x in self.s["sources"]}
        self.assertGreaterEqual(len(sources), 35)
        self.assertGreaterEqual(len(self.u["references"]), 20)
        for x in self.u["references"]:
            self.assertEqual(x["visibility"], "PRIVATE")
            self.assertIn("/X-SuperPlay-AI-Learning-OS/blob/main/", x["url"])
            self.assertTrue(x["path"].startswith("docs/"))
            self.assertTrue(set(x["target_ids"]).issubset(ids))
        for x in self.c["topics"]:
            self.assertTrue(set(x["resources"]).issubset(sources))

    def test_pedagogy_links_and_diagrams(self):
        body = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        self.assertIn("product-lifecycle-mermaid.md", body)
        self.assertIn("product-manager-primer.md", body)
        self.assertIn("upstream-pm-knowledge-index.md", body)
        self.assertGreaterEqual((ROOT / "docs/atlas/product-lifecycle-mermaid.md").read_text(encoding="utf-8").count("```mermaid"), 4)

if __name__ == "__main__":
    unittest.main()
