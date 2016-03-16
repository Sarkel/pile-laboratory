import sqlite3
from typing import Sequence
from org.wrappers.flight import FlightData

__author__ = "Sebastian Kubalski"


class Base:
    #constructor
    def __init__(self, path: str) -> None:
        self._db = sqlite3.connect(path)
        self._db.isolation_level = None
        self._cur = self._db.cursor()

    def close(self) -> None:
        self._db.close()

    def createTable(self) -> None:
        statement = '''
            CREATE TABLE IF NOT EXISTS Parameters(
                id INTEGER PRIMARY KEY,
                flight_id TEXT,
                latitude NUMERIC,
                longitude NUMERIC,
                altitude INTEGER,
                start VARCHAR(10),
                destination VARCHAR(10),
                speed INTEGER,
                time BIGINT
            );
        '''
        self._cur.execute(statement)

    def dropTable(self) -> None:
        self._cur.execute('DROP TABLE Parameters;')

    def select(self) -> Sequence[dict]:
        self._cur.execute('SELECT * FROM Parameters')
        return self._cur.fetchall()

    def insert(self, observed: FlightData) -> None:
        statement = '''
            INSERT INTO Parameters(
              flight_id,
              latitude,
              longitude,
              altitude,
              start,
              destination,
              speed,
              time)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self._cur.execute(statement, tuple([observed[name] for name in observed.keys()]))