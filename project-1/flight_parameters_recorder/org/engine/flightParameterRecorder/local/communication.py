from random import randint
from threading import Timer
from urllib.request import urlopen
from urllib.error import URLError

import time
import jsonpickle
import requests

from org.engine.exceptions.connection import ConnectionException
from org.engine.flightParameterRecorder.local.base import Base

__author__ = "Sebastian Kubalski"


class Communication(object):
    def __init__(self) -> None:
        Communication.schedule(self.__init__)
        self._url = 'localhost:8000'
        self._sleep = 5
        self._run()

    @staticmethod
    def _synchronize(local: list) -> list:
        #response = requests.get(self._url).json()
        # mocked data for development
        response = [{"latitude": 40.1217, "longitude": 111.8845, "localId": 1, "speed": 340, "time": 1458176200, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1217, "longitude": 111.8845, "localId": 2, "speed": 340, "time": 1458176200, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1217, "longitude": 111.8845, "localId": 3, "speed": 340, "time": 1458176200, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1234, "longitude": 111.8497, "localId": 4, "speed": 340, "time": 1458176215, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1234, "longitude": 111.8497, "localId": 5, "speed": 340, "time": 1458176215, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1234, "longitude": 111.8497, "localId": 6, "speed": 340, "time": 1458176215, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1258, "longitude": 111.8006, "localId": 7, "speed": 340, "time": 1458176240, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1258, "longitude": 111.8006, "localId": 8, "speed": 340, "time": 1458176240, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1258, "longitude": 111.8006, "localId": 9, "speed": 340, "time": 1458176240, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1278, "longitude": 111.7588, "localId": 10, "speed": 339, "time": 1458176260, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1278, "longitude": 111.7588, "localId": 11, "speed": 339, "time": 1458176260, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1278, "longitude": 111.7588, "localId": 12, "speed": 339, "time": 1458176260, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1296, "longitude": 111.7192, "localId": 13, "speed": 339, "time": 1458176279, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1296, "longitude": 111.7192, "localId": 14, "speed": 339, "time": 1458176279, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 40.1296, "longitude": 111.7192, "localId": 15, "speed": 339, "time": 1458176279, "altitude": 36100, "destination": "HMI", "flightId": "91dd4d6", "start": "PEK"}, {"latitude": 37.2701, "longitude": 128.4722, "localId": 16, "speed": 510, "time": 1458222271, "altitude": 37025, "destination": "KIX", "flightId": "91ee82d", "start": "TSN"}, {"latitude": 37.2701, "longitude": 128.4722, "localId": 17, "speed": 510, "time": 1458222271, "altitude": 37025, "destination": "KIX", "flightId": "91ee82d", "start": "TSN"}, {"latitude": 37.2701, "longitude": 128.4722, "localId": 18, "speed": 510, "time": 1458222271, "altitude": 37025, "destination": "KIX", "flightId": "91ee82d", "start": "TSN"}, {"latitude": 37.2585, "longitude": 128.5128, "localId": 19, "speed": 510, "time": 1458222286, "altitude": 37000, "destination": "KIX", "flightId": "91ee82d", "start": "TSN"}, {"latitude": 37.2585, "longitude": 128.5128, "localId": 20, "speed": 510, "time": 1458222286, "altitude": 37000, "destination": "KIX", "flightId": "91ee82d", "start": "TSN"}, {"latitude": 37.2585, "longitude": 128.5128, "localId": 21, "speed": 510, "time": 1458222286, "altitude": 37000, "destination": "KIX", "flightId": "91ee82d", "start": "TSN"}]
        dif = []
        for loc in local:
            isDif = True
            for el in response:
                if (loc['localId'] is el['localId']) and (loc['flightId'] is el['flightId']):
                    isDif = False
            if isDif:
                dif.append(loc)
        return dif

    @staticmethod
    def _check() -> None:
        try:
            urlopen('http://google.pl', timeout=1)
        except URLError:
            raise ConnectionException('connection')

    def _run(self) -> None:
        db = Base('./test.db')
        Communication._check()
        diffs = self._synchronize(list(db.select()))
        # self._updateRemote(diffs)
        print(jsonpickle.encode(diffs, unpicklable=False))
        time.sleep(self._sleep)

    def _updateRemote(self, data: list) -> None:
        requests.post(self._url, jsonpickle.encode(data), unpicklable=False)

    @staticmethod
    def schedule(function: callable) -> None:
        interval = 5 * 60
        timer = Timer(interval, function)
        timer.setName('Communication Thread ' + str(randint(0, 10000)))
        timer.start()
