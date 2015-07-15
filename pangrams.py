# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
criba = [0]*26
first_letter = ord('a')
for car in s.lower():
  if car.isalpha():
    index = ord(car)-first_letter    
    criba[index]=1

if sum(criba)==26:
    print "pangram"
else:
    print "not pangram"
