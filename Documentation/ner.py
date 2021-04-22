# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 15:57:23 2021

@author: Iro Sfoungari
"""
from sys import exit
import scispacy
import spacy
import pandas as pd

#Core models
import en_core_sci_sm

#NER specific models
import en_ner_craft_md
import en_ner_bc5cdr_md
import en_ner_jnlpba_md
import en_ner_bionlp13cg_md

#Load the models
nlp_craft_md = en_ner_craft_md.load()
nlp_bc5cdr_md = en_ner_bc5cdr_md.load()
nlp_bionlp13cg = en_ner_bionlp13cg_md.load()
nlp_jnlpba = en_ner_jnlpba_md.load()
med7 = spacy.load("en_core_med7_lg")

fileinput = str(input("File:"))
if not ".csv" in fileinput:
  fileinput += ".csv"

from pathlib import Path
     
fileName = Path(fileinput)
if fileName.is_file():
    print ("File exists")
    data = pd.read_csv(fileName)
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

#Read in file
Instace=NER(data) 
df = data.dropna(subset=['abstract'])

#Create disease craft table 
doiList = df['cord_uid'].tolist()
abstractList = df['abstract'].tolist()
table = Instace.extract_entities_craft_md(abstractList, doiList)
final_df = pd.DataFrame(table)
print(final_df)

#create bc5cdr  table (DISEASE)
table1 = Instace.extract_entities_bc5cdr_md(abstractList, doiList)
final_df1 = pd.DataFrame(table1)
print(final_df1)


#create bionlp13cg  table 
table2 = Instace.extract_entities_bionlp13cg(abstractList, doiList)
final_df2 = pd.DataFrame(table2)
print(final_df2)

#create jnlpba  table 
table3 = Instace.extract_entities_bionlp13cg(abstractList, doiList)
final_df3 = pd.DataFrame(table3)
print(final_df3)

#create med7  table 
table4= Instace.extract_entities_med7(abstractList, doiList)
final_df4 = pd.DataFrame(table4)
print(final_df4)


#C:/Users/Iro Sfoungari/Desktop/data2.csv