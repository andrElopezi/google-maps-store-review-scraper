thonimport unittest
from pathlib import Path
from src.exporters.data_exporter import DataExporter

class TestExporter(unittest.TestCase):
    def setUp(self):
        self.data = [{"a": 1, "b": 2}]
        self.exporter = DataExporter()

    def test_export_json_creates_file(self):
        path = Path("data/test_output.json")
        self.exporter.export_json(self.data, path)
        self.assertTrue(path.exists())
        path.unlink()

if __name__ == "__main__":
    unittest.main()