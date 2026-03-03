from pymongo import MongoClient
from services.profile_service import ProfileService
from services.post_service import PostService

client = MongoClient("mongodb://root:root@localhost:27017/")
db = client["testdb"]

profile_service = ProfileService(db)

result = profile_service.get_profile_with_posts("profile_101")

print(result)
# print(PostService.get_posts_by_profile('profile_101'))