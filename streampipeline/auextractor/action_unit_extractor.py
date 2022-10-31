from abc import ABC, abstractmethod
import numpy as np

class ActionUnitExtractor(ABC):
    def __init__(self):
        pass

    # TODO: find exact type to return
    @abstractmethod
    def extract_aus(self, frame: np.array):
        pass
