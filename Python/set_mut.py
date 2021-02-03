def read_num_set():
    return set([int(i) for i in input().split()])

if __name__ == '__main__':
    input()
    sett = read_num_set()
    n = int(input().strip())
    for _ in range(n):
        opp = input().split()[0]
        mordekaiser = read_num_set()
        if opp == "update":
            sett.update(mordekaiser)
        elif opp == "intersection_update":
            sett. intersection_update(mordekaiser)
        elif opp == "symmetric_difference_update":
            sett.symmetric_difference_update(mordekaiser)
        elif opp == "difference_update":
            sett.difference_update(mordekaiser)
    print(sum(sett))