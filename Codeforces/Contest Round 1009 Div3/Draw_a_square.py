# Taking inputs and analysing it using below made function
def main():
    t = int(input())
    points = []
    for i in range(t):
        points.append(list(map(int, input().split())))
    for point in points:
        print(square(point))


# Defining a function that checks if it's a square
def square(coordinates):
    if len(set(coordinates)) == 1:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    main()