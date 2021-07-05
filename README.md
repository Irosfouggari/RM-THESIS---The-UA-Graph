# RM-THESIS---KNOWLEDGE-GRAPH
AUTOMATIC MAINTENANCE OF COVID-19 RELATED KNOWLEDGE GRAPHS BASED ON LARGE-SCALE INFORMATION EXTRACTION ON SCIENTIFIC LITERATURE

## Table of Contents (Optional)

- [Motivation](#Motivation)
- [Contribution](#Contributions)
- [Contributing](#contributing)


# Motivation

> Our motivation is to contribute to the necessity for machine-actionable scientific representation through KGs and subsequently to assist researchers in finding papers relevant to their interests. According to related research, indeed plenty of projects are engaged to scientific KGs. The majority of them, however, produce KGs based on pre-existing data models. Our project intends to prove that a KG can indeed be implemented based on a data model which is so general that it can be considered domain-independent and so specific at the same time.

![Σχέδιο χωρίς τίτλο](https://user-images.githubusercontent.com/18035161/110914432-a70b8000-8316-11eb-9805-d9e23cb597ee.jpg)

# Contribution
Our main contribution is the production of the UA-Graph, which is a scientific KG that will assist researchers in finding papers relevant to their research. The production of the graph is based on three individual phases and therefore three individual contributions. <br />
- We propose a semi-automatic methodology that receives scientific data (publication metadata and unstructured text) and extracts structured information ready to be used as input to the KG. Our methodology applies NLP, Topic, and Information Extraction techniques to produce meaningful results from scientific text. <br />
- Additionally, we design the UA-data model, a flexible and interoperable data model. The proposed model is domain-independent and consists of classes, instances and relationships between them. Moreover, the model allows class hierarchies and inheritance.
- Finally, we implement the UA-data model in Neo4j, which is a graph DBMS and finally produce the UA-Graph a scientific and hierarchical KG. In addition, we present a methodology that allows querying this graph top-down. 

In order to evaluate both our methodology and the produced KG, we used the COVID-19 Open Research Dataset (CORD-19). 
> 



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


