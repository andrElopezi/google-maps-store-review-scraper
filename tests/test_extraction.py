thonimport unittest
from src.extractors.google_maps_parser import GoogleMapsParser
from src.extractors.review_cleaner import ReviewCleaner

class TestExtraction(unittest.TestCase):
    def test_parser_returns_reviews(self):
        parser = GoogleMapsParser()
        result = parser.extract_reviews("https://maps.google.com/test")
        self.assertTrue(len(result) > 0)
        self.assertIn("review_text", result[0])

    def test_cleaner_removes_extra_spaces(self):
        cleaner = ReviewCleaner()
        review = {"review_text": " Hello   world "}
        cleaned = cleaner.clean_review(review)
        self.assertEqual(cleaned["review_text"], "Hello world")

if __name__ == "__main__":
    unittest.main()