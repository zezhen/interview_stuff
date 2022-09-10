# ML Interview Preparation 2019
----

This is the note when preparing ML engineer interview before leaving Yahoo

[machine-learning-interview-questions on github](https://github.com/Sroy20/machine-learning-interview-questions)

[[Facebook NewsFeed Ranking|Facebook NewsFeed Ranking]]


Algorithm and Theory
![[Archive/Machine Learning/_resources/ML_Interview_Preparation_2019.resources/unknown_filename.png]]

1.  When to use machine learning?
    1.  A machine learning problem consist of three things:
        1.  There exist a pattern.
        2.  You cannot solve it mathematically (even by writing exponential equations).
        3.  You have data on it.
2.  Dataset 
    1.  How would you handle an imbalanced dataset?
        1.  Collect more data if possible
        2.  Change the performance metric
            1.  accuracy won’t be a good metric on skewed dataset,  
                1.  e.g. Cancer classification problem, only 0.5% of patients has cancer (y=1), 99.5% don’t (y=0)
                2.  we can predict all are y=0, the accuracy is 99.5%
            2.  we should use Sensitivity (True Positive Rate), Specificity (True Negative Rate) and F1-score
        3.  Try Resampling the dataset
            1.  over-sampling: sampling with replacement, add copies of instances from the under-represented class
            2.  under-sampling: delete instances from the over-represented class
        4.  Try generate synthetic samples
            1.  e.g. randomly sample the attributes from instances in the minority class, SMOTE algorithm.
        5.  Try Different Algorithms, Penalized Models, …
    2.  If you got very less training data, how to build model based on that?
        1.  Pre-trained models
        2.  better algorithm
        3.  get more data
            1.  data augmentation
            2.  get started with generating the data
            3.  download from internet
    3.  How to handle missing data if there is a lot.
        1.  Assign a unique category to missing values, who knows the missing values might decipher some trend
        2.  We can remove them blatantly.
        3.  Or, we can sensibly check their distribution with the target variable, and if found any pattern we’ll keep those missing values and assign them a new category while removing others.
        4.  or use [Random Forest](https://www.youtube.com/watch?v=nyxTdL_4Q-Q)
    4.  Dimension Reduction
        1.  multicollinearity
            1.  To check multicollinearity, we can create a correlation matrix to identify & remove variables having correlation above 75% (deciding a threshold is subjective). In addition, we can use calculate VIF (variance inflation factor) to check the presence of multicollinearity. VIF value <= 4 suggests no multicollinearity whereas a value of >= 10 implies serious multicollinearity. Also, we can use tolerance as an indicator of multicollinearity.
            2.  But, removing correlated variables might lead to loss of information. In order to retain those variables, we can use penalized regression models like ridge or lasso regression. Also, we can add some random noise in correlated variable so that the variables become different from each other. But, adding noise might affect the prediction accuracy, hence this approach should be carefully used.
        2.  separate the numerical and categorical variables and remove the correlated variables. 
            1.  For numerical variables, we’ll use [[correlation.md|correlation]]. 
            2.  For categorical variables, we’ll use [chi-square test](https://en.wikipedia.org/wiki/Chi-squared_test) ([video](https://www.khanacademy.org/math/statistics-probability/inference-categorical-data-chi-square-tests/chi-square-goodness-of-fit-tests/v/pearson-s-chi-square-test-goodness-of-fit))
            3.  we can use ANCOVA (analysis of covariance) technique to capture association between continuous and categorical variables.
        3.  use PCA and pick the components which can explain the maximum variance in the data set.
            1.  ![[Archive/Machine Learning/_resources/ML_Interview_Preparation_2019.resources/unknown_filename.2.png]]
            2.  ![[Archive/Machine Learning/_resources/ML_Interview_Preparation_2019.resources/unknown_filename.3.png]]
            3.  ![[Archive/Machine Learning/_resources/ML_Interview_Preparation_2019.resources/unknown_filename.4.png]]
            4.  Rotation (orthogonal) is necessary because it maximizes the difference between variance captured by the component.For PCA, we aim to select fewer components (than features) which can explain the maximum variance in the data set.
            5.  Before run PCA, it’s better to remove correlated variables first, otherwise PCA might put more importance on those variable
        4.  sample a dataset and use GBDT to train, select the top k important features
    5.  Important Variables Selection
        1.  Remove the correlated variables prior to selecting important variables
        2.  Use linear regression and select variables based on p values
        3.  Use Forward Selection, Backward Selection, Stepwise Selection
        4.  Use Random Forest, Xgboost and plot variable importance chart
        5.  Use Lasso Regression
        6.  Measure information gain for the available set of features and select top n features according
    6.  [Label Encoder vs One-Hot Encoder](https://medium.com/@contactsunny/label-encoder-vs-one-hot-encoder-in-machine-learning-3fc273365621)
        1.  For the country feature, in label encoder, different numbers in one column, like \[0,1,2,3,4,5,…\], 0 maybe France, 1 maybe Spain, etc, the problem is that the model will misunderstand the data to be in some kind of order, 0 < 1 < 2
            1.  from sklearn.preprocessing import LabelEncoder
            2.  labelencoder = LabelEncoder()
            3.  x\[:, 0\] = labelencoder.fit\_transform(x\[:, 0\])
        2.  One hot encoder, splits the categorical column into multiple columns, numbers are replaced by 1s and 0s, depending on which column has what value.
            1.  from sklearn.preprocessing import OneHotEncoder
            2.  onehotencoder = OneHotEncoder(categorical\_features = \[0\])
            3.  x = onehotencoder.fit\_transform(x).toarray()
    7.  Feature Scaling: make sure features are on a similar scale.
        1.  xi  = (xi - x\_avg) / range => -1 <= xi <= 1
        2.  ![[Archive/Machine Learning/_resources/ML_Interview_Preparation_2019.resources/unknown_filename.5.gif]]
3.  Model Training Analysis
    1.  Trade-off between bias and variance?
        1.  The inability for a ML method to capture the true relationship is called Bias
            1.  models with low bias are usually complex.
            2.  high bias models are simple
        2.  The different fits between datasets is called variance.
            1.  High variance method maybe represent training set well but are at risk of overfitting to noisy or unrepresentative training data.
            2.  Low variance usually produce simpler model and underfit the training data.
    2.  How do you ensure you’re not overfitting with a model? (low bias but high variance => Overfit)
        1.  Keep the model simpler: reduce variance by taking into account fewer variables and parameters, thereby removing some of the noise in the training data.
        2.  Use cross-validation techniques such as k-folds cross-validation.
        3.  Use regularization techniques such as LASSO that penalize certain model parameters if they’re likely to cause overfitting.
    3.  How a ROC curve works? => [[ML Basic.md|ML Basic]]
4.  Model Comparison
    1.  Classification vs Regression
        1.  Classification is the task of predicting a discrete class label.
        2.  Regression is the task of predicting a continuous quantity.
    2.  Decision Tree vs Logistic Regression
        1.  Decision Boundaries
            1.  LR search for a single linear decision boundary in the feature space
            2.  DT decision boundaries are parallel to the axes, chop up the feature space into rectangles 
        2.  Which is preferable?
            1.  Logistic regression will work better if there's a single decision boundary, not necessarily parallel to the axis.
            2.  Decision trees can be applied to situations where there's not just one underlying decision boundary, but many, and will work best if the class labels roughly lie in hyper-rectangular regions.
        3.  Complexity
            1.  Logistic regression is intrinsically simple, it has low variance and so is less prone to over-fitting. 
            2.  Decision trees can be scaled up to be very complex, are are more liable to over-fit. Pruning is applied to avoid this.
        4.  Questions:
            1.  decision boundary seems work for classification, rather than regression?
            2.  why not compare decision tree vs linear classification? 
            3.  regression will fit the curve to the data, like data subject to data linearity, while classification is to find a boundary to separate the data
    3.  GBDT vs Random Forest (Boosting vs Bagging)
        1.  Bagging algorithms divides a data set into subsets made with repeated randomized sampling. Then, these samples are used to generate  a set of models using a single learning algorithm. Later, the model predictions are combined using voting (classification) or averaging (regression). 
            1.  Bagging, e.g. RF, use fully grown devision trees (low bias, high variance), which are prone to overfitting, in order to achieve high accuracy, create a large number of trees(classifier) based on [bagging](https://en.wikipedia.org/wiki/Bootstrap_aggregating), different trees overfit the data in different way, and through voting to average out the difference.
            2.  RF grows trees in parallel, each tree is independently from the rest.
            3.  RF has very less parameters to tune, e.g. tree numbers (the more the better), how many data in leaf (default is 1, can increase a bit to get smaller tree)
        2.  In boosting, after the first round of predictions, the algorithm weighs misclassified predictions higher, such that they can be corrected in the succeeding round. This sequential process of giving higher weights to misclassified predictions continue until a stopping criterion is reached.
            1.  Boosting is based on weak classifier (high bias, low variance), e.g. shallow tree, the next tree is trained to improve the already trained ensemble.
            2.  Boosting is sequential
            3.  GBT has many parameters to tune, 
        3.  Referece
            1.  https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80
        4.  Decision Tree Algorithms
            1.  CART
            2.  C4.5
    4.  Decision Tree vs Neural Network
        1.  Decision Trees
            1.  Should be faster once trained (although both algorithms can train slowly depending on exact algorithm and the amount/dimensionality of the data). This is because a decision tree inherently "throws away" the input features that it doesn't find useful, whereas a neural net will use them all unless you do some feature selection as a pre-processing step.
            2.  If it is important to understand what the model is doing, the trees are very interpretable.
            3.  Only model functions which are axis-parallel splits of the data, which may not be the case.
            4.  You probably want to be sure to prune the tree to avoid over-fitting.
        2.  Neural Nets
            1.  Slower (both for training and classification), and less interpretable.
            2.  If your data arrives in a stream, you can do incremental updates with stochastic gradient descent (unlike decision trees, which use inherently batch-learning algorithms).
            3.  Can model more arbitrary functions (nonlinear interactions, etc.) and therefore might be more accurate, provided there is enough training data. But it can be prone to over-fitting as well.
    5.  KNN vs K-means clustering
        1.  KNN is supervised, it tries to classify an unlabeled observation based on its k surrounding neighbors, can be used as classification or regression algorithm.
        2.  K-means is unsupervised, it partitions a data set into clusters such that a cluster formed is homogeneous and the points in each cluster are close to each other.
    6.  [Ensemble Learning](https://en.wikipedia.org/wiki/Ensemble_learning)
        1.  ensemble learners are based on the idea of combining weak learners to create strong learners. But, these learners provide superior result when the combined models are uncorrelated.
        2.  [Ensemble Methods](https://medium.com/@aravanshad/ensemble-methods-95533944783f)
5.  Advanced
    1.  Difference between ==L1== (Lasso regression) and ==L2== (Ridge regureesion) regularization
        1.  L2 regularization tends to spread error among all the terms, while L1 is more binary/sparse, with many variables either being assigned a 1 or 0 in weighting. L1 corresponds to setting a Laplacean prior on the terms, while L2 corresponds to a Gaussian prior.
        2.   L1 regularization helps perform feature selection in sparse feature spaces, and that is a good practical reason to use L1 in some situations.
        3.  Computational difficulty: L2 > L1
        4.  Sparsity: L1 > L2
        5.  https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/
        6.  ![[Archive/Machine Learning/_resources/ML_Interview_Preparation_2019.resources/unknown_filename.1.png]]
    2.  How is a decision tree pruned? => [Pruning (decision trees)](https://en.wikipedia.org/wiki/Pruning_%28decision_trees%29)
        1.  Pruning is what happens in decision trees when branches that have weak predictive power are removed in order to reduce the complexity of the model and increase the predictive accuracy of a decision tree model. Pruning can happen bottom-up and top-down, with approaches such as reduced error pruning and cost complexity pruning.
        2.  Reduced error pruning is perhaps the simplest version: replace each node. If it doesn’t decrease predictive accuracy, keep it pruned. While simple, this heuristic actually comes pretty close to an approach that would optimize for maximum accuracy.


Courses

*   [ML Courses by Andrew Ng](https://www.youtube.com/watch?v=r3uBEDCqIN0&index=71&list=PLZ9qNFMHZ-A4rycgrgOYma6zxF4BZGGPW)



----

- Date: 2019-01-22
- Tags: #machineLearning #Interview 



