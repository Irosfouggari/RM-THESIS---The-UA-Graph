# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:25:26 2021

@author: Iro Sfoungari
"""

# Usual import
from sys import exit
from pathlib import Path
from os import path
import numpy as np
import pandas as pd
import string
import os.path


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
    path=str(FilePath)
    path1 = path + str('/')
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
        data_length=len(data)
        print(data_length)
        
    def ask_entity_type(self):
        entity = str(input("Which Entity Class do you want to extract? : ")).upper()
        if entity == "":
            exit()
        else:
            print(entity)
        return entity
    
    def create_csv(self,data,entity):
        df=data[data['Class'].str.contains(entity)]
        len(df)
        if (len(df)==0):
                print("This Entity category does not exist!")
        data2=df.groupby('cord_uid', sort=False).Entity.unique().agg(', '.join).reset_index()
        data2.head(5)
        data2['Class'] = entity
        return data2


        
        

Instance=Data_Preprocessing(data)
entity=Instance.ask_entity_type() 
data2=Instance.create_csv(data,entity) 
print(data2.head(5))
if (len(data2!=0)):
    data2['Entity'] = data2['Entity'].str.strip()
    data2.Entity = data2.Entity.replace('\s+', ' ', regex=True)
    data2.to_csv(path1 + entity +'_Entities.csv', index = False)
else: 
    exit()

#C:/Users/Iro Sfoungari/Desktop/sum/Entities/bc5cdr_md.csv