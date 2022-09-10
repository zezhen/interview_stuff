# Cloud Messaging Service - Yahoo
----



Geo Replication


*   Asynchronous replication, integrated in the broker message flow
*   Simple configuration to add/remove regions
*   Individually configurable for different users and applications

![[Archive/面试资料/System Design/_resources/Cloud_Messaging_Service_-_Yahoo.resources/unknown_filename.png]]

Architecture


*   Separate Layers between brokers and storage (bookies)
    *   Broker and bookies can be added independently
    *   Traffic can be shifted very quickly across brokers
    *   New bookies will ramp up on traffic quickly

![[Archive/面试资料/System Design/_resources/Cloud_Messaging_Service_-_Yahoo.resources/unknown_filename.2.png]]


*   Broker
    *   End-to-end async message processing
    *   Messages are replayed across producers, bookies and consumers with no copies
    *   Pooled ref-counted buffers
    *   Cache recent messages


![[Archive/面试资料/System Design/_resources/Cloud_Messaging_Service_-_Yahoo.resources/unknown_filename.1.png]]

[Getting Started with CMSv2](https://docs.google.com/document/d/1og5FQXFJhucBFOLvlJE1S64A7_b5_413ToWaRaVu7a8/edit#)




----

- Date: 2019-01-17
- Tags: #Interview/System-Design 



