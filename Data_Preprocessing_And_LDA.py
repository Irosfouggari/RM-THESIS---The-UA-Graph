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
    
    #next step is stopword removal and tokeization with spacy tokenizer     
    def spacy_stropword_rem(self,sentence):
        mytokens = parser(sentence)
        # Lemmatizing each token and converting each token into lowercase
        mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
        # Removing stop words
        mytokens = [ word for word in mytokens if word not in stopwords and word not in punctuations]
        return mytokens
    
    
    #cleaning a bit leftovers maybe numbers using Gensim’s simple_preprocess()
    def clean_words(self,sentences):
        for sentence in sentences:
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations

    
    def make_bigrams(self,texts):
        return [bigram_mod[doc] for doc in texts]

    def make_trigrams(self,texts):
        return [trigram_mod[bigram_mod[doc]] for doc in texts]
    
    
    #spacy lemmatization
    def lemmatization(self,texts):
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.lemma_!='-PRON-'])
            return texts_out


class LDA:
    
    def __init__(self,data_lemmatized):
        self.data=data_lemmatized
        print("hii kai twra")

    
    def compute_coherence_values(self, dictionary, corpus, texts, limit, start=2, step=3):
        coherence_values = []
        model_list = []
        for num_topics in range(start, limit, step):
            model=LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)
            model_list.append(model)
            coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='c_v')
            coherence_values.append(coherencemodel.get_coherence())
    
        return model_list, coherence_values






First_Instace=Data_Preprocessing(data) 
data["Lang"]=data["abstract"].apply(First_Instace.language_detection) #passes a Series object, row-wise
#we keep only the english abstracts
data=data[data['Lang'].str.contains("en")]
print("We care only about english abstracts!")
print(len(data))
data_temp  = data.abstract.tolist()
no_stopwords = list(map(First_Instace.spacy_stropword_rem, data_temp))
tokenized_clean_text = list(First_Instace.clean_words(no_stopwords))
bigram = gensim.models.Phrases(tokenized_clean_text, min_count=5, threshold=100) # higher threshold fewer phrases.
trigram = gensim.models.Phrases(bigram[tokenized_clean_text], threshold=100)  
bigram_mod = gensim.models.phrases.Phraser(bigram)
trigram_mod = gensim.models.phrases.Phraser(trigram)
data_words_bigrams = First_Instace.make_bigrams(tokenized_clean_text)
data_words_trigrams = First_Instace.make_trigrams(data_words_bigrams)
data_lemmatized = First_Instace.lemmatization(data_words_trigrams)
print(data_lemmatized[0])

#FOR LDA
First_Instace2=LDA(data_lemmatized) 

# Create Dictionary
id2word = corpora.Dictionary(data_lemmatized)
# Create Corpus
texts = data_lemmatized
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# View
print(corpus[:1][0][:30])
model_list, coherence_values = First_Instace2.compute_coherence_values(dictionary=id2word, corpus=corpus, texts=data_lemmatized, start=2, limit=20, step=3)
# Print the coherence scores
#for m, cv in zip(x, coherence_values):
 #   print("Num Topics =", m, " has Coherence Value of", round(cv, 4))

#C:\Users\Iro Sfoungari\Desktop\data2.csv