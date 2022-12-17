

from neko_sdk.ocr_modules.charset.chs_cset import t1_3755;
from neko_sdk.ocr_modules.charset.etc_cset import latin62;
from neko_sdk.ocr_modules.charset.jap_cset import hira,kata,Kyoiku_kanji,Joyo_kanji
from neko_sdk.ocr_modules.charset.no_filter import all_words;

def with_hirakata(gt):
    return len(set(gt).intersection(hira.union(kata)))>0;
def wo_hirakata(gt):
    return len(set(gt).intersection(hira.union(kata))) ==0;
def seen(gt):
     return len(set(gt).intersection(t1_3755.union(latin62)))==len(set(gt))
def ukanji(gt):
    return wo_hirakata(gt) and not seen(gt);

def get_jap_filters():
    return {
        "Overall": all_words,
        "Seen":seen,
        "Unique Kanji": ukanji,
        "All Kanji": wo_hirakata,
        "Kana": with_hirakata
    }
