K = int(raw_input())

if ( K == 1 or K == 0 ):
    print("1")
elif ( K > 1):
    print((K+1)*K/2)
else:
    print((-K+1)*K/2 + 1)
