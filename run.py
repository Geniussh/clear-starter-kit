import numpy as np
from evaluation_utils.base_predictor import BaseMNISTPredictor


class MNISTPredictor(BaseMNISTPredictor):
    def __init__(self):
        pass

    def prediction_setup(self):
        pass

    def prediction(self, image_file_path: str):
        return np.random.randint(0, 10)
