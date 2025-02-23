from itertools import combinations
from itertools import permutations
comb = combinations([1,2,3,4,5,6],3)
perm = permutations([1,2,3,4])
for i in list(comb):
    print(i)
print("===================")
for v in perm:
    print(v)
