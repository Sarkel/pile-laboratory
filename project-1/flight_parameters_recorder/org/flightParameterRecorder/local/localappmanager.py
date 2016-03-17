from threading import BoundedSemaphore
from threading import active_count as activeThreads
from time import sleep
from org.communication.interface import Interface
from org.exceptions.flight import FlightException
from org.exceptions.scheduler import SchedulerException
from org.flightParameterRecorder.local.base import Base
from org.flightParameterRecorder.local.scheduler import Scheduler

__author__ = "Sebastian Kubalski"


class LocalAppManager(object):
    def __init__(self):
        self._maxNumberOfThreads = 3
        self._time = 5

    @staticmethod
    def initialize() -> None:
        conn = Base('./test.db')
        conn.createTable()
        conn.close()

    def schedule(self) -> None:
        with BoundedSemaphore(self._maxNumberOfThreads):
            interface = Interface()
            try:
                while True:
                    threads = []
                    if activeThreads() < self._maxNumberOfThreads + 1:
                        threads.append(self._executeRequest(interface, './test.db'))
                    else:
                        for thread in threads:
                            if type(thread) is Scheduler:
                                thread.join()
                        threads.clear()
                        sleep(self._time)
            except FlightException as e:
                raise e
            except Exception:
                raise SchedulerException('thread')

    def _executeRequest(self, interface: Interface, db: str) -> Scheduler:
        print('Initialize new thread')
        thread = Scheduler('Thread: ' + str(activeThreads() + 1), interface, db)
        thread.start()
        return thread
