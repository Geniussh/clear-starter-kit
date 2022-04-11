import numpy as np
from evaluation_utils.base_predictor import BaseMNISTPredictor


class MNISTPredictor(BaseMNISTPredictor):
    def __init__(self):
        pass

    def prediction_setup(self):
        seed_value = 12345
        np.random.seed(seed_value)

    def prediction(self, image_file_path: str):
        return np.random.randint(0, 10)


if __name__ == "__main__":
    from local_evaluation import main

    main()
