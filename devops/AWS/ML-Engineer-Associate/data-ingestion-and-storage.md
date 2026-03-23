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
- You can transition between storage classes
- Amazon S3 lifecycle rules:
    - Trasition actions
    - Expiration actions: configure objects to expire after some time
- Amazon S3 Analytics help you decide when to transition objects to the right storage class
- Amazon S3 Event Notification:
    - Can create as many S3 events as desired
    - SNS, SQS, Amazon Lambda can be event notification target
- Amazon EventBridge
- To setup event notifications: `bucket->properties->event-notifications`
- Amazon S3 Performance:
    - Latency 100-200 ms
    - 3500 PUT/DELETE per second
    - 5500 GET per second
    - Multi-part upload: can help parallelize upload
    - S3 transfer acceleration
    - S3 byte-range fetches
- Amazon S3 - Object Encryption
    - You can encrypt objects in S3 buckets using one of 4 methods
        - Server-Side-Encryption
            - SSE with AWS S3 Managed Keys
            - SSE with keys stored in AWS KMS
            - SSE with customer provided keys
        - Client-Side-Encryption
        - Dual-Layer Server Side Encryption based on KMS
    - KMS Advantage: user control + audit key usage using Cloudtrail
- Amazon S3 Access Points. Example: Finance Access points, Sales Access points, Analytics Access points
- S3 Object Lambda
    - Use AWS Laambda funcions to change the object before it is retrieved by the caller application
    - S3 bucket -> Lambda Access Point -> Redacting Lambda Function -> S3 Object Lambda Access Point


### Amazon EBS

- They can be mounted to one instance at a time
- They are bound to a specific availability zone
- It's a network drive
    - It uses the network to communicate to the instance
    - It can detached from an EC2 instance and attached to another quickly
- Have a provisioned capacity
- EBS delete on termination attribute: controls the EBS behaviour when an EC2 instance terminates
    - By default, the root EBS volume is deleted (attribute enabled)
- Amazon EBS Elastic Volumes
    - You don't have to detach a volume or restart your instance to change it
        - Just go to actions/modify volume from the console
    - Increase volume size
        - You can only increase, not decrease

### Amazon EFS

- Managed NFS that can be mounted on many EC2
- EFS work with EC2 instances in multi-AZ
- Highly available, scalable, expensive, pay per use
- Use cases: content management, web serving, data sharing, wordpress
- Uses NFSv4.1 protocol
- Only compatible with Linux based AMI
- Encryption at REST
- Performance Mode (set at EFS creation time)
    - General Purpose
    - Max I/O
- Throughput Mode:
    - Bursting
    - Provisioned
    - Elastic: automatically scales throughput up or down

### Amazon Fsx

- Launch 3rd party high-performance file systems on AWS
- Fully managed service
- Fsx for Lustre, Fsx for NetApp, Fsx for Windows file server
- FSx for OpenZFS
- FSx for Windows is a fully managed Windows file system share drive
- Support SMB protocol and Widows NTFS
- Lustre is a type of parallel distributed file system, for large scale computing
- The name Lustre is derived from Linux and cluster
- Lustre is used for High Performance Computing
- FSx file system deployment options:
    - Scratch file system
    - Persistent File system
- Amazon Fsx for NetApp ONTAP
- Amazon Fsx for OpenZFS

### Amazon Kinesis Data Streams

- Collect and store steaming data in real-time
- Real-time-data -> Producers -> Amazon Kinsis Data Streams -> Consumers
- Retention between upto 365 days
- Ability to replay data by consumers
- Provisioned Mode
    - Choose number of shards
- On-demand mode
    - No need of manual scaling