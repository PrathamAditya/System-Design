from services.post_service import PostService

class ProfileService:
    def __init__(self, db):
        self.db = db
        self.post_service = PostService(db)

    def get_profile_with_posts(self, profile_id: str):
        profile = self.db.profiles.find_one(
            {"profile_id": profile_id},
            {"_id": 0}
        )

        if not profile:
            return None

        posts = self.post_service.get_posts_by_profile(profile_id)

        profile["posts"] = posts
        return profile