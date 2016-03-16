import random
import requests
from org.validators.interface import Interface as Validator
from org.wrappers.flight import FlightData as Wrapper

__author__ = "Sebastian Kubalski"


class Interface:
    def __init__(self) -> None:
        self._url = 'https://data.flightradar24.com/zones/fcgi/feed.js'
        objects = self._request()
        keys = list(objects.keys())
        self._observedId = keys[random.randint(0, len(objects) - 1)]

    def get(self) -> Wrapper:
        objects = self._request()
        observed = Validator.observedObjectStillExists(objects, self._observedId)
        Validator.checkTypes(observed)
        return Wrapper(self._observedId, observed)

    def _request(self) -> dict:
        response = requests.get(self._url)
        Validator.isResponseCorrect(response.status_code)
        return Validator.isResponseCorrectFormatted(response)