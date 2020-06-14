#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们给出两个单词数组 A 和 B。每个单词都是一串小写字母。 
# 
#  现在，如果 b 中的每个字母都出现在 a 中，包括重复出现的字母，那么称单词 b 是单词 a 的子集。 例如，“wrr” 是 “warrior” 的子集，
# 但不是 “world” 的子集。 
# 
#  如果对 B 中的每一个单词 b，b 都是 a 的子集，那么我们称 A 中的单词 a 是通用的。 
# 
#  你可以按任意顺序以列表形式返回 A 中所有的通用单词。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# 输出：["facebook","google","leetcode"]
#  
# 
#  示例 2： 
# 
#  输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# 输出：["apple","google","leetcode"]
#  
# 
#  示例 3： 
# 
#  输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# 输出：["facebook","google"]
#  
# 
#  示例 4： 
# 
#  输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# 输出：["google","leetcode"]
#  
# 
#  示例 5： 
# 
#  输入：A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo
# "]
# 输出：["facebook","leetcode"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length, B.length <= 10000 
#  1 <= A[i].length, B[i].length <= 10 
#  A[i] 和 B[i] 只由小写字母组成。 
#  A[i] 中所有的单词都是独一无二的，也就是说不存在 i != j 使得 A[i] == A[j]。 
#  
#  Related Topics 字符串

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        ans = []
        counterB =collections.Counter()
        for sub in B:
            for char,n in collections.Counter(sub).items():
                counterB[char] = max(counterB[char],n)
        # print(counterB)
        for word in A:
            if not (counterB - collections.Counter(word)) :
                ans.append(word)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

