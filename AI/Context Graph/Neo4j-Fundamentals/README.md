# Neo4j Fundamentals

Ref: https://graphacademy.neo4j.com/courses/neo4j-fundamentals

## What is Neo4j?

https://graphacademy.neo4j.com/courses/neo4j-fundamentals/1-graph-thinking/1-what-is-neo4j/

- Graph databases are useful when connection between the data is as useful as data itself

## Thinking in Graphs

https://graphacademy.neo4j.com/courses/neo4j-fundamentals/1-graph-thinking/2-thinking-in-graphs/

- Relationships in a graph are treated with the same importance as nodes that connect them.
- When you create a relationship between two nodes, the database stores a pointer to the relationship with each node. When reading data, the database will follow pointers in memory rather than relying on an underlying index.
- This means that the query time remains constant to the size of the relationships expanded regardless of the overall size of the data.
- Graph databases are a great fit for scenarios when you need to handle relationships efficiently.
