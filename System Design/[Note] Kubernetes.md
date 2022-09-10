# [Note] Kubernetes
----

在集群化环境中运行基于容器的应用程序, 需要解决如下问题:

1.  调度
    *   确保应用程序在计划的正确的时间和位置运行.
2.  负载平衡
    *   确保客户端的负载均衡地分布在集群中的节点上.
3.  应用程序扩展
    *   根据客户端的需求来处理负载高峰, 即容器的上/下线
4.  集群管理与监控.
    *   需要定义、启动、扩展、平衡负载和监控正在运行的容器的健康情况


![[Archive/面试资料/System Design/_resources/[Note]_Kubernetes.resources/unknown_filename.png]]

[Pod](http://kubernetes.io/v1.1/docs/user-guide/pods.html)安排在节点上，包含一组容器和卷, 它们协同执行一个应用程序功能（或一组功能），是Kubernetes 中的调度单元。同一个Pod里的容器共享同一个网络命名空间，可以使用localhost互相通信。Pod是短暂的，不是持续性实体. Volume(卷)是Pod中能够被多个容器访问的共享目录。定义在Pod之上，被一个Pod里的多个容器挂载到具体的文件目录之下；与Pod生命周期相同。

一个Label是attach到Pod的一对键/值对，用来传递用户定义的属性。比如，你可能创建了一个"tier"和“app”标签，通过Label（tier=frontend, app=myapp）来标记前端Pod容器

Replication Controller确保任意时间都有指定数量的Pod“副本”在运行。如果为某个Pod创建了Replication Controller并且指定3个副本，它会创建3个Pod，并且持续监控它们。如果某个Pod不响应，那么Replication Controller会替换它，保持总数为3. 如果之前不响应的Pod恢复了，现在就有4个Pod了，那么Replication Controller会将其中一个终止保持总数为3。如果在运行中将副本总数改为5，Replication Controller会立刻启动2个新Pod，保证总数为5

[Service](http://kubernetes.io/v1.1/docs/user-guide/services.html)是定义一系列Pod以及访问这些Pod的策略的一层抽象, Service通过Label找到Pod组 (因为Pods是短暂的，那么重启时IP地址可能会改变), frontend通过本地DNS获取prod ip地址, 通过kube-proxy达到透明的均衡负载

集群拥有一个Kubernetes Master, 提供集群的独特视角，并且拥有一系列组件，比如Kubernetes API Server。API Server提供可以用来和集群交互的REST端点。master节点包括用来创建和复制Pod的Replication Controller。

**etcd**是一个键值存储仓库，用于配置共享和服务发现

[Google Container Engine](https://cloud.google.com/container-engine/docs/)是托管的Kubernetes容器环境









----

- Date: 2018-05-05
- Tags: #Interview/System-Design 



