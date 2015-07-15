# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
for _ in range(t):
    s = raw_input()
    middle = len(s)/2
    acum = 0
    for i in range(middle):
        j = i + 1
        l1 = ord(s[i])
        l2 = ord(s[-j])
        #print s, s[i], s[-j]
        acum = acum + abs(l1 - l2)
    print acum