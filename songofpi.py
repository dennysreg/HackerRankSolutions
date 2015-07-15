t = int(raw_input())
pi = "31415926535897932384626433833"
for _ in range(t):
  songLengths = "".join([str(len(x)) for x in raw_input().split()])  
  n = len(songLengths)
  if songLengths == pi[:n]:
    print "It's a pi song."
  else:
    print "It's not a pi song."
