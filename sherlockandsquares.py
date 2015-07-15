import math
t = int(raw_input())
sq_a=0
sq_b=0
for _ in range(t):
  a,b = map(int, raw_input().split())  
  sq_b = math.floor(pow(b,0.5))
  sq_a = math.ceil(pow(a,0.5))
  n =  sq_b - sq_a + 1  
  print "%d" % n