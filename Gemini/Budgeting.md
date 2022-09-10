# Budgeting
----

Best Practice of High Available and Resilient, Eventual Consistent System

![[Archive/工作资料/Gemini/_resources/Budgeting.resources/unknown_filename.png]]


1.  High Availability
    1.  Built on lambda architecture, using Storm as speed/streaming layer to process spend events within milliseconds
    2.  Within Storm, topology processes events without acknowledge, a.k.a. at-most-once process, to guarantee the latest events could be process immediately, at same time, no-ack can avoid spend duplication. The lacking spend could be adjusted eventually by batch layer.
    3.  Storm is designed to be fail-fast and stateless, including nimbus, supervisors, for the application bolts and spouts, if they’re stateless, it’s easy to be bring up by supervisors, while for stateful bolts/spouts, better to have fault tolerant protection, e.g. redundancy, etc.
2.  Eventual Consistency
    1.  Message Order
        1.  Interface between Budgeting and Serving is message, which contains ad\_id, throttle\_rate, sequence\_no, the principle for Serving is to honor the throttle\_rate with larger sequence\_no for one ad\_id.
        2.  sequence\_no(long): epoch\_time / 1000 / 100 (8 digits) + type (1 digit) + incremental\_count (11 digits), which can support 1e12-1 sno in 15 minutes (initial cycle period)
    2.  Message Delivery Consistency
        1.  Auditor is used to detect the mismatch between Budgeting and Serving system, which might be due to messages lost, apply failure, etc
        2.  Auditor checks the status of all ad\_id  between two systems periodically (15 minutes), once any mismatch found, incremental patch will be applied to Serving via resending latest status
        3.  Auditor also runs in Serving side to apply the ‘latest’ full snapshot to its own system
    3.  Spend Consistency
        1.  As described in above section, no-ack mechanism might cause spend loss, which impact the pacing accuracy, system will apply historical spend feed through batch layer, along with latest adverting meta information from COW into speed layer to guarantee high pacing accuracy.
3.  High Resilience
    1.  Question: how to guarantee Budgeting system work properly when dependent system met incidents.
    2.  Monitor & Alert: be aware of dependent system’s incidents
        1.  monitor on input/output volume between two systems in two location (marked as blue and red color), including input events # from upstream, output messages # to downstream, input/output within system topology, etc
        2.  monitor heartbeats of all threads/processes/jobs
        3.  monitor data freshness e.g. timestamp
        4.  Alert once metrics over threshold
    3.  Action: failover to another system in different location (red vs blue)
        1.  two systems are running as hot-warm mode, both receive same data but only hot side publishes control signals while warm side sends heartbeat for connection
            1.  why only one system publishes signals? because it’s a control system, we need one brain to make decision, otherwise two brains will cause confusion.
        2.  can we do the failover automatically? As manual operation always has some delay. Thus, we have two ways to make that
            1.  Auto-Failover: once monitor system detected issues, the failover occurs automatically. This solution heavily depends on the monitor system, which needs to provide low latency and high quality metrics collection, otherwise too many ‘failover’ will cause system instability.
            2.  Hot-Hot: make two systems work at same time, once one side is down, another side can continue without downtime. This solution depends on the mechanism to resolve the conflict of the signals from two sides. There two options:
                1.  Clients do the job. Publisher sides add flag, e.g. red or blue to indicate the source of the signals, the client can follow some rules that pick the correct signal to apply. Pros is that clients can receive signals from both sides, so they have more information to make right decision, cons is that it didn’t solve the original problem but just push it from publisher side to client side.
                2.  Publisher do the job.
                    1.  One way is to make two systems/publishers communicate with each other. The pros is both can know the status of each other, so they can coordinate with each other to make decision, or once one system down, another will know immediately and take it over. The cons is we include another dependency, we need always guarantee the connection is alive, what if connection down? and we need a mechanism to confirm the system works correctly, what’s more a proper coordination are necessary as most time the system works well.
                    2.  Another way is to keep hot-warm mechanism, but let ‘warm’ do more job rather than just send heartbeat. The issue of failed to failover is out of control, it mainly the system fail to send signals or send incorrect signal, the most critical cause is over-delivery, so we can just solve the over-delivery problem only? If so, can we let ‘warm’ side only send STOP signal, it’s no harm because ‘hot’ side will send that if over-delivery. The pros is no logic change in ‘hot’ side, no extra dependency, both side make decision independently. The cons is that how to guarantee the STOP from ‘warm’ is correct? One simple way is to ask ‘warm’ do that with more strict criterions, e.g. send STOP with 5% more spend (averagely post-tp spend has 5%). Therefore, the STOP from ‘warm’ give us more confidence.
4.  Pacing
    1.  This is the most important job of Budgeting, beside the system stability, which we need to guarantee advertisers are happy with their money spending, as well as system overall revenue. The basic idea of pacing is because ads have various targeting audiences and bids, some ads has broad audience and high bid, it’s easy for them to win the auction and show to users, which means they would deplete their budget in short period, which doesn’t meet advertisers’ happiness. We have two ways to do the pacing, DR or BAR
    2.  Delivery Rate (DR)
        1.  or Throttle Rate, which is equivalent to 1-DR. We can treat DR as the probability of ads to take participate into the auction, e.g. DR=0.8 means the ads will join 8 auctions out of 10. Therefore, we can control ads’ spend pacing through tuning up or down their DRs. 
        2.  Regarding of DR, we could break it into multiple buckets across from 0.0 to 1.0, or change the DR according some tuning formula.
        3.  The pros of DR is straightforward, ads only looks at their own spending pacing and adjust their own DR.
        4.  The cons is that DR is the probability, 1.0 is the max value, it cannot help ads win the auction, another thing is the DR apply before auction, which is hard-throttling, we might lose some price support due to second-price auction.
    3.  Bid Adjustment Rate (BAR)
        1.  Rather than DR is applied before auction, BAR is applied into auction procedure. Ads auction is mainly to rank ads by their ecpm = bid \* pCTR, BAR is apply as a bid multiplier, the final ranking formula would be like ecpm = bid \* BAR \* pCTR, where BAR is range from 0 to 1 or higher.
        2.  Similar to DR, we could break BAR into multiple buckets or using tuning formula.
        3.  The pros of BAR is more power than DR, which could even lift the position in auction by assign over 1.0 number.
        4.  The cons of BAR is that ads still have lots of chance to show, we need a fast feedback to guarantee we find the correct BAR in time.
    4.  Spend Shape
        1.  Another topic is spend shape, can we make ads to spend following some special shapes, like big head (morning) and thin body (afternoon) or tail (even), or big body, or some consumed shapes?
        2.  We could reach that by assigned weighted budget across UNITs, the UNIT can be day, hour or minute. We can create the budget shape through unit weights, then within each unit, we apply DR or BAR to reach smooth spending. 
        3.  Overall, through the weighted unit budget allocation and intro-unit DR/BAR tuning to reach the spend shape.
    5.  Reference
        1.  [smart pacing for effective online ad campaign optimization](https://arxiv.org/pdf/1506.05851). pacing algorithm on DSP, similar to Budgeting pacing while they need to handle some performance campaign, which need to meet campaigns’ performance/conversion goal.
        2.  
5.  Pre-Serve vs Post-Serve Pacing
    1.  Budgeting is post-serve, rate tuning is triggered by revenue-bearing events, e.g. clicks or impression; more pre-serve refer to [[Smart Pricing|Smart Pricing]]


![[Archive/工作资料/Gemini/_resources/Budgeting.resources/unknown_filename.1.png]]


----

- Date: 2019-03-25
- Tags: #Interview/Gemini 



