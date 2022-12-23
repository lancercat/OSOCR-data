import os
import regex
from osocr_tasks.tasksg1.dscs import makept

def prepare_pt(langroot):
    dictp=os.path.join(langroot,"meta","dict.pt");
    if(os.path.exists(dictp)):
        print("skipping pt build, to force rebuilding, remove", dictp);
        return dictp;

    with open(os.path.join(langroot,"meta","alphabets.txt"))as fp:
        chars=[l.strip() for l in fp];
        allch=[];
        masters=[];
        servants=[];
        for ch in chars:
            if(len(ch)):
                l= regex.findall(r'\X', ch, regex.U);
                allch+=l;
                for i in range(1,len(l)):
                    masters.append(l[0]);
                    servants.append(l[i]);
    allch=list(set(allch));
    fntp=os.path.join(langroot,"meta","notofont.ttf");
    makept(None, [fntp],
           dictp,
           allch, {}, masters=masters, servants=servants);

    return dictp;
