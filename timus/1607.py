str =  raw_input().split(' ')
a = int(str[0])
b = int(str[1])
c = int(str[2])
d = int(str[3])

x = a
y = c

while ( x < y ):
    x += b
    if ( x > y ):
        x = y
    if ( y-d > x ):
        y -= d
    else:
        y = x
        break

print( x )

