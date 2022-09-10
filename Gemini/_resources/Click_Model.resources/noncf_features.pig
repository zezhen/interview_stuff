/**
 * Pig script to generate text features
 * @param UDFS : path for python scripts
 * @param INPUT : input modeling data path
 * @param OUTPUT : path where features will be stored.
 **/

DEFINE NormalizeUrlV1  com.yahoo.modeling.udf.NormalizeUrlV1();
DEFINE NormalizeHTML   com.yahoo.modeling.udf.NormalizeHTML();
DEFINE Bigrams  com.yahoo.modeling.util.Bigrams();
DEFINE FeaturePrefixAdd   com.yahoo.modeling.util.FeaturePrefixAdd();

REGISTER $UDFS/noncf_features/TextSimilarityFeatures.py USING jython AS TextSimilarity;
REGISTER $UDFS/noncf_features/util.py                   USING jython AS util;
DEFINE IP2ConnectionData com.yahoo.geo.iplookup.udf.IP2ConnectionData();

/*
DEFINE AttachIpConnectionFeatures(ImpsEvents) RETURNS EventsWithIpConnectionInfo {
  EventsWithConn = FOREACH $ImpsEvents GENERATE *,IP2ConnectionData(ip) AS ipConnInfo:map[];
  EventsWithIpFeatures = FOREACH EventsWithConn GENERATE *,
                                          ((ipConnInfo#'isp' IS NOT NULL AND ipConnInfo#'isp' != '') ? ipConnInfo#'isp':'UNKNOWN') AS ISP,
                                          ((ipConnInfo#'proxyType' IS NOT NULL AND ipConnInfo#'proxyType' != '') ? ipConnInfo#'proxyType':'UNKNOWN') AS PROXYTYPE,
                                          ((ipConnInfo#'connectionType' IS NOT NULL AND ipConnInfo#'connectionType' != '') ? ipConnInfo#'connectionType':'UNKNOWN') AS CONNSPEED,
                                          ((ipConnInfo#'asn' IS NOT NULL AND ipConnInfo#'asn' != '') ? ipConnInfo#'asn':'-1') AS ASN;

  FeaturesWithoutSpace = FOREACH EventsWithIpFeatures GENERATE $0..ipConnInfo,
                                          CONCAT('ISP=', LOWER(REPLACE(ISP, ' ', '_'))) AS ISP,
                                          CONCAT('PROXYTYPE=', LOWER(REPLACE(PROXYTYPE, ' ', '_'))) AS PROXYTYPE,
                                          CONCAT('CONNSPEED=', LOWER(REPLACE(CONNSPEED, ' ', '_'))) AS CONNSPEED,
                                          CONCAT('ASN=', ASN) AS ASN;

  $EventsWithIpConnectionInfo = FOREACH FeaturesWithoutSpace GENERATE $0..ipConnInfo,
                                                                      util.concatSep(' ',ISP,PROXYTYPE,CONNSPEED,ASN) AS ipConnFeatures;
};
*/

impressions = LOAD '$INPUT' using PigStorage();
impressionsFiltered = FILTER impressions BY
    (      (sec == 'ov-top')    -- Use only north impressions in modeling data
    --    (sec == 'ov-top' OR sec == 'ov-east')
        AND (iguid IS NOT NULL AND iguid NEQ '')
    );

