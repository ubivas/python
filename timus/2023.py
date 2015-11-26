import sys

N = int(raw_input())

d = {   "A": 1, "P": 1, "O": 1, "R": 1, 
        "B": 2, "M": 2, "S": 2 };

last = 1
num = 0
for i in range(0,N):
    s =  raw_input()
    L = s[0]
    if L in d:
        next = d[L]
    else:
        next = 3

    if ( next > last ):
        num += next - last
    else:
        num += last - next
        
    last = next

sys.stdout.write(str(num)+"\n")
