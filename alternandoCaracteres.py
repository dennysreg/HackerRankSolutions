t = int(raw_input())
for _ in range(t):
    borrados = 0
    s = [ord(car) for car in raw_input()]
    n = len(s)
    i = 0
    j = 1
    while j < n:
        if s[j]-s[i]!=0:
            i = j
            j = j + 1
        else:
            borrados += 1
            j= j + 1
    print borrados