big_A = ["qyfltnfphn", "rxnaoymlsh", "dxemqpgmlk", "nmwmwwaxrs", "sxgjnracmk", "nftybtfwmi", "xrbnenadsm", "tscteswveh", "fradngxsmr",
         "rnsmmimaxu", "xxbsagrnmh", "dvylwdbihx", "dksuclcwwc", "ynharsxmoq", "llusfcgext", "mnxarsmuea", "ibwxjtxvih", "jvoursbocg",
         "fugjniqmbx", "xhrnorbmas", "lmxchguteu", "xamnxsromu", "apvnmrqsxw", "dfzddaufvi", "eawdyiuxyx", "gvconbeywb", "nmxeqrausb",
         "gwyxrasqmn", "emasdxsrnn", "ttvwfcsrjs", "whdanbhvjc", "gvrvanrxms", "nabszrmgcx", "kawserpfkt", "wrasxmjenz", "jghfhofphx",
         "kgyyurspls", "bemszxqrmi", "wneasjvxmr", "qnmbtzrsxa", "cyeqsgospe", "jrxaomasnb", "faxsnmvsvr", "dllofblfxf", "uhmaysrxna",
         "criimolvww", "atsxbgrynm", "xnkrsxaskm", "knrysmxatp", "ystjraxmnt", "sydzvjmjiw", "xryasmmucn", "uvjcptpgld", "kxjtnarrik",
         "jkeacnrsmx", "xwntwwwqxz", "jhjyyokcvc", "arrmtrxnns", "rxkfeltwwr", "xnmrslxayl", "onderyufeb", "ivwvwaskvu", "ungttqntla",
         "bnsaxvrxmn", "czifqhrqdj", "najrymlxsd", "gagprlmmbt", "chcmukkbkx", "mxrasbnage", "mbhsojafxa", "axntxmsgrs", "hcejzsygsn",
         "samyxrfnmu", "nfqlgslfte", "srfbknmhax", "jamtasfeia", "dhqgqbhxlk", "zfjerbumle", "mwhczdxnsu", "aeobxfygbk", "uwylqxksyy",
         "smvtlidfkt", "dnsraxmkaq", "jnjcsgtlfx", "eukjqerhyj", "lyfmhxzckl", "duibgrijsy", "srlmnzuwxa", "xdmnsaacnr", "pgmnmdnusa",
         "ansrxhkygm", "jnsekamtrx", "fymxiaycrv", "lbivftcjii", "bmkaxsnrje", "kosmnmarxh", "avrnhhwgyu", "axsnvrmmxj", "iksedeywhs",
         "zxztmerkiw", "pnrwxrsazm", "dtxrransmd", "zbcsecmedk", "salmxrnfgw", "mwfymexdmt", "reasexsncm", "frsnxisaam", "mtanxroejs",
         "fhmyxarsfn", "saanymarxe", "ijyjajkmkx", "mwasuxnrwc", "afjwxvbbzw", "osatnrzxvm", "nrihcbtrlw", "aqoyeydzks", "xdgspkyxgr",
         "ecwvbmmbbn", "xngasmrvaz", "sfguydgrbi", "xnspmnrmaa", "jyjlwkbrgb", "ygpeflzwyd", "fkncsfrjoc", "hyrzefgfih", "asxyqqnixc",
         "ctgxmnrsab", "nsnavmnxrz", "rubjhwpiry", "fjqqrenrzw", "vsxayrnmnw", "anrxsmbgkb", "sksvfeknyg", "jswgfihdnh", "zjgyujkuhd",
         "wzzcyrnpoe", "xwjueiqope", "sinwxbunip", "anlxrsallm", "zhwiboqcpx", "kbneqsanhi", "thzoryzvzo", "vppmfvwzqc", "ijolocbzin",
         "rfgmxknasg", "mrbxoadzsn", "saqnxmtria", "jxnsmrrsaz", "mxonajssrf", "xmnrlsrsat", "nsvamxrnne", "mssrxtnaux", "racwsmwnnx",
         "taisfhrnxm", "fugpzkerzl", "waiacbovii", "ragnomsbxc", "gceyadwjid", "sltimtbbqe", "ixmxkrngas", "sroxmafons", "bodrcejsui",
         "gieqlssdzp", "nsraxeboam", "tdxrphrxer", "urnamxashs", "nsmraxlamh", "nmxxsacxrf", "obgsixxvky", "mrnxqzqdas", "xrsjenasym",
         "xmraisnaek", "ydekuvcuod", "yikeaksxar", "hyfyppzwam", "sqaxprnmxd", "mnrnalmwsx", "spnwmyxroa", "wkiffzyodb", "swzlnzqzpr",
         "vhocvroqph", "alzbmgddqa", "axnlzasrrm", "gldcqxfofh", "txpnrvyasm", "dxmngnaesr", "sexbkmjczl", "exhkidgeva", "abnikzyajx",
         "okmotiygbm", "nxmxcsrqba", "ppimkpeoqc", "fpjoekarel", "ytqfbgbbof", "gyzboiydub", "mxamrhsncn", "asmqyrnfdx", "cgadqjpkxw",
         "nsemovxars", "sxwxrmhnia", "ovxmmnsrsa", "mxsmarwnxc", "nmarxpaavs", "msralnsoxy", "aekpwlwsny", "vtgsbaglmq", "tsnyaemirx",
         "mrepaksznx", "ujqlagbeoy", "xeqsqrunam", "sarmnemxuq", "ekmblnivfp", "vaxuhxghki", "rcawmlfxns", "scaxanmryx", "rsioxdvhfv",
         "mxrnhkvsla", "rnrwsxnfma", "hvsrjankxm", "psajmxzxnr", "dhvbhtepcf", "vupaghuzxq", "hismezqtri", "zbdvzudcnf", "bqxzrigjkh",
         "manmrbskxx", "hppetkzyun", "ammirxnosc", "eelxezaizb", "esmkxidrjj", "vlcztoqrgz", "aycrmnxsrd", "jrnxtnnmas", "fktfzdzkya",
         "jjuhwjvojh", "wxvemhjero", "bfltyaluev", "nsaximsari", "rdaxisname", "fgnqgilhmc", "bsxkneqntk", "gmltrrjsob", "fsivxochti",
         "bkebaledff", "uguimjdmzv", "ramxswnrmu", "umfsujnlfw", "norxuasmsj", "eleiedjduc", "asxnaqrcmx", "qbqfiaumwn", "hmsrwnqxau",
         "rngsamrsux", "owfxwedjhr", "lrdsmnxabg", "rwdwnsmxav", "jbheoabmul", "wkrnxxapms", "wxamwvrsdn", "bdiyhwahyv", "vwcirlxroo",
         "oxbvfpluvb", "jaaygnekvc", "vkauilpehs", "dcrshxnath", "egrcccqrnp", "rmnasxhhrr", "mxjsnrvmal", "oxsruybgme", "mrnalrmxys",
         "xgcrmhayns", "tyjaampjji", "mediqbvwlq", "ktgbzgehrn", "bgdybankyr", "urfyxsneam", "vrnmxvzzsa", "vgiyhguhao", "oxqasnmfnr",
         "hvsrjtcckk", "nxrhtknykm", "axanwsymcr", "xumxrsngac", "sqmknmrrax", "idnovkaupt", "epomnpqwrd", "dacrdctfak", "nnkrvedirc",
         "hxanemrvsd", "rdosaomrxn", "xrxwxnamsp", "zrjxjsanvm", "zyxcronmas", "znarjauhlv", "ktewjcrhju", "ohrryweiwp", "rznapxsmwq",
         "areiirhlau", "gmpjlcyjlq", "zxnaronsam", "ryzxvmnast", "hfesjxnarm", "orvxnmnsal", "sawbhaxidt", "sydlzromrt", "zxsafrmsnk",
         "czdmggufxe", "xihrssnmah", "vsthkbvafu", "snjdmpmxra", "nomrexfsya", "masxqpnnrs", "txyuildvhe", "lzrlpdmnnk", "urzwrhksoq",
         "qpwrphwfgy", "ywaxyegmff", "xhnsmsamri", "sarmxrlnco", "qdeupbmyqq", "nrmlrxusat", "gaqhmnrswx", "namxmrsstn", "gjwshlgsut",
         "esmcaxnnzr", "xprnamsesk", "gharasxomn", "dyrnexanms", "asycylstjt", "ptmnsrixan", "rexxhvzgcn", "nearmqlssx", "xmrgvmrsan",
         "arvxxmxsnd", "bixzkiypuq", "yxawkpxjny", "ncxnccsmar", "hlmrursxna", "rvuabujvii", "pkgcccdzwt", "gtqsflolaw", "wcewjbxrrx",
         "nqrasyxdmx", "nlpoqbqvbs", "arssnxyamm", "mstcxanraj", "atxtnnskmr", "mgciwkwndo", "ribyaewndo", "vwolvbbcgr", "nmbwrslaxn",
         "xalsyrysnm", "sxphznnmra", "othbvvqmwl", "vzuhdzwyzh", "gmfsayrhnx", "emxogreuuj", "yoojsixgex", "mdwasnxdrn", "slnlrzxmax",
         "sxgrfpnmaj", "gavyahhziy", "zpmmxkfyxz", "ragamfsnrx", "lonpfehenp", "eyonafvech", "rbzxpnsgam", "dgsgxamirn", "mjrsghaxgn",
         "rvxacmksnf", "mnpbjbuxjn", "jlbdkpykcy", "mtrinsarxj", "nmsrrxrqan", "mwckukfebo", "tscxqgnmqs", "amrkxyrnas", "zklljevbco",
         "vucmxrsnia", "nlsubxmrva", "bekzrhesfs", "egaisppfjk", "ixnmsxyrap", "sxafcjnrml", "haqtvfnlfe", "osjmynrgax", "gnwyfvpixa",
         "xmasrnexaa", "axxmrrnsos", "ntrmsyapxu", "rmssidnaxv", "ewngcavrvt", "mrbmsaxcmn", "amtlrsngsx", "smrwxbniaw", "fcysiqtisv",
         "rernalvmsx", "pnrxasmswx", "nraxymszfc", "nfcxapsrsp", "nxxzwmaosr", "kcuzkzggbn", "lsugnmraax", "rvapnksamx", "qzrgsmnuxa",
         "hktwblsrhr", "nhaxrhsjmz", "agnrmwrxes", "kvvjndwkik", "hpnhsurinz", "avxsrnlsem", "cvzjjlnjes", "asmnytpxrf", "apsxamtnir",
         "oiuwwsoqsx", "qwxmcnarsz", "vpzrepejus", "dblmsnxarf", "aniwjmxrsf", "jdlxdwbdts", "rpdppbwtcm", "wmiaeszwkl", "mvrxsmnago",
         "kgassmrznx", "olngrxtror", "jrnamsxgnl", "lxdrvsmnxa", "iiictidobw", "wlssqxlwdw", "nosmerxfat", "rxomianrsw", "xanrmqxvts",
         "xrzasxnkim", "srasymnxao", "sdgnmaxmrm", "dxrfrxmnas", "ncgxamrgds", "phhnckmufk", "eqfreiatza", "esarixnrjm", "vckwfmwsjt",
         "shmrcgnxla", "dvmlfykwiu", "qgtddslopo", "mdlxcnarsn", "naaslxmrsg", "csgbvkfgsv", "hcbjtwppqs", "swukegpsse", "rrmxsajnlt",
         "mrysmxkxna", "qiqffmjfgj", "cezczfwwec", "rnxtmvsabe", "usyrxafnmw", "rxnsnathmm", "sbhprxwnam", "amasslnxrz", "axsrjnpmam",
         "mzsslraxgn", "tvjktxqngh", "qqootmmyjh", "xcgcepjnnq", "raygxnscrm", "rzbjxelavn", "xzukfuypoq", "amqspnryxv", "namsxmrsdq",
         "xnarfwirsm", "nmrsxachqn", "bcmbsxkkwy", "zsqtxvyagg", "niokzstoix", "yatnnsrvxm", "qfafsxrngm", "tycmxsnoar", "aasmanlxrw",
         "oanjgpzcsp", "irhmaxjsrn", "msbnfkwrxa", "xrvnasekmi", "nxsrawmtka", "dsmjkxnarn", "gtthbwlqow", "naxrupsdmu", "nqbaxgomrs",
         "anmosmdprx", "idkyzkguxp", "auunmsxfrt", "kqwxrnsanm", "ajdxaonsrm", "qydvamdpjl", "hpndnsozwo", "txasmnmetr", "srnfeuxmap",
         "fmpcvcwovd", "rxwmrfanbs", "bmkwhzitno", "kjmjxfgvjg", "lovozumzek", "aimximnrds", "wkilhrbpyf", "uwdxoplttb", "nsmqegravx",
         "unkiyelqqp", "axeplmnsry", "almsnuyrxi", "vsgsiwfaqz", "nabsrmsxhn", "bnmxasprey", "irdqvilxlc", "rsxmaemein", "hinsamrxnv",
         "ejbncwrmib", "faxsrdmnxa", "oxwszaprmn", "omrkitubyp", "xiakthumag", "xmcrsrnoca", "svianbrxmj", "lfavtxenpb", "rmnxrsasos",
         "eyvzfvuprz", "erogcvmrmz", "iutyeagton", "nxnxsqmard", "lashrlumxn", "mgdhtxpuru", "javmrxsmsn", "ypdjjghbug", "znmasruxgy",
         "yasrrnklmx", "tgtxxmyale", "arnfsmvayx", "qtwvvubwph", "fgaexfnmre", "cjfusjccfi", "njtyzfrmkj", "ixdwnmasrj", "smaejrzjxn",
         "zasmrkitpb", "cqnkoznezp", "spmpanrxsb", "tmuwdwpsdr", "sqqeqmgnoi", "retkayuueu", "rmsxmvgafn", "ynkwawdydk", "nemxwrsfas",
         "szemranxmn", "ugjhkfpfvn", "bafgzqtsmc", "amzneroxis", "inkdzriiit", "nmrgfsxkao", "bkcqqdlskz", "urfxnmssma", "anmxrxrspy",
         "nagbxprmas", "uavoigugzv", "zcoinnqeyh", "aukjszdqck", "dgmxkrsanz", "rrxdnrsoam", "yrsmansfxa", "zjbgapnfib", "amxxtnlsrh",
         "mglastrnjx", "owcmrgpkbz", "grxmbizjcq", "cznrxasmii", "mlfvlgdvju", "ksnxzyrmam", "xnnamjmjrs", "xmgaznrsrf", "hclrdkvbgl",
         "nnrnjxmsxa", "nxkmarirxs", "wsmqbrnxan", "ebamznxdsr", "mdaebonrsx", "xaurnrwmws", "nbpwpuzisp", "wgvvjfdsqb", "orxlnmtsda",
         "xahnsbncmr", "xnpuwpkhzh", "jspahptyik", "hrnmsazrxr", "trrcaxmnsd", "bsmdnapmrx", "rixlaasndm", "algmrsnxxc", "amqxtlnrsf",
         "rpgxmohfsa", "csvsonbsia", "mnwaysvrax", "qmmqehiogr", "xzlsamrqng", "xrapmrspns", "cwuqbckawt", "hhdjmszdnp", "yvznmsqtkf",
         "xrcanmrosw", "hdeqxdmyzb", "wsrnamdxxa", "blvpyfvcey", "rhaswxyfhi", "khtievhdqw", "zmbvwjkvcm", "xhkhqukxjj", "vxurznmsay",
         "xnyrnaklsm", "qyxvvmfqkd", "fubnadmhdq", "wmskinmlho", "wywxnwvocu", "axastfovah", "rzayxmssnx", "rjmhnusxar", "snhhraimax",
         "efdnqmxsar", "umfrnosxva", "vbojcpsapl", "mpxhsvnavr", "ziljxjwsru", "ryqcruamgo", "zkeacamset", "slygbbruch", "evhrlqpchl",
         "nleqasrjuz", "ijktjmmkmk", "nrgtmnsaxx", "sirmvmxxan", "esamonrxan", "cwlnlhwbov", "djlkhtdjof", "ecyczcdkkb", "cvcecrxkmb",
         "ahrxsnaams", "jusvamcrxn", "mwbarxxvkt", "dnsaexgmfr", "uvdhyzgsxi", "xsmblwarvn", "syjrxaavnm", "axhryaknms", "vsfhespyrj",
         "coxfbomsnh", "rwjjfgeaua", "mxxrdzafsn", "dkdkstkrdr", "svlwupivpg", "eookdewgyc", "njakrkanau", "nxpkmsavre", "azvlxynlke",
         "erxsbanmjr", "rzdjsixgfx", "sxxnmlraam", "aablpxhgah", "uzrzlrtjwi", "hrakzapeuu", "sanrmhxczw", "yqsyraxmnt", "cmsxxrnazy",
         "pfjvfiqivq", "ibwjzynwvq", "swmanrkvrx", "mtfxbrnsoa", "mdanxrcsgd", "twglivfrcl", "nzspzrdulg", "xsrnsecavm", "qmvnsirxau",
         "rxqnmszoan", "mqvxhvrykc", "ashmermanx", "xaaxmrrwsn", "jmxirntsra", "akxrkwonms", "bzozsnlbtw", "cvqxvgrbpa", "bxnvasmrse",
         "ptykifqzoc", "gtqzzgrasa", "dyfbrsyduk", "dwhbuhujqi", "mwwsodizdi", "rlayamsnlx", "psylobxxfb", "ysmnmaxara", "naxgsmyerz",
         "bebyoljpir", "wyntzxpscv", "bstlmxsiao", "rbigdjfhsv", "mrxnstokas", "qyyujsjzys", "ayxryxmsns", "sdbmfmevmk", "sramnaxsyq",
         "sxmnxvfraa", "ixyigapcps", "nxmaraxdrs", "yrxsvgsanm", "pmtaxrrsxn", "uxymsrnkav", "gtuoslllec", "zmsapybtny", "nxawsvgmmr",
         "hxrtsagmgn", "wvmxplmjdg", "ekiicghxdp", "vumujzzhpf", "uzgdtjxscm", "bnbsfsotrf", "ghsuttpfwa", "azujpiodyi", "celthyegpp",
         "xajmnrohos", "roqjjnsyjy", "qexrqzscai", "cmsxmjcnar", "mnrlesxdsa", "easjgmqtfg", "mrnjsqxfta", "urvudiyshp", "rmxdhwnsai",
         "mnlxcuqxgl", "ohcbauasqx", "olzpqqdirh", "xomubhuark", "rnamsgxlbo", "cppqfdncwk", "urhnayxmrs", "smmcmnjpci", "xpdmnkarls",
         "cxsfaxmgus", "enqmnapxsr", "nmhrnaqsxr", "ofmqcxtook", "drynshyvde", "qgrmxsaakn", "dcgijuzlyq", "nmxaxansrn", "nihramsxue",
         "exmgcinnmc", "kmasrixnsk", "mrgnyxmasr", "snxamrxwpe", "vuxyukyvdr", "xazumfnrsn", "vmrndmxsad", "qezucfhiwj", "zojasaifot",
         "ppklczomyk", "pjshnfnxpe", "ebrllddqbe", "nnnrwrxmas", "vmrzsuxang", "ntewjwslvx", "fwreidvelz", "njnxisrlam", "xmncrssajt",
         "czubrwrdry", "bncerswyyz", "cqfebgyjwx", "ijsraqmnxj", "mtxraosnub", "lmuhfrnsxa", "mssrxainzs", "xnilsraamh", "jkxkqrnysi",
         "zfwpgcqsqm", "ihmwbqxaua", "cqnabjhttj", "iksqrisnvq", "sxramtaesn", "rlamhvqcdc", "sssrdkkxje", "xlnmnssbar", "prxfwwnqll",
         "lsyxynklum", "hrnssmaunx", "kbfnluxert", "gjxnryamso", "jzzehkorou", "svnmafwrxl", "qprjtakdje", "sunrgahxcm", "scnhrmavmx",
         "darmscxqnq", "onemsqatxr", "sregfknamx", "eqkboatdtd", "xlyorhubyf", "demnimqqqn", "wifovewqow", "ocleuynlcc", "bjmnuzpxao",
         "qusozeiyes", "nrxasumrfe", "bmgxpztyty", "pjawqncaqm", "aensxlcmer", "vbwkyorvle", "pmxwsrsnaq", "mrsrnxwjxa", "xfzpjzoscp",
         "azumxrmsan", "geyaadzdpp", "fnsaxlaimr", "emwnscraox", "rseonarmex", "ansmtlxqgr", "vsspanawut", "artniensxm", "iazxmvsrnd",
         "mjyunxzars", "pqentliwti", "tweuilloym", "oicuvstguq", "gqahmnjsxr", "stsysmxran", "xyjaynweoy", "uedammqmlq", "nxajjfrbsm",
         "rguzqvkztj", "mmzxwhajvo", "usufapvlyw", "sqxonamrtc", "lcrbnfidvk", "qjsprmzhne", "xsamynroum", "xansrncbmh", "naxlbmvlsr",
         "syrqnamjrx", "ppheoxnycu", "rszugaaxmn", "nnssaeoxrm", "ocmgpaenvi", "oihgrexaji", "pqsfjnjflx", "stubbikyuz", "fsnmxaonjr",
         "denmpxpwrf", "aobqzhvfut", "ujtwyphmra", "reassomnhx", "nodrkmsgxa", "amnksrxyob", "mxqsrqdank", "mgrmtablkp", "xzmnamlszr",
         "xrwmnkmsqa", "namxrmfrsb", "holymlsvav", "ianmczrsxp", "iilqmuzfig", "axrnsomnux", "pdmrjwiggq", "axdbdcldta", "jzuwriavme",
         "xgvtnmrmas", "yplzbkdnuz", "anlmquxrse", "nasoozrxmm", "bpzzowjche", "yassmztxrn", "xrnasjmysg", "fsugfkrnls", "xnsaamarrw",
         "zrmxnrhazs", "manxrsmznh", "sxframlqnn", "mxniiyrsau", "ntcpizxqdx", "asxrfltman", "jruzufvcet", "tfnsmlrfxa", "xspnatmbrq",
         "srnxapmayn", "ikiieevhex", "rnkaxsmpya", "shaxmdrbnw", "liamxlsqnr", "xmgmrniswa", "ceaxnrfmds", "ulquuhiaqi", "nsxkamickr",
         "gjmfsqjddk", "hiiwkqukga", "srnmddxhaq", "tsnxmmrzal", "lnasjfrmxc", "nsrmanakxx", "mcufdicvhm", "cxaisemnrx", "rkjwfbacfw",
         "pxyajnsdoe", "xflrqfmwkv", "nnosmxnarg", "jykatzahro", "kbnndbtykl", "hzvywrttes", "gdigbfxwzk", "urxmwjpaea", "eramksxnsm",
         "knpudvcnyo", "rngkaxspmf", "wupnfcaohl", "tbyrlopvtv", "vlfbdolsey", "nmarkxclxs", "ujadmlkucs", "sqaxmznhrx", "innkxsyamr",
         "guwzpxhnlr", "nfospzmtdo", "himfcnjbia", "rlctymknbr", "nmxasyrgja", "xepyfoaqgz", "bboyanvlkw", "rwsfndamxl", "cxhtjcdmqy",
         "rmynsienax", "zizdoxokip", "khoisnwoik", "ashtxnrtmi", "qnhwmlcuyz", "xbmsoarwxn", "lknoksitej", "fcbzpvwzja", "gaxnasbmrd",
         "lqouvvaaos", "msnajbsxrp", "jcmovuzdev", "ajnxawscmr", "ownrmxxxas", "eqgvjlrcnw", "wsmrnxyaxf", "mwamxrasnx", "imskprzime",
         "rwmgsxoarn", "rbunslmxea", "ufromsscye", "feybtfxaxx", "msrddrnazx", "bqhqijhklx", "bnhdeykjte", "lluexycmey", "mnyrjasxto",
         "xrslimkmna", "edfjhiillf", "xgrwqwndgd", "fswaimxnrq", "nhrqvqhpro", "mxxtadrans", "nekowcthlj", "iuumtseftd", "asmdgcngqx",
         "ztcwnucdci", "siwloxomuj", "vmarnsgcux", "hpbmactyog", "afwpfinaye", "bpwtddjwlm", "zrgrmxnasx", "xccqmcamiz", "yxaosdnrmp",
         "cugcfcabtf", "ximarsrnax", "aqncradxms", "nykvfdnaww", "asjomtvnrx", "aisnvrmxxd", "zbnsbialcg", "mtgugfkfnl", "nkpjpctles",
         "amenlxtrse", "jsjiwxliuj", "arnxlbajms", "mlarxsmnxh", "ipjffrnzcp", "lsackchndh", "mspvnajmrx", "urqaibqksj", "hlmikpnotf",
         "qsraxegmnf", "lggvsrxanm", "nmrsyxsdna", "nxmmacrsty", "pnamjgrqsx", "xsorymnakv", "manurzhsxa", "otfsmosavn", "oklyalgmdd",
         "mvldecbhiu"]
