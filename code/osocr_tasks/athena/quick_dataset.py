import os.path

from osocr_tasks.athena.quicklmdb import quick_lmdb
from osocr_tasks.athena.quickptg1 import prepare_pt

def quick_dataset(langroot):
    prepare_pt(langroot);
    quick_lmdb(langroot,os.path.join(langroot,"lmdb"),"None");

