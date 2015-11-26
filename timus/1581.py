import sys


N = int(raw_input())

last = -1
num = 0
s =  raw_input().split(' ')
for i in range(0,N):
    K = int(s[i])
    if last==K:
        num += 1
    else:
        if last !=-1:
            sys.stdout.write(str(num)+" "+str(last)+" ")
        last = K
        num = 1

sys.stdout.write(str(num)+" "+str(last)+"\n")
