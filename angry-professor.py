# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for _ in range(n):
    n,k = map(int, raw_input().split())
    arrived_time = [int(x) for x in  raw_input().split()]    
    ok_time = len([x for x in arrived_time if x <=0])    
    print 'YES' if ok_time < k else 'NO'