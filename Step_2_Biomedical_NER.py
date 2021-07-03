# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:57:23 2021
@author: Iro Sfoungari
"""
from sys import exit
import scispacy
import spacy
import pandas as pd
from pathlib import Path
from os import path
import numpy as np
import string
import os.path
import warnings
warnings.filterwarnings("ignore")

#Core models
import en_core_sci_sm

#NER specific models
import en_ner_craft_md
import en_ner_bc5cdr_md
import en_ner_jnlpba_md
import en_ner_bionlp13cg_md

#STANZA
import stanza

#Load the models
nlp_craft_md = en_ner_craft_md.load()
nlp_bc5cdr_md = en_ner_bc5cdr_md.load()
nlp_bionlp13cg = en_ner_bionlp13cg_md.load()
nlp_jnlpba = en_ner_jnlpba_md.load()
med7 = spacy.load("en_core_med7_lg")


#load stanza
nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})


fileinput = str(input("Please give the csv file to be preprocessed:"))
if not ".csv" in fileinput:
  fileinput += ".csv"

     
fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    data = pd.read_csv(fileName)
    print(len(data))
    data=data[0:10]
    fileinput2 = str(input("Please give a directory to save your results:"))
    FilePath = Path(fileinput2)
    if os.path.isdir(FilePath):
        print ("Thanks")
        path = str(FilePath) + str('/Entities/')
        path1 = Path(path)
        try:
            path1.mkdir(parents=True, exist_ok=False)
        except FileExistsError:
            print("Folder is already there")
        else:
            print("Folder was created")
    else: 
        print ("Directory does not exist! Try again")
        exit()

else:
    print ("This file does not exist!")
    exit()



class NER:
        
    def __init__(self,data):
        self.data=data
        print(len(data))
  
    def extract_entities_craft_md(self,abstractList, doiList):
        i = 0
        table= {"cord_uid":[], "Entity":[], "Class":[]}
        for doc in nlp_craft_md.pipe(abstractList):
            doi = doiList[i]
            for x in doc.ents:
              table["cord_uid"].append(doi)
              table["Entity"].append(x.text)
              table["Class"].append(x.label_)
            i +=1
        return table


    def extract_entities_bc5cdr_md(self,abstractList, doiList):
        i = 0
        table= {"cord_uid":[], "Entity":[], "Class":[]}
        for doc in nlp_bc5cdr_md.pipe(abstractList):
            doi = doiList[i]
            for x in doc.ents:
              table["cord_uid"].append(doi)
              table["Entity"].append(x.text)
              table["Class"].append(x.label_)
            i +=1
        return table
    
    def extract_entities_bionlp13cg(self,abstractList, doiList):
        i = 0
        table= {"cord_uid":[], "Entity":[], "Class":[]}
        for doc in nlp_bionlp13cg.pipe(abstractList):
            doi = doiList[i]
            for x in doc.ents:
              table["cord_uid"].append(doi)
              table["Entity"].append(x.text)
              table["Class"].append(x.label_)
            i +=1
        return table

    def extract_entities_jnlpba(self,abstractList, doiList):
        i = 0
        table= {"cord_uid":[], "Entity":[], "Class":[]}
        for doc in nlp_jnlpba.pipe(abstractList):
            doi = doiList[i]
            for x in doc.ents:
              table["cord_uid"].append(doi)
              table["Entity"].append(x.text)
              table["Class"].append(x.label_)
            i +=1
        return table
    
    def extract_entities_med7(self,abstractList, doiList):
        i = 0
        table= {"cord_uid":[], "Entity":[], "Class":[]}
        for doc in med7.pipe(abstractList):
            doi = doiList[i]
            for x in doc.ents:
                table["cord_uid"].append(doi)
                table["Entity"].append(x.text)
                table["Class"].append(x.label_)
            i +=1
        return table
    
    def extract_entities_stanza_i2b2(self,text):
        a_list = []
        doc = nlp(text)
        for ent in doc.entities:
            k = ent.text,ent.type
            a_list.append(tuple(k))
        return a_list
    

#Read in file
Instace=NER(data) 
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
df = data.dropna(subset=['Tokenized_Text'])

#Create disease craft table 
doiList = df['cord_uid'].tolist()
abstractList = df['Tokenized_Text'].tolist()

table = Instace.extract_entities_craft_md(abstractList, doiList)
final_df = pd.DataFrame(table)
final_df.to_csv(os.path.join(path1,r'craft_md.csv'), index = False)

#create bc5cdr  table (DISEASE)
table1 = Instace.extract_entities_bc5cdr_md(abstractList, doiList)
final_df1 = pd.DataFrame(table1)
final_df1.to_csv(os.path.join(path1,r'bc5cdr_md.csv'), index = False)


#create bionlp13cg  table 
table2 = Instace.extract_entities_bionlp13cg(abstractList, doiList)
final_df2 = pd.DataFrame(table2)
final_df2.to_csv(os.path.join(path1,r'bionlp13cg.csv'), index = False)

#create jnlpba  table 
table3 = Instace.extract_entities_jnlpba(abstractList, doiList)
final_df3 = pd.DataFrame(table3)
final_df3.to_csv(os.path.join(path1,r'jnlpba.csv'), index = False)

#create med7  table 
table4= Instace.extract_entities_med7(abstractList, doiList)
final_df4 = pd.DataFrame(table4)
final_df4.to_csv(os.path.join(path1,r'med7.csv'), index = False)


#for stanza
data["Tokenized_Text"]=data["Tokenized_Text"].astype(str) 
n=100
list_df = [data[i:i+n] for i in range(0,data.shape[0],n)]
appended_data = []
for x in range(len(list_df)):
    data_tmp=list_df[x]
    data_tmp["entities"] = data_tmp["Tokenized_Text"].apply(Instace.extract_entities_stanza_i2b2)
    print(data_tmp.head())
    appended_data.append(data_tmp)
    appended_data1 = pd.concat(appended_data)

appended_data = pd.concat(appended_data)
data2 = appended_data1[['cord_uid', 'entities']]

df1 = (data2.assign(category = data2['entities'].str.split(','))
         .explode('entities')
         .reset_index(drop=True))
del df1['category']
df1["entities"]=df1["entities"].astype(str)
df1["entities"]=df1["entities"].str.replace(")", "").str.replace("'", "").str.replace("(", "")
#df2= df1['Intersection'].str.split("\*", expand=True)
df2= df1['entities'].str.split(",", expand=True)
final_df5=pd.concat([df1['cord_uid'], df2], axis=1)
final_df5.columns = ['cord_uid', 'Entity', 'Class']
print(final_df5.head())
final_df5.to_csv(os.path.join(path1,r'stanza.csv'), index = False)


#sources
#https://stanfordnlp.github.io/stanza/ner.html
#https://allenai.github.io/scispacy/
#https://towardsdatascience.com/using-scispacy-for-named-entity-recognition-785389e7918d
