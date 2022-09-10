# Streaming
----

How to evaluate whether a distributed system is good or not, there are several principles as below we need to consider.


1.  Delivery Guarantees: Atleast-once,Atmost-once  ,Exactly-once
2.  Fault Tolerance: Failure(Node,Network), Recovery(Checkpoint)
3.  State Management
4.  Performance: Latency,Throughput,Scalability
5.  Advanced Features: Event Time Processing,Watermarks,Windowing
6.  Maturity



Checkpoint of Fault Tolerance 

==Flink==: ABS with ==Barriers== <= Lightweight Asynchronous Snapshots for Distributed Dataflows
    => Similar to Chandy-Lamport algorithm

![[Archive/面试资料/System Design/_resources/Streaming.resources/unknown_filename.png]]
\*[An introduction to snapshot algorithms in distributed computing](http://iopscience.iop.org/article/10.1088/0967-1846/2/4/005/pdf)


[Tyler Akidau](https://www.linkedin.com/in/takidau/): Google Senior Stuff, 不错的两篇文章
    [The world beyond batch: Streaming 101](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-101)
    [The world beyond batch: Streaming 102](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-102)



https://www.oreilly.com/ideas/questioning-the-lambda-architecture

1.  Lambda architecture
2.  Kappa architecture



----

- Date: 2018-08-09
- Tags: #Interview/System-Design 



