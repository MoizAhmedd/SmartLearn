from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from security import subscription_key, endpoint
from keyword_questions import *
import random
from random import randrange
import os
#Set Environment Variables or set to empty string in production
subscription_key =subscription_key
endpoint = endpoint

credentials = CognitiveServicesCredentials(subscription_key)

text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "I had the best day of my life."
    }
]

response = text_analytics.key_phrases(documents=documents)
for document in response.documents: 
    for key_word in document.key_phrases: 
        #create poll with title key word
        #add question to poll
        if key_word in keyword_questions.math_questions.keys():
            question = keyword_questions.math_questions[key_word][randrange(len(keyword_questions.math_questions[key_word]))]
            #create poll with question
            for option in keyword_questions.math_questions[key_word][question]:
                #add option to poll
        elif keyword in keyword_questions.biology_questions.keys():
            question = keyword_questions.biology_questions[key_word][randrange(len(keyword_questions.biology_questions[key_word]))]
            #create poll with question
            for option in keyword_questions.biology_questions[key_word][question]:
                #add option to poll