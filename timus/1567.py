def Presses( c ):
    if c <= ord('z') and c >= ord('a'):
    	return 1+((c-ord('a'))%3)
    if c == ord(','):
    	return 2
    if c == ord('!'):
    	return 3
    return 1

s =  raw_input()
i = 0
N = 0
while i < len(s):
	N += Presses(ord(s[i]))
	i += 1

print( N )
