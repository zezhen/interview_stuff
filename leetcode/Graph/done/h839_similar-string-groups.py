'''
https://leetcode.com/problems/similar-string-groups
https://leetcode.com/articles/similar-string-groups
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

Example 1:


Input: ["tars","rats","arts","star"]
Output: 2

Note:


	A.length <= 2000
	A[i].length <= 1000
	A.length * A[i].length <= 20000
	All words in A consist of lowercase letters only.
	All words in A have the same length and are anagrams of each other.
	The judging time limit has been increased for this question.

'''

import collections
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        def similar(w1, w2):
            mm = 0
            for i, ch in enumerate(w1):
                if ch != w2[i]:
                    mm += 1
                    if mm > 2: return False
            return mm == 2

        def swapTwo(word, w_idx):
            k = len(word)
            sim_idx = []
            for i in range(k-1):
                for j in range(i+1, k):
                    word_sim = word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
                    if word_sim in w_idx:
                        sim_idx.append(w_idx[word_sim])
            return sim_idx

        def connect(edges, visited, i):
            if visited[i]: return

            visited[i] = True
            for neighbor in edges[i]:
                if visited[neighbor]: continue
                connect(edges, visited, neighbor)
        
        A = list(set(A))
        n_words, n_letters = len(A), len(A[0])
        edges = collections.defaultdict(list)
        if n_words >= n_letters ** 2:
            w_idx = {A[i]:i for i in range(n_words)}
            for i in range(n_words-1):
                sim_idxes = swapTwo(A[i], w_idx)
                for j in sim_idxes:
                    edges[i].append(j)
                    edges[j].append(i)
        else:
            for i in xrange(n_words):
                for j in xrange(i+1, n_words):
                    if similar(A[i], A[j]):
                        edges[i].append(j)
                        edges[j].append(i)

        ans = 0        
        visited = [False] * n_words
        for i in xrange(n_words):
            if visited[i]: continue
            connect(edges, visited, i)
            ans += 1
        
        return ans
        
s = Solution()
# print s.numSimilarGroups(["tars","rats","arts","star"])
# print s.numSimilarGroups(["tars","rats","art","star"])

