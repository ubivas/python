s =  raw_input().split(' ')
N = int(s[0])
K = int(s[1])

if N == 1:
    print( 0 )
else:
    i = 1
    j = 0
    while ( i < N ):
        if i < K:
            i *= 2
            j += 1
        else:
            j += ((N-i)+(K-1))/K
            break
    print( j )

