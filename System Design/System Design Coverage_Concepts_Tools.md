# System Design Coverage/Concepts/Tools
----

\# Cover 

1.  Features
2.  Throughput => Read/Write QPS, Bandwidth
3.  Volume => DB size, Memory size
4.  Basic Function => High Level Architect
5.  Database => schema
    1.  bit length for id
6.  Data Partition/Shading => partition key
    1.  how to query
    2.  hot spot problem
    3.  how to update if necessary
7.  Latency => Caching
8.  Availability => Load Balancer
9.  
10.  Security & Privacy (encryption, private/public key)
11.  Define APIs (Restful / RPC)
12.  Cost Effective (value per call, how many hosts, etc)
13.  Class Diagram


Following below 5 steps:

1.  Define functionalities.
2.  Calculate data size, request volume(read/write), etc.
3.  Implement logic and data table in one host.
4.  Scale data and requests, pay attention to the hotspot issues.
5.  Handle requests concurrency and system corruption issues, understand data lifecycle, request lifecycle.


\# Concepts

1.  ==CAP theorem==
    1.  Consistency
    2.  Availability
    3.  Partition Tolerance
2.  ACID vs BASE
    1.  ACID: transaction database
        1.  Atomicity guarantees each transaction as a single “unit”, which either succeeds or fails completely, no partial changed, if fails, need to rollback to the state before this transaction.
        2.  Consistency ensure a transaction can only bring the database from one valid state to another, any change must be valid according to all defined rules.
        3.  Isolation ensure concurrent execution of transactions leave the database in the same state, that transaction were executed sequentially.
        4.  Durability guarantee that once a transaction has been committed, it will remain committed even in case of a system failure.
    
    *   RDBMS use logging to guarantee ACD, use lock to guarantee I
    
    3.  BASE: basic available + soft-state + eventual consistency
        1.  anti-ACID, partition >= available > consistency
