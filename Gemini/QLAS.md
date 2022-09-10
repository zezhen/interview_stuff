# QLAS
----

**[Introduction](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/QlasDocs.html)**

Query Linguistic Analysis Services (QLAS) is a service which provides linguistic analysis of queries. At a high level, QLAS takes below as input.

1.  a query
2.  a context associated with that query, e.g.  the user who issued the query, the location, the time, etc.
3.  a configuration
4.  parameters for overriding configuration defaults on a per-query basis


The output is a single object which contains its analysis of the query, which consists of these main aspects:

1.  Modification
    *   A modification is either the original query or some modification of it. An example modification would be a spelling correction. Note that by "original query" we mean a normalized query (normal UTF-8, lowercase, whitespace trimmed), as opposed the "raw query" which the user typed in the search box.
    *   An analysis will have the original query "modification" and zero or more true modifications.
2.  Span
    1.  A span is a substring range of a modification, along with an associated class and referent.
    2.  The class is some classification of the span according to the [QLAS Span Schema](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/QLASClassTaxonomy).
    3.  The referent is an optional identifier for entities for uniquely specifying that entity within the class.
    4.  A token is the simplest span. It has a class of token and no referent. A more complex span is Michael Jordan with class person\_name and some referent to distinguish the entity from some other person\_name entity with the same name. Spans may overlap but must nest within an interpretation.
3.  Interpretation
    1.  An interpretation is a set of spans that cover the query which make up a single certain interpretation about the query as a whole.
    2.  For example, the query cafe sydney may have one interpretation with the span cafe syndey meaning the entity that is the cafe named Cafe Sydney, and one interpretation with the span cafe the business category and sydney the city.
    3.  The interpretation may also have a decoration containing the specific meaning
4.  Decoration
    1.  The analysis, modification, interpretation, and span objects all have an associated set of decorations.
    2.  A decoration is a key value pair and the key is unique within the set. Keys are strings and values can be any JSON value.


**QLAS Analysis Process**

**Tagging/Entity Detection**

Each query is run through all the configured taggers to generate more spans for the internal analysis. The taggers tend to run in the order shown below because the model-based taggers can tag advantage of the previous tags (dictionary, pattern, etc) as features.


1.  Matcher
    *   a simple tagger which looks up sequences of tokens in a dictionary called the knowledgebase. All consecutive sequences of tokens in the query are looked up and the lookup is by exact string match. Each hit creates a span of the class, referent, and attributes associated with it in the knowledgebase.
2.  Pattern Tagger
    *   generates spans by matching single tokens against patterns, detecting code spans of class fedex\_tracking, isbn, ncode, phone\_number, upc, ups\_tracking, usps\_tracking, vin.
3.  WOE Tagger
    *   uses libinternetlocality to detect a location in the query. Currently it detects only 0 or 1 most likely locations. A detected place\_name span is decorated with the WOE ID.
4.  Contextual Tagger
    1.  Several machine learned contextual taggers run to detect spans of different classes. [**CRF** models](https://en.wikipedia.org/wiki/Conditional_random_field) are used almost exclusively; spans detected this way are decorated with the tag and sequence probabilities.
        1.  Product tagger: classes brand\_name (manufacturer and model), product
        2.  Local tagger: classes organization\_name, place\_name (city and state), business
        3.  Person name tagger: class person\_name (for detecting any person name, not just notable people)
    2.  There is another 2-level contextual tagger nicknamed **QI**.
        1.  The first level is a CRF tagger whose tag set is the set of all [QLAS](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/QLAS) span classes in the [QLAS Span Schema](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/QLASClassTaxonomy).
        2.  The second level is a Maximum Entropy tagger that assigns up to one decoration to the span, typically a node in the most important taxonomy for the class. The top sequences are store later as a source of interpretations.

****
**Interpretation Generation**

Each interpretation is run through a set of rules written in [Jabba](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/Jabba) to add decorations for what the interpretation means as a whole. Each interpretation will match zero or more rules. Any matches will show up in the domain decoration of the interpretation.When the Jabba interpreter is run prior, these decorations are added at the time of interpretation generation to save time and this step is skipped.


1.  Powerset Interpretation Tagging
    *   The powerset interpreter simply generates all possible segmentations of the query from the bag of spans, each one creating an interpretation.
    *   The maximum number of segmentations and the maximum number of interpretations to generate can be set.
2.  Jabba interpretation generation
    *   The jabba interpreter generates an interpretation for any possible sequence of spans that matches patterns from a Jabba file in the configuration.
    *   It does this without having to generate every possible sequence and test against all patterns, by using backtracking in the Jabba state machine.
3.  QI  interpretation generation
    *   Sequences saved from the QI tagger are emitted as interpretations.
4.  Null  interpretation generation
    *   This interpreter makes sure the token-only interpretation is always generated, even when the powerset bails out.



![[Archive/工作资料/Gemini/_resources/QLAS.resources/unknown_filename.png]]

**QLAS Span Schema**

A major function of [QLAS](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/QLAS) is to find spans of text (substrings) within queries that have identifiable meaning. It [labels](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/NextGenSearch/KnowledgeDefinitionV2.html) the spans with a representation of their meanings.


**QLAS Interpretation Schema**

A domain decoration in QLAS interpretations is a notion of what the interpretation means as a whole, below is an example, there are three kinds of domain/schema: Jabba and lm.
decorations=
 \[domain\]->\[
 {
 "name":"product",
 "schema":"jabba",
 "slots":{
 "category":\[ 5 \]
 }
 },
 {
 "name":"domain\_product",
 "schema":"lm",
 "prob":0.861912
 }
 \]


1.  Jabba
    1.  Jabba domains are created when an interpretation matches a [Jabba](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/Jabba) rules, e.g. event, local, product, travel, weather, etc
    2.  Jabba is a regular language for matching or generating sequences of structured text and defining associated actions and used for contextual tagging, query classification, query filtering, generating overrides, and more
    3.  read more from [jabba tutorial](https://archives.ouroath.com/twiki/twiki.corp.yahoo.com/view/P13nContextual/JabbaTutorial.html)
2.  Language Model
    1.  LM domains are created when an LM classifier decides the query is in a class with a certain confidence prob between \[0, 1\].
    2.  class will be one of autos, local, product, travel.
3.  





----

- Date: 2019-03-19
- Tags: #Interview/Gemini 



