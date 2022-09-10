# Factorization
----

[srinath slides](https://docs.google.com/presentation/d/1Rt61A21DjAFL4CNar5xR30-9zhRCRj8xMbsgDiUIDQg/edit#slide=id.g4a827c8a17_0_2018)

Embeddings


1.  Categorical data is generally represented by one-hot encoding
    1.  4 advertisers - 4 dimensional one-hot encoding
    2.  3 sites - 3 dimensional one-hot encoding
    3.  Works well in case of smaller dimensionality
2.  How can we represent large dimensional categorical features ?
    1.  Advertisers - 25k, Sites - 10k
    2.  One-hot encoding: Learn 25k weights for advertisers and 10k weights for sites
        1.  Needs more training data (to learn (25k + 10k) parameters)
        2.  Lots of computation (very sparse input representation)
    3.  Translate large sparse vectors into lower-dimension space preserving semantic relationships
        1.  Let’s say: Advertisers represented by 6 dimensional dense vectors (real valued vectors)
        2.  Sites represented by 4 dimensional dense vectors
    4.  Goal : Similar items should be close to each other in d-dimensional space


![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.1.png]]  ===>![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.png]]

y = sigmoid(x \* w + b), w is the weight as original, while x is embedding features, we need calculate both w and x => gradient descent
![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.2.png]]![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.3.png]]

Feature Conjunctions

1.  Let’s say we have 10k sites and 25k advertisers
    1.  How many feature conjunctions? 10k x 25k = 250M parameters
    2.  Model size is quite big once we add <site, advertiser> conjunctions
    3.  Learning 250M parameters require a lot of training examples
2.  May not have training examples for every possible combination <s, a>
    1.  Can’t learn weight if we don’t have training examples for a particular combination
    2.  For example: no training examples for combination <news, chase>
        1.  Can’t learn weight for this feature conjunction
        2.  Can we generalize solution based on other feature conjunctions?
    3.  Memorization vs Generalization
3.  Can we do something better than this approach?


Field Aware Factorization

*   Learn a k dimensional latent vector for every feature to model latent effect with every other feature (feature conjunction)



*   Let’s say we don’t have any training data for <news, etrade> combination
    *   How can we learn weight for this particular feature conjunction ?
    *   Can we predict probability of click for <news, etrade> opportunity (impression) ?
*   Plain vanilla version of feature conjunction
    *   Didn’t  learn weight for feature conjunction <new, etrade> (since no training examples)
    *   ![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.5.png]]
*   How about using Factorization latent vectors to model this ?
    *   ![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.7.png]]
*   How about using Field Aware Factorization latent vectors to model this ?
    *   ![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.4.png]]
    *   In below chart, in the table, each feature (A-D) use 2 embeddings, each has 4 conjunction features
    *   left is the demonstration of each features and it’s conjunctions, right is the true features for each field values
        *   e.g. site=news, then it has two embeddings, and conjunctions related with ’news’, like W\_news,adv, 
        *   non-related fields can be set as 1
    *   ![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.8.png]]
    *   


AdaGrad Algorithm


*   Adjusts learning rate for each parameter based on its previous gradients
    *   Maintains sum of squares of past gradients (G) for each parameter
    *   Learning rate is updated for each parameter by dividing it sqrt(G)
        *   Add square of current gradient to G (past gradients sum)
    *   ![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.6.png]]



Offset (one-pass factorization of feature sets)


*   Key ideas:
    *   use embedding and factorization to generate user and ads features vectors
    *   Score between user and ad is represented as inner product between user and ad vectors
    *   Compute click predictability applying sigmoid transformation on score
*   Collaborative Filtering
    *   Provide item recommendations or predictions based on opinions of other like minded users
    *   Models both users and ads by mapping their features to a latent space
*   Latent Space
    *   Two users are close in latent space if their choices overlap over multiple ads
        *   For example if they click on the same set of ads, they should be close to each other
    *   Two ads are close in latent space if they are clicked by common set of users
    *   Use small representation for users and ads - d-dimensional vector (data is sparse)
*   Left graph is classical LR, users’ features and ads features are both treated as input, model computes the weights
*   Right graph is offset model, which use dot-product, the computation is similar to embedding above, which need to adjust both vector u and a.
    *   ![[Archive/工作资料/Gemini/_resources/Factorization.resources/unknown_filename.9.png]]



[https://git.ouroath.com/Curveball/tf\_training\_pipeline/blob/v2/src/offset/tf\_runner.py](https://git.ouroath.com/Curveball/tf_training_pipeline/blob/v2/src/offset/tf_runner.py)

Reference

1.  Factorization Machine











----

- Date: 2019-02-05
- Tags: #Interview/Gemini 



