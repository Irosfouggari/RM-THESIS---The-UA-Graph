# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:48:16 2021
@author: Iro Sfoungari
"""

# Usual import
from pprint import pprint
from pandas import DataFrame
from sys import exit
import numpy as np
import pandas as pd
import ast

import string
import os
import ast
from pathlib import Path

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from gensim.models.ldamodel import LdaModel
from gensim.corpora.dictionary import Dictionary
from gensim.utils import simple_preprocess

#LDA Mallet
from gensim.models.wrappers import LdaMallet

#os.environ.update({'MALLET_HOME':r'C:/new_mallet/mallet-2.0.8/'})
#mallet_path = r'C:/new_mallet/mallet-2.0.8/bin/mallet.bat'


fileinput = str(input("Please give the txt file:"))
if not ".txt" in fileinput:
  fileinput += ".txt"
    


fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    with open(fileName, 'r') as f:
        text_list = ast.literal_eval(f.read())
        fileinput2 = str(input("Please give a directory to save your results:"))
        FilePath = Path(fileinput2)
        path=str(FilePath)
        fullpath=str(path +'/')
        if os.path.isdir(FilePath):
           print ("Thanks")
           path = fullpath + str('/Topics/')
           path1 = Path(path)

           try:
               path1.mkdir(parents=True, exist_ok=False)
           except FileExistsError:
                  print("Folder is already there")
           else:
                print("Folder was created")
           while True:
               try:
                   topic_num = int(input("Enter the number of topics: "))
                   break
               except ValueError:
                   print("Please input integer...")  
                   continue
        else:
            print ("Directory does not exist! Try again")
            exit()
else:
    print ("This file does not exist!")
    exit()



class LDA:
    
    def __init__(self,text_list):
        self.text_list=text_list
        print("hii")
        print(len(text_list))

    def create_dict_corpus(self,text):
         # Create Dictionary
        id2word = corpora.Dictionary(text)
        # Create Corpus
        texts = text
        # Term Document Frequency
        corpus = [id2word.doc2bow(text) for text in texts]
        # View
        print(corpus[:1][0][:30])
        return id2word, corpus


    def model(self, id2word, corpu,num_topics):
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics, 
                                           random_state=100,
                                           passes=50,
                                           alpha='auto',
                                           per_word_topics=True)
        return lda_model
    
    
    '''
    def lda_Mallet(self, id2word, corpus):
        ldamallet = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=2, id2word=id2word)
        return ldamallet
    '''
       
    def articles_to_topics(self,corpus,lda_model,id_list):
        lda_corpus = lda_model.get_document_topics(corpus)
        k=[doc for doc in lda_corpus]
        k1=list(zip(id_list, k))
        print(k1)
        df = DataFrame (k1,columns=['cord_uid','Topic'])
        df['Topic'] = df['Topic'].astype(str)
        df['Topic'] = df['Topic'].str.replace("[","").str.replace("(","").str.replace("]","").str.replace(" ","")
        df2= df['Topic'].str.split("\),", expand=True)
        data=pd.concat([df['cord_uid'], df2], axis=1)

        return df,data
   
    def Topics_per_doc(self,data,df,lda_model):
        for x in range(len(data.columns)-1):
            Datas_First_Topic = data[['cord_uid', x]]
            Datas_First_Topic= Datas_First_Topic[x].str.split(",", expand=True)
            Datas_First_Topic=pd.concat([df['cord_uid'], Datas_First_Topic], axis=1)
            Datas_First_Topic.columns = ['cord_uid', 'Topic', 'Probability']
            Datas_First_Topic['Probability'] = Datas_First_Topic['Probability'].str.replace(")","")
            new_df = Datas_First_Topic[Datas_First_Topic["Topic"].str.contains('None') == False]
            for index, row in new_df.iterrows():
                row['Topic']=lda_model.print_topic(int(row['Topic']))
            new_df['Topic']=new_df['Topic'].str.replace('"','')
            new_df['Topic']=new_df['Topic'].str.replace(" ","")
            new_df['Topic']=new_df['Topic'].str.replace("+",", ")
            new_df["Topic"]=new_df["Topic"].str.replace(", ", ",")
            new_df.to_csv(path +str(x)+'_Topic.csv', index = False)






Instace=LDA(text_list)
Lemmatized_Text = DataFrame (text_list,columns=['cord_uid','Topic'])
id_list=Lemmatized_Text.cord_uid.tolist()
id2word, corpus= Instace.create_dict_corpus(Lemmatized_Text['Topic'])


lda_model=Instace.model(id2word, corpus,topic_num)
print(lda_model.print_topics(num_topics=topic_num))

df,data=Instace.articles_to_topics(corpus,lda_model,id_list)
print(data.head(5))

Instace.Topics_per_doc(data,df,lda_model)



#C:\Users\Iro Sfoungari\Desktop\sum\Text_for_TE.txt