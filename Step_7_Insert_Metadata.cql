CREATE CONSTRAINT ON (p:Publication) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT ON (j:Journal) ASSERT j.name IS UNIQUE;
CREATE CONSTRAINT ON (a:Author) ASSERT a.name IS UNIQUE;


//create node type: Publication 
:auto using periodic commit
load csv with headers from 'file:///English_Data.csv' as line
merge (p:Publication {id: line.cord_uid})
on create set
    p.title =line.title,
    p.doi = line.doi, 
    p.publish_time=line.publish_time,
    p.type="Publication";


//create node type: Journal
:auto using periodic commit
load csv with headers from 'file:///English_Data.csv' as line
with line where line.journal is not null
merge (p:Publication {id: line.cord_uid})
on create set
    p.title =line.title,
    p.doi = line.doi, 
    p.publish_time=line.publish_time,
    p.type="Publication"
merge (j:Journal {name: line.journal})
on create set
	p.type="Journal"
merge (p)-[:PUBLISHED_IN]->(j)


//create node type: Author
:auto using periodic commit
load csv with headers from 'file:///English_Data.csv' as line
merge (p:Publication {id: line.cord_uid})
on create set
    p.title =line.title,
    p.doi = line.doi, 
    p.publish_time=line.publish_time,
    p.type="Publication"
with p,line,split(line.authors, ',') as authors
foreach (f in authors |merge (author:Author {name: f}) merge (p)-[:HAS_AUTHOR]->(author))


