# Returns verdict on division
def main():
    weight = int(input())
    print(watermelon(weight))


# Analysing the division of watermelon
def watermelon(w):
    if (w%2) == 0 and w != 2:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    main()