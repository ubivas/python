N = int(raw_input())
s =  raw_input().split(' ')
A = []
for i in range (0,N):
    A.append(int(s[i]))
M = A[0]+A[1]+A[2]
m = M
I = 2
for i in range (3,N):
    m -= A[i-3]
    m += A[i]
    if ( m > M ):
        M = m
        I = i

print( str(M) + " " + str(I) )
