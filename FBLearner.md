# FBLearner
----

FB ML Overview
![[Archive/Machine Learning/_resources/FBLearner.resources/unknown_filename.1.png]]

Tutorials

1.  [ML Academy Lab: Train a search ranking model](https://our.internmc.facebook.com/intern/wiki/ML_Academy_Lab/) => copy flow, run一下, 对model train/workflow 有个大致的了解, 需要自己手动做一个
    1.  Train a LambdaMART model
    2.  Train with Super/Submodel
    3.  Parameter Sweeping
2.  [Predicting\_User\_Churn](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Getting_Started_with_Flow/Tutorial_-_Predicting_User_Churn)
    1.  prepare data (e.g. format: label, features: map<field, value>, ds, type: train or test) in hive or somewhere else, dataswarm pipeline is helpful here
    2.  create or clone a workflow, change the parameters if necessary, then run
        1.  check more from [Trainer API](https://our.internmc.facebook.com/intern/fblearner/docs/workflow/training.trainer.Trainer/) or [train.py](https://phabricator.internmc.facebook.com/diffusion/FBS/browse/master/fbcode/fblearner/flow/projects/training/trainer.py)
    3.  evaluate the results, e.g. ROC, precision recall curve, feature stats, or model introspection, 
    4.  optimize model by using parameter sweep => GridSearch
    5.  Use model
        1.  live prediction: query the model through [FBLearner Predictor](https://our.intern.facebook.com/intern/dex/fblearner-predictor/), which is querying directly from WWW
        2.  batch prediction: collect data in a hive and run prediction workflow, can use [Hive Evaluation Workflow](https://our.intern.facebook.com/intern/fblearner/docs/workflow/evaluators.hive_evaluation.Workflow/)
    6.  Recurring training
3.  [Hello World](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Getting_Started_with_Flow/Hello_World/)
    1.  write basic workflow using python, submit using flow-cli command


[ML\_Algorithms](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/ML_Algorithms/?vitals_event=wiki_click_navigation_link)

1.  Asimo: a set of tools to ease and automate the process of feature selection and feature removal
    1.  based on boosting tree features importance, set a threshold to cut the features who importances are below that
2.  GBDT
    1.  Feature selection based on <Gradient Boosted Feature Selection\> kdd'14
3.  LR
4.  Sigrid (large scale LR) -> [[SparseNN.md|SparseNN]]
5.  StarSpace: train embeddings for entities within subsets of Facebook's social graphs


Training

1.  [Flow](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/?vitals_event=wiki_click_navigation_link) (some important sections list below)
    1.  [Creating\_a\_Workflow/Author\_Guide](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Creating_a_Workflow/Author_Guide)
        1.  [Author\_Guide(how to write your own workflow)](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Creating_a_Workflow/Author_Guide/?vitals_event=wiki_click_navigation_link)
        2.  [Builds\_in\_FBLearner\_Flow](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Creating_a_Workflow/Author_Guide/Builds_in_FBLearner_Flow/?vitals_event=wiki_click_navigation_link)
    2.  [Flow\_Oncall\_and\_Troubleshooting](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Flow_Oncall_and_Troubleshooting/?vitals_event=wiki_click_navigation_link)
    3.  [Publishing\_a\_Workflow](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Publishing_a_Workflow/?vitals_event=wiki_click_navigation_link)
    4.  [Running\_Deep\_Learning\_Models\_on\_FBLearner](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Running_Deep_Learning_Models_on_FBLearner/)
    5.  ![[Archive/Machine Learning/_resources/FBLearner.resources/unknown_filename.png]][flow-architecture](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Getting_Started_with_Flow/flow-architecture/?vitals_event=wiki_click_navigation_link)
    6.  [Flow\_N00b\_Resources](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Getting_Started_with_Flow/Flow_N00b_Resources/)
2.  [Fluent2](https://our.intern.facebook.com/intern/dex/fluent2/): a declarative ML framework for training models (uses Flow under the hood)
    1.  combine different models to solve practical problems, one of the ways to interface with Flow. 
    2.  [What Kind of Place Is This?](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Author_Guide/Fluent2_-_A_Place_Prediction_Tutorial/Looking_Under_the_Hood/) 
3.  [AutoML](https://our.internmc.facebook.com/intern/wiki/AutoML/): hyper-parameter tuning
4.  Deep Personalization (aka DPer)
    
    1.  [Model Architecture (aka "arch")](https://our.internmc.facebook.com/intern/wiki/Deep_Personalization_(aka_DPer)/Model_Architecture/?vitals_event=wiki_click_breadcrumb_direct_link)


Data & Features

1.  [Feature Store](https://our.intern.facebook.com/intern/dex/feature-store/)
    1.  Reuse common features
    2.  [Using the feature store to predict Facebook age](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Author_Guide/ML_Academy/) 
2.  [Dataswarm](https://our.internmc.facebook.com/intern/wiki/Dataswarm/%20)
    1.  Where is the data? iData 
    2.  How to query data? [Daiquery](https://our.internmc.facebook.com/intern/wiki/Daiquery-tutorial/)
    3.  How to run pipeline? DataswarmStudio, Dataswarm
        1.  If one query needs two tables from different, use the namespace with large data, as it will move another namespace's data to this.
    4.  Some other tools:
        1.  Uhaul: move data from one namespace to another
3.  [FBJoiner](https://our.intern.facebook.com/intern/dex/fbjoiner/): a service to join features and events in order to generate labelled data for ML training
4.  [UFF](https://our.internmc.facebook.com/intern/wiki/Uff/): computing features by aggregating events


Preditor/Inference

1.  [Inference Platform](https://our.intern.facebook.com/intern/dex/fblearner-predictor/): AI Infra Inference Platform provides a managed environment for hosting and serving ml models in production


All-in-One

1.  [Loopers](https://our.intern.facebook.com/intern/dex/looper/) 
    1.  based on Fluent2, only support GBDT now 
2.  [FBMLKit](https://our.intern.facebook.com/intern/dex/fbmlkit/): Looper for mobile


Specialized Applications

1.  [TexAS](https://our.intern.facebook.com/intern/dex/text-as-service/) - Text As a Service
    1.  Tutorial: [CLUE for the Clueless: an intro to ML, CLUE, and text prediction](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/User_Guide/CLUE_for_the_Clueless/)
    2.  Tutorial: [What is this Status Update About: an Intro to FBLearner Flow](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Introduction_to_Machine_Learning_by_Use_Case_Example/What_is_this_Status_Update_About_:_an_Intro_to_FBLearner_Flow/)
    3.  [Training DocNN](https://our.intern.facebook.com/intern/dex/training-doc-nn/) 
2.  [X-RAY](https://our.intern.facebook.com/intern/dex/xray/) -- image feature detection
    1.  [Predicting User Churn](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/User_Guide/Predicting_User_Churn/) 
3.  [Lumos](https://our.intern.facebook.com/intern/dex/lumos/) : Content Understanding Platform (<- [CLUE](https://our.internmc.facebook.com/intern/wiki/FBLearner_and_Family/Flow/Advanced_Flow_Models/CLUE_for_the_Clueless/))
    1.  Use X-Ray to generate/create features, then it uses these features for classifying flower by finding which features make up a flower  
4.  [ActivationVis: Caffe2](https://our.internmc.facebook.com/intern/wiki/Fblearner-activationvis/)
5.  [Census](https://our.internmc.facebook.com/intern/wiki/Census/)
6.  PYSF
7.  Segmentation/ GAN#
8.  Spark/ Plasma Operator
9.  PVC



----

- Date: 2019-06-24
- Tags: #facebook #machineLearning 



