# Consistenct Hash and Load Balancer
----

1.  String Hash
    1.  ![[Archive/面试资料/System Design/_resources/Consistenct_Hash_and_Load_Balancer.resources/unknown_filename.png]]
    2.  MD5: 128 bit, 不具备强抗碰撞性
    3.  SHA-1: 160 bit, 不具备强抗碰撞性
    4.  SHA-2: 商业机构
    5.  Non-cryptographic hash functions
        1.  [MurmurHash](https://github.com/aappleby/smhasher)
        2.  [xxHash](https://github.com/cespare/xxhash)
        3.  [MetroHash](https://github.com/dgryski/go-metro) 
        4.  [SipHash1–3](https://github.com/dgryski/go-sip13)
2.  Consistent Hash
    1.  Start from 1997: [Consistent Hashing and Random Trees](https://www.akamai.com/es/es/multimedia/documents/technical-publication/consistent-hashing-and-random-trees-distributed-caching-protocols-for-relieving-hot-spots-on-the-world-wide-web-technical-publication.pdf) => used in Amazon Dynamo
        *   [Uhashring](https://github.com/ultrabug/uhashring)
            1.  Nodes w/ or w/o weights => vnodes => hash ring
            2.  key => hash => search in hash ring => node
            3.  add/remove node don’t have to move too much data compared with mod n mechanism
    2.  Still have problems:
        1.  the load distribution across the nodes can still be uneven
        2.  increase vnodes can mitigate #1 but comes with significant memory cost
    3.  Jump Hash 2014 Google: [A Fast, Minimal Memory, Consistent Hash Algorithm](https://arxiv.org/abs/1406.2294)
        *   it has no memory overhead and virtually perfect key distribution.
        *   The loop executes O(ln n) times, faster by a constant amount than the O(log n) binary search for Ring Hash
        *   https://github.com/dgryski/go-jump
    4.  [Multi-Probe Consistent Hashing](https://arxiv.org/abs/1505.00062) 2015 Google
        *   instead of hashing the nodes multiple times and bloating the memory usage, the nodes are hashed only once but the key is hashed ktimes on lookup and the closest node over all queries is returned. 
        *   https://github.com/dgryski/go-mpchash
    5.  [Maglev: A Fast and Reliable Software Network Load Balancer](https://research.google.com/pubs/pub44824.html) 
    6.  Implementation:
        
        1.  https://github.com/ultrabug/uhashring: 逻辑比较简单, 默认用md5作为hash func, node根据权重等信息生成tag并hash, 加入到有序数组中作为hash ring; 查找key的hash值在hash ring(有序数组)中二分查找, 即可得到对应位置; 插入/删除 node需要重新生成hash ring, 没有node间的通讯协议.
        2.  Java version as below
3.  Load Balance
    
    1.  [Maglev: A Fast and Reliable Software Network Load Balancer](https://blog.acolyer.org/2016/03/21/maglev-a-fast-and-reliable-software-network-load-balancer/) 2016 Google
    2.  The first, from 2016, [Consistent Hashing with Bounded Loads](https://research.googleblog.com/2017/04/consistent-hashing-with-bounded-loads.html). As the keys are distributed across servers, the load is checked and a node is skipped if it’s too heavily loaded already. There’s a detailed post detailing how it was added to [HAProxy at Vimeo](https://medium.com/vimeo-engineering-blog/improving-load-balancing-with-a-new-consistent-hashing-algorithm-9f1bd75709ed), (with a cameo by Yours Truly :). It’s also available as a [standalone package](https://github.com/buraksezer/consistent)
    3.  For clients in a choosing which set of backends to connect to, Google’s [SRE Book](https://landing.google.com/sre/book.html) outlines an algorithm called “deterministic subsetting”. For full details, see the description in chapter 20, “[Load Balancing in the Datacenter](https://landing.google.com/sre/book/chapters/load-balancing-datacenter.html)”. I have a quick implementation at [github.com/dgryski/go-subset](https://github.com/dgryski/go-subset)
    4.  Load balancing is a huge topic and could easily be its own book. For two overviews, see
        1.  [Load Balancing Is Impossible](https://www.youtube.com/watch?v=kpvbOzHUakA) by Tyler McMullen
        2.  [Predictive Load-Balancing: Unfair But Faster & More Robust](https://www.youtube.com/watch?v=6NdxUY1La2I) by Steve Gury



public class ConsistentHash<T> {

 private final HashFunction hashFunction;
 private final int numberOfReplicas;
 private final SortedMap<Integer, T> circle =
 new TreeMap<Integer, T>();

 public ConsistentHash(HashFunction hashFunction,
 int numberOfReplicas, Collection<T> nodes) {

 this.hashFunction = hashFunction;
 this.numberOfReplicas = numberOfReplicas;

 for (T node : nodes) {
 add(node);
 }
 }

 public void add(T node) {
 for (int i = 0; i < numberOfReplicas; i++) {
 circle.put(hashFunction.hash(node.toString() + i),
 node);
 }
 }

 public void remove(T node) {
 for (int i = 0; i < numberOfReplicas; i++) {
 circle.remove(hashFunction.hash(node.toString() + i));
 }
 }

 public T get(Object key) {
 if (circle.isEmpty()) {
 return null;
 }
 int hash = hashFunction.hash(key);
 if (!circle.containsKey(hash)) {
 SortedMap<Integer, T> tailMap =
 circle.tailMap(hash);
 hash = tailMap.isEmpty() ?
 circle.firstKey() : tailMap.firstKey();
 }
 return circle.get(hash);
 }

}

----

- Date: 2019-01-03
- Tags: #Interview/System-Design 



