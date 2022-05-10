######################################################################################
### This is a read-only file to allow participants to run their code locally.      ###
### It will be over-writter during the evaluation, Please do not make any changes  ###
### to this file.                                                                  ###
######################################################################################

import glob
import os
import signal
from contextlib import contextmanager

import pandas as pd
import numpy as np
from sklearn.metrics import f1_score, accuracy_score
from tqdm.auto import tqdm

from evaluation_utils.base_predictor import BaseMNISTPredictor


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise TimeoutException("Prediction timed out!")

    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)


class MNISTEvaluator:
    def __init__(
        self,
        test_data_path: str,
        predictions_file_path: str,
        ground_truth_data_path: str,
        predictor: BaseMNISTPredictor,
    ):
        self.test_data_path = test_data_path
        self.predictions_file_path = predictions_file_path
        self.ground_truth_path = ground_truth_data_path

        self.prediction_setup_timeout = 120
        self.prediction_per_image_timeout = 1
        self.predictions = {}
        self.predictor = predictor

    def validate_predictions(self, prediction):
        assert isinstance(prediction, int)
        assert 0 <= prediction <= 9

    def save_predictions(self):
        df = pd.DataFrame(self.predictions.items(), columns=["image_id", "label"])
        df.to_csv(self.predictions_file_path, index=False)

    def get_all_image_paths(self):
        return glob.glob(os.path.join(self.test_data_path, "*.jpg"))

    def add_prediction(self, img_id, prediction):
        self.validate_predictions(prediction)
        self.predictions[img_id] = prediction

    def evaluation(self):
        try:
            with time_limit(self.prediction_setup_timeout):
                self.predictor.prediction_setup()
        except NotImplementedError:
            pass

        image_paths = self.get_all_image_paths()
        for image_path in tqdm(image_paths):
            with time_limit(self.prediction_per_image_timeout):
                prediction = self.predictor.prediction(image_path)

            image_id = os.path.basename(image_path).replace(".jpg", "")
            if isinstance(prediction, np.ndarray):
                self.add_prediction(image_id, prediction.tolist())
            else:
                self.add_prediction(image_id, prediction)

        self.save_predictions()

    def scoring(self, ground_truth_path, prediction_file_path):
        gt_labels = pd.read_csv(ground_truth_path)
        predictions = pd.read_csv(prediction_file_path)
        assert len(gt_labels) == len(predictions)

        gt_labels = gt_labels.sort_values(by="image_id")
        predictions = predictions.sort_values(by="image_id")

        scores = {
            "score": f1_score(gt_labels["label"].values, predictions["label"].values, average="macro"),
            "score_secondary": accuracy_score(gt_labels["label"].values, predictions["label"].values),
            "meta": {}
        }
        return scores
