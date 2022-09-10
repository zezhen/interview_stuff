# SparseNN Arch
----


<processor\_type\>{<optional\_arguments\>}(<nested\_arch\>, <sparse\_arch\>) \[<over\_arch\>\]
https://fburl.com/g942hz8o (old version of arch), nested\_arch is next level arch or last dense arch


*   dot(128-64, 74)32-16



1.  Dense Features: 563 raw features for example.
    1.  First fed into FC NN before feeding into next level NN (64-32)
    2.  First\[1\] (or last\[2\]) level dense NN also fed into single-layer NN with 74 nodes (dense feature embedding vector)
    3.  special cases: empty string -> output dense feature w/o any processing; 0 -> no dense feature
    4.  ![[Archive/Machine Learning/_resources/SparseNN_Arch.resources/unknown_filename.png]]
2.  Sparse Features (id-list features)
    1.  First learn embeddings for each id of each sparse feature, 74 dimensions
    2.  Sum all ids' embedding vectors in same feature set to represent this sparse feature
    3.  Do pair-wise dot-product, with dense embedding vectors and got 6 scalars
        1.  \[2\] use sparse embedding self dot-product
    4.  ![[Archive/Machine Learning/_resources/SparseNN_Arch.resources/unknown_filename.1.png]]
3.  Over Arch
    1.  Concatenate 6 scalars from sparse NN with final layer of dense NN (64 vector) and get 70 neuron
    2.  Feed 70 neurons to over arch:  FC + Relu NN structure (32-16)
    3.  The final 16 neurons will then form 1 final node as model prediction
    4.  ResNet is also supported in <over\_arch>. e.g. \[128-64-32\]^3 will construct ResNet 128-64-32-128-64-32-128-64-32-128, where all the 128s are connected using the skip mechanism of ResNet
4.  [Processors](https://our.internmc.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Model_Architecture/Processors) -> [full list](https://our.internmc.facebook.com/intern/diffusion/FBS/browse/master/fbcode/caffe2/caffe2/fb/dper/layer_models/sparse_nn/processor_factory.py)
    1.  [Dot processor](https://our.internmc.facebook.com/intern/diffusion/FBS/browse/master/fbcode/caffe2/caffe2/fb/dper/layer_models/sparse_nn/dot_processor.py): 1) compute embedding of each feature by MLP, 2) compute embedding pair-wise dot products, 3) concat dot products into a vector and feed to over/top arch; some optional parameters:
        1.  embeddings, embedding\_scales, skip\_ids, transfer (default: relu), ==feature fusion==
        2.  [compress\_dot\_products](https://fb.workplace.com/notes/shouyuan-chen/dot-product-matrix-compression-via-learnable-projection/239256290258455/)
            1.  dot processor by default calculates all pairwise dot products between each pair of embedding vector, e.g. 10 sparse features, num\_sparse = 3, plus 1 dense embedding, there will be 31 \* 31 = 961 dot products
            2.  dot\_group can help but need non-trivial human input
            3.  dot product of n embedding vectors (size d) is same as matrix computation, let X be an n\*d matrix, the calculation is XX^T
            4.  we can calculate X(X^Y), where Y is a n\*k matrix, k < n, then the output will be n\*k size vector, the computing complexity drop from O(n^2d) to O(ndk)
            5.  compression method exploits the fact that the dot product matrix XX^T has rank d when d <= n, where d is the dimensionality of embedding vectors. This means that XX^T is a low rank matrix that has O(nd) degree of freedom, instead of O(n^2)
            6.  in theory, we can reduce vectors size from n\*n to n\*d without loss of information, if k < d, it might loss information
        3.  [split\_dense\_input](https://fb.workplace.com/notes/alireza-vahdatpour/an-efficient-way-to-include-more-dense-features-in-ranking-models/338357313585774/): \[400-150-1-512\] [example](https://our.intern.facebook.com/intern/fblearner/run/compare/?baseline_run=70543622&compare_to=73198661&all_runs=70543622%2C73198661)
            1.  if there are lots of dense feature and FC NN will need large size of weights,
            2.  we can split dense feature into k groups first, each group learn part of first layer, can FC with dense arch
            3.  ![[Archive/Machine Learning/_resources/SparseNN_Arch.resources/unknown_filename.2.jpeg]]
    2.  [Unary processor](https://phabricator.intern.facebook.com/diffusion/FBS/browse/master/fbcode/caffe2/caffe2/fb/dper/layer_models/sparse_nn/unary_processor.py): creates a one-dimensional embedding lookup table for each sparse feature, and concatenates the sum of the pooled weights for each sparse feature with the output of the inner nested arch.
        1.  skip\_ids, include\_ids, ==enable\_residual\_learning==
    3.  ==st\_id\_match Processor==: transform sparse features to dense features and concatenate with output of nested arch
        1.  include\_ids
5.  



\[1\] [SparseNN Basics](https://our.internmc.facebook.com/intern/wiki/EntitiesGuide/athens/SparseNN/?vitals_event=wiki_click_navigation_link)

1.  dot(128-64, 74)32-16: learn how Dense and sparse construct the architecture
2.  Multi-Sparse and Multi-Dense, e.g. dot{"num\_sparse": 3}(128-64, 74)32-16
3.  Position-Weighting: dot{"num\_sparse": 2, "pooling\_method": "PositionWeighted\[1,3,5,6,7\]"}(128, 36)128-128
4.  Unary: sigrid transform or unary
5.  Advanced Treatments
    1.  Customized embedding dimension: we can have larger embedding vector for features we think have a lot of latent topics/dimensions
    2.  Heterogeneous Multi-Sparse
    3.  Customized group interactions

\[2\] [the-mysterious-arch-string](https://our.internmc.facebook.com/intern/wiki/Training-sparse-n-n-models-for-feed-ranking/the-mysterious-arch-string/)
\[3\] [Model Architecture (aka "arch")](https://our.internmc.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Model_Architecture/)

----

- Date: 2019-10-29
- Tags: #facebook #machineLearning 



