# Relational Social Network Schema

Designed a minimal social media relational model in MySQL.

## Tables
- users (PK, UNIQUE, CHECK constraint)
- posts (1:N with users, ON DELETE CASCADE)
- profile (strict 1:1 using PK = FK)
- following (N:M self-referencing, composite PK, self-follow prevention)

## Transaction Experiments
1. Inserted user + profile inside a transaction → committed successfully.
2. Inserted user + invalid profile FK inside transaction → FK failed.
3. Committed after failure → successful statements persisted.

## Key Learnings
- Foreign keys enforce referential integrity.
- MySQL does not auto-rollback entire transaction on statement failure.
- Atomicity requires explicit ROLLBACK handling.
- Composite primary keys prevent duplicate relationships.