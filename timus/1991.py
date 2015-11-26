s1 =  raw_input().split(' ')
N = int(s1[0])
K = int(s1[1])

L = 0
R = 0

i = 0
s2 =  raw_input().split(' ')
while ( i < N ):
    a = int(s2[i])
    if a <= K:
        R += a
    else:
        R += K
        L += (a-K)
#        print( " == " + str(a-K))
    i += 1
print( str(L) + " " + str(N*K-R))
