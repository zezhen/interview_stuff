# Click Model
----



1.  [Mappi](https://docs.google.com/document/d/1COARbJFKy5yv57x6PsmR6uJh9aTSvjfyp71P1Bc6u60/edit#)
    1.  Algorithm
        1.  Logistic Regression
    2.  [Features](https://git.ouroath.com/Curveball/mappi/blob/master/src/main/scripts/config/inputconfig.json)
        1.  Time(10): e.g. hourofday, dayofweek, isweekend, etc
        2.  Supply(15): e.g. section, category, max\_downloads, min\_downloads, rating, vertical
        3.  Demand(33): e.g. adv, cmpgn, adg, ad, appId, demandMaxDownloads, demandRating, appStoreId, cmp\_ctr\_bin, etc
        4.  User (Mx3) (31): e.g. gender, age, country, city, device, os, 
        5.  App Category(1)
        6.  Mx3\_Install\_Propensity(6) : apps\_clk\_propensity\_10Bin, apps\_clk\_propensity\_50Bin, apps\_conv\_impr\_propensity\_100Bin, etc
            1.  refer to “[Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution)” in [[Probability and Statistics|Probability and Statistics]] to understand how to calculate propensity
        7.  Cross Features (187)
            1.  advertiser\_category (30)
            2.  campaign\_objective  (21)
            3.  site  (18)
            4.  os  (18)
            5.  country (17)
            6.  traffic\_type    (15)
            7.  section (14)
            8.  age (14)
            9.  gender  (11)
            10.  platform  (10)
            11.  section  (10)
            12.  ...
2.  Search Clkb
    1.  Algorithm: [Personalized Click Prediction in Sponsored Search](http://www.wsdm-conference.org/2010/proceedings/docs/p351.pdf). WSDM 2010
        1.  Logistic Regression
    2.  Features
        1.  click feedback features
            1.  EC: expected click = sum of pClick
                1.  q\_ec, bt\_ec, crt\_ec, usr\_ec, q\_bt\_ec, ...
            2.  COEC: click on EC = sum(clicks) / EC
                1.  corresponding above EC
            3.  ![[cf_features.pig]]
        2.  Non-CF features
            1.  devicePosition
            2.  matchType
            3.  matchAlgo
            4.  sitelinks
            5.  textFeature         # text similarity of query, title, description, etc
            6.  userWoeidCity
            7.  dayOfWeekHourOfDay
            8.  dayOfWeekPartOfDay
            9.  query
            10.  domain
            11.  creativeId/biddedtermid/adgid/cmpgn/advertiser/etc
            12.  ![[noncf_features.pig]]
        3.  Cross Features
            1.  lots of EC vs COEC conjunctions
            2.  ![[conjunctions.conf]]
3.  Native
    1.  Algorithm
        1.  https://docs.google.com/presentation/d/1R8vBeFvbP5OZkcPKa1c277pDawTNC31juLPc0TGkhao/edit#slide=id.p
        2.  Offset (refer to [[Factorization|Factorization]])
    2.  Features
        1.  Features: 12, Conjunction Pairs: 66, Total Size : 954
        2.  e.g. feature day has 10 embeddings, mappi has 7 embeddings, they has 15 conjunctions (which should be also embeded)
        3.  ![[Archive/工作资料/Gemini/_resources/Click_Model.resources/unknown_filename.png]]
4.  Gemini X
    1.  [Introduction](https://drive.google.com/open?id=1eabfYrdV-V9z87GoELbLXfMB2MnylJawXPA50e8h8K4)




----

- Date: 2019-02-05
- Tags: #Interview/Gemini 



