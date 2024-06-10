N = int(input())
li = []

for a in range(10) :
    for b in range(10) :
        for c in range(10) :
            for d in range(10) :
                for e in range(10) :
                    for f in range(10) :
                        for g in range(10) :
                            if ( 1000001 *a +100001 *b +10001 * c + 1001 * d + 101 *e + 11 * f + 2 * g) == N :
                                li.append( 1000000 *a +100000 *b +10000 * c + 1000 * d + 100 *e + 10 * f + g) 
if li:
    print(min(li))
else:
    print(0)