# Videos related to infra design

- [Engineering a Kubernetes Operator: Lessons Learned from Versions 1 to 5 - Andrew L'Ecuyer](https://www.youtube.com/watch?v=p2v7bPJkrVU)
    - Operators manage complexity. Adding HA, DR and seamless upgrades to Postgres isn't easy
    - Postgres HA & Operator HA
    - Automatically grow PVC. Run a sidecar in each Postgres instance to determine if it's running out of storage space or not. Then, use Kubernetes  PVC volume expansion to allow automatic resizing of PVC's without rolling update
    - Updates: A safe, fully-automated rolling update strategy for most upgrades & changes in Postgres
    - Disaster Recovery: Design considerations: WAL, Volume snapshot, Postgres Replica, Postgres Primary
        - A decentralized architecture allows them to operate on scale
        - Fight the "Not Invented Here" syndrome, and embrace existing solutions within the community
        - Prevention is better than praparedness
        - Manage risk associated with upgrade automation, and only automate when risks can be mitigated
        - When we can't automate, ensure we can orchestrate
        - Use status, conditions & events for upgrade visibility, and to empower engineers to safely perform upgrades

- [Explaining Prometheus Architecture](https://youtu.be/f4W_eEJC-20?si=W7kpLRQ1qcnder1T)
    - Prometheus collects metrics by sending http requests to /metrics endpoint of each target
    - Prometheus can be configured to use a different path other than /metrics
    - Prometheus has several native exporters
        - Node exporters
        - Windows
        - MySQL
        - Apache
        - HAProxy
    - Prometheus comes with client libraries that allow you to expose any application metrics you need Prometheus to track
    - Prometheus follows a pull based model
    - Prometheus needs to have a list of all targets it should scrape
    
