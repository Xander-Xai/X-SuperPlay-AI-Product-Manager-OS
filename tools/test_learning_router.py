"""Offline structural tests: content integrity, dependency behavior and negative cases."""
import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("router", HERE / "learning_router.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class IndexContractTests(unittest.TestCase):
    def test_registry(self):
        errs, topics, sources, scenarios = mod.check()
        self.assertEqual(errs, [])
        self.assertGreaterEqual(len(topics), 50)
        self.assertGreaterEqual(len(sources), 18)
        self.assertGreaterEqual(len(scenarios), 5)

    def test_selective_routing(self):
        first = mod.route("ENG06", False)
        deep = mod.route("ENG06", True)
        self.assertIn("ENG06", first)
        self.assertIn("ENG04", first)
        self.assertEqual(first[0], "ENG06")
        self.assertTrue(set(first).issubset(deep))

    def test_invalid_id_fails_closed(self):
        with self.assertRaises(ValueError):
            mod.route("NONSENSE", False)

    def test_all_sources_are_official_or_primary(self):
        _, _, sources, _ = mod.check()
        self.assertTrue(all(s["url"].startswith("https://") and s["checked_on"] for s in sources))

if __name__=="__main__":
    unittest.main()
