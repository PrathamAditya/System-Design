class PostService:
    def __init__(self, db):
        self.db = db

    def get_posts_by_profile(self, profile_id: str):
        print(f"{profile_id}")
        return list(self.db.posts.find(
            {"profile_id": profile_id},
            {"_id": 0}
        ))