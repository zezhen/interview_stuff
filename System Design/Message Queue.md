# Message Queue
----

 


below is note from [RabbitMQ vs Kafka Series](https://jack-vanlightly.com/blog/2017/12/3/rabbitmq-vs-kafka-series-introduction)
**RabbitMQ**
****
![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.4.png]]


1.  Core Concepts
    1.  Producer emits messages to Exchange with routing key or header
    2.  Consumer get pushed messages from Queue
    3.  Binding connects an Exchange with a Queue using binding key
    4.  Exchange compares Routing key with Binding key or queue name (default exchange)
2.  Exchange Type
    1.  Fanout (fastest)
        1.  A message sent to a Fanout exchange will be broadcast to all queues and exchanges that have a binding to the exchange.
        2.  ![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.8.png]]
    2.  Direct
        1.  Route messages using the Routing Key set by the publisher, key is exact match by configuration.
        2.  Default Exchange
            1.  special direct exchange, implicit binding to each queue has as its binding key the name of the queue, can send a message directly to a specific queue by its name 
        3.  ![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.9.png]]
    3.  Topic
        1.  route using the Routing Key, but offer the use of two types of wildcard in the Binding Key.
            1.  \* wildcard matches a single word
            2.  # wildcard matches any number of words
    4.  Header (slowest)
        1.  parse the message headers, e.g. key->value information, set binding rules for various queues.
            1.  entity.type=booking, change.type=cancelled, x-match=all. I want all cancelled booking messages.
            2.  agent.id=2, client.id=1001, x-match=any. I want all messages related the specific travel agent or end client.
    5.  Consistent Hashing
        1.  partition a single queue into multiple queues and distribute messages between them via a hashing of the routing key, message header or message property.
        2.  problems:
            1.  RabbitMQ doesn't help you to coordinate your consumers across the partitioned queues like Kafka does
            2.  No virtual nodes to help prevent imbalanced distribution.
        3.  ![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.7.png]]
3.  Special Types
    1.  Dead Letter Exchanges
        1.  eject the messages that pass their TTL or from the full queue
    2.  Ephemeral Queues
        1.  auto-delete, exclusive queue for some consumers, TTL
    3.  Priority Queues
    4.  RPC: Direct Reply-To
        1.  The sender puts the name of a "pseudo queue" called amq.rabbitmq.reply-to in the reply-to message header. It is a pseudo queue because it is not really a queue at all, but it can be treated as one. The sender consumes this amq.rabbitmq.reply-to queue in no-ack mode
        2.  The recipient sends the response message to the Default exchange with the routing key as the name of this pseudo queue
        3.  The consumer gets pushed the message from the RabbitMQ node directly, without it having ever been written to a queue
4.  Push and Consumer Prefetch
    1.  pushes messages to consumers in a stream.
    2.  each consumer can configure a prefetch limit (aka  a QoS limit), to avoid upstream overwhelm


Kafka

![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.5.png]]

1.  Distributed, Replicated Commit Log.
    1.  ordering guarantees inside a log partition, each message is persisted to the log and remains there until cleaned up.
2.  Messaging Publish Subscribe
3.  Kafka can be an event sourcing platform, if size is not a problem, it can store the entire history of events
    1.  partition then become the key point, good partition reduce application reply or lookup effort, as it need to filter/transform on the sequential data
    2.  ![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.6.png]]
4.  Log Compaction
    1.  The standard data retention policies are time and space based policies
    2.  a log is compacted, the result is that only the most recent message per message key is retained, the rest are removed.
5.  Kafka Storage refer to [Gemini Kafka Workshop](https://docs.google.com/presentation/d/1WzpyUyiJX50eZ85DuJEzWcYiXJ2zCecYpb2Lp5Z1Q3M/edit?usp=sharing)
    *   Each partition is mapped to a logical file: represented as a set of segment files
    *   Each segment file has a corresponding Index file
        *   Translates logical message offsets to physical positions in the data file
        *   Each record contains 4 bytes logical offset and 4 bytes physical offset
        *   May not hold entry for all records in the message file
        *   Simple binary search to locate the key in index based on logical offset
        *   Offset stored is relative to the base offset of the index file (4 bytes instead of 8 bytes)
    *   Broker simply appends the message to the last segment file when producer publishes a message to the partition
    *   Messages stored in Kafka doesn’t have explicit message ids
    *   Messages are exposed by the logical offset in the log
        *   Id of next message = current logical offset + length of current message
    *   ![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.11.png]]
