import sys

n = []
for line in sys.stdin:
   for word in line.split(' '):
      n.append(int(word))

print( n[0]*n[1]*n[2]*2)