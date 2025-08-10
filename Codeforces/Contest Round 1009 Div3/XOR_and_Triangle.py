# Taking multiple inputs and analysing in below functions
def main():
    t = int(input())
    x_list = []
    for i in range(t):
        x_list.append(int(input()))
    for x in x_list:
        print(check(x))
    


# Defining a function such that checks there exists required "y"
def check(x):
    y = 0
    for i in range(x):
        if x + i > (x^i) and x + (x^i) > i and (x^i) + i > x:
            y = i
        else:
            continue
    if y == 0:
        return -1
    else:
        return y
        



if __name__ == "__main__":
    main()