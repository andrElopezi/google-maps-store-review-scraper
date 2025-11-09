thonimport json
import csv
import logging
from pathlib import Path
import pandas as pd

class DataExporter:
    def export_json(self, data, filepath: Path):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logging.info(f"Exported {len(data)} reviews to JSON: {filepath}")

    def export_csv(self, data, filepath: Path):
        if not data:
            logging.warning("No data to export to CSV.")
            return
        keys = data[0].keys()
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        logging.info(f"Exported {len(data)} reviews to CSV: {filepath}")

    def export_excel(self, data, filepath: Path):
        if not data:
            logging.warning("No data to export to Excel.")
            return
        df = pd.DataFrame(data)
        df.to_excel(filepath, index=False)
        logging.info(f"Exported {len(data)} reviews to Excel: {filepath}")