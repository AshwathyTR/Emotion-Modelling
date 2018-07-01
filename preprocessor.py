# -*- coding: utf-8 -*-
"""
Created on Sun Jul 01 11:34:50 2018

@author: hp
"""

from gensim.models import Word2Vec
import os.path


import re    #for regex
from nltk.corpus import stopwords
import pandas as pd
from nltk.stem.wordnet import WordNetLemmatizer 
# Tweet tokenizer does not split at apostophes which is what we want
from nltk.tokenize import TweetTokenizer  
import sys
lib_path = r'..\corpora'
sys.path.insert(0, lib_path)
import appos
#contains appostrophe corrections
from tqdm import tqdm

class PreProcessor:
    
    eng_stopwords = set(stopwords.words("english"))
    lem = WordNetLemmatizer()
    tokenizer=TweetTokenizer()
    APPO = appos.appos

    
    def __init__(self):
        pass 
        

    def clean(self,comment):
        """
        This function was taken from Kaggle - Stop the S@as
        This function receives comments and returns clean word-list
        """
        comment=comment.lower()
        #remove \n
        comment=re.sub("\\n","",comment)
         #remove non ascii characters
        comment = self.remove_non_ascii(comment)
        #removing non-alphabet characters 
        comment = re.sub("[^a-z\s]", "", comment)
       #Split the sentences into words 
        words=self.tokenizer.tokenize(comment)
        # (')aphostophe  replacement (ie)   you're --> you are  
        words=[self.APPO[word] if word in self.APPO else word for word in words]
        words=[self.lem.lemmatize(word, "v") for word in words]
       #remove stop words
        words = [w for w in words if not w in self.eng_stopwords]
        clean_sent=" ".join(words)
        return(clean_sent)

    def remove_non_ascii(self,text):
            ascii_chars = ""
            for character in text:
                try:
                    character.encode('utf-8')
                    ascii_chars = ascii_chars + character
                except:
                    pass
            return ascii_chars

    

        
        

            

