# RM-THESIS---KNOWLEDGE-GRAPH
AUTOMATIC MAINTENANCE OF COVID-19 RELATED KNOWLEDGE GRAPHS BASED ON LARGE-SCALE INFORMATION EXTRACTION ON SCIENTIFIC LITERATURE

## Table of Contents (Optional)

- [Introduction](#Introduction)
- [Process](#Process)
- [Contributing](#contributing)


# Introduction

> This project inspired by knowledge graphs will attempt to provide assistance to people involved with research regarding COVID-19 which is today’s major global health concern. The proposed method involves the employment of knowledge graphs. Since COVID-19 pandemic began to spread, a plethora of publications have appeared and research towards a cure will be prevalent globally for some time to come. In other words, we will attempt to design a system which will explore knowledge graphs (browse and search), so as to assist researchers in finding papers relevant to their interests based on topics, quality, and connections with other papers.

![architecture](https://user-images.githubusercontent.com/18035161/106641608-aea56f80-6587-11eb-94e7-175ba83db9ee.PNG)




# Process
# Steps that lead to the KG generation
> Step 1: Data Cleaning and preprocessing. See the `code` snippet above. 
>Input data: All the abstracts from the Initial Dataset
>Output Data: A version of the intitial dataset containing only english publications and the Data_lemmatized.txt



>Step 2: Topic Extraction. 
>Input data: Data_lemmatized.txt from Step:1 
>Output Data: LDA model



>Step 3: Scispacy Entity extraction. 
>Input data: Only english publications from Step:1
>Output Data: All the available Scispacy entities: bc5cdr.csv, bionlp13cg, craft_md.csv, jnlpba.csv


>Step 3: Entity Preprocessing. All the entities should follow the pattern: Cord_uid, Entity, Class. So here we have to group all the entities based on the publication they belong to and then specify their class. Each csv file should contain only a unique class. 
>Input data: CSV files extracted on step: 3
>Output Data: One class entities eg. Disease, DNA, RNA, CHEBI, TAXON ...


