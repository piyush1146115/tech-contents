# Data Ingestion and Storage

## Data Engineering Fundamentals

### Types of data:
- Structured: DB tables, CSV with consisteent column
- Semi-structured: Has some level of structure like tags, hierarchies, or other patterns. Example: JSON, XML, log files
- Unstructured: Data that doesn't have pre-defined schema.Example: Image, videos, audio, text files

### Properties of data

- Volume: Amount or size of data
- Velocity: Speed at which new data is geenerated
- Variety: Refers to the different types, structures, and sources of data

### Data warehouses, Lakes, and Lakehouses

- Data warehouse: A central repo optimized for analysis where data from different sources stored in a structured format. Example: Amazon Redshift, Google BigQuery
- Data lake: A storage repo that holds vast amounts of raw data in its native format including structured, semi-structured, and unstructured data. Example: AWS S3, Azure, Hadoop
- Data Lakehouse: A hybrid data architecture that combines best features of data lakes and data warehouses. Example: AWS Lake Formation, Databricks Lakehouse Platform, Azure Synapse
- ETL pipeline: Extract, Transform, Load

### Data Mesh

- Domain based data management
- Individual teams own data products within a given domain

### ETL Pipelines

- ETL stands for Extract, Transform, Load. It's a process used to move data from source systems into a data warehouse
- Convert the extracted data into a format suitable for the target data warehouse
    - Encoding or decoding data
    - Handling the missing data
- Load: Move the transfomed data into the target data warehouse or another data repository
- This process must be automated in some reliable way
- Example: AWS Glue
- Orchestration services:
    - EventBridge
    - Amazon Managed workflows for Apache Airflow
    - Lambda
    - Glue workflows

### Common Data Sources

- JDBC
  - java database connectivity
  - platform independent
  - language dependent
- ODBC
  - Open database connectiviry
  - Platform dependent
  - Language indenpendent
- Raw logs
- API's
- Stream

- CSV
- JSON: Lightweight, text-based
- Avro: Binary format that stores both the data and its schema
- Parquet: Columnar storage format optimized for analytics. Allows for efficient compression and encoding schemes.

### Amazon S3

- Max object size in S3 is 5 TB
- You can version your files in AWS S3. By default, the version id is empty
- Replication: Cross-region replication and same-region replication
    - Replication only works if versioning is enabled
    - Buckets can be in different AWS accounts
    - There is no chaining of replication
    - Create Repliation Rule from the source bucket's management tab
- S3 storage classes:
    - S3 standard general purpose
    - s3 stadard-infrequent access
    - s3 one zone infrequent access
    ....
- Durability: The durability is same for all storage classes
- Availability: Availability is different for different storage classes
- S3 intelligent tiering:
    - Small montly monitoring and auto-tiering fee
    - Moves object automatically between Access Tiers based on usage
    - There are no retrieval charges in S3 intelligent tiering

