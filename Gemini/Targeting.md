# Targeting
----

Audience

1.  Custom Audiences:
    1.  Device IDs: Apple IDFA or Google IDs, advertisers can upload a whitelist for different types.
    2.  Conversion Rule: advertisers use conversion pixels to create audiences for future LAL Modeling
2.  Yahoo Audiences:
    1.  Search Retargeting: serve display/video/native ads to people who have searched for specific keywords (advertisers uploaded)
    2.  Email Domain: serve display/video/native ads to people who received emails from specific domains (advertisers uploaded)
    3.  Email Purchase Receipt: server ads based on purchase confirmation emails in several categories
        1.  Entertainment - Live Events
        2.  Entertainment - Movie Theater Tickets
        3.  Invoices and Statements
        4.  Products
        5.  Travel - Car
        6.  Travel - Flight
        7.  Travel - Hotel
3.  Lookalike (LAL) Audiences
4.  Composite Audiences: Yahoo Data, Yahoo Interest Categories, Third Party Data

|     |     |     |
| --- | --- | --- |
| Audience Type | Description (Details in Appendix Slides) | Data Source |
| Composite | Create an audience from multiple ingredient facts and audiences. | A combination of Yahoo data, customer data and third-party data |
| Device ID | Target Apple iPhone and Google Android device IDs from first party advertiser data | A list of customer device IDs that you provide |
| Dot Pixel/Conversion Rule | Yahoo’s universal, cross-platform pixel for retargeting and conversion tracking | First party data tracked using Dot tags you create on the [Pixels](https://developer.yahoo.com/brightroll/dsp/docs/advertisers/pixels/) page<br> |
| Third Party (3P) | Third party audiences are imported using our DataX API.<br> | First and Third Party Data |
| Email Address | Target first party advertiser Email addresses uploaded that BrightRoll DSP anonymizes and matches to Yahoo user profiles | Users who have used their email address to create a Yahoo account directly or as an alternate email address to create a Yahoo account |
| Lookalike | People who have similar interests and behaviors as those of your existing audiences. An automated process that analyzes user attributes to find similar people for audience extension use cases | Combination of advertiser and yahoo data. |
| Mail Domain | Yahoo Mail users who received emails from specific domains | Yahoo Mail |
| POI Location | Create an audience based on offline store/Point of Interest visitation | Flurry, Yahoo Apps / O&O, Mapping Services (Infogroup, Here) |
| Purchase Receipt | Yahoo Mail users who have received email indicating that they have completed a purchase or payment | Yahoo Mail |
| Search Keyword RT | Yahoo Search users who searched for specific keywords | Yahoo Search |
| YICs / MICs | Yahoo & Mobile Interest Categories segments are constructed by interpreting user activities across desktop and mobile devices, | Search queries, search clicks, page clicks and ad clicks on desktop, Mobile apps, Yahoo O&O content interests, Mail data |
| Verified Demo | Demographic models tuned towards third party verification providers (Nielsen / Comscore) | Yahoo Best Known Demo + Third Party Measurements |







![[Archive/工作资料/Gemini/_resources/Targeting.resources/unknown_filename.png]]


1.  Unicorn
    1.  Segment lifecycle management (activation, deactivation)
2.  Dragonite
    1.  Real time reach estimates for audience builder
3.  Device Graph
    1.  Deterministic and probabilistic mappings between devices and cookies. 650M+ clusters.
4.  App Graph
    1.  Mappings of devices and installed apps.
5.  ID Synch
    1.  Generate and store ID mappings for Supply and Data Partners. 80+ Data Partners, 50+ Supply Partners.
6.  Partner (PII) Match
    1.  Online to Offline matching using secure PII matching w ~9 trusted partners
7.  DMP UI
    1.  Tool for 3P Taxonomy administration (access control, pricing, processing status) for Data Ops and Partners.
8.  Audience Insights
    1.  Pre-sales tools for audience analysis powered by GUP data


![[Archive/工作资料/Gemini/_resources/Targeting.resources/unknown_filename.1.png]]


----

- Date: 2019-04-25
- Tags: #Interview/Gemini 



