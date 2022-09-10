# Scikit-Learn
----

A gold standard of classical ML library, it mainly covers below functions, refer detail to [here](https://scikit-learn.org/stable/). [Numpy](https://docs.scipy.org/doc/numpy-1.15.0/user/index.html) and [Pandas](http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html) are useful while using scikit-learn

1.  Preprocessing
2.  Dimensionality Reduction
3.  Model Selection
4.  Classification
5.  Regression
6.  Clustering


Tutorials:

1.  Supervised learning
    1.  Nearest neighbor and the curse of dimensionality
    2.  Linear model: Linear regression, Shrinkage, Sparsity, Classification
    3.  Support vector machines (SVMs): Linear SVMs, Kernels
2.  Model Selection
    1.  Cross-Validation: KFold, cross\_val\_score
    2.  Grid-search
3.  Unsupervised learning
    1.  Clustering: K-means, [vector quantization](https://en.wikipedia.org/wiki/Vector_quantization), Hierarchical agglomerative clustering, 
    2.  Decompositions: Principal component analysis (PCA), Independent Component Analysis (ICA)
4.  [Text Classifier](https://colab.research.google.com/drive/1t733jHB-_3tIetLpgXURTFEPypAXSk87#scrollTo=zJT_QAiKcb4q)
    1.  extension: [Multi-class/multi-label](https://scikit-learn.org/stable/modules/multiclass.html#multiclass), [Truncated SVD](https://scikit-learn.org/stable/modules/decomposition.html#lsa) for [latent semantic analysis](https://en.wikipedia.org/wiki/Latent_semantic_analysis), [Out-of-core Classification](https://scikit-learn.org/stable/auto_examples/applications/plot_out_of_core_classification.html#sphx-glr-auto-examples-applications-plot-out-of-core-classification-py) for out of memory data training, [Hashing Vectorizer](https://scikit-learn.org/stable/modules/feature_extraction.html#hashing-vectorizer) as a memory efficient alternative to [CountVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html#sklearn.feature_extraction.text.CountVectorizer)
5.  External Resources
    1.  [Tutorial: scikit-learn - Machine Learning in Python with Contributor Jake VanderPlas](https://www.youtube.com/watch?v=cHZONQ2-x7I)
    2.  ==Intro to scikit-learn (I), SciPy2013 Tutorial,== [Part 1](https://www.youtube.com/watch?time_continue=1886&v=r4bRUvvlaBw)==,== [Part 2](https://www.youtube.com/watch?v=hlaMiXCRxB0)==,== [Part 3](https://www.youtube.com/watch?v=XS4TIGe7MaU)




![[Archive/Machine Learning/_resources/Scikit-Learn.resources/unknown_filename.png]]
[original link](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)


1.  [Supervised Learning](https://scikit-learn.org/stable/supervised_learning.html)
    1.  Generalized Linear Models
        1.  Ordinary Least Squares
        2.  Ridge, Lasso, Elastic Net, LSRS (least-angle regression), OMP (Orthogonal Matching Pursuit), Bayesian Regression, Logistic Regression, Perceptron, Passive Aggressive Algorithms, SGD (Stochastic Gradient Descent)
        3.  Robustness regression estimators: RANSAC, Theil Sen and HuberRegressor
        4.  Polynomial regression
    2.  Linear and Quadratic Discriminant Analysis (LDA and QDA)
        1.  two classic classifier, generating a linear and a quadratic decision surface
        2.  dimensionality reduction using LDA, vs PCA
    3.  Kernel Ridge Regression
        1.  KernelRidge or SVR (support vector regression)
    4.  Support Vector Machines
        1.  Classification: SVC, NuSVC and LinearSVC.
            1.  Multiple classes: SVC: one-vs-one (platt scaling), LinearSVC: one-vs-rest
            2.  Unbalanced problems
        2.  Regression: extended from classification, depends only on a subset of the training data near margin.
        3.  Outlier detection: One-Class SVM
        4.  Tips and Practical Use
        5.  Kernel functions: linear, polynomial, rbf, sigmoid, etc
    5.  Stochastic Gradient Descent
        1.  SGDClassifier: a plain stochastic gradient descent learning routine which supports different loss functions and penalties for classification.
            1.  loss="hinge": linear SVM, “log”: LR
            2.  penalty=“l2”: L2-norm, “l1”: l1-norm, “elasticnet”: (1 - l1\_ratio) \* L2 + l1\_ratio \* L1
            3.  support weighted class and weighted instances
        2.  SGDRegression: well suited for regression problems with a large number of training samples (> 10.000)
            1.  for other problems we recommend Ridge, Lasso, or ElasticNet
            2.  loss = “squared\_loss”, “huber”, “epsilon\_insensitive"
    6.  Nearest Neighbors
        1.  Unsupervised NN: BallTree, KDTree, BruteForce(pair wise)
        2.  NN Classification/Regression:
            1.  Classification: discrete value, majority vote of the nearest neighbors of each point
            2.  Regression: continuous, mean of the labels of its nearest neighbors
            3.  KNeighbors\*, Radiusneighbots\*
    7.  ==Gaussian Processes==: a generic supervised learning method designed to solve regression and probabilistic classification problems.
    8.  Cross Decomposition
        1.  contains two main families of algorithms: the partial least squares (PLS) and the canonical correlation analysis (CCA)
        2.  are useful to find linear relations between two multivariate datasets
    9.  Naive Bayes
        1.  Gaussian NB: The likelihood of the features is assumed to be Gaussian
        2.  Multinomial NB: multinomial distributed data, e.g. text classification
        3.  Complement NB: an adaptation of the standard MNB algorithm that is particularly suited for imbalanced data sets
        4.  Bernoulli NB: multivariate Bernoulli distributions, e.g. multiple features but each is binary-valued.
    10.  Decision Trees
        1.  scikit-learn uses an optimized version of the CART algorithm, 
        2.  does not support by now: 1) categorical variables, 2) pruning
        3.  over-fitting, local optimal problem, etc can be solved by assembled learner (multiple trees, boosting or bagging)
        4.  hard to learn: XOR, parity or multiplexer problems; learn biased tree if some classes dominate
    11.  Ensemble methods
        1.  bagging methods work best with strong and complex models (e.g., fully developed decision trees), in contrast with boosting methods which usually work best with weak models (e.g., shallow decision trees).
        2.  Bagging:  samples are drawn with replacement, 
            1.  Random Forests: a random subset of features is used for node splitting, then looking for the most discriminative thresholds
            2.  Extremely Randomized Trees: random-generate thresholds for features and choose the best one for splitting.
        3.  AdaBoost
            1.   fit a sequence of weak learners, then combined through a weighted majority vote (or sum) to produce the final prediction.
        4.  ====Gradient Tree Boosting====
        5.  Voting Classifier: combine different classifiers and use a majority vote (hard) or average predicted probabilities (soft) to predict the class labels
    12.  Multi-class and multi-label algorithms
        1.  1) Inherently multi-class, 2) Multi-class One-vs-One, 3) multi-class One-vs-All, 4) Support multi-label, 5) support multi-class and multi-output
    13.  Feature selection
        1.  Removing features with low variance: VarianceThreshold
        2.  Univariate feature selection: select the best features based on univariate statistical tests
            1.  For regression: f\_regression, mutual\_info\_regression
            2.  For classification: chi2, f\_classif, mutual\_info\_classif
        3.  SelectFromModel: L1-based or tree-based feature select
    14.  Semi-Supervised
        1.  some of the samples are not labeled in training data, perform well when we have a very small amount of labeled points and a large amount of unlabeled points. => LabelPropagation and LabelSpreading
    15.  Isotonic Regression:  fits a non-decreasing function to data
    16.  Probability calibration: allows you to better calibrate the probabilities of a given model, or to add support for probability prediction.
    17.  Neural network models: multiple-layer perceptron (MLP), MLPClassifier, MLPRegression
