#!/usr/bin/env python3
'''Task 8 module.
'''

import pymongo


def list_all(mongo_collection):
    """Return list of all docs in collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
