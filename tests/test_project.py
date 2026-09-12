from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ProjectStructureTest(unittest.TestCase):
    def test_required_files_exist(self):
        required_files = [
            "README.md",
            "index.html",
            "login.html",
            "styles.css",
            "docs/resumen-tecnico.md",
            "docs/reflexion-critica.md",
            ".github/workflows/ci.yml",
        ]

        for file_name in required_files:
            with self.subTest(file=file_name):
                self.assertTrue((ROOT / file_name).is_file())

    def test_login_form_contains_required_fields(self):
        html = (ROOT / "login.html").read_text(encoding="utf-8").lower()

        expected_fragments = [
            'name="usuario"',
            'name="password"',
            'type="password"',
            'type="submit"',
            "ingresar",
        ]

        for fragment in expected_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, html)


if __name__ == "__main__":
    unittest.main()
