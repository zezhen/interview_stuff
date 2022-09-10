# NoSQL数据库笔谈
----

# NoSQL数据库笔谈

[databases](http://sebug.net/paper/databases/) , [appdir](http://sebug.net/appdir/) , [node](http://sebug.net/node/) , [paper](http://sebug.net/paper/)[颜开](http://www.yankay.com/) , v0.2 , 2010.2

1.  [序](http://sebug.net/paper/databases/nosql/Nosql.html#_3648342117667198_092538481578)
    
    1.  [CAP](http://sebug.net/paper/databases/nosql/Nosql.html#CAP_7730791447684169_231516710)
        1.  [变体](http://sebug.net/paper/databases/nosql/Nosql.html#_688371617347002_0840630698949)
    2.  [BASE](http://sebug.net/paper/databases/nosql/Nosql.html#BASE_9958890723064542_78222997_869969945038222)
        1.  [I/O的五分钟法则](http://sebug.net/paper/databases/nosql/Nosql.html#I_O_9886723485627446_373115905_5228612841633498)
        2.  [不要删除数据](http://sebug.net/paper/databases/nosql/Nosql.html#_8314717379700977_930601348298)
        3.  [RAM是硬盘,硬盘是磁带](http://sebug.net/paper/databases/nosql/Nosql.html#RAM_147097721381792_7902793153_006425076106569838)
        4.  [Amdahl定律和Gustafson定律](http://sebug.net/paper/databases/nosql/Nosql.html#Amdahl_Gustafson_9052423372139)
        5.  [万兆以太网](http://sebug.net/paper/databases/nosql/Nosql.html#_5841810574932209)
    
    1.  [亚马逊的现状](http://sebug.net/paper/databases/nosql/Nosql.html#_735276508313792_2270315258144_9783657311654288)
    2.  [算法的选择](http://sebug.net/paper/databases/nosql/Nosql.html#_6454406003627595_776185765138)
    
2.  [Quorum NRW](http://sebug.net/paper/databases/nosql/Nosql.html#NRW_012323816604251636_2127662_10272764961707637)
3.  [Vector clock](http://sebug.net/paper/databases/nosql/Nosql.html#Vector_clock_41690548602491617_5257623065741377)
4.  [Virtual node](http://sebug.net/paper/databases/nosql/Nosql.html#Virtual_node_6496471269056201_)
    1.  [Gossip (State Transfer Model)](http://sebug.net/paper/databases/nosql/Nosql.html#Gossip_State_Transfer_Model_14_5181318348909955)
    2.  [Gossip (Operation Transfer Model)](http://sebug.net/paper/databases/nosql/Nosql.html#Gossip_Operation_Transfer_Mode_688725990810297)
5.  [Merkle tree](http://sebug.net/paper/databases/nosql/Nosql.html#Merkle_tree_26526400726288557__5335256577035526)
    1.  [背景](http://sebug.net/paper/databases/nosql/Nosql.html#_08464202471077442_91161458194)
6.  [DHT](http://sebug.net/paper/databases/nosql/Nosql.html#_DHT_1358780225498577_43241378_3858325568533115)
7.  [Map Reduce Execution](http://sebug.net/paper/databases/nosql/Nosql.html#Map_Reduce_Execution_846077151)
8.  [Handling Deletes](http://sebug.net/paper/databases/nosql/Nosql.html#Handling_Deletes_5351970902357)
9.  [存储实现](http://sebug.net/paper/databases/nosql/Nosql.html#_9441494032710129_695390093706)
10.  [节点变化](http://sebug.net/paper/databases/nosql/Nosql.html#_6926584525683441_048149148503_6730095064772663)
    1.  [描述](http://sebug.net/paper/databases/nosql/Nosql.html#_9307460655327144_814779051211_16340782010495503)
    2.  [特点](http://sebug.net/paper/databases/nosql/Nosql.html#_0735241653420401_214353696530_10910972604729818)

1.  [特点](http://sebug.net/paper/databases/nosql/Nosql.html#_5715430571410516_795932562480_594496466269948)
2.  [内存分配](http://sebug.net/paper/databases/nosql/Nosql.html#_30675244504305366_58003565301_10183704247790026)
3.  [缓存策略](http://sebug.net/paper/databases/nosql/Nosql.html#_25401546959033316_54044164260_21550351004030177)
4.  [缓存数据库查询](http://sebug.net/paper/databases/nosql/Nosql.html#_9681760638005524_476574154195_29919331639865443)
5.  [数据冗余与故障预防](http://sebug.net/paper/databases/nosql/Nosql.html#_24413638147967254_17374089581)
6.  [Memcached客户端（mc）](http://sebug.net/paper/databases/nosql/Nosql.html#Memcached_mc_4754505836919398_)
7.  [缓存式的Web应用程序架构](http://sebug.net/paper/databases/nosql/Nosql.html#_Web_06299667034235767_0770205)
8.  [性能测试](http://sebug.net/paper/databases/nosql/Nosql.html#_2923975010491904_991216856614_6695281938071784)

1.  [Memcached 和 dbcached 在功能上一样吗?](http://sebug.net/paper/databases/nosql/Nosql.html#Memcached_dbcached_80228012544_7159779747569146)

1.  [Hadoop之Hbase](http://sebug.net/paper/databases/nosql/Nosql.html#Hadoop_Hbase_7008211932696602_)
2.  [耶鲁大学之HadoopDB](http://sebug.net/paper/databases/nosql/Nosql.html#_HadoopDB_694108467096603_8508)
3.  [GreenPlum](http://sebug.net/paper/databases/nosql/Nosql.html#GreenPlum_9589918625911178_389_2571204937078031)
    1.  [Cassandra特点](http://sebug.net/paper/databases/nosql/Nosql.html#Cassandra_7570848905089025_855)
    2.  [Keyspace](http://sebug.net/paper/databases/nosql/Nosql.html#Keyspace_4281837751378973_7779)
    3.  [Column family（CF）](http://sebug.net/paper/databases/nosql/Nosql.html#Column_family_CF_7300188887469)
    4.  [Key](http://sebug.net/paper/databases/nosql/Nosql.html#Key_8652924433729429_945524073)
    5.  [Column](http://sebug.net/paper/databases/nosql/Nosql.html#Column_7210506089658316_137983)
    6.  [Super column](http://sebug.net/paper/databases/nosql/Nosql.html#Super_column_7509394918740693__5465405669459864)
    7.  [Sorting](http://sebug.net/paper/databases/nosql/Nosql.html#Sorting_02237180483759471_3623)
    8.  [存储](http://sebug.net/paper/databases/nosql/Nosql.html#_9140782690107976_782512314168_5668600168551156)
    9.  [API](http://sebug.net/paper/databases/nosql/Nosql.html#API_26318602548081826_11761206)
4.  [Google之BigTable](http://sebug.net/paper/databases/nosql/Nosql.html#Google_BigTable_89699097442012_4732490241509013)
    1.  [特点](http://sebug.net/paper/databases/nosql/Nosql.html#_277640536666413_1438417866912_5870416136781664)
        1.  [Record-level mastering 记录级别主节点](http://sebug.net/paper/databases/nosql/Nosql.html#Record_level_mastering_5517762_46835816908332717)
        2.  [PNUTS的结构](http://sebug.net/paper/databases/nosql/Nosql.html#PNUTS_8107177845815062_9043074_09676675858475725)
        3.  [Tablets寻址与切分](http://sebug.net/paper/databases/nosql/Nosql.html#Tablets_42011614117692475_6287_8740690747386985)
        4.  [Write调用示意图](http://sebug.net/paper/databases/nosql/Nosql.html#Write_09715737083689369_039670_4594814468066295)
    2.  [PNUTS感悟](http://sebug.net/paper/databases/nosql/Nosql.html#PNUTS_232566011293608_85456655)
5.  [微软之SQL数据服务](http://sebug.net/paper/databases/nosql/Nosql.html#_SQL_014314330249305951_274686)

3.  [非云服务竞争者](http://sebug.net/paper/databases/nosql/Nosql.html#_5549467765717498_055917970185)
    
    1.  [特性](http://sebug.net/paper/databases/nosql/Nosql.html#id3_7125310846245526_994698240_046846452482873)
    
    2.  [Riak](http://sebug.net/paper/databases/nosql/Nosql.html#Riak_22101400413903483_0979197)
    3.  [MongoDB](http://sebug.net/paper/databases/nosql/Nosql.html#MongoDB_6119060613540953_36142)
    4.  [Terrastore](http://sebug.net/paper/databases/nosql/Nosql.html#Terrastore_9954661491866293_58)
    5.  [ThruDB](http://sebug.net/paper/databases/nosql/Nosql.html#ThruDB_380390167243812_4644251)
    
    1.  [Amazon之SimpleDB](http://sebug.net/paper/databases/nosql/Nosql.html#Amazon_SimpleDB_52017362120027_8392263913000672)
    2.  [Chordless](http://sebug.net/paper/databases/nosql/Nosql.html#Chordless_5471036441883179_507)
    3.  [Redis](http://sebug.net/paper/databases/nosql/Nosql.html#Redis_5387336107639441_6223163)
    4.  [Scalaris](http://sebug.net/paper/databases/nosql/Nosql.html#Scalaris_7621760337337995_5287)
    5.  [Tokyo cabinet / Tyrant](http://sebug.net/paper/databases/nosql/Nosql.html#Tokyo_cabinet_Tyrant_545688958_7406684038893259)
    6.  [CT.M](http://sebug.net/paper/databases/nosql/Nosql.html#CT_M_9097645017290603_52052040)
    7.  [Scalien](http://sebug.net/paper/databases/nosql/Nosql.html#Scalien_704454814757133_326936)
    8.  [Berkley DB](http://sebug.net/paper/databases/nosql/Nosql.html#Berkley_DB_9606079710191457_91)
    9.  [MemcacheDB](http://sebug.net/paper/databases/nosql/Nosql.html#MemcacheDB_06512137876498592_4)
    10.  [Mnesia](http://sebug.net/paper/databases/nosql/Nosql.html#Mnesia_9154183157888259_898783)
    11.  [LightCloud](http://sebug.net/paper/databases/nosql/Nosql.html#LightCloud_823765875537818_453)
    12.  [HamsterDB](http://sebug.net/paper/databases/nosql/Nosql.html#HamsterDB_05420895958151517_68)
    13.  [Flare](http://sebug.net/paper/databases/nosql/Nosql.html#Flare_8050426165277293_5400566_5744763652908157)
    
    1.  [功能特色](http://sebug.net/paper/databases/nosql/Nosql.html#_5504176676028282_249060984314_6205024527039867)
    2.  [架构特色](http://sebug.net/paper/databases/nosql/Nosql.html#_3991007534787059_800100618042)
    
    1.  [简介](http://sebug.net/paper/databases/nosql/Nosql.html#_855878707383143_0006899688354_7439637158723382)
    2.  [更新](http://sebug.net/paper/databases/nosql/Nosql.html#_8856209489372642_306660973986_09293410042228067)
    3.  [特性](http://sebug.net/paper/databases/nosql/Nosql.html#_5668651611345044_858602237877_6976689272639188)
    4.  [性能](http://sebug.net/paper/databases/nosql/Nosql.html#_25480733904987574_39869615321)
    
    1.  [两个设计上的Tips](http://sebug.net/paper/databases/nosql/Nosql.html#_Tips_7329128378643512_0444030_21084614206097596)
    
    4.  [Voldemort](http://sebug.net/paper/databases/nosql/Nosql.html#Voldemort_09926958376271466_23_3723235398029888)
    5.  [Dynomite](http://sebug.net/paper/databases/nosql/Nosql.html#Dynomite_9324181654488122_3155)
    6.  [Kai](http://sebug.net/paper/databases/nosql/Nosql.html#Kai_8461184647175368_911329902)
    
    1.  [Skynet](http://sebug.net/paper/databases/nosql/Nosql.html#Skynet_9220649347100478_689227)
    2.  [Drizzle](http://sebug.net/paper/databases/nosql/Nosql.html#Drizzle_9847466828815841_11171_39190645551632586)
    
    1.  [可扩展性](http://sebug.net/paper/databases/nosql/Nosql.html#_10969047341495752_68719353526)
    2.  [数据和查询模型](http://sebug.net/paper/databases/nosql/Nosql.html#_587794222868979_1359147783368_00199023178757618)
    3.  [持久化设计](http://sebug.net/paper/databases/nosql/Nosql.html#_23622012604027987_99347529746_4971976801014726)

1.  [eBay 架构经验](http://sebug.net/paper/databases/nosql/Nosql.html#eBay_7439944222569466_24644076_7816704294788374)
2.  [淘宝架构经验](http://sebug.net/paper/databases/nosql/Nosql.html#_7241636626422405_709893183782_6238797470731577)
3.  [Flickr架构经验](http://sebug.net/paper/databases/nosql/Nosql.html#_Flickr_11598328692846749_1352)
    
    1.  [Metrics](http://sebug.net/paper/databases/nosql/Nosql.html#_Metrics_44020236287486847_696)
    2.  [配置管理](http://sebug.net/paper/databases/nosql/Nosql.html#_6825445668030796_760233095682)
    3.  [Darkmode](http://sebug.net/paper/databases/nosql/Nosql.html#Darkmode_5259184612638798_9242_24315166669659272)
    4.  [进程管理](http://sebug.net/paper/databases/nosql/Nosql.html#_15026388981903727_49114302769)
    5.  [硬件](http://sebug.net/paper/databases/nosql/Nosql.html#_0638721247682108_828753285625)
    
    1.  [Review制度](http://sebug.net/paper/databases/nosql/Nosql.html#_Review_2868290775437222_09924_496206508469592)
    2.  [部署管理](http://sebug.net/paper/databases/nosql/Nosql.html#_9450378125913654_306697729191)
    3.  [团队沟通](http://sebug.net/paper/databases/nosql/Nosql.html#_9827601284285629_932863057418_1654637779888143)
    
    3.  [Cache](http://sebug.net/paper/databases/nosql/Nosql.html#Cache_7188110122840438_8250995)
4.  [云计算架构](http://sebug.net/paper/databases/nosql/Nosql.html#_7156457947548296_394763811409)
    
    1.  [单点失败（Single Point of Failure）](http://sebug.net/paper/databases/nosql/Nosql.html#1_Single_Point_of_Failure_0747)
    2.  [同步调用](http://sebug.net/paper/databases/nosql/Nosql.html#2_4706029240041971_38065281044)
    3.  [不具备回滚能力](http://sebug.net/paper/databases/nosql/Nosql.html#3_2901653153821826_08160938974)
    4.  [不记录日志](http://sebug.net/paper/databases/nosql/Nosql.html#4_6656234869733453_99668187927)
    5.  [无切分的数据库](http://sebug.net/paper/databases/nosql/Nosql.html#6_27202645502984524_3263167534)
    6.  [无切分的应用](http://sebug.net/paper/databases/nosql/Nosql.html#7_1922687441110611_96343139093)
    7.  [将伸缩性依赖于第三方厂商](http://sebug.net/paper/databases/nosql/Nosql.html#8_03636558633297682_8496042666)
    
    1.  [OLAP报表产品最大的难点在哪里？](http://sebug.net/paper/databases/nosql/Nosql.html#OLAP_4599690049262246)
    
    1.  [假设失效是必然发生的](http://sebug.net/paper/databases/nosql/Nosql.html#_8299268803807944)
    2.  [对数据进行分区](http://sebug.net/paper/databases/nosql/Nosql.html#_3399782225793654)
    3.  [保存同一数据的多个副本](http://sebug.net/paper/databases/nosql/Nosql.html#_6817497787365963)
    4.  [动态伸缩](http://sebug.net/paper/databases/nosql/Nosql.html#_41232823879475633)
    5.  [查询支持](http://sebug.net/paper/databases/nosql/Nosql.html#_4374214008737275)
    6.  [使用 Map/Reduce 处理汇聚](http://sebug.net/paper/databases/nosql/Nosql.html#_Map_Reduce__0618697512503632)
    7.  [基于磁盘的和内存中的实现](http://sebug.net/paper/databases/nosql/Nosql.html#_7409241799750766)
    8.  [仅仅是炒作?](http://sebug.net/paper/databases/nosql/Nosql.html#_147455643042405)

1.  [感谢](http://sebug.net/paper/databases/nosql/Nosql.html#_2173698448339071_054548149739)
2.  [版本志](http://sebug.net/paper/databases/nosql/Nosql.html#_6935117091385137_745914644052_9642310538889594)
3.  [引用](http://sebug.net/paper/databases/nosql/Nosql.html#_4067787453532219_249561086297_6469049028134853)



# 序

日前国内没有一套比较完整的NoSQL数据库资料，有很多先驱整理发表了很多，但不是很系统。不材尝试着将各家的资料整合一下，并书写了一些自己的见解。本书写了一些目前的NoSql的一些主要技术，算法和思想。同时列举了大量的现有的数据库实例。读完全篇，相信读者会对NoSQL数据库了解个大概。另外我还准备开发一个开源内存数据库galaxydb.本书也是为这个数据库提供一些架构资料。

# 

## 

[Brewer's CAP Theorem](http://www.julianbrowne.com/article/viewer/brewers-cap-theorem)


## 

### 

## 

## 

### 

[Jim Gray](http://en.wikipedia.org/wiki/Jim_Gray_%28computer_scientist%29) 与 Gianfranco Putzolu 发表了这个"五分钟法则"的观点，简而言之，如果一条记录频繁被访问，就应该放到内存里，否则的话就应该待在硬盘上按需要再访问。这个临界点就是五分钟。 看上去像一条经验性的法则，实际上五分钟的评估标准是根据投入成本判断的，根据当时的硬件发展水准，在内存中保持 1KB 的数据成本相当于硬盘中存据 400 秒的开销(接近五分钟)。这个法则在 1997 年左右的时候进行过一次回顾，证实了五分钟法则依然有效（硬盘、内存实际上没有质的飞跃)，而这次的回顾则是针对 SSD 这个"新的旧硬件"可能带来的影响。
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.45.gif]]随着闪存时代的来临，五分钟法则一分为二：是把 SSD 当成较慢的内存（extended buffer pool ）使用还是当成较快的硬盘（extended disk）使用。小内存页在内存和闪存之间的移动对比大内存页在闪存和磁盘之间的移动。在这个法则首次提出的 20 年之后，在闪存时代，5 分钟法则依然有效，只不过适合更大的内存页(适合 64KB 的页，这个页大小的变化恰恰体现了计算机硬件工艺的发展，以及带宽、延时)。


### 

### 

[Jim Gray](http://research.microsoft.com/~Gray/JimGrayHomePageSummary.htm)在过去40年中对技术发展有过巨大的贡献，“内存是新的硬盘，硬盘是新的磁带”是他的名言。“实时”Web应用不断涌现，达到海量规模的系统越来越多，这种后浪推前浪的发展模式对软硬件又有何影响？[Tim Bray](http://www.tbray.org/ongoing/)早在网格计算成为热门话题之前，就[讨论过](http://www.tbray.org/ongoing/When/200x/2006/05/24/On-Grids)以RAM和网络为中心的硬件结构的优势，可以用这种硬件建立比磁盘集群速度更快的RAM集群。

> 对于数据的随机访问，内存的速度比硬盘高几个数量级（即使是最高端的磁盘存储系统也只是勉强达到1,000次寻道/秒）。其次， 随着数据中心的网络速度提高，访问内存的成本更进一步降低。通过网络访问另一台机器的内存比访问磁盘成本更低。就在我写下这段话的时候，Sun的 Infiniband产品线中有一款具备9个全互联非阻塞端口交换机，每个端口的速度可以达到30Gbit/sec！Voltaire产品的端口甚至更多；简直不敢想象。（如果你想了解这类超高性能网络的最新进展，请关注Andreas Bechtolsheim在Standford开设的课程。）

各种操作的时间，以2001年夏季，典型配置的 1GHz 个人计算机为标准：

|     |     |
| --- | --- |
| 执行单一指令 | 1 纳秒 |
| 从L1 高速缓存取一个字 | 2 纳秒 |
| 从内存取一个字 | 10 纳秒 |
| 从磁盘取连续存放的一个字 | 200 纳秒 |
| 磁盘寻址并取字 | 8 毫秒 |
| 以太网 | 2GB/s |

Tim还指出Jim Gray的名言中后半句所阐述的真理：“对于随机访问，硬盘慢得不可忍受；但如果你把硬盘当成磁带来用，它吞吐连续数据的速率令人震惊；它天生适合用来给以RAM为主的应用做日志（logging and journaling）。” 时间闪到几年之后的今天，我们发现硬件的发展趋势在RAM和网络领域势头不减，而在硬盘领域则止步不前。Bill McColl提到用于并行计算的[海量内存系统已经出现](http://www.computingatscale.com/?p=54)：

> 内存是新的硬盘！硬盘速度提高缓慢，内存芯片容量指数上升，in-memory软件架构有望给各类数据密集的应用带来数量级的性能提升。小型机架服务器（1U、2U）很快就会具备T字节、甚至更大量的内存，这将会改变服务器架构中内存和硬盘之间的平衡。硬盘将成为新的磁带，像磁带一样作为顺序存储介质使用（硬盘的顺序访问相当快速），而不再是随机存储介质（非常慢）。这里面有着大量的机会，新产品的性能有望提高10倍、100倍。

Dare Obsanjo指出[如果不把这句真言当回事，会带来什么样的恶劣后果](http://www.25hoursaday.com/weblog/2008/05/23/SomeThoughtsOnTwittersAvailabilityProblems.aspx)—— 也就是Twitter正面临的麻烦。论及Twitter的内容管理，Obsanjo说，“如果一个设计只是简单地反映了问题描述，你去实现它就会落入磁盘 I/O的地狱。不管你用Ruby on Rails、Cobol on Cogs、C++还是手写汇编都一样，读写负载照样会害死你。”换言之，应该把随机操作推给RAM，只给硬盘留下顺序操作。 [Tom White](http://www.lexemetech.com/)是[Hadoop Core](http://hadoop.apache.org/core)项目的提交者，也是Hadoop项目管理委员会的成员。他对Gray的真言中“硬盘是新的磁带”部分作了更深入地探讨。White在讨论MapReduce编程模型的时候指出，为何对于Hadloop这类工具来说，[硬盘仍然是可行的](http://www.lexemetech.com/2008/03/disks-have-become-tapes.html)应用程序数据存储介质：

> 本质上，在MapReduce的工作方式中，数据流式地读出和写入硬盘，MapReduce是以硬盘的传输速率不断地对这些数据进行排序和合并。 与之相比，访问关系数据库中的数据，其速率则是硬盘的寻道速率（寻道指移动磁头到盘面上的指定位置读取或写入数据的过程）。为什么要强调这一点？请看看寻道时间和磁盘传输率的发展曲线。寻道时间每年大约提高5%，而数据传输率每年大约提高20%。寻道时间的进步比数据传输率慢——因此采用由数据传输率决定性能的模型是有利的。MapReduce正是如此。

虽然固态硬盘（SSD）能否改变寻道时间/传输率的对比还有待观察，[White文章的跟贴](http://www.lexemetech.com/2008/03/disks-have-become-tapes.html?showComment=1205973660000#c2336624186434337035)中，很多人都认为[SSD会成为RAM/硬盘之争中的平衡因素](http://www.lexemetech.com/2008/03/disks-have-become-tapes.html?showComment=1205987880000#c135263265622703132)。 Nati Shalom对[内存和硬盘在数据库部署和使用中的角色作了一番有理有据的评述](http://natishalom.typepad.com/nati_shaloms_blog/2008/03/scaling-out-mys.html)。 Shalom着重指出用数据库集群和分区来解决性能和可伸缩性的局限。他说，“数据库复制和数据库分区都存在相同的基本问题，它们都依赖于文件系统/硬盘 的性能，建立数据库集群也非常复杂”。他提议的方案是转向In-Memory Data Grid（IMDG），用Hibernate二级缓存或者GigaSpaces Spring DAO之类的技术作支撑，将持久化作为服务（Persistence as a Service）提供给应用程序。Shalom解释说，IMDG

> 提供在内存中的基于对象的数据库能力，支持核心的数据库功能，诸如高级索引和查询、事务语义和锁。IMDG还从应用程序的代码中抽象出了数据的拓扑。通过这样的方式，数据库不会完全消失，只是挪到了“正确的”位置。

IMDG相比直接RDBMS访问的优势列举如下：

*   位于内存中，速度和并发能力都比文件系统优越得多
*   数据可通过引用访问
*   直接对内存中的对象执行数据操作
*   减少数据的争用
*   并行的聚合查询
*   进程内（In-process）的局部缓存
*   免除了对象-关系映射（ORM）

你是否需要改变对应用和硬件的思维方式，最终取决于你要用它们完成的工作。但似乎公论认为，开发者解决性能和可伸缩性的思路已经到了该变一变的时候。

### 

### 

# 

## 

#### 

[有一个临界点](http://alan.blog-city.com/has_amazon_ec2_become_over_subscribed.htm)：

> 在开始的日子里Amazon的表现非常棒。实例在几分钟内启动，几乎没有遇到任何问题，即便是他们的[小实例（SMALL INSTANCE）](http://aws.amazon.com/ec2/instance-types/)也很健壮，足以支持适当使用的MySQL数据库。在20个月内，Amazon云系统一切运转良好，不需要任何的关心和抱怨。
> 
> ……
> 
> 然而，在最后的八个月左右，他们“盔甲”内的漏洞开始呈现出来了。第一个弱点前兆是，新加入的Amazon SMALL实例的性能出现了问题。根据我们的监控，在服务器场中新添加的机器，与原先的那些相比性能有所下降。开始我们认为这是自然出现的怪现象，只是碰 巧发生在“吵闹的邻居”（Noisy Neighbors）旁边。根据随机法则，一次快速的停机和重新启动经常就会让我们回到“安静的邻居”旁边，那样我们可以达到目的。
> 
> …… 然而，在最后的一两个月中，我们发现，甚至是这些“使用高级CPU的中等实例”也遭受了与小实例相同的命运，其中，新的实例不管处于什么位置，看起来似乎都表现得一样。经过调查，我们还发现了一个新问题，它已经悄悄渗透到到Amazon的世界中，那就是内部网络延迟。

#### 

## 

## 

## 

## 

### 

### 

## 

## 

[paxos](http://en.wikipedia.org/wiki/Paxos_algorithm)是一种处理一致性的手段，可以理解为事务吧。其他的手段不要Google GFS使用的Chubby的Lock service。我不大喜欢那种重型的设计就不费笔墨了。

### 

[![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.3.png]]
](http://timyang.net/blog/wp-content/uploads/2010/02/idc-transaction.png)

## http://timyang.net/blog/wp-content/uploads/2010/02/idc-transaction.png

[Distributed hash table](http://en.wikipedia.org/wiki/Distributed_hash_table)
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.32.png]]


## 

## 

## 

 [CouchDB](http://horicky.blogspot.com/2008/10/couchdb-implementation.html) and Google BigTable.CouchDB has a MVCC model that uses a copy-on-modified approach. Any update will cause a private copy being made which in turn cause the index also need to be modified and causing the a private copy of the index as well, all the way up to the root pointer.
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.23.png]]
Notice that the update happens in an append-only mode where the modified data is appended to the file and the old data becomes garbage. Periodic garbage collection is done to compact the data. Here is how the model is implemented in memory and disks
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.17.png]]
In Google BigTable model, the data is broken down into multiple generations and the memory is use to hold the newest generation. Any query will search the mem data as well as all the data sets on disks and merge all the return results. Fast detection of whether a generation contains a key can be done by checking a bloom filter.
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.37.png]]
When update happens, both the mem data and the commit log will be written so that if the

## 

## 

### 

### 

[简单分析含源码](http://www.penglixun.com/work/database/column-oriented_dbms_analyse.html)

# 

## 

### 

#### 

#### 

#### 

#### 

#### 

#### 

[memcached api page](http://danga.com/memcached/apis.bml) \[2\]。大家可以根据自己项目的需要，选择合适的客户端来集成。

#### 

#### 

[源代码级别的分析](http://blog.developers.api.sina.com.cn/?p=124)[非常好的剖析文章](http://tech.idv2.com/2008/08/17/memcached-pdf/)

### 

[Report of Benchmark Test](http://qdbm.sourceforge.net/benchmark.pdf)》。
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.43.png]]


#### 

[dbcached 的故障转移支持、设计方向以及与 Memcachedb 的不同之处](http://code.google.com/p/dbcached/wiki/Failover)》

## 

### 

[**Hadoop / HBase**](http://hadoop.apache.org/): API: **Java / any writer**, Protocol: **any write call**, Query Method: **MapReduce Java / any exec**, Replication: **HDFS Replication**, Written in: **Java**, Concurrency: ?, Misc: **Links**: 3 Books \[[1](http://www.amazon.com/Hadoop-Action-Chuck-Lam/dp/1935182196/ref=sr_1_3?ie=UTF8&amp;s=books&amp;qid=1256498379&amp;sr=1-3), [2](http://www.amazon.com/Pro-Hadoop-Jason-Venner/dp/1430219424/ref=sr_1_2?ie=UTF8&amp;s=books&amp;qid=1256498379&amp;sr=1-2), [3](http://www.amazon.com/Hadoop-Definitive-Guide-Tom-White/dp/0596521979/ref=sr_1_1?ie=UTF8&amp;s=books&amp;qid=1256498379&amp;sr=1-1)\]

### 

### 

### 

[**Cassandra**](http://incubator.apache.org/cassandra/): API: **many** **Thrift** [»](http://incubator.apache.org/thrift/) **languages**, Protocol: ?, Query Method: **MapReduce**, Replicaton: , Written in: **Java**, Concurrency: **eventually consistent** , Misc: like "Big-Table on Amazon Dynamo alike",  initiated by Facebook, Slides [»](http://www.slideshare.net/jericevans/an-introduction-to-cassandra) , Clients [»](http://wiki.apache.org/cassandra/ClientExamples)Cassandra是facebook开源出来的一个版本，可以认为是BigTable的一个开源版本，目前twitter和digg.com在使用。

#### 

http://blog.evanweaver.com/articles/2009/07/06/up-and-running-with-cassandra/，有非常详细的介绍。Cassandra以单个节点来衡量，其节点的并发读写性能不是特别好，有文章说评测下来Cassandra每秒大约不到1万次读写请求，我也看 到一些对这个问题进行质疑的评论，但是评价Cassandra单个节点的性能是没有意义的，真实的分布式数据库访问系统必然是n多个节点构成的系统，其并 发性能取决于整个系统的节点数量，路由效率，而不仅仅是单节点的并发负载能力。

#### 

#### 

#### 

#### 

#### 

#### 

#### 

#### 

[我](http://www.hellodba.net/)对Cassandra数据模型的理解：1.column name存放真正的值，而value是空。因为Cassandra是按照column name排序，而且是按列存储的，所以往往利用column name存放真正的值，而value部分则是空。例如：“jacky”:“null”，“fenng”:”null”2.Super column可以看作是一个索引，有点象关系型数据库中的外键，利用super column可以实现快速定位，因为它可以返回一堆column，而且是排好序的。3.排序在定义时就确定了，取出的数据肯定是按照确定的顺序排列的，这是一个巨大的性能优势。4\. 非常灵活的schema，column可以灵活定义。实际上，colume name在很多情况下，就是value（是不是有点绕）。5.每个column后面的timestamp，我并没有找到明确的说明，我猜测可能是数据多版本，或者是底层清理数据时需要的信息。最后说说架构，我认为架构的核心就是有所取舍，不管是CAP还是BASE，讲的都是这个原则。架构之美在于没有任何一种架构可以完美的解决各种问题，数据库和NoSQL都有其应用场景，我们要做的就是为自己找到合适的架构。**Hypertable**[**Hypertable**](http://couchdb.apache.org/): (can you help?) Open-Source Google BigTable alike.它是搜索引擎公司Zvents根据Google的9位研究人员在2006年发表的一篇论文《[Bigtable：结构化数据的分布存储系统](http://labs.google.com/papers/bigtable.html)》 开发的一款开源分布式数据储存系统。Hypertable是按照1000节点比例设计，以 C++撰写，可架在 HDFS 和 KFS 上。尽管还在初期阶段，但已有不错的效能：写入 28M 列的资料，各节点写入速率可达7MB/s，读取速率可达 1M cells/s。Hypertable目前一直没有太多高负载和大存储的应用实例，但是最近，Hypertable项目得到了[百度](http://www.baidu.com/)的赞助支持，相信其会有更好的发展。

### 

[![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.7.jpeg]]](http://code.google.com/appengine/docs/python/datastore/)[Google AppEngine Datastore](http://code.google.com/appengine/docs/python/datastore/) 是在BigTable之上建造出来的，是Google的内部存储系统，用于处理结构化数据。AppEngine Datastore其自身及其内部都不是直接访问BigTable的实现机制，可被视为BigTable之上的一个简单接口。AppEngine Datastore所支持的项目的数据类型要比SimpleDB丰富得多，也包括了包含在一个项目内的数据集合的列表型。如果你打算在Google AppEngine之内建造应用的话，几乎可以肯定要用到这个数据存储。然而，不像SimpleDB，使用谷歌网络服务平台之外的应用，你并不能并发地与AppEngine Datastore进行接口 (或通过BigTable)。

### 

#### 

#### 

##### 

##### 

##### 

##### 

#### 

[I want a big, virtual database](http://glinden.blogspot.com/2006/03/i-want-big-virtual-database.html)What I want is a robust, high performance virtual relational database that runs transparently over a cluster, nodes dropping in an out of service at will, read-write replication and data migration all done automatically.I want to be able to install a database on a server cloud and use it like it was all running on one machine.详细资料：http://timyang.net/architecture/yahoo-pnuts/

### 

[SQL数据服务](http://www.microsoft.com/azure/data.mspx) 是微软 [Azure](http://www.microsoft.com/azure/default.mspx) 网 络服务平台的一部分。该SDS服务也是处于测试阶段，因此也是免费的，但对数据库大小有限制。 SQL数据服务其自身实际上是一项处在许多SQL服务器之上的应用，这些SQL服务器组成了SDS平台底层的数据存储。你不需要访问到它们，虽然底层的数 据库可能是关系式的；SDS是一个键/值型仓储，正如我们迄今所讨论过的其它平台一样。微软看起来不同于前三个供应商，因为虽然键/值存储对于可扩性���言非常棒，相对于RDBMS，在数据管理上却很困难。微软的方案似乎是入木三分，在实现可扩性和分布机制的同时，随着时间的推移，不断增加特性，在键/值存储和关系数据库平台的鸿沟之间搭起一座桥梁。

## 

## 

### 

[**C**](http://couchdb.apache.org/)[**ouchDB**](http://couchdb.apache.org/):  API: **JSON**, Protocol: **REST**, Query Method: **MapReduceR of JavaScript Funcs**, Replication: **Master Master**, Written in: **Erlang**, Concurrency: **MVCC**,  **Misc**: **Links**: 3 CouchDB books [»](http://couchdb.apache.org/docs/books.html), Couch Lounge [»](http://code.google.com/p/couchdb-lounge/) (partitioning / clusering),  ...它是Apache社区基于 Erlang/OTP 构建的高性能、分布式容错非关系型数据库系统（NRDBMS）。它充分利用 Erlang 本身所提供的高并发、分布式容错基础平台，并且参考 Lotus Notes 数据库实现，采用简单的文档数据类型（document-oriented）。在其内部，文档数据均以 JSON 格式存储。对外，则通过基于 HTTP 的 REST 协议实现接口，可以用十几种语言进行自由操作。
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.33.png]]
CouchDB一种半结构化面向文档的分布式，高容错的数据库系统，其提供RESTFul HTTP/JSON接口。其拥有MVCC特性，用户可以通过自定义Map/Reduce函数生成对应的View。在CouchDB中，数据是以JSON字符的方式存储在文件中。

#### 

### 

[**Riak**](http://riak.basho.com/): API: **JSON**, Protocol: **REST**, Query Method: **MapReduce term matching** , Scaling: **Multiple Masters**; Written in: **Erlang**, Concurrency: **eventually consistent** (stronger then MVCC via Vector Clocks), **Misc:** ... **Links**: talk [»](http://riak.basho.com/nyc-nosql/),

### 

[**MongoDB**](http://www.mongodb.org/):  API: **BSON**, Protocol: **lots of langs**, Query Method: **dynamic object-based language**, Replication: **Master Slave**, Written in: **C++**,Concurrency: **Update in Place**. **Misc:** ... **Links**: Talk [»](http://www.leadit.us/hands-on-tech/MongoDB-High-Performance-SQL-Free-Database),MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。他支持的数据结构非常松散，是 类似json的bjson格式，因此可以存储比较复杂的数据类型。Mongo最大的特点是他支持的查询语言非常强大，其语法有点类似于面向对象的查询语 言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。Mongo主要解决的是海量数据的访问效率问题，根据官方的文档，当数据量达到50GB以上的时候，Mongo的数据库访问速度是MySQL的 10倍以上。Mongo的并发读写效率不是特别出色，根据官方提供的性能测试表明，大约每秒可以处理0.5万－1.5次读写请求。对于Mongo的并发读 写性能，我（robbin）也打算有空的时候好好测试一下。因为Mongo主要是支持海量数据存储的，所以Mongo还自带了一个出色的分布式文件系统GridFS，可以支持海量的数据存储，但我也看到有些评论认为GridFS性能不佳，这一点还是有待亲自做点测试来验证了。最后由于Mongo可以支持复杂的数据结构，而且带有强大的数据查询功能，因此非常受到欢迎，很多项目都考虑用MongoDB来替代MySQL来实现不是特别复杂的Web应用，比方说[why we migrated from MySQL to MongoDB](http://blog.boxedice.com/2009/07/25/choosing-a-non-relational-database-why-we-migrated-from-mysql-to-mongodb/)就是一个真实的从MySQL迁移到MongoDB的案例，由于数据量实在太大，所以迁移到了Mongo上面，数据查询的速度得到了非常显著的提升。MongoDB也有一个ruby的项目[MongoMapper](http://github.com/jnunemaker/mongomapper)，是模仿Merb的DataMapper编写的MongoDB的接口，使用起来非常简单，几乎和DataMapper一模一样，功能非常强大易用。

### 

[**Terrastore**](http://code.google.com/p/terrastore/): API: **Java & http**, Protocol: **http**, Language: **Java**, Querying: **Range queries, Predicates**, Replication: **Partitioned with consistent hashing**, Consistency: **Per-record strict consistency**, Misc: Based on Terracotta

### 

[**ThruDB**](http://code.google.com/p/thrudb/): (please help provide more facts!) Uses Apache [Thrift](http://incubator.apache.org/thrift/) to integrate multiple backend databases as BerkeleyDB, Disk, MySQL, S3.

## 

### 

[**Amazon SimpleDB**](http://aws.amazon.com/simpledb/): **Misc**: not open source, Book [»](http://www.apress.com/book/view/1430225335)****[SimpleDB](http://aws.amazon.com/simpledb/) 是一个亚马逊网络服务平台的一个面向属性的键/值数据库。SimpleDB仍处于公众测试阶段；当前，用户能在线注册其“免费”版 --免费的意思是说直到超出使用限制为止。SimpleDB有几方面的限制。首先，一次查询最多只能执行5秒钟。其次，除了字符串类型，别无其它数据类型。一切都以字符串形式被存储、获取和 比较，因此除非你把所有日期都转为ISO8601，否则日期比较将不起作用。第三，任何字符串长度都不能超过1024字节，这限制了你在一个属性中能存储 的文本的大小（比如说产品描述等）。不过，由于该模式动态灵活，你可以通过追加“产品描述1”、“产品描述2”等来绕过这类限制。一个项目最多可以有 256个属性。由于处在测试阶段，SimpleDB的域不能大于10GB，整个库容量则不能超过1TB。SimpleDB的一项关键特性是它使用一种[最终一致性模型](http://www.allthingsdistributed.com/2008/12/eventually_consistent.html)。 这个一致性模型对并发性很有好处，但意味着在你改变了项目属性之后，那些改变有可能不能立即反映到随后的读操作上。尽管这种情况实际发生的几率很低，你也 得有所考虑。比如说，在你的演出订票系统里，你不会想把最后一张音乐会门票卖给5个人，因为在售出时你的数据是不一致的。****

### 

[**Chordless**](http://sourceforge.net/projects/chordless/): API: **Java & simple RPC to vals**, Protocol: **internal**, Query Method: **M/R inside value objects**, Scaling: **every node is master for its slice of namespace**, Written in: **Java**, Concurrency: **serializable transaction isolation**, **Links**:

### 

[**Redis**](http://code.google.com/p/redis/) : (please help provide more facts!)  API: **Tons of languages**, Written in: **C**, Concurrency: **in memory** and saves asynchronous disk after a defined time. Append only mode available. Different kinds of fsync policies. Replication: **Master / Slave**,Redis是一个很新的项目，刚刚发布了1.0版本。Redis本质上是一个Key-Value类型的内存数据库，很像memcached，整个数据库统 统加载在内存当中进行操作，定期通过异步操作把数据库数据flush到硬盘上进行保存。因为是纯内存操作，Redis的性能非常出色，每秒可以处理超过 10万次读写操作，是我知道的性能最快的Key-Value DB。Redis的出色之处不仅仅是性能，Redis最大的魅力是支持保存List链表和Set集合的数据结构，而且还支持对List进行各种操作，例 如从List两端push和pop数据，取List区间，排序等等，对Set支持各种集合的并集交集操作，此外单个value的最大限制是1GB，不像 memcached只能保存1MB的数据，因此Redis可以用来实现很多有用的功能，比方说用他的List来做FIFO双向链表，实现一个轻量级的高性 能消息队列服务，用他的Set可以做高性能的tag系统等等。另外Redis也可以对存入的Key-Value设置expire时间，因此也可以被当作一 个功能加强版的memcached来用。Redis的主要缺点是数据库容量受到物理内存的限制，不能用作海量数据的高性能读写，并且它没有原生的可扩展机制，不具有scale（可扩展） 能力，要依赖客户端来实现分布式读写，因此Redis适合的场景主要局限在较小数据量的高性能操作和运算上。目前使用Redis的网站有 github，Engine Yard。

### 

[**Scalaris**](http://code.google.com/p/scalaris/): (please help provide more facts!) Written in: **Erlang**, Replication: **Strong consistency over replicas**, Concurrency: **non blocking Paxos**.

### 

[**Tokyo Cabinet / Tyrant**](http://1978th.net/): **Links**: nice talk [»](http://www.infoq.com/presentations/grigorik-tokyo-cabinet-recipes), slides [»](http://www.scribd.com/doc/12016121/Tokyo-Cabinet-and-Tokyo-Tyrant-Presentation), Misc: **Kyoto** Cabinet [»](http://1978th.net/kyotocabinet/)它是日本最大的SNS社交网站[mixi.jp](http://mixi.jp/)开发的 Tokyo Cabinet key-value数据库网络接口。它拥有Memcached兼容协议，也可以通过HTTP协议进行数据交换。对任何原有Memcached客户端来讲， 可以将Tokyo Tyrant看成是一个Memcached，但是，它的数据是可以持久存储的。Tokyo Tyrant 具有故障转移、日志文件体积小、大数据量下表现出色等优势，详见：http://blog.s135.com/post/362.htmTokyo Cabinet 2009年1月18日发布的新版本（Version 1.4.0）已经实现 Table Database，将key-value数据库又扩展了一步，有了MySQL等关系型数据库的表和字段的概念，相信不久的将来，Tokyo Tyrant 也将支持这一功能。值得期待。
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.29.png]]TC除了支持Key-Value存储之外，还支持保存Hashtable数据类型，因此很像一个简单的数据库表，并且还支持基于column的条 件查询，分页查询和排序功能，基本上相当于支持单表的基础查询功能了，所以可以简单的替代关系数据库的很多操作，这也是TC受到大家欢迎的主要原因之一， 有一个Ruby的项目[miyazakiresistance](http://github.com/tsukasaoishi/miyazakiresistance)将TT的hashtable的操作封装成和ActiveRecord一样的操作，用起来非常爽。TC/TT在mixi的实际应用当中，存储了2000万条以上的数据，同时支撑了上万个并发连接，是一个久经考验的项目。TC在保证了极高的并发 读写性能的同时，具有可靠的数据持久化机制，同时还支持类似关系数据库表结构的hashtable以及简单的条件，分页和排序操作，是一个很棒的 NoSQL数据库。TC的主要缺点是在数据量达到上亿级别以后，并发写数据性能会大幅度下降，[NoSQL: If Only It Was That Easy](http://bjclark.me/2009/08/04/nosql-if-only-it-was-that-easy/)提到，他们发现在TC里面插入1.6亿条2-20KB数据的时候，写入性能开始急剧下降。看来是当数据量上亿条的时候，TC性能开始大幅度下降，从TC作者自己提供的mixi数据来看，至少上千万条数据量的时候还没有遇到这么明显的写入性能瓶颈。这个是Tim Yang做的一个[Memcached，Redis和Tokyo Tyrant的简单的性能评测，仅供参考](http://timyang.net/data/mcdb-tt-redis/)


### 

[**GT.M**](http://fis-gtm.com/): API: **M, C, Python, Perl**, Protocol: **native, inprocess C**, Misc: Wrappers: **M/DB for SimpleDB compatible HTTP** [»](http://www.mgateway.com/mdb.html), **MDB:X** for XML [»](http://mgateway.com/), **PIP** for mapping to tables for SQL [»](http://fis-pip.com/), Features: Small footprint (17MB), Terabyte Scalability, Unicode support, Database encryption, Secure, ACID transactions (single node), eventual consistency (replication), License: AGPL v3 on x86 GNU/Linux, **Links**: Slides [»](http://www.slideshare.net/robtweed/gtm-a-tried-and-tested-schemaless-database),

### 

[**Scalien**](http://scalien.com/):  API / Protocol: **http** (text, html, JSON)**, C, C++, Python**, Concurrency: **Paxos**.

### 

[**Berkley DB**](http://www.oracle.com/database/berkeley-db/db/index.html): API: **Many languages**, Written in: **C**, Replication: **Master / Slave**, Concurrency: **MVCC**, License: **Sleepycat**, **BerkleyDB Java Edition**: API: **Java**, Written in: **Java**, Replication: **Master / Slave**, Concurrency: **serializable transaction isolation**, License: **Sleepycat**

### 

[**MemcacheDB**](http://memcachedb.org/): API: Memcache protocol (get, set, add, replace, etc.), Written in: **C**, Data Model: **Blob**, Misc: Is Memcached writing to BerkleyDB.它是新浪互动社区事业部为在Memcached基础上，增加Berkeley DB存储层而开发一款支持高并发的分布式持久存储系统，对任何原有Memcached客户端来讲，它仍旧是个Memcached，但是，它的数据是可以持久存储的。
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.27.jpeg]]


### 

[**Mnesia**](http://www.erlang.org/doc/apps/mnesia/index.html): (ErlangDB [»](http://www.infoq.com/news/2007/08/mnesia))

### 

[**LightCloud**](http://opensource.plurk.com/LightCloud/):  (based on Tokyo Tyrant)

### 

[**HamsterDB**](http://hamsterdb.com/):  (embedded solution) ACID Compliance, Lock Free Architecture (transactions fail on conflict rather than block), Transaction logging & fail recovery (redo logs), In Memory support – can be used as a non-persisted cache, B+ Trees – supported \[Source: Tony Bain [»](http://blog.tonybain.com/)\]

### 

## 

### 

[**Amazon Dynamo**](http://www.allthingsdistributed.com/2007/10/amazons_dynamo.html): **Misc**: not open source (see KAI below)

#### 

#### 

### 

#### 

 http://groups.google.com/group/beandb/

#### 

#### 

#### 

  

  **[BeansDB设计实现（非常难得的中文资料）](http://beansdb.googlecode.com/files/Inside%20BeansDB.pdf)[PPT](http://www.slideshare.net/hongqn/qcon-beijing-2009)**



### 

#### 

### 

[**Voldemort**](http://project-voldemort.com/): (can you help)Voldemort是个和Cassandra类似的面向解决scale问题的分布式数据库系统，Cassandra来自于Facebook这个 SNS网站，而Voldemort则来自于Linkedin这个SNS网站。说起来SNS网站为我们贡献了n多的NoSQL数据库，例如 Cassandar，Voldemort，Tokyo Cabinet，Flare等等。Voldemort的资料不是很多，因此我没有特别仔细去钻研，Voldemort官方给出Voldemort的并发读 写性能也很不错，每秒超过了1.5万次读写。
![[Archive/面试资料/System Design/_resources/NoSQL数据库笔谈.resources/unknown_filename.13.png]]
其实现在很多公司可能都面临着这个抽象架构图中的类似问题。以 Hadoop 作为后端的计算集群，计算得出来的数据如果要反向推到前面去，用什么方式存储更为恰当? 再放到 DB 里面的话，构建索引是麻烦事；放到 Memcached 之类的 Key-Value 分布式系统中，毕竟只是在内存里，数据又容易丢。[Voldemort](http://project-voldemort.com/) 算是一个不错的改良方案。值得借鉴的几点:

*   键(Key)结构的设计，有点技巧；
*   架构师熟知硬件结构是有用的。越大的系统越是如此。
*   用好并行。[Amdahl 定律](http://en.wikipedia.org/wiki/Amdahl%27s_law)以后出现的场合会更多。

详细：http://www.dbanotes.net/arch/voldemort\_key-value.htmlhttp://project-voldemort.com/blog/2009/06/building-a-1-tb-data-cycle-at-linkedin-with-hadoop-and-project-voldemort/

### 

[**Dynomite**](http://wiki.github.com/cliffmoon/dynomite/dynomite-framework): (can you help)

### 

[**KAI**](http://sourceforge.net/projects/kai/): Open Source Amazon Dnamo implementation, Misc: [slides](http://www.slideshare.net/takemaru/kai-an-open-source-implementation-of-amazons-dynamo-472179) ,

## 

### 

### 

[Drizzle](https://launchpad.net/drizzle)可 被认为是键/值存储要解决的问题的反向方案。Drizzle诞生于MySQL（6.0）关系数据库的拆分。在过去几个月里，它的开发者已经移走了大量非核 心的功能（包括视图、触发器、已编译语句、存储过程、查询缓冲、ACL以及一些数据类型），其目标是要建立一个更精简、更快的数据库系统。Drizzle 仍能存放关系数据；正如MySQL/Sun的Brian Aker所说那样：“没理由泼洗澡水时连孩子也倒掉”。它的目标就是，针对运行于16核（或以上）系统上的以网络和云为基础的应用，建立一个半关系型数据 库平台。

## 

### 

### 

### 

# 

## 

##  

## 

## 

[Slides](http://assets.en.oreilly.com/1/event/29/Fixing%20Twitter_%20Improving%20the%20Performance%20and%20Scalability%20of%20the%20World%27s%20Most%20Popular%20Micro-blogging%20Site%20Presentation.pdf)\] \[[Video](http://blip.tv/file/2300327) (GFWed)\]，这是Twitter的John Adams在[Velocity 2009](http://en.oreilly.com/velocity2009)的一个演讲，主要介绍了Twitter在系统运维方面一些经验。 本文大部分整理的观点都在Twitter(@[xmpp](http://twitter.com/xmpp))上发过，这里全部整理出来并补充完整。

Twitter没有自己的硬件，都是由NTTA来提供，同时NTTA负责硬件相关的网络、带宽、负载均衡等业务，Twitter operations team**只关注核心的业务，包括Performance，Availability，Capacity Planning容量规划，配置管理**等，这个可能跟国内一般的互联网公司有所区别。

### 

#### 

#### 

#### 

#### 

#### 

### 

#### 

#### 

#### 

[Campfire](http://campfirenow.com/)官方说明。

### 

*   [Memcached数据被踢(evictions>0)现象分析](http://timyang.net/data/memcached-lru-evictions/)中的一些经验一致。
*   Memcached SEGVs, Memcached崩溃(cold cache problem)据称会给这种高度依赖Cache的Web 2.0系统带来灾难，不知道Twitter具体怎么解决。
*   在Web层Twitter使用了Varnish作为反向代理，并对其评价较高。

## 

[**伸缩性**](http://www.jdon.com/jivejdon/tags/2513)架构设计完全交给谷歌负责，最终用户完全不必担心管理基础设施。Force.com平台类似，但采用了自定义的编程语言名为Apex。如果你是一个大型企业寻求内部开发应用的部署，这层是你的顶峰。**The SaaS Layer**如 果您是中小型企业（SME）和大企业不希望开发自己的应用程序时，SaaS的层是你的顶峰（是你将直接面对的）。您只是进行有兴趣地采购如电子邮件或客户 关系管理服务，这些功能服务已经被供应商开发成功，并部署到云环境中了，您只需验证的应用是否符合你的使用需要，帐单可以基于包月租费等各种形式，，作为 最终用户的您不会产生开发和维护拓展应用程序软件的任何成本。越来越多的企业订阅Salesforce.com和Sugar CRM的SaaS产品。

## 

### 

### 

### 

### 

### 

### 

### 

## 

### 

[服务器](http://www.ciw.com.cn/Search.asp?Field=Title&amp;keyword=%E6%9C%8D%E5%8A%A1%E5%99%A8)上。这样，当最终用户在调阅这个分析模型的时候，就可以直接使用这个CUBE，在此基础上根据用户的维选择和维组合进行复运算，从而达到实时响应的效果。

## 

### 

 [Why Existing Databases (RAC) are So Breakable!](http://natishalom.typepad.com/nati_shaloms_blog/2009/11/why-existing-databases-rac-are-so-breakable.html) 中找到进一步描述。哪里，我介绍了一些来自 [Jason McHugh](http://qconsf.com/sf2009/speaker/Jason+McHugh) 的讲演的面向失效的架构设计的内容（Jason 是在 Amazon 做 S3 相关工作的高级工程师）。

### 

### 

### 

 [Ricky Ho](http://www.blogger.com/profile/03793674536997651667) 的文章 [NOSQL Patterns](http://horicky.blogspot.com/2009/11/nosql-patterns.html%20) 。

### 

### 

 [Ricky Ho](http://www.blogger.com/profile/03793674536997651667) 的文章 [Query Processing for NOSQL DB](http://horicky.blogspot.com/2009/11/query-processing-for-nosql-db.html) 。

### 

### 

[进一步阅读](http://natishalom.typepad.com/nati_shaloms_blog/2009/11/why-existing-databases-rac-are-so-breakable.html)）所有这些导致了对这类“可伸缩性优先数据库”的需求。这里，我引用 AWS团队的接触工程师、VP， [James Hamilton](http://mvdirona.com/jrh/work/) 在他的文章 [One Size Does Not Fit Al](http://perspectives.mvdirona.com/2009/11/03/OneSizeDoesNotFitAll.aspx)l 中的一段话：

> “伸缩性优先应用是那些必须具备无限可伸缩性的应用，能够不受限制的扩展比更丰富的功能更加重要。这些应用包括很多需要高 可伸缩性的网站，如 Facebook, MySpace, Gmail, Yahoo 以及 Amazon.com。有些站点实际上使用了关系型数据库，而大部分实际上并未使用。这些服务的共性在于可扩展性比功能公众要，他们无法泡在一个单一的 RDBMS 上。”

总结一下——我认为，现有的 SQL 数据库可能不会很快淡出历史舞台，但同时它们也不能解决世上的所有问题。NOSQL 这个名词现在也变成了 Not Only SQL，这个变化表达了我的观点。

# 

## 

## 

##

----

- Date: 2012-07-18
- Tags: #db #Interview/System-Design 
- Source URL: [](http://sebug.net/paper/databases/nosql/Nosql.html)



