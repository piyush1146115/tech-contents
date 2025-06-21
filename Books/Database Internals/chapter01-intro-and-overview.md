# Introduction and Overview

Database management systems can serve different purposes: some are used primarily for temporary hot data, some serve as a long-lived cold storage, some allow complex analytical queries, some only allow accessing values by the key, some are optimized to store time-series data, and some store large blobs efficiently.

Some sources group DBMSs into three major categories:
- Online transaction processing (OLTP) databases
- Online analytical processing (OLAP) databases
- Hybrid transactional and analytical processing (HTAP)

## DBMS Architecture

There’s no common blueprint for database management system design. Every database is built slightly differently, and component boundaries are somewhat hard to see and define.

Database management systems use a client/server model, where database system instances (nodes) take the role of servers, and application instances take the role of clients. Client requests arrive through the transport subsystem. Requests come in the form of queries, most often expressed in some query language. The transport subsystem is also responsible for communication with other nodes in the database cluster.

The execution plan is handled by the execution engine, which collects the results of the execution of local and remote operations. Remote execution can involve writing and reading data to and from other nodes in the cluster, and replication.

Local queries (coming directly from clients or from other nodes) are executed by the storage engine. The storage engine has several components with dedicated
responsibilities:
- **Transaction manager**
This manager schedules transactions and ensures they cannot leave the database in a logically inconsistent state.
- **Lock manager**
This manager locks on the database objects for the running transactions, ensuring that concurrent operations do not violate physical data integrity.
Access methods (storage structures)
These manage access and organizing data on disk. Access methods include heap
files and storage structures such as B-Trees or LSM Trees.
- **Buffer manager**
This manager caches data pages in memory
- **Recovery manager**
This manager maintains the operation log and restoring the system state in case
of a failure.

Together, transaction and lock managers are responsible for concurrency control: they guarantee logical and physical data integrity while ensuring that concurrent operations are executed as efficiently as possible.

## Memory- Versus Disk-Based DBMS

Database systems store data in memory and on disk. In-memory database management systems (sometimes called main memory DBMS) store data primarily in memory and use the disk for recovery and logging. Disk-based DBMS hold most of the data on disk and use memory for caching disk contents or as a temporary storage. Both types of systems use the disk to a certain extent, but main memory databases store their
contents almost exclusively in RAM.

Disk-based databases use specialized storage structures, optimized for disk access. In-memory, pointers can be followed comparatively quickly, and random memory access is significantly faster than the random disk access. Disk-based storage structures often have a form of wide and short trees, while memory-based implementations can choose from a larger pool of data structures and perform optimizations that would otherwise be impossible or difficult to implement on disk. Similarly, handling variable-size data on disk requires special attention, while in memory it’s often a matter of referencing the value with a pointer.

## Column- Versus Row-Oriented DBMS

Most database systems store a set of data records, consisting of columns and rows in tables. One of the ways to classify databases is by how the data is stored on disk: row- or column-wise. Tables can be partitioned either horizontally (storing values belonging to the same row together), or vertically (storing values belonging to the same column together).

Examples of row-oriented database management systems are abundant: MySQL, PostgreSQL, and most of the traditional relational databases. The two pioneer open source column-oriented stores are MonetDB and C-Store (C-Store is an open source predecessor to Vertica).

Column-oriented stores are a good fit for analytical workloads that compute aggregates, such as finding trends computing average values, etc. Processing complex aggregates can be used in cases when logical records have multiple fields, but some of them (in this case, price quotes) have different importance and are often consumed together.

During the last several years, likely due to a rising demand to run complex analytical queries over growing datasets, we’ve seen many new column-oriented file formats such as Apache Parquet, Apache ORC, RCFile, as well as column-oriented stores, such as Apache Kudu, ClickHouse, and many others [ROY12]

It is not sufficient to say that distinctions between row and column stores are only in the way the data is stored. Choosing the data layout is just one of the steps in a series of possible optimizations that columnar stores are targeting.

## Data Files and Index Files

The primary goal of a database system is to store data and to allow quick access to it. But how is the data organized? Why do we need a database management system and not just a bunch of files? How does file organization improve efficiency?

The main reasons to use specialized file organization over flat files are:
- Storage efficiency: Files are organized in a way that minimizes storage overhead per stored data record
- Access efficiency: Records can be located in the smallest possible number of steps.
- Update efficiency: Record updates are performed in a way that minimizes the number of changes on disk

A database system usually separates data files and index files: data files store data records, while index files store record metadata and use it to locate records in data files. Index files are typically smaller than the data files. Files are partitioned into pages, which typically have the size of a single or multiple disk blocks. Pages can be organized as sequences of records or as a slotted pages

New records (insertions) and updates to the existing records are represented by key/value pairs. Most modern storage systems do not delete data from pages explicitly. Instead, they use deletion markers (also called tombstones), which contain deletion metadata, such as a key and a timestamp. Space occupied by the records shadowed by their updates or deletion markers is reclaimed during garbage collection, which reads the pages, writes the live (i.e., nonshadowed) records to the new place, and discards the shadowed ones.

### Data Files

Data files (sometimes called primary files) can be implemented as index-organized tables (IOT), heap-organized tables (heap files), or hash-organized tables (hashed files).

When records are stored in a separate file, index files hold data entries, uniquely identifying data records and containing enough information to locate them in the data file. For example, we can store file offsets (sometimes called row locators), locations of data records in the data file, or bucket IDs in the case of hash files. In index-organized tables, data entries hold actual data records.

### Index Files

An index is a structure that organizes data records on disk in a way that facilitates efficient retrieval operations. Index files are organized as specialized structures that map keys to locations in data files where the records identified by these keys (in the case of heap files) or primary keys (in the case of index-organized tables) are stored.
An index on a primary (data) file is called the primary index. However, in most cases we can also assume that the primary index is built over a primary key or a set of keys identified as primary. All other indexes are called secondary.

If the order of data records follows the search key order, this index is called clustered (also known as clustering). Data records in the clustered case are usually stored in the same file or in a clustered file, where the key order is preserved. If the data is stored in a separate file, and its order does not follow the key order, the index is called nonclustered (sometimes called unclustered).

### Buffering, Immutability, and Ordering

A storage engine is based on some data structure. However, these structures do not describe the semantics of caching, recovery, transactionality, and other things that storage engines add on top of them. Storage structures have three common variables: they use buffering (or avoid using it), use immutable (or mutable) files, and store values in order (or out of order). Most of the distinctions and optimizations in storage structures discussed in this book are
related to one of these three concepts.

- **Buffering**
  This defines whether or not the storage structure chooses to collect a certain amount of data in memory before putting it on disk.
- **Mutability (or immutability)**
  This defines whether or not the storage structure reads parts of the file, updates them, and writes the updated results at the same location in the file. Immutable structures are append-only: once written, file contents are not modified. Instead, modifications are appended to the end of the file. 
- **Ordering**
  This is defined as whether or not the data records are stored in the key order in the pages on disk. 