# Keyword Matching
----


Some Concepts in Curveball

1.  Match type vs Matching
    1.  Match types, like exact, phrase or broad are what advertisers’ ask, how they want users’ query match with their keywords.
        1.  Exact match type means the query should be exact same as the keyword advertisers specified
        2.  Phrase match type, a.k.a. consecutive sub-query match type, which means a consecutive subquery is exact same as the keyword.
        3.  Broad match type allow arbitrary queries to match with the keyword with some level similarity.
    2.  Matching, like exact, phrase, broad are how algorithms do the match in runtime, like the matching results in subword2vec is borad matching.
        1.  Exact matching can match the query with the ads with all match types, including exact, phrase and broad match types
        2.  Phrase matching can match the query with the ads with phrase or broad match types
        3.  Broad matching can only match the query with the ads with broad match types.
2.  Canonicalization
    1.  The users’ queries might be various and arbitrary, like wrong spelling, using additional spaces or vice verse, using abbreviation, etc, the keywords advertisers uploaded are better but not all are in same format, so it’s necessary for us to transform the queries and keywords into some unified format, which is known as canonicalization.
    2.  The core of canonicalization [library](https://git.ouroath.com/QNS/QNS_Gemini) is data tables, which are phrases to canonicalized phrase lookup tables, the canonicalization or transformation has below types:
        1.  StopWordRemoval, e.g. http, www, in, at, etc
        2.  Stemming: e.g. past/future tense to present tense, plural to singular, etc
        3.  PhraseSwapper: add/remove space between words, location/airport/airline abbreviation transformation, word reorder, etc
    3.  How to find the transformation relationship in the data tables?
        
        1.  The main idea is based on co-click, which is multiple users search various queries but the click on same url, if the concurrency is above some threshold, we can confirm that these queries are similar semantically, then we extract similar phrases from such query groups.
        2.  Based on the relationship between the phrase p and canonicalized phrase p', we get three kind of query/keyword canonicalization:
        
        1.  exact canon: there is no much difference between p and p’ literally, transformation like one hundred to 100, ca to California, spelling correction, etc
        2.  variant canon: mainly the plural to singular transformation, split or join words with space, re-order some words, etc
        3.  broad canon: some transformation that change words but same means semantically, e.g. pictures to photo, child to kid
        
3.  x.


Keyword and Ads Meta Data

1.  In Curveball, there are multiple layers from advertiser to keywords.
    1.  One adverser can have multiple campaigns, one campaign will have multiple adgroup
    2.  Each adgroup has various keywords, each keyword is a bidterm and have bidterm id, thus multiple bidterm can share same keyword text.
    3.  There are one or more ad creatives under each adgroup, in runtime ad creatives are selected randomly once one keyword is match.
2.  Some other settings
    1.  budget is set on advertiser and campaign level.
    2.  bid price is set on keyword, adgroup or campaign level
    3.  negative keywords are set on advertiser level
3.  Data Storage ([[YCDB|YCDB]]: key value database)
    1.  bid term DB: key is the MUR hash value of bidterm text, value is a tuple including ad id, adgroup id,  campaign id, advertiser id, etc
    2.  ad creative DB: key is hash value of ad creative id, value is ad creative meta info, including title, description, whether active, etc
    3.  advertiser DB: key is hash value of adgroup id (avoid hotspot), value is advertiser/campaign meta information, including negative keywords list for advertiser, whether active, etc
    4.  ad extension DB: key is has value of advertiser id, value is various extensions, e.g. annotations
4.  Runtime Matching
    1.  Matching algorithms will prepare a bunch of bidterms and send to MatchBroker, which works like the scatter-gather
    2.  In first step, MB calls bidterm DB in parallel given the bidterms, and gets (ad, adgroup, campaign, advertiser) tuples
    3.  Then MB calls advertiser DB for activeness and negative keywords check and filtering
    4.  After that MB call ad creative and extension DB in parallel to get necessary information
    5.  At last, gather all data and filter the items if total amount exceeds the client ask, then return back to client.



Matching Algorithms


1.  Phrase Matching ([[Phrase Match|Phrase Match]]: another summary)
    1.  phrase generation: generate all candidates of subquery (phrase), except the one token is person name (judged by QLAS) 
    2.  phrase scoring
        1.  Model: GBDT
        2.  Features (300)
            1.  Len: LEN\_Q\_0\_LEN\_P\_0
            2.  Part of Speech: POS\_L\_P\_0\_S\_4, POS\_N\_Q\_8\_P\_1
                1.  Q/P: query and phrase
                2.  S/E: start or end words of phrase
                3.  L/R: left or right words of phrase
                4.  N: number of pos
            3.  QLAS: QLAS\_P\_BRAND\_EXACT
            4.  Query-Phrase Cosine Similarity
    3.  ad matching: l runtime matching in above section
    4.  ad selection
        1.  One option is to select the ads with top query-phrase score, that’s what we did since beginning, the hypothesis is that the high query phrase score means better quality of ads, potentially we could improve CTR and RPM accordingly.
            1.  That works well since beginning, while after multiple time’s improvement, the margin left for us to improve model itself is less and less. Is the hypothesis still working?
            2.  The final goal of our tuning is to improve RPM, so we could consider the bid as well and come out the option 2
        2.  Option 2 is to combine query-phrase score and ads bid together, then rank and select ads based the combination score: final\_score = bid \* ( 1 - ( 1 - similarity) ^ 2). Below chart show function of y=1-(1-x)^2 (blue line) and y=x (black line), transformed similarity with bid can consider both sides and allow ads with low similarity and high bid to be selected.
            1.  when query phrase similarity is low, transformed similarity dramatically increases along with similarity increasing, thus similarity dominates the final score.
            2.  when query phrase similar is high, transformed similarity is close to each other, bid will dominate the final scores.
        3.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.png]]
