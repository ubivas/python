N = int(raw_input())

if N < 5:
    print("few")
elif N <=9:
    print("several")
elif N <=19:
    print("pack")
elif N <=49:
    print("lots")
elif N <=99:
    print("horde")
elif N <=249:
    print("throng")
elif N <=499:
    print("swarm")
elif N <=999:
    print("zounds")
else:
    print("legion")

