from typing import Sequence
from org.flightParameterRecorder.remote.base import Base

__author__ = "Sebastian Kubalski"


class Communication(object):
    @staticmethod
    def synchronize() -> Sequence[dict]:
        return Base().select(fields={'flightId': True, 'localId': True, '_id': False})
