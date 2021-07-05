# RM-THESIS---THE UA-KNOWLEDGE GRAPH
AUTOMATIC MAINTENANCE OF COVID-19 RELATED KNOWLEDGE GRAPHS BASED ON LARGE-SCALE INFORMATION EXTRACTION IN SCIENTIFIC LITERATURE

## Table of Contents
- [Motivation](#Motivation)
- [Contribution](#Contribution)
- [Production](#Production)

# Motivation

> Main motivation: to contribute to the necessity for machine-actionable scientific representation through KGs and subsequently to assist researchers in finding papers relevant to their interests. This project intends to prove that a KG can indeed be implemented based on a data model which is so general that it can be considered domain-independent and so specific at the same time.


# Contribution
Main contribution: the production of the UA-Graph, which is a scientific KG that will assist researchers in finding papers relevant to their research. 
- We propose a semi-automatic methodology that receives scientific data (publication metadata and unstructured text) and extracts structured information ready to be used as input to the KG. Our methodology applies NLP, Topic, and Information Extraction techniques to produce meaningful results from scientific text. <br />
- Additionally, we design the UA-data model, a flexible and interoperable data model. The proposed model is domain-independent and consists of classes, instances and relationships between them. Moreover, the model allows class hierarchies and inheritance.
- Finally, we implement the UA-data model in Neo4j, which is a graph DBMS and finally produce the UA-Graph a scientific and hierarchical KG. In addition, we present a methodology that allows querying this graph top-down. 

In order to evaluate both our methodology and the produced KG, we used the COVID-19 Open Research Dataset (CORD-19). 
> 

# Production 
The production of the UA-Graph is based on the design of a flexible data model and then on the KG implementation. There are four aspects related to the UA-Graph production process. 

- Model Design
- Model Implementation in Neo4j 
- Data Processing
- KG Population  

### Data Processing
![code_to_graph](https://user-images.githubusercontent.com/18035161/124457430-17d61c80-dd8c-11eb-93c5-2886508485ba.jpg)


