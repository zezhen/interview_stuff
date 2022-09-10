# Probability and Statistics
----

[[Correlation and Regression|Correlation and Regression]]


[P-value and Probability](https://www.youtube.com/watch?v=5Z9OIYA8He8)

Probability = number of outcomes of interest  / the total number of outcomes
[P-value](https://www.statsdirect.com/help/basics/p_values.htm) is the probability that random chance generated the data, or something else that is equal or rarer
    The P value, is the probability of finding the observed, or more extreme, results when the null hypothesis (H0) of a study question is true. => 

![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.1.png]]



[Probability vs Likelihood](https://www.youtube.com/watch?v=pYxNSUDSFH4&t=0s&list=WL&index=20)

![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.png]]
![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.4.png]]


1.  Probability: what’s the chance of observing particular data or sample given a specific model or population?
2.  Likelihood: Given observed data, what’s the chance of a given reality or model is true? 



[Normal Distribution](https://en.wikipedia.org/wiki/Normal_distribution)
Normal distributions are often used in the [natural](https://en.wikipedia.org/wiki/Natural_science) and [social sciences](https://en.wikipedia.org/wiki/Social_science) to represent real-valued [random variables](https://en.wikipedia.org/wiki/Random_variable) whose distributions are not known. It’s useful because of the [central limit theorem](https://en.wikipedia.org/wiki/Central_limit_theorem). In its most general form, under some conditions (which include finite [variance](https://en.wikipedia.org/wiki/Variance)), it states that averages of samples of observations of [random variables](https://en.wikipedia.org/wiki/Random_variables) independently drawn from independent distributions [converge in distribution](https://en.wikipedia.org/wiki/Convergence_in_distribution) to the normal, that is, they become normally distributed when the number of observations is sufficiently large. 
![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.3.svg]]
![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.2.png]]


[Binomial Distribution](https://en.wikipedia.org/wiki/Binomial_distribution)

binomial distribution with parameters n and p is the [discrete probability distribution](https://en.wikipedia.org/wiki/Discrete_probability_distribution) of the number of successes in a sequence of n [independent](https://en.wikipedia.org/wiki/Statistical_independence) [experiments](https://en.wikipedia.org/wiki/Experiment_(probability_theory)), each asking a [yes–no question](https://en.wikipedia.org/wiki/Yes%E2%80%93no_question).

The binomial distribution is frequently used to model the number of successes in a sample of size n drawn [with replacement](https://en.wikipedia.org/wiki/Sampling_(statistics)#Replacement_of_selected_units) from a population of size N. If the sampling is carried out without replacement, the draws are not independent and so the resulting distribution is a [hypergeometric distribution](https://en.wikipedia.org/wiki/Hypergeometric_distribution), not a binomial one. However, for N much larger than n, the binomial distribution remains a good approximation, and is widely used.

In general, if the random variable X follows the binomial distribution with parameters n ∈ ℕ and p ∈ \[0,1\], we write X ~ B(n, p). The probability of getting exactly k successes in n trials is given by the [probability mass function](https://en.wikipedia.org/wiki/Probability_mass_function):
    ![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.7.svg]]
    ![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.5.svg]]

Cumulative distribution function
    ![[unknown_filename.6.svg]]

e.g. In Mappi, one feature called propensity, which is to measure the users’ click propensity. Before dive into this, let’s assume one case: user A has 1000 impressions and 10 clicks, user B has 1 impression and 1 click, question is which user has higher click propensity. For this case, given a impression, user can trigger a click on that, or ignore it, which is non-click. it’s a yes-no question or 0/1 distribution.

Considering the total ads impressions N is very large, thus we can approximate the impression-click problem as binomial distribution, the distribution probability p is overall ctr, which considering all impressions and clicks. For user A, n = 1000, k = 10, for user B, n=1, k=1, then we can calculate the cumulative distribution function for both users and get propensity. below is a python script.

def calcCDF(impr, clk, ctr):
    pval = (1 - ctr)\*\*impr
    sumAll = pval
    if clk == 0:
        return sumAll
    else:
        for c in xrange(1, clk + 1):
            nextpval = pval \* ctr \* (impr - c + 1)/(c \* (1 - ctr))
            sumAll = sumAll + nextpval
            pval = nextpval
        return sumAll


[Poisson Distribution](https://en.wikipedia.org/wiki/Poisson_distribution)

is a [discrete probability distribution](https://en.wikipedia.org/wiki/Discrete_probability_distribution) that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant rate and [independently](https://en.wikipedia.org/wiki/Statistical_independence) of the time since the last event. The Poisson distribution can also be used for the number of events in other specified intervals such as distance, area or volume.

The Poisson distribution is popular for modelling the number of times an event occurs in an interval of time or space.

Assumptions:

*   k is the number of times an event occurs in an interval and k can take values 0, 1, 2, ….
*   The occurrence of one event does not affect the probability that a second event will occur. That is, events occur independently.
*   The rate at which events occur is constant. The rate cannot be higher in some intervals and lower in other intervals.
*   Two events cannot occur at exactly the same instant; instead, at each very small sub-interval exactly one event either occurs or does not occur.

Or

*   The actual probability distribution is given by a [binomial distribution](https://en.wikipedia.org/wiki/Binomial_distribution) and the number of trials is sufficiently bigger than the number of successes one is asking about


An event can occur 0, 1, 2, … times in an interval. The average number of events in an interval is designated ![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.9.svg]] (lambda). Lambda is the event rate, also called the rate parameter. The probability of observing k events in an interval is given by the equation
![[Archive/Machine Learning/_resources/Probability_and_Statistics.resources/unknown_filename.8.svg]]

Beta Distribution

Beta分布是二项分布之上的分布(distribution over bionominals)，也是二项分布的共轭先验分布(conjugate prior of bionominals)。


Dirichlet分布是多项分布之上的分布

----

- Date: 2019-01-13
- Tags: #machineLearning #statistics 



