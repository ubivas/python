import sys

N = int(raw_input())

mx = -1
num = 0
s =  raw_input().split(' ')
for i in range(0,N):
    K = int(s[i])
    if K > mx:
        mx = K
    num += K
num += mx

sys.stdout.write(str(num)+"\n")
