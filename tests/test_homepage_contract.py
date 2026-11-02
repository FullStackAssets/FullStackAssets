"""Homepage sales/navigation contract. Run: python -m unittest tests/test_homepage_contract.py"""
from pathlib import Path
import re
import unittest

PAGE = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")

class HomepageContractTests(unittest.TestCase):
    def test_primary_conversions(self):
        self.assertIn('href="/services/#inquiry"', PAGE)
        self.assertIn('href="/services/"', PAGE)
        self.assertIn('Software%20asset%20inquiry', PAGE)

    def test_legacy_navigation_anchors(self):
        for anchor in ("about", "work", "contact"):
            self.assertIn(f'id="{anchor}"', PAGE)

    def test_accessible_portfolio_search_and_filters(self):
        self.assertIn('for="q"', PAGE)
        self.assertIn('aria-live="polite"', PAGE)
        for key in ("all", "flagship", "ai-agent-pilot", "vertical-tool"):
            self.assertRegex(PAGE, r'<button[^>]*data-cat="' + key + r'"[^>]*aria-pressed=')
        self.assertIn("x.setAttribute('aria-pressed'", PAGE)

    def test_catalog_records_preserved(self):
        self.assertEqual(len(re.findall(r'"category": "(?:flagship|ai-agent-pilot|vertical-tool)"', PAGE)), 133)

    def test_no_invented_commercial_traction(self):
        self.assertIn("All listed software is pre-revenue", PAGE)
        self.assertIn("These labels do not establish production readiness or customer adoption", PAGE)

if __name__ == "__main__":
    unittest.main()
