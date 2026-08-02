# PART I - Introduction to Observability

- Chapter 1 traces where the term “observability” came from, how it was adapted for software systems, and what it actually means to have an observable system. It also looks at how to think about observability in the age of AI-assisted development and agentic applications.
- Chapter 2 is about how code crosses over from development into production, and what it takes to do that well.
- Chapter 3 is a retrospective on the evolution of observability, written by coauthor Charity Majors from her own perspective.


# CHAPTER 1 - What Is Observability?

The term “observability” was coined by engineer Rudolf E. Kálmán in 1960, in a paper that we now cite as the birth of modern control theory—the mathematics of systems you want to steer toward a desired state despite noise, disturbance, and incomplete information.

Kálmán’s key insight was that observability and controllability are duals. A system you cannot observe is, in a precise mathematical sense, a system you cannot control, and vice versa.

In 1995, Jean-Claude Laprie proposed a framework for measuring software dependability by evaluating six complementary properties that together describe a system’s
overall trustworthiness:
- Availability
- Reliability
- Maintainability
- Safety
- Confidentiality
- Integrity

To assess dependability, you have to look at three things together: what the system is supposed to do (functions), what it actually does (behavior), and how it’s built (structure)

## Cardinality

In mathematics, cardinality refers to the number of elements in a set. In databases, it means the number of unique values in a column. A column called Status that contains “true” or “false” has a cardinality of 2, while a universally unique identifier
(UUID) or any other unique set of values has the highest possible cardinality.

High-cardinality data is the most descriptive and identifying type of data, and it is vital for observability. Think of all the most useful attributes you would like to search or group by: build number, commit hash, container ID, span ID, user ID, app name, query hash, etc. All of which are high cardinality, and that is why they’re useful.

Cardinality is a never-ending nuisance for teams that rely heavily on metrics. High-cardinality data is the most valuable data, but metrics aren’t built to handle it. A
single metric can increase your bill by tens of thousands of dollars per week if enough cardinality slips into the data unnoticed.


## Observability Is a Property of Dependable Software

Can any engineer on your team, regardless of experience, quickly diagnose complex issues by interrogating the data your system emits? Or does a correct diagnosis
require deep institutional knowledge and a sixth sense?

In a software system with a high degree of observability, you should be able to:
-  Understand any system state that your application may have gotten itself into, even completely novel ones, without shipping new code to handle it (which
would imply you needed to know about it to find it).
- Compare one set of feature flags against any other set, then break down and group by endpoint, API key, query hash, or any other combination of interesting
dimensions, with no limits on cardinality.
- See how users are interacting with the feature you just shipped. Trace by transaction request, browser session, mobile app session, or chat history.
- If any of your service level objectives (SLOs) are burning hot, you should be able to select the violating events and surface any patterns. (“The spike in slow
requests is coming from read replicas in Australia, from a build ID we just deployed to 1% of canaries using flags x, y, and z; the client error string says DNS
is timing out.”)
- Find outliers. Any kind. Easily.