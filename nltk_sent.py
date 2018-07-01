# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 18:00:19 2018

@author: hp

Script for sent analysis with Vader
"""
import pylab as pl

from data import affect_data
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from preprocessor import PreProcessor
pp=PreProcessor()
def get_polarities(dataset):
    sid = SentimentIntensityAnalyzer()       
    predictions = {}
    for entry in dataset.keys():
        sentence = pp.clean(dataset[entry]['raw_text'])
        polarity = sid.polarity_scores(sentence)
        predictions[entry] = polarity['compound']
    return predictions

def get_correct(dataset):
    correct = {}
    for entry in dataset.keys():
        correct[entry] = dataset[entry]['class']
    return correct

def get_accuracy(pred,corr,class_name):
    tp=0
    fp=0
    tn=0
    fn=0
    total=0
    for entry in pred.keys():    
           if(corr[entry]==class_name):
               if(pred[entry]==class_name):
                   tp=tp+1
               else:
                   fn=fn+1
           else:
               if(pred[entry]==class_name):
                   fp=fp+1
               else:
                   tn=tn+1
               
           total=total+1
    return float(tp+tn)/float(total)

def get_total_acc(pred,corr):
    correct=0
    total=0
    for entry in corr.keys():
        if(pred[entry]==corr[entry]):
            correct=correct+1
        total=total+1
    return float(correct)/float(total)

def get_class(t1,t2,score):
    if(score<t1):
        return '-'
    elif score<t2:
        return 'N'
    else:
        return '+'

def get_predictions(t1,t2,polarities):
    predictions={}
    for entry in polarities:
        predictions[entry]=get_class(t1,t2,polarities[entry])
    return predictions
        
def find_thresh(polarities,correct,dataset):
    best_acc=0
    best_t1=0
    best_t2=0
    for t1 in pl.frange (-1.0,1.0,0.1):
        for t2 in pl.frange(t1,1.0,0.1):
            pred_classes = get_predictions(t1,t2,polarities)
            acc = get_total_acc(pred_classes,correct)
            if acc > best_acc :
                best_acc = acc
                best_t1 = t1
                best_t2 = t2
    
    return best_t1,best_t2,best_acc

def standard_thresh_acc(polarities, correct,dataset):
    pred_classes = get_predictions(-0.05,0.05,polarities)
    acc = get_total_acc(pred_classes,correct)
    return acc
          
                    
dataset=affect_data().load_affect_data()
polarities=get_polarities(dataset)
correct = get_correct(dataset)
print find_thresh(polarities,correct,dataset)


'''
Output:
best acc = 0.540485074627
t1 = 0.43
t2 = 0.437
'''
        