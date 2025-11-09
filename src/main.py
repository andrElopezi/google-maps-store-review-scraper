thonimport json
import logging
from pathlib import Path
from extractors.google_maps_parser import GoogleMapsParser
from extractors.review_cleaner import ReviewCleaner
from exporters.data_exporter import DataExporter
from utils.language_filter import LanguageFilter
from utils.sort_handler import SortHandler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    input_file = Path("data/inputs.sample.txt")
    output_file = Path("data/sample_output.json")

    if not input_file.exists():
        logging.error(f"Input file {input_file} not found.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    parser = GoogleMapsParser()
    cleaner = ReviewCleaner()
    exporter = DataExporter()
    lang_filter = LanguageFilter(allowed_languages=["en", "es", "fr"])
    sorter = SortHandler(sort_by="newest")

    all_reviews = []
    for url in urls:
        logging.info(f"Extracting reviews from {url}")
        reviews = parser.extract_reviews(url)
        cleaned = [cleaner.clean_review(r) for r in reviews]
        filtered = lang_filter.filter_reviews(cleaned)
        sorted_reviews = sorter.sort(filtered)
        all_reviews.extend(sorted_reviews)

    exporter.export_json(all_reviews, output_file)
    logging.info(f"Extraction complete. Output saved to {output_file}")

if __name__ == "__main__":
    main()