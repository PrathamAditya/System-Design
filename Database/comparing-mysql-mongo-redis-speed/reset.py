import mysql.connector
import redis
from pymongo import MongoClient

print("Connecting...")

# ---------------- MYSQL ----------------
mysql_conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3307,
    user="root",
    password="root",
    database="testdb"
)
mysql_cursor = mysql_conn.cursor()

# ---------------- MONGO ----------------
mongo_client = MongoClient(
    "mongodb://root:root@127.0.0.1:27017/admin"
)
mongo_db = mongo_client["testdb"]
mongo_collection = mongo_db["users"]

# ---------------- REDIS ----------------
redis_client = redis.Redis(
    host="127.0.0.1",
    port=6379,
    password="root",
    decode_responses=True
)

print("Deleting records...")

# MySQL (fastest way)
mysql_cursor.execute("TRUNCATE TABLE users") ## TRUNCATE >>> DELETE FROM because it doesn't log individual row deletions
mysql_conn.commit()

# Mongo (delete all docs)
mongo_collection.delete_many({})

# Redis (clear entire DB)
redis_client.flushdb()

print("All records deleted successfully.")