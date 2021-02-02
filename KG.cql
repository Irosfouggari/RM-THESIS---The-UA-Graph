#Read the first line of the CSV-Cypher (check for required properties)
LOAD CSV WITH HEADERS FROM
"file:///complaints.csv" AS LINE
RETURN LINE
limit 1


//Create: All Nodes Indexes (unique constraint)
// Uniqueness constraints.
CREATE CONSTRAINT ON (c:Complaint) ASSERT c.id IS UNIQUE;
CREATE CONSTRAINT ON (c:Company) ASSERT c.name IS UNIQUE;
CREATE CONSTRAINT ON (r:Response) ASSERT r.name IS UNIQUE;
CREATE CONSTRAINT ON (p:Product) ASSERT p.name IS UNIQUE;
CREATE CONSTRAINT ON (i:Issue) ASSERT i.name IS UNIQUE;
CREATE CONSTRAINT ON (s:SubProduct) ASSERT s.name IS UNIQUE;
CREATE CONSTRAINT ON (s:SubIssue) ASSERT s.name IS UNIQUE;

//Create: Complaint nodes with properties (split date)
// Load Complaint Nodes.
LOAD CSV WITH HEADERS
FROM "file:///complaints.csv" AS line
WITH DISTINCT line, SPLIT(line.`Date received`, '/') AS date
CREATE (complaint:Complaint { id: TOINT(line.`Complaint ID`) })
SET complaint.year = TOINT(date[2]),
complaint.month = TOINT(date[0]),
complaint.day = TOINT(date[1])


//Create: Company, Response nodes with MERGE (find or create)
// Load Company, Response Nodes.
LOAD CSV WITH HEADERS
FROM "file:///Consumer_Complaints.csv" AS line
MERGE (company:Company { name: UPPER(line.Company) })
MERGE (response:Response { name: UPPER(line.`Company
response to consumer`) })


'H1N1 influenza infection' 'cancer' 'H1N1 infection'
 'acute respiratory failure' 'viral H1N1 infection' 'solid organ tumors'
 'hematological malignancies' 'bacterial bronchopneumonia' 'deaths'
 'organ failure' 'lung disease' 'alveolar damage' 'bronchiolitis'
 'hemorrhage' 'H1N1 viral infection' 'illness'
 'acute respiratory distress syndrome' 'death'