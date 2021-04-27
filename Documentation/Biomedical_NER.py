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
df = data.dropna(subset=['Abstract'])

#Create disease craft table 
doiList = df['cord_uid'].tolist()
abstractList = df['Abstract'].tolist()
table = Instace.extract_entities_craft_md(abstractList, doiList)
final_df = pd.DataFrame(table)
final_df.to_csv(os.path.join(FilePath,r'craft_md.csv'))

#create bc5cdr  table (DISEASE)
table1 = Instace.extract_entities_bc5cdr_md(abstractList, doiList)
final_df1 = pd.DataFrame(table1)
final_df1.to_csv(os.path.join(FilePath,r'bc5cdr_md.csv'))


#create bionlp13cg  table 
table2 = Instace.extract_entities_bionlp13cg(abstractList, doiList)
final_df2 = pd.DataFrame(table2)
final_df2.to_csv(os.path.join(FilePath,r'bionlp13cg.csv'))

#create jnlpba  table 
table3 = Instace.extract_entities_jnlpba(abstractList, doiList)
final_df3 = pd.DataFrame(table3)
final_df3.to_csv(os.path.join(FilePath,r'jnlpba.csv'))

#create med7  table 
table4= Instace.extract_entities_med7(abstractList, doiList)
final_df4 = pd.DataFrame(table4)
final_df4.to_csv(os.path.join(FilePath,r'med7.csv'))


#for stanza
data["Abstract"]=data["Abstract"].astype(str) 
data=data[0:10]
data["entities"] = data["Abstract"].apply(Instace.extract_entities_stanza_i2b2)
df1 = (data.assign(category = data['entities'].str.split(','))
         .explode('entities')
         .reset_index(drop=True))
del df1['category']
df1["entities"]=df1["entities"].astype(str)
df1["entities"]=df1["entities"].str.replace(")", "").str.replace("'", "").str.replace("(", "")
#df2= df1['Intersection'].str.split("\*", expand=True)
df2= df1['entities'].str.split(",", expand=True)
df3=pd.concat([df1['cord_uid'], df2], axis=1)
print(df3.head())
df3.to_csv(os.path.join(FilePath,r'stanza_i2b2.csv'))

#C:/Users/Iro Sfoungari/Desktop/sum/Lemmatized_Text.csv