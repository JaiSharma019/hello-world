t = int(input())
good = []

for m in range(t):
    length = int(input())
    if length%2 == 0:
        arr = [-1, 2]
        n = int((length/2))-1
        for i in range(n):
            arr = [-1, 1] + arr
    else:
        arr = [-1, 3, -1]
        n = int((length/2))-1
        for j in range(n):
            arr = [-1, 1] + arr
    good.append(arr)

for a in good:
    print(*a, sep=" ")

