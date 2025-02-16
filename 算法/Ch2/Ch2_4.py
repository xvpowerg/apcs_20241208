scores = [87,66,90,65,70]
score_sum = 0
count = len(scores)
score_max = scores[0]
score_min = scores[0]
for i in range(count):
    s = scores[i]
    print(f"第{i + 1}學生的分數{s}")
    score_sum += s
    if score_max < s:
        score_max = s
    if score_min > s:
        score_min = s
print("======================")
print(f"總分:{score_sum}")
print(f"平均:{score_sum/count:.2f}")
print(f"Max:{score_max}")
print(f"Min:{score_min}")
