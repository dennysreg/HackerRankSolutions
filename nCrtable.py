
#precalcula triangulo de pascal
n = 1001
triangulo = [[]]*n

triangulo[0]=[1]
triangulo[1]=[1, 1]
#print triangulo
for i in range(2,n):
  k = i - 1
  j = len(triangulo[k]) - 1
  row = [1]
  for x in range(j):
      next_value = triangulo[k][x] + triangulo[k][x+1]
      row += [ next_value % 1000000000]
  row +=[1]
  triangulo[i]=row

t = int(raw_input())
for _ in range(t):
  n = int(raw_input())
  print " ".join(str(x) for x in triangulo[n])
