## Relations

[![Build Status](https://api.travis-ci.org/inspirehep/relations.svg)](https://travis-ci.org/inspirehep/relations)

[![Coverage Status](https://coveralls.io/repos/inspirehep/relations/badge.svg?branch=master&service=github)](https://coveralls.io/github/inspirehep/relations?branch=master)

[![PyPi](https://img.shields.io/pypi/dm/inspire-relations.svg)](https://pypi.python.org/pypi/inspire-relations/)

[![License](https://img.shields.io/github/license/inspirehep/relations.svg)](https://github.com/inspirehep/relations/master/LICENSE.txt)

A simple module built on top of neomodels, py2neo to persist citation graph information to a neo4j graph database.

### Installation

```python

pip install inspire_relation

# export this variable - required for neomodels to connect to the database.
export NEO4J_REST_URL=http://localhost:7474/db/data/

```

```python

relation_manager = RelationManager()
_dummy_citation_network = [
    {"record": 1, "references": [11, 15, 17, 18], "authors": [1, 2, 3]},
    {"record": 2, "references": [15, 17, 18], "authors": [2, 3]}, 
    {"record": 3, "references": [1, 2, 18], "authors": [3, 2]}
]

for citation_graph_item in _dummy_citation_network:
    for reference in citation_graph_item["references"]:
        relation_manager.add_reference(citation_graph_item["record"], reference)

    for author in citation_graph_item["authors"]:
        relation_manager.add_author(citation_graph_item["record"], author)
    
```

Now, from the relation_manager you can get some information back

- Give me back all the citations for record 2

  ```
  citations = self.relation_manager.get_citations_for_record(2)

  for citation in citations:
  	print citation.record_id
  
  #  Will return 3, referring to record 3.
  ```
  


- Give me back the references for a record

  ```
  references = self.relation_manager.get_references_for_record(2)
  
  for reference in references:
    print reference.record_id
    
  #  Will return 18,17,5, referring to the 3 papers references by record 2.
  ```
  
- Give me back the authors for a record

  ```
  authors = self.relation_manager.get_authors_for_record(2)
  
  for author in authors:
    print author.author_id
    
  #  Will return 3 and 2, referring to the 2 author ids for record 2.
  ```
  

I can also easily find which papers were created by a particular author using its author ID.

 ```
  authors = self.relation_manager.get_authors_for_record(2)
  
  papers_for_author = self.relation_manager.get_papers_for_author(2)
  for paper in papers_for_author:
    print paper.record_id
    
  #  Will return 3, 2 and 1, referring to the 3 papers authored by author 2.
  ```