2.  Qbert Matching
    1.  In high level, it provides query rewrite for given user query. Query rewrite mainly comes from
        1.  Co-Session: Mods, Word2vec
        2.  Co-Click: Oscar, Hubble, Random Walk
        3.  Co-Bid: BeverlyHill
        4.  Click-LandingPage: Griffith
    2.  Mods
        1.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.1.png]]
        2.  data range can be day or session; generalizes MODS to also extract non-consecutive query pairs from user sessions     
    3.  Hubble
        1.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.2.png]]
    4.  Oscar
        1.  Uses the query-url graph instead of the query-ad graph
        2.  Edge strength between queries and urls in terms of clicks instead of COEC (edges with fewer clicks than a given threshold are pruned)                   
        3.  Given a query q0, produces a ranking of similar queries        
        4.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.3.png]]
    5.  Random Walk
        1.  [https://docs.google.com/presentation/d/1F28R2j3YzMQv3e6W2KQmpkjIF\_PqDmSIg43Y67RHU28/edit#slide=id.p23](https://docs.google.com/presentation/d/1F28R2j3YzMQv3e6W2KQmpkjIF_PqDmSIg43Y67RHU28/edit#slide=id.p23)
    6.  BeverlyHill
        1.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.5.png]]
    7.  Griffith
        1.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.4.png]]
    8.  Rewrite Scoring
        1.  GBDT model provides an unified quality measure for all query rewrite. [features](https://docs.google.com/spreadsheets/d/1zAsp2YYb94lUsUM9e7RmJcl_FqS3PnXf3utMiuw1jYE/edit#gid=1640184626)
3.  QuAd
    1.  In high level, it provide matching ads given user queries, it can expand from similar queries, similar ads, high frequency query to ads, etc
    2.  Remember Me:
        1.  It’s to retain high quality <query, ad> pairs, which has high historical click rates
        2.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.6.png]]
    3.  Reuse Qbert data to extend <query, ad> pair
    4.  Antares: ads recommendation using word2vec
