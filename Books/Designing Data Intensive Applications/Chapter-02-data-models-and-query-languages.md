# Chapter 02: Data Models and Query Languages


Most applications are built by layering one data model on top of another. For each layer, the key question is: how is it represented in terms of the next-lower layer?

There are many different kinds of data models, and every data model embodies assumptions about how it is going to be used. Some kinds of usage are easy and some are not supported; some operations are fast and some perform badly; some data transformations feel natural and some are awkward.


## Relational Model versus Document Model

The best-known data model today is probably that of SQL, based on the relational model proposed by Edgar Codd in 1970 [1]: data is organized into relations (called tables in SQL), where each relation is an unordered collection of tuples (rows in SQL).

The roots of relational databases lie in business data processing, which was performed on mainframe computers in the 1960s and ’70s. Other databases at that time forced application developers to think a lot about the
internal representation of the data in the database. The goal of the relational model was to hide that implementation detail behind a cleaner interface.

### The Birth of NoSQL

The name “NoSQL” is unfortunate, since it doesn’t actually refer to any
particular technology—it was originally intended simply as a catchy Twitter hashtag for a meetup on open source, distributed, nonrelational databases in 2009. 

There are several driving forces behind the adoption of NoSQL databases, including:
- A need for greater scalability than relational databases can easily achieve, including very large datasets or very high write throughput
- Specialized query operations that are not well supported by the relational model
- Frustration with the restrictiveness of relational schemas, and a desire for a more dynamic and expressive data model

### Many-to-One and Many-to-Many Relationships

In the preceding section, region_id and industry_id are given as
IDs, not as plain-text strings "Greater Seattle Area" and "Philanthropy". Why?

Whether you store an ID or a text string is a question of duplication. When you use an ID, the information that is meaningful to humans (such as the word Philanthropy) is stored in only one place, and everything that refers to it uses an ID (which only has meaning within the database). When you store the text directly, you are duplicating the human-meaningful information in every record that uses it.

In relational databases, it’s normal to refer to rows in other tables by ID, because joins are easy. In document databases, joins are not needed for one-to-many tree structures, and support for joins is often weak. 


### The relational model

What the relational model did, by contrast, was to lay out all the data in the open: a relation (table) is simply a collection of tuples (rows), and that’s it. In a relational database, the query optimizer automatically decides which parts of the
query to execute in which order, and which indexes to use. 

In a relational database, the query optimizer automatically decides which parts of the query to execute in which order, and which indexes to use. 


## Relational Versus Document Databases Today

The main arguments in favor of the document data model are schema flexibility, better performance due to locality, and that for some applications it is closer to the data structures used by the application. The relational model counters by providing better
support for joins, and many-to-one and many-to-many relationships.

The poor support for joins in document databases may or may not be a problem, depending on the application. For example, many-to-many relationships may never be needed in an analytics application that uses a document database to record which events occurred at which time.

It’s not possible to say in general which data model leads to simpler application code;
it depends on the kinds of relationships that exist between data items. For highly
interconnected data, the document model is awkward, the relational model is accept‐
able, and graph models (see “Graph-Like Data Models” on page 49) are the most
natural.

### Data locality for queries

A document is usually stored as a single continuous string, encoded as JSON, XML,or a binary variant thereof (such as MongoDB’s BSON). If your application often needs to access the entire document (for example, to render it on a web page), there is a performance advantage to this storage locality. If data is split across multiple tables, like in Figure 2-1, multiple index lookups are required to retrieve it all, which may require more disk seeks and take more time.


## Query Languages for Data

In a declarative query language, like SQL or relational algebra, you just specify the pattern of the data you want—what conditions the results must meet, and how you want the data to be transformed (e.g., sorted, grouped, and aggregated)—but not how to achieve that goal. It is up to the database system’s query optimizer to decide which
indexes and which join methods to use, and in which order to execute various parts of the query. The fact that SQL is
more limited in functionality gives the database much more room for automatic optimizations.

In databases, declarative query languages
like SQL turned out to be much better than imperative query APIs.

## MapReduce Querying

MapReduce is a programming model for processing large amounts of data in bulk across many machines, popularized by Google.



The map and reduce functions are somewhat restricted in what they are allowed to do. They must be pure functions, which means they only use the data that is passed to them as input, they cannot perform additional database queries, and they must not have any side effects. 

## Graph-Like Data Models

We saw earlier that many-to-many relationships are an important distinguishing feature between different data models.

A graph consists of two kinds of objects: vertices (also known as nodes or entities) and
edges (also known as relationships or arcs). Many kinds of data can be modeled as a
graph. Typical examples include:
- Social graphs
Vertices are people, and edges indicate which people know each other.
- The web graph
Vertices are web pages, and edges indicate HTML links to other pages.
- Road or rail networks. Vertices are junctions, and edges represent the roads or railway lines between them

Well-known algorithms can operate on these graphs: for example, car navigation systems search for the shortest path between two points in a road network, and
PageRank can be used on the web graph to determine the popularity of a web page and thus its ranking in search results.

## The Cypher Query Language

Cypher is a declarative query language for property graphs, created for the Neo4j graph database.