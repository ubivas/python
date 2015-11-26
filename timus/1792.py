import sys

def GetBit( v, bit ):
    return (v>>(4-bit))&1;
    
def IfOneBit( v ):
    if (v&(v-1)) == 0:
        return 1
    else:
        return 0

def Print7LastBits( n ):
    for i in range (0,7):
        sys.stdout.write( str( (n>>(6-i) ) & 1 ) )
        if ( i < 6 ):
            sys.stdout.write( " " )
        else:
            sys.stdout.write( "\n" )

        
#S = "0 1 0 1 1 0 1"
#s =  S.split(' ')
s =  raw_input().split(' ')
A = 0

for i in range (0,7):
    A = ( A << 1) | ( int(s[i]) )

B = []
for i in range (0,16):
    B.append(i)
for i in range (0,16):
    B[i] = (B[i]<<3) | ((GetBit(B[i],2)^GetBit(B[i],3)^GetBit(B[i],4))<<2) | ((GetBit(B[i],1)^GetBit(B[i],3)^GetBit(B[i],4))<<1) | ((GetBit(B[i],1)^GetBit(B[i],2)^GetBit(B[i],4)))
#    Print7LastBits( B[i] )

for i in range (0,16):
    if ( A==B[i] ):
        Print7LastBits( A )
        break
    if IfOneBit ( A ^ B[i] ):
        Print7LastBits( B[i] )
        break
