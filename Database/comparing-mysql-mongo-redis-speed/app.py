import time
import mysql.connector
import redis
from pymongo import MongoClient

ITERATIONS = 10000
TEST_ID = 5000

# ---------------- MYSQL ----------------
mysql_conn = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="testdb"
)
mysql_cursor = mysql_conn.cursor(dictionary=True)

# Warm-up
mysql_cursor.execute("SELECT * FROM users WHERE id = %s", (TEST_ID,))
mysql_cursor.fetchone()

start = time.perf_counter()
for _ in range(ITERATIONS):
    mysql_cursor.execute("SELECT * FROM users WHERE id = %s", (TEST_ID,))
    mysql_cursor.fetchone()
mysql_time = time.perf_counter() - start

# ---------------- MONGO ----------------
mongo_client = MongoClient(
    "mongodb://root:root@127.0.0.1:27017/admin",
    authSource="admin"
)

# Force authentication immediately
mongo_client.admin.command("ping")

mongo_db = mongo_client["testdb"]
mongo_collection = mongo_db["users"]

# Warm-up
mongo_collection.find_one({"id": TEST_ID})

start = time.perf_counter()
for _ in range(ITERATIONS):
    mongo_collection.find_one({"id": TEST_ID})
mongo_time = time.perf_counter() - start

# ---------------- REDIS ----------------
redis_client = redis.Redis(host="localhost", port=6379, password="root", decode_responses=True)

# Warm-up
redis_client.get(f"user:{TEST_ID}")

start = time.perf_counter()
for _ in range(ITERATIONS):
    redis_client.get(f"user:{TEST_ID}")
redis_time = time.perf_counter() - start

print("\n----- RESULTS -----")
print(f"MySQL Time  : {mysql_time:.6f} sec")
print(f"MongoDB Time: {mongo_time:.6f} sec")
print(f"Redis Time  : {redis_time:.6f} sec")