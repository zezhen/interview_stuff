# Unsupervised Learning and Anomaly Detection
----

[Andrew Ng Course](https://www.youtube.com/watch?v=PK5JsJZd1Uk&list=PLZ9qNFMHZ-A4rycgrgOYma6zxF4BZGGPW&index=77)

K-Means
Principal Component Analysis

[**Anomaly Detection**](https://www.youtube.com/watch?v=hhI-PdMO1sk&list=PLZ9qNFMHZ-A4rycgrgOYma6zxF4BZGGPW&index=89)

Fraud Detection:
 x(i) = features of user i’s activities
 Model p(x) from data
 Identify unusual users by checking which have p{x) < threshold


Assume all features are subject to Normal Distribution  
![[Archive/Machine Learning/_resources/Unsupervised_Learning_and_Anomaly_Detection.resources/unknown_filename.png]]

How to determine the threshold?
Given some label data, e.g. 10000 is normal data and 20 is anomaly data. we can divide them into train/validation/test data set.

1.  Train: 6000 normal data (y=0)
2.  Validation: 2000 normal data (y=0), 10 anomaly data (y=1)
3.  Test: 2000 normal data (y=0), 10 anomaly data (y=1)

Train model on train data, use cross validation to determine the best threshold, metrics can be F1-score, AUC, etc


Why not using supervised learning considering we have labelled data?

Anomaly Detection:

1.  Very skewed data, eg. large negative (y=0) data but very less positive (y=1) data
2.  Many different ’types’ of anomalies, hard for any algorithm to lear from position examples,
    1.  future anomalies may look nothing like any of the anomalous example we seen by now.
3.  e.g. Fraud detection, Manufacturing (aircraft engines), Monitoring machines in data center, etc

Supervised Learning

1.  Large number of position and negative examples
2.  Enough positive examples for algorithm to learn what the positive examples are like.
    1.  future positive examples likely to be similar to ones in training set.
3.  e.g. Email spam classification, Weather prediction, Cancer classification


How to choose features to use?

1.  non-gaussian features: try to transform them to gaussian. like x-> log(x), x^c, c can be 0.01, 0.5, 2, 4, etc
2.  Error analysis: run first version model, check the failure cases, try to figure out any other features could work for this cases.
3.  Choose features that might take on unusually large or small values in the events of an anomaly.
4.  Features conjunctions 



![[Archive/Machine Learning/_resources/Unsupervised_Learning_and_Anomaly_Detection.resources/unknown_filename.1.png]]

**Multivariant Gaussian Distribution**

![[Archive/Machine Learning/_resources/Unsupervised_Learning_and_Anomaly_Detection.resources/unknown_filename.2.png]]

Original Model

1.  manually create features to capture anomalies where x1, x2, take unusually combination of values, e.g. x3=x1/x2
2.  Computationally cheaper
3.  OK even if training set size m is small

Multivariate Model

1.  Automatically captures correlations between features
2.  Computationally more expensive
3.  Must have m > n or else Sigma is non-invertible (better m >= 10\*n)




----

- Date: 2019-01-30
- Tags: #machineLearning #anomalyDetection #course 



