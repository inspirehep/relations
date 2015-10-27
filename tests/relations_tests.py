import unittest

from relations.utils import RelationManager

__author__ = 'eamonnmaguire'


class RelationTest(unittest.TestCase):
    def setUp(self):
        self.relation_manager = RelationManager()

        _dummy_citation_network = [{"record": 1, "references": [11, 15, 17, 18], "authors": [1, 2, 3]},
                                   {"record": 2, "references": [15, 17, 18], "authors": [2, 3]},
                                   {"record": 3, "references": [1, 2, 18], "authors": [3, 2]}]

        for citation_graph_item in _dummy_citation_network:
            for reference in citation_graph_item["references"]:
                self.relation_manager.add_reference(citation_graph_item["record"], reference)

            for author in citation_graph_item["authors"]:
                self.relation_manager.add_author(citation_graph_item["record"], author)

    def test_graph_query(self):

        citations = self.relation_manager.get_citations_for_record(2)
        references = self.relation_manager.get_references_for_record(2)
        authors = self.relation_manager.get_authors_for_record(2)

        print 'CITATIONS'
        for citation in citations:
            print citation.record_id
        self.assertTrue(len(citations) == 1)

        print 'REFERENCES'
        for reference in references:
            print reference.record_id
        self.assertTrue(len(references) == 3)

        print 'AUTHORS'
        for author in authors:
            print author.author_id
        self.assertTrue(len(authors) == 2)

        papers_for_author_2 = self.relation_manager.get_papers_for_author(2)
        print 'PAPERS FOR AUTHOR 2'
        for paper in papers_for_author_2:
            print paper.record_id

        self.assertTrue(len(papers_for_author_2) == 3,
                        msg="The number of papers for author {0} is mismatched with the expected value of 3")
