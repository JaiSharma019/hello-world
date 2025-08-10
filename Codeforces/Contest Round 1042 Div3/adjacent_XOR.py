t = int(input())
arr = []

for i in range(t):
    n = int(input())
    a_line = input().split()
    b_line = input().split()

    a_arr = [int(a) for a in a_line]
    b_arr = [int(b) for b in b_line]

    for j in range(n):
        if (a_arr[j]^a_arr[j+1] == b_arr[j]) and a_arr[j] != b_arr[j]:
            a_arr[j] = b_arr[j]
    if a_arr == b_arr:
        arr.append("YES")
    else:
        arr.append("NO")