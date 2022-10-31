import numpy as np
from feat import Detector

import action_unit_extractor


class PyFeatAUExtractor(action_unit_extractor.ActionUnitExtractor):
    detector: Detector

    def __init__(self):
        super().__init__()

        self.detector = Detector(
            face_model="retinaface",
            landmark_model="mobilefacenet",
            au_model="jaanet",
            emotion_model="resmasknet",
            facepose_model="img2pose",
        )

    def extract_aus(self, frame: np.array):
        return self.detector.detect_image(["no_smile.jpg"])
