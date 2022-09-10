# Data Partitioning/Sharding
----


For the tweets in twitter system or newsfeed in Facebook, we need to partition data into multiple hosts, how to evenly distribute the large scale of data is key point.

Functions
Here is some functions for tweets system:

1.  Users can post tweets
2.  One user can follow other users
3.  In one user’s stream, he/she can see his/her own tweets and his/her followings’ tweets, order by some weights, like timestamp, likeness, etc
4.  Users can visit other users’ profiles, where will show their information (alias, description, follower #, following #, tweets desc order by post time, etc)
5.  Once one user post a tweet, it can be seen by his/her followers, in some way as followers’ preference, e.g. notify them directly (push), or wait user ask for updates (pull)


QPS/Data Volume
(omitted here)

Design


1.  Database Schema


user table: id (PK), name, email, description, follower #, following #, etc
tweet table: id (PK), user\_id, timestamp, text, image\_urls, video\_url
following table: follower\_id (PK), following\_id, timestamp
user\_tweet\_table: user\_id (PK), timestamp (clustering key), tweet\_id (or keep in cache)


2.  Data Partition/Sharding


user and following tables are partitioned by user id, one user’s profile and following information will be distributed one host.
tweet table is partitioned by tweet id, so that tweet can be distributed evenly in clusters.
user\_tweet\_table is partition by user id, timestamp is clustering key for range query (sorted)

Some scenarios for system functions.

1.  Posting tweets
    1.  application server receive text/image/video, after load balancing (round robin)
    2.  image and video will be stored into BlobStorage and get urls (data partition and cache before storage are plus)
    3.  tweet id, user\_id, text, timestamp, image\_urls, video\_url will insert into tweet table and user\_tweet\_table
    4.  Send tweet information to notification server in case need push to followers immediately or push to followers timeline queue (fanout)
        1.  for the celebrity, like Justin Bieber, we can switch to pull mode (timer)
2.  Stream/Tweets building/ranking server
    1.  User login request or periodically pre-build users’ steam, this server will fetch user following user ids.
    2.  Query followings’ tweets in some period time, and get the tweets id, 
        1.  Consider one’s following # won’t exceed 10k, this process is efficient, e.g. Cassandra can use parallel queries
        2.  In batch mode, we query user\_tweet\_table in all hosts for the tweets in past period time, then fetch tweets accordingly. (or only fetch frequent login users)
        3.  or we can create latest\_tweets\_cache or table to keep last period tweets, so we don’t have scan two much parallel queries
    3.  Ranking tweets based on some weights => [[Facebook NewsFeed Ranking|Facebook NewsFeed Ranking]]
    4.  Put ranked feeds into cache for user’s future fetch or notify application server to fetch top k feeds (async) or push feeds to application server (sync)
3.  User visits another user’s profile
    1.  fetch this user’s tweets from user\_tweet\_table or some caching, then query all these tweets (caching popular user’s profile is plus)
4.  Tweet notification according to users’ preference
    1.  in #1.4, application server can trigger notification server in short period after tweet posted
    2.  or notification server can periodically fetch latest tweets from user\_tweet\_table or latest\_tweets\_cache
5.  latest\_tweets\_table
    1.  tweet id can be timestamp + count
    2.  latest\_tweets\_table is the key order by ByteOrderedPartitioner


[Twitter System Design](https://www.youtube.com/watch?v=wYk0xPP_P_8&t=0s&index=21&list=WL)



----

- Date: 2019-01-16
- Tags: #note #Interview/System-Design 



