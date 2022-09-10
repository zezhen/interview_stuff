# Query Ads Relevance
----

[The Role of Relevance in Sponsored Search](https://iarapakis.github.io/papers/CIKM16.pdf): CIKM 2016

1.  query and ad relevance is modeled using a Gradient Boosted Decision Tree (GBDT).
2.  The features are text based and are extracted from query and ad title, ad description and ad display URL.
    *   185 text-based features 3 what we call ClickSim features.
    *   The 185 text-based features mainly consist of the following feature groups
        *   common counts
        *   Jaccard similarity of unigrams, bigrams, q-grams2 between query and each ad component (i.e., title, description and display URL);
        *   TF-IDF,
        *   BM25
        *   LSI
3.  use cases
    1.  pre-filtering of irrelevance of ads (AQF)
    2.  recovering ads with little history
        1.  above two are in prod
    3.  improving clkb prediction: too many features in clkb model, one more feature didn’t make a difference
    4.  re-ranking of ads on final search results: didn’t improve RPM


ClickSim: [Learning Query and Document Relevance from a Web-scale Click Graph](http://www.yichang-cs.com/yahoo/SIGIR16_clickgraph.pdf): SIGIR 2016

[Scalable Semantic Matching of Queries to Ads in Sponsored Search Advertising](https://astro.temple.edu/~tuc17157/pdfs/grbovic2016sigir.pdf): SIGIR 2016

[Context- and Content-aware Embeddings for Query Rewriting in Sponsored Search](https://astro.temple.edu/~tuc17157/pdfs/grbovic2015sigir.pdf): SIGIR 2015

A survey on session detection methods in query logs and a proposal for future evaluation. Inf. Sci. 2009

LSI: Indexing by latent semantic analysis. 1990

----

- Date: 2019-04-12
- Tags: #Interview/Gemini 



