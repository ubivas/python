import math
import sys

def IsOne( i ):
    a = int(math.sqrt(i))
    if ((a*(a+1))==i):
        return 1
    else:
        return 0

N = int(raw_input())
i = 0
for i in range (0,N):
    K = int(raw_input())
    if (IsOne(2*(K-1))==1):
        sys.stdout.write("1")
    else:
        sys.stdout.write( "0" )

    if (i==N-1):
        sys.stdout.write( "\n" )
    else:
        sys.stdout.write( " "  )
