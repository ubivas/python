s =  raw_input().split(' ')
N = int(s[0])
K = int(s[1])

if (N*K)%2 == 0:
    print ( "[:=[first]" )
else:
    print ( "[second]=:]" )

