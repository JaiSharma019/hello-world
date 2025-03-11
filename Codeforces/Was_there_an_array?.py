def main():
    n = int(input())
    list_to_check = list(map(int, input().split()))
    print(check(list_to_check, n))

def check(list_to_check, n):
    num = 0
    new_list = [1]*(n+2)
    while num != n+1:
        for b in list_to_check:
            if b == 1:
                new_list[num+1] = new_list[num]
                num += 1
                new_list[num+2] = new_list[num]
                num += 1
