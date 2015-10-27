__author__ = 'eamonnmaguire'

from neomodel import (StructuredNode, IntegerProperty,
                      RelationshipFrom, StringProperty, StructuredRel, DateProperty)


class Author(StructuredNode):
    """
    Lets us know who authored a paper
    """
    author_id = IntegerProperty()

    def papers(self):
        results, columns = self.cypher("START a=node({self}) MATCH a-[:AUTHOR]->(b) RETURN b")
        return [Record.inflate(row[0]) for row in results]


class Reference(StructuredRel):
    """
    type: e.g. self_reference
    """
    type = StringProperty()


class Record(StructuredNode):
    record_id = IntegerProperty()
    date_published = DateProperty()
    author = RelationshipFrom("Author", "AUTHOR")
    reference = RelationshipFrom("Record", "REFERENCE", model=Reference)

    def citations(self):
        """
        :return: everything this record cites
        """
        results, columns = self.cypher("START a=node({self}) MATCH a-[:REFERENCE]->(b) RETURN b")
        return [self.inflate(row[0]) for row in results]

    def references(self):
        """
        Find all references for a publication
        :return:
        """
        results, columns = self.cypher("START a=node({self}) MATCH (b)-[:REFERENCE]->a RETURN b")
        return [self.inflate(row[0]) for row in results]

    def authors(self):
        """
        :return: all authors related to a record
        """
        results, columns = self.cypher("START a=node({self}) MATCH (b)-[:AUTHOR]->a RETURN b")
        return [Author.inflate(row[0]) for row in results]


