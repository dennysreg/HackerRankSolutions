n = int(raw_input())
#matrix = []
d1 = 0
d2 = 0
for i in range(n):
  row = [int(x) for x in raw_input().split()]  
  d1 += row[i]
  d2 += row[n-i-1]  
  #matrix.append(row)
#print matrix, d1,d2, abs(d1-d2)
print abs(d1-d2)

