#!/usr/bin/env python3
""" Write a Python function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """ ... """
    doc = {
            "topics": {
                "$elemMatch": {
                    "$eq": topic,
                    },
                },
            }
    return [d for d in mongo_collection.find(doc)]
