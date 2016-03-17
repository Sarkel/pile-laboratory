from threading import BoundedSemaphore
from threading import enumerate as threadsList
from time import sleep
from org.communication.interface import Interface
from org.exceptions.flight import FlightException
from org.exceptions.scheduler import SchedulerException
from org.flightParameterRecorder.local.base import Base
from org.flightParameterRecorder.local.scheduler import Scheduler

__author__ = "Sebastian Kubalski"


class AppManager(object):
    @staticmethod
    def initialize() -> None:
        conn = Base('./test.db')
        conn.createTable()
        conn.close()

    @staticmethod
    def schedule() -> None:
        maxNumberOfThreads = 3
        time = 5
        with BoundedSemaphore(maxNumberOfThreads):
            interface = Interface()
            try:
                while True:
                    threads = []
                    activeThreads = len([x for x in threadsList() if x.getName() is not 'Communication Thread'])
                    if activeThreads < maxNumberOfThreads + 1:
                        threads.append(AppManager._executeRequest(activeThreads, interface, './test.db'))
                    else:
                        for thread in threads:
                            if type(thread) is Scheduler:
                                thread.join()
                        threads.clear()
                        sleep(time)
            except FlightException as e:
                raise e
            except Exception:
                raise SchedulerException('thread')

    @staticmethod
    def _executeRequest(activeThreads: int, interface: Interface, db: str) -> Scheduler:
        print('Initialize new thread')
        thread = Scheduler('Thread: ' + str(activeThreads + 1), interface, db)
        thread.start()
        return thread

