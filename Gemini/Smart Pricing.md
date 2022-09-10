# Smart Pricing
----


==Gemini Traffic Quality Based Pricing==

Traffic Quality is measure by CPA?

![[Archive/工作资料/Gemini/_resources/Smart_Pricing.resources/unknown_filename.png]]

![[Archive/工作资料/Gemini/_resources/Smart_Pricing.resources/unknown_filename.1.png]]


1.  Consider Each Ads Separately
    1.  CVR = conversions / clicks
    2.  Ad level ratio of CVR  = CVR\_publisher / CVR\_Yahoo
2.  Combine separated ratio into one
    1.  Weighted Average: [Inverse variance weighting](https://en.wikipedia.org/wiki/Inverse-variance_weighting)
    2.  Given a sequence of independent observations yi with variances σi2, the inverse-variance weighted average is given by
    3.  ![[Archive/工作资料/Gemini/_resources/Smart_Pricing.resources/unknown_filename.2.svg]]
3.  Generate the final Pricing Tables at 4 levels from the most to the least granular:
    1.  Level 1) Device \* Section \* Query \* Advertiser
    2.  Level 2) Device \* Section \* Query
    3.  Level 3) Device \* Section \* Advertiser
    4.  Level 4) Device \* Section
4.  V9 workflow as below graph, V10 add campaign dimension.


![[SearchSmartPricingModelWorkflow__20170118__V9.pdf]]
[Comparison of Two Meta-Analysis Methods: Inverse-Variance-Weighted Average and Weighted Sum of Z-Scores](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5287121/)

Reference

1.  [Lift-Based Bidding in Ad Selection](https://arxiv.org/abs/1507.04811) AAAI 2016. Proposed by Jian Xu in DSP, ranking ads by CTR lift rather than ecpm, experiment but didn’t push to production due to revenue concern.



----

- Date: 2019-03-20
- Tags: #Interview/Gemini 



