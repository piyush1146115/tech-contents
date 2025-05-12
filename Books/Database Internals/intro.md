# Who is this book for
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