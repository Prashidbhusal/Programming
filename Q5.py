p=64
for i in range(4):
    p += 1
    for j in range(i+1):
        print(chr(p), end =" ")
    print()