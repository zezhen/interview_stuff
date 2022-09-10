# DSP
----

![[Archive/工作资料/Gemini/_resources/DSP.resources/unknown_filename.jpeg]]

Workflow:

1.  User -> SSP —bid request—> Bid Server (Gateway)
2.  BidServer 300+ per colo
    1.  SSP requests => uniform request
        1.  one DSP will subscribe multiple SSPs, vice versa, which might have different formats
        2.  e.g. Adx from Google wrap openRTB data in protobuf format, some others are using json format
    2.  QPS Throttling (reduced QPS to 10k-15k per bid server)
    3.  Traffic Protection
    4.  pull user profile from profile server, send user and publisher profile, etc to Optimizer Server (OptServer or Adserver)
        1.  via RPC call, data encoded in protobuf format
    5.  ...
3.  OptServer 400+ per colo
    1.  Indexing
        1.  Entity: campaign, ads, advertiser, etc
            1.  data is built in inverted index in MEM for quick retrieval, e.g. segments, ads/section size, location, etc
        2.  Parse perf: for various models.
    2.  Targeting
        1.  user segments, 70+ various publisher filters
    3.  Auction: click/conversion model => Junwei
4.  Meta Data
    1.  domain model is stored in mysql, each record is attached with a version (mysql provided table level global incremental version)
    2.  one “Dist” host periodically query mysql table to get the data with forward version then local version.
        1.  need to scan whole table, it’s ok due to limited data size
        2.  why only one “Dist”? some bottleneck in mysql end.
    3.  all other 10+ slave hosts read data from this “Dist” and served as the cache for BidServer and OptServer
5.  Control Server
    1.  5 min batch update delivery rate for all ads/lines
    2.  users’ impression/click events => Kafka => Storm => Control Server
6.  Presentation
    1.  BidServer only return a url to SSP, if it wins, SSP or User call presentation to show the ad
    2.  Presentation logging the impression events 0.7% of serve events.




----

- Date: 2019-05-15
- Tags: #Interview/Gemini 



