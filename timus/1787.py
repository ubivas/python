s =  raw_input().split(' ')
K = int(s[0])
N = int(s[1])

s =  raw_input().split(' ')
S = 0
for i in range (0,N):
    a = int(s[i])
    S += a
    S -= K
    if ( S < 0 ):
        S = 0

print ( S )
