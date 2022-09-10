# Facebook NewsFeed Ranking
----

**EdgeRank**

1.  EdgeRank is the Facebook algorithm that decides which stories appear in each user's newsfeed. The algorithm hides boring stories, so if your story doesn't score well, no one will see it. As of _2011, Facebook has **stopped** using the EdgeRank system_ and uses a [machine learning](https://en.wikipedia.org/wiki/Machine_learning) algorithm that, as of 2013, takes more than 100,000 factors into account.
2.  Every action their friends take is a potential newsfeed story. Facebook calls these actions "Edges." That means whenever a friend posts a status update, comments on another status update, tags a photo, joins a fan page, or RSVP's to an event it generates an "Edge," and a story about that Edge might show up in the user's personal newsfeed.
3.  Features
    1.  Affinity Score
        1.  It means how "connected" a particular user is to the Edge
        2.  Facebook calculates affinity score by looking at explicit actions that users take, and factoring in 
            1.  the strength of the action, 
            2.  how close the person who took the action was to you, 
            3.  how long ago they took the action.
        3.  Explicit actions include commenting > liking > clicking, tagging, sharing, and friending
        4.  It’s one-wa
    2.  Edge Weight
        1.  Each category of edges has a different default weight, e.g photos and videos have a higher weight than links
    3.  Time Decay
        1.  Facebook is just multiplying the story by 1/x, where x is the time since the action happened. This may be a linear decay function, or it may be exponential like (1-r)^x
    4.  ![[Archive/Machine Learning/_resources/Facebook_NewsFeed_Ranking.resources/unknown_filename.png]]



ML Modeling

1.  Objective: For a user u, given a list of posts p, how should we ranking p, so that we can show top k posts to user, considering p is large.
2.  Proposal 1:
    1.  For the history training data, we can scoring different actions
        1.  follow/friend 50, 
        2.  send message/share 40
        3.  comment 20
        4.  like 5
        5.  click/save/‘view video’ as 1
        6.  ‘view’ only can be 0, 
        7.  unfollow/hide/unfriend  -100
    2.  Then we can predict whether likeness of user to this post, when rank the higher likeness posts with higher score
    3.  We can use GBDT (multi-target regression trees) or Offset to modeling it
    4.  Follower's features:
        1.  follower\_id, follower #, following #
        2.  click\_propensity: how frequently or the confident that he/she will click based on views
        3.  like\_propensity: how frequently or the confident that he/she will like
        4.  comment\_propensity: how frequently or the confident that he/she will comment
    5.  Post Features:
        1.  post\_id, poster\_id, poster’s follower #, poster’s following #, poster’s category
        2.  image #, video #, test length, 
        3.  hashtag 
        4.  like #, comment #
    6.  Time features
        1.  decay\_function(view time - post time)
        2.  hour of day, day of week, day of month, 
    7.  Interaction Features
        1.  likes times #, comment times #, 
        2.  likes times %, comment times %, 
        3.  revesed\_likes #, reversed\_comment #
        4.  common friends/follower #
        5.  common friends/follower like/comment # on post
        6.  is\_following\_each\_other
    8.  Feedback Features
        1.  EC(expected click), COEC (click on EC)
        2.  EL/LOEL (like, comment, ...)
3.  Model for Instagram Discover
    1.  two steps: first collect post candidates, then ranking using same model above #2
    2.  how to collect data:
        1.  CF based content
        2.  How to discover old post? depend on someone view followers’ profile and unearth old posts based on their actions.
        3.  Randomly select some posts from users, based on their image/description/hashtag
4.  [Facebook Sharing](https://www.youtube.com/watch?v=iXKR3HE-m8c)
    1.  Boot Decision Tree 
        1.  Start with over > 100k (dense) features
        2.  Prune to top ~2K: too much features need large training and runtime time
        3.  Historical counts and propensity are some of the strongest features
    2.  Logistic Regression
        1.  simple, fast and easy to distribute
    3.   Stacking: Combined Tree + LR
        1.  BDT -> feature selection
        2.  ![[Archive/Machine Learning/_resources/Facebook_NewsFeed_Ranking.resources/unknown_filename.1.png]]
    4.  Neural Network + Sparse features
        1.  NN: discard final layer, use final layer outputs as features
        2.  sparse features, such as text or content id
        3.  ![[Archive/Machine Learning/_resources/Facebook_NewsFeed_Ranking.resources/unknown_filename.2.png]]‘’
    5.   Measurement
        1.  Engegement, e.g. Click, Like
        2.  Longitudinal metrics, e.g. dwell time, abandonment
        3.  Quality: survey score
            1.  Pairwise comparison survey
            2.  In or out Survey
            3.  Rating Survey



Reference

*   http://edgerank.net/
*   [Moving Beyond EdgeRank for Personalized News Feeds](https://codeburst.io/moving-beyond-edgerank-for-personalized-news-feeds-a2cf3fdf2fa7)
*   [Ewa Dominowska — Generating a Billion Personal News Feeds — MLconf SEA 2016](https://www.youtube.com/watch?v=iXKR3HE-m8c)



----

- Date: 2019-02-03
- Tags: #machineLearning 



