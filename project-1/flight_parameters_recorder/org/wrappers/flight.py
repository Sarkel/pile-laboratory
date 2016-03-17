from typing import Sequence
from org.wrappers.basicwrapper import BasicWrapper

__author__ = "Sebastian Kubalski"


class FlightDataWrapper(BasicWrapper):
    def __init__(self, key: str, observed: list) -> None:
        self.id = key
        self.latitude = observed[1]
        self.longitude = observed[2]
        self.altitude = observed[4]
        self.start = observed[11]
        self.destination = observed[12]
        self.speed = observed[5]
        self.time = observed[10]

    @staticmethod
    def keys() -> Sequence[str]:
        return ['id', 'latitude', 'longitude', 'altitude', 'start', 'destination', 'speed', 'time']
