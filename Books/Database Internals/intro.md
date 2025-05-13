# Intro

## Who is this book for
If your company depends on any infrastructure component, be it a
database, a messaging queue, a container platform, or a task scheduler, you
have to read the project change-logs and mailing lists to stay in touch with
the community and be up-to-date with the most recent happenings in the
project. Understanding terminology and knowing what’s inside will enable
you to yield more information from these sources and use your tools more
productively to troubleshoot, identify, and avoid potential risks and
bottlenecks. Having an overview and a general understanding of how
database systems work will help in case something goes wrong. Using this
knowledge, you’ll be able to form a hypothesis, validate it, find the root
cause, and present it to other project maintainers.


This book is also for curious minds: for the people who like learning
things without immediate necessity, those who spend their free time
hacking on something fun, creating compilers, writing homegrown
operating systems, text editors, computer games, learning programming
languages, and absorbing new information.

One of the advantages of learning the fundamental concepts, proofs, and
algorithms is that they never grow old. Of course, there will always be new
ones, but new algorithms are often created after finding a flaw or room for
improvement in a classical one. Knowing the history helps to understand
differences and motivation better.

## Scope of This Book
This is neither a book about relational database management systems nor
about NoSQL ones, but about the algorithms and concepts used in all
kinds of database systems, with a focus on a storage engine and the
components responsible for distribution.

## Part I. Storage Engines
The primary job of any database management system is reliably storing
data and making it available for users. 

The storage engine (or database engine) is a software component of a
database management system responsible for storing, retrieving, and
managing data in memory and on disk, designed to capture a persistent,
long-term memory of each node. One way to look at this is that database
management systems are applications built on top of storage engines,
offering a schema, a query language, indexing, transactions, and many
other useful features. Storage engines such as BerkeleyDB, LevelDB and its descendant
RocksDB, LMDB and its descendant libmdbx, Sophia, HaloDB, and many
others were developed independently from the database management
systems they’re now embedded into.

Using pluggable storage engines has enabled database developers to bootstrap database systems using existing storage engines, and concentrate on the other subsystems.

### Comparing Databases

Every comparison should start by clearly defining the goal, because even the slightest bias may completely invalidate the entire investigation. o detect potential
problems, it is best to have long-running tests in an environment that simulates the
real-world production setup as closely as possible.

Knowing these variables can help to answer the following questions:
• Does the database support the required queries?
• Is this database able to handle the amount of data we’re planning to store?
• How many read and write operations can a single node handle?
• How many nodes should the system have?
• How do we expand the cluster given the expected growth rate?
• What is the maintenance process?

Most databases already have stress tools that can be used to reconstruct specific use cases. If there’s no standard stress tool to generate realistic randomized workloads in the database ecosystem, it might be a red flag. The more knowledge
you have about the database before using it, the more time you’ll save when running it in production. Choosing a database is a long-term decision, and it’s best to keep track of newly released versions, understand what exactly has changed and why, and have an upgrade strategy. New releases usually contain improvements and fixes for bugs and security issues, but may introduce new bugs, performance regressions, or unexpected behavior, so testing new versions before rolling them out is also critical. Checking how database implementers were handling upgrades previously might give you a good idea about what to expect in the future. Past smooth upgrades do not guarantee that future ones will be as smooth, but complicated upgrades in the past might be a sign that future ones won’t be easy, either.

### Understanding Trade-Offs

When looking at different storage engines, we discuss their benefits and shortcomings. If there was an absolutely optimal storage engine for every conceivable use case, everyone would just use it. But since it does not exist, we need to choose wisely, based on the workloads and use cases we’re trying to facilitate. There are many storage engines, using all sorts of data structures, implemented in different languages, ranging from low-level ones, such as C, to high-level ones, such
as Java. All storage engines face the same challenges and constraints.