-- Field order in projection should be same as that in schema.py.
-- Verify using bash "paste" command.
impressionsProjected = FOREACH impressionsFiltered {
               timestampPrefix = (timestamp IS NOT NULL? CONCAT((chararray) timestamp, '_') : '0_');
               dayOfWeek    = (((timestamp + 345600) / 86400) % 7);
               hourOfDay    = ((timestamp / 3600) % 24);
               partOfDay    = (((timestamp / 3600) % 24) / 6);
               dayOfWeekHourOfDay = (chararray) CONCAT(CONCAT((chararray) dayOfWeek, '_'), (chararray) hourOfDay);
               dayOfWeekPartOfDay = (chararray) CONCAT(CONCAT((chararray) dayOfWeek, '_'), (chararray) partOfDay);
  GENERATE
               CONCAT(timestampPrefix, CONCAT(iguid, pagePos))  AS iguidPagePos,
               CONCAT('Click::', (chararray) adSitelinkClicks)  AS click,
               'Weight::1'                                      AS weight,

               -- Constant bias feature.
               'CONSTANT=bias'                                  AS constantBias,

               -- Page placement features.
               CONCAT('DEVPOS=', LOWER(deviceCategory), '_', LOWER(pagePos))    AS devicePosition,
  (chararray)  CONCAT('SLK=', (chararray) sitelinkNum)                          AS sitelinks,
  
               -- Match type and algo features.
  (chararray)  CONCAT('MT=', LOWER(deliveredMatchType))      AS matchType,
  (chararray)  CONCAT('MA=', LOWER(matchType))               AS matchAlgo,

               -- Text similarity features.
               TextSimilarity.getTextFeatures(normalizedQuery,
                    NormalizeHTML(title), NormalizeHTML(description),
                    NormalizeUrlV1(targetUrl))                                          AS textFeatures,

               -- Location-time features.
  (chararray)  CONCAT('USRWCITY=', (chararray) woeidCity)        AS userWoeidCity,
  (chararray)  CONCAT('DAYHOUR=', dayOfWeekHourOfDay)            AS dayOfWeekHourOfDay,
  (chararray)  CONCAT('DAYPART=', dayOfWeekPartOfDay)            AS dayOfWeekPartOfDay,
  
               -- Sparse features.
  -- Currently query terms are already included in text similarity features and is based on raw query with porter stemming.
  -- (chararray)  FeaturePrefixAdd(normalizedQuery, 'QT=')                                         AS queryTerms,
  (chararray)  FeaturePrefixAdd(Bigrams(normalizedQuery, '\u0001'), 'QB=')                      AS queryBigrams,
  (chararray)  CONCAT('Q=', REPLACE(normalizedQuery, ' ', '\u0001'))                            AS query,
  (chararray)  CONCAT('DOM=', REPLACE(displayUrlDomain, ' ', '\u0001'))                         AS domain,
  (chararray)  CONCAT('DSP=', REPLACE(normalizedDisplayUrl, ' ', '\u0001'))                     AS displayUrl,
  (chararray)  (cbCreativeId IS NOT NULL ? CONCAT('CRT=', (chararray) cbCreativeId) : '')       AS cbCreativeId,
  (chararray)  (cbBiddedTermId IS NOT NULL ? CONCAT('BT=', (chararray) cbBiddedTermId) : '')    AS cbBiddedTermId,
  (chararray)  (cbAdgroupId IS NOT NULL ? CONCAT('ADG=', (chararray) cbAdgroupId) : '')         AS cbAdgroupId,
  (chararray)  (cbCampaignId IS NOT NULL ? CONCAT('CMP=', (chararray) cbCampaignId) : '')       AS cbCampaignId,
  (chararray)  (cbAdvertiserId IS NOT NULL ? CONCAT('ADV=', (chararray) cbAdvertiserId) : '')   AS cbAdvertiserId,
  (chararray)  (apCreativeId IS NOT NULL ? CONCAT('ACRT=', (chararray) apCreativeId) : '')      AS apCreativeId,
  (chararray)  (apBiddedTermId IS NOT NULL ? CONCAT('ABT=', (chararray) apBiddedTermId) : '')   AS apBiddedTermId,

               -- Ad source.
  (chararray)  CONCAT('ADSRC=', (chararray) adSource)        AS adSource,

               -- Query + page position conjunction for QNFP
  (chararray)  CONCAT('QPP=', REPLACE(phraseCanonQuery, ' ', '+'), '_', (chararray) pagePos)     AS queryPagePos,

               -- IP address features (derived later).
               ipConnFeatures AS ipConnFeatures;
};

--impressionsProjected = AttachIpConnectionFeatures(impressionsProjected);

noncfFeatures = FOREACH impressionsProjected GENERATE
       iguidPagePos                     AS iguidPagePos,
       click                            AS click,
       weight                           AS weight,
  (chararray) util.concatSep(' ',
            constantBias,
            devicePosition,
            sitelinks,
            matchType,
            matchAlgo,
            textFeatures,
            userWoeidCity,
            dayOfWeekHourOfDay,
            dayOfWeekPartOfDay,
            query,
            -- queryTerms,
            queryBigrams,
            domain,
            displayUrl,
            cbCreativeId,
            cbBiddedTermId,
            cbAdgroupId,
            cbCampaignId,
            cbAdvertiserId,
            apCreativeId,
            apBiddedTermId,
            adSource,
            queryPagePos,
            ipConnFeatures)             AS features;

noncfFeatures = FOREACH noncfFeatures GENERATE
    iguidPagePos                    AS iguidPagePos,
    click                           AS click,
    weight                          AS weight,
    CONCAT('Features::', features)  AS features;

STORE noncfFeatures INTO '$OUTPUT' USING PigStorage('\t', '-schema');
