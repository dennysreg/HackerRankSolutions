n = int(raw_input())
for _ in range(n):
  h,m,sx = raw_input().split(':')
  h = int(h)
  m = int(m)
  s = int(sx[:2])
  mer = sx[-2:]
  if mer == "PM" and h < 12:
    h = h+12
  elif mer == "AM" and h == 12:
    h = 0

  print "%02d:%02d:%02d"%(h,m,s)
