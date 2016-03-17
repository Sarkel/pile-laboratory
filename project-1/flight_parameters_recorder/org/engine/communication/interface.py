import random
import requests

from org.engine.validators.interface import Interface as Validator
from org.engine.wrappers.flight import FlightDataWrapper as Wrapper

__author__ = "Sebastian Kubalski"


class Interface(object):
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
        return Validator.isResponseCorrectFormatted(response)
