# Blogs related to Backend Engineering

- [Understanding Database Isolation Levels](https://medium.com/nerd-for-tech/understanding-database-isolation-levels-c4ebcd55c6b9)
- [SSTables and LSM Trees](https://medium.com/the-developers-diary/sstables-and-lsm-trees-2e4b6c8be251)
- [Certificate Revocation is broken](https://scotthelme.co.uk/revocation-is-broken/)
- [SSL certificate revocation and how it is broken in practice](https://medium.com/@alexeysamoshkin/how-ssl-certificate-revocation-is-broken-in-practice-af3b63b9cb3)
- [Debugging the One-in-a-Million Failure: Migrating Pinterest’s Search Infrastructure to Kubernetes](https://medium.com/pinterest-engineering/debugging-the-one-in-a-million-failure-migrating-pinterests-search-infrastructure-to-kubernetes-bef9af9dabf4)
- [Why Google Uses Go, Mozilla Uses Rust, and Banks Still Use Java](https://medium.com/@harish852958/why-google-uses-go-mozilla-uses-rust-and-banks-still-use-java-8f5247910a66)
- [Cache Coherence: How the MESI Protocol Keeps Multi-Core CPUs Consistent](https://medium.com/codetodeploy/cache-coherence-how-the-mesi-protocol-keeps-multi-core-cpus-consistent-a572fbdff5d2)
- [What every programmer should know about memory, Part 1](https://lwn.net/Articles/250967/)

- [How one connection kills a database](https://planetscale.com/blog/debugging-live-database-connections)
    - If the app doesn't handle errors gracefully and depends on quick responses from orders, you've got downtime.
    - Not because of a hack, but because one unhandled exception prevented a COMMIT, kept a connection open, blocked a migration, and that migration blocked everything else.
    - By the way, this is preventable. It happens because the default for idle_in_transaction_session_timeout is disabled. Give it a value and Postgres times out transactions that haven't closed.

- [Problems with large tables in Postgres](https://planetscale.com/blog/dealing-with-large-tables-in-postgres)
    - Tell me to stop when I name the largest table in your database: logs, ledger, notifications, feed, events, chonk ... admit it, I got it, right? Product success leads to lots of data, lots of data leads to big tables, but big tables lead to predictable problems.
    - A customer had two tables, A and B. Table B is large and unpartitioned. It has a foreign key to A with cascade delete turned on. A single delete on A has to delete every child row in B. That can be 100s or 1000s of rows in B for every one in A.
    - You may already know that deleted rows in Postgres aren't automatically removed; they are marked for deletion. These marked rows hold space until the vacuum process reclaims it. Read Every UPDATE leaves a ghost to learn more. What you might not realize is that vacuum runs per table.
    - Vacuuming a single large table can tie up a worker for a long time. Vacuum uses a ring buffer so it does not evict the rest of shared_buffers (Postgres's shared page cache), but on a table larger than RAM it still competes with user queries for the same disks.
    - Large tables take longer to vacuum, and they also wait longer to start.
    - On Postgres 17, the default trigger is 20% of the table. A table with ~500 million rows needs ~100 million dead tuples before autovacuum begins. You can modify this value cluster-wide or per table by changing autovacuum_vacuum_scale_factor.
    - Partitioning can be a good first move to split your large table into more reasonable-size chunks, if it has a suitable key.
    - Partitioning also helps avoid autovacuum's late start. Each partition is its own smaller heap, so the 20% trigger fires after far fewer dead tuples. Workers vacuum partitions in parallel and ANALYZE samples a smaller relation.
    - Vertical scaling can help more workers finish sooner with faster disks. That does not change the trigger on one huge heap, and the table may still not fit in RAM.
    - Sharding (horizontal scaling) gives you the best of both worlds. Smaller tables on smaller databases, each with their own isolated resources.
    - Sharding also solves foundational parts of Postgres that can't be resolved by more resources.
    - Vacuum can't remove a dead tuple while any transaction in the cluster still needs it.
    - To compact a bloated table while reads and writes continue, enable pg_squeeze on the database's Clusters page (that requires a restart), then run a one-time squeeze or register the table for regular cleanup. Be aware that pg_squeeze has no throttle. Squeezing a large table can saturate I/O and CPU and cause an outage. Only run it when the cluster has spare capacity.
    - It is impossible to write a Postgres article about performance and not mention that Postgres has a connection-per-process architecture. Connection hygiene matters even more when your database has a large table.
    - Postgres gives you three ways to take a backup. A large table complicates each one in a unique way.
    - A logical dump with pg_dump writes live rows, so dead tuples stay out of the output. The dump still walks the bloated heap, and it holds a transaction snapshot the whole time. On a small table, that pin is brief. On a large table, the backup is a long-running transaction against the cluster.
    - A file system backup copies the data directory, bloat and all. Faster than dumping rows. A consistent copy usually means shutting the database down, or relying on atomic snapshots from the file system. You might be okay with a maintenance window for a database of small tables, but a single large table could add hours just to copy one relation.
    - Continuous archiving copies the data files while Postgres is still running, then keeps the WAL so you can replay through the modified bits and land on a consistent copy. No dump pin, no shutdown. You still copy the large table, bloat, and its indexes. What grows with the table is restore time. How long an incident waits on this heap plus the WAL written while the copy ran.
    - Partitioning rearranges files but doesn't shrink the copy. A pin held during dump is still cluster-wide. A physical backup includes the same bloat even if it is split across smaller tables.
    - Vertical scaling means faster copies through more resources. But the files aren't any smaller, so restore is only quicker because the disks are faster.
    - But neither partitioning nor vertical scaling changes the size of the data.
    - Sharding breaks down backups and restores into smaller, distinct units of work, allowing them to complete much faster. Recovery time depends on the slowest shard instead of the largest table.
    - To keep queries fast, you keep adding indexes to the table. While indexes make queries fast, they aren't free. They take disk, get vacuumed, get backed up, and make every write touch more files.
    - Indexes on a partitioned table are created on the logical table but stored and updated on each partition. Those smaller indexes are faster to build and cheaper to REINDEX.
    - Vertical scaling buys you more space to store more indexes ... but that's like fixing traffic congestion by adding another lane to the freeway.
    - A table is not only large because it has many rows; it might be that the rows are wide with many columns, or each row contains a large amount of data.
    - If a row exceeds ~2KB, oversized values go to TOAST, a separate table and indexes next to the heap you are already struggling to vacuum.
    - Just as partitioning breaks up a single table into many small pieces, sharding distributes the workload of your reads and writes across many database clusters.
    - Sharded database backups are individually smaller and can be massively parallelized, making database restoration faster as well. Operations finish at the time of the slowest shard, not all at once waiting on large, bloated tables.


































