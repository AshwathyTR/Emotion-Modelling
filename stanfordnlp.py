# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:28:40 2018

@author: hp
"""

from data import Affect_Data
ad = Affect_Data()

import json 
import os

from pycorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP('http://localhost:9000')

#annotators = 'tokenize, ssplit, pos, lemma, ner, entitymentions,coref'
#options = {'openie.resolve_coref': True}

#nlp = StanfordCoreNLP(annotators=annotators)

dataset = ad.load_affect_data()
read=""
current_story=""

for entry in range(0,len(dataset.keys()),1):
    if (dataset[entry]["story"]+".json" in os.listdir()):
        continue
    if (dataset[entry]["story"] != current_story):
        
        
        text = (read)
        output = nlp.annotate(text, properties={    'annotators': 'tokenize,ssplit,pos,ner,depparse,coref',
                                                'outputFormat': 'json'
                                            })
        with open(current_story+".json",'w') as jf:
            json.dump(output,jf)
            
        current_story=dataset[entry]["story"]
        read=""
        
    read=read+" "+dataset[entry]["raw_text"]

    
   






#document = nlp(text)

#print(output) # prints 'text'