6.  Consumer Groups and more refer to[Gemini Kafka Workshop](https://docs.google.com/presentation/d/1WzpyUyiJX50eZ85DuJEzWcYiXJ2zCecYpb2Lp5Z1Q3M/edit?usp=sharing)
    1.  Group Coordinator
        1.  One broker is designated as consumer group co-ordinator
        2.  All consumers in group maintain their membership (partition allocation) by sending heartbeats to group coordinator
        3.  Loss of heartbeats from a consumer can trigger partition assignment - rebalance
    2.  Partition Assignment
        
        1.  coordinator select one of the consumers in group as leader
        2.  topic subscriptions from all members are propagated to the leader
        3.  leader decides partition assignment for whole group, e.g. round robin
        

**Comparison**

1.  Message Order
    
    1.  RabbitMQ: FIFO ordering guarantee at queue level, consumers can share one queue, which are competing consumers, it can guarantee global order in queue, but no order among consumers
    2.  Kafka: partition more to scale out, but only ensure publishing and consuming order within partition
    
    1.  Pull and Push
        1.  push is great for low latency, and when have competing consumers of a single queue, push can distributed evenly, pull in this scenario will cause uneven.\]
        2.  pull is controlled in consumer side by maintaining offset, and can reply easily, batching messages can reach high throughput
    2.  Delivery Guarantees
        1.  RabbitMQ: at-most-once or at-least-once
            1.  Message Durability - not losing messages once stored in RabbitMQ
                1.  Queue Mirroring: queues can be replicated across multiple nodes, 
                    1.  mirrors don’t exist for scale out but solely for redundancy.
                    2.  when master dies, the cluster then promotes the oldest mirror to be new master
                        1.  what if queues are scheduled to one or less nodes? => Rebalancing Masters, but there is not great tools and queue blocking sync.
                    3.  Data Synchronization 
                        1.  For a new or outdated mirror queue, should master copy (push) all its data to it? Notice, **data sync is blocking operation**.
                            1.  ha-sync-mode=automatic, automatically sync data from master, full redundancy.
                            2.  ha-sync-mode=manual, keep empty, sync new message write to master
                                1.  what if this queue is promoted to master? all other queues older than it are down. there are two choices
                                    1.  ha-promote-on-failure=always: promoted regardless of data loss => High Availability
                                    2.  ha-promote-on-failure=when-synced: wait until previous master come back => Data Consistency
                                2.  considering the messages in RabbitMQ is transitory, this queue will eventually be sync with master.
                            3.  automatic can guarantee data consistency but when the data in master is large, it’s tradeoff is the availability.
                                1.  what if do the copy from another mirror?
                    4.  Network Partitions
                        1.  A netword partition happened, whether need to promoted mirror to master? a.k.a. split-brain
                        2.  if split and publisher write to both masters => data diverge
                        3.  if not, publisher in the network without master cannot write => lost availability
                        4.  ![[Archive/面试资料/System Design/_resources/Message_Queue.resources/unknown_filename.10.png]]
                        5.  Split-Brain + Pause Minority
                            1.  do split brain when network partition occurs, pause the queues in minority side, pause the clients’ connection
                            2.  promote oldest queue in majority side, redirect all clients to master,
                            3.  Client Connectivity is important for availability.
                                1.  Access the cluster via a load balancer and remove the paused/downed nodes from the list as soon as detected
                                2.  clients can connect to any node and internal routing ensures that the client talks to the right node.
                2.  Durable: persisted to Disk or ==Mnesia database==
                3.  Key Deficiencies: 
                    1.  nodes that rejoin a cluster throw away their data
                    2.  synchronization is blocking and causes queue unavailability
            2.  Message acknowledgements - signalling between RabbitMQ and publishers/subscribers
                1.  publisher can choose ack or no ack.
                2.  consumer can choose no act or manual ack
                3.  connection exceptions or broker failure: republish or ignore? as there is no way for publisher or broker to know exact status
                    
            3.  Kafka: at-most-once or at-least-once, exactly-once with Kafka Streams
                1.  Message durability - not losing messages once stored in a topic
                    1.  Log Replication: leader-followers at log partition level. 
                        1.  All reads and writes on a partition go to the leader, followers are for redundancy.
                        2.  Followers periodically send **fetch** requests to the leader to get the latest messages. (default 500ms)
                            1.  The leader and each follower stores a Log End Offset (LEO) and Highwater Mark (HW). The LEO is the last message offset the replica has locally and the HW is the last committed offset.
                            2.  When the leader receives a message, it persists it locally. A follower makes a fetch request, sending its own LEO. The leader then sends a batch of messages starting from that LEO and also sends the current HW. When the leader knows that all replicas have persisted a message at a given offset, it advances the HW.
                            3.  Consumers are only delivered messages up to the current HW
                        3.  Master Balancing: Kafka has concepts that preferred replica leaders, which tries to distribute the leaders of each partition evenly across the nodes, controller node can automatically reassign leadership back to preferred replica leaders, dive into ISR
                    2.  In-Sync Replicas (ISR)
                        1.  A follower is considered “in-sync” if it's completely up-to-date with the leader at some point within _replica.lag.time.max.ms (x)_ time period
                        2.  A follower will be removed from the ISR if 1) they don’t make fetch request with x time period (dead),  2) out of date for longer than x time period (slow followers)
                        3.  publisher write message with ack=all, the leader must wait for all replicas in the ISR to have persisted the message
                            
                            1.  consider follower periodically fetch, the latency would be at least 500ms, what’s more, a slow follower may make longer latency, default is 10s!!, but eventually it would be remove from ISR and bring latency back. (very good design)
                            
                        4.  Leader Fail-Over
                            1.  Controller is notified by zk, the first follower in ISR become the leader, it make the HW as current LEO, other followers truncate their local log to HW to avoid divergence.
                                1.  It is possible that the follower that gets elected is not the most caught up, ack=all is important, if set, then the log truncation won’t be a big problem (all is bet)
                            2.  Fail-over to unclean leader? unclean.leader.election.enable=true?
                                1.  It might failover to a slow follower that has less data, choose availability or data consistency? If producer cannot write, can it persistent itself?
                                2.  min.insync.replicas specify min number ISR, choose consistency over availability.
                        5.  Data Synchronization
                            1.  New or rejoined followers will start outside of the ISR and not participate in message commits. They will simply be there, fetching messages as fast as they can until they are caught up with the leader and are added to the ISR. 
                            2.  There is no blocking, there is no throwing away all their data.
                        6.  Network Partitions
                            1.  Scenario 1: A follower cannot see the leader, but can still see Zookeeper
                                *   follower will be removed from ISR, no data loss, just reduced redundancy, it will catch up once network partitions resolved
                            2.  Scenario 2: A leader cannot see any of its followers, but can still see Zookeeper
                                *   the ISR shrinks, no data loss
                            3.  Scenario 3: A follower can see the leader, but cannot see Zookeeper
                                *   in ZK, this follower will be marked as dead, but no action need to take (controller still know it)
                            4.  Scenario 4: A leader can see its followers, but cannot see Zookeeper
                                *   ZK will mark it dead, and notify Controller to elect a new leader, in a short period, there might be two leader, until the former leader realize it lose connection with ZK and reject all writes, clients will find new leader later.
                                *   during this period, there would be data loss.
                            5.  Scenario 5: A follower is completely partitioned from both the other Kafka nodes and Zookeeper
                                *   ZK mark it’s dead, leader remove it from ISR
                            6.  Scenario 6: A leader is completely partitioned from both the other Kafka nodes and Zookeeper
                                *   similar to scenario 4, 
                            7.  Scenario 7: The Kafka controller node cannot see another Kafka node
                                *   this node won’t be a leader in a failover
                            8.  Scenario 8: The Kafka controller cannot see Zookeeper
                        
                        *   ZK mark it’s dead and elect new controller
                        
                        8.  Client Connectivity
                            1.  Clients can be given multiple brokers that they can connect to, in the _bootstrap.servers_ producer and consumer configs.
                            2.  boostrap servers are a bridgehead. The client can ask them which node hosts the leader of the partition they want to read/write to, it is critical for ensuring that clients can talk to the right nodes and detect the new node once a fail-over has occurred.
                    3.  Message acknowledgements - signalling between Kafka (and possibly ZooKeeper) and publishers/subscribers
                        1.  publisher send a message with expect Acks: no ack, leader persist ack, leader and all in sync replica persist
                        2.  consumer offset tracking: offset can be stored in zookeeper, but for batch messages, failure might happen after partial data processed
                            1.  exact-once on batch messages => [Kafka Streams](https://kafka.apache.org/documentation/streams/) whose output of processing a message is to write a new message to a different topic can achieve exactly-once processing.
                        3.  connection exceptions or broker failure: Kafka has ==message deduplication== feature, e.g. idempotent publishing
                    4.  Consensus Architecture - Zookeeper
                        1.  Storing the list of topics, the partitions, configuration, current leader replicas, preferred replicas, ISR.
                            1.  Each leader is responsible for maintaining the ISR, and update to Zookeeper
                        2.  Monioring heartbeats from all brokers
                        3.  Electing the controller node which includes controller node fail-over when the controller dies.
                            1.  controller node is one of the Kafka brokers, has responsibility of electing replica leaders.
                            2.  Zookeeper sends the Controller notifications about cluster membership and topic changes and the Controller must act on those changes, e.g.
                                1.  a new topic with 10 partitions and replica factor of 3
                                2.  a Kafka broker dies that hosts a replica leader
                    5.  Message Loss Scenarios
                        1.  Any leader fail-over where messages were acknowledged with acks=1
                        2.  Any unclean fail-over (to a follower outside of the ISR), even with acks=all
                        3.  A leader isolated from Zookeeper receiving messages with acks=1
                        4.  A fully isolated leader whose ISR was already shrunk to itself, receving any message, even acks=all. This is true only if min.insync.replicas=1.
                        5.  Simultaneous failures of all nodes of a partition. Because messages are acknowledged once in memory, some messages may not yet have been written to disk. When the nodes come back up some messages may have been lost.
                2.  A Note about Batching
                    1.  RabbitMQ achieve something similar to batching as below, similar like TCP does.
                        1.  pausing publishing every x messages until all acks have been received, group acknolwedgements using the multiple flag.
                        2.  consumers setting a prefetch and grouping acks using the multiple flag
                    2.  Kafka
                        1.  publisher can achieve higher performance, but tradeoff is that more duplication or double processing once failure
                        2.  consumer side is more efficient, each partition has only one consumer
                            *   not like RabbitMQ may meets unbalanced loads across competing consumers
                3.  A Note about persisted
                    1.  RabbitMQ will only send a publisher confirm once the master and all mirrors have written the message to **disk**
                        1.  this adds extra latency, 1) fsyncs are invoked every few hundred milliseconds, 2) mirrors can go offline and it can take up to the net tick time to discover it is down. This can add latency when a mirror is slow or down
                    2.  Kafka has made the decision to acknowledge once a message is in **memory** for performance reasons
                        1.  it fsyncs to disk on an interval, it’s a bet that redundancy will make up for the risk of storing acknowledged messages in memory only for a short period of time
                            
                4.  
            
            [[__Cloud Messaging Service - Yahoo__.md|**Cloud Messaging Service - Yahoo**]]
            
            
            * * *
            
            Message Queue
            
            Message Queue（MQ），消息队列中间件。很多人都说：MQ通过将消息的发送和接收分离来实现应用程序的异步和解偶，这个给人的直觉是——MQ是异步的，用来解耦的，但是这个只是MQ的效果而不是目的。MQ真正的目的是为了通讯，屏蔽底层复杂的通讯协议，定义了一套应用层的、更加简单的通讯协议。一个分布式系统中两个模块之间通讯要么是HTTP，要么是自己开发的TCP，但是这两种协议其实都是原始的协议。HTTP协议很难实现两端通讯——模块A可以调用B，B也可以主动调用A，如果要做到这个两端都要背上WebServer，而且还不支持长连接（HTTP 2.0的库根本找不到）。TCP就更加原始了，粘包、心跳、私有的协议，想一想头皮就发麻。MQ所要做的就是在这些协议之上构建一个简单的“协议”——生产者/消费者模型。MQ带给我的“协议”不是具体的通讯协议，而是更高层次通讯模型。它定义了两个对象——发送数据的叫生产者；消费数据的叫消费者， 提供一个SDK让我们可以定义自己的生产者和消费者实现消息通讯而无视底层通讯协议。
            
            
            ## MQ的流派
            
            **列出功能表来比较MQ差异或者来一场“MQ性能大比武”的做法都是比较扯的**，首先要做的事情应该是分类。我理解的MQ分为两个流派
            
            *   
            
            *   
            
            *   
            *   
            *

----

- Date: 2016-07-20
- Tags: #note #Interview/System-Design 
- Source URL: [](http://mp.weixin.qq.com/s?__biz=MzIxMjAzMDA1MQ==&mid=2648945475&idx=1&sn=b9758fdc31925419f12a9ece1d27018d&scene=2&srcid=0721LeL1Tjc5OGIG0ZrSH8oy&from=timeline&isappinstalled=0#wechat_redirect)



