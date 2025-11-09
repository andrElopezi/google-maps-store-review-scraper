thonimport logging
import random
import datetime

class GoogleMapsParser:
    def extract_reviews(self, url: str):
        logging.debug(f"Simulating extraction for {url}")
        fake_data = []
        for i in range(random.randint(3, 6)):
            review = {
                "input_url": url,
                "shop_name": "Sample Coffee Shop",
                "shop_rating": "4.5",
                "shop_review_count": 1000,
                "author_name": f"User{i}",
                "author_profile_link": f"https://maps.google.com/user{i}",
                "is_local_guide": random.choice(["Yes", "No"]),
                "author_review_count": random.randint(1, 500),
                "author_photo_count": random.randint(0, 100),
                "author_rating": random.randint(1, 5),
                "author_review_timestamp": (datetime.datetime.now() - datetime.timedelta(days=i*10)).isoformat(),
                "review_text": f"Great place #{i}",
                "review_image_urls": [],
                "review_likes": random.randint(0, 20),
                "review_link": f"{url}/review{i}",
                "review_details": {"Service": 5, "Atmosphere": 4},
            }
            fake_data.append(review)
        return fake_data