#!/usr/bin/env python3
from pymongo import MongoClient
"""
Write a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """ retirives all documents """
    documents = mongo_collection.find()
    return list(documents)
