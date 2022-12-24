import torch;
from neko_sdk.ocr_modules.charset.jap_cset import kata,hira;
from neko_sdk.ocr_modules.charset.chs_cset import t1_3755;

from osocr_tasks.tasksg1.dscs import makept

# OSR
def jap_osr(root):
    makept(root+"mlttrjp_hori/",
           [root+"mltnocr/synth_data/fnts/NotoSansCJK-Regular.ttc"],
       root+"dicts/dabjpmltch_osr.pt",
           set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"),
           set(hira).union(set(kata)), space=t1_3755.union(set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890")));

# OCR (with KUC)
def jap_no_novel(root):
    makept(root+"mlttrjp_hori/",
           [root+"mltnocr/synth_data/fnts/NotoSansCJK-Regular.ttc"],
       root+"dicts/dabjpmltch_sharedkanji.pt",
        set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"),
           set(hira).union(set(kata)),space=t1_3755);

# OSR + GZSL >= GOSR.
# Cognition actually means the existance boundary,
# and GZSL says that a boundary is always tractable if you give it sideinfo.
# Unfortunately there is no public available metric for OSTR.
def jap_no_hirakata(root):
    makept(root+"mlttrjp_hori/",
           [root+"mltnocr/synth_data/fnts/NotoSansCJK-Regular.ttc"],
       root+"dicts/dabjpmltch_nohirakata.pt",
        set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"),
           set(hira).union(set(kata)));

# when all four present... full OSTR
def jap_kanji(root):
    makept(root+"mlttrjp_hori/",
           [root+"mltnocr/synth_data/fnts/NotoSansCJK-Regular.ttc"],
       root+"dicts/dabjpmltch_kanji.pt",
           set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"),
           set(hira).union(set(kata)).union(set("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"))
           );
def make_all(root):
    jap_no_hirakata(root);
    jap_osr(root);
    jap_no_novel(root);
    jap_kanji(root);
