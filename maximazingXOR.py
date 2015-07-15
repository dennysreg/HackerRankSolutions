import math

# Complete the function below.


def  maxXor( l,  r):
  cte = int(0b1111111111)
  a = l  
  b = bin(~a & cte)
  x = int(math.trunc(math.log(r)/math.log(2)))
  s = b[-x : ]
  n = int(s,2)
  n2 = n | int('1'+'0'*x,2) 
  result = n  
  if n2 <= r:
    result = n2
  print l,r,a,b,x,s,bin(n),bin(n2), result

  if result >=l and result <= r:
    return a^result 
  else:
    return 0

  
    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)