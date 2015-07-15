# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for _ in range(n):
    cycles = int(raw_input())
    k = cycles / 2
    m = 1 if cycles % 2 == 0 else 2
    print 2**(k+m) - m
    