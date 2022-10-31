import numpy as np

import auextractor
import auinterpreter
import bowprocessor


class PipelineCombiner:

    au_extractor: auextractor.ActionUnitExtractor
    au_interpreter: auinterpreter.ActionUnitInterpreter
    bow_processor: bowprocessor.BoWProcessor

    def __init__(self):
        self.au_extractor = auextractor.PyFeatAUExtractor()

    def append(self, frame: np.array):
        aus = self.au_extractor.extract_aus(frame)
        duchenne_smile = self.au_interpreter.interpret_aus(aus)

        # Save duchenne smile to time series here?

        self.bow_processor.append(duchenne_smile)

    def get_current_word(self):
        pass
