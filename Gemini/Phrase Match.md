# Phrase Match
----

Phrase Match Understanding 
[https://docs.google.com/presentation/d/1mbjf0X2B1hymnxJj\_KTWO1nBBebwms8qaKPKkiTB9eM/edit#slide=id.g9cee41b7f\_0\_0](https://docs.google.com/presentation/d/1mbjf0X2B1hymnxJj_KTWO1nBBebwms8qaKPKkiTB9eM/edit#slide=id.g9cee41b7f_0_0)

Problem: Given a query Q = (w1 w2 w3 ...wn), generate most relevant phrases { (wi wi+1 wi+2  … wi+k) }
![[Archive/工作资料/Gemini/_resources/Phrase_Match.resources/unknown_filename.png]]

Offline Training: (P, Q, Label) + Online Serving: (P, Q)

Features:

1.  Term Importance: IDF, Click Feedback, Global weighting tree, …
2.  Syntactic Features: part of speech, noun phrase, length ratio
3.  Topic Phrase
    1.  Calculate importance score for a phrase based on the co-occurrence of phrases in query logs.
    2.  Calculate importance score for a phrase based on the share in one query
        *   line 8, the less share in one query, the higher t(p, q) will be.
    3.  Calculate importance score for a phrase based on variance in query logs
        *   line 10, the less variance, the less denominator, the higher m(p)
    4.  ![[Archive/工作资料/Gemini/_resources/Phrase_Match.resources/unknown_filename.1.png]]
4.  Brand
5.  Association Rules
6.  Semantic Featuers



\*Phrase Match by Srinath
https://docs.google.com/document/d/12tKWELTyzX5Uzj4ZwlgvLv8hsH8ZEEPkczDuiYpLFfk/edit

Here is summary of phrase match steps:
1\. Determine commercial intent of query
2\. Part Of Speech parsing of query
3\. Extract phrases for a given query (based on static file generated offline)
4\. Generate all possible phrase candidates
5\. For each candidate, generate features (Part Of Speech, IDF, Topic, Brand, IsQbertPhrase, Length)
6\. Finally score each candidate using GBDT model and select candidate if passes threshold

Knowledge Transfer
[https://docs.google.com/document/d/1rfz24esnBG-RnuQ1vZ3G7DVIaZ0\_XYpUpdN2RID\_BCE/edit](https://docs.google.com/document/d/1rfz24esnBG-RnuQ1vZ3G7DVIaZ0_XYpUpdN2RID_BCE/edit)

ClickText Similarity
[https://docs.google.com/document/d/1h1ASImgKNXuupDKEaDYcz9M\_bpmPNMIqoL6waMmlTNA/edit](https://docs.google.com/document/d/1h1ASImgKNXuupDKEaDYcz9M_bpmPNMIqoL6waMmlTNA/edit)



*   **GBDT**

[GBDT（MART） 迭代决策树入门教程](http://blog.csdn.net/w28971023/article/details/8240756)
    介绍Regression Decision Tree, Gradient Boosting, GBDT工作工作实例, 应用范围, 搜索引擎排序应用 RankNet

GBDT在phrase matching中的应用 [latest launch review - yinghua](https://docs.google.com/presentation/d/1r9V-DVnHOWFlGJc9JpbmxSIyPuvKiCAvU9lCmeiC72o/edit#slide=id.g29f9a4b833_0_7)
        https://git.ouroath.com/Curveball/VespaQueryRewrites/tree/master/gbdt-training
        https://git.ouroath.com/yingli/PhraseGbdt
    Boosting Decision Tree入门教程 http://www.schonlau.net/publication/05stata\_boosting.pdf
    LambdaMART 用于搜索排序入门教程 http://research.microsoft.com/pubs/132652/MSR-TR-2010-82.pdf



----

- Date: 2018-01-02
- Tags: #Interview/Gemini 



