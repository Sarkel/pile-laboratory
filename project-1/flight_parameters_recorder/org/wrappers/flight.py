__author__ = "Sebastian Kubalski"


class FlightData:
    def __init__(self, key: str, observed: list) -> None:
        self.id = key
        self.latitude = observed[1]
        self.longitude = observed[2]
        self.altitude = observed[4]
        self.start = observed[11]
        self.destination = observed[12]
        self.speed = observed[5]
        self.time = observed[10]

    def keys(self):
        return ['id', 'latitude', 'longitude', 'altitude', 'start', 'destination', 'speed', 'time']

    def __getitem__(self, item: str):
        return getattr(self, item)