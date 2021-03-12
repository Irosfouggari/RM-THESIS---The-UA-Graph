CREATE CONSTRAINT ON (e:Entity) ASSERT e.name IS UNIQUE;
CREATE CONSTRAINT ON (c:Concept) ASSERT c.name IS UNIQUE;
CREATE CONSTRAINT ON (t:Topic) ASSERT t.tid IS UNIQUE;




//create  entities and relationship with publication
:auto using periodic commit
load csv with headers from 'file:///Entities/Cancer_Entities.csv' as line
merge (p:Publication {id: line.cord_uid})
on create set
    p.title =line.title,
    p.doi = line.doi, 
    p.publish_time=line.publish_time,
    p.type="Publication"
with p,line,split(line.Entity, ',') as entities
foreach (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:IDENTIFIED_IN]->(p))

//Connect entities with the class - concept they belong to
:auto using periodic commit
load csv with headers from 'file:///Entities/Cell_Entities.csv' as line
merge  (c:Concept {name:line.Class})
with c,line,split(line.Entity, ',') as entities
foreach (f in entities |merge (entity:Entity {name: f}) merge (entity)-[:INSTANCE_OF]->(c))



:auto using periodic commit
LOAD CSV WITH HEADERS FROM 'file:///Topics/Final_Topic_keywords.csv' AS row
WITH row.rec_id AS tid, row.Final_Topic_Keywords AS kw
merge (t:Topic {tid: tid})
with t, SPLIT(kw,',') AS word
  set t.k1 = word[0], t.k2= word[1],t.k3 = word[2], t.k4= word[3], t.k5 = word[4], t.k6= word[5],t.k7 = word[6], t.k8= word[7],t.k9 = word[8], t.k10= word[9]
return count(t)


:auto using periodic commit
LOAD CSV WITH HEADERS FROM 'file:///Topics/Final_Topic_keywords.csv' AS line
merge (p:Publication {id: line.cord_uid})
on create set
    p.title =line.title,
    p.doi = line.doi, 
    p.publish_time=line.publish_time,
    p.type="Publication"
MERGE (t:Topic {tid:line.rec_id})
MERGE (p)-[r:HAS_TOPIC {Probability:line.Probability}]->(t)
RETURN count(r)


:auto using periodic commit
LOAD CSV WITH HEADERS FROM 'file:///Topics/KeywordsBecameEntities.csv' AS line
merge (t:Topic {tid:line.rec_id})
merge (e:Entity {name: line.Word})
merge (t)-[:K{ProbabProbability:line.Probability}]->(e)
