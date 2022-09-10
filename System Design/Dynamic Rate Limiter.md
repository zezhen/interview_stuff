# Dynamic Rate Limiter
----


On Friday, 02/08, I had a discussion with colleagues about how to implement the rate limiter, this is also one Apple onsite interview question. There are two implementation ways:

1.  Put requests into a limited size queue, if the queue is full, then the server will decline the new coming requests. Working threads pick requests from queue to process, once the queue have more space, new requests can be accepted.
2.  Set a sliding window with limited QPS rate, each slot in the window hold the request number arrive in this slot time, the granularity can be 1 ms, when the total request in this window exceed the limit, then server decline all the coming request. The sliding window move as time move, once the new slot available, new requests can be accepted.


There are some pros and cons of both implementations, (do the comparison later), but here we want to talk about some other strategy.


1.  Stack implementation: LIFO
    1.  The reason is that if the working threads somehow meet problems and delay to process requests as above, the new coming requests will be accepted but might be wait timeout in the queue, or even they’re finally picked and processed successfully, the clients might already timeout, which caused ‘wasting computation’. In this case, if the logic support, anyway we will ‘fail’ to process the request, we can choose the latest requests, rather than the ‘already waited’ requests.
2.  Dynamic Limit
    1.  The problem of all implementations is that the limit number is fixed, the number is usually come from profiling, experience, or etc, but it’s not accurate all the time, it might be correct at beginning, but after the servers running for a while, their performance might be declined, or we add new functions on this servers, which might has different performance requirements, thus a dynamic way is necessary.
    2.  We can do it in two ways: Vertical or Horizontal
        1.  Vertical means server capacity, e.g. CPU/Core/Virtual Node, Memory, IO, etc. in current modern server, memory and IO should not be a problem, we can focus on CPU.
            1.  Some server might has 4 CPU, 8 Core and 16 virtual node, which means their concurrency can reach to 16, if they serve light request with 16 threads, it should work fine.
            2.  but some request or processing in server need multi-threads, depends on the implementation, it needs a lot of waiting/blocking/switch between threads with in one virtual node, so it’s better to have one core or even one CPU to process these requests, which would decrease the latency for this requests.
            3.  Another scenarios is DB, if multiple requests access same DB, which might have to wait on the lock, reduce request concurrency will help accelerate request processing time.
            4.  
        2.  Horizontal means waiting queue size or sliding window limit, we can easily enlarge or shrink it to scale out the server request accept capacity 
            1.  Large accept capacity is good if there is no process SLA for clients, server can guarantee all the requests can be processed eventually
            2.  But if clients are waiting, blindly enlarge the queue/limit size but no SLA guaranteed will cause lots of socket timeout, the services won’t be trustable, what’s more there will be ‘wasting computation’ issue as well
            3.  If the queue/limit size is too small, we will decline too many requests but the servers are idle, which waste the power of computation.
    3.  How to dynamic tune the limit?
        1.  First of all, server need to know when need to tune the limit, and how? So we need to define the service quality, here we simply choose latency to measure the quality.
        2.  Processing latency per request matters to Vertical, which means how much time to process the request, we can choose an average latency in past period, if server (coordinator process) detected that the average processing latency increase, which might because of too many requests are causing conflicts on whatever CPU computation resource, Memory resource or DB resource, etc, server can try to decrease the concurrency to see whether it could reduce the latency. Of course, we can set a range \[min\_nthread, max\_nthread\] to guarantee there won’t be too less concurrency.
            1.  How to choose a comfortable number? We can follow the TCP/IP rules, when server start and it can enter the warm up stage, the server start with min\_nthread threads, if latency is good and it tries to increase the threads until reach the max\_nthread. 
            2.  If somehow the latency increase, server can decrease the nthread accordingly
            3.  if the coming requests is stable and the concurrency threads threshold would eventually converge to a number.
        3.  Waiting Time (latency) in the queue per request matters to Horizontal, no matter which kinds of implementations, FIFO queue, LIFO queue or sliding windows (some queue mechanism as well), higher limit will cause higher latency, while lower limit will have lower latency regardless of the declined requests. Therefore, server can do similar as vertical, start from minimum size of queue, monitor the average waiting latency in past period, enlarge or shrink the queue accordingly.



----

- Date: 2019-02-10
- Tags: #Interview/System-Design 