print s.numSimilarGroups(["gvdgdgudskiffjbepaqr","dukadjbvgfsigrdgpfeq","rjgqbskepagudvfdfdig","dfdibsvgdqagrugpfjke","fidgvbfdagrepjduskgq","vfpuakdjdggifdqbgesr","jpikvdgeffgadsdqgurb","gdvaiukdgbqjpgffsedr","gkugfqddgfvearpbdisj","svqdpkbffdgurjigadge","gedusqvifafgkddgbrpj","jdqugdvbgsifedaprgkf","qupdegjgaddksffbvgir","fdsdruggpbakfvidgejq","gasufpidgrdgfedbjqkv","igdsjuprebffggdqvkad","sgdffudjrqaidepgkbgv","rigsjkpddvfeuagfqgbd","gjrdaukqfvbigsefddgp","dqfugijdpfdesbgavrkg","vgfqgkjbsrpedafidgdu","sbdgkeauqfdgvgfijdrp","rgkgaeqjfpfudbvgsddi","fjsrggdqbugfpddveaki","krggudafebvddgpjifsq","jsevdufrpdfgiqgagdbk","dugrfqskdagbvigefjdp","fgqdddjbgsfikvaperug","dupkvgqjsibdfefrgagd","pgfeurfdajdvgbgidqsk","sergudagjddffkqbgpvi","iqfeurdsvkbgpdjfgadg","deafurijkvdsgpqbggdf","gdqbfsaddpregkvgifju","duffgqddiebgksvjprga","sbddkeauqfdgvgfijgrp","biurgedaksfqvgpdgdjf","rdsfgbddkuavfgeigjqp","gdgbsqduekgvfidarjpf","geddspfjqikagvbugrdf","qjudgfdgabfrgdvpksie","jgsfkvepdadggiqudrbf","jrfdqgepfsivkgdgabud","fidgvbfddgrepjauskgq","qaggdrdusfipgkbdfvje","ebsdpgkdvajiguqfgrdf","gipdvfbdgeqsfugdjrka","drdqgbuggvefjsipfadk","qdgpregdvfdsijfbugak","gqdruiadfgegspkdvjbf","jfrdadpgfsuqggbkidev","raejikdpgugqfsvdfbgd","djpgubvfsgkdrdaiqegf","drgvgaqbgpdifjsdfkue","sfgurdvqgiddfkapbgej","pfdaqvgsfgdduebgirjk","ekggdfrfdbujdgapsivq","gkggpdbeijqardvfusdf","gdedbviqparsfkujgdfg","epkggdurfjvfdbasgqid","egkgjfrfdbuddgapsivq","fagqgedpidudbgfsrkvj","gevgarbfdudgqsfpjdik","dvugdpkfaerbggdisfjq","dadvgpsqbegkfuigjfdr","dkggirjsabgfddupveqf","gdjvdprgfqdbufkiegas","sdikgjfgapurfebvgdqd","bqrakegsduddigfvpgfj","guafviekdrfgpqgdjdbs","dvadujgiqrgpksgbdffe","guafviekdrfgpdgdjqbs","qgddieprkvdbjafsgfgu","ggddpidsgjqfvbekafur","sdafvqudigdfgjbgrkep","dgrijeggqbpfadvskufd","addikfgvgsdujgbrfqep","fdadfgvdspiqgjreukbg","gjrfdbdkvsupgdaqfige","epgdfsjrqgvdfkdgauib","gedfspdjqikagbvugrdf","pfdakvgsfgdduebgirjq","gedgsqviffagkddubrpj","qgrjfsgafdgvdubpkeid","igddgavjkpegffdruqbs","vfdddggsrigkjqubpefa","sfgerdvqgiddfkapbguj","ubefkvdgrqpjsddgagif","ugbfvqdafggsjiddrkep","iqrgkgpevdagjddbuffs","dqufvrjfesdgibakggdp","arvgbgkesigdfpdqfjud","gujddpvrfsfdqkgbegai","ebsdpgkdvrjiguqfgadf","fdkajsbgegdfpgiruvdq","dfusbergpajqkvigdgdf","jbdfgqdkagueivgpsdrf","bsgdrifuvaeqjddggkfp","dpsffeakvgbudrdggqji","febrpgggisaddfudjkqv","fjsrpgdqbugfgddveaki","fgjddpseikvggdfabrqu","fdgudesvpkqfbjrgdgai","ifujrqdgpdevggsbkfda","vijreugkdgfqapdbfdsg","rdsfgbddkupvfgeigjqa","abrdqseguijvpfddgfkg","afsdgifdrekgvbpujqdg","uspjaqevggbfrgkddfdi","giggbrdkpsqefddjuvaf","kdbpqfurafggdgsevidj","apgkbujdrfgsddigevfq","kqfsggirpajvdgdebudf","rajpeqgdgfsgifudbdvk","dfudgqgkfprjgiebadsv","rgvjiadfqgfdduegbpsk","adsdepjrqdbgkgufgfiv","rjqdidbdsagkpgeuvfgf","vbdeggkfqddarpgjusif","ijkggvpuderbfdgfasqd","esjfqukdfrigpdgavbdg","vauqgrddiebffjgdgpsk","arvgbgkesigdfpddfjuq","ueifsgdjrpfbgdvgqdak","vbadsfiqudpedggrkgjf","fubqpddeggjgvrfsdkia","pudjbsfaggekdfvqrgid","idgrgfkjvafusdqebdpg","ebfqjpdfkiagdvgrsugd","fgiabsqddguverpkdgjf","ffskirbvdpdqagjuggde","krfgudafebvddgpjigsq","edbsgpdfuvargfkgjiqd","dgepsgiadvgjfdfukbqr","dqfugirdpfdesbgavjkg","rijpeqgdgfsgafudbdvk","qkivupaeddfbdjfgrggs","aiqurpgdsbefkgfjgdvd","dupkvgqjsibdfefgragd","viajpbfsrdqgdfudeggk","difgfjgsaqkedbrgduvp","fgdivgukdqbefrajpsdg","uvdbedfgagrkdjspigfq","dsadguvrfgpfkqejigdb","fdgugvprgbjiseddkqfa","gefgsqvidfagkddubrpj","kqfsggirpajvdgddbuef","jfaqpgkfgsbiddgevudr","gpifbsdgdavfkrjedguq","gjdaqgfukprfibdvedsg","dddrvaugksjbepgifgqf","gevgasbfdudgqrfpjdik","gdaievrqfkpgujsgdbfd","efisvgaggpbrduqdjdkf","vfdpaggsidqdubkgfjre","iqkggvpuderbfdgfasjd","apsdedjrqdbgkgufgfiv","ujgqfagdvfikpgdersbd","digsrkpfdbfjuageqgvd","fjfguidqbvgrgkdasped","fvdgggudjksfbidepaqr","sergudagjdfdfkqbgpvi","rpfeijagbusddggdvfkq","jgsfkvepdadgdiqugrbf","qavsderjkbuifgggfddp","rquggpvbkfgidjsadefd","dugrfqskdagfvigebjdp","gqbsrjfaekfiduggdvdp","uagrjdbidpsqgfdgvfke","rsgddvkbgpaegdifqfuj","kgbrdupvgiqsfgfjdead","vkrfgddbejusgfaqgpid","dpfgdedrfukqavbsgjgi","ffdbiadgvrsdggqpkuje","rdvkpfqgusfajgdeigbd","dfgpbjdkqsfireudggav","pdrqkgudajgsfdfgbvie","idfgurdjgpqfgkadevbs","buafsjgddvfgiregqkdp","dgfdrgsafdqkvjgbiepu","efisvgaggpbdjuqrddkf","dvgfdfpskagijubdgeqr","rqpgfjddbegusvaigfdk","addfrgjdsbpqgkeigfuv","darkddqgbfpfesjugvig","gfdkqrugsdbdpagviefj","jgqggredudfdpikasfvb","sdfkfrjqedvdgubpagig","fragjvspibefdqgdgkdu","egjpidbdrdffkausgqgv","fgdbigvarkfjgeupsqdd","gfdrfjugsvgipkdaebdq","gfidbsrudjggfevpdqka","ddkarfevgqsgfgibupdj","digfdvkrbguaedgfpsjq","beqapgkrvifsfgddujdg","ugdgvfrjddsbgaekqpif","fgkabdfrgdiqdgjpevsu","fvqgfjruskddegbgdpai","kipdvfbdgeqsfugdjrga","vdagqfpdgbifjeukgrds","addfrgjdspbqgkeigfuv","giugbrdkpgqefddjsvaf","sfdiuadkggbfvrjdpgeq","drgvddfiebsfgjgquapk","fudsvdgrfpkajdqgbgie","dvgfdfpjkagisubdgeqr","afsdgfidrekgvbpujqdg","sfdiuadkggefvrjdpgbq","dpiedgrfvbsadfjkgguq","fiavbfdsdduqkrgggepj","useabpqdgfgjdkdigrvf","dgfdrbsafdkqvjgigepu","dgedbvipqarsfkujgdfg","kgdusgfqgdivfbpadrje","saepgrqdkgdbgjvifudf","dadvgpsqfegkbuigjfdr","gfvkqrudsdbdpaggiefj","aigjpddsrdqvbfufeggk","jqirdddaekpfgggfbsvu","ipddskgbvggjqurfedfa","qgpdskefdbdfauigrjgv","dpgegfsgurijdvadqkfb","fpgudfqbkivgeagsddrj","gsdagdvbfeuqgfdijrpk","sfuadgjgbqdpgikdfvre","efbpikgfaugdsvddjgqr","svqgpkbffdgurjidadge","fguabsqvdgidrepkdgjf","bkvqgguejfgdpfrdaids","ddrfgvubjgpqkefagdsi","dpfguedrfdkgavbsgjqi","gsiaddrpbufvjgkgqefd","fdsrpgjqbugfgddveaki","vdagqfpdgbifjeukgsdr","ukpjaqevggbfrgsddfdi","svifqdaufgpkebgdjdrg","fgjvrkeddgdigaqpbufs","gdarqfpdgbifjeuksgvd","gaqbfsdddpregkvgifju","agdfburjksdqdvfegigp","qgbdggadkfjdpifesvru","biurgdesdafqvgpkgdjf","fdqgkiegfddsjrbvpgau","febrpgggidaddfusjkqv","qrdgjfdbggipsueakfvd","biurgdeskafqvgpdgdjf","uigqfagdvfjkpgdersbd","ifdbvseduggjrkpgfdqa","rdkgaeqjfpfugbvgsddi","rajpeqgdkfsgdfuibdvg","vsjrduabigdggfkqfped","ugbrjfgiavgskfddeqpd","bgfkprigdjddafguvqse","gevgarbfdudgdsfpjqik","jadvdpfruggsifeqgdkb","puigrgefgdqvadskfdbj","qsgapvkfidufjdbrdegg","vadeugspgkdrfqgijdfb","pfdakvgsfgdiuebgdrjq","uagrjdbifpsqgfdgdvke","gqjrdifdgdvpuaskbfeg","gduaivkdgbqjpgffsedr","ebddqjffvspguagrgidk","gdpgevsfqibgafudrkjd","pgsgijfdfvddqkugbear","ddkgrfevgqsafgibupdj","jipkvdgeffgadsdqgurb","efigkdqdjrgpdfbvuasg","pgsrijfdfvddqkugbeag","bgddgavjkpegffdruqis","rbguiqedvfapkdjfggsd","kgbrduivgpqsfgfjdead","afjdripuqgskvedfggdb","fbsdpgkdfajiguqegrdv","ugfvebqdasgrdfidpjgk","vffkibdggdjsgpdaeruq","aivjpdfsrdqgdfubeggk","jrvdagepbsikfgdgqfud","gdugbrdkpgqefdijsvaf","agduqdgreskidjfbvpfg","gpifbfdgdavskrjedguq","duiedgrfvbjadfskggpq","adjdgeqbggfkrdsivfup","gvpfdkdufdsrgqjbgaie","dpqfjidggabdurgevfks","ffskirbddpvqagjuggde","dvduaqdgrjegifksgpbf","sgdffudjrqaidepgvbgk","jrvdqgepfsikfgdgabud","fgbdjgdvfrgdakpiesuq","vffkibdgedjsgpdagruq","kqjrdifdgdvpuasgbfeg","darkddugbfpfesjqgvig","gbdegvkdqfdafpgjusir","iqjkfpesbfvgragddudg","jergudagsddffkqbgpvi","gepvrfqdggsukbfiadjd","resgjufadidgfkbgpdqv","fedkidggrgjfuadbvpqs","gsdagdvbkeuqgfdijrpf","baegqfjdipksdugdfvrg","dkasrdpefjfuqdigvgbg","ueifsgdprjfbgdvgqdak","digddvkrbguaefgfpsjq","rigspvegfdbfqudkdajg","dfkvaipdgfdsqgreugjb","rdjkpfqgfsuavgdeigbd","dgfdrbsafdqkvjggiepu","ddffsuberpkggavdgqij","fgpqeuvdasibdggdjkfr","fiavbfugdddqkrggsepj","eiufksggqgpjdfbddrav","duksdjbvgfaigrdgpfeq","asdgjkgrgufqbepfdivd","fgfqgkjbsrpedavidgdu","dpfgdedrfukgavbsgjqi","vgsbefrgifkddpgajduq","djbsrdpvefagkiqfdugg","dugferigpfkddvgbqasj","rgpggdafevdqfsdbujki","dfpibsvgdqagrugdfjke","qsgapvkfgdufjdbrdeig","eiufkgggqspjdfbddrav","bgdaudqvfjekspfgirdg","vfpuaedjdggifdqbgksr","arfggdkvpusqejdfbgid","dfrfvgdgsqagpdkiejub","gddpifjqgvdakgesfubr","pfdasvrqfgdjuebgigdk","krjadpggfsudefidbgqv","dgapgkvfjfdisruedgbq","ffdarsjepkggvdibugdq","biurgedskafqvgpdgdjf","pgigrfajqsdkfveugbdd","dvgfefpskagijubdgdqr","fgbdqedvfrgdakpigsuj","ebsdpgkdfajiguqfgrdv","dugdfqskragbvigefjdp","dvdgggudskiffjbepaqr","pfdaqvrsfgdjuebgigdk","gjdaqgfukpefibdvrdsg","sjigfqdafbpkgudegvrd","esjfqugdfrigpdgavbdk","rvigqbdgpdafufdegsjk","bdeggdufsvapjfdgirqk","efdrskgjqgivfdgbpdau","gdqpregdvfdsijfbugak","rajpefgdkfsgdquibdvg","drfbiudaegkfvpqsgdgj","qkgedsgpjdurvabfgfdi","vfdgadrdpgqfkiuejgbs","uigqfagdvfjkpgdsrebd","skgddrgbipevgfduajfq","prvfdgdasgigkuqdbfje","dveukdrjggqbisgafpdf","gfsrgjipgddqefvdubak","gfudgqdkfprjgiebadsv","ddfigreqagbdpvsgfukj","vadeugspgidrfqgkjdfb","jifkvdregpgadsdqfugb","ikgagqdvjerbpfdsgufd","fjaqubvfsgkdrgdidegp","uadefsdgjgkvifgqrdpb","ukbfgqefdgdigdajprvs","fedggrjasduqibdgvfkp","sdrkjqapgggiddfbvefu","feqgggapkvubrdfsdidj","iadegugrpffbsddjvkqg","febspgggidaddfurjkqv","qfkbggvepdsjddfgarui","duegbvipqarsfkgjddfg","dpsfferuvgbkdadggqji","fiqpgkgdjgaedrbdvufs","pgigrfajusdkfveqgbdd","biurggpsdafqvgekjddf","fbfggaudkjqdedrivgps","brqgkagjedpfsfugvddi","arvguskfpgdqejdfbgid","efigsdqdjrgpdfbvuakg","asdgjkdrgufqbepfgivd","gejdrggpuiasvqfbkddf","qgdadejvdurgfgbspfki","dquffrjvesdgibakggdp","gfqdbskrddguifajepvg","jkbvsdqapggdeigrfdfu","bvefdrdfsggaugkjqpdi","afgjgdqkufvgbderdpsi","sfqgpfbkvdgirjudadge","eqdjgdduvsagfprkgifb","jipkvdgegfgadsdqfurb","dvbfkijuefqrgggdadsp","qpsjgrdfddggvefbikau","edfkpfgrijddbgsuavqg","fiavbfdgdduqkrggsepj","sigfkdfdudbravgegpqj","fjaqubvfsgkdegdidrgp","dedrvaugksjbdpgifgqf","grggqudsfadpefikdvbj","qgddieprkvabjdfsgfgu","frgdvapkejdbigsufdqg","gkqbafdrefusjddgigpv","dfrfvgdasqggpdkiejub","fgugeaqbrkpdvdjdgsfi","dvqgdisagderpjufgbkf","djagubvfsgkdrdpiqegf","gfqdsbkrddguifajepvg","ijkggvpuderbfdgfsaqd","gbdpqvuaddsriegfkfgj","dfkvaipdqfdsggreugjb","duiedgrfvbsadfjkggpq","fgiabsqvdguderpkdgjf","fdgudesvrkqfbjpgdgai","vekdaggdqdugjrfspibf","gedgsqvifafgkddubrpj","geddrggpuiasvqfbkjdf","pfdaqvgsfgdjuebgirdk","fgpqguvdasibdgedjkfr","dgskfgguerdqifbjdavp","deqdfiubagjsfvdkgprg","rpfidjagbusddggevfkq","sgvfafdqjdepgkdgrbiu","dpkgegjrfdsfbgaquvid","pukqbdedjdrggfsgvfai","skfbqudgggpvdiredfja","fbjdrkvaifpgsdugqged","ddrfgvubjgpqkedaifsg","agfbdqdsipdrvekugjfg","upffkiagdsgjqddrbgve","fbidrkvajfpgsdugqged","sdgefguvabqjkfdidrgp","gekbvfgqarfupddjdisg","eggjkdvugdbffaqpsrdi","jadufpedfrdiqgbsggvk","fgidrkvajfpgsdubqged","gdefjudivdgkprqgbsfa","afsdgifdregkvbpujqdg","sgvbjdadgrgifpqukedf","krfgpdafebvddgujigsq","fgiabsqdeguvdrpkdgjf","sjgfbdudpeavrifkqgdg","ekqjdbsgrfauvigfdgdp","drggvaqbgpdifjsdfkue","dqasrdpefjfuidkgvgbg","divrkjbdsufaepfgggqd","kgdusiaqgdgvfbpfdrje","fgfugkjbsrpedavidgdq","dgqdrgsafdfkvjgbiepu","geqarvjigdsgdkufbpdf","egjpidbdrdffkvusgqga","deqdgiabugjsfvdkgprf","bsddkeauqfdgvgfijgrp","sadffudjrqgidepgkbgv","fgugeaibrkpdvdjdgsfq","qvpefjugfdbadidgrgsk","rfijkgagufvsdpqbgedd","fgdbegvajkfrgiupsqdd","ipddskrbvggjqugfedfa","jdsfkvepdadggiqugrbf","iprdskdbvggjqugfedfa","bvdgggudjkiffsdepaqr","safbqdjfegvkrdgpudgi","eadfggfrbgddiksvqpju","aivjpddsrdqgbfufeggk","fedvpkidsgrgdqgaubjf","pfrgvsbegdgdkijudaqf","fdfdgdagvgirbusepkqj","fvgkpusbdfdjraiqgegd","efgpqbkjursddgfdigva","dgedsgiadvgjfpfukbqr","jqseggravgdpkdfdufib","keqjdbsgrfauvigfdgdp","deqdgiubagjsfvdkgprf","dvrqpidkbejfdasguggf","rpfiejagbusddggdvfkq","fdgguvprgbjiseddkqfa","fgkabdfrgdiqdgjsevpu","fgbdqgdvfrgdakpiesuj","iqjffpeskbvgragddudg","gdugbidkpgqefdrjsvaf","rquggpibkfgvdjsadefd","gfvbqrudsdkdpaggiefj","qsdgffdbggiprueakjvd","gjrfdbdevsupgdaqfigk","arvgudkfpgsqejdfbgid","bdqjfgdrfekagpvdgusi","gpggjfvkadqisefuddrb","gddpbfjqgvdakgesfuir","gjdaqgsfkprfibdvedug","pukqbdedjdsggfrgvfai","aivjpbfsrdqgdfudeggk","vbdeggkfqddafpgjusir","fdguaesvpkqfbjrgdgdi","sfveqbkfjpudgdgrgadi","jfiguqgkdfgdrvepasbd","jadvdpfeuggsifrqgdkb","fedbiadgvrsdggqpkujf","qibskgafpdugfdvejrgd","qgddieprkvfbjadsgfgu","qrdgffdbggipsueakjvd","rqpgfjddiegusvabgfdk","fpkajsbgegdfdgiruvdq","uggfvqdafbgsjiddrkep","dgrijeggqkpfadvsbufd","bpfidjqgrusddggevfka","idqbpfgdageuvjdgkrsf","gfabdsjgrvpdiugfdqek","iudjbsfaggekdfvqrgpd","ddrfgvubjgpqkedagfsi","gkugfaddgfveqrpbdisj","qgrjgvedikbsdpafudgf","bdgefguvasqjkfdidrgp","gefsvudkadggbjqfdipr","vudfdgrpsdgikajbgefq","igfgrpegsdukbddjvqaf","agfqdrdsipdbvekugjfg","rsgdddkbgpaegvifqfuj","gfdrfjugsvgdpkiaebdq","rkvbgdqgaigsepfudjdf","jbefdvkgrqpusddgagif","grjdbukqfvaigsefddgp","dgfigreqddbapvsgfukj","fbjdrkvaifegsdugqgpd","krdajpggfsudefidbgqv","dsbkedrpfqvgafjgdgui","ksugdgargfbdjedvpiqf","bufqpddeggjgvrfsdkia","iedfuvdrbfdjpkgasqgg","ubfivgsddgaefpdkjgqr","gasqfbgdpkdvguferjdi","edbsgpdquvargfkgjifd","dvugdqkfaerbggdisfjp","pbfdkavdirgesufgqgjd","iqjkfpesfbvgragddudg","krggudafebvddgjpifsq","qaggdrdusfipgkvdfbje","fakjqbesvgdudgrpifdg","kpevdgddgjgsuqfabfir","agfqdbdsipdrvekugjfg","adbgegjurqdkdvfipsgf","dpsfferkvgbudadggqji","gdedbvipqarsfkujgdfg","djagubvfsgkfrdpiqegd","skigqvejffdrbdadggpu","bvefdrdfpggaugkjqsdi","ugggvfrjddsbdaekqpif","bsgdjifuvaeqrddggkfp","qvabeidrddffkgsgujgp","uiddkedbpavgqfgfrsgj","efrgsdqujdgpifbvdakg","gbdegvpdqfdafkgjusir","ksdjvfddebqfarupgigg","aqbvfpgikrgdjegfsdud","gpdsfdduvkaifeqgbrgj","rgpggfafevdqdsdbujki","pafvgsfjbegdigudrdkq","fgrkjupfggdvdbdasieq","frdgkggdjvuaqsifbpde","fgrfgvkbjpiseddaqdgu","gdqdregpvfdsijfbugak","jipkvdregfgadsdqfugb","kgdusgaqgdivfbpfdrje","qrvguskfpgddejdfbgia","dvbgdqkfaeruggdisfjp","dvgjfkdbipdserafuggq","krfggdpebajusgfvdidq","afsdgfidqekgvbpujrdg","dfgeaispujqfrdgbdgvk","ffdsvdgrupkajdqgbgie","fdsrpgvqbugfgddjeaki","pbggersdfjdqdvugfaik","sgdffudjrqaidepgbvgk","ebfdagkdvrjiguqfgpds","abkeripsugdqgdvjgdff","jgfsdpdeikvggdfabrqu","gujgsbedgqffvikaprdd","gqdkfvrudjgspigfdeba","edqjkpdugrgiafgbsfdv","bdkqgdgpigjuafvfrdse","adjdgeqbdgfkrgsivfup","jrkdqgepfsivfgdgabud","sdgeigudabqjfkdfvrgp","iadegrgupffbsddjvkqg","sdfkfjuqedvdgrbpagig","kbrjuevgadpgsdqfgfid","gjdaqgsukprfibdvedfg","feadfgvdspiqgjrdukbg","rgpggfafevdqdsubdjki","dpjfgevaidgsrufkdbqg","djasrdpefkfuqdigvgbg","gsdufjqfdkdggbeiavpr","fbjerkvaifdgsdugqgpd","rqjugbvgfdikpgdedfsa","fiqpgjgdkgaedrbdvufs","kefridgfgddjvqsgpaub","sddfkgaqfjgvdbepgiru","qidvgggfjkaeddfrbups","efdgsdqdjrgpifbvuakg","kdrqpgudaggsfdfjbvie","kpjfdibqdgvdraguegfs","kdfidbsjfguvrapgqdeg","fjagubvfsgkdrqpidegd","bideufrkvjfsgggqdapd","jskrfguddfvggeqbpiad","sfveqbkfjpidgdgrgadu","rgbqfdvdkspdeajguigf","rdkgaeqjfpfudbvgsdgi","dpfeijagbugdrgsdvfkq","dpsffeakvgbuddrggqji","dqkfddauvrspfbjgggei","dujffeddgrqgsbkiagvp","ffsdirbddpvqagjuggke","fgdivsukdqbefrajpgdg","pudjbsfaggekvfdqrgdi","gdqdregpvfjsidfbugak","qjfagpddivgurfegbdks","fgdduefgagripsdqjbvk","rifuddevbgqjpfadgskg","grepfjbaqdkgufdgdsvi","sdafbqudigdfgjvgrkep","uvffsidgkbgejgdadrpq","pgfekrfdajdvgbgidqsu","gjrdbukqfvaigsefddgp","efisvgaggpbdduqrjdkf","vbpufedjdggiadfqgksr","ebfdpgkdvrjiguqfgads","ffdbiadgvrsdggqjkupe","dkggirjsabgfvdupdeqf","fpddbejgsdvugrgiaqkf","igrfggdsukfqdepdjvba","juqfggrfegpbskaddvid","dqvjrpsffkbiadgugged","pegsgaukgfbvidqjdrdf","vgsefkirdpgufdgdjbaq","arfggdvkpusqejdfbgid","vkfbqudgggpsdiredfja","siduqfgfrdjkepdggbva","beqakgprvifsfgddujdg","kivupgdgfgdfeqbdjrsa","rqjugbvgfdikpgdedasf","qgpdsgefdbdfauikrjgv","rpdsfdduvkaifeqgbggj","gejqrggpuiasbdfvkddf","dupkvgqjsibdfefgradg","gfedbkqijrgfdpgvasud","dqsgbdpgkaujifvefgrd","fjfguidqbvgrekdaspgd","djagubvfsgkfrqpidegd","addikfgvjsduggbrfqep","fvdgggkdjusfbidepaqr","frvfdgdpsgigkuqdbaje","dkdgirjsabgfgdupfeqv","drbgdqkfaevuggdisfjp","dkdgvuqdagjpfbsefigr","vfdpdggsidqaubkgfjre","qupdegjgaidksffbvgdr","spgkadufgvrdjqdiebgf","dvgjfkibdpdserafuggq","adugevfqgirdbspkgdfj","drfbiudaegkfvpqsgdjg","vgsbefrgifpddkgajduq","fpkedgdubfvjagdgrsqi","gbefdvkjrqpusddgagif","rajpeqgdgfsgdfuibdvk","bdgaudqvfjekspfgirdg","skigqvejfgdrbdadfgpu","sjgfbduvpeadrifkqgdg","dfiefdbgkgvrsqugdjap","apsdfdjrqdbgkguegfiv","gdadqfpdgbifjeukgsvr","qrvguskfpgdaejdfbgid","qgrifseafdgvdubpkgjd","vfpufedjdggiadqbgksr","rigsjkpddbffuageqgvd","rdjkpfqgusfavgdeigbd","dvdufbjsrdqigkfgaepg","gdrgdaibjefvgkfqpusd","sdfbqajfegvkrdgpudgi","fgidrkvajgpgsdubqfed","qerdpjiffudbdgvkaggs","biurgdpsdafqvgekgdjf","dugdfvskragbqigefjdp","qupdegjfaidksgfbvgdr","gjkudbdedsfgvqrifpag","fguabsqvdgiderpkdgjf","ikavsqgujrbfepddgfgd","edqjbpdugrgiafgksfdv","pfdasvrgfqdjuebgigdk","gdrgdvibjefagkfqpusd","qjsfgrekdaggbivdfdup","gdfdfdagvgirbusepkqj","gejqrgspuiagbdfvkddf","dpfguedgfdkgarbsvjqi","dpgegfsgdriujvadqkfb","rgibavddjpgqdgfeusfk","gjsfgedfiagprkdbdvqu","fjaqubvfsgkdrgpidegd","gjsfgedfiagpqkdbdvru","ibguqgjdsrgavdefkdpf","rpfidjqgbusddggevfka","idvkpfqgusfajgdergbd","eavgifqdsbkfgpgdrduj","jrvdagepfsikfgdgqbud","gfjdqkpgdedfsriuvgab","kiqpgjgdfgaedrbdvufs","vdadqfpdgbifjeukgsgr","efdgsdqujrgpifbvdakg","ekggjfrfdbuddgapsivq","uavjdedgkrisfbgdpqgf","vgabefrgifpddkgsjduq","dpfeijagbusdrggdvfkq","jebgkqaudffgvddigprs","jaqgbgkfgreipdusvdfd","jkqsvfgegdddbfpguria","dejvafqipbgrdgkgdsuf","rufdpijqgdbvkdggfase","vbdeggkdqfdafpgjusir","fpqgdjugdriksbevgafd","jebgkfaudqfgvddigprs","juggsbedgqffvikaprdd","arvggdkfpusqejdfbgid","jigsrkpddbffuageqgvd","ipadskgbvggjqurfedfd","ddfarfevgqsgkgibupdj","adgidffgrpsduegqkjbv","dfgerdvqgisdfkapbguj","gedusqvifafgddkgbrpj","fskrafvepgddjggibdqu","eadfggfrbgddiksvqjpu","rfegpdjgsdavgikubdqf","fgdskgubepiqavfjdgdr","dvsfdfpjkagigubdgeqr","dbrfdvuagkpjsfeqidgg","jffsrddbkpgvdgigquae","dsavgudrfgpfkqejigdb","qegabpgddgfufrkjdvis","kiqpgjgdfgardebdvufs","ggpfsgddibrqedfjukva","vaujgfkpgdqfdsdribeg","gpkedgdubfvjafdgrsqi","auesgbigddfpgfrdqvkj","dkdgirjsabgfgdupveqf","dpfguedrfdkgagbsvjqi","udaedgkbrifvjfsdpgqg","vfdgadrpdgqfkiuejgbs","fguabgqvdgidrepkdsjf","easfqigbpkgvugddjdrf","dpeggfsgurijdvadqkfb","bvdgggudskiffjdepaqr","deqggiabudjsfvgkdprf","rbguiqedvfapddjfggsk","gfbdksvfdapreugjgdqi","kdggdfbeqpjvarufgisd","fpgudfqbkijgeagsddrv","fbpggvgkdsfejdurdiaq","fagqgedpidfdbgusrkvj","vgdsjuprebffggdqikad","gisgbudaqpfgkverjdfd","kpjfdgbqdgvdragueifs","dveugdrjggqbiskafpdf","qspagedjrgukdfvbgifd","deqggiabugjsfvdkdprf","sqdpdfggbervgukdaijf","gaqgeupkbdrfsidvgfjd","aivjpdfsrdqgbfudeggk","iagsprdfqgbugddekvfj","fjfbuidqgvgrekdaspgd","aqbvdpgikrgdjegfsfud","grdkfejagvpgsudbdfiq","gfidpbgdufkvadjegsqr","qupdegjdagdksffbvgir","fdqgkiegfddsjpuvrgab","fagudesvrkqfbjpgdgdi","gfbpikgfaugdsvddjeqr","kdfspgrvgqdjefidbuag","dgegbvipqarsfkujddfg","vdediufdbgsrgpqkgafj","vfbddggsrigkjqudpefa","deqgigabudjsfvgkdprf","qpsjgdgfddrgvefbikau","vfpufedjdggiadbqgksr","afgjgdqkufvgbderdspi","dgfigreqadbdpvsgfukj","fbgijpdvdfgauqkregsd","sdfkfruqedvdgjbpagig","gdarqfpdgbifjeukgsvd","rfijkgagefvsdpqbgudd","svqgpfbkfdgurjidadge","gkqbafdgefusjddgirpv","pkbesivfgdgargjddquf","jigsrkpfdbfduageqgvd","ggjreadfpqigdvdkfsub","ffdarsjepkggvdiubgdq","pudjbsfeggakvfdqrgdi","grgpafdbigdqkudfjsve","gqugdpdvdiaebjfrfksg","arvfdgdpsgigkuqdbfje","gefdrggpuiasvqfbkjdd","dvjkgqipfredsbgdafug","pbdgefruvdgikasjfqdg","sbdgkeduqfagvgfijdrp","puigrgqfgdevadskfdbj","saedgrqdkgdbgjvifupf","frdguqjdvdgsebkfgapi","fgjugkfbsrpedavidgdq","dpsgegarfdkfbijquvgd","adsdeqjrpdbgkgufgfiv","pudjbsfaggekdfvqrgdi","dpkgegarfdsfbijquvgd","jsdrpkidefdfbuvqgagg","kdrqpgudajgsfdfgbvie","skagdrgbipevgfdudjfq","fsegjdkgfgpvqruddaib","krjggdpebafusgfvdidq","fgdrpebskdvfaggdijqu","deafurijkvdbgpqsggdf","ajdikfgvgsdudgbrfqep","apsqgfdgbedfdjukrvig","kujffeddgrqgsbdiagvp","sugkdagdfedgjfbqripv","esrbdgafgdipfqvjkdug","dfudgqgkfprjigebadsv","jfsdgdprgkufebvqgadi","qgddieprkgdbjafsgfvu","kgdusiaqgdgvbfpfdrje","ubefdvkgrqpjsddgagif","dgakfusfjbdepvqggrid","ebgfqpduskavggjdrdfi","pgrkjuffggdvdbdasieq","sjgfbdvupeadrifkqgdg","sdgeiguvabqjfkdfdrgp","pgjkruffggdvdbdasieq","bgiqjrvffkeugpgsddad","apdqfgfrbgjdvdgsekui","ukbdgqeffgdigdajprvs","drgaddfiebsfgjgquvpk","bdpqeiggkgadujvfsfrd","edufsgjpdkqvfbggidra","ggjreudfpqigdvdkfsab","grepfjbaqdkgufdgdsiv","iedguvdrbfdjpkgasqgf","esjfqugdfrigpdgadbvk","fgjsdpdeikvggdfabrqu","ibguqgjdkrgavdefsdpf","dgfdrbsafdkqvjggiepu","gejqrggpuiasvdfbkddf","fudsvdgrfpkajdbgqgie","gpdugigvbrjfeafdkqsd","jfaqpgkfgsbidvgedudr","bduadfqfgjkdirgvepgs","dufeifpgdjqkbgdsvrga","vkrgddifeqsbgudjgfpa","gigdvsdqfubpgdkefrja","gdrdfqkjabdeufvgpgis","rigsjkpddbfeuagfqgvd","rjfibqgudvkdgdfepasg","qgrjivedgkbsdpafudgf","gsiaddrgbufvjgkpqefd","dqasrdpefjfukdigvgbg","qpsjgdgfddrgvefuikab","qrbjgkevdufdgpgifads","drfgpedjkbsggaidqfuv","gpjdgrsdudiqavkgfbef","sfqgpfbkvdgurjidadge","pgigsfajurdkfveqgbdd","gdfdfdegvgirbusapkqj","kveudidgdsfbgqgfrapj","efbpikgfguadsvddjgqr","puirjvdbkesgafgqgdfd","dfpibsvgdqagrugkfjde","pefdiqsbavfgjudgkgdr","dfpsbivgdqagrugkfjde","qvekibgfddgjgraufdps","vdegiufdbgsrdpqkgafj","uadefsigjgkvdfgqrdpb","rdjkpfqgfsuavgdgiebd","egpdsgqfdbdfauikrjgv","grggdudsfaqpefikdvbj","vesdaggdqdugjrfkpibf","jrdkfegagvpgsudbdfiq","saedgpqdkgdbgjvifurf","fgjvrkeddgdigaqpbfus","gsjavpgrbdqieddukffg","dpgegfsguridjvadqkfb","fgdbigvajkfrgeupsqdd","fgrfgvkejpisbddaqdgu","rfggpdjesdavgikubdqf","rdsdgbfdkupvfgeigjqa","ksgapvqfgdufjdbgdeir","bvdgggudjksffidepaqr","adgidfqgrpsduegfkjbv","rafdgjgskdguivbqdfep","giugbrdkpsqefddjgvaf","gefsvuddakggbjqfdipr","dgapgkvfbfdisruedgjq","kdggdfbeqfjvarupgisd","dkggiqjsabgfvdupderf","vdegqfpdgbifjaukgrds","sfurdgjgbqdpgikdfvae","vapdgqdsjffbkgedgrui","idqbpfgdagervjdgkusf","dqadgjbudfgksevgfrpi","bgdskgufepiqavfjdgdr","gdaievrqfkpjugsgdbfd","kpgidgqfasdrdgjbuefv","qaffdkdigpbgjvgsreud","biurgjpsdafqvgekgddf","fbsrggdqjugfpddveaki","efdibsvgdqagrugpfjkd","dvduaqdgrjegiffsgpbk","rdaedgkbuifvjfsdpgqg","eavgifqdsbdfgpgkrduj","jkqsvfgrgdddbfpgueia","gepvraqdggsukbfifdjd","fdbpergvsuqidkfjggda","dfvrgjdqdpfbkgueasgi","qgrjfseafdgvdubpkgid","brqgkagfedpfsjugvddi","sfjbuaefiprvqgddgdgk","febspgggidkddfurjaqv","baegqfjdipksdugdvfrg","gfdkqruvsdbdpaggiefj","dddefrbpggufajgvisqk","sfigjqdafbpkgudegvrd","gdqjkpdugreiafgbsfdv","dpkgegarfdsfbgjquvid","kgifsguvjradgdfbeqdp","udaedskbrifvjfgdpgqg","gevgarbfdudgisfpjqdk","ridsfkfaggdubdjvqegp","ddrfgvubjkpqgedaifsg","eqigkdfdjrgpdfbvuasg","iqgaddggeuvfdbfpsjrk","avddufbiegfqdkgjgsrp","dfugvgjdgikasdqerfpb","fajvrkeddgdiggqpbfus","sdgeigduabqjfkdfvrgp","dffuqasrvddgjgbekpgi","gdrgdvibjefkgafqpusd","absifgedpkrfjdvgudqg","vkrgddiefqsbgudjgfpa","skgadrgbipevgfdudjfq","igrfpgdsukfqdegdjvba","gersgdaqkgupffvbdidj","ugdgvrfjddsbgaekqpif","dvqgdisagdefpjurgbkf","gjsfgedfiagprkdqdvbu","gudrqiadfgegspkdvjbf","qpsjgdrfddggvefbikau","sdgefguvabqjfkdidrgp","pdukgjsfdgaqigvbrdef","kddfggsdviaguerbqpjf","rggvdgkedbufiaspdqjf","srujqbggkipaegddffdv","sifkfjuqedvdgrbpagdg","rdaeddkbuifvjfsgpgqg","degugbdgiqadvfjkpsfr","gkdgbsgpqdfvfeidajru","uagrjdbifpsqgfdgvdke","qpfgagejdrvufgsdikdb","sugkdaddfeggjfbqripv","pfgdeavqgkgdrsjfbdiu","biurgedaksfqvgdpgdjf","fakjqresvgdudgbpifdg","ddkgrfevgqsbfgiaupdj","jdfidbegfrgapgksvuqd","geddspfjqikagbvugrdf","fdqgkiegfddsjruvpgab","sdikgjfggpurfebvadqd","fgbdqedvfrgdakpsgiuj","qdfdfgebgjapdsugikrv","apgkbujdrfgsqdigevfd","iadegugrdffbspdjvkqg","gbefdvkqrjpusddgagif","edufsgjpkdqvfbggidra","dskabjdvggqdifgruepf","uddqggrgabvfeikfspdj","ksgapvqfgdufjdbrdeig","uddbedfgagrkvjspigfq"])


