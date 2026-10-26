# ACID

ACID = Atomicity, Consistency, Isolation and Durability

- What is a transaction?
- Atomicity
- Isolation
- Consistency
- Durability

## What is Transaction

- A transaction is a collection of queries
- One unit of work
- Example: Account Deposit (SELECT, UPDATE, UPDATE)
- Transaction Lifespan
    - Starts with BEGIN
    - Ends with COMMIT
    - Transaction ROLLBACK
    - Transaction unexpected ending = ROLLBACK


## Isolation

- Can my inflight transaction see changes made by other trasactions?
- Dirty reads: You read something, but that write was not actually fully flushed
- Non repeatable reads
- Phantom reads
- Lost Updates