__author__ = "Sebastian Kubalski"


class ConnectionException(object):
    def __init__(self, msg: str, breakable: bool = False) -> None:
        self.msg = msg
        self.breakable = breakable
    