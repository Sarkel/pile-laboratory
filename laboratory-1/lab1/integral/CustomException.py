__author__ = 'Sebastian Kubalski'

class CustomException(Exception):
    def __init__(self, msg):
        self.msg = msg
