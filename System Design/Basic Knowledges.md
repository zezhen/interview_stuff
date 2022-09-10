# Basic Knowledges
----

1.  CPU and virtual cores
    1.  e.g. SoFE hosts has 4 CPU, each has 6 cores including logic threads, 2.4GHz
    2.  Concurrency: it depends on CPU # and cores #
2.  MEM
    1.  
3.  [Latency (~2012)](https://gist.github.com/jboner/2841832)
    1.  L1 cache reference ................................................ 0.5 ns
    2.  Branch mispredict .................................................... 5 ns
    3.  L2 cache reference ................................................... 7 ns
    4.  Mutex lock/unlock .................................................. 25 ns
    5.  Main memory reference ........................................ 100 ns 
    6.  Compress 1K bytes with Zippy ......................... 3,000 ns  =   3 µs
    7.  Send 2K bytes over 1 Gbps network .............. 20,000 ns  =  20 µs
    8.  SSD random read .......................................... 150,000 ns  = 150 µs
    9.  Read 1 MB sequentially from memory .......... 250,000 ns  = 250 µs
    10.  Round trip within same datacenter ............... 500,000 ns  = 0.5 ms
    11.  Read 1 MB sequentially from SSD\* …….... 1,000,000 ns  =   1 ms
    12.  Disk seek ................................................. 10,000,000 ns  =  10 ms
    13.  Read 1 MB sequentially from disk ........... 20,000,000 ns  =  20 ms
    14.  Send packet CA->Netherlands->CA ..... 150,000,000 ns  = 150 ms
    15.  
    16.  TCP connection: 3 handshake?
    17.  Server Process: processing logic complexity
    18.  Tips:
        
        1.  1K bytes is 16K bits
        2.  IO usually is not a problem for current modern hosts
        3.  Assuming ~1GB/sec SSD
        
    19.  Throughput
        1.  it depends on Latency and Concurrency, 100 concurrency + 1 ms latency can support 100k throughput.
        2.  e.g. Segment GDS has 24 cores (4 cpus), average latency ~1.5ms (request to response), thus GDS per host can support 16k QPS
    20.  


----

- Date: 2019-01-23
- Tags: #Interview/System-Design 



