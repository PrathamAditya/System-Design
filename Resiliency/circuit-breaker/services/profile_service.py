# services/profile_service.py

import requests

POST_SERVICE_URL = "http://localhost:8001"

class ProfileService:

    def __init__(self, db):
        self.db = db

    def get_profile_with_posts(self, profile_id: str):
        profile = self.db.profiles.find_one(
            {"profile_id": profile_id},
            {"_id": 0}
        )

        if not profile:
            return None
        
        response_check_health = requests.get(f"{POST_SERVICE_URL}/health").status_code
        is_response_healthy = (response_check_health == 200)
        print(response_check_health)
        if(is_response_healthy):
            response = requests.get(f"{POST_SERVICE_URL}/posts/{profile_id}")
            posts = response.json()
        else:
            print("Post service is not healthy. Returning profile with empty posts list.")
            posts = []

        profile["posts"] = posts
        return profile