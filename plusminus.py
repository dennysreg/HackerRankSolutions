from __future__ import division

n = int(raw_input())
array = [int(x) for x in raw_input().split()]
positivos = len([x for x in array if x > 0])
negativos = len([x for x in array if x < 0])
zeros = n - positivos - negativos
fp =  positivos/n
fn = negativos/n
fz = zeros/n
print "%.3f\n%.3f\n%.3f" %  (fp,fn,fz)