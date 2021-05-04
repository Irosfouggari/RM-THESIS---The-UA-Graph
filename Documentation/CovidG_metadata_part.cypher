CREATE CONSTRAINT ON (sd:Sci_Domain) ASSERT sd.id IS UNIQUE;
CREATE CONSTRAINT ON (jas:Articles) ASSERT jas.id IS UNIQUE;
CREATE CONSTRAINT ON (journals:Journals) ASSERT journals.id IS UNIQUE;
CREATE CONSTRAINT ON (authors:Authors) ASSERT authors.name IS UNIQUE;




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
:auto using periodic commit
load csv with headers from 'file:///Data_no_abstract.csv' as line
match (p:Sci_Domain {name: "Publication", id:"PublicationId" })
match (j:Sci_Domain { name: "Journal", id: "JournalId" })
merge (js:Journals {name: line.journal})
merge (a:Articles {id: line.cord_uid})
on create set
    a.title =line.title,
    a.doi = line.doi, 
    a.publish_time=line.publish_time
MERGE (a)-[:In]->(js)
merge (a)-[:instanceOf]->(p)
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
FOREACH (f in authors |merge (author:Authors {name: f}) merge (author)-[:Authored_by]->(a))
