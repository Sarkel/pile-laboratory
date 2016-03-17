__author__ = "Sebastian Kubalski"


class BasicWrapper(object):
    def __getitem__(self, key: str):
        return getattr(self, key)
    