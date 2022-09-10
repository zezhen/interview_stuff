[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/)

[Permalink](https://github.com/graykode/distribution-is-all-you-need/blob/105fef4b156af2d97f48d42edc234c235fcb998f/README.md)

## **distribution-is-all-you-need**

**#distribution -is-all-you-need** is the basic distribution probability tutorial for **most common distribution focused on Deep learning** using python library.

#### Overview of distribution probability

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/overview.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/overview.png)

-   `conjugate` means it has relationship of **conjugate distributions**.
    
    > In [Bayesian probability](https://en.wikipedia.org/wiki/Bayesian_probability) theory, if the [posterior distributions](https://en.wikipedia.org/wiki/Posterior_probability) _p_(_θ_ | _x_) are in the same [probability distribution family](https://en.wikipedia.org/wiki/List_of_probability_distributions) as the [prior probability distribution](https://en.wikipedia.org/wiki/Prior_probability_distribution) _p_(θ), the prior and posterior are then called **conjugate distributions,** and the prior is called a **conjugate prior** for the [likelihood function](https://en.wikipedia.org/wiki/Likelihood_function). [Conjugate prior, wikipedia](https://en.wikipedia.org/wiki/Conjugate_prior)
    
-   `Multi-Class` means that Random Varivance are more than 2.
    
-   `N Times` means that we also consider prior probability P(X).
    
-   To learn more about probability, I recommend reading \[pattern recognition and machine learning, Bishop 2006\].
    

## distribution probabilities and features

1.  **Uniform distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/uniform.py)
    -   Uniform distribution has same probaility value on \[a, b\], easy probability.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/uniform.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/uniform.png)

2.  **Bernoulli distribution(discrete)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/bernoulli.py)
    -   Bernoulli distribution is not considered about prior probability P(X). Therefore, if we optimize to the maximum likelihood, we will be vulnerable to overfitting.
    -   We use **binary cross entropy** to classify binary classification. It has same form like taking a negative log of the bernoulli distribution.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/bernoulli.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/bernoulli.png)

3.  **Binomial distribution(discrete)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/binomial.py)
    -   Binomial distribution with parameters n and p is the discrete probability distribution of the number of successes in a sequence of n independent experiments.
    -   Binomial distribution is distribution considered prior probaility by specifying the number to be picked in advance.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/binomial.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/binomial.png)

4.  **Multi-Bernoulli distribution, Categorical distribution(discrete)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/categorical.py)
    -   Multi-bernoulli called categorical distribution, is a probability expanded more than 2.
    -   **cross entopy** has same form like taking a negative log of the Multi-Bernoulli distribution.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/categorical.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/categorical.png)

5.  **Multinomial distribution(discrete)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/multinomial.py)
    -   The multinomial distribution has the same relationship with the categorical distribution as the relationship between Bernoull and Binomial.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/multinomial.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/multinomial.png)

6.  **Beta distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/beta.py)
    -   Beta distribution is conjugate to the binomial and Bernoulli distributions.
    -   Using conjucation, we can get the posterior distribution more easily using the prior distribution we know.
    -   Uniform distiribution is same when beta distribution met special case(alpha=1, beta=1).

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/beta.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/beta.png)

7.  **Dirichlet distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/dirichlet.py)
    -   Dirichlet distribution is conjugate to the MultiNomial distributions.
    -   If k=2, it will be Beta distribution.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/dirichlet.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/dirichlet.png)

8.  **Gamma distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/gamma.py)
    -   Gamma distribution will be beta distribution, if `Gamma(a,1) / Gamma(a,1) + Gamma(b,1)` is same with `Beta(a,b)`.
    -   The exponential distribution and chi-squared distribution are special cases of the gamma distribution.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/gamma.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/gamma.png)

9.  **Exponential distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/exponential.py)
    -   Exponential distribution is special cases of the gamma distribution when alpha is 1.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/exponential.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/exponential.png)

10.  **Gaussian distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/gaussian.py)
    -   Gaussian distribution is a very common continuous probability distribution

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/gaussian.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/gaussian.png)

11.  **Normal distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/normal.py)
    -   Normal distribution is standarzed Gaussian distribution, it has 0 mean and 1 std.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/normal.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/normal.png)

12.  **Chi-squared distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/chi-squared.py)
    -   Chi-square distribution with k degrees of freedom is the distribution of a sum of the squares of k independent standard normal random variables.
    -   Chi-square distribution is special case of Beta distribution

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/chi-squared.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/chi-squared.png)

13.  **Student-t distribution(continuous)**, [code](https://github.com/graykode/distribution-is-all-you-need/blob/master/student-t.py)
    -   The t-distribution is symmetric and bell-shaped, like the normal distribution, but has heavier tails, meaning that it is more prone to producing values that fall far from its mean.

[![](https://github.com/graykode/distribution-is-all-you-need/raw/master/graph/student_t.png)](https://github.com/graykode/distribution-is-all-you-need/blob/master/graph/student_t.png)

## Author

If you would like to see the details about relationship of distribution probability, please refer to [this](https://en.wikipedia.org/wiki/Relationships_among_probability_distributions).

[![](https://camo.githubusercontent.com/bf3b3bb04aec83bdeb2d72a41b16d937046ede4b56671c77080906dbbfffe82b/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f362f36392f52656c6174696f6e73686970735f616d6f6e675f736f6d655f6f665f756e69766172696174655f70726f626162696c6974795f646973747269627574696f6e732e6a70672f3238383070782d52656c6174696f6e73686970735f616d6f6e675f736f6d655f6f665f756e69766172696174655f70726f626162696c6974795f646973747269627574696f6e732e6a7067)](https://camo.githubusercontent.com/bf3b3bb04aec83bdeb2d72a41b16d937046ede4b56671c77080906dbbfffe82b/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f362f36392f52656c6174696f6e73686970735f616d6f6e675f736f6d655f6f665f756e69766172696174655f70726f626162696c6974795f646973747269627574696f6e732e6a70672f3238383070782d52656c6174696f6e73686970735f616d6f6e675f736f6d655f6f665f756e69766172696174655f70726f626162696c6974795f646973747269627574696f6e732e6a7067)

-   Tae Hwan Jung [@graykode](https://github.com/graykode), Kyung Hee Univ CE(Undergraduate).
-   Author Email : [nlkey2022@gmail.com](mailto:nlkey2022@gmail.com)
-   **If you leave the source, you can use it freely.**