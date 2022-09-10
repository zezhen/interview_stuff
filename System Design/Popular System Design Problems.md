# Popular System Design Problems
----



1.  [[Designing Typeahead Suggestion|Designing Typeahead Suggestion]]
    1.  The basic idea is to build all the user type queries and their frequency into a trie tree, and keep top k queries in each node, which are summarized from children nodes
    2.  Two main problem:
        1.  Trie tree maintenance: build, update
            1.  aggregate user queries into hourly or daily feed
            2.  aggregate queries and frequencies in a window with size s
            3.  build the trie tree, do some compression on leave node, then update top k queries from bottom up to root
            4.  sliding window with some period p, generate incremental update data, apply to trie tree and rebuild the top k queries in each node if applicable.
        2.  Trie data partition
            1.  Range based partitioning
                1.  partition by first several letters, like ‘a’ or ‘ab’, etc, keep this partitioning meta information in zk for runtime check
                2.  need to consider hot spot problem, if a lot of words start with ‘a’, we can further partition using two first letters, but ‘b’ using only one letter.
                3.  might have to query multiple servers, e.g. user typed ’a’, we need to check ‘ab’, ‘ac’, …
            2.  Hash based partitioning
                1.  another hot spot is runtime request, if some prefix ‘cap’ is very popular, that server might have problems.
                2.  we could hash terms into multiple servers, but cons is that we need ask multiple server then aggregate the results.
2.  [[Designing Pastebin|Designing Pastebin]]
    1.  Create: user upload text, generate the id, text, user, etc into DB (consistent hashing, by paste\_id), store into LRU cache
    2.  Access: check caching first, if not hit, fetch from DB
    3.  Calculate QPS/Storage/Bandwidth/Memory, etc
3.  [[Designing Instagram|Designing Instagram]]
4.  [[Designing Twitter|Designing Twitter]]
5.  [[Designing Facebook’s Newsfeed|Designing Facebook’s Newsfeed]]
    1.  Above three are similar, including feed generation, storage, partition, notification, ranking
    2.  Data Partition refer to [[Data Partitioning_Sharding|Data Partitioning/Sharding]]
    3.  Feed Ranking refer to [[EdgeRank.md|EdgeRank]]
    4.  Overview
        *   ![[F63938DF-2C7F-412E-B384-A45ACD3DFE24.png]]
6.  [[Designing a Web Crawler|Designing a Web Crawler]]
    1.  This problem mainly focus on components’ functions, like URL frontier, document dedupe, url dedupe, etc
    2.  Overview
        *   ![[FC202A92-E85C-4892-86E8-F9D74135B137.png]]
7.  [[Designing Youtube or Netflix|Designing Youtube or Netflix]]
    1.  For the user uploaded videos, beside storing them, we have more things to need to do as below, thus 
        1.  encoding or compression.
        2.  store thumbnails picture, automatically generate or user provide
        3.  generate 1-3 seconds preview (youtube has)
        4.  video deduplication check
    2.  Overview
        *   ![[FE36A75A-B81C-40E9-BE75-69392312B983.png]]
8.  [[Designing a URL Shortening service like TinyURL|Designing a URL Shortening service like TinyURL]]
    1.  The main problem here is how to generate and partition the tinyurl token.
        1.  we need to avoid the duplication token
        2.  token is not predictable
    2.  Key Generation Service
        1.  pre-build all keys into key-DB
        2.  One or more services load the keys from DB, once it complete the load, they mark the keys as occupied, need to add lock during the loading time.
        3.  KGS persiste keys into local disk in case of server restart, flush used keys into key-DB periodically.
    3.  Overview
        *   ![[9DFD97CC-4623-4CAB-A523-A688B8683F9A.png]]
9.  [[Designing Twitter Search|Designing Twitter Search]]
    1.  It’s more similar to Gemini Search architecture. LB -> Adserver -> MatchBroker -> Query/Advertiser Servers
    2.  Overview
        *   ![[84B3AB7B-7969-4F7B-8AAE-0F5A7D3B0362.png]]
10.  [[Designing Facebook Messenger|Designing Facebook Messenger]]
    1.  Something learn from [Tushar’s V edio](https://www.youtube.com/watch?v=zKPNUMkwOJE)
        1.  Use websocket to create bi-direction communication between client and server, 
        2.  Use ZK to keep users’ login status, which determine whether we need push messages immediately or wait user to pull when login
        3.  Use encryption key  between two users’ conversion, use it to encrypt the message content
11.  [[Designing Dropbox|Designing Dropbox]]
    1.  The biggest problem is synchronization service and data duplication
        1.  we divide files into 4MB chunks, calculate the chunks’ hash and compare with all others’ to determine whether it’s already exist.
        2.  the goal of synchronization service is to reduce the amount of data to be transferred, thus it's only transferring the modified chunks.
    2.  Clients
        1.  Upload and download files.
        2.  Detect file changes in the workspace folder.
        3.  Handle conflict due to offline or concurrent updates.
    3.  Queue Service: a middleware between clients and notification service, 
        1.  Client send request to the global request queue to update the Meta Database
        2.  The Response Queues that correspond to individual subscribed clients are responsible for delivering the update messages to each client. (we can use rabbitMQ here)
    4.  Workflow
        1.  Client A uploads chunks to cloud storage.
        2.  Client A updates metadata and commits changes.
        3.  Client A gets confirmation, and notifications are sent to Clients B and C about the changes.
        4.  Client B and C receive metadata changes and download updated chunks.
    5.  Overview
        *   ![[7CC5883F-2C43-4BC7-A20A-F41B13F81E5D.png]]
12.  [[Designing an API Rate Limiter (__New__).md|Designing an API Rate Limiter (\*New\*)]]
    1.  Slide window
13.  [Twitter System Design](https://youtu.be/wYk0xPP_P_8)
    1.  ![[Archive/面试资料/System Design/_resources/Popular_System_Design_Problems.resources/unknown_filename.jpeg]]
14.  CDN
    1.  DNS + Cache
15.  



----

- Date: 2019-02-03
- Tags: #Interview/System-Design 



