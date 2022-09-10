# Cache
----

Terminology

1.  Storage Cost
2.  Retrieval Cost :  network load, algorithm load
3.  Invalidation: keep data up to date, remove irrelevant data
4.  Replacement Policy: FIFO?LFU/LRU/MRU/Random vs Belady’s algorithm
5.  Code/Warm Cache
6.  Cache Hit/Miss Ratio
7.  Write
    1.  Write Through
    2.  Write Around
    3.  Write Back

Spec

1.  Tera Byte
2.  50k to 1M QPS
3.  ~ 1ms Latency
4.  LRU (eviction)
5.  100% Availability
6.  Scalable


caches are only efficient when the benefits of faster access outweigh the overhead of checking and keeping your cache up to date; more cache hits than misses.

Where are caches used?

1.  Hardware level, e.g. cpu, hdd
2.  OS, e.g. RAM
3.  Web stack
    1.  Browser
    2.  DNS
    3.  CDN
4.  Applications
    1.  query cache, e.g.Mysql, files
    2.  storing denormalized result in DB
    3.  object cache, e.g. Hashtable


Redis Lazy Free

1.  for each redis object, there is an expiration time. Unless you set the object to expire, that time is "never".
2.  the expiration mechanism itself is semi-lazy. Lazy expiration means that you don't actually expire the objects until they are read
3.  the problem is that if a key is never touched, it just takes up memory for no reason.
4.  Redis adds a second layer of random active expiration. It just reads random keys all the time, and when an expired key is touched it is deleted based on the lazy mechanism. This does not affect the expire behavior, it just adds "garbage collection" of expired keys.

[Lazy Redis is better Redis](http://antirez.com/news/93)
UNLINK is a smart command: it calculates the deallocation cost of an object, and if it is very small it will just do what DEL is supposed to do and free the object ASAP. Otherwise the object is sent to the background queue for processing. Otherwise the two commands are identical from the point of view of the keys space semantics.

[[YCDB|YCDB]]
****
min-sketch

----

- Date: 2019-03-04
- Tags: #Interview/System-Design 



