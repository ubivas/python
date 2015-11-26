N = int(raw_input())

lst = {}
for i in range(0,N):
    s =  raw_input()
    if s in lst:
        lst[s] += 1
    else:
        lst[s] = 1
#inverse = [(value, key) for key, value in lst.items()]
#print max(inverse)[1]
#print max(lst, key=lst.get)
print max(lst, key=lambda k: lst[k])

