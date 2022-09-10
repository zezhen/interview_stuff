# Search Engine
----

[Vespa](https://docs.vespa.ai/documentation/overview.html) vs [Solr](http://lucene.apache.org/solr/) vs [ElasticSearch](https://www.elastic.co/)

[Lucene](http://lucene.apache.org/) is a low level Java library (with ports to .NET, etc.) which implements indexing, analyzing, searching, etc. Solr and ElasticSearch are the pre-configured product/webapp which uses Lucene. A simple way to conceptualize the relationship between Solr/ElasticSearch and Lucene is that of a car and its engine.

1.  [Lucene简介和索引原理](https://blog.csdn.net/lfdns/article/details/78799238)
2.  [Realtime Search with Lucene](http://2010.berlinbuzzwords.de/sites/2010.berlinbuzzwords.de/files/busch_bbuzz2010.pdf)


[[ElasticSearch|ElasticSearch]]

1.  [Elasticsearch from the Bottom Up](https://www.elastic.co/videos/elasticsearch-from-the-bottom-up)
2.  [Anatomy of an Elasticsearch Cluster: Part I](https://blog.insightdatascience.com/anatomy-of-an-elasticsearch-cluster-part-i-7ac9a13b05db)
3.  [Anatomy of an Elasticsearch Cluster: Part II](https://blog.insightdatascience.com/anatomy-of-an-elasticsearch-cluster-part-ii-6db4e821b571)
4.  [Anatomy of an Elasticsearch Cluster: Part III](https://blog.insightdatascience.com/anatomy-of-an-elasticsearch-cluster-part-iii-8bb6ac84488d)


[[Vespa|Vespa]]

1.  Comparison vs Lucene
    1.  [Vespa vs Lucene: First Impressions @2017.06](https://opensourceconnections.com/blog/2017/10/06/vespa-vs-lucene-initial-impressions/)
    2.  [Comparison to ElasticSearch from vespa blog](https://docs.vespa.ai/documentation/elastic-search-comparison.html)
    3.  Support Tensor, seems better in ML


[Lucene Based: solr-vs-elasticsearch](https://logz.io/blog/solr-vs-elasticsearch/)

1.  Indexing and Searching
    1.  Data Source
    2.  Searching
    3.  Indexing
2.  Scalable and Distributed
    1.  Could and Distributed
    2.  Shard Splitting and Rebalancing

![[Archive/工作资料/Gemini/_resources/Search_Engine.resources/unknown_filename.png]]

1.  ElasticSearch is more popular among newer developers due to its ease of use. But if you are already used to working with Solr, stay with it because there is no specific advantage of migrating to ElasticSearch
2.  If you need it to handle analytical queries in addition to searching text, Elasticsearch is the better choice
3.  If you need distributed indexing, then you need to choose Elasticsearch. Elasticsearch is the better option for cloud and distributed environments that need good scalability and performance



----

- Date: 2018-10-06
- Tags: #Interview/Gemini 



