"""
=========
IMPORTANT
=========

THE CONTENTS OF THIS FILE WILL BE REPLACED DURING EVALUATION.
ANY CHANGES MADE TO THIS FILE WILL BE DROPPED DURING EVALUATION.

THIS FILE IS PROVIDED ONLY FOR YOUR CONVINIENCE TO TEST THE CODE LOCALLY.

"""

from tqdm.auto import trange
from config import SubmissionConfig
from evaluator.mnist_evaluator import MNISTEvaluator


def main():
    predictor = SubmissionConfig.predictor()
    evaluator = MNISTEvaluator()
    scores = []

    iterations = 10000

    for _ in trange(iterations):
        result = predictor.predict_batch([i for i in range(10)])
        assert len(result) == 10
        scores.append(evaluator.evaluate(result))
    
    return {
        "score": sum(scores)/iterations,
    }


if __name__ == "__main__":
    score = main()
    print(score)

