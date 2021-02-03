def generate_combos(arrs, i):
    if i+1 == len(arrs):
        return [[x] for x in arrs[i]]
    return [[x] + y for x in arrs[i] for y in generate_combos(arrs, i+1)]

def maximize(m, arrs):
    mx = 0
    for combo in generate_combos(arrs, 0):
        s = sum([x**2 for x in combo])%m
        mx = s if s > mx else mx
    print(mx)

if __name__ == "__main__":
    inp = input().split()
    n = int(inp[0])
    m = int(inp[1])
    arrs = []
    for _ in range(n):
        arrs.append(list(map(int, input().split()[1:])))
    maximize(m, arrs)
