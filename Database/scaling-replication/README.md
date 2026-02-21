# MySQL Replication Lab (Master–Replica Architecture)

## Overview

This lab demonstrates MySQL master–replica replication using Docker.

Two MySQL 8.0 instances were configured:

- mysql-master → Port 3308
- mysql-replica → Port 3307

Replication is configured using binary logs and asynchronous replication.

---

## Infrastructure Setup

- Docker containers used for isolation
- Master configured with:
  - server-id
  - binary logging enabled
- Replica configured with:
  - unique server-id
  - relay log
- Replication started using:
  - CHANGE REPLICATION SOURCE TO
  - START REPLICA

Replication status verified with:

Replica_IO_Running: Yes  
Replica_SQL_Running: Yes  

---

## Replication Behavior

Any DDL or DML executed on the master:

- CREATE DATABASE
- CREATE TABLE
- INSERT
- UPDATE
- DELETE
- ALTER TABLE

is automatically replicated to the replica.

Replication flow:

Master → Replica

Replication is asynchronous.

---

## Important Architectural Rule

Replication is strictly one-directional:

Master → Replica

There is no reverse replication.

Replica should be treated as read-only.

---

## Why Writing to Replica Is Dangerous

If data is inserted directly into the replica:

- That data exists only on replica
- It does NOT go back to master
- It does NOT replicate to other replicas
- System becomes inconsistent

This condition is called:

Replica Drift

Replica drift causes distributed data inconsistency.

---

## Production Safety Configuration

In production environments, replicas are configured with:

read_only = 1  
super_read_only = 1  

This prevents accidental writes to replica nodes.

---

## Transaction Observations

During transaction experiments:

- Foreign key violations do NOT automatically rollback entire transaction.
- Only the failing statement is rolled back.
- Explicit ROLLBACK is required to undo the full transaction.
- COMMIT persists successful statements.

Atomicity requires explicit handling at application level.

---

## Application-Level Read/Write Split (Python Demo)

A small Python script was used to:

- Connect to master for writes
- Connect to replica for reads

This simulates:

- Read scaling
- Master-replica routing
- Replication lag awareness

---

## Key Concepts Learned

- Referential Integrity
- Transaction Control
- Asynchronous Replication
- Read/Write Splitting
- Replica Drift
- Infrastructure vs Application Responsibility
- Distributed Data Consistency

---

## Next Steps

- Simulate replication lag
- Implement basic sharding
- Add routing logic at application level
- Explore Proxy-based routing (e.g., ProxySQL)