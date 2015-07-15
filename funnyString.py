# Enter your code here. Read input from STDIN. Print output to STDOUT
def esPalindromo(s):
    n = len(s)
    middle = n/2
    for i in range(middle):        
        if s[i]!=s[n-i-1]:
            return False
    return True
    
t = int(raw_input())
for _ in range(t):
    s = raw_input()
    n = len(s)    
    ascii = [ord(x) for x in s]    
    numbers = [abs(ascii[i+1] - ascii[i]) for i in range(0,n-1)]
    if esPalindromo(numbers):
        print "Funny"
    else:
        print "Not Funny"