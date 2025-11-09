thonimport re
import logging

class ReviewCleaner:
    def clean_review(self, review: dict) -> dict:
        text = review.get("review_text", "")
        cleaned_text = re.sub(r"\s+", " ", text.strip())
        review["review_text"] = cleaned_text
        logging.debug(f"Cleaned review for {review.get('author_name')}")
        return review