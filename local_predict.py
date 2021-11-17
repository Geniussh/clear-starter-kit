from tqdm.auto import trange
from config import SubmissionConfig
from evaluator.evaluator import AIcrowdEvaluator


def main():
    predictor = SubmissionConfig.predictor()
    evaluator = AIcrowdEvaluator()
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

