import os.path

from osocr_tasks.athena.quicklmdb import quick_lmdb
from osocr_tasks.athena.quickptg1 import prepare_pt_wfallback

def quick_manyfnt_dataset(langroot,fnts,pfx="png"):
    prepare_pt_wfallback(langroot,fnts);
    quick_lmdb(langroot,os.path.join(langroot,"lmdb"),"None",pfx);
