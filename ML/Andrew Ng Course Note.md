# Andrew Ng Course Note
----

[Andrew Ng Courses](https://www.youtube.com/watch?v=r3uBEDCqIN0&list=PLZ9qNFMHZ-A4rycgrgOYma6zxF4BZGGPW&index=71)
 [[Unsupervised Learning and Anomaly Detection|Unsupervised Learning and Anomaly Detection]]


1.  Cost Function
    *   ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.1.png]] 
    *   using Squared Error function for cost function, the goal is to minimize the cost function.
2.  Gradient Decent Algorithm
    1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.2.png]] repeat until converge,
    2.  alpha is the learning rate, for training can try alpha 0.001, 0.01, 0.1, 1, etc
3.  Linear Regression
    1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.3.png]] x0 = 1
4.  Normal Equation
    1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.4.png]] ==> ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.5.png]]
    2.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.6.png]]
5.  Classification
    1.  Linear Regression for classification. Not stable.
        1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.png]]
6.  Logistic Regression
    1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.7.png]]![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.8.png]]
    2.  Classification
        1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.9.png]]
        2.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.10.png]]
    3.  Cost Function
        1.  linear regression uses squared error, while because of the g(z) is non-linear function, it will make the cost function to be non-convex, which cannot guarantee the global minimum.
        2.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.11.png]]
        3.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.12.png]]
        4.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.13.png]]![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.14.png]]
        5.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.15.png]]
        6.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.16.png]] this looks identical to linear regression, but the h\_theta(x) function is sigmoid
        7.  Gradient Descent is only one optimization algorithm, others like Conjugate gradient, BFGS, L-BFGS, no need to manually pick alpha, often faster than GD but more complex.
7.  Regularization
    1.   ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.17.png]] (linear regression)
    2.  if lambda is extremely large value, the theta values trends to 0, which will cause underfit
    3.  after applied regularization, theta updating become a bit smaller theta (e.g. 0.99) + gradient descent update.
        1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.18.png]]
8.  Neural Network
    1.  [[Understanding Deep Learning - Implemention XOR|Understanding Deep Learning - Implemention XOR]]
    2.  Multi-class Classification
        1.  Cost Function
            1.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.19.png]], L is the layer number, sl is the node number in layer l, K is the output classes number
        2.  Forward Propagation
            *   ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.20.png]]
        3.  Back Propagation
            *   ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.21.png]]
            *   ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.22.png]]
        4.  
9.  Model Selection: How to choose best one from multiple models?
    1.  Split data into training set (60%), cross validation (20%), test set(20%)
    2.  Train model using training set data, then use cross validation set to choose the best model (to avoid the case that model fit test set and get high perf)
    3.  Estimate error by test set data.
10.  Bias vs Variance
    1.  underfit => high bias, both train error and cross validation error are high, they are close
        1.  model is too simple, increase data set might not help much
        2.  Try getting additional features
        3.  Try adding polynomial features (x1^, x1x2, etc)
        4.  Try decreasing lambda (regularization)
        5.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.26.png]]
    2.  overfit => high variance, train error is low but cross validation error is high
        1.  there is gap between train and cv, get more data is likely to help
        2.  Try smaller sets of features
        3.  Try increasing lambda (regulariization)
        4.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.25.png]]
    3.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.23.png]]![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.24.png]]
    4.  
11.  [[Support Vector Machine.md|Support Vector Machine]]
12.  [[Unsupervised Learning and Anomaly Detection|Unsupervised Learning and Anomaly Detection]]
13.  Mini-Batch Gradient Descent
    1.  b is the examples number in each iteration, b=m is Batch GD, b=1 is Stochastic
    2.  we can use n / b tasks train theta in parallel, then combine multiple thetas into one. 1) wait all theta return or 2) drop partial
    3.  each iteration, we consider b examples to adjust theta, the larger b is, the easier/non-fluctuant to convergence, but less partition to train in parallel
    4.  ![[Archive/Machine Learning/_resources/Andrew_Ng_Course_Note.resources/unknown_filename.27.png]]
14.  [Application Example: Photo OCR](https://www.youtube.com/watch?v=jOyeJ4-sWqc&index=103&list=PLZ9qNFMHZ-A4rycgrgOYma6zxF4BZGGPW)



----

- Date: 2019-01-29
- Tags: #machineLearning #course



