# Asking for inputs using below function to give output
def main():
    t = int(input())
    problems = []
    for i in range(t):
        problems.append(list(map(int, input().split())))
    print(solve(problems))


# Defining a function to analyse if question is to be answered
def solve(matrix):
    n = 0
    for array in matrix:
        i = 0
        for j in range(len(array)):
            if array[j] == 1:
                i += 1
                if i == 2:
                    n += 1
                    break
            else:
                continue
    return n



if __name__ == "__main__":
    main()