def average_score(scores) -> float:
    if not scores:
        return 0.0

    scores_sum = sum(scores)
    scores_count = len(scores)
    average_film_score = (scores_sum / scores_count)
    average_film_score_usual = round(average_film_score, 1)
    return average_film_score_usual