'''
class Solution(object):
    
    def checkSimilar(self, word_0, word_1):
        n = len(word_0)
        
        ct = 0
        for i in range(n):
            if word_0[i] != word_1[i]:
                ct += 1
            if ct == 3:
                return False
                
        return True
    
    def swapTwo(self, word, w_idx):
        n = len(word)
        sim_idx = []
        for i in range(n-1):
            for j in range(i+1, n):
                word_sim = word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]
                if word_sim in w_idx:
                    sim_idx.append(w_idx[word_sim])
                
        return sim_idx

    
    def connectNodes(self, node, edgess, visited):
        
        if node in visited:
            return
        visited.add(node)
        neighbors = edgess[node]
        for nei in neighbors:
            self.connectNodes(nei, edgess, visited)
    
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n_words, n_letters = len(A), len(A[0])
        edgess = [[] for i in range(n_words)]
        
        if n_words >= n_letters ** 2:
            w_idx = {A[i]:i for i in range(n_words)}
            
            for i in range(n_words-1):
                sim_idxes = self.swapTwo(A[i], w_idx)
                for j in sim_idxes:
                    edgess[i].append(j)
                    edgess[j].append(i)
                    
        else:            
            for i in range(n_words-1):
                for j in range(i+1, n_words):
                    if self.checkSimilar(A[i], A[j]):
                        edgess[i].append(j)
                        edgess[j].append(i)
        
        visited = set()
        n_groups = 0
        for i in range(n_words):
            if i not in visited:
                n_groups += 1
                self.connectNodes(i, edgess, visited)
                
        return n_groups
'''