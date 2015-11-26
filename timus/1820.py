s =  raw_input().split(' ')
N = int(s[0])
K = int(s[1])

if N == 1 or (N*2+K-1)<2*K:
    print ( 2 )
else:
    print ( (N*2+K-1)/K )

