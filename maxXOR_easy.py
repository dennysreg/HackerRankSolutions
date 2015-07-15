import math

# Complete the function below.


def  maxXor( l,  r):  
  
  b = bin(0b1111111111)
  diff = l ^ r
  x = int(math.trunc(math.log(diff)/math.log(2))) + 1
  return int('1'*x, 2)
  

  
    
_n = int(raw_input());
for _ in range(_n):
  _l = int(raw_input());


  _r = int(raw_input());

  res = maxXor(_l, _r);
  print(res)