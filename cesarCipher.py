n = int(raw_input())
s = raw_input()
k = int(raw_input())
r = ""
for i in range(n):
  car = s[i]
  if car.isalpha():
    inicio = ord('A')
    if car.islower():
      inicio = ord('a')    
    car =  chr(inicio + ( ord(car) - inicio + k) % 26)
  r+=car
print r