import numpy as np
import nltk
import tkinter as tk
import string
import random
from pyparsing import Word
f=open('twitter.txt','r',errors = 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower() #Converts text to lowercase
nltk.download('punkt') #Using the Punkt tokenizer
nltk.download('wordnet') #Using the WordNet dictionary
nltk.download('omw-1.4')
sent_tokens = nltk.sent_tokenize(raw_doc) #Converts doc to list of sentences 
word_tokens = nltk.word_tokenize(raw_doc) #Converts doc to list of words
sent_tokens[:2]
word_tokens[:2]
lemmer = nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREET_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greet(sentence):
 
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def response(msg):
  robo1_response=''
  TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
  tfidf = TfidfVec.fit_transform(sent_tokens)
  vals = cosine_similarity(tfidf[-1], tfidf)
  idx=vals.argsort()[0][-2]
  flat = vals.flatten()
  flat.sort()
  req_tfidf = flat[-2]
  if(req_tfidf==0):
    robo1_response=robo1_response+"I am sorry! I don't understand you"
    return robo1_response
  else:
    robo1_response = robo1_response+sent_tokens[idx]
    return robo1_response
def get_response(msg1):
    msg1 = msg1.lower()
    if(msg1!='bye'):
        if(msg1=='thanks' or msg1=='thank you' ):
            flag=False
            print("BOT: You are welcome..")
        else:
            if(greet(msg1)!=None):
                print("BOT: "+greet(msg1))
            else:
            
                sent_tokens.append(msg1)
                word_tokens=sent_tokens+nltk.word_tokenize(msg1)
                final_words=list(set(word_tokens))
                print("BOT: ",end="")
                print(response(msg1))
                sent_tokens.remove(msg1)
    else:
        flag=False
        print("BOT: Goodbye! Take care <3 ")
    