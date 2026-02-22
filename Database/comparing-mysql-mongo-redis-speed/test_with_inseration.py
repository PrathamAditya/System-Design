import time
import random
import mysql.connector
import redis
from pymongo import MongoClient

TOTAL_RECORDS = 10000
READ_ITERATIONS = 10000

print("Connecting to databases...")

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
mongo_client.admin.command("ping")

mongo_db = mongo_client["testdb"]
mongo_collection = mongo_db["users"]

# ---------------- REDIS ----------------
redis_client = redis.Redis(
    host="127.0.0.1",
    port=6379,
    password="root",
    decode_responses=True
)
redis_client.ping()

print("All databases connected successfully.\n")

# ============================================================
# INSERT DATA
# ============================================================

print("Inserting data...")

# MySQL
mysql_cursor.execute("DELETE FROM users")
mysql_conn.commit()

for i in range(1, TOTAL_RECORDS + 1):
    mysql_cursor.execute(
        "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
        (i, f"User {i}", f"user{i}@test.com")
    )
mysql_conn.commit()

# Mongo
mongo_collection.delete_many({})
docs = [
    {"id": i, "name": f"User {i}", "email": f"user{i}@test.com"}
    for i in range(1, TOTAL_RECORDS + 1)
]
mongo_collection.insert_many(docs)
mongo_collection.create_index("id", unique=True)

# Redis
redis_client.flushdb()
for i in range(1, TOTAL_RECORDS + 1):
    redis_client.set(
        f"user:{i}",
        f'{{"id":{i},"name":"User {i}","email":"user{i}@test.com"}}'
    )

print("Data inserted successfully.\n")

# ============================================================
# WARMUP
# ============================================================

print("Warming up...")

for _ in range(1000):
    rand_id = random.randint(1, TOTAL_RECORDS)
    mysql_cursor.execute("SELECT * FROM users WHERE id=%s", (rand_id,))
    mysql_cursor.fetchone()
    mongo_collection.find_one({"id": rand_id})
    redis_client.get(f"user:{rand_id}")

print("Warmup complete.\n")

# ============================================================
# BENCHMARK
# ============================================================

print("Running benchmark...\n")

# ---------------- MYSQL ----------------
start = time.perf_counter()
for _ in range(READ_ITERATIONS):
    rand_id = random.randint(1, TOTAL_RECORDS)
    mysql_cursor.execute("SELECT * FROM users WHERE id=%s", (rand_id,))
    mysql_cursor.fetchone()
mysql_time = time.perf_counter() - start

# ---------------- MONGO ----------------
start = time.perf_counter()
for _ in range(READ_ITERATIONS):
    rand_id = random.randint(1, TOTAL_RECORDS)
    mongo_collection.find_one({"id": rand_id})
mongo_time = time.perf_counter() - start

# ---------------- REDIS ----------------
start = time.perf_counter()
for _ in range(READ_ITERATIONS):
    rand_id = random.randint(1, TOTAL_RECORDS)
    redis_client.get(f"user:{rand_id}")
redis_time = time.perf_counter() - start

# ============================================================
# RESULTS
# ============================================================

print("========== RESULTS ==========")

def print_stats(name, total_time):
    avg_latency = (total_time / READ_ITERATIONS) * 1000
    qps = READ_ITERATIONS / total_time
    print(f"{name}:")
    print(f"  Total Time     : {total_time:.4f} sec")
    print(f"  Avg Latency    : {avg_latency:.4f} ms")
    print(f"  Requests/sec   : {qps:.2f}")
    print()

print_stats("MySQL", mysql_time)
print_stats("MongoDB", mongo_time)
print_stats("Redis", redis_time)