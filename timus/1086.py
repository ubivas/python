A = {}

def IsSimple( i ):
    n = 1
    while (A[n]*A[n]) <= i:
        if ( i % A[n] ) == 0:
            return 0
        n += 1
    return 1

N = int(raw_input())

A[1] = 2
j = 2
i = 1
while j <= 15000:
    i += 2
    while not IsSimple(i):
        i += 2
    A[j] = i
    j += 1
    
for i in range (0,N):
    K = int(raw_input())
    print( A[K] )
