import sys

N = int(raw_input())

A = []
B = []
sum = 0.0
exc = 0.0
s =  raw_input().split(' ')
for i in range(0,N):
    A.append(int(s[i]))
    sum += A[i]
portion = sum / (N+1)
#sys.stdout.write("\n== "+str(portion)+"\n")
for i in range(0,N):
    b = A[i] - portion
    if b < 0:
        b = 0
    B.append(b)
    exc += b
for i in range(0,N):
    res = int(0.0000000001+(100*B[i])/exc)
    if i == N-1:
        sys.stdout.write(str(res)+"\n")
    else:
        sys.stdout.write(str(res)+" ")
