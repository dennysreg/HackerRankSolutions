string = raw_input()
 
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
criba = [0]*26
first_letter = ord('a')
for car in string:
  criba[ord(car)-first_letter]+=1 
letras_impares = len([odd for odd in criba if odd%2!=0])
found = (letras_impares == 0 or letras_impares == 1)
print found

