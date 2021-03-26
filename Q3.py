p=65
for i in range(4,0,-1):
    for j in range(i):
        print(chr(p), end = " ")
        p +=1
    print()