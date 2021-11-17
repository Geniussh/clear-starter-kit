import json
import numpy as np
from evaluator.base_predictor import AIcrowdPredictor


class RandomPredictor(AIcrowdPredictor):
    def __init__(self):
        self.model = None
        self.model_path = "models/model.json"
        self.load_model()

    def load_model(self):
        if self.model is not None:
            return

        with open(self.model_path) as fp:
            self.model = json.load(fp)

    def predict_batch(self, batch_input):
        result = []
        for sample in batch_input:
            result.append(np.random.randint(self.model["lower_bound"], self.model["upper_bound"]))
        return result


