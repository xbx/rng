'''
Created on Aug 27, 2012

@author: xbx
'''
from pymongo import Connection
from bson import InvalidDocument
import logging


class RngDbHandler(object):
    """ Database access handler """

    def __init__(self, collection, db='rng', host='localhost',
                 port=None):
        """ Init log handler and store the collection handle """

        self.collection = Connection(host, port)[db][collection]

    def insert(self, record):
        """ Store the record to the collection. Async insert """
        try:
            self.collection.save(record)
        except InvalidDocument, e:
            logging.error("Unable to save log record: %s", e.message)

    def find(self):
        return [x for x in self.collection.find()]
