# RM-THESIS---KNOWLEDGE-GRAPH
AUTOMATIC MAINTENANCE OF COVID-19 RELATED KNOWLEDGE GRAPHS BASED ON LARGE-SCALE INFORMATION EXTRACTION ON SCIENTIFIC LITERATURE

![architecture](https://user-images.githubusercontent.com/18035161/106641608-aea56f80-6587-11eb-94e7-175ba83db9ee.PNG)

# Introduction

> Anomaly ....

>  

***USER INTERFACE***

![23](https://user-images.githubusercontent.com/18035161/87792650-7b4a0000-c844-11ea-913f-4a3bdf2dcbe2.PNG)
>Anomaly time-series detection tool offers a simplistic browser menu containing the following six tabs: Detect Anomalies, Configure Isolation Forest, Configure One-Class SVM, Configure Decision Tree, Upload a CSV, Connect to InfluxDB. The initial step is providing system with data. The user has the flexibility to provide data either in CSV format or through InfluxDB. In InfluxDB the desired dataset can be easily determined by selecting database and measurement (table).  
Compromise: in order to obtain more accurate results, we agree that each imported dataset should contain two columns [TIME or DATE] [VALUES] and an optional column [CLASS], in case the user wants detect anomalies in supervised mode. 

>By selecting "Detect Anomalies" from the main menu, the user will be led to a new menu with three algorithms (Isolation Forest, One-Class SVM, Decision Tree). The user can pick one from the available algorithms to detect the anomalous points in the dataset uploaded in the former  step. Again, a new Grafana window will automatically highlight the anomalous points.



>Algorithm Configuration:
The application in its simplest mode may detect anomalies directly, however it is possible to determine parameters for a given algorithm.

>Import - Export Configuration: Our tool allows users to save past configuration combinations in the local disk, just by giving a name for the configuration file to the field "Save Configuration as" and by clicking "Export Configuration". A .ini file will be automatically saved in the folder “Configuration” created in each working directory respectively. If the user wants to import a pre-existing configuration combination, can simply import the .ini in the field "Import a configuration file" file and press "Import Configuration".


>Upload a Train Set:
Concerning supervised learning, there is an additional step. User needs to train based on a different dataset (train set). If a user tries to detect anomalies before training, then the system will display a message suggesting user to train first. The upload a training set step, is in the algorithm configuration page. 



## Table of Contents (Optional)

- [Installation](#installation)
- [Grafana](#Grafana)
- [Contributing](#contributing)


---
---

## Installation

- All the `code` required to get started

### Clone

- Clone this repo to your local machine using `https://github.com/Irosfouggari/Anomaly-Detection-Time-Series`






---
## Grafana


## Contributing

> To get started...

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/Irosfouggari/Anomaly-Detection-Time-Series`

### Step 2

- **Read the technical documendation!** 🔨🔨🔨 
    - Add an algorithm following the pre-existing format
    - Add Configuration of the new algorithm in the Main_Web.py
    - Add Detecting Anomalies in the Main_Web.py for this algorithm
    - Visualize the results
