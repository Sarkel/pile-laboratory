from sqlite3 import connect
from typing import Sequence

from org.engine.wrappers.flight import FlightDataWrapper
from org.engine.wrappers.parameters import ParametersWrapper

__author__ = "Sebastian Kubalski"


class Base(object):
    def __init__(self, path: str) -> None:
        self._db = connect(path)
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

    def select(self, params: tuple=None) -> Sequence[dict]:
        if params:
            self._cur.execute('SELECT * FROM Parameters WHERE id IN (?);', (params))
        else:
            self._cur.execute('SELECT * FROM Parameters;')
        return [ParametersWrapper(element) for element in self._cur.fetchall()]

    def insert(self, observed: FlightDataWrapper) -> None:
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
            VALUES(?, ?, ?, ?, ?, ?, ?, ?);
        '''
        self._cur.execute(statement, tuple([observed[name] for name in FlightDataWrapper.keys()]))
