score = 95
if score >= 60:
    print("及格")
    if score >= 90:
        print("領獎")
else:
    print("考試不及格")
    if score >= 40:
        print("補考")
    else:
        print("重修")
print("分數:",score)        
