for i in range(int(input())):
    s = input()
    for j in range(len(s)):
        if s[j : j + 3] == "кот":
            print(i + 1, j + 1)
            break
