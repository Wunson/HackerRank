def merge_the_tools(string, k):
    i = 0
    while i < len(string):
        out = ""
        for _ in range(k):   
            char = string[i]
            if char not in out:
                out = out + char
            i += 1
        print(out)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)