4.  [Subword2Vec](https://drive.google.com/file/d/1G224ecsY_i8CLDk7qi9yLWKRhMWnJP9M/view?usp=sharing)
    1.  Before it, there are word2vec model already, which cover head queries, while tail query coverage isn’t high even we have already multiple algorithms.
    2.  In high level, it’s train a model using query’s uni-/bi-gram with ads in one session, and construct query’s vector from uni-/bi-gram to find nearest ads.
    3.  Offline:
        1.  collect user session data, including query, click url and ads, then break down query into uni-/bi-gram
        2.  use word2vec train and get 300 vectors for gram and ads vectors
        3.  clustering ads into 100 clusters by kmeans, upload to vespa
    4.  Online:
        1.  given the query, generate its normalized vectors from it’s uni-/bi-gram's vectors
        2.  search top 10 nearest ads clusters and retrieve nearest ads met special criterions, e.g. mat
5.  [VespaQueryRewrite](https://docs.google.com/presentation/d/1rkEuPUtlIBMxO6Tuii4SGC1TI_9YK6LM8o2ah0dV6o8/edit%23slide=id.p%0A)
    1.  In high level, its goal is to increase query-rewrite coverage for tail queries, it’s heavily based on [[QLAS|QLAS]] output, which contains multiple interpretations/modification, we can extract semantic similar rewrites from them and generate new candidates, then GBDT scoring these candidates and return the top ones.
    2.  Offline
        1.  _![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.7.png]]_
        2.  In Vespa, we keep keyword index with some meta data
        3.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.8.png]]
    3.  Online
        1.  Given the query and its QLAS features, we generate YQL for example query “pek airport car rental hours”, where “beijing airport”, “beijing capital airport” are parsed from QLAS interpretations.
            1.  select \* from sources \*
            2.  where
            3.   rank
            4.   (
            5.   rewrite contains equiv("pek airport", “beijing airport”, …, “beijing capital airport”))
            6.   and
            7.   rewrite contains phrase("car", "rental")
            8.   ),
            9.   rewrite contains "hour")
        2.  After we got matched keywords from Vespa, e.g. "beijing capital international airport car rental hours", "beijing capital airport car rental hours", "beijing airport car rental hours”, we can search-and-replace equivalent surface text to generate additional candidates.
        3.  Unified Rewrite Scoring
            1.  Use GBDT to scoring query and candidates, while the model will use some features from vespa, thus we need upload the data to vespa then scrape all necessary features for training.
            2.  200K query-rewrite pairs with score (Excellent=1.0, Good=0.8, Fair=0.5, Bad=0.0)
            3.  GBDT regression model: 100 trees, 10 nodes per tree
            4.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.9.png]]
            5.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.10.png]]
6.  [RNN Query Rewrite](https://docs.google.com/presentation/d/1TnpE_e1MKF1AEr1yQHxnT6epHTRurTseFh8CWHoW3uQ/edit#slide=id.p)
    1.  In high level, it uses Neural Machine Translation to rewrite user queries to increase coverage of user query matching to ads, no feature engineering needed.
    2.  Neural Machine Translation (NMT)
        1.  ![[Archive/工作资料/Gemini/_resources/Keyword_Matching.resources/unknown_filename.11.jpeg]]
        2.  Evaluation metric => [BLEU score](http://www.aclweb.org/anthology/P02-1040.pdf) + Editorial Judgement (Excellent/Good/Fair/Bad)
    3.  [Tranning](https://git.ouroath.com/Curveball/NeuralQueryRewrites/blob/master/train.py)
        1.  Data: 100M queries and rewrite pairs from Qbert, ~1M vocabulary after filter out low frequent words
        2.  Training: [tensorflow on spark](https://docs.google.com/presentation/d/1sToYYvD053JOkhD5SRy7zQxadQD5xELF-Sg9sPkGE8A/edit#slide=id.g1fcd10973c_0_131)
            1.  continuous training: Load model from previous checkpoint and start next round of training with new data
                1.  10M each, 1 epoch (~150000 steps), training time 22 hrs on 3 PS, 3 GPU, 4 CPU
            2.  apply learning rate decay by half each round, apply polynomial decay within one round.
        3.  Synchronous and Asynchronous Training
        4.  Model: Bidirectional RNN with LSTM cells, Beam Search with beam-width = 10
7.  






----

- Date: 2019-03-21
- Tags: #Interview/Gemini 