2.  [Unsupervised Learning](https://scikit-learn.org/stable/unsupervised_learning.html)
    1.  Gaussian mixture models: a probabilistic model that assumes all the data points are generated from a mixture of a finite number of Gaussian distributions with unknown parameters.
        1.  The [GaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html#sklearn.mixture.GaussianMixture) object implements the [expectation-maximization](https://scikit-learn.org/stable/modules/mixture.html#expectation-maximization) (EM) algorithm for fitting mixture-of-Gaussian models, it comes with different options to constrain the covariance of the difference classes estimated: spherical, diagonal, tied or full covariance.
        2.  The [BayesianGaussianMixture](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.BayesianGaussianMixture.html#sklearn.mixture.BayesianGaussianMixture) object implements a variant of the Gaussian mixture model with variational inference algorithms. 
            1.  Variational inference is an extension of expectation-maximization that maximizes a lower bound on model evidence (including priors) instead of data likelihood.
    2.  Manifold learning: an approach to non-linear dimensionality reduction
        1.  PCA, LDA, ICA define specific rubrics to choose an “interesting” linear projection of the data
        2.  There are various algorithms: Isomap, Locally Linear Embedding, t-SNE, etc. read more from [Comparison of Manifold Learning methods](https://scikit-learn.org/stable/auto_examples/manifold/plot_compare_methods.html#sphx-glr-auto-examples-manifold-plot-compare-methods-py)
    3.  Clustering
        1.  [K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means), [Affinity propagation](https://scikit-learn.org/stable/modules/clustering.html#affinity-propagation), [Mean-shift](https://scikit-learn.org/stable/modules/clustering.html#mean-shift), [Spectral clustering](https://scikit-learn.org/stable/modules/clustering.html#spectral-clustering), [Ward hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering), [Agglomerative clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering), [DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan), [OPTICS](https://scikit-learn.org/stable/modules/clustering.html#optics), [Gaussian mixtures](https://scikit-learn.org/stable/modules/mixture.html#mixture), [Birch](https://scikit-learn.org/stable/modules/clustering.html#birch)
        2.  Performance evaluation:
            1.  metrics.adjusted\_rand\_score, adjusted\_mutual\_info\_score, homogeneity\_score, completeness\_score, v\_measure\_score, fowlkes\_mallows\_score, silhouette\_score, calinski\_harabasz\_score, davies\_bouldin\_score, contingency\_matrix, , ,
    4.  Biclustering: simultaneously cluster rows and columns of a data matrix
        1.  The [SpectralCoclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.bicluster.SpectralCoclustering.html#sklearn.cluster.bicluster.SpectralCoclustering) algorithm finds biclusters with values higher than those in the corresponding other rows and columns. Each row and each column belongs to exactly one bicluster, so rearranging the rows and columns to make partitions contiguous reveals these high values along the diagonal
        2.  The [SpectralBiclustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.bicluster.SpectralBiclustering.html#sklearn.cluster.bicluster.SpectralBiclustering) algorithm assumes that the input data matrix has a hidden checkerboard structure. 
    5.  Decomposing signals in components
        1.  Principal component analysis (PCA): decompose a multivariate dataset in a set of successive orthogonal components that explain a maximum amount of the variance.
            1.  [IncrementalPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.IncrementalPCA.html#sklearn.decomposition.IncrementalPCA), [KernelPCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.KernelPCA.html#sklearn.decomposition.KernelPCA), [SparsePCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.SparsePCA.html#sklearn.decomposition.SparsePCA), 
        2.  [TruncatedSVD](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD) implements a variant of singular value decomposition (SVD) that only computes the k largest singular values, where k is a user-specified parameter.
        3.  Independent component analysis(ICA): separates a multivariate signal into additive subcomponents that are maximally independent
        4.  Non-negative matrix factorization (NMF): finds a decomposition of samples X into two matrices W and H of non-negative elements, by optimizing the distance dbetween X and the matrix product WH
        5.  Latent Dirichlet Allocation (LDA)
    6.  Covariance estimation
        1.  Empirical covariance: The covariance matrix of a data set is known to be well approximated by the classical maximum likelihood estimator (or “empirical covariance”), provided the number of observations is large enough compared to the number of features (the variables describing the observations). 
        2.  Shrunk Covariance: 
        3.  Sparse Inverse covariance:
        4.  Robust Covariance Estimation.
    7.  Novelty and Outlier Detection
        1.  both are used for anomaly detection,
        2.  outlier detection try to fit the regions where the training data is the most concentrated, ignoring the deviant observations;
        3.  novelty detection is to identify whether a new observation is an outlier/novelty.  
    8.  Density Estimation
        1.  Histogram
        2.  Kernel density estimation: uses the Ball Tree or KD Tree for efficient queries
    9.  Neural network models
        1.  Restricted Boltzmann machines (RBM) are unsupervised nonlinear feature learners based on a probabilistic model
3.  [Model Selection and Evaluation](https://scikit-learn.org/stable/model_selection.html)
    1.  Cross-validation: evaluating estimator performance
        1.  from sklearn.model\_selection import train\_test\_split, cross\_val\_score
        2.  KFold, LeaveOneOut, LeavePOut, ShuffleSplit, ShuffleKFold, GroupKFold, etc
    2.  Tuning the hyper-parameters of an estimator
        1.  [GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV) exhaustively considers all parameter combinations,
        2.  [RandomizedSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.RandomizedSearchCV.html#sklearn.model_selection.RandomizedSearchCV) can sample a given number of candidates from a parameter space with a specified distribution
        3.  Specify an objective metric: by default parameter search uses score function to evaluate a parameter setting, while for some application, such as unbalanced data, we can specify alternative scoring function via \`scoring\` parameter.
            1.  [sklearn.metrics.accuracy\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score) for classification and [sklearn.metrics.r2\_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score) for regression.
        4.  Alternative to Brute Force parameter search
            1.  model specific cv, information criterion, out of bag estimates
    3.  Model evaluation: quantifying the quality of predictions
        1.  Estimator score method. The default score function of estimators to evaluate criterion for the designed problem.
        2.  [Scoring parameter](https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter). Model-evaluation tools using [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html#cross-validation) to take a scoring parameter that controls what metric they apply to the estimators evaluated.
        3.  Metric functions from [sklearn.metrics](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics). The metrics module implements functions assessing prediction error for specific purposes. [classification-metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics), [multilabel-ranking-metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#multilabel-ranking-metrics), [regression-metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics), [clustering-metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#clustering-metrics), [dummy-estimators](https://scikit-learn.org/stable/modules/model_evaluation.html#dummy-estimators)
    4.  Model persistence
        1.  pickle.dumps/loads, or joblib.dump/load, the latter is more efficient on objects that carry large numpy arrays internally.
    5.  Validation curves: plotting scores to evaluate models
        1.  from sklearn.model\_selection import validation\_curve
        2.  from sklearn.model\_selection import learning\_curve
4.  [Inspection](https://scikit-learn.org/stable/inspection.html)
    1.  Partial dependence plots
5.  [Dataset Transformations](https://scikit-learn.org/stable/data_transforms.html)
    1.  Pipelines and composite estimators
        1.  estimators \= \[('reduce\_dim', PCA()), ('clf', SVC())\]
        2.  TransformedTargetRegressor transforms the targets y before fitting a regression model. 
    2.  Feature extraction (generate transformers)
        1.  [DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html#sklearn.feature_extraction.DictVectorizer) support ‘one-hot’ coding for categorical features. DictVectorizer().fit\_transform(some\_data)
        2.  [FeatureHasher](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html#sklearn.feature_extraction.FeatureHasher) apply a hash function to the features to determine their column index, it uses the signed 32-bit variant of MurmurHash3
        3.  Text feature extraction
    3.  Preprocessing data (clean transformers)
        1.  Standardization: zero mean and uni variance.
            1.  X\_scaled \= preprocessing.scale(X\_train)
            2.  scaler \= preprocessing.StandardScaler().fit(X\_train)
            3.  scaling data with outliers: [RobustScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html#sklearn.preprocessing.RobustScaler)
        2.  Non-linear transformation
            1.  [QuantileTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html#sklearn.preprocessing.QuantileTransformer): provide a non-parametric transformation to map the data to a uniform distribution with values between 0 and 1
                1.  quantile\_transformer \= preprocessing.QuantileTransformer(random\_state\=0)
            2.  [PowerTransformer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PowerTransformer.html#sklearn.preprocessing.PowerTransformer) aim to map data from any distribution to as close to a Gaussian distribution, currently provides two such power transformations, the Yeo-Johnson transform and the Box-Cox transform.
                1.  pt \= preprocessing.PowerTransformer(method\='box-cox', standardize\=False)
        3.  Normalization: scaling individual samples to have unit norm
        4.  Encoding categorical features
            1.  [OrdinalEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OrdinalEncoder.html#sklearn.preprocessing.OrdinalEncoder): transforms each categorical feature to one new feature of integers (0 to n\_categories - 1)
            2.  [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder): transforms each categorical feature with n\_categories possible values into n\_categories binary features
                1.  enc \= preprocessing.OneHotEncoder()
        5.  [Discretization](https://en.wikipedia.org/wiki/Discretization_of_continuous_features): aka quantization or binning, partitions continuous features into discrete values
            1.  [KBinsDiscretizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.KBinsDiscretizer.html#sklearn.preprocessing.KBinsDiscretizer) discretizes features into k bins
        6.  Generating polynomial features
            1.  poly \= PolynomialFeatures(2); poly.fit\_transform(X) 
        7.  [Compare the effect of different scalers on data with outliers](https://scikit-learn.org/stable/auto_examples/preprocessing/plot_all_scaling.html#sphx-glr-auto-examples-preprocessing-plot-all-scaling-py)
    4.  Imputation of missing values
        1.  [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer),  [IterativeImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html#sklearn.impute.IterativeImputer),  [MissingIndicator](https://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html#sklearn.impute.MissingIndicator)
    5.  Unsupervised dimensionality reduction (reduce transformers)
        1.  [decomposition.PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA):  [Decomposing signals in components (matrix factorization problems)](https://scikit-learn.org/stable/modules/decomposition.html#decompositions)
        2.  random\_projection provides several tools for data reduction by random projections
        3.  [cluster.FeatureAgglomeration](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.FeatureAgglomeration.html#sklearn.cluster.FeatureAgglomeration) applies [Hierarchical clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering) to group together features that behave similarly
    6.  Random Projection
        1.  theoretical foundation: [Johnson-Lindenstrauss lemma](https://en.wikipedia.org/wiki/Johnson%E2%80%93Lindenstrauss_lemma)
        2.  [GaussianRandomProjection](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.GaussianRandomProjection.html#sklearn.random_projection.GaussianRandomProjection): projects the original input space on a randomly generated matrix
        3.  [SparseRandomProjection](https://scikit-learn.org/stable/modules/generated/sklearn.random_projection.SparseRandomProjection.html#sklearn.random_projection.SparseRandomProjection) reduces the dimensionality by projecting the original input space using a sparse random matrix
    7.  Kernel Approximation (expand transformers)
        1.  [Nystroem](https://scikit-learn.org/stable/modules/generated/sklearn.kernel_approximation.Nystroem.html#sklearn.kernel_approximation.Nystroem), Radial Basis Function Kernel, Additive Chi Squared Kernel, Skewed Chi Squared Kernel
    8.  Pairwise metrics, Affinities and Kernels
        1.  Cosine similarity, Linear kernel, Polynomial kernel, Sigmoid kernel, RBF kernel, Laplacian kernel, Chi-squared kernel
    9.  Transforming the prediction target (y)
        1.  [LabelBinarizer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelBinarizer.html#sklearn.preprocessing.LabelBinarizer), [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html#sklearn.preprocessing.LabelEncoder)
6.  [Dataset loading utilities](https://scikit-learn.org/stable/datasets/index.html)
    1.  Toy datasets: small standard datasets
        1.  regression: [boston](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston) house price, [diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes), [linnerud](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud)
        2.  classification: [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris), [digits](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits), [wine](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine), [breast\_cancer](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer)
    2.  Real world datasets: download large dataset
        1.  regression: [olivetti\_faces](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_olivetti_faces.html#sklearn.datasets.fetch_olivetti_faces), [20newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups), [20newsgroups\_vectorized](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups_vectorized.html#sklearn.datasets.fetch_20newsgroups_vectorized), [lfw\_people](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_people.html#sklearn.datasets.fetch_lfw_people), [lfw\_pairs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_lfw_pairs.html#sklearn.datasets.fetch_lfw_pairs), [covtype](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html#sklearn.datasets.fetch_covtype), [rcv1](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_rcv1.html#sklearn.datasets.fetch_rcv1), [kddcup99](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_kddcup99.html#sklearn.datasets.fetch_kddcup99)
        2.  classification: [california\_housing](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html#sklearn.datasets.fetch_california_housing)
    3.  Generated datasets: various random sample generators to build artificial datasets
        1.  classification/clustering, regression, manifold learning, decoposition
    4.  Loading other datasets
        1.  sample images, datasets in svmlight/libsvm format, datasets from [openml.org](http://openml.org) repository, external datasets
7.  [Computing with scikit-learn](https://scikit-learn.org/stable/modules/computing.html)
    1.  Strategies to scale computationally: bigger data
        1.  using out-of-core/external-memory learning
            1.  streaming instances: using external storage
            2.  extracting features
            3.  incremental algorithms: use partial\_fit API to learn min batch data, sometimes called "online learning", [list of incremental estimators](https://scikit-learn.org/stable/modules/computing.html#incremental-learning)
    2.  Computational Performance
    3.  Parallelism, resource management, and configuration



















----

- Date: 2019-04-16
- Tags: #machineLearning 



