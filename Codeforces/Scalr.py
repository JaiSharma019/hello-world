Radius = []
def main():
    t = int(input())
    for _ in range(t):
        R = int(input())
        Radius.append(R)
    for r in Radius:
        print(volume(r))

def volume(r):
    pi = 22/7
    vol = 4*pi*(r**3)/3
    return round(vol, 2)

main()