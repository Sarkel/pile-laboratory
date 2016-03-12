import sys
from lab1.integral.CustomException import CustomException
from lab1.integral.InputReader import InputReader
from lab1.integral.InputValidator import InputValidator
from lab1.integral.TrIntegrator import TrIntegrator

__author__ = 'Sebastian Kubalski'

#class is manager of entire functionality
class ApplicationMgr:
    #constructor
    def __init__(self):
        self._result = None

    #method run entire logic
    def run(self):
        try:
            fileName = InputValidator.inputParamValidator(sys.argv)
            reader = InputReader(fileName)
            InputValidator.isFileValidator(reader.fileName)
            reader.loadData()
            InputValidator.inputDataValidator(reader.getInputData())
            InputValidator.inputTypeValidator(reader.getInputData())
            integralEngine = TrIntegrator(reader.getInputData())
            self._result = integralEngine.integrate()
            self._printResults()
        except KeyboardInterrupt:
            print('Program has been stopped')
        except CustomException as e:
            print(e.msg)
        except Exception:
            print("Something went wrong")


    #printing results of calculating integral
    def _printResults(self):
        print('Result: ' + str(self._result))
