# SparseNN
----

[Guide to SparseNN](https://our.internmc.facebook.com/intern/wiki/Dper/SparseNNGuide/)

Framework

1.  \*\*[[SparseNN Arch|SparseNN Arch]]
2.  [DPER2 Multi-Task Learning](https://fb.workplace.com/notes/huazhong-ning/dper2-multi-task-learning/350553618716639/)
    1.  input features -> shared layers -> task\_i over layers -> loss/prediction/metrics
    2.  positive\_weight(example weight -> negative downsample rate), bucket\_based
    3.  dedicated layers
    4.  ==label\_weights==: pos\_weight, neg\_weight. One task might be more important than others
    5.  add bias terms
    6.  break-dowm calibrations
    7.  ==dependent tasks== => [A General Dependent Task Framework for MTML flow](https://fb.quip.com/utWaAhn0Iyio)
    8.  gradient on shard: control how much gradients of this task can be back-propagated to the shared layers. 1) sparse feature is pre-train 2) The data of one task need go N > 1 passes, to avoid overfit
3.  [**Attention FM**](https://our.internmc.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/New_Model_Architecture:_Attention_Factorization_Machine_(FM)/): discriminating the importance of feature interactions
4.  [**Sparsely-gated\_Mixture-of-expert\_Models**](https://our.internmc.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Sparsely-gated_Mixture-of-expert_Models/)
5.  
6.  [Multi\_Tower\_SparseNN\_Model](https://our.internmc.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Multi_Tower_SparseNN_Model/)
7.  [Modeling Video-Video Relevance with Two-Tower](https://fb.prod.facebook.com/notes/jing-qian/modeling-video-video-relevance-with-two-tower/239610183478367/)
8.  [Ads\_Ranking\_Modeling\_Infrastructure](https://our.internmc.facebook.com/intern/wiki/Ads_Ranking_Modeling_Infrastructure/)
9.  [SparseNN Delivery Details](https://fb.facebook.com/notes/andrey-malevich/sparsenn-delivery-details/102575797143110/)


Training

1.  [Train SparseNN Model](https://our.internmc.facebook.com/intern/wiki/Training-sparse-n-n-models-for-feed-ranking/reference-for-workflow-configs/?vitals_event=wiki_click_navigation_link)
    1.  talk a bit about reader\_options, model\_options,
    2.  hash\_size is the maximum value for ids used in this sparse NN.
    3.  [sigrid\_transforms](https://our.internmc.facebook.com/intern/diffusion/FBS/browse/master/fbcode/sigrid/lib/transforms/if/transforms.thrift)
        1.  use boosting decision trees as a sparse feature
        2.  position feature for modeling position bias in training data
    4.  meta\_source\_options: feature transforms to normal distribution
    5.  online training: 



Concepts

1.  [Deep Personalization: Learning from Facebook Sparse Data](https://fb.workplace.com/notes/liang-xiong/deep-personalization-learning-from-facebook-sparse-data/10153508038043053) by Liang Xiong 04/21/2016
    1.  Data sparsity is a central problem in ML, using generalizable sparse features, and using embeddings are two important ones of many ways to attach it.
        1.  Generalizable sparse features
            1.  instead of using User ID and Ad ID directly, a better alternative is to use denser, more persistent, and semantically meaningful sparse IDs for representation; for the user, we can represent user as a bag of pages that he/she liked.
            2.  e.g. represent a Ad with the set of keywords fo this Ad, Since keywords live much longer than Ads, we will not lose what we learned in a short time
        2.  Embeddings
            1.  replaces each sparse ID by a short vector (aka latent features/factors), we learn these embeddings from data so that two vectors are close (in terms of geometric distance) if their corresponding sparse IDs are “close” (in terms of semantic similarity)
        3.  \=> [Embedding for Ads Ranking](https://fb.workplace.com/notes/tianshi-gao/embedding-for-ads-ranking/1548206688826990)
    2.  E-P Model
        1.  Embedding: Convert sparse IDs into low dimensional vectors
        2.  Pooling: Merge the set of vectors derived from multiple sparse IDs into a single vector, for easy and cheap processing. average/sum or max-pooling
        3.  The E-P layer will be the key building block for our sparse NN models
        4.  ![[Archive/Machine Learning/_resources/SparseNN.1.resources/unknown_filename.jpeg]]
        5.  Sigrid (Logistic Regression): represent each sparse ID by a single number and do sum-pooling
            1.  ![[Archive/Machine Learning/_resources/SparseNN.1.resources/unknown_filename.1.jpeg]]
        6.  DoubleHelix: embedding + linear pooling, then it explicitly captures the interaction between two entities by the dot product between their representational vectors
            1.  ![[Archive/Machine Learning/_resources/SparseNN.1.resources/unknown_filename.2.jpeg]]
    3.  Key Benefit from NN
        1.  Flexibility: we can put the building blocks together in many different ways (see more architectures in post), use different pooling methods, include more than 2 entities in model, try different ways of capturing interactions between entities, e.g. dot-product, addition, concatenation, multiplication, etc
        2.  since NN is a holistic model, we will able to do end-to-end training of everything together
2.  [SparseNN Modeling 2016 H2 Summary](https://fb.workplace.com/notes/xianjie-chen/deep-personalization-sparsenn-modeling-2016-h2-summary/1222495837858513/) (1/17/2017)
    1.  Xianjie Chen describes quantitative gains to CTR, revenue, etc., also develops the dot-product/grouping ideas from Andrey Malevich's note.
    2.  cover more areas based on #1, including attention based pooling, diagnostic experiments and future work
3.  [SparseNN Models in Ads and NF](https://fb.workplace.com/notes/adnan-aziz/sparsenn-models-in-ads-and-nf-a-quantitative-introduction-for-ai-infra-n00bs/352801795499924/) (01/11/2019) Computational patterns perspective
    1.  Both Ads and News Feed (henceforth, NF) solve the following problem: given a user, find a set of candidates (ads for Ads and posts for NF), and score these candidates using ML models.
        1.  Ads will select a single model based on the ad type, i.e., there are different models for ads that pay for views, clicks, conversions, app installs, etc.
        2.  NF will evaluate multiple models, e.g., for probability of click, like, share, comment, view video for more than 30 seconds, etc., and feed these probabilities to a value model, which assigns different weights to each event. (These weights are set in an ad hoc fashion, and emphasize socially meaningful interactions.)
    2.  Ads: models and compute
        1.  ![[Archive/Machine Learning/_resources/SparseNN.1.resources/unknown_filename.3.jpeg]]
        2.  Embeddings (read more from post)
            1.  sparse features include ads-side one-hot ID (e.g. accout\_id, campaign\_id), length=1, ads-side content (e.g. text tokens, xray hash), length in \[20, 500\], user history lengths of different behaviors (e.g. sparse\_user\_enhaged\_page\_ids, user\_clicked\_campaign\_ids), length is usually truncated at 100, with average around 60
            2.  over 20M pages => 20M wide vector, assume 20M \* 64 matrix and 32fp => 5GB, perform row-wise quantization, each row is quantized separately with a scale and bias, now has size 64+8 bytes => 1.44 GB
        3.  Compute
            1.  AdFinder is using roughly 100K machines, 11M eligible ads, 247K are considered, 67K are matched, 9K are ranked by AdIndexer, 600 are returned
            2.  Of the 19k machines used for training, CPU utilization is 35% and 50% of that is AVX. Low utilization is mainly due to bad scheduling and training jobs are throughput oriented and not latency bound
            3.  A single model (as described above) is trained on 22 machines - many different experiments take place concurrently
                1.  The model is trained end-to-end, i.e., embeddings as well as networks
                2.  Training takes about 5 days
                3.  Of the 22 machines, 10 read the data, 5 run training, and 7 operate as parameter servers
    3.  NF models and compute
        1.  ![[Archive/Machine Learning/_resources/SparseNN.1.resources/unknown_filename.4.jpeg]]
        2.  NF runs multiple ML models (20-30) corresponding to different user actions - click, like, comment, share, watch for more than 30 seconds, etc. The final feed ranking is done by a “value model”, which gives weights to user actions, and computes the weighted sum.
        3.  read more from post, similar to Ads but there are some different or NF specific.
4.  


Followup Readings

*   [Wide & Deep Learning: Better together with TensorFlow](https://ai.googleblog.com/2016/06/wide-deep-learning-better-together-with.html) (6/16) Google blog post - introduces the SparseNN concept, and gives a lot of insight into why SparseNNs work well. (There’s a detailed paper at [ArXiv](https://l.workplace.com/l.php?u=https%3A%2F%2Farxiv.org%2Fabs%2F1606.07792&h=AT0IkBnlszDr2DM30o9gmK1UFCRqwcnZzY3zqIUOfno4GInElqOYd10B-EbbgP6qWPnY6BR0bzOvWUD99jFCKcefu2mfpNO7PetCT-UDoeV828E8P8PPez1yPbuuel5vvzTSXVE6HnixxEALv9Fk5g), but the blog post is more accessible.)
*   [Factorization Machines: Squeezing out more from sparse data](https://fb.workplace.com/notes/andrey-malevich/factorization-machines-squeezing-out-more-from-sparse-data/1088309524539311) (8/16) Andrey Malevich talks to the dot-product operations shown in the schematics.
*   [Layered Cake of Our Models](https://fb.workplace.com/notes/dmytro-dzhulgakov/layered-cake-of-our-models/1613529182292620) (6/16) Dmytro Dzhulgakov's tour de force exposition of models; comprehensive review of notation use by FB AI researchers.
*   [Personalization DL](https://fb.workplace.com/notes/maxim-naumov/personalization-dl-models-services-and-hw-implications/342146156586912/) (12/18) Maxim Naumov talks about Ads models with a focus on accelerators.
*   [Deep Learning with Python](https://l.workplace.com/l.php?u=https%3A%2F%2Fwww.amazon.com%2FDeep-Learning-Python-Francois-Chollet%2Fdp%2F1617294438&h=AT2VvK5BNLmPf9-W0jM8mBMYto3UHsql6ZKOl-If-yTDh83ufbewG0zomcMqo_mvn3iGlDtutfBaBDM132MF7DfVLKwxj9jIUqTlymKHnTQDnfWgU79dHaiIRj4D5Mru5bsPKXlZ3e5k50NLrc0JQA): the vast majority of published accounts of deep learning are on perceptual networks, e.g., CNNs, RNNs, LSTMs, used for vision, speech, text. This book uses Keras (analog to PyTorch) gives a nice account of these networks (with the caveat that such models are qualitatively different from the SparseNN models used for recommendation described in this note).
*   [Distributed Sparse Model Training by Ou Jin](https://fb.workplace.com/notes/ou-jin/distributed-sparse-model-training/1358009504249450) 12/29/2016
*   [Swimming in Sparse NN](https://fb.quip.com/AQHwAeytEow0)
*   [Basics of model architecture (aka](https://our.intern.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Model_Architecture/) ["arch"](https://our.intern.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Model_Architecture/) [in input\_configs) in DPER2](https://our.intern.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Model_Architecture/) and [another guide on arch string](https://our.intern.facebook.com/intern/wiki/Training-sparse-n-n-models-for-feed-ranking/the-mysterious-arch-string/) (beware, it's quite peculiar format)
*   [Serving infra perspective and related architecture choices](https://fb.workplace.com/notes/andrey-malevich/sparsenn-delivery-details/102575797143110/) (by Andrey, 2017)


Related Models -> [Guide to SparseNN](https://our.internmc.facebook.com/intern/wiki/Dper/SparseNNGuide/)

1.  DeepFM
2.  ResNet
3.  BigNN/HugeNN
4.  User-side/ad-side computation
5.  Auto Dense to Sparse
6.  Model-based id matching
7.  Cross Net
    1.  Optimization
    2.  Dot/Cat/Unary Processors
    3.  Dot-processor settings
    4.  Attention pooling methods
    5.  Performance settings
8.  Blob Names
9.  TTSN
10.  Decoupled SparseNN (User-only SparseNN)
11.  MTML












----

- Date: 2019-07-15
- Tags: #facebook #sparseNN #machineLearning 



