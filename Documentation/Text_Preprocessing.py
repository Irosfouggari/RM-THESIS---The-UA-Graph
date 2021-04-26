"""
Created on Thu Apr 22 15:09:26 2021

@author: Iro Sfoungari
"""
#In case you use a different dataset rename the column containing abstract to 'abstract' and id to 'cord_uid'

# Usual import
from sys import exit
from pathlib import Path
from os import path
import numpy as np
import pandas as pd
import string
import os.path

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from gensim.utils import simple_preprocess


#For language detection
from langdetect import detect

# spaCy for tokenization, stop word removal and  lemmatization
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English

# Create our list of punctuation marks
punctuations = string.punctuation
# Initialize spacy 'en' model, keeping only tagger component needed for lemmatization
nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
parser = English()

#stop words needs to be removed + some other we added
all_stopwords = nlp.Defaults.stop_words
all_stopwords.add("and/or")


fileinput = str(input("Please give the csv file to be preprocessed:"))
if not ".csv" in fileinput:
  fileinput += ".csv"

     
fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    data = pd.read_csv(fileName)
    print(len(data))
    fileinput2 = str(input("Please give a directory to save your results:"))
    FilePath = Path(fileinput2)
    if os.path.isdir(FilePath):
        print ("Thanks")
    else: 
        print ("Directory does not exist! Try again")
        exit()

else:
    print ("This file does not exist!")
    exit()

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
    
    #next step is stopword removal and tokeization with spacy tokenizer     
    def spacy_stropword_rem(self,sentence):
        mytokens = parser(sentence)
        # Lemmatizing each token and converting each token into lowercase
        mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
        # Removing stop words
        mytokens = [ word for word in mytokens if word not in all_stopwords and word not in punctuations]
        return mytokens
    
    
    #clean symbols, unnecessary characters etc. 
    def clean_words(self,sentences):
        for sentence in sentences:
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

        #spacy lemmatization
    def lemmatization(self,texts,allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.lemma_!='-PRON-'])
        return texts_out


    def bigrams(self,texts):
        return [bigram_mod[doc] for doc in texts]

    def trigrams(self,texts):
        return [trigram_mod[bigram_mod[doc]] for doc in texts]
    
    
 
    def save_data(self,data_lemmatized):
       with open(os.path.join(FilePath,'Data_lemmatized.txt'), "w+", encoding="utf-8") as f:
           for item in data_lemmatized:
               f.write("%s\n" % item)



Instace=Data_Preprocessing(data)
#First keep in a separate csv publications with no available abstract
data["abstract"]=data["abstract"].astype(str) 
data_no_abstract = data[data.abstract == 'nan']
data_no_abstract.to_csv(os.path.join(FilePath,r'Data_no_abstract.csv'))
print('\nData without an abstract available: ',len(data_no_abstract))

#1st Step: Language Detection, we keep only the English abstracts 
data= data[data.abstract != 'nan']
data["Lang"]=data["abstract"].apply(Instace.language_detection)
final_dataset=data[data['Lang'].str.contains("en")]
print('\nData with English abstracts: ', len(data))


#tokenization, stopword removal, cleaning unecessary characters, lemmatization
temp=final_dataset[['cord_uid', 'abstract']]
abstract_list= final_dataset.abstract.tolist()
id_list=final_dataset.cord_uid.tolist()
no_stopwords = list(map(Instace.spacy_stropword_rem, abstract_list))
print('\nExample tokenization - stopword removal: ',no_stopwords[5])
token_stop_clean_text = list(Instace.clean_words(no_stopwords))
data_lemmatized = Instace.lemmatization(token_stop_clean_text)
print('\nExample Lemmatization: ',data_lemmatized[5])
k=list(zip(id_list, abstract_list))
print('\nExample Lemmatization: ',k[0])
Lemmatized_Text = pd.DataFrame(k)
Lemmatized_Text.columns = ['cord_uid','Abstract']
#this csv file will be used for NER, I need the cord_uid that is why i kept it in this form
Lemmatized_Text.to_csv(os.path.join(FilePath,r'Lemmatized_Text.csv'))


#bigram and trigram identification
bigram = gensim.models.Phrases(data_lemmatized, min_count=5, threshold=100) # higher threshold fewer phrases.
trigram = gensim.models.Phrases(bigram[data_lemmatized], threshold=100)  
bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)

data_words_bigrams = Instace.bigrams(data_lemmatized)
data_words_trigrams = Instace.trigrams(data_lemmatized)
#I will use these data for LDA 
Instace.save_data(data_lemmatized)


#C:\Users\Iro Sfoungari\Desktop\data2.csv