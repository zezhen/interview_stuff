# Vespa
----

Components

1.  [Distributors](https://docs.vespa.ai/documentation/distributor.html): documents are accessed through a distributor.
2.  [Buckets](https://docs.vespa.ai/documentation/content/buckets.html): groups of [documents](https://docs.vespa.ai/documentation/documents.html), using hashing or hints in the document id.
    1.  Buckets are split when they grow too large, and joined when they shrink. This is a key feature for high performance in very small to very large instances, and eliminates need for downtime or manual operations when scaling.
    2.  A bucket contains [tombstones](https://docs.vespa.ai/documentation/elastic-vespa.html#data-retention-vs-size) of recently removed documents. Read more about document expiry and batch removes in [document expiry](https://docs.vespa.ai/documentation/documents.html#document-expiry).
3.  Content Nodes: provide a Service Provider Interface (SPI) between elastic bucket management system and the storage ([proton](https://docs.vespa.ai/documentation/proton.html)).
4.  [Cluster Controller](https://docs.vespa.ai/documentation/clustercontroller.html): manages the state of the distributor and content nodes.


[Elastic Vespa](https://docs.vespa.ai/documentation/elastic-vespa.html)

1.  Indexing
    1.  Offline index is not supported
        1.  It requires the partition layout to be known in the offline system, which is in conflict with elasticity and auto-recovery
        2.  it is completely at odds with realtime writes. 
    2.  [Writing to Vespa](https://docs.vespa.ai/documentation/writing-to-vespa.html)
        1.  [Document API](https://docs.vespa.ai/documentation/document-api-guide.html): Restful, http client, linux client, java API
        2.  [Processing chain](https://docs.vespa.ai/documentation/document-processing-overview.html): manipulating and indexing documents, forward the request to distributor using the distribution algorithm and the cluster state.
            1.  With no known cluster state, the client library will send requests to a random node, which replies with the updated cluster state if the node was incorrect. Cluster states are versioned, such that clients hitting outdated distributors do not override updated states with old states.
        3.  Distributor: maps the documents to bucket and sends it to content nodes.
            1.  It keeps track of which content nodes that stores replicas of each bucket, based on the redundancy and information from the cluster controller.
            2.  Each bucket holds which content nodes store replicas of the buckets, the checksum of the bucket content and the number of documents and meta entries within the bucket.
        4.  [Cluster Controller](https://docs.vespa.ai/documentation/clustercontroller.html): manages the state of the distributor and content nodes.
        5.  Content node: it has a bucket management system, refer to proton. (each node has one distributor?)
        6.  Eventual [Consistency](https://docs.vespa.ai/documentation/content/consistency.html): it's maintained at bucket level. Content nodes calculate checksums based on the bucket contents, and the distributors compare checksums among the bucket replicas. And no node may store more than one replica of a bucket.
            1.  Write consistency
                1.  Write operations wait for replies from every replica and fail if less than redundancy are persisted within timeout. if success, changes to the search indexes are immediately visible by default.
                2.  Operations are persisted to a write-ahead log before being applied, the log is synced to disk at OS-specific intervals, usually 30s.
                3.  Each document write assigns a new ==wall-clock timestamp== to the resulting ==document version==. As a consequence, configure servers with NTP to keep clock drift as small as possible.
                4.  Multi-document transactions are not supported
            2.  Read consistency
                1.  Get or Visit operation never observe a partially updated document, as writes behave as if they are atomic.
                2.  Searches may observe partial updates, as updates are not atomic across index structures.
                3.  If replicas diverge, during a Get, Vespa performs a read-repair to fetch the document with latest version; during a Visit, the operation will by default wait until the replicas are back in sync.
            3.  ![[Archive/工作资料/Gemini/_resources/Vespa.resources/unknown_filename.png]]
2.  Retrieving Document
    1.  Get a document with specified id.
        1.  Request forward to a distributor vis document API;
        2.  The content node scans through all the document databases, and for each one it checks all three sub-databases. Once the document is found, the scan is stopped and the document returned. If the document is found in a Ready sub-database, the document retriever will apply any changes that is stored in the [attributes](https://docs.vespa.ai/documentation/attributes.html) before returning the document.
    2.  Visit a range of documents using [selection expression](https://docs.vespa.ai/documentation/reference/document-select-language.html)
        1.  A visit request creates an iterator over each candidate bucket. This iterator will retrieve matching documents from all sub-databases of all document databases. As for get, attributes values are applied to document fields in the Ready sub-database.
    3.  ![[Archive/工作资料/Gemini/_resources/Vespa.resources/unknown_filename.1.png]]
3.  Searching
    1.  Indexed search has a separate pathway through the system, no distributor, no SPI, etc
    2.  QR-server (query rewrite server) in [JDisc Container](https://docs.vespa.ai/documentation/jdisc/)  issues one query per document type to the top level dispatcher.
    3.  Top level dispatcher
        1.  a small process by default running on each container node, which is responsible for sending the query to each content node and collecting partial results.
        2.  It pings all content nodes every second to know whether they are alive, and keeps open TCP connections to each one.
        3.  If a node goes down, the elastic system will make the documents available on other nodes.
    4.  Content node matching
        1.  The match engine receives queries and routes them to the right document database based on the document type. The query is passed to the Ready sub-database, where the searchable documents are.
    5.  ![[Archive/工作资料/Gemini/_resources/Vespa.resources/unknown_filename.2.png]]
4.  Resizing
    1.  Resizing is orchestrated by the distributor, and happens gradually in the background. It uses a variation of the RUSH algorithms to distribute documents. Under normal circumstances, it makes a minimal number of documents move when nodes are added or removed. read more in section “document and bucket distribution”.
    2.  Adding nodes
        1.  new ideal states are calculated for all buckets. The buckets that should have a replica on the new node are moved, while the superfluous are removed
        2.  ![[Archive/工作资料/Gemini/_resources/Vespa.resources/unknown_filename.3.png]]
    3.  Removing nodes
        1.  The same redistribution happens like adding nodes. 
        2.  Once the node fails the secondary replicas are set active. If they were already in a ready state, they can start serving queries immediately. Otherwise they will have to index their data.
5.  Limitation and Tradeoffs: availability, data mention, remove unstable nodes, etc


[Proton](https://docs.vespa.ai/documentation/proton.html)

1.  Bucket management
    1.  keep the partitions and the buckets per partition; once all bucket managements are up, distributors will have full picture of buckets metadata, then all content nodes become up state.
    2.  Operations are ordered according to priority, and only one operation per bucket can be in-flight at a time
2.  Document DB
    1.  Each DB is responsible for a single document type.
    2.  FeedHandler handle the write, update or remove requests, logging first then hand to sub-DB based on request type.
    3.  Sub-Database
        1.  Ready: indexed documents, one copy is active for search, the rest are not active for redundancy.
        2.  Not-Ready: holds the redundant documents that are not searchable, documents there are not indexed.
        3.  Removed: keep the removed documents and it’s timestamp, pruned once timeout, or merge buckets from multiple nodes.
3.  Index
    1.  Index fields are string fields, for text search.
    2.  It has a memory index for the recent changes, implemented using B-trees, periodically flush to disk to merge.
    3.  When updating an indexed field, the document is read from the document store, the field is updated, and the full document is written back to the store. Read more from [Writing to Vespa](https://docs.vespa.ai/documentation/writing-to-vespa.html#performance).
4.  ![[Archive/工作资料/Gemini/_resources/Vespa.resources/unknown_filename.4.png]]



Documents and Buckets Distribution

1.  Documents to buckets
    1.  mapping documents into buckets is easy for content nodes to control, e.g. even distribution, simple caching and metadata transfer, simple consistency management, etc, and the number of buckets is controllable through configure.
    2.  As clusters grow or shrink, or document sizes in the cluster change, one may want to have a different amount of buckets in the cluster. This is achieved by bucket splitting and joining.
    3.  Documents have string identifiers that maps to a 58 bit numeric location. A bucket is defined as all the documents that shares a given amount of least significant bits within the location. The amount of bits used controls how many buckets will exist.
        1.  For instance, if a bucket contains all documents whose 8 LSB bits is 0x01, the bucket can be split in two by using the 9th bit in the location to split them. Similarly buckets can be joined by requiring one less bit in common.
    4.  The distributors may split the buckets further than the distribution bit count indicates, allowing more units to be distributed among the content nodes to create a more even distribution, while not affecting routing from client to distributors.
2.  Buckets to content nodes or distributor: [Ideal state distribution algorithm](https://docs.vespa.ai/documentation/content/idealstate.html)
    1.  Desired qualities for the ideal state algorithm:
        1.  minimal re-assignment on cluster state change. e.g.
            1.  if a node goes down or capacity reduced, only the buckets on this node will be reassigned.
            2.  if a node comes up or capacity increased, only buckets that moved to this node will be reassigned.
        2.  No skew in distribution
        3.  Lightweight algorithm.
    2.  Weighted random election
        1.  Given a bucket, we seed a random number generator with bucket id, then get pseudo-random node sequence.
        2.  Each node is assigned a distribution-key in the configuration, which is an index in the number sequence.
    3.  Weighted nodes
        1.  By enforcing all the numbers drawn to be floating point numbers between 0 and 1, we can introduce node weights using the following formula: ==r^(1/c)==, where r is the floating point number between 0 and 1 that was drawn for a given node, and c is the node capacity, which is the weight of the node.
    4.  Hierarchical distribution
        1.  By default, Vespa distributes buckets uniformly across all distributor and storage nodes, which doesn't consider location, nodes in same rack has higher network bandwidth, compared with that in one cluster or cross datacenter.
        2.  hierarchical distribution: datacenter -> cluster -> rack -> node
            1.  cautious data placement: each replica is distributed into diff rack, one will be in another cluster or even datacenter
            2.  performance data placement: all replicas are distributed into diff nodes in one rack for quick sync/recovery with higher network
            3.  hybrid data placement: e.g. 3 replicas, 2 in same rack, the rest one in another rack same cluster, datacenter or even another datacenter.


**Querying Vespa**

1.  ![[Archive/工作资料/Gemini/_resources/Vespa.resources/unknown_filename.5.svg]]
2.  Matching?
3.  Ranking

1.  First-phase ranking: a smaller and less accurate one on all matches as they are found, e.g. [nativeRank](https://docs.vespa.ai/documentation/nativerank.html): text match score
2.  Second-phase ranking(optional): a more expensive and accurate one only on the 100 best hits per content node, after matching and before information is returned to the container.



----

- Date: 2019-04-18
- Tags: #Interview/Gemini 



