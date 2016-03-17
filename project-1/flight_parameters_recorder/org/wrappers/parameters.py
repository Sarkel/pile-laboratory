from org.wrappers.basicwrapper import BasicWrapper

__author__ = "Sebastian Kubalski"


class ParametersWrapper(BasicWrapper):
    def __init__(self, parameters: tuple) -> None:
        self.localId = parameters[0]
        self.flightId = parameters[1]
        self.latitude = parameters[2]
        self.longitude = parameters[3]
        self.altitude = parameters[4]
        self.start = parameters[5]
        self.destination = parameters[6]
        self.speed = parameters[7]
        self.time = parameters[8]
