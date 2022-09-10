# Measurement
----


AUC/ROC vs Log Loss

AUC is a rank statistic (i.e. scale invariant) & log loss is a calibration statistic.


AUC/ROC vs F1 score

One must understand crucial difference between AUC ROC and "point-wise" metrics like accuracy/precision etc. ROC is a function of a threshold. Given a model (classifier) that outputs the probability of belonging to each class, we predict the class that has the highest probability (support). However, sometimes we can get better scores by changing this rule and requiring one support to be 2 times bigger than the other to actually classify as a given class. This is often true for imbalanced datasets. This way you are actually modifying the learned prior of classes to better fit your data. ROC looks at "what would happen if I change this threshold to all possible values" and then AUC ROC computes the integral of such a curve.

Consequently:

1.  high AUC ROC vs low f1 or other "point" metric, means that your classifier currently does a bad job, however you can find the threshold for which its score is actually pretty decent
2.  low AUC ROC and low f1 or other "point" metric, means that your classifier currently does a bad job, and even fitting a threshold will not change it
3.  high AUC ROC and high f1 or other "point" metric, means that your classifier currently does a decent job, and for many other values of threshold it would do the same
4.  low AUC ROC vs high f1 or other "point" metric, means that your classifier currently does a decent job, however for many other values of threshold - it is pretty bad


[[Loss Function|Loss Function]]

[ROC (receiver operating characteristic) curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic)
AUC (Area Under Curve) [Clearly Explained](https://www.youtube.com/watch?v=AJN2yl004-4)

curve is generated from various thresholds in one model, different thresholds cause different True Positive and False Positive, we can draw the curve from these TP-FP points.
then we select the best TP-FP point using linear programing, and mapping back to the threshold we use.


![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.6.png]]

[Probabilistic Classification](https://www.youtube.com/watch?v=RXMu96RJj_s&list=PLYx7XA2nY5GcDQblpQ_M1V3PQPoLWiDAC&index=12)


1.  which model is better?
    1.  Naive Bayes vs Logistic Regress: big difference between distribution but close AUC scores
    2.  ![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.png]]
2.  What's AUC socre?
    1.  TruePositiveRate (TPR) = TruePositive / (TruePositive + FalseNegative) = Correctly Classified as 1  / Total Positives
    2.  FalsePositiveRate (FPR) = FalsePositive / (FalsePositive + TrueNegative) = Falsely Classified as 1 / Total Negative
    3.  AUC is a rank statistical, below table (left) contains three columns: rank #, observed (P/N), forecasted score
    4.  we first rank all items by predicted score, start from (0,0) point, scan the table, every time meet a P, move up, N then move right, then we got ROC curve
        1.  the probability we predicted is only used for ranking the list, AUC score only care about the ranking, it's also called c-statistics, it's a probability
        2.  \=> AUC score is not a good metrics for probabilistic classification
    5.  ![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.1.png]]
3.  Brier Score
    1.  We split the forested probabilities into K buckets, we calculated average forecasted and observed score, then draw the calibration plot, diagonal is the ideal calibrated
        1.  ![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.2.png]]
    2.  We bucket by K unique predictions
        1.  Reliability or calibration: how close your prediction to the reliability.
        2.  Resolution is to make point far away from ground truth
        3.  Uncertainty is to measure the noise level of data
        4.  ![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.3.png]]
    3.  Brier Score
        1.  BS is a mean square error
        2.  ![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.4.png]]
    4.  Probability Calibration Algorithms: given the calibration plot, whether we can transform the points to diagonal?
        1.  ==Platt Scaling==
        2.  ==Isotonic Regression==
        3.  ==Spline==
        4.  calibration algorithm can significantly improve brier score but no much change on AUC
        5.  ![[Archive/Machine Learning/_resources/Measurement.resources/unknown_filename.5.png]]
    5.  Why not apply calibration algorithm to Logistic Regression but only to Naive Bayes?
        1.  LR  loss function is already trying to minimize (y^ - y), which means if LR converge, the brier score is minimum
        2.  Naive Bayes has the conditional independence assumption, which cause evidence being counted multiple times
        3.  Most algorithms has similar calibration problems, NB is tend to push the probabilities to two ends, assembly models, like boosting trees, is tend to push probabilities to the middle due to the voting mechanism.



----

- Date: 2019-08-24
- Tags: #machineLearning 



