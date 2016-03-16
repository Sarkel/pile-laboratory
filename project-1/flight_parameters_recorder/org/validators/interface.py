import requests
from org.exceptions.flight import FlightException

__author__ = "Sebastian Kubalski"


class Interface:
    @staticmethod
    def observedObjectStillExists(response: dict, index: str) -> list:
        if index in response:
            return response[index]
        else:
            raise FlightException('not exists')

    @staticmethod
    def isResponseCorrect(status: int) -> None:
        if status is not requests.codes.ok:
            raise FlightException('code')

    @staticmethod
    def isResponseCorrectFormatted(response: requests) -> dict:
        try:
            return response.json()
        except:
            raise FlightException('decoding')

    @staticmethod
    def checkTypes(observed: list) -> None:
        if len(observed) < 12:
            raise FlightException('len')
        elif type(observed[1]) is not float:
            raise FlightException('1')
        elif type(observed[2]) is not float:
            raise FlightException('0')
        elif type(observed[4]) is not int:
            raise FlightException('4')
        elif type(observed[11]) is not str:
            raise FlightException('11')
        elif type(observed[12]) is not str:
            raise FlightException('12')
        elif type(observed[5]) is not int:
            raise FlightException('5')
        elif type(observed[10]) is not int:
            raise FlightException('10')