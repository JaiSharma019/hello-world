# Taking multiple inputs and implementing in below made function
def main():
    t = int(input())
    n = []
    a = []
    for i in range(t):
        n.append(int(input()))
        a.append(list(map(int, input().split())))
    for i in range(len(a)):
        print(maximum(a[i]))

# Defining a function such that gives the last and the maximum side possible
def maximum(array):
    max_side = array[0]
    while len(array) != 1:
        array.append(array[0]+array[1]-1)
        del array[0:2]
        max_side = array[0]
    return max_side


if __name__ == "__main__":
    main()