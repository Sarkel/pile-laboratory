__author__ = 'Sebastian Kubalski'

class TestHelper:
    @staticmethod
    def createInputData(first, last) -> dict:
        return {
            "params": [1, 0],
            "rank": 1,
            "first": first,
            "last": last,
            "numberOfDivisions": 10000
        }
