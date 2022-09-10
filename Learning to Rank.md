# Learning to Rank
----

Start from [A Short Introduction to Learning to Rank](http://times.cs.uiuc.edu/course/598f14/l2r.pdf) 2011

1.  Difference from ordinal classification
    1.  In ranking, one cares more about accurate ordering of objects
    2.  In ordinal classification, one cares more about accurate ordered-categorization of objects, 
    3.  From loss function perspective, ranking care about the instance order error, using DCG, ordinal classification/regression care about predict value/score error, using square error
2.  Evaluation
    1.  [NDCG](https://en.wikipedia.org/wiki/Discounted_cumulative_gain) (Normalized Discounted Cumulative Gain)
        1.  CG (Cumulative Gain): the sum of the graded relevance values of all results in a search result list.
            1.  ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.7.svg]]
        2.  DCG (Discounted CG): highly relevant documents appearing lower in a search result list should be penalized as the graded relevance value is reduced logarithmically proportional to the position of the result.
            1.  ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.8.svg]]
        3.  NCDG (Normalized DCG): Search result lists vary in length depending on the query; 
            1.  IDCG (Ideal DCG): the DCG of the result list sorting by their relative relevance, which is maximum DCG of all permutation. 
            2.  ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.9.svg]], ![[unknown_filename.10.svg]]
    2.  [MAP](https://en.wikipedia.org/wiki/Evaluation_measures_(information_retrieval)#Mean_average_precision) (Mean Average Precision)
    3.  [Kendall's Tau](https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient)
3.  Ranking Types:
    1.  \*Point-wise Ranking(1): Ranking problem is transformed to classification, regression or ordinal classification.
    2.  \*\*Pair-wise Ranking(2): Ranking problem is transformed to pair-wise classification or regression
        *   ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.png]]
    3.  \*\*\*List-wise Ranking(3): It takes ranking lists as instances in both learning and prediction.
