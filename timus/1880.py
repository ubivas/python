A = {}
for n in range (0,3):
    N = int(raw_input())
    s =  raw_input().split(' ')
    for i in range (0,N):
        K = int(s[i])
        if K in A:
            A[K] += 1
        else:
            A[K] = 1
R = 0
for i in A:
    if A[i] == 3:
        R += 1

print ( R )
