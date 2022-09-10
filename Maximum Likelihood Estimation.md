# Maximum Likelihood Estimation
----

![[Archive/Machine Learning/_resources/Maximum_Likelihood_Estimation.resources/unknown_filename.png]]


1.  Likelihood: Given observed data, what’s the chance of a given reality or model is true? 
2.  Maximum Likelihood Estimation
    1.  Determine best model parameters (reality) that fit given data
        *   \=> Maximizes log-likelihood function to estimate parameters
        *   ![[Archive/Machine Learning/_resources/Maximum_Likelihood_Estimation.resources/unknown_filename.5.png]]
        *   Likelihood Function L: ![[Archive/Machine Learning/_resources/Maximum_Likelihood_Estimation.resources/unknown_filename.3.png]]
        *   Maximization of L is difficult in practice, so the method maximizes log-likelihood instead ![[Archive/Machine Learning/_resources/Maximum_Likelihood_Estimation.resources/unknown_filename.1.png]]
    2.  Compare multiple models to determine the best fit to data.
        *   \=> Uses  information theory to compare model fits
        *   Kullback-Leibler Information
            *   Use information theory techniques to quantify the distance between models f and g (each is a probability density function)
            *   ![[Archive/Machine Learning/_resources/Maximum_Likelihood_Estimation.resources/unknown_filename.4.png]]
            *   Information Lost when g used to approximate f
            *   model g over parameter space theta
        *   Model Selection with **AIC**
            *   Hirotugu Akaike shows that K-L information could be estimated based on the maximum log-likelyhood and created “an/Akaike information criterion” 
            *   ![[Archive/Machine Learning/_resources/Maximum_Likelihood_Estimation.resources/unknown_filename.2.png]]
            *   K is smilar as regularization, a tradeoff between bias and variance.
            *   Akaike Weights




Reference

1.  [Maximum Likelihood Estimation](https://www.youtube.com/watch?v=2vh98ful3_M&index=27&list=WL&t=0s)



----

- Date: 2019-02-03
- Tags: #machineLearning #statistics 



