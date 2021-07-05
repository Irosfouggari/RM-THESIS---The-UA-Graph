# RM-THESIS---KNOWLEDGE-GRAPH
AUTOMATIC MAINTENANCE OF COVID-19 RELATED KNOWLEDGE GRAPHS BASED ON LARGE-SCALE INFORMATION EXTRACTION ON SCIENTIFIC LITERATURE

## Table of Contents (Optional)

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

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

# Production 
The production of the UA-Graph is based on the design of a flexible data model and then on the KG implementation. There are four aspects related to the UA-Graph production process. 

- Model Design
- Model Implementation in Neo4j 
- Data Collection and Processing
- KG Population  

This is an <h6> tag


