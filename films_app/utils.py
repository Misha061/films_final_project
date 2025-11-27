def average_score(scores:list) -> float:
    if not scores:
        return 0

    scores_sum = sum(scores)
    scores_count = len(scores)
    average_film_score = scores_sum / scores_count
    return average_film_score