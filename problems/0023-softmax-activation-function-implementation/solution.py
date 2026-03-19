from math import exp


def softmax(scores: list[float]) -> list[float]:
    all_class_prob = sum((exp(score) for score in scores))
    return [round(exp(score) / all_class_prob, 4) for score in scores]