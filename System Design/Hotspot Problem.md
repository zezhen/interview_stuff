# Hotspot Problem
----

Hotspot is mainly caused by two problems:

1.  Data uneven distributed
2.  Hotkeys
    1.  large data hotkeys
    2.  heavy reading hotkeys
    3.  heavy writing hotkeys


4 Main Scenarios:

1.  Storage hotspot
    1.  too much data that cannot fit into one host
        1.  sharding, e.g. partitioned by keys
    2.  uneven data distribution
        1.  use another primary key
        2.  use compound key
            1.  multiple keys
                1.  reading data need know all partition keys
            2.  primary key + (hashcode(another key\[s\]) % n), n is the weight for different key, default can be 1, n > 1 for hot keys
                1.  reading data need to scatter-gather n partition to read full data
                2.  writing data need to generate (hashcode(another key\[s\]) % n)
2.  Large Data Hotkeys
    1.  Whitelist or dynamic detect such hotkeys
    2.  Partition these keys data by primary key + (hashcode(another key\[s\]) % n)
        1.  reading and writing data described as #1.2.2.
3.  Heavy Writing Hotkeys
    1.  Separate reading and writing, e.g. master-slaves,
    2.  There can be multiple masters and their corresponding slaves, each maintains one partition
        1.  Redis cluster has multiple master-slaves for each partition
        2.  Cassandra use consistent hashing, there will be one partition and several replica.
    3.  Writing request
        1.  Add request into one queue and one working thread process the requests one by one, e.g. Redis (single-thread)
        2.  Call partition service directly, request-response mode, e.g. Cassandra
    4.  If one thread or one master host is not efficient to handle all write request, how to handle this problem?
        1.  We have to sacrifice the consistency or read performance
        2.  Sacrificing consistency: write to multiple-master, then merge data, remove either version if conflict
        3.  Sacrificing read performance: N hosts are for both read and write, R + W >= N, set W = 1 and R = N, write once and read all replica.
    5.  Writing Process Modes
        1.  Write Back
            1.  write to cache, ack success once cache confirmed. read more from “Success Writing Confirm” below.
            2.  cache async the updates to DB periodically, e.g. 2PC in zookeeper, redis or Gossip in Dynamo
            3.  high efficiency but potentially has data loss risk.
        2.  Write Through
            1.  write to both cache and DB
            2.  strong consistency, lower availability.
        3.  Write Around
            1.  write to DB only
            2.  strong consistency but increasing reading latency as first read always cache miss
4.  Heavy Reading Hotkeys
    1.  DB perspective
        1.  Option 1
            1.  whitelist/dynamic detect hotkeys and change hotkey to compound keys, e.g. add (random number % n)
            2.  duplicate hotkeys’ data into all compound keys, n replicas
            3.  while reading, use (random number % n) to generate compound keys and send read request
        2.  Option 2
            1.  whitelist or dynamic detect hotkeys
            2.  set up another set of hosts or small cluster dedicated for these host keys, each host keep full replica data
            3.  while reading, check whitelist first, send hotkeys request to this cluster, round robin select host for read
        3.  Comparison
            1.  Option 1
                1.  pros: reuse same cluster, e.g. Cassandra, no need other setting
                2.  cons: n replicas share exact same data, each replica has k replicas by Cassandra, (k=3 by default), more space need
            2.  Option 2
                1.  pros: dedicated cluster, thus no impact on primary cluster, n hosts maintain 1 replica, less space need
                2.  cons: need to maintain separated clusters or hosts
    2.  Cache perspective
        1.  Option 1: similar to option 1 in DB perspective, add more redundancy and round robin distribute reading requests to multiple replica
        2.  Option 2: cache the hotkeys’ data in application servers (LRU), considering application servers can vertically scaling efficiently.
        3.  Two options can be applied together.
5.  Detect Reading/Writing Hotkeys
    1.  trending topic: sliding windows + hotkey threshold
6.  Success Writing Confirm
    1.  There are several way to confirm the writing is successfully.
        1.  Write into MEM,
        2.  Sync to local disk,
        3.  Write to k replica out of m.
    2.  only #1is not persistent as once the host down, the data will gone.
    3.  only #2 is better as host restart can retrieve the snapshot back, cons is 1) must in same host, 2) periodically persistent into disk is low efficient.
    4.  #1 + #3: persistent and efficient, e.g. Kafka, while need to keep k above some level, another concern is that the network and replica hosts performance will have big impact on the writing performance. Two ways for the data sync between writing node and replica nodes.
        1.  Push: most time is blocking push until replica hosts confirm, there will be a downtime depends the size of data need to sync, e.g. RabbitMQ
        2.  Pull: replica hosts trigger the sync periodically, master node has watermark indicate the latest state, every replica keep its own watermark, so that they can pull the gap data + latest updated data. Once catch up, replica ack to master node, then master update the watermark and ack to client. e.g. Kafka, which has a ISR to reduce the impact of network and low perf hosts. refer to [[Message Queue|Message Queue]].
    5.  #2 + #3: more persistent but lower efficient than above, e.g. RabbitMQ




----

- Date: 2019-03-06
- Tags: #Interview/System-Design 



