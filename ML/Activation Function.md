# Activation Function
----


没有激活函数的神经网络本质上只是一个线性回归模型。[sharing](https://www.jiqizhixin.com/articles/2020-03-06-6)


*   Binary Step（二元阶跃）
*   Linear（线性）
*   Sigmoid（S型）
    *   非线性, 连续可微
    *   [vanishing gradient](http://neuralnetworksanddeeplearning.com/chap5.html#the_vanishing_gradient_problem)
*   Tanh（双曲正切）
    *   比sigmoid梯度更陡, 关于0点对称
*   ReLU（线性整流单元）
    *   优点: 不会同时激活所有神经元
    *   缺点: 负值时梯度为0, 反向传播过程中, 神经元不会有更新
*   Leaky ReLU（泄露型线性整流函数）
*   Parameterised ReLU（参数化线性整流函数）
*   Exponential Linear Unit（指数化线性单元）
*   Swish
*   Softmax


选择正确的激活函数

*   对于分类器，Sigmoid函数及其组合通常工作得更好。
*   由于有梯度消失的问题，有时会避免使用sigmoid和tanh函数。
*   ReLU函数是一种通用的激活函数，目前被广泛使用。
*   如果在我们的网络中遇到神经元未激活的情况，Leaky ReLU函数是最好的选择。
*   始终记住，ReLU函数应该只在隐藏层中使用。
*   根据经验，您可以从使用ReLU函数开始，然后在ReLU不能提供最佳结果的情况下转移到其他激活函数。



----

- Date: 2020-03-14
- Tags: #machineLearning 



