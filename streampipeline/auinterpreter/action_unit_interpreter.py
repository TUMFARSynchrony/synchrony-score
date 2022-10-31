from abc import ABC, abstractmethod


class ActionUnitInterpreter(ABC):

    # TODO: figure out input format
    @abstractmethod
    def interpret_aus(self, aus):
        pass