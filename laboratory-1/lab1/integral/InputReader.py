import json

__author__ = 'Sebastian Kubalski'

#reader class
class InputReader:
    #constructor
    def __init__(self, fileName):
        self.fileName = fileName

    #load data from selected file
    def loadData(self):
        self._inputData = json.loads(open(self.fileName).read())

    #getter for input data
    def getInputData(self):
        return self._inputData
