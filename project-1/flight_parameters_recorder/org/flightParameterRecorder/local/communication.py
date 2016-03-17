import requests

__author__ = "Sebastian Kubalski"


class Communication(object):
    def __init__(self) -> None:
        self._url = 'localhost:8000'

    def synchronize(self, local: list) -> bool:
        response = requests.get(self._url)
