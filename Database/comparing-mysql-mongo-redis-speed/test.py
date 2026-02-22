# from pymongo import MongoClient

# mongo_client = MongoClient(
#     "mongodb://root:root@127.0.0.1:27017/admin",
#     authSource="admin"
# )

# # Force authentication immediately
# mongo_client.admin.command("ping")

# mongo_db = mongo_client["testdb"]
# mongo_collection = mongo_db["users"]

# print("Mongo connected successfully!")

# import redis

# redis_client = redis.Redis(host="localhost", port=6379, password="root", decode_responses=True)
# print(redis_client.ping())

from pymongo import MongoClient

client = MongoClient("mongodb://root:root@127.0.0.1:27017/admin")
client.admin.command("ping")

db = client["testdb"]
collection = db["users"]

print("Document count:", collection.count_documents({}))