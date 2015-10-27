__author__ = 'eamonnmaguire'
from relations.model import Record, Author


class RelationManager(object):

    def find_vertex_by_id(self, id, type):
        to_return = None
        if type is 'record':
            records = Record.nodes.filter(record_id=id)
            for record in records:
                to_return = record

        elif type is 'author':
            authors = Author.nodes.filter(author_id=id)
            for author in authors:
                to_return = author

        return to_return

    def get_or_create_vertex(self, id, type):

        if type is 'record':

            record = self.find_vertex_by_id(id, 'record')
            if record is None:
                record = Record(record_id=id)
                record.save()
            return record

        elif type is 'author':

            author = self.find_vertex_by_id(id, 'author')

            if author is None:
                author = Author(author_id=id)
                author.save()

            return author

    def add_reference(self, record_id, reference_id):
        record = self.get_or_create_vertex(record_id, 'record')
        reference = self.get_or_create_vertex(reference_id, 'record')
        record.reference.connect(reference, {'type': 'journal'})
        record.save()

    def add_author(self, record_id, author_id):
        record = self.get_or_create_vertex(record_id, 'record')
        author = self.get_or_create_vertex(author_id, 'author')
        record.author.connect(author)
        record.save()

    def get_citations_for_record(self, record_id):
        existing_record = self.find_vertex_by_id(record_id, 'record')

        if existing_record:
            return existing_record.citations()

    def get_authors_for_record(self, record_id):
        existing_record = self.find_vertex_by_id(record_id, 'record')

        if existing_record:
            return existing_record.authors()

    def get_references_for_record(self, record_id):
        existing_record = self.find_vertex_by_id(record_id, 'record')

        if existing_record:
            return existing_record.references()

    def get_papers_for_author(self, author_id):
        existing_record = self.find_vertex_by_id(author_id, 'author')
        if existing_record:
            return existing_record.papers()
