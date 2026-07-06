# Videos about backend or DB

- [What are Reactive Databases and why DiceDB exists?](https://youtu.be/V6hi86woFl8?si=y-79sgNNGt-GW-bJ)

- [How do indexes make databases read faster?](https://youtu.be/3G293is403I?si=tAdIDU1WNuTwn961)

- [What are L4 Load Balancers](https://youtu.be/RcarDmgWezY?si=MPM2jnHCxwTKQgq5)
    - L4 load-balacer works in 2 modes- passthrough mode and proxy mode
    - Selection is based on connection-level metadata
    - Source IP and Port, Destination IP and Port Protocol, or some metadata
    - Proxy mode:
        -  LB Terminates client connection
        - Starts a new TCP connection to the backend
        - Two TCP connection exists: Client <> LB <> Backend
        - Example: HAProxy, Envoy, Nginx Stream falls under this category 

- [How PayPal Beat the Thundering Herd Problem and Fixed Their Architecture](https://www.youtube.com/watch?v=pFBCgFzS2W8)
    - A simple solution could be exponential backoff
    - DLQ- unprocessed message gets dumped there
    - Job retry storms can bring down distributed systems
    - Processor service gets overwhelmed when bursts of jobs retry at once
    - Jitter introduces random variation to retry delays to desynchronize retry attempts
        - breaks retry convergence
        - scatters retry attempts across a time window
        - reduces peak loads during degradation
        
- [The Best Programmer I Know • Daniel Terhorst-North • GOTO 2024](https://youtu.be/ybA0zxwgpxw?si=-4zez1i90sksDRFz)

- [PostgreSQL Internal Architecture Explained](https://youtu.be/Q56kljmIN14?si=MUvLFKgmu7gGlKGs)
    - PostMaster process: 5432
        - Postgres handle the MVCC by following append-only model
    - Postgres is process based
    - Append only mechanism for writing
    - Worker group
    - Background workers
    - Auxilary processes
        - Check pointer
        - Logger
        - Backend writer
        - Auto Vacuam Launcher
        - wal archiver, wal receiver, wal writer
    - Redo logs

- [The Complexity of Simplicity](https://www.youtube.com/watch?v=Cum5uN2634o&t=2096s)
    - The essence of software systems is the creation of abstraction
    - Abstractions are qualitative; good ones allow us to hide gory implementation details - to build castles atop them and tunnels beneath
    - Once you understand how extraordinary complicated it is for a machine to work at all, you are humbled
    - Uncontained accidental complexity in one component can become essential complexity in something that must interact with it
    - Bad ones, however, leak: instead of sealing implementation details, they seep them- yielding systems that are unwidely and brittle
    - It's actually glorious to not to know how an operating system works. The developers of operating systems could hide all the layers of complexity inside the abstraction
    - Essential complexity and accidental complexity
    - Constructed systems
        - Constructed systems have high degrees of essential complexity and complicated abstractions - often to seeereve larger functionality
        - Big with reespect to scope, people, and time - it's software in the large
        - Example: OS, Complier, DB
    - Rebellious systems
        - The sheer girth and scope of constructed software systems often leave technologists asking: "does it have to be this complicated?!"
        - This leads to rebellious systems, once that overthrow what came before them, often by discarding unnecessary constraints
        - Example: RISC (v. CISC), Unix (v. Multics), PDF (v. PostScript), Microservices (v. monoliths)
    - Accreted systems
        - Accreted systems are ones that no one would design from first principles - they are by their nature compromises with time or space
    - Revolutionary systems
        - There are systems that seek to innovate with respect to the abstraction itself- the problem that they are solving includes the abstraction
        - These are revolutionary systems, which are often (but not always) developed by small, focussed teams - over an extended period of time
        - Example systems: CDC 6600, TCP/IP, Macintosh, EC2, HTTP, S3, EC2, Disco/VMware, LLVM, SQlite, Java, Python, Go, NFS, Typescript, Docker, Rust, Oxide
        - Revolutionary systems take both a long time to develop and it can be unclear when to ship
        - The biggest challenge for a revolutionary system is to stay funded long enough to effect the revolution it envisions for itself
        - It follows that developing revolutionary systems often requires taking on extraordinary amounts of essential complexity
        - Revolutionary systems are revolutionary exactly because they tackle essential complexity in a way that allows others to abstract it away
        - While we may feel we're drowning in complexity, remember that complexity is not entropy - revolutionary systems do exist!
        - It is very complicated to make things simple!

- [Designing Data-intensive Applications with Martin Kleppmann](https://www.youtube.com/watch?v=SVOrURyOu_U)
    - Reliability means fault tolerance. That means a system will work if something breaks like network, storage etc. 
    - Scalability
    - You can not make any assumption about upper bound of network delay in distributed systems
    - The goal of the book is to enable people making educated decision
    - A new ethics section in the 2nd edition
    - Relying on clock time doesn't work well in distributed systems
    - Sometimes to learn something, you need to struggle a bit with it
    - His recent research topics: Local first software, formal verification

- [What is Clickhouse](https://www.youtube.com/watch?v=FtoWGT7kS-c)
    - Open source
    - Column Oriented
    - Distributed
    - OLAP database
        - OLAP stands for Online Analytical Processing. In the context of ClickHouse, it refers to a category of database systems designed specifically for analytical workloads — as opposed to OLTP (Online Transaction Processing) systems like PostgreSQL or MySQL

- [In-depth: ClickHouse vs PostgreSQL](https://www.youtube.com/watch?v=iLXXoDaFoxs)
    - Clickhouse is a columnar database. That means it can contain an incredibly high amount of columns inside it and extremely fast at reading those
    - Clickhouse contantly merges data in background to collapse series data into single values to expedite queries
    - Postgres in single threaded, mainly memory heavy. Clickhouse has parellelized execution model, scale both in CPU and RAM types
    - Updating data in Clickhouse is expensive operation than Postgres
    - Postgres runs on a single engine. Clickhouse has different engine for your different purpose. Example: MergeTree, Replacing MergeTree, Aggregating MergeTree
    - Clickhouse use Apache Zookeeper to manage the shards
    - Clichouse was made to handle a lot of aggregate data, where Postgres in flexible
    - Clickhouse optimized data at every level. From storage to caching to return
    - Clickhouse often isn't being used alone. It complements other DBs like Postgres


- [The Cost of Concurrency Coordination with Jon Gjengset](https://www.youtube.com/watch?v=tND-wBBZ8RY&list=WL&index=11)
    - Have you heard these before?
        - Mutexes are slow
        - Reader-writer locks are best for read-heavy workloads
        - Lock-free data structures are always faster
    - More threads = worse performance
    - RwLock barely beats Mutex
    - Interlude: CPU Caches
    - Each CPU core has private caches
        - What happens when two cores cache the same memory and one wants to write?
        - CPU has hierarchy of caches. Most commonly, CPU has 3 levels of cache
        - L1 cache is very clsoe to CPU, its like soldered in the CPU
        - L3 cache on thee other hand, is pretty close to RAM. It is not far as RAM, but it is closer to CPU.
        - L3 cache usually shared amonng all the cores of CPU
        - L1 cache is not shared among cores
        - L2 is somewhere between L1 and L3. It's latency is also somewhere between L1 and L3.
        - These increase in size as they go up. L1 cache is very small, L2 cache is comparatively larger, L3 cache is decently larger
    - What happens if one core has some amount of memory like a counter in a local cache and then some other CPU core wants to read that memory
    - Cache coherence: the MESI protocol
        - MESI: Modified Exclusive Shared Invalid
        - Hardware tracks the state of each cache line
        - States: Modified, Exclusive, Shared, Invalid
            - Modified: Only copy, dirty (dirty means it differs from what's in RAM)
            - Exclusive: Only copy, clean
            - Shared: Multiple caches have it
            - Invalid: No valid copy
    - Write to shared data requires coordination between cores
    - Reader-writer read lock requires a WRITE
    - Two readers acquiring a read lock
    - Cache line ping-pong is expensive
    - Each invalidation is ~30+ ns - approaching main memory latency
    - As you get more readers, they contend more and more with each other
    - The left-right data structure
        - Let's keep two copies of the data
        - One for all the readers, and one for the writer (if any)
        - Swap the pointers when there are updates
        - The readers don't share state with each others
        - Rare writes is the key
    - A debugging story: the 4-core cliff
    - Left-right is NOT a drop-in replacement
        - 2X memory usage
        - Readers see stale data during publish
        - Single writer only
        - Operations must be deterministic
        - Writer waits for all readers to exi
    - Questions to ask yourself
        - What's my read/write ratio?
        - How long is my critical section
        - How many threads will contend?
        - Can I tolerate stale reads?
        - Do I need linerizability?
    - The real lesson: it's not about locks
        - Coordination is expensive because of cache coherence, not because of locks
    - Further reading:
        - "What every programmer should know about memory" - Ulrich Drepper
        - "Is parallel programming hard?" - Paul Mckenney
        - "Scalable reader-writer locks" - Andrei Pechkurov
        - "The left-right crate" - Jon Gjenset

```rs
pub fn read(&self) -> RwLockReadGuard {
    self.reader_count.fetch_add(1, ...);
}
```

- [Make computers FAST (Systems Performance chapter 1)](https://www.youtube.com/live/RBpIzmOcPmw?si=tdAnB6rXsKf3Sv4i)
    - The software stack
        - many components, each contributing to perf
        - Application -> database -> system libraries -> system calls -> kernel -> hardware devices
        - Kernel = (Proc scheduler, file system, network card, virtual memory)
    - Case study in slow DB queries
        - Reports of slow disk
        - what's the root cause
    - Profiling vs tracing
    - Flame graphs 