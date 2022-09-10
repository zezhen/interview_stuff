/**
 * Pig script to generate EC and COEC features
 * @param INPUT : input modeling data path
 * @param OUTPUT : path where generated features will be stored.
 **/

DEFINE Feature     com.yahoo.modeling.util.FeatureFormat('~');
DEFINE FeatureJoin com.yahoo.modeling.util.ConcatSep(' ');

impressions = LOAD '$INPUT' using PigStorage();
impressionsFiltered = FILTER impressions BY
                     (      (sec == 'ov-top')    -- Use only north impressions in modeling data
                      --    (sec == 'ov-top' OR sec == 'ov-east')
                            AND (iguid IS NOT NULL AND iguid != '')
                     );

cfFeatures = FOREACH impressionsFiltered {
        timestampPrefix = (timestamp IS NOT NULL? CONCAT((chararray) timestamp, '_') : '0_');

        q_dsp_ec   = Feature('Q_DSP_EC', q_dsp_ec);             q_dsp_coec = Feature('Q_DSP_COEC', q_dsp_coec);
        q_dom_ec   = Feature('Q_DOM_EC', q_dom_ec);             q_dom_coec = Feature('Q_DOM_COEC', q_dom_coec);
        dsp_ec     = Feature('DSP_EC',   dsp_ec);               dsp_coec   = Feature('DSP_COEC',   dsp_coec);
        dom_ec     = Feature('DOM_EC',   dom_ec);               dom_coec   = Feature('DOM_COEC',   dom_coec);
        q_ec       = Feature('Q_EC',     q_ec);                 q_coec     = Feature('Q_COEC',     q_coec);

        q_btt_dsp_ec = Feature('Q_BTT_DSP_EC', q_btt_dsp_ec);      q_btt_dsp_coec = Feature('Q_BTT_DSP_COEC', q_btt_dsp_coec);
        q_btt_dom_ec = Feature('Q_BTT_DOM_EC', q_btt_dom_ec);      q_btt_dom_coec = Feature('Q_BTT_DOM_COEC', q_btt_dom_coec);
        q_btt_ec     = Feature('Q_BTT_EC',     q_btt_ec);          q_btt_coec     = Feature('Q_BTT_COEC',     q_btt_coec);
        btt_dsp_ec   = Feature('BTT_DSP_EC',   btt_dsp_ec);        btt_dsp_coec   = Feature('BTT_DSP_COEC',   btt_dsp_coec);
        btt_dom_ec   = Feature('BTT_DOM_EC',   btt_dom_ec);        btt_dom_coec   = Feature('BTT_DOM_COEC',   btt_dom_coec);
        btt_ec       = Feature('BTT_EC',       btt_ec);            btt_coec       = Feature('BTT_COEC',       btt_coec);

        q_bt_crt_ec = Feature('Q_BT_CRT_EC', q_bt_crt_ec);      q_bt_crt_coec = Feature('Q_BT_CRT_COEC', q_bt_crt_coec);
        q_bt_ec     = Feature('Q_BT_EC',     q_bt_ec);          q_bt_coec     = Feature('Q_BT_COEC',     q_crt_coec);
        q_crt_ec    = Feature('Q_CRT_EC',    q_crt_ec);         q_crt_coec    = Feature('Q_CRT_COEC',    q_crt_coec);
        q_adg_ec    = Feature('Q_ADG_EC',    q_adg_ec);         q_adg_coec    = Feature('Q_ADG_COEC',    q_adg_coec);
        q_cmp_ec    = Feature('Q_CMP_EC',    q_cmp_ec);         q_cmp_coec    = Feature('Q_CMP_COEC',    q_cmp_coec);
        q_adv_ec    = Feature('Q_ADV_EC',    q_adv_ec);         q_adv_coec    = Feature('Q_ADV_COEC',    q_adv_coec);
        bt_crt_ec   = Feature('BT_CRT_EC',   bt_crt_ec);        bt_crt_coec   = Feature('BT_CRT_COEC',   bt_crt_coec);
        bt_ec       = Feature('BT_EC',       bt_ec);            bt_coec       = Feature('BT_COEC',       bt_coec);
        crt_ec      = Feature('CRT_EC',      crt_ec);           crt_coec      = Feature('CRT_COEC',      crt_coec);
        adg_ec      = Feature('ADG_EC',      adg_ec);           adg_coec      = Feature('ADG_COEC',      adg_coec);
        cmp_ec      = Feature('CMP_EC',      cmp_ec);           cmp_coec      = Feature('CMP_COEC',      cmp_coec);
        adv_ec      = Feature('ADV_EC',      adv_ec);           adv_coec      = Feature('ADV_COEC',      adv_coec);

        usr_q_dom_ec  = Feature('USR_Q_DOM_LT_EC',  usr_q_dom_ec);  usr_q_dom_coec  = Feature('USR_Q_DOM_LT_COEC',  usr_q_dom_coec);
        usr_dom_ec    = Feature('USR_DOM_LT_EC',    usr_dom_ec);    usr_dom_coec    = Feature('USR_DOM_LT_COEC',    usr_dom_coec);
        usr_q_ec      = Feature('USR_Q_LT_EC',      usr_q_ec);      usr_q_coec      = Feature('USR_Q_LT_COEC',      usr_q_coec);
        usr_ec        = Feature('USR_LT_EC',        usr_ec);        usr_coec        = Feature('USR_LT_COEC',        usr_coec);

        ecCoecFeatures = FeatureJoin(q_dsp_ec,      q_dsp_coec,
                                     q_dom_ec,      q_dom_coec,
                                     dsp_ec,        dsp_coec,
                                     dom_ec,        dom_coec,
                                     q_ec,          q_coec,

                                     q_btt_dsp_ec,   q_btt_dsp_coec,
                                     q_btt_dom_ec,   q_btt_dom_coec,
                                     q_btt_ec,       q_btt_coec,
                                     btt_dsp_ec,     btt_dsp_coec,
                                     btt_dom_ec,     btt_dom_coec,
                                     btt_ec,         btt_coec,

                                     q_bt_crt_ec,   q_bt_crt_coec,
                                     q_bt_ec,       q_bt_coec,
                                     q_crt_ec,      q_crt_coec,
                                     q_adg_ec,      q_adg_coec,
                                     q_cmp_ec,      q_cmp_coec,
                                     q_adv_ec,      q_adv_coec,
                                     bt_crt_ec,     bt_crt_coec,
                                     bt_ec,         bt_coec,
                                     crt_ec,        crt_coec,
                                     adg_ec,        adg_coec,
                                     cmp_ec,        cmp_coec,
                                     adv_ec,        adv_coec,

                                     usr_q_dom_ec,  usr_q_dom_coec,
                                     usr_dom_ec,    usr_dom_coec,
                                     usr_q_ec,      usr_q_coec,
                                     usr_ec,        usr_coec);
    GENERATE 
        CONCAT(timestampPrefix, CONCAT(iguid, pagePos)) AS iguidPagePos,
        CONCAT('Click::', (chararray) adSitelinkClicks) as click,
        'Weight::1' AS weight,
        CONCAT('Features::', ecCoecFeatures) AS features;
};

STORE cfFeatures INTO '$OUTPUT' USING PigStorage('\t', '-schema');
