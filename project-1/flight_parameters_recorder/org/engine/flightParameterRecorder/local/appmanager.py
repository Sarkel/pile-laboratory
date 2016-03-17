from threading import BoundedSemaphore, Thread
from threading import enumerate as threadsList
from time import sleep

from org.engine.communication.interface import Interface
from org.engine.exceptions.flight import FlightException
from org.engine.exceptions.scheduler import SchedulerException
from org.engine.flightParameterRecorder.local.base import Base
from org.engine.flightParameterRecorder.local.communication import Communication
from org.engine.flightParameterRecorder.local.scheduler import Scheduler

__author__ = "Sebastian Kubalski"


class AppManager(object):
    @staticmethod
    def _synchronize():
        Communication()

    @staticmethod
    def run():
        AppManager._initialize()
        AppManager._schedule()
        AppManager._synchronize()

    @staticmethod
    def _initialize() -> None:
        conn = Base('./test.db')
        conn.createTable()
        conn.close()

    @staticmethod
    def _schedule() -> None:
        def fun(x: Thread): ('Communication Thread' not in x.getName()) and (x.getName() is not 'MainThread')
        maxNumberOfThreads = 3
        time = 5
        with BoundedSemaphore(maxNumberOfThreads):
            interface = Interface()
            try:
                while True:
                    threads = []
                    activeThreads = len([x for x in threadsList() if fun(x)])
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
