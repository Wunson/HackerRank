if __name__ == '__main__':
    grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls = grades.get(score, [])
        ls.append(name)
        grades[score] = ls
    key = list(sorted(grades.keys()))[1]
    for name in sorted(grades[key]):
        print(name)

