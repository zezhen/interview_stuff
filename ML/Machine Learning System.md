# Machine Learning System
----

Introduction

1.  [Square off: Machine learning libraries](https://www.oreilly.com/ideas/square-off-machine-learning-libraries%0A)
    1.  Supervised and unsupervised:
        1.  Spark MLlib, scikit-learn, H2O.ai, MMLSpark, Mahout
    2.  Deep learning
        1.  TensorFlow, PyTorch, Caffe2 (image), Keras, MXNet, CNTK, BigDL, MMLSpark (image and text), H2O.ai (via the deepwater plugin)
    3.  Recommendation system
        1.  Spark MLlib, H2O.ai (via the sparkling-water plugin), Mahout
2.  [2018 机器学习开源项目及框架](https://segmentfault.com/a/1190000017403332)
3.  [2018 30 Amazing Machine Learning Projects for the Past Year](https://medium.mybridge.co/30-amazing-machine-learning-projects-for-the-past-year-v-2018-b853b8621ac7)



* * *

1.  [[Scikit-Learn|Scikit-learn]]
2.  [Spark MLlib](https://spark.apache.org/mllib/)
3.  [vowpal\_wabbit](https://github.com/VowpalWabbit/vowpal_wabbit/wiki)
    1.  started from Yahoo Research and continuing at Microsoft Research to design a fast, scalable, useful learning algorithm.
    2.  Parallelization
        1.  The way vw distributes work consists of forming a [spanning tree](https://en.wikipedia.org/wiki/Spanning_tree) across the worker nodes.
    3.  Posts
        1.  [Vowpal Wabbit tutorial for the Uninitiated](https://www.zinkov.com/posts/2013-08-13-vowpal-tutorial/)
        2.  [VW on FastML](http://fastml.com/blog/categories/vw/)
4.  [Parameter Server](http://www.cs.cornell.edu/courses/cs6453/2017sp/slides/paramserver.pdf)
    1.  [An Architecture for Parallel Topic Models](http://vldb.org/pvldb/vldb2010/papers/R63.pdf). VLDB 2010 (1st generation)
        1.  used memcached for synchronization
    2.  [Parameter Server for Distributed Machine Learning](https://pdfs.semanticscholar.org/30e9/4e24d67994c5a8e2f20f852a51d28a720de2.pdf).WDSM 2012
    3.  [Large Scale Distributed Deep Networks](https://papers.nips.cc/paper/4687-large-scale-distributed-deep-networks.pdf). NIPS 2012,
    4.  [More Effective Distributed ML via a Stale Synchronous Parallel Parameter Server](https://papers.nips.cc/paper/4894-more-effective-distributed-ml-via-a-stale-synchronous-parallel-parameter-server.pdf). NIPS 2013
        1.  application specific parameter servers
    5.  [Communication Efficient Distributed Machine Learning with the Parameter Server.](https://www.cs.cmu.edu/~muli/file/parameter_server_nips14.pdf) NIPS 2014
    6.  [Scaling Distributed Machine Learning with the Parameter Server](https://www.cs.cmu.edu/~muli/file/parameter_server_osdi14.pdf). OSDI 2014
        1.  
    7.  [Distributed GraphLab: A Framework for Machine Learning and Data Mining in the Cloud](http://vldb.org/pvldb/vol5/p716_yuchenglow_vldb2012.pdf). PVLDB 2012
        1.  Uses coarse-grained snapshots for fault tolerance, impeding scalability
        2.  Doesn’t scale elastically like map-reduce frameworks
        3.  Asynchronous task scheduling is the main contribution
    8.  [Piccolo: Building Fast, Distributed Programs with Partitioned Tables](https://www.usenix.org/legacy/event/osdi10/tech/full_papers/Power.pdf). OSDI 2010.



----

- Date: 2019-04-12
- Tags: #machineLearning 