3.  [Fallacies of Distributed Computing](https://en.wikipedia.org/wiki/Fallacies_of_distributed_computing)
4.  [FLP impossibility](https://www.the-paper-trail.org/post/2008-08-13-a-brief-tour-of-flp-impossibility/)
5.  [[Data Partitioning_Sharding|Data Partitioning/Sharding]]
    1.  Partition Methods
        1.  Horizontal scaling means that you scale by adding more machines into your pool of resources
            1.  easy scale out dynamically by adding more machines (partition), tradeoff due to CAP,  e.g. Cassandra, MongoDB
            2.  split different rows data into multiple tables/servers
            3.  caution: carefully select the split points to avoid unbalanced tables/servers.
        2.  Vertical scaling means that you scale by adding more power (CPU, RAM) to an existing machine.
            1.  single machine with upper limiter, scale up by more power/multi-core support and downtime,  e.g. MySql
            2.  split data by special features/columns, straightforward, low impact on other applications
            3.  caution: once the data growth, it may be necessary to further partition a feature specific DB across various servers.
        3.  Directory Based Partitioning
            1.  create a lookup service which knows your current partitioning scheme and abstracts it away from the DB access code
            2.  decouple applications from DB,
            3.  caution: add one more component, need to effort to maintain and also increase more latency
    2.  Partition Criteria
        1.  Key or Hash-based
            1.  hashcode % n : fixed the servers numbers
                1.  single point of failure
            2.  hashcode % (n/2): replica = 2 to solve SPOF, switch automatically between two replicas, e.g. Datastore
                1.  uneven load distribution, hot spot
            3.  Consistent hashing: distribute server nodes or their virtual nodes to hash ring, even load distribution, e.g. Dynamo, Cassandra
        2.  List Partition
            1.  each partition is assigned a list of values, so whenever we want to insert a new record, we will see which partition contains our key and then store it there
        3.  Round-robin partitioning
    3.  Common Problems: Join and denormalization (database de-norm); Referential integrity; Rebalancing.
6.  Strong vs Eventual consistency
    1.  Strong Consistency offers up-to-date data but at the cost of high latency.
        1.  Quorum NRW
            1.  N: replica numbers or quorum; R: minimum nodes a request need to read from; W: minimum nodes a request need to write to;
            2.  W + R > N guarantee strong consistency: 
                1.  W = 1, R = N: high write QPS
                2.  R = 1, W = N: high read QPS
                3.  W = R = N / 2 + 1 for normal use cases
    2.  Eventual consistency offers low latency but may reply to read requests with stale data since all nodes of the database may not have the updated data.
        1.  [Vector Clock and Causal Consistency](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
            1.  ![[Archive/面试资料/System Design/_resources/System_Design_Coverage_Concepts_Tools.resources/unknown_filename.4.png]]
        2.  Gossip: e.g. Casandra
            1.  State Transfer Model
                1.  the client will attach its vector clock and the replica will send back a subset of the state tree which precedes the client's vector clock (this will provide monotonic read consistency).
                2.  The client will then advance its vector clock by merging all the versions. This means the client is responsible to resolve the conflict of all these versions because when the client sends the update later, its vector clock will precede all these versions.
                3.  the client will send its vector clock and the replica will check whether the client state precedes any of its existing version, if so, it will throw away the client's update.
                4.  Replicas also gossip among each other in the background and try to merge their version tree together.
            2.  Operation Transfer Model
                1.  the sequence of applying the operations is very important, each replica has to defer executing the operation until all the preceding operations has been executed. 
                2.  Therefore replicas save the operation request to a log file and exchange the log among each other and consolidate these operation logs to figure out the right sequence to apply the operations to their local store in an appropriate order.
7.  ==Consensus== over distributed hosts
    
    *   ![[Archive/面试资料/System Design/_resources/System_Design_Coverage_Concepts_Tools.resources/unknown_filename.1.png]]
    
    1.  Master-Slave
        *   read from slave but replication with latency, write to master but has SPOF;
    2.  Multiple-Master
        *   solve SPOF problem but complicated to merge multiple versions
    3.  2PC
        
        *   ![[Archive/面试资料/System Design/_resources/System_Design_Coverage_Concepts_Tools.resources/unknown_filename.2.png]]
        
        1.  Disadvantage: it is a blocking protocol. If the coordinator fails permanently, some participants will never resolve their transactions: After a participant has sent an agreement message to the coordinator, it will block until a commit or rollback is received.
    4.  3PC
        
        *   ![[Archive/面试资料/System Design/_resources/System_Design_Coverage_Concepts_Tools.resources/unknown_filename.3.png]]
        
        1.  The main disadvantage to this algorithm is that it cannot recover in the event the network is segmented in any manner. (??) and longer latency due to 3 round trips.
    5.  Paxos
        1.  Phase 1 Proposer Election
            1.  a. Prepare: a proposer creates a message with a monotonically increasing number id n, and send to a Quorum of Acceptors.
            2.  b. Promise: acceptors received the prepare message with number n
                1.  if n is larger than every previous proposal numbers received, return “Promise” message, and ignore all future proposals with a number less than n; 
                    *   if it accepted a proposal in the past, it must include the previous number say m and corresponding value, say w in the response.
                2.  otherwise ignore this proposal. No response return or response denial message (Nack) to early stop this proposal.
        2.  Phrase 2: Propose
            1.  a. Accept
                1.  If a Proposer receives enough "Promises" from a Quorum of Acceptors, it needs to set a value v to its proposal, send to an Accept message (n, v) to a Quorum of Acceptors. ( v is z or x)
                    1.  if any Accepters report previous accepted proposal w (phase 1.b), choose the one with highest number, say z
                    2.  otherwise choose the original proposal value, say x
            2.  b. Accepted
                1.  if an Acceptor receives an Accept message (n, v), it must accept it if and only if it has not already promised to only consider proposals have a number greater than n.
                    1.  response an Accepted message to Proposer
                    2.  note: If another Proposer, unaware of the new value being decided, starts a new round with a higher number n, the Accepter can promise and later accept the new proposed value, even though it has accepted another one earlier.
                2.  otherwise ignore it
        3.  refer to [如何浅显易懂地解说 Paxos 的算法？](https://www.zhihu.com/question/19787937/answer/107750652), [Paxos算法](https://zh.wikipedia.org/wiki/Paxos%25E7%25AE%2597%25E6%25B3%2595%20), [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science))
    6.  ==Raft==
        1.  Leader Selection
        2.  Log Replication
        3.  Safety
        4.  Membership Change
        5.  
        6.  refer to [[Raft|Raft]], [raft-paper](https://www.infoq.cn/article/raft-paper)
    7.  Zookeeper Automic Broadcast protocol (ZAB)
        1.  Prospective leader election
            1.  ==Fast Paxos==
        2.  Discovery
            1.  Leader gathers information about the most recent transactions that its followers accepted
            2.  To discover the most updated sequence of accepted transactions among a quorum, and to establish a new epoch so that previous leaders cannot commit new proposals
        3.  Synchronization (2PC)
            1.  The leader communicates with the followers, proposing transactions from its updated history from the discovery phase
            2.  Followers acknowledge the proposals if their own history is behind the leader’s history. When the leader sees acknowledgements from a quorum, it issues a commit message to them. 
        4.  Broadcast or Write
            
            *   client Reads from any nodes
            *   clients Write state changes to any of the ZooKeeper nodes and this state changes are forward to the leader node. 
            
            1.  Proposal: leader generate a transaction with sequel number c and the leader’s epoch e, and send the transaction to all followers
            2.  Ack: a follower adds the transaction to its history queue and send ACK to the leader. 
            3.  Commit: a leader receives ACK’s from a quorum it send the the quorum COMMIT for that transaction. a follower that accept COMMIT will commit this transaction unless c is higher than any sequence number in its history queue. 
                1.  Blocking: follower will wait for receiving COMMIT’s for all its earlier transactions (outstanding transactions) before commiting.
        5.  Failures Detection
            1.  If a leader does not receive heartbeats from a quorum of followers within a given timeout, it abandons its leadership and shifts to leader election phase.
            2.  if a follower does not receive heartbeats from its leader within a timeout, it goes to leader election phase as well
8.  Optimistic vs Pessimistic Locking
    1.  Optimistic Locking: 
        1.  Begin: Record a timestamp/version marking the transaction's beginning.
        2.  Modify: Read database values, and tentatively write changes.
        3.  Validate: Check whether other transactions have modified data that this transaction has used (read or written). This includes transactions that completed after this transaction's start time/version, and optionally, transactions that are still active at validation time.
        4.  Commit/Rollback: If there is no conflict, make all changes take effect. If there is a conflict, resolve it, typically by aborting the transaction, although other resolution schemes are possible. 
    
    *   most applicable to high-volume systems and three-tier architectures where you do not necessarily maintain a connection to the database for your session
    
    3.  Pessimistic Locking:
        1.  lock the record for your exclusive use until you have finished with it. It has much better integrity than optimistic locking but requires you to be careful with your application design to avoid Deadlocks
        2.  To use pessimistic locking you need either a direct connection to the database (as would typically be the case in a two tier client server application) or an externally available transaction ID that can be used independently of the connection.
9.  [[NoSQL数据库笔谈|NoSQL数据库笔谈]]
    1.  Key-Value: Redis
    2.  Wide Column: Cassandra vs HBase
        1.  Cassandra: master-less, weak point is data consistency
        2.  HBase: master-slave, SPOF, weak point is data available
    3.  Document based: MongoDB vs Vespa
    4.  Graph based: Neo4j
10.  [[Caching|Caching]]: split or not, cannot be the source of truth
    1.  [Apache Traffic Server](https://docs.trafficserver.apache.org/en/latest/preface/index.en.html#what-is-apache-traffic-server) (ATS): a high-performance [web proxy](https://docs.trafficserver.apache.org/en/latest/admin-guide/configuration/cache-basics.en.html) [cache](https://docs.trafficserver.apache.org/en/latest/developer-guide/cache-architecture/architecture.en.html) that improves network efficiency and performance by caching frequently-accessed information at the edge of the network. 
        1.  SoN use [HTTP\_GET](https://docs.trafficserver.apache.org/en/latest/developer-guide/plugins/http-headers/index.en.html), client choose partition, no zookeeper
    2.  [Redis](https://redis.io/topics/introduction): in-memory data structure store, used as a database, cache and message broker. It supports multiple data structures, has built-in replication, automatic partitioning with Redis Cluster
11.  [Load Balancer](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5747976207073280): L4 vs L7 (TCP layer, L4 consider IP and port, L7 consider http uri)
    1.  distribute requests
        1.  round-robin, 
        2.  least-conn
        3.  ip-hash (session persistence)
        4.  random with weighting for memory or CPU utilization, etc.
    2.  keeps track of the status of all the resources while distributing requests
    3.  ![[56EAEAB4-FD75-4684-81CF-21CE50CD2B53.png]]
    4.  Layer 4 load balancing
        1.  transport layer, make routing decision on the source and destination IP and ports in packet header, without considering the contents of the packet
        2.  require less computation vs L7 
    5.  Layer 7 load balacing
        1.  application layer, make routing decision on various characteristics of the HTTP header and on the actual contents of the message, such as the URL, the type of data (text, video, graphics), or information in a cookie.
        2.  require more computing power, but has greater overall efficiency, 
    6.  [HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
    7.  [Nginx](http://nginx.org/en/docs/http/load_balancing.html)
    8.  DNS: one domain can points to multiple hosts
12.  CDNs & Edge
    1.  Content Delivery/Distribution Network
    2.  An edge server is a type of edge device that provides an entry point into a network, it serves as the connection between separate networks, Other edges devices include routers and routing switches.
13.  [Bloom Filters](https://blog.csdn.net/hguisu/article/details/7866173)
    1.  An empty Bloom filter is a [bit array](https://en.wikipedia.org/wiki/Bit_array) of m bits, all set to 0. There must also be k different [hash functions](https://en.wikipedia.org/wiki/Hash_function) defined, each of which [maps](https://en.wikipedia.org/wiki/Map_(mathematics)) or hashes some set element to one of the m array positions, generating a uniform random distribution.
    2.  To add an element, feed it to each of the k hash functions to get k array positions. Set the bits at all these positions to 1.
    3.  To query for an element (test whether it is in the set), feed it to each of the k hash functions to get k array positions. If any of the bits at these positions is 0, the element is definitely not in the set. If all are 1, then either the element is in the set, or the bits have by chance been set to 1 during the insertion of other elements, resulting in a [false positive](https://en.wikipedia.org/wiki/False_positive).
    4.  ![[Archive/面试资料/System Design/_resources/System_Design_Coverage_Concepts_Tools.resources/unknown_filename.png]]
    5.  [Count-min sketch](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch)
        1.  The goal of the basic version of the count–min sketch is to consume a stream of events, one at a time, and count the frequency of the different types of events in the stream. At any time, the sketch can be queried for the frequency of a particular event type i (0 ≤ i ≤ n for some n), and will return an estimate of this frequency that is within a certain distance of the true frequency, with a certain probability.
        2.  The actual sketch data structure is a two-dimensional array of w columns and d rows. The parameters w and d are fixed when the sketch is created, and determine the time and space needs and the probability of error when the sketch is queried for a frequency or [inner product](https://en.wikipedia.org/wiki/Inner_product). Associated with each of the d rows is a separate hash function;
14.  Design pattern & object oriented design
15.  virtual machines & containers
    1.  [[Note Kubernetes.md|Note Kubernetes]]
16.  [[Message Queue|Message Queue]]
17.  multi-threading, consistency, locks, synchronization, CAS (compare-and-swap)
18.  ==DB Indexes==: 
    1.  makes the trade-offs of increased storage overhead, and slower writes for the benefit of faster reads
    2.  [[从B树、B+树、B__树谈到R 树.md|从B树、B+树、B\*树谈到R 树]]
19.  http vs http2 vs long-polling vs web-sockets
    1.  http
        1.  Client opens a connection and requests data from the server.
        2.  The server calculates the response.
        3.  The server sends the response back to the client on the opened request
    2.  traditional polling: keep asking the server for any new data, a lot of responses are empty creating HTTP overhead.
    3.  long polling
        1.  the client requests information from the server exactly as in normal polling, but with the expectation that the server may not respond immediately
        2.  If the server does not have any data available for the client, instead of sending an empty response, the server holds the request and waits until some data becomes available.
        3.  Once the data becomes available, a full response is sent to the client. The client then immediately re-request information from the server so that the server will almost always have an available waiting request that it can use to deliver data in response to an event.
        4.  Each Long-Poll request has a timeout. The client has to reconnect periodically after the connection is closed, due to timeouts.
    4.  web-sockets:  bi-direction conversation over a single TCP connection, provides a persistent connection between a client and a server that both parties can use to start sending data at any time
    5.  Server-Sent Events (SSEs): the client establishes a persistent and long-term connection with the server. The server uses this connection to send data to a client
20.  ==Http (Restful) vs RPC vs Socket==:
    1.  RPC is built top on TCP, more efficient
    2.  Socket is an interface wrapper of TCP
21.  TCP/IP model
22.  ipv4 vs ipv6
23.  TCP vs UDP
24.  https & TLS
25.  
26.  DNS lookup
27.  Public key infrastructure & certificate authority 
28.  Symmetric and asymmetric encryption 
29.  
30.  Data Center/Racks/Hosts
    1.  [Datacenter Traffic Control: Understanding Techniques and Trade-offs](https://arxiv.org/pdf/1712.03530.pdf)
31.  CPU/Memory/HardDrive/Network/Bandwidth
32.  Random vs Sequential read/write on (traditional) disk
    1.  Ramdon Write need seek the disk before do writing, usually each disk seek will take around 10ms, it would take a lot of time if you randomly write many small data.
    2.  Sequentially writing data to that same disk takes about 30ms per MB
    3.  In Flash disk, random write don’t need to seek any more, if you write small data, each time system will load the entire page, modify the bytes then write back to disk.
    4.  https://flashdba.com/2013/04/15/understanding-io-random-vs-sequential/


\# Tools


1.  Cassandra
    1.  De-centralized, nodes construct a consistent hashing ring
    2.  Nodes use Gossip protocol to exchange information, thus each nodes has all information of others
    3.  User request to a node, it becomes a coordinator and contract with others pending on the request keys 
    4.  Primary key is for partition, secondary or tertiary keys are for sorting within partition
    5.  Cassandra offers the following partitioners:
        1.  Murmur3Partitioner (default): uniformly distributes data across the cluster based on MurmurHash hash values.
        2.  RandomPartitioner: uniformly distributes data across the cluster based on MD5 hash values.
        3.  ByteOrderedPartitioner: keeps an ordered distribution of data lexically by key bytes
    6.  development:
        1.  [Things You Should Be Doing When Using Cassandra Drivers](https://ahappyknockoutmouse.wordpress.com/2014/11/12/246/)
2.  HBase
    1.  Master-Slave, one or more region servers, each region server handles one or more regions
    2.  Data are ordered by rowkey and distributed into multiple region server, each server maintain one slice.
    3.  User request will go to the region server that contains the corresponding rowkeys, handle all the process
    4.  Further partition can be done based on rowkey, e.g. first 2 bytes, use the rest part to do ordering.
3.  MongDB/CouchBase
4.  Mysql
5.  Memcached / Redis: distributed mem caching
6.  Zookeeper
7.  Kafka
8.  NGINX/HAProxy: load balancer
9.  Solr/ElasticSearch
10.  BlobStore, like amazon S3
11.  Docker: Kubernetes, Mosos
12.  Hadoop/Spark
    1.  HDFS


\# Reference 
https://github.com/checkcheckzz/system-design-interview

----

- Date: 2019-01-02
- Tags: #note #Interview/System-Design 



