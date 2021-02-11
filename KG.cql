CREATE CONSTRAINT ON (p:Publication) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT ON (j:Journal) ASSERT j.name IS UNIQUE;
CREATE CONSTRAINT ON (a:Author) ASSERT a.name IS UNIQUE;
CREATE CONSTRAINT ON (e:Entity) ASSERT e.name IS UNIQUE;
CREATE CONSTRAINT ON (d:Disease) ASSERT d.name IS UNIQUE;
CREATE CONSTRAINT ON (c:Cancer) ASSERT c.name IS UNIQUE;
CREATE CONSTRAINT ON (pr:Protein) ASSERT pr.name IS UNIQUE;



//Create Publication node
LOAD CSV WITH HEADERS FROM 'file:///General_Data.csv' AS row
WITH row.cord_uid AS cordId, row.title AS title, row.doi AS doi, 
datetime(row.publish_time) AS publish_time
MERGE (p:Publication {cord_id: cordId})
  SET p.title = title, p.doi = doi,p.publish_time=publish_time
RETURN count(p)


//Create Journal node
LOAD CSV WITH HEADERS FROM 'file:///General_Data.csv' AS row
MERGE (p:Publication {cord_id:row.cord_uid})
MERGE (j:Journal {name: row.journal})
MERGE (p)-[:PUBLISHED_IN]->(j)
RETURN count(j)


//Create Authors
LOAD CSV WITH HEADERS FROM 'file:///General_Data.csv' AS row
MERGE (p:Publication {cord_id:row.cord_uid})
WITH p,row,split(row.authors, ';') AS authors
FOREACH (f in authors |merge (author:Author {name: f}) merge (p)-[:HAS_AUTHOR]->(author))


//Create (disease) entities and relationship with publication
LOAD CSV WITH HEADERS FROM 'file:///DiseasesForNeo_Class.csv' AS row
MERGE (p:Publication {cord_id:row.cord_uid})
WITH p,row,split(row.Entity, ',') AS entities
FOREACH (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:IDENTIFIED_IN]->(p))



//disease entities and relationship with DISEASE node
LOAD CSV WITH HEADERS FROM 'file:///DiseasesForNeo_Class.csv' AS row
MERGE (d:Disease {name:row.Class})
WITH d,row,split(row.Entity, ',') AS entities
FOREACH (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:INSTANCE_OF]->(d))


//Create (protein) entities and relationship with publication
LOAD CSV WITH HEADERS FROM 'file:///ProteinsToNeo_Class.csv' AS row
MERGE (p:Publication {cord_id:row.cord_uid})
WITH p,row,split(row.Entity, ',') AS entities
FOREACH (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:IDENTIFIED_IN]->(p))


//protein entities and relationship with PROTEIN node
LOAD CSV WITH HEADERS FROM 'file:///ProteinsToNeo_Class.csv' AS row
MERGE (pr:Protein {name:row.Class})
WITH pr,row,split(row.Entity, ',') AS entities
FOREACH (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:INSTANCE_OF]->(pr))


//Create (cancer) entities and relationship with publication
LOAD CSV WITH HEADERS FROM 'file:///CancerForNeo_Class.csv' AS row
MERGE (p:Publication {cord_id:row.cord_uid})
WITH p,row,split(row.Entity, ',') AS entities
FOREACH (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:IDENTIFIED_IN]->(p))

//cancer entities and relationship with CANCER node
LOAD CSV WITH HEADERS FROM 'file:///CancerForNeo_Class.csv' AS row
MERGE (c:Cancer {name:row.Class})
WITH c,row,split(row.Entity, ',') AS entities
FOREACH (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:INSTANCE_OF]->(c))







//Create Topic
LOAD CSV WITH HEADERS FROM 'file:///ready.csv' AS row
WITH row.Dominant_Topic AS DT, row.Topic_Keywords AS kw
MERGE (t:Topic {dt: DT})
WITH t, SPLIT(kw,',') AS word
  SET t.k1 = word[0], t.k2= word[1],t.k3 = word[2], t.k4= word[3], t.k5 = word[4], t.k6= word[5],t.k7 = word[6], t.k8= word[7],t.k9 = word[8], t.k10= word[9]
RETURN count(t)

 
// Trial Topic
LOAD CSV WITH HEADERS FROM 'file:///te_notgood.csv' AS row,WITH row.Topic0 AS First_topic,MERGE (tt:Trial_Topic {ft:First_topic}),WITH tt, SPLIT(First_topic,',') AS word,  SET tt.k1 = word[0], tt.k2= word[1],tt.k3 = word[2], tt.k4= word[3], tt.k5 = word[4], tt.k6= word[5],tt.k7 = word[6], tt.k8= word[7],tt.k9 = word[8], tt.k10= word[9],RETURN count(tt),, ,
