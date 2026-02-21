import mysql.connector
import time

# Master connection (writes)
master = mysql.connector.connect(
    host="localhost",
    port=3308,
    user="root",
    password="root",
    database="test_replication"
)

# Replica connection (reads)
replica = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="root",
    database="test_replication"
)


master_cursor = master.cursor()
replica_cursor = replica.cursor()

# Insert into master
print("Inserting into master...")
master_cursor.execute(
    "INSERT INTO demo (id, name) VALUES (%s, %s)",
    (2, "ReplicaTest")
)
master.commit()

time.sleep(1)
# Read from replica
print("Reading from replica...")
replica_cursor.execute("SELECT * FROM demo")
rows = replica_cursor.fetchall()

for row in rows:
    print(row)


master.close()
print("master connection closed.")
replica.close()
print("replica connection closed.")