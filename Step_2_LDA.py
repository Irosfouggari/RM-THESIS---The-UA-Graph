# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:58:49 2021

@author: Iro Sfoungari
"""

# Usual import
import numpy as np
import pandas as pd
import string
import ast


# Gensim
import gensim
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from gensim.utils import simple_preprocess
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from gensim.test.utils import datapath




fileinput = str(input("File:"))
if not ".txt" in fileinput:
  fileinput += ".txt"

from pathlib import Path
     
fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    with open(fileName, 'r',encoding='utf-8') as f:
        data_lemmatized = [ast.literal_eval(line.strip()) for line in f]
    
else:
    print ("This file does not exist!")


class LDA:
    
    def __init__(self,data):
        self.data=data
        print("hii")
        print(len(data))

    def create_dict_corpus(self,data):
         # Create Dictionary
        id2word = corpora.Dictionary(data)
        # Create Corpus
        texts = data
        # Term Document Frequency
        corpus = [id2word.doc2bow(text) for text in texts]
        # View
        print(corpus[:1][0][:30])
        return id2word, corpus

    def compute_coherence_values(self, dictionary, corpus, texts, limit=30, start=2, step=3):
        """
        Compute c_v coherence for various number of topics
    
        Parameters:
        ----------
        dictionary : Gensim dictionary
        corpus : Gensim corpus
        texts : List of input texts
        limit : Max num of topics
    
        Returns:
        -------
        model_list : List of LDA topic models
        coherence_values : Coherence values corresponding to the LDA model with respective number of topics
        """
        coherence_values = []
        model_list = []
        for num_topics in range(start, limit, step):
            model=LdaModel(corpus, dictionary, num_topics)
            model_list.append(model)
            coherencemodel = CoherenceModel(self,model, texts, dictionary, coherence='c_v')
            coherence_values.append(self, coherencemodel.get_coherence())
    
        return model_list, coherence_values

     
    def save(self,):
        #Save model to disk.
        temp_file = datapath("C:/Users/Iro Sfoungari/Desktop/THESIS DATA/FINAL_DATABASE/lda_model.csv")
        optimal_model.save(temp_file)
        



First_Instace=LDA(data_lemmatized) 
dictionary, corpus= First_Instace.create_dict_corpus(data_lemmatized)
model_list, coherence_values = First_Instace.compute_coherence_values(dictionary, corpus, data_lemmatized)
x = range(start, limit, step)

for m, cv in zip(x, coherence_values):
    print("Num Topics =", m, " has Coherence Value of", round(cv, 4))

optimal_model = model_list[5]
model_topics = optimal_model.show_topics(formatted=False)






#C:\Users\Iro Sfoungari\Desktop\example_data_lem.txt