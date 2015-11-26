s1 =  raw_input().split(' ')
X = int(s1[0])
Y = int(s1[1])
C = int(s1[2])
x = min(X,Y)
y = max(X,Y)

if X+Y<C:
    print( "Impossible" )
elif X<C:
    print( str(X)+" "+str(C-X) )
else:
    print( "0 "+str(C) )
