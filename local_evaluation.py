"""
=========
IMPORTANT
=========

THE CONTENTS OF THIS FILE WILL BE REPLACED DURING EVALUATION.
ANY CHANGES MADE TO THIS FILE WILL BE DROPPED DURING EVALUATION.

THIS FILE IS PROVIDED ONLY FOR YOUR CONVINIENCE TO TEST THE CODE LOCALLY.

"""

import os
from evaluation_utils.clear_evaluator import CLEAREvaluator
from run import CLEARPredictor


def main():
    evaluator = CLEAREvaluator(
        test_data_path=os.getenv("AICROWD_DATASET_DIR", "test_data"),
        models_path=os.path.join(os.getcwd(), "models"),
        predictions_file_path=os.getenv(
            "AICROWD_PREDICTIONS_FILE", "results/shared/predictions.txt"
        ),
        predictor=CLEARPredictor(),
    )
    evaluator.evaluation()
    scores = evaluator.scoring(evaluator.ground_truth_path, evaluator.predictions_file_path)
    print(scores)


if __name__ == "__main__":
    main()
