t = int(input())
iterations = []

for k in range(t):
    n = int(input())
    a_line = input().split()
    b_line = input().split()

    a_arr = [int(a) for a in a_line]
    b_arr = [int(b) for b in b_line]
    iteration = 0
    for i in range(n):
        if a_arr[i] > b_arr[i]:
            iteration += (a_arr[i]-b_arr[i])
    iterations.append(iteration+1)

for n in iterations:
    print(n)