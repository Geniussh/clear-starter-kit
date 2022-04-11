"""
=========
IMPORTANT
=========

THE CONTENTS OF THIS FILE WILL BE REPLACED DURING EVALUATION.
ANY CHANGES MADE TO THIS FILE WILL BE DROPPED DURING EVALUATION.

THIS FILE IS PROVIDED ONLY FOR YOUR CONVINIENCE TO TEST THE CODE LOCALLY.

"""

import os
from evaluation_utils.mnist_evaluator import MNISTEvaluator
from run import MNISTPredictor


def main():
    evaluator = MNISTEvaluator(
        test_data_path=os.getenv("AICROWD_DATASET_DIR", "data/images"),
        predictions_file_path=os.getenv("AICROWD_PREDICTIONS_FILE", "data/results.csv"),
        ground_truth_data_path=os.getenv("AICROWD_GROUND_TRUTH_PATH", "data/labels.csv"),
        predictor=MNISTPredictor(),
    )
    evaluator.evaluation()
    scores = evaluator.scoring(evaluator.ground_truth_path, evaluator.predictions_file_path)
    print(scores)


if __name__ == "__main__":
    main()
