from threading import Thread
import time
from org.communication.interface import Interface
from org.flightParameterRecorder.local.base import Base

__author__ = "Sebastian Kubalski"


class Scheduler(Thread):
    def __init__(self, name: str,interface: Interface, db: str) -> None:
        Thread.__init__(self)
        self._sleep = 15
        self._interface = interface
        self.setName(name)
        self._db = db

    def run(self) -> None:
        conn = Base(self._db)
        conn.insert(self._interface.get())
        time.sleep(self._sleep)
