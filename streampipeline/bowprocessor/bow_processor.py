from abc import ABC, abstractmethod


class BoWProcessor(ABC):

    timeseries: list

    def __init__(self):
        self.timeseries = []

    @abstractmethod
    def append(self, interpreted_aus):
        pass

    # TODO: get with offset?
    @abstractmethod
    def get(self):
        pass
