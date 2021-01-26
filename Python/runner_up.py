if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mx = -101
    second = -101
    for x in arr:
        if x > mx:
            second = mx
            mx = x
        elif x > second and x != mx:
            second = x
    if second == -101:
        second = mx
    print(second)
