from typing import Sequence
from pymongo import MongoClient

__author__ = "Sebastian Kubalski"


class Base(object):
    def __init__(self) -> None:
        self._client = MongoClient()
        self._db = self._client['pite-project-1']
        self._collection = self._db['flight-parameters']

    def insert(self, document: Sequence[dict]) -> list:
        return self._collection.insert_many(document).inserted_ids

    def select(self, search: dict = None, fields: dict = None) -> Sequence[dict]:
        cursor = self._collection.find(search, fields)
        return [doc for doc in cursor]

    def close(self) -> None:
        self._client.close()