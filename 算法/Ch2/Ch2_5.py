scores = [87,66,90,65,70]
score_sum = 0
count = len(scores)
score_max = scores[0]
score_min = scores[0]
scores.sort()
total = sum(scores)
print(f"sum:{sum(scores)}")
print(f"avg:{total/count:.2f}")
print(f"max:{scores[-1]}")
print(f"min:{scores[0]}")