big_B = ["rn", "x", "ranxs", "xm", "x", "s", "xmrn", "asmn", "na", "x", "rs", "rn", "an", "xmasn", "mxs", "r", "m", "s", "s", "a", "axm",
         "anmsr", "srxm", "s", "nm", "nx", "xsa", "anmsx", "m", "xmans", "rsnax", "rasxn", "snamr", "n", "msn", "srn", "sax", "nr", "xsam",
         "xsn", "rnm", "mar", "rxm", "n", "mx", "mnsrx", "xnasm", "xmnra", "rm", "mxnsr", "mxs", "xsmr", "masr", "mxnsa", "mrsan", "ax",
         "m", "mrans", "sr", "snr", "axs", "raxns", "xmrs", "anrs", "am", "nsar", "smrx", "n", "xrn", "snamx", "nmras", "sran", "xan",
         "rmxa", "s", "axs", "sra", "m", "ans", "ra", "smran", "asxn", "sr", "asnm", "nrsma", "xams", "mnxs", "nxsam", "axmsr", "rsa",
         "rmxa", "sn", "mxasn", "anrs", "rax", "srnm", "a", "rm", "xnasm", "xm", "sarx", "s", "msarx", "sraxm", "amx", "xmrsa", "xa", "m",
         "nsar", "xr", "r", "mas", "snam", "ar", "snm", "nr", "sa", "naxms", "mn", "s", "nsr", "sarxm", "rn", "ansxm", "mns", "r", "ms",
         "asxrm", "xr", "xsr", "msnra", "mrs", "snrx", "r", "sra", "sarxm", "axs", "xmasn", "mnrx", "mxs", "rasmx", "arxm", "rmxn", "xs",
         "x", "m", "x", "mxsnr", "sax", "sxmr", "xsman", "nx", "ma", "man", "sarmn", "s", "snax", "sa", "a", "arnxs", "r", "nar", "xs",
         "asmr", "rm", "nx", "nsx", "r", "xna", "asrxn", "axn", "rx", "rnsx", "nx", "srn", "amsnr", "r", "asnx", "s", "xa", "a", "mxn",
         "xs", "msarx", "x", "arm", "sraxn", "s", "xsm", "ma", "nm", "nmx", "r", "x", "saxn", "sxmna", "ra", "rax", "x", "nsm", "nsxa",
         "rm", "s", "ar", "ns", "arm", "amnx", "xasr", "xmar", "srm", "sr", "xnasr", "mns", "xm", "x", "xarn", "r", "xnrm", "nmasr", "xm",
         "ms", "ms", "rxsa", "m", "smar", "snmra", "mnrax", "nrs", "rmasx", "snxmr", "rsx", "sra", "mxr", "nr", "sxn", "xas", "rxms",
         "snma", "snmr", "xmras", "naxmr", "snx", "nsmxr", "m", "nr", "xamnr", "r", "x", "ra", "xamn", "rm", "mr", "ans", "mr", "xr", "r",
         "xrnma", "armsn", "am", "srx", "rnsax", "r", "amn", "a", "m", "s", "xrn", "nr", "amx", "srx", "asr", "amsx", "smra", "na", "rs",
         "mns", "asmx", "xsnra", "a", "rmasn", "sxa", "n", "xrnms", "axsr", "nrxm", "na", "xman", "ma", "a", "n", "nrxsa", "m", "ansm", "s",
         "smrax", "sxn", "nx", "rxn", "r", "x", "x", "na", "s", "nasrx", "msnx", "anx", "xnm", "nrxas", "arnxs", "sxan", "nams", "m",
         "ramn", "nxr", "xrns", "mnr", "rmsn", "mr", "nsmr", "xamrn", "ramn", "nmxa", "mrna", "xmar", "nr", "rnma", "n", "nrmxs", "nmx",
         "mxs", "nr", "m", "xm", "nrsm", "nsxa", "mxs", "asnm", "sxam", "x", "nmra", "n", "smnx", "xsmnr", "rma", "nx", "m", "mxna", "sma",
         "xrnm", "arxs", "s", "xmran", "a", "rxsma", "anxrs", "nxsm", "nma", "axs", "n", "ar", "as", "saxnr", "nxsrm", "mx", "snx", "axr",
         "mnxra", "rnmx", "xsmar", "r", "x", "xam", "xas", "nrsax", "mran", "mnx", "x", "n", "smaxr", "rn", "as", "srxn", "rsm", "xmr",
         "asmn", "n", "ar", "nxra", "n", "m", "sxrnm", "xr", "ax", "nsx", "saxmr", "xr", "msnar", "snax", "nrsm", "n", "x", "x", "sn", "s",
         "nmrs", "xsm", "nmxsr", "m", "r", "xnrs", "rxnm", "rms", "nrxsm", "mnrs", "n", "arn", "smx", "raxmn", "ran", "snaxm", "xn", "xan",
         "anmr", "mar", "r", "anrs", "na", "anm", "sxr", "sxm", "sxna", "nr", "amx", "r", "snmx", "sarm", "x", "maxns", "x", "xsanm",
         "sarnm", "rmx", "xa", "mrsn", "s", "asxn", "rma", "axs", "nasx", "nrx", "maxn", "m", "nxma", "rnxa", "xnsa", "srnx", "a", "r",
         "rsxm", "nams", "n", "rasn", "nrmas", "xr", "axns", "smx", "smxr", "ra", "san", "smxa", "x", "nramx", "msx", "snr", "axrn", "a",
         "amr", "sn", "s", "n", "mnr", "n", "m", "rmxan", "masr", "nmsa", "srma", "xanr", "a", "msnrx", "mrx", "x", "xmns", "n", "asmx",
         "m", "ns", "rsan", "ans", "armxn", "xns", "saxmn", "amn", "mxa", "x", "n", "srxam", "amxns", "rasxn", "xanms", "anmrx", "nr", "s",
         "rsn", "rasx", "anmsx", "mnxsr", "sam", "sar", "nsrxa", "asm", "n", "mx", "nr", "s", "nrxsm", "mxar", "rn", "na", "ax", "x",
         "rsxan", "rm", "nm", "mxnsa", "sxm", "rn", "nsmx", "rn", "a", "nxrm", "m", "nrms", "xm", "rnas", "anmrx", "rx", "a", "sxn", "anrm",
         "r", "rn", "asm", "xm", "msnrx", "amsnx", "nxa", "rn", "rnxa", "m", "max", "sn", "ma", "nm", "nxar", "xsn", "xn", "ax", "srnxa",
         "arsnm", "axm", "ax", "nsm", "sarn", "sma", "rnmsa", "x", "nax", "nxs", "sxmn", "rxans", "asmr", "xansr", "asmxr", "xnrs", "rs",
         "sma", "smnx", "xr", "ansxm", "armsx", "rsxnm", "s", "nsmxa", "n", "msanr", "mrsnx", "rn", "axsn", "nas", "anr", "xa", "srn", "a",
         "nrsa", "amns", "snx", "nasxr", "n", "nmsrx", "ams", "mx", "asn", "nsxam", "nx", "sn", "na", "amsr", "rasmn", "s", "nm", "nasx",
         "sna", "mraxn", "nxram", "na", "asmxn", "r", "nxams", "mnxs", "asm", "x", "sa", "nrsx", "snxr", "m", "nasrx", "mxan", "r", "xnma",
         "smanr", "as", "msxn", "r", "mxnrs", "mr", "rsam", "xan", "rn", "mxrs", "mxasn", "xmrns", "m", "masn", "nsa", "r", "rxman", "nr",
         "rxm", "xmra", "xmrsa", "xmsr", "nsmxa", "a", "nrxas", "rxnsa", "nxmr", "xasn", "x", "amsr", "sxmn", "axsmn", "n", "xrms", "axnsm",
         "mx", "rm", "mrn", "rmnxa", "nxsam", "xasrm", "xnra", "a", "n", "rn", "rnmx", "xnms", "mars", "rm", "msx", "asr", "rn", "sr", "rx",
         "sa", "nxmar", "sxmr", "sx", "rsnam", "arnm", "anmx", "x", "sx", "an", "smran", "nasm", "nmx", "axmrn", "nrxm", "narsx", "s",
         "snarx", "anm", "mnrx", "rsxn", "sx", "mn", "xarnm", "s", "sxrnm", "anm", "xmnr", "sx", "m", "rxan", "a", "xa", "mrsa", "mrax",
         "r", "am", "s", "nxm", "xms", "n", "nxr", "na", "m", "sax", "a", "mar", "ms", "axr", "n", "n", "axrs", "nxrm", "rm", "s", "rsan",
         "asxm", "nxrms", "msxna", "n", "amsx", "mnrsx", "amrnx", "raxms", "xsam", "xmnar", "s", "nxr", "nxsrm", "as", "r", "a", "rxs",
         "nr", "rxnms", "xn", "s", "mas", "rx", "sxra", "ams", "x", "mx", "xrns", "ar", "srn", "mnsa", "n", "ramns", "n", "snarx", "xs",
         "sn", "n", "anm", "na", "ax", "amxr", "n", "m", "r", "sax", "rxa", "rmxn", "arm", "mnx", "m", "saxr", "ansxr", "xsn", "ar", "sx",
         "snm", "ax", "rns", "smxr", "mrsx", "arnm", "mrxn", "xra", "ns", "amxs", "nsr", "namrs", "anms", "xsmr", "mxrs", "x", "snmra",
         "xas", "anm", "nx", "nra", "s", "nasxr", "mn", "smrx", "n", "rm", "xn", "xrs", "xrsma", "nraxs", "sxa", "rx", "rnam", "n", "mna",
         "ma", "s", "ns", "nxa", "ax", "samrx", "xna", "xms", "amxns", "nxas", "nxam", "nmar", "s", "x", "smx", "xsrm", "sm", "x", "s", "s",
         "a", "rmxn", "nsarx", "xs", "maxn", "xna", "xman", "rs", "a", "m", "mn", "sxa", "xsnma", "a", "n", "nxasm", "ax", "a", "ra", "rn",
         "m", "samn", "mraxs", "ar", "s", "mnsar", "xsn", "mra", "axs", "nrs", "rsxna", "msn", "a", "msna", "rms", "ns", "n", "xra", "nrm",
         "xnmr", "srmx", "sa", "rma", "asrn", "nxrma", "s", "rsnmx", "xans", "a", "rms", "rnms", "r", "srax", "snax", "s", "msnr", "sxan",
         "rxa", "xms", "sramn", "xasr", "m", "srnma", "rm", "mxn", "s", "mxa", "rxanm", "m", "sxnm", "s", "x", "xna", "as", "mrxn", "ra",
         "amx", "x", "mas", "mans", "xsn", "xna", "srxn", "xmsra", "x", "asm", "rxs", "ns", "nxa", "msan", "man", "m", "axnr", "xmanr",
         "xnrs", "mr", "ax", "snmra", "man", "mraxn", "rsman", "mnxas", "msan", "raxsm", "xsam", "ansx", "m", "xmrn", "xa", "rx", "nas",
         "sam", "ransx", "mx", "xsrm", "asn", "xn", "s", "r", "nr", "rm", "xas", "amnxs", "r", "xmnas", "xnma", "s", "nx", "rmx", "x",
         "anxs", "sxa", "rnsx", "xa", "rasn", "rx", "mna", "r"]
