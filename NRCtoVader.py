# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 11:43:59 2018

@author: hp
Script to convert NRC emotion dict to format usable by Vader
"""

from preprocessor import PreProcessor

vader_path=r"C:\Coursework\Project\corpora\vader_lexicon.txt"
nrc_path=r"C:\Coursework\Project\corpora\nrc_intensity_lexicon.txt"

with open(nrc_path,'r') as nrc:
    nrclines = nrc.readlines()

pp = PreProcessor()  
nrc_lex={}
i=0
negs=['anger','fear','sadness']
pos = ['joy']
for entry in nrclines:
    parts=entry.split()
    word = parts[0]
    word = pp.clean(word)
    word=word.strip()
    if(word==''):
        continue
    valence = float(parts[1])
    dim = parts[2]
    if dim in negs:
        valence = -valence
    if word in nrc_lex.keys():
        nrc_lex[word] = nrc_lex[word]+valence
    else:
        nrc_lex[word]=valence

'''with open('vader_lexicon.txt','w') as vader:
    for entry in nrc_lex.keys():
        vader.write(entry+"\t"+str(nrc_lex[entry])+"\n")  '''      