# This file is part of the Etsin service
#
# Copyright 2017-2018 Ministry of Education and Culture, Finland
#
# :author: CSC - IT Center for Science Ltd., Espoo Finland <servicedesk@csc.fi>
# :license: MIT

import json


class ESDatasetModel:
    """
    Class for Metax dataset data that can be indexed into Etsin Elasticsearch
    """

    def __init__(self, doc_obj):
        self.doc_obj = doc_obj

    def to_es_document_string(self):
        return json.dumps(self.doc_obj)

    def get_es_document_id(self):
        return self.doc_obj.get('identifier', '')
