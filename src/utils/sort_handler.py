thonfrom datetime import datetime

class SortHandler:
    def __init__(self, sort_by="newest"):
        self.sort_by = sort_by

    def sort(self, reviews):
        if self.sort_by == "newest":
            return sorted(reviews, key=lambda r: r.get("author_review_timestamp", ""), reverse=True)
        elif self.sort_by == "oldest":
            return sorted(reviews, key=lambda r: r.get("author_review_timestamp", ""))
        elif self.sort_by == "rating_high":
            return sorted(reviews, key=lambda r: r.get("author_rating", 0), reverse=True)
        elif self.sort_by == "rating_low":
            return sorted(reviews, key=lambda r: r.get("author_rating", 0))
        else:
            return reviews