# Designing Pastebin
----

### 
1\. What is Pastebin?

Pastebin like services enable users to store plain text or images over the network (typically the Internet) and generate unique URLs to access the uploaded data. Such services are also used to share data over the network quickly, as users would just need to pass the URL to let other users see it.

If you haven’t used [pastebin.com](http://pastebin.com/) before, please try creating a new ‘Paste’ there and spend some time going through different options their service offers. This will help you a lot in understanding this chapter better.

### 
2\. Requirements and Goals of the System

Our Pastebin service should meet the following requirements:

**Functional Requirements:**

1.  Users should be able to upload or “paste” their data and get a unique URL to access it.
2.  Users will only be able to upload text.
3.  Data and links will expire after a specific timespan automatically; users should also be able to specify expiration time.
4.  Users should optionally be able to pick a custom alias for their paste.

**Non-Functional Requirements:**

1.  The system should be highly reliable, any data uploaded should not be lost.
2.  The system should be highly available. This is required because if our service is down, users will not be able to access their Pastes.
3.  Users should be able to access their Pastes in real-time with minimum latency.
4.  Paste links should not be guessable (not predictable).

**Extended Requirements:**

1.  Analytics, e.g., how many times a times a paste was accessed?
2.  Our service should also be accessible through REST APIs by other services.

### 
3\. Some Design Considerations

Pastebin shares some requirements with [URL Shortening service](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5668600916475904), but there are some additional design considerations we should keep in mind.

**What should be the limit on the amount of text user can paste at a time?** We can limit users not to have Pastes bigger than 10MB to stop the abuse of the service.

**Should we impose size limits on custom URLs?** Since our service supports custom URLs, users can pick any URL that they like, but providing a custom URL is not mandatory. However, it is reasonable (and often desirable) to impose a size limit on custom URLs, so that we have a consistent URL database.

### 
4\. Capacity Estimation and Constraints

Our services would be read heavy; there will be more read requests compared to new Pastes creation. We can assume 5:1 ratio between read and write.

**Traffic estimates:** Pastebin services are not expected to have traffic similar to Twitter or Facebook, let’s assume here that we get one million new pastes added to our system every day. This leaves us with five million reads per day.

New Pastes per second:

1M / (24 hours \* 3600 seconds) ~= 12 pastes/sec

Paste reads per second:

5M / (24 hours \* 3600 seconds) ~= 58 reads/sec

**Storage estimates:** Users can upload maximum 10MB of data; commonly Pastebin like services are used to share source code, configs or logs. Such texts are not huge, so let’s assume that each paste on average contains 10KB.

At this rate, we will be storing 10GB of data per day.

1M \* 10KB => 10 GB/day

If we want to store this data for ten years, we would need the total storage capacity of 36TB.

With 1M pastes every day we will have 3.6 billion Pastes in 10 years. We need to generate and store keys to uniquely identify these pastes. If we use base64 encoding (\[A-Z, a-z, 0-9, ., -\]) we would need six letters strings:

64^6 ~= 68.7 billion unique strings

If it takes one byte to store one character, total size required to store 3.6B keys would be:

3.6B \* 6 => 22 GB

22GB is negligible compared to 36TB. To keep some margin, we will assume a 70% capacity model (meaning we don’t want to use more than 70% of our total storage capacity at any point), which raises our storage needs up to 47TB.

**Bandwidth estimates:** For write requests, we expect 12 new pastes per second, resulting in 120KB of ingress per second.

12 \* 10KB => 120 KB/s

As for read request, we expect 58 requests per second. Therefore, total data egress (sent to users) will be 0.6 MB/s.

58 \* 10KB => 0.6 MB/s

Although total ingress and egress are not big, we should keep these numbers in mind while designing our service.

**Memory estimates:** We can cache some of the hot pastes that are frequently accessed. Following 80-20 rule, meaning 20% of hot pastes generate 80% of traffic, we would like to cache these 20% pastes

Since we have 5M read requests per day, to cache 20% of these requests, we would need:

0.2 \* 5M \* 10KB ~= 10 GB

### 
5\. System APIs

We can have SOAP or REST APIs to expose the functionality of our service. Following could be the definitions of the APIs to create/retrieve/delete Pastes:

addPaste(api\_dev\_key, paste\_data, custom\_url\=None user\_name\=None, paste\_name\=None, expire\_date\=None)

**Parameters:**api\_dev\_key (string): The API developer key of a registered account. This will be used to, among other things, throttle users based on their allocated quota.paste\_data (string): Textual data of the paste.custom\_url (string): Optional custom URL.user\_name (string): Optional user name to be used to generate URL.paste\_name (string): Optional name of the paste expire\_date (string): Optional expiration date for the paste.

**Returns:** (string)A successful insertion returns the URL through which the paste can be accessed, otherwise, returns an error code.

Similarly, we can have retrieve and delete Paste APIs:

getPaste(api\_dev\_key, api\_paste\_key)

Where “api\_paste\_key” is a string representing the Paste Key of the paste to be retrieved. This API will return the textual data of the paste.

deletePaste(api\_dev\_key, api\_paste\_key)

A successful deletion returns ‘true’, otherwise returns ‘false’.

### 
6\. Database Design

A few observations about nature of the data we are going to store:

1.  We need to store billions of records.
2.  Each metadata object we are going to store would be small (less than 100 bytes).
3.  Each paste object we are storing can be of medium size (it can be a few MB).
4.  There are no relationships between records, except if we want to store which user created what Paste.
5.  Our service is read heavy.

#### Database Schema:

We would need two tables, one for storing information about the Pastes and the other for users’ data.

----

- Date: 2019-01-02
- Tags: #catherine #Interview/System-Design 
- Source URL: [](https://www.educative.io/collection/page/5668639101419520/5649050225344512/5653164804014080)



