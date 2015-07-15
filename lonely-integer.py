def lonelyinteger(a):
    answer = 0    
    freq = {}
    for i in a:
        if i not in freq:            
            freq[i] = 1
        else:
            freq[i] = freq[i] + 1
    
    for key, value in freq.iteritems():
        if value == 1:
            return key

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)