big_expected = ['rxnaoymlsh', 'nmwmwwaxrs', 'sxgjnracmk', 'xrbnenadsm', 'fradngxsmr', 'rnsmmimaxu', 'xxbsagrnmh', 'ynharsxmoq',
                'mnxarsmuea', 'xhrnorbmas', 'xamnxsromu', 'apvnmrqsxw', 'nmxeqrausb', 'gwyxrasqmn', 'emasdxsrnn', 'gvrvanrxms',
                'nabszrmgcx', 'wrasxmjenz', 'wneasjvxmr', 'qnmbtzrsxa', 'jrxaomasnb', 'faxsnmvsvr', 'uhmaysrxna', 'atsxbgrynm',
                'xnkrsxaskm', 'knrysmxatp', 'ystjraxmnt', 'xryasmmucn', 'jkeacnrsmx', 'arrmtrxnns', 'xnmrslxayl', 'bnsaxvrxmn',
                'najrymlxsd', 'mxrasbnage', 'axntxmsgrs', 'samyxrfnmu', 'srfbknmhax', 'dnsraxmkaq', 'srlmnzuwxa', 'xdmnsaacnr',
                'ansrxhkygm', 'jnsekamtrx', 'bmkaxsnrje', 'kosmnmarxh', 'axsnvrmmxj', 'pnrwxrsazm', 'dtxrransmd', 'salmxrnfgw',
                'reasexsncm', 'frsnxisaam', 'mtanxroejs', 'fhmyxarsfn', 'saanymarxe', 'mwasuxnrwc', 'osatnrzxvm', 'xngasmrvaz',
                'xnspmnrmaa', 'ctgxmnrsab', 'nsnavmnxrz', 'vsxayrnmnw', 'anrxsmbgkb', 'anlxrsallm', 'rfgmxknasg', 'mrbxoadzsn',
                'saqnxmtria', 'jxnsmrrsaz', 'mxonajssrf', 'xmnrlsrsat', 'nsvamxrnne', 'mssrxtnaux', 'racwsmwnnx', 'taisfhrnxm',
                'ragnomsbxc', 'ixmxkrngas', 'sroxmafons', 'nsraxeboam', 'urnamxashs', 'nsmraxlamh', 'nmxxsacxrf', 'mrnxqzqdas',
                'xrsjenasym', 'xmraisnaek', 'sqaxprnmxd', 'mnrnalmwsx', 'spnwmyxroa', 'axnlzasrrm', 'txpnrvyasm', 'dxmngnaesr',
                'nxmxcsrqba', 'mxamrhsncn', 'asmqyrnfdx', 'nsemovxars', 'sxwxrmhnia', 'ovxmmnsrsa', 'mxsmarwnxc', 'nmarxpaavs',
                'msralnsoxy', 'tsnyaemirx', 'mrepaksznx', 'xeqsqrunam', 'sarmnemxuq', 'rcawmlfxns', 'scaxanmryx', 'mxrnhkvsla',
                'rnrwsxnfma', 'hvsrjankxm', 'psajmxzxnr', 'manmrbskxx', 'ammirxnosc', 'aycrmnxsrd', 'jrnxtnnmas', 'nsaximsari',
                'rdaxisname', 'ramxswnrmu', 'norxuasmsj', 'asxnaqrcmx', 'hmsrwnqxau', 'rngsamrsux', 'lrdsmnxabg', 'rwdwnsmxav',
                'wkrnxxapms', 'wxamwvrsdn', 'rmnasxhhrr', 'mxjsnrvmal', 'mrnalrmxys', 'xgcrmhayns', 'urfyxsneam', 'vrnmxvzzsa',
                'oxqasnmfnr', 'axanwsymcr', 'xumxrsngac', 'sqmknmrrax', 'hxanemrvsd', 'rdosaomrxn', 'xrxwxnamsp', 'zrjxjsanvm',
                'zyxcronmas', 'rznapxsmwq', 'zxnaronsam', 'ryzxvmnast', 'hfesjxnarm', 'orvxnmnsal', 'zxsafrmsnk', 'xihrssnmah',
                'snjdmpmxra', 'nomrexfsya', 'masxqpnnrs', 'xhnsmsamri', 'sarmxrlnco', 'nrmlrxusat', 'gaqhmnrswx', 'namxmrsstn',
                'esmcaxnnzr', 'xprnamsesk', 'gharasxomn', 'dyrnexanms', 'ptmnsrixan', 'nearmqlssx', 'xmrgvmrsan', 'arvxxmxsnd',
                'ncxnccsmar', 'hlmrursxna', 'nqrasyxdmx', 'arssnxyamm', 'mstcxanraj', 'atxtnnskmr', 'nmbwrslaxn', 'xalsyrysnm',
                'sxphznnmra', 'gmfsayrhnx', 'mdwasnxdrn', 'slnlrzxmax', 'sxgrfpnmaj', 'ragamfsnrx', 'rbzxpnsgam', 'dgsgxamirn',
                'mjrsghaxgn', 'rvxacmksnf', 'mtrinsarxj', 'nmsrrxrqan', 'amrkxyrnas', 'vucmxrsnia', 'nlsubxmrva', 'ixnmsxyrap',
                'sxafcjnrml', 'osjmynrgax', 'xmasrnexaa', 'axxmrrnsos', 'ntrmsyapxu', 'rmssidnaxv', 'mrbmsaxcmn', 'amtlrsngsx',
                'smrwxbniaw', 'rernalvmsx', 'pnrxasmswx', 'nraxymszfc', 'nxxzwmaosr', 'lsugnmraax', 'rvapnksamx', 'qzrgsmnuxa',
                'nhaxrhsjmz', 'agnrmwrxes', 'avxsrnlsem', 'asmnytpxrf', 'apsxamtnir', 'qwxmcnarsz', 'dblmsnxarf', 'aniwjmxrsf',
                'mvrxsmnago', 'kgassmrznx', 'jrnamsxgnl', 'lxdrvsmnxa', 'nosmerxfat', 'rxomianrsw', 'xanrmqxvts', 'xrzasxnkim',
                'srasymnxao', 'sdgnmaxmrm', 'dxrfrxmnas', 'ncgxamrgds', 'esarixnrjm', 'shmrcgnxla', 'mdlxcnarsn', 'naaslxmrsg',
                'rrmxsajnlt', 'mrysmxkxna', 'rnxtmvsabe', 'usyrxafnmw', 'rxnsnathmm', 'sbhprxwnam', 'amasslnxrz', 'axsrjnpmam',
                'mzsslraxgn', 'raygxnscrm', 'amqspnryxv', 'namsxmrsdq', 'xnarfwirsm', 'nmrsxachqn', 'yatnnsrvxm', 'qfafsxrngm',
                'tycmxsnoar', 'aasmanlxrw', 'irhmaxjsrn', 'msbnfkwrxa', 'xrvnasekmi', 'nxsrawmtka', 'dsmjkxnarn', 'naxrupsdmu',
                'nqbaxgomrs', 'anmosmdprx', 'auunmsxfrt', 'kqwxrnsanm', 'ajdxaonsrm', 'txasmnmetr', 'srnfeuxmap', 'rxwmrfanbs',
                'aimximnrds', 'nsmqegravx', 'axeplmnsry', 'almsnuyrxi', 'nabsrmsxhn', 'bnmxasprey', 'rsxmaemein', 'hinsamrxnv',
                'faxsrdmnxa', 'oxwszaprmn', 'xmcrsrnoca', 'svianbrxmj', 'rmnxrsasos', 'nxnxsqmard', 'lashrlumxn', 'javmrxsmsn',
                'znmasruxgy', 'yasrrnklmx', 'arnfsmvayx', 'ixdwnmasrj', 'smaejrzjxn', 'spmpanrxsb', 'rmsxmvgafn', 'nemxwrsfas',
                'szemranxmn', 'amzneroxis', 'nmrgfsxkao', 'urfxnmssma', 'anmxrxrspy', 'nagbxprmas', 'dgmxkrsanz', 'rrxdnrsoam',
                'yrsmansfxa', 'amxxtnlsrh', 'mglastrnjx', 'cznrxasmii', 'ksnxzyrmam', 'xnnamjmjrs', 'xmgaznrsrf', 'nnrnjxmsxa',
                'nxkmarirxs', 'wsmqbrnxan', 'ebamznxdsr', 'mdaebonrsx', 'xaurnrwmws', 'orxlnmtsda', 'xahnsbncmr', 'hrnmsazrxr',
                'trrcaxmnsd', 'bsmdnapmrx', 'rixlaasndm', 'algmrsnxxc', 'amqxtlnrsf', 'mnwaysvrax', 'xzlsamrqng', 'xrapmrspns',
                'xrcanmrosw', 'wsrnamdxxa', 'vxurznmsay', 'xnyrnaklsm', 'rzayxmssnx', 'rjmhnusxar', 'snhhraimax', 'efdnqmxsar',
                'umfrnosxva', 'mpxhsvnavr', 'nrgtmnsaxx', 'sirmvmxxan', 'esamonrxan', 'ahrxsnaams', 'jusvamcrxn', 'dnsaexgmfr',
                'xsmblwarvn', 'syjrxaavnm', 'axhryaknms', 'mxxrdzafsn', 'nxpkmsavre', 'erxsbanmjr', 'sxxnmlraam', 'sanrmhxczw',
                'yqsyraxmnt', 'cmsxxrnazy', 'swmanrkvrx', 'mtfxbrnsoa', 'mdanxrcsgd', 'xsrnsecavm', 'qmvnsirxau', 'rxqnmszoan',
                'ashmermanx', 'xaaxmrrwsn', 'jmxirntsra', 'akxrkwonms', 'bxnvasmrse', 'rlayamsnlx', 'ysmnmaxara', 'naxgsmyerz',
                'mrxnstokas', 'ayxryxmsns', 'sramnaxsyq', 'sxmnxvfraa', 'nxmaraxdrs', 'yrxsvgsanm', 'pmtaxrrsxn', 'uxymsrnkav',
                'nxawsvgmmr', 'hxrtsagmgn', 'xajmnrohos', 'cmsxmjcnar', 'mnrlesxdsa', 'mrnjsqxfta', 'rmxdhwnsai', 'rnamsgxlbo',
                'urhnayxmrs', 'xpdmnkarls', 'enqmnapxsr', 'nmhrnaqsxr', 'qgrmxsaakn', 'nmxaxansrn', 'nihramsxue', 'kmasrixnsk',
                'mrgnyxmasr', 'snxamrxwpe', 'xazumfnrsn', 'vmrndmxsad', 'nnnrwrxmas', 'vmrzsuxang', 'njnxisrlam', 'xmncrssajt',
                'ijsraqmnxj', 'mtxraosnub', 'lmuhfrnsxa', 'mssrxainzs', 'xnilsraamh', 'sxramtaesn', 'xlnmnssbar', 'hrnssmaunx',
                'gjxnryamso', 'svnmafwrxl', 'sunrgahxcm', 'scnhrmavmx', 'darmscxqnq', 'onemsqatxr', 'sregfknamx', 'nrxasumrfe',
                'aensxlcmer', 'pmxwsrsnaq', 'mrsrnxwjxa', 'azumxrmsan', 'fnsaxlaimr', 'emwnscraox', 'rseonarmex', 'ansmtlxqgr',
                'artniensxm', 'iazxmvsrnd', 'mjyunxzars', 'gqahmnjsxr', 'stsysmxran', 'nxajjfrbsm', 'sqxonamrtc', 'xsamynroum',
                'xansrncbmh', 'naxlbmvlsr', 'syrqnamjrx', 'rszugaaxmn', 'nnssaeoxrm', 'fsnmxaonjr', 'reassomnhx', 'nodrkmsgxa',
                'amnksrxyob', 'mxqsrqdank', 'xzmnamlszr', 'xrwmnkmsqa', 'namxrmfrsb', 'ianmczrsxp', 'axrnsomnux', 'xgvtnmrmas',
                'anlmquxrse', 'nasoozrxmm', 'yassmztxrn', 'xrnasjmysg', 'xnsaamarrw', 'zrmxnrhazs', 'manxrsmznh', 'sxframlqnn',
                'mxniiyrsau', 'asxrfltman', 'tfnsmlrfxa', 'xspnatmbrq', 'srnxapmayn', 'rnkaxsmpya', 'shaxmdrbnw', 'liamxlsqnr',
                'xmgmrniswa', 'ceaxnrfmds', 'nsxkamickr', 'srnmddxhaq', 'tsnxmmrzal', 'lnasjfrmxc', 'nsrmanakxx', 'cxaisemnrx',
                'nnosmxnarg', 'eramksxnsm', 'rngkaxspmf', 'nmarkxclxs', 'sqaxmznhrx', 'innkxsyamr', 'nmxasyrgja', 'rwsfndamxl',
                'rmynsienax', 'ashtxnrtmi', 'xbmsoarwxn', 'gaxnasbmrd', 'msnajbsxrp', 'ajnxawscmr', 'ownrmxxxas', 'wsmrnxyaxf',
                'mwamxrasnx', 'rwmgsxoarn', 'rbunslmxea', 'msrddrnazx', 'mnyrjasxto', 'xrslimkmna', 'fswaimxnrq', 'mxxtadrans',
                'vmarnsgcux', 'zrgrmxnasx', 'yxaosdnrmp', 'ximarsrnax', 'aqncradxms', 'asjomtvnrx', 'aisnvrmxxd', 'amenlxtrse',
                'arnxlbajms', 'mlarxsmnxh', 'mspvnajmrx', 'qsraxegmnf', 'lggvsrxanm', 'nmrsyxsdna', 'nxmmacrsty', 'pnamjgrqsx',
                'xsorymnakv', 'manurzhsxa']


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "o"]), ["facebook", "google", "leetcode"]),
    pytest.param(dict(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["e", "oo"]), ["facebook", "google"]),
    pytest.param(dict(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["l", "e"]), ["apple", "google", "leetcode"]),
    pytest.param(dict(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["lo", "eo"]), ["google", "leetcode"]),
    pytest.param(dict(A=["amazon", "apple", "facebook", "google", "leetcode"], B=["ec", "oc", "ceo"]), ["facebook", "leetcode"]),
    pytest.param(dict(A=big_A, B=big_B), big_expected),
])
def test_solutions(kwargs, expected):
    assert Solution().wordSubsets(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
