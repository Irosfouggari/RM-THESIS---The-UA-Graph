CREATE CONSTRAINT ON (sd:Sci_Domain) ASSERT sd.id IS UNIQUE;
CREATE CONSTRAINT ON (jas:Articles) ASSERT jas.id IS UNIQUE;
CREATE CONSTRAINT ON (journals:Journals) ASSERT journals.id IS UNIQUE;
CREATE CONSTRAINT ON (authors:Authors) ASSERT authors.name IS UNIQUE;
CREATE CONSTRAINT ON (bc:Biomedical_Concepts) ASSERT bc.name IS UNIQUE;
CREATE CONSTRAINT ON (t:Topics) ASSERT t.tid IS UNIQUE;




CREATE (o:Sci_Domain { name: "Object", id: "ObjectId" })
CREATE (t:Sci_Domain { name: "topic",  id: "TopicId" })
CREATE (e:Sci_Domain { name: "Entity",  id: "EntityId" })
CREATE (p:Sci_Domain { name: "Publication", id:"PublicationId" })
CREATE (per:Sci_Domain { name: "Person", id: "PersonId" })
CREATE (org:Sci_Domain { name: "Organisation", id: "OrganisationId" })
CREATE (bc:Sci_Domain { name: "Biomedical_Concept",  identifier: "Biomedical_ConceptId" })
CREATE (ca:Sci_Domain { name: "Conference_Article", id: "Conference_ArticleId" })
CREATE (ja:Sci_Domain { name: "Journal_Article", id: "Journal_ArticleId" })
CREATE (a:Sci_Domain { name: "Author", id: "AuthorId" })
CREATE (pub:Sci_Domain { name: "Publisher", id: "PublisherId" })
CREATE (uni:Sci_Domain { name: "University", id: "UniversityId" })
CREATE (ser:Sci_Domain { name: "Series", id: "SeriesId" })
CREATE (j:Sci_Domain { name: "Journal", id: "JournalId" })
CREATE (pro:Sci_Domain { name: "Proceedings", id: "ProceedingsId" })


CREATE (t)-[:isA]->(o)
CREATE (e)-[:isA]->(o)
CREATE (p)-[:isA]->(e)
CREATE (per)-[:isA]->(e)
CREATE (org)-[:isA]->(e)
CREATE (bc)-[:isA]->(e)
CREATE (ca)-[:isA]->(p)
CREATE (ja)-[:isA]->(p)
CREATE (a)-[:isA]->(per)
CREATE (pub)-[:isA]->(org)
CREATE (uni)-[:isA]->(org)
CREATE (ser)-[:isA]->(e)
CREATE (j)-[:isA]->(ser)
CREATE (pro)-[:isA]->(ser)


//create article label nodes
:auto using periodic commit 10000
load csv with headers from 'file:///Data_no_abstract.csv' as line
with line where line.journal is not null
match (ja:Sci_Domain { name: "Journal_Article", id: "Journal_ArticleId" })
match (j:Sci_Domain { name: "Journal", id: "JournalId" })
merge (js:Journals {name: line.journal})
merge (a:Articles {id: line.cord_uid})
on create set
    a.title =line.title,
    a.doi = line.doi, 
    a.publish_time=line.publish_time
MERGE (a)-[:In]->(js)
merge (a)-[:instanceOf]->(ja)
merge (js)-[:instanceOf]->(j)


:auto using periodic commit
load csv with headers from 'file:///Data_no_abstract.csv' as line
merge (articles:Articles {id: line.cord_uid})
on create set
    articles.title =line.title,
    articles.doi = line.doi, 
    articles.publish_time=line.publish_time
WITH articles,line,split(line.authors, ',') AS authors
match (a:Sci_Domain { name: "Author", id: "AuthorId" })
FOREACH (f in authors |merge (author:Authors {name: f}) merge (articles)-[:Authored_by]->(author))
FOREACH (f in authors |merge (author:Authors {name: f}) merge (author)-[:instanceOf]->(a))





//create  entities and relationship with publication
:auto using periodic commit
load csv with headers from 'file:///Entities/jnlpba/CELL_TYPE_Entities.csv' as line
match (bc:Sci_Domain { name: "Biomedical_Concept",  identifier: "Biomedical_ConceptId" })
merge (articles:Articles {id: line.cord_uid})
merge (disease:Sci_Domain { name: "Cell_type", id: "Cell_typeId" })
merge (disease)-[:isA]->(bc)
WITH articles,line,split(line.Entity, ',') AS entities
match (disease:Sci_Domain { name: "Cell_type", id: "Cell_typeId" })
foreach (f in entities |merge (entity:Biomedical_Concepts {name: f}) merge (articles)-[:refers]->(entity))
foreach (f in entities |merge (entity:Biomedical_Concepts {name: f}) merge (entity)-[:instanceOf]->(disease))
return count(entities)




:auto using periodic commit
LOAD CSV WITH HEADERS FROM 'file:///Topics/FinalKeywordsforallTopics.csv' AS line
match (topic:Sci_Domain { name: "topic",  id: "TopicId" }),(articles:Articles {id: line.cord_uid})
merge (t:Topics {tid: line.rec_id}), (articles)-[r:HAS_TOPIC{Probability:line.Probability}]->(t), (t)-[:isA]->(topic)
with t, SPLIT(line.Final_Topic_Keywords,',') AS word
  set t.k1 = word[0], t.k2= word[1],t.k3 = word[2], t.k4= word[3], t.k5 = word[4], t.k6= word[5],t.k7 = word[6], t.k8= word[7],t.k9 = word[8], t.k10= word[9]
return count(t)


:auto using periodic commit
LOAD CSV WITH HEADERS FROM 'file:///Topics/KeywordsBecameEntities.csv' AS line
merge (t:Topics {tid:line.rec_id}), (e:Entity {name: line.Word})
merge (t)-[:K{ProbabProbability:line.Probability}]->(e)


//External Source

//create Journal type nodes
:auto using periodic commit
load csv with headers from 'file:///crossref_metadata.csv' as line
match (org:Sci_Domain { name: "Organisation", id: "OrganisationId" })
merge (p:Publishers {name: line.publisher}), (a:Articles {id: line.cord_uid})
merge (p)-[:instanceOf]->(org), (a)-[:Published_by]->(p)