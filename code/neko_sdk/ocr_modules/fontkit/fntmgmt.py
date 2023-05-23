
from fontTools.ttLib import TTFont
from fontTools.unicode import Unicode
import unicodedata

from fontTools.otlLib.builder import buildCoverage
import torch;
from itertools import chain
class fntmgmt:
    NORMAL_CHARACTER=["Lo","Lu","Ll","So","Sm","Nd","Nl","No",]
    @classmethod
    def parse_sub_4(cls,sub):
        ret=[];
        for k in sub.ligatures.keys():
            for l in sub.ligatures[k]:
                magic=[k]+l.Component;
                ret.append(magic);
        return ret;
    @classmethod
    def parse_sub_1(cls,sub):
        return sub.mapping.keys();

    @classmethod
    def parse_sub_2(cls, sub):
        return sub.mapping.values();

    @classmethod
    def parse_sub(cls,sub):
        if(sub.LookupType==1):
            return cls.parse_sub_1(sub);
        elif(sub.LookupType==2):
            return cls.parse_sub_2(sub);
        elif(sub.LookupType==3):
            pass;

        elif(sub.LookupType==4):
            return cls.parse_sub_4(sub);
        else:
            # print(sub.LookupType);
            return [];
    @classmethod
    def get_charset(cls, fp):
        ttf = TTFont(fp, 0,fontNumber=0, verbose=0, allowVID=0,
                     ignoreDecompileErrors=True)
        chars = chain.from_iterable([chr(y[0]) for y in x.cmap.items()] for x in ttf["cmap"].tables)
        return set(chars);


    def init_charset(this,fnt_d):
        for k in fnt_d:
            this.charset_d[k]=this.get_charset(fnt_d[k]);
            torch.save(this.charset_d,"charset_d.pt")
            print(k,"scanned");
    def load_charset(this):
        this.charset_d=torch.load("charset_d.pt");
    def __init__(this,fnt_d):
        this.charset_d={};
        if(fnt_d is None):
            this.load_charset();
        else:
            this.init_charset(fnt_d);
        pass;

