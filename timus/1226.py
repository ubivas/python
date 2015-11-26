import sys
for line in sys.stdin:
    i = 0
    S = ""
    while i < len(line):
        s = ""
        while ( (i < len(line)) and line[i].isalpha() ):
            s = line[i] + s
            i += 1
        S += s
        while ( (i < len(line) ) and not line[i].isalpha() ):
            S += line[i]
            i += 1
    sys.stdout.write(S)
