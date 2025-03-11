# Takes input in a loop for t testcases
def main():
    t = int(input())
    long_words = []
    for i in range(t):
        long_words.append(input())
    for long_word in long_words:
        print(abbreviation(long_word))


# Function which makes abbreviation
def abbreviation(word):
    letters = list(word)
    if len(letters) > 10:
        return f"{letters[0]}"+f"{len(letters)-2}"+f"{letters[-1]}"
    else:
        return word


if __name__ == "__main__":
    main()