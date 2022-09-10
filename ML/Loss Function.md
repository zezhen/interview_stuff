---
typora-root-url: ../../../Obsidian-note
---




损失函数（loss function）是用来估量你模型的预测值f(x)与真实值Y的不一致程度，它是一个非负实值函数, 通常使用L(Y, f(x))来表示，损失函数越小，模型的鲁棒性就越好。损失函数是经验风险函数的核心部分，也是结构风险函数重要组成部分, 模型的结构风险函数包括了经验风险项和正则项. 整个式子表示的意思是找到使目标函数最小时的θ值

![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.png]]


1.  Log Loss 对数损失
    1.  ![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.1.png]]
    2.  在极大似然估计中，通常都是先取对数再求导，再找极值点，这样做是方便计算极大似然估计。损失函数L(Y,P(Y|X))是指样本X在分类Y的情况下，使概率P(Y|X)达到最大值
    3.  比如Logistic Regression, LR的推导中, 它假设样本服从Bernoulli (0-1)分布, 然后求得满足该分布的似然函数, 接着用对数求极值. LR并没有求对数似然函数的最大值，而是把极大化当做一个思想，进而推导它的风险函数为最小化的负的似然函数, 即max F(y, f(x)) —> min -F(y, f(x))。从损失函数的角度上，它就成为了log损失函数
2.  Square Loss 平方损失
    1.  ![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.2.png]]
    2.  最小二乘法是线性回归的一种方法，它将回归的问题转化为了凸优化的问题, 基本原则是: 最优拟合曲线应该使得所有点到回归直线的距离和最小. 
    3.  平方损失函数可以通过线性回归在假设样本是高斯分布的条件下推导得到
3.  Exp Loss 指数损失
    1.  ![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.3.png]]
    2.  e.g. Adaboost
4.  [Hinge Loss](https://en.wikipedia.org/wiki/Hinge_loss)
    1.  详见[[统计学习方法|统计学习方法]]中线性SVM
    2.  ![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.4.png]], 前项为hinge loss function, 后者相当于L2 regulation
5.  0-1 Loss
    1.  ![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.5.gif]]
6.  Absolute Value loss
    1.  ![[Archive/Machine Learning/_resources/Loss_Function.resources/unknown_filename.6.gif]]


Log Loss vs Cross Entropy

1. They're almost the same => [here](https://jamesmccaffrey.wordpress.com/2016/09/25/log-loss-and-cross-entropy-are-almost-the-same/)
2. Log loss is usually used when there are just two possible outcomes that can be either 0 or 1, so the y or (1-y) is 0; Cross entropy is usually used when there are three or more possible outcomes.
3. read more about [entropy in ML](https://medium.com/swlh/shannon-entropy-in-the-context-of-machine-learning-and-ai-24aee2709e32)

logloss = -y \* log(pctr) - (1-y)\*log(1-pctr)
normalizer = -tctr \* log(tctr) - (1-tctr) \* log(1-tctr), where pctr is predicted ctr, tctr is actual ctr
normalized entropy (NE) = logloss / normalizer => [ideas behind normalized cross-entropy](https://www.nist.gov/system/files/documents/2017/11/30/nce.pdf)

Normalized entropy just normalizes the cross entropy and log loss constructs. It normalizes the log loss with a baseline: the log loss of a constant predictor (model) what always outputs the probability of a class to be the average rate of that class appearing in the corresponding data set. e.g. if the ratio of examples of clicks in a data set is 0.6, then the constant predictor predicts 0.6 for a click, and 0.4 for not-a-click. (https://fb.quip.com/mLLRA037sbFd, [Practical Lessons from Predicting Clicks on Ads at Facebook](https://scontent-sjc3-1.xx.fbcdn.net/v/t39.8562-6/240842589_204052295113548_74168590424110542_n.pdf?_nc_cat=109&ccb=1-7&_nc_sid=ad8a9d&_nc_ohc=aQfJ6bOFDVgAX9fECxC&_nc_ht=scontent-sjc3-1.xx&oh=00_AT-mFVZVXSeAKveLKw8f0thA2Q9OLFA24XxYFXgfajtvwA&oe=62D8EF0A))

![image-20220716234018515](/Archive/img/image-20220716234018515.png)

* huber loss vs MSE/MAE [https://fburl.com/ililcrl2](https://fburl.com/ililcrl2)   
* Huber Loss is often used in regression problems. Compared with MSE, Huber Loss is less sensitive to outliers as if the loss is too much it changes quadratic equation to linear and hence is a combination of both MSE and MAE. ([ref](https://www.numpyninja.com/post/loss-functions-when-to-use-which-one))

Reference

1.  [损失函数](http://www.csuldw.com/2016/03/26/2016-03-26-loss-function/)



----

- Date: 2019-06-16
- Tags: #machineLearning 



