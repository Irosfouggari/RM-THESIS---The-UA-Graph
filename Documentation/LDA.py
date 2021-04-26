# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:48:16 2021
@author: Iro Sfoungari
"""

# Usual import
from pprint import pprint
import numpy as np
import pandas as pd
from tqdm import tqdm
import string
import os
import ast
from pathlib import Path
from pandas import DataFrame


# Gensim
import gensim
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from gensim.utils import simple_preprocess

#LDA Mallet
from gensim.models.wrappers import LdaMallet

os.environ.update({'MALLET_HOME':r'C:/new_mallet/mallet-2.0.8/'})
mallet_path = r'C:/new_mallet/mallet-2.0.8/bin/mallet.bat'


fileinput = str(input("Please give the txt file:"))
if not ".txt" in fileinput:
  fileinput += ".txt"
    


fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    with open(fileName, 'r',encoding='utf-8') as f:
        data_lemmatized = [ast.literal_eval(line.strip()) for line in f]
        fileinput2 = str(input("Please give a directory to save your results:"))
        FilePath = Path(fileinput2)
        if os.path.isdir(FilePath):
           print ("Thanks")
        else:
            print ("Directory does not exist! Try again")
            exit()

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
        #print(corpus[:1][0][:30])
        return id2word, corpus


    def model(self, id2word, corpus):
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=2, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
        return lda_model
    
    
    
    def lda_Mallet(self, id2word, corpus):
        ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=2, id2word=id2word)
        return ldamallet
    
       
    def file(self):
       fileinput2 = str(input("Please give the csv file to be preprocessed:"))
       if not ".csv" in fileinput2:
           fileinput2 += ".csv"
       fileName2 = Path(fileinput2)
       if fileName2.is_file():
           print ("File exists")
           data = pd.read_csv(fileName2)
           print(len(data))
       else: 
        print ("This file does not exist!")
        self.file()
       return data
   
    def filee(self, data2, lda, corpus):
        print("hiiiii")
        doiList = data2.cord_uid.tolist()
        corpus_transformed = lda[corpus]
        s1=list(corpus_transformed)
        k=list(zip(doiList, s1))
        print(doiList)
        print(s1)
        #df = DataFrame (k,columns=['cord_uid','Topic'])
        #print(k)
        #print(len(df))
        #csv_data = df.to_csv(r'C:/Users/Iro Sfoungari/Desktop/255_cols.csv', index = False)

        #df['Topic'] = df['Topic'].astype(str)
        #df['Topic'] = df['Topic'].str.replace("[","")
        #df['Topic'] = df['Topic'].str.replace("(","")
        #df['Topic'] = df['Topic'].str.replace("]","")
        #df['Topic'] = df['Topic'].str.replace(" ","")

        #df2= df['Topic'].str.split("\),", expand=True)
        #df2.head(10)
        #data2=pd.concat([df['cord_uid'], df2], axis=1)
        #print(data2.head(10))
        return k
       




First_Instace=LDA(data_lemmatized) 
data=data_lemmatized
id2word, corpus= First_Instace.create_dict_corpus(data_lemmatized)
print("it works")
#print(corpus[:1][0][:30])
lda_model=First_Instace.model(id2word, corpus)
#pprint(lda_model.print_topics())


#lda_mallet=First_Instace.model(dictionary, corpus)
#print('\nLDA MALLET: ', lda_mallet.show_topics(formatted=False))
#print("telikoooooo")
#optimal_model = model_list_mallet[9]
#model_topics = lda_mallet.show_topics(formatted=False)
#pprint(lda_mallet.print_topics(num_words=40))



data=First_Instace.file()
#print(data.head(5))

data2=First_Instace.filee(data,lda_model,corpus)
#print(len(data2.columns))
var1= lda_model.num_topics
print(var1)


#C:\Users\Iro Sfoungari\Desktop\sum\Data_lemmatized.txt