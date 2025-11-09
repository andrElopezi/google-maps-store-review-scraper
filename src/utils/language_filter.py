thonimport langdetect
import logging

class LanguageFilter:
    def __init__(self, allowed_languages=None):
        self.allowed_languages = allowed_languages or ["en"]

    def filter_reviews(self, reviews):
        filtered = []
        for r in reviews:
            try:
                lang = langdetect.detect(r.get("review_text", ""))
                if lang in self.allowed_languages:
                    filtered.append(r)
                else:
                    logging.debug(f"Filtered out non-allowed language: {lang}")
            except langdetect.lang_detect_exception.LangDetectException:
                logging.warning("Could not detect language, skipping review.")
        return filtered