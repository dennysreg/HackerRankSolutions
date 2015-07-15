#from datetime import date
cur_d, cur_m, cur_y = map(int, raw_input().split())
#cur_date = datetime(y, m, d)
d, m, y = map(int, raw_input().split())
#exp_date = datetime.date(y,m, d)
fine = 0
if cur_y > y:
  fine = 10000
elif cur_y == y and cur_m > m:
  fine = 500 * (cur_m - m)
elif cur_y == y and cur_m == m and cur_d > d:
  fine = 15 * (cur_d - d)
print fine
