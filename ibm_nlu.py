# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 14:18:25 2018

@author: hp
"""

import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="*******",
  password="*******",
  version='2018-03-16')

response = natural_language_understanding.analyze(
  url='http://www.authorama.com/grimms-fairy-tales-1.html',
  features=Features(
    entities=EntitiesOptions(
      sentiment=True,
      emotion=True,
      limit=1)))

print(json.dumps(response, indent=2))


