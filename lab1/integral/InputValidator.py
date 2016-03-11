from os import path
from lab1.integral.CustomException import CustomException

__author__ = 'Sebastian Kubalski'

class InputValidator:
    _keys = ('params', 'first', 'last', 'rank', 'numberOfDivisions')

    #check if file exists
    @staticmethod
    def isFileValidator(fileName):
        if not path.isfile(fileName):
            raise CustomException('Parameter is not a file')

    #check if input data format is correct
    @staticmethod
    def inputDataValidator(inputData):
        if type(inputData) is not dict:
            raise CustomException('Incorrect input data')
        for key in InputValidator._keys:
            if key not in inputData.keys():
                raise CustomException('Incorrect input data')

    #check if file name has been passed
    @staticmethod
    def inputParamValidator(params):
        if type(params) is list and len(params) > 1:
            return params[1]
        else:
            raise CustomException('Wrong input parameter')

    #check if input data has correct types
    @staticmethod
    def inputTypeValidator(inputData):
        if type(inputData['params']) is not list:
            raise CustomException('Params should be list')
        elif type(inputData['numberOfDivisions']) is not int:
            raise  CustomException('numberOfDivisions should be integer')
        for key in filter(lambda x: x not in ('params', 'numberOfDivisions'), InputValidator._keys):
            if (type(inputData[key]) is not int) and (type(inputData[key]) is not float):
                raise CustomException(str(key) + ' should be integer or float')
