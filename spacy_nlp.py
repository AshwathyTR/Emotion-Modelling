# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 19:20:08 2018

@author: hp
"""

import en_coref_md
from data import Affect_Data

nlp = en_coref_md.load()
ad = Affect_Data()

def get_quotes(text):
    quotes={}
    inquote=False
    quote=""
    qnum=1
    txt=""
    for char in text:
        if inquote and char!='\"':
            quote=quote+char
        elif(char!='\"'):
            txt=txt+char
        if(char == '\"' and inquote==False):
            inquote=True
            quote=""
        elif(char == '\"' and inquote==True):
            quotes[qnum]=quote
            inquote=False
            txt= txt+" q"+str(qnum)+". "
            qnum=qnum+1
    return txt, quotes

def get_named_entity_counts(doc):
    entity_counts={}
    for entity in doc.ents:
       if (entity.label_ =='PERSON'):
            if entity.text in entity_counts.keys():
                entity_counts[entity.text]= entity_counts[entity.text]+1
            else:
                 entity_counts[entity.text]=0
    return entity_counts

def get_entity_counts(doc):
    entity_counts={}
    for token in doc:
       if (token.dep_=='nsubj'):
            if token.text in entity_counts.keys():
                entity_counts[token.text]= entity_counts[token.text]+1
            else:
                 entity_counts[token.text]=0
    #print (doc)
    #print (entity_counts)
    return entity_counts

def get_protagonist(doc):
    entity_counts=get_entity_counts(doc)
    ent_max=0
    protagonist=""
    for entity in entity_counts.keys():
        if (entity_counts[entity]>ent_max):
            protagonist=entity
            ent_max=entity_counts[entity]
    return protagonist
        
        
dataset = ad.load_affect_data()
read=""
current_story=""
doc=nlp("")
protagonist=""
for entry in range(0,len(dataset.keys()),1):
    if (dataset[entry]["story"] != current_story):
        print(current_story+"-----"+protagonist)
        current_story=dataset[entry]["story"]
        read=""
        
        
    read=read+" "+dataset[entry]["raw_text"]
    
    text, quotes = get_quotes(read)
    text = (text)
    doc = nlp(text)
    doc = nlp(doc._.coref_resolved)
    protagonist=get_protagonist(doc)
    
    

    



    
