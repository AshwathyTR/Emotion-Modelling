# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 19:10:34 2018

@author: Ashwathy
"""

import os

class affect_data:
    corpus_path = r'C:\Coursework\Project\corpora\AnnotatedGrimms\Grimms\emmood'
    affect_scores = {'H':1,
                     'S':-1,
                     'Sa':-1,
                     'A':-1,
                     '+':1,
                     '-':-1,
                     'Su+':1,
                     'Su-':-1,
                     'N':0,
                     'F':-1,
                     'D':-1}
    
    def load_affect_data(self):
        dataset={}
        entry=0
        for story_name in os.listdir(self.corpus_path):
            if '$' in story_name:
               continue
            with open(os.path.join(self.corpus_path,story_name),'r') as story:
                for sentence in story.readlines():
                    parts=sentence.split(); 
                    dataset[entry]={}
                    dataset[entry]["story"]=story_name
                    dataset[entry]["sent_id"] = parts[0].split(':')[0]
                    dataset[entry]["em"]= parts[1].split(':')
                    dataset[entry]["mood"]= parts[2].split(':')
                    dataset[entry]["score"] = self.get_score( dataset[entry]["mood"] + dataset[entry]["em"])
                    dataset[entry]["class"] = self.get_class(dataset[entry]["score"] )
                    
                    raw_text= sentence.strip('\n')
                    raw_text=raw_text.replace('\t','')
                    raw_text = raw_text.replace(parts[0],'')
                    raw_text = raw_text.replace(parts[1],'')
                    raw_text = raw_text.replace(parts[2],'')
                    
                    dataset[entry]["raw_text"] = raw_text
                    entry=entry+1
                    
        return dataset

    def get_score(self,annots):
        score=0
        for annot in annots:
            score=score+self.affect_scores[annot]
        return score/4.0
    
    def get_class(self,score):
        if score> 0:
            return '+'
        elif score<0:
            return '-'
        else:
            return 'N'


  
d=affect_data()          
print d.load_affect_data()[77]
    