4.  Algorithms
    1.  \*RankProp: Rich Caruana, et al. Rankprop and Multitask Learning for Medical Risk Evaluation, 1996
        1.  a neural net ranking model, two phases
        2.  1) an MSE regression on the current target values, and an adjustment of the target values themselves to reflect the current ranking given by the net;
        3.  2) a mapping of the data to a large number of targets which reflect the desired ranking, which performs better than just regressing to the original, scaled rank values
    2.  \*\*Ranking SVM: Herbrich et al. Large margin rank boundaries for ordinal regression, 2000
        1.  learn a classifier for classifying the order of pairs of objects, as below, within one query result(group), we can transfer rank problem to Linear SVM
        2.  hinge loss: ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.3.png]]
            *   ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.1.png]]![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.2.png]]
    3.  \*[Prank](https://pdfs.semanticscholar.org/906f/50f545890ca81231be7cec7c59555c679dba.pdf)  Koby Crammer, Yoram Singer, Pranking with Ranking, 2002
        1.  Associate each ranking with distinct sub-interval of the reals, b1 <= b2 <= ... <= bk = infinity
        2.  using Perceptron Ranking like idea to compare the predicted y with all k-1 rank, then update the threshold w and b
            *   ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.4.png]]
    4.  \*[SVM for Ordinal Classification](https://pdfs.semanticscholar.org/99aa/142d6df2abb244dcdd64dea3655db4bb7020.pdf) Amnon Shashua, Anat Levin, Ranking with Large Margin Principle: Two Approaches. 2002
        1.  Inherit the idea from Prank, while using SVM to maximize the margins between multiple linear models (parallel hyperplanes)
        2.  key point need to understand here is the loss function
            *   ![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.5.png]]![[Archive/Machine Learning/_resources/Learning_to_Rank.resources/unknown_filename.6.png]]
    5.  \*Harrington E. Online ranking/collaborative filtering using Perceptron algorithm. 2003
    6.  \*\*[RankBoost](http://jmlr.csail.mit.edu/papers/volume4/freund03a/freund03a.pdf) 2003 An Efficient Boosting Algorithm for Combining Preferences
        1.  exponential loss
    7.  \*\*Dekel, [Log-Linear Models for Label Ranking](https://nlp.stanford.edu/pubs/dekel2004ranking.pdf), 2004
        1.  
    8.  \*\*[RankNet](https://icml.cc/2015/wp-content/uploads/2015/06/icml_ranking.pdf) 2005 Learning to Rank using Gradient Descent
        1.  gradient descent and neural network model, logistic loss
    9.  \*\*[IR SVM](http://www.bigdatalab.ac.cn/~junxu/publications/SIGIR2006_AdaptSVM.pdf) 2006: Adapting Ranking SVM to Document Retrieval
        1.  optimize "Ranking SVM" from 1) the top of the result list is crucial, 2) no bias towards the queries with large number of documents
    10.  \*[Subset Ranking](https://web.stanford.edu/group/mmds/slides/zhang-mmds.pdf) using Regression 2006
    11.  \*\*[LambdaRank](https://pdfs.semanticscholar.org/fc9a/e09f9ced555558fdf1e997c0a5411fb51f15.pdf) 2007
        1.  implicit cost functions to optimize directly the quality measures, neural network
    12.  \*\*[GBRank](https://pdfs.semanticscholar.org/8f8d/874a3f0217289ba317b1f6175ac3b6f73d70.pdf) 2007 A General Boosting Method and its Application to Learning Ranking Functions for Web Search
        1.  
    13.  \*\*\*[ListNet](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2007-40.pdf): 2007 From Pairwise Approach to Listwise Approach
        1.  introduce two probability models: permutation prob and top one prob to define listwise loss function, Neural Network and Gradient Descent
    14.  \*\*\*[AdaRank](http://www.bigdatalab.ac.cn/~junxu/publications/SIGIR2007_AdaRank.pdf): 2007 A Boosting Algorithm for Information Retrieval
        1.  minimize a loss function directly defined on the performance measures, boosting framework
    15.  \*\*\*[SVM MAP](https://www.cs.cornell.edu/people/tj/publications/yue_etal_07a.pdf): 2007 A Support Vector Method for Optimizing Average Precision
        1.  a general SVM learning algorithm that efficiently finds a globally optimal solution to a straightforward relaxation of MAP
    16.  \*\*\*[ListMLE](http://icml2008.cs.helsinki.fi/papers/167.pdf): 2008 Listwise Approach to Learning to Rank - Theory and Algorithm
        1.  proposes conducting theoretical analysis of learning to rank algorithms, analyze 3 loss functions: likelihood loss, cosine loss, and cross entropy loss
        2.  latter two were used in RankCosine and ListNet, likelihood loss => ListMLE
    17.  \*\*\*[SoftRank](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.469.3608&rep=rep1&type=pdf): 2008 Optimizing Non-Smooth Rank Metrics
        1.  a new family of training objectives that are derived from the rank distributions of documents, induced by smoothed scores.
    18.  \*[McRank](https://papers.nips.cc/paper/3270-mcrank-learning-to-rank-using-multiple-classification-and-gradient-boosting.pdf) 2008 Learning to Rank Using Multiple Classification and Gradient Boosting
        1.  using the Expected Relevance to convert class probabilities into ranking scores, gradient boosting tree
        2.  improve subset ranking and lambdaRank in DCG
    19.  \*\*[LambdaMART](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.157.5117&rep=rep1&type=pdf) 2010 Adapting Boosting for Information Retrieval Measures
        1.  combine boosted tree classification and LambdaRank
    20.  \*\*[From RankNet to LambdaRank to LambdaMART: An Overview](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.180.634&rep=rep1&type=pdf)  -- Christopher J.C. Burges
    21.  https://www.quora.com/What-is-the-intuitive-explanation-of-Learning-to-Rank-and-algorithms-like-RankNet-LambdaRank-and-LambdaMART-In-what-types-of-data-variables-can-these-techniques-be-used-What-are-their-strengths-and-limitations/answer/Nikhil-Dandekar
    22.  [Learning to Rank for Information Retrieval](http://didawikinf.di.unipi.it/lib/exe/fetch.php/magistraleinformatica/ir/ir13/1_-_learning_to_rank.pdf)
5.  Current and Future research directions
    1.  training data creation
    2.  semi-supervised learning and active learning
    3.  feature learning
    4.  scalable and efficient training
    5.  domain adaptation and multi-task learning
    6.  ranking by ensemble learning
    7.  global ranking
    8.  ranking of nodes in a graph



----

- Date: 2019-03-06
- Tags: #machineLearning 



