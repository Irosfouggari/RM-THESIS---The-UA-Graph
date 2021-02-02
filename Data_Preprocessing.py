# Usual import
from pprint import pprint
import numpy as np
import pandas as pd
from tqdm import tqdm
import string

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary

#For language detection
from langdetect import detect

# spaCy for tokenization, stop word removal and  lemmatization
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
#!python -m spacy download en_core_web_lg

# Create our list of punctuation marks
punctuations = string.punctuation
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')
parser = English()


fileinput = str(input("File:"))
if not ".csv" in fileinput:
  fileinput += ".csv"

from pathlib import Path
     
fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    data = pd.read_csv(fileName)
    print(len(data))
else:
    print ("This file does not exist!")


class Data_Preprocessing:
    
    def __init__(self,data):
        self.data=data
        print("hii")
        data_length=len(data)
        print(data_length)
    
    #first step language detection
    def language_detection(self,sentence):
        try:
            lang = detect(sentence)
        except:
            lang = 'Other'
        return lang
    
    #next step is tokenization with spacy tokenizer 
    def tokenization(self,sentence):
        mytokens = parser(sentence)
        # Lemmatizing each token and converting each token into lowercase
        mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
        # Removing stop words
        mytokens = [ word for word in mytokens if word not in stopwords and word not in punctuations ]
        # return preprocessed list of tokens
        mytokens = " ".join([i for i in mytokens])
        return mytokens
    
     #some more preprocessing and put text into list 
    #some more preprocessing and put text into list 

    def sent_to_words(self,sentences):
         for sentence in sentences:
             yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
             print("shmera bghkan eukola")
             return sentences # deacc=True removes punctuations

    def big_trig_model(self):
        # Build the bigram and trigram models
        bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100) # higher threshold fewer phrases.
        trigram = gensim.models.Phrases(bigram[data_words], threshold=100)  

        # Faster way to get a sentence clubbed as a trigram/bigram
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        trigram_mod = gensim.models.phrases.Phraser(trigram)
        return trigram

    def make_bigrams(self,texts):
        return [self.big_trig_model.bigram_mod[doc] for doc in texts]


First_Instace=Data_Preprocessing(data) 
data["Lang"]=data["abstract"].apply(First_Instace.language_detection) #passes a Series object, row-wise
#we keep only the english abstracts
data=data[data['Lang'].str.contains("en")]
print(len(data))
data["processed_description"] = data["abstract"].apply(First_Instace.tokenization)
data2 = data.processed_description.values.tolist()
data_words = list(First_Instace.sent_to_words(data2))
print(data_words[0])
First_Instace.big_trig_model()
# Form Bigrams
data_words_bigrams =First_Instace.make_bigrams(data_words)
print(print(data_words_bigrams[0]))
#C:\Users\Iro Sfoungari\Desktop\data2.csv