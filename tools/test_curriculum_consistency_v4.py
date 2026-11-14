"""V4 complete coverage, source aliases and professional terminology consistency tests."""
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))

class V4ConsistencyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.topics = load("docs/atlas/knowledge-catalog.json")["topics"]
        cls.sources = load("resources/authorities.json")["sources"]
        cls.domains = load("docs/quality/coverage-matrix.json")["domains"]
        cls.handbook = (ROOT / "docs/atlas/knowledge-handbook.md").read_text(encoding="utf-8")
        cls.roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")

    def test_domain_coverage_is_complete(self):
        ids = {x["id"] for x in self.topics}
        mapped = {id for d in self.domains for id in d["topic_ids"]}
        self.assertEqual(ids, mapped)
        self.assertEqual(len(self.domains), 18)

    def test_every_topic_has_practical_evidence_and_refs(self):
        valid = {x["id"] for x in self.sources}
        for topic in self.topics:
            with self.subTest(topic=topic["id"]):
                self.assertTrue(topic["exercise"])
                self.assertTrue(topic["evidence"])
                self.assertTrue(topic["trigger"])
                self.assertTrue(topic["resources"])
                self.assertTrue(set(topic["resources"]).issubset(valid))

    def test_handbook_indexes_every_node(self):
        tick=chr(96)
        for topic in self.topics:
            with self.subTest(topic=topic["id"]):
                self.assertIn("| "+tick+topic["id"]+tick+" |",self.handbook)

    def test_source_urls_are_canonical_or_declared_alias(self):
        urls={}
        ids={s["id"]:s for s in self.sources}
        for src in self.sources:
            with self.subTest(source=src["id"]):
                self.assertTrue(src["url"].startswith("https://"))
                if src["url"] in urls:
                    self.assertEqual(src.get("alias_of"),urls[src["url"]])
                else:
                    self.assertNotIn("alias_of",src)
                    urls[src["url"]]=src["id"]
                if src.get("alias_of"):
                    self.assertIn(src["alias_of"],ids)
                    self.assertEqual(ids[src["alias_of"]]["url"],src["url"])

    def test_web_security_and_llm_security_are_distinct(self):
        sources={x["id"]:x for x in self.sources}
        nodes={x["id"]:x for x in self.topics}
        self.assertNotEqual(sources["S08"]["url"],sources["S56"]["url"])
        self.assertIn("S56",nodes["AI12"]["resources"])
        self.assertIn("S56",nodes["AI06"]["resources"])

    def test_professional_role_and_result_contract(self):
        text=(ROOT/"docs/quality/terminology-contract.md").read_text(encoding="utf-8").lower()
        for term in ["product manager","product owner","project manager","definition of done",
                     "definition of ready","acceptance criteria","mvp","poc","pilot",
                     "production","not_run","verified_by_owner_repo"]:
            self.assertIn(term,text)

    def test_no_stale_core_docs_counts(self):
        for name in ["README.md","ROADMAP.md","docs/atlas/product-manager-primer.md",
                     "docs/learning/optional-cadence.md"]:
            body=(ROOT/name).read_text(encoding="utf-8")
            for stale in ["55 节点","55+ 扩展","约 84 个知识节点","v0.2.0","v0.3.0"]:
                self.assertNotIn(stale,body,name)
        self.assertIn("coverage-audit-20261114.md",self.roadmap)
        self.assertIn("product-foundations-task-router.md",self.roadmap)

    def test_timebox_is_optional(self):
        body=(ROOT/"docs/learning/optional-cadence.md").read_text(encoding="utf-8")
        self.assertIn("不是必修先后",body)
        self.assertIn("不是强制",body)

if __name__ == "__main__":
    unittest.main()
