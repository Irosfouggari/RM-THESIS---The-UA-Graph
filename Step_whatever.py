# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:07:15 2021

@author: Iro Sfoungari
"""

# Usual import
import numpy as np
import pandas as pd
from pathlib import Path
import os
import pandas as pd
import glob
####### import data into neo4j ##### 
from neo4j import GraphDatabase
from py2neo import Graph

#graph = Graph("bolt://localhost:7687", user="neo4j", password="1111")



user_input = input("Enter the folder containing all the Topic files:")
if (os.path.exists(user_input)):
    print("Folder exists")
    path =user_input # use your path
    #k=graph.run("MATCH (e:Entity)-[IDENTIFIED_IN]->(p:Publication) RETURN e.name, p.id").data()
    #df = pd.DataFrame(k)
    #print(len(df))
    #Entities=df.groupby('p.id', sort=False).agg(', '.join).reset_index()
    #Entities.rename(columns = {'e.name':'Entities'}, inplace = True)
    #Entities.rename(columns = {'p.id':'id'}, inplace = True)
    #print(Entities.head())
    Entities = pd. read_csv("C:/Users/Iro Sfoungari/Desktop/ayeaye.csv")
else:
    print("Folder does not exist, try again!")





class Topics:
    
    def __init__(self,path):
        self.path=path
        print("hii")
 
    from re import search


    def Intersection(self, s0, s1):
        temp_list = []
        k=s0
        s0 = ''.join([i for i in s0 if not i.isdigit()])
        s0 = s0.replace(".*", "")
        l1 = s0.split(",")
        l2= s1.split(",")
        l3=k.split(",")
        x= list(set(l1).intersection(set(l2)))
        for idx, word in enumerate(x):
            for i in range(len(l3)):
                g = ''.join([i for i in l3[i] if not i.isdigit()])
                g= g.replace(".*", "")
                if word==g:
                    temp_list.append(l3[i])
        k= ",".join(str(x) for x in temp_list)
        return k

    def Final_Topic_Keywords(self, s0, s1):
        s0List = s0.split(",")
        x=s0List
        s1List = s1.split(",")
        y=s1List
        x= [i for i in y if i not in x]
        k= ", ".join(str(j) for j in x)
        return(k)
    

    def Topic_Keywords(self,path,Entities):
        all_files = glob.glob(path + "/*.csv")
        li = []
        i=0
        for filename in all_files:
            topics = pd.read_csv(filename, index_col=None, header=0)
            topics['Entities'] = topics.cord_uid.map(Entities.set_index('id')['Entities'])
            topics["Entities"]=topics["Entities"].astype(str)
            topics["Entities"]=topics["Entities"].str.replace(", ", ",")
            topics["Entities"]=topics["Entities"].str.replace(", ", ",")
            topics['Intersection'] = topics.apply(lambda x: self.Intersection(x.Topic, x.Entities), axis=1)
            topics["Intersection"]=topics["Intersection"].astype(str)
            topics['Final_Topic_Keywords'] = topics.apply(lambda x: self.Final_Topic_Keywords(x.Intersection, x.Topic), axis=1)
            topics = topics.assign(rec_id=np.arange(len(topics))).reset_index(drop=True)
            topics['rec_id'] ='T'+str(i)+'_' + topics['rec_id'].astype(str)
            #csv_data = topics.to_csv(r'C:/Users/Iro Sfoungari/Desktop/somethinggg/new/'+str(i)+'Topic.csv', index = False)
            i=i+1
            li.append(topics)
        frame = pd.concat(li, axis=0, ignore_index=True)
        csv_data = frame.to_csv(path+'/FinalKeywordsforallTopics.csv', index = False)
        return(frame)
    
    def Keywords_became_entities(self,path,topics):
        result=topics[topics['Intersection']!='']
        result=result.drop(['Topic', 'Probability', 'Entities', 'Final_Topic_Keywords'], axis = 1) 
        splitted = result['Intersection'].str.split(',\s*')
        s = splitted.str.len()
        df = pd.DataFrame({'rec_id': np.repeat(result['rec_id'].values, s),
                           'Intersection':np.concatenate(splitted.values)}, columns=['rec_id','Intersection'])
        df1= df['Intersection'].str.split("\*", expand=True)
        df2=pd.concat([df['rec_id'], df1], axis=1)
        df2.columns = ['rec_id', 'Probability', 'Word']
        csv_data = df2.to_csv(path+'/KeywordsBecameEntities.csv', index = False)
        return(df2)

First_Instace=Topics(path) 
FinalKeywordsforallTopics=First_Instace.Topic_Keywords(path,Entities)
K=First_Instace.Keywords_became_entities(path,FinalKeywordsforallTopics)

#C:\Users\Iro Sfoungari\Desktop\somethinggg
#C:\Users\Iro Sfoungari\Desktop\THESIS DATA\FINAL_DATABASE\Topics