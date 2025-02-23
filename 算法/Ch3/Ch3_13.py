count = 0
c = 65
print(chr(c),chr(c+1))
for i in range(0,5):
    for j in range(0,5):
        if j == i:
            continue
        for k in range(0,5):
            if k == j or k == i:
                continue
            for l in range(0,5):
                if l == k or l ==j or l == i:
                    continue
                for m in range(0,5):
                    if m == l or m ==k or m == j or m ==i:
                        continue
                    count+=1
                    print(f"{count}:{chr(c+i)},{chr(c+j)},{chr(c+k)},{chr(c+l)},{chr(c+m)}")
