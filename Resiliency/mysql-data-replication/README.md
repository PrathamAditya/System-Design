# MySQL Master–Replica Replication (Docker Compose)

## 1. Start Containers

docker compose -f docker-compose-replication.yml up -d

Wait until both containers are fully initialized.

---

## 2. Configure Master

Login to master:

docker exec -it mysql-master-test mysql -uroot -proot

Set server id:

SET GLOBAL server_id = 101;

Create replication user:

CREATE USER 'replica'@'%'  -> '%' allowed to connect from any host.
IDENTIFIED WITH mysql_native_password 
BY 'replica_pass';

GRANT REPLICATION SLAVE ON *.* TO 'replica'@'%'; -> special privilege '.' apply to all DBs
FLUSH PRIVILEGES; -> reload table, mysql may not apply changes instantly

Get binary log coordinates:

SHOW MASTER STATUS;

Note the File and Position values.

---

## 3. Configure Replica

Login to replica:

docker exec -it mysql-replica-test mysql -uroot -proot

Set server id:

SET GLOBAL server_id = 102;

Configure replication (replace FILE and POSITION with actual values from master):

CHANGE REPLICATION SOURCE TO
  SOURCE_HOST='mysql-master-test',
  SOURCE_USER='replica',
  SOURCE_PASSWORD='replica_pass',
  SOURCE_LOG_FILE='mysql-bin.000003',
  SOURCE_LOG_POS=862;

START REPLICA;

Verify replication:

SHOW REPLICA STATUS\G

Ensure the following values:

Replica_IO_Running: Yes
Replica_SQL_Running: Yes

---

## 4. Test Replication

On master:

CREATE DATABASE testdb;
USE testdb;

CREATE TABLE users(
  id INT PRIMARY KEY,
  name VARCHAR(50)
);

INSERT INTO users VALUES (1, 'test_user');

On replica:

USE testdb;
SELECT * FROM users;

The inserted row should be visible on the replica.