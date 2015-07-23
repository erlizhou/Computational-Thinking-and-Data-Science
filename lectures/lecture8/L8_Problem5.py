import itertools
def genPset(Items):
    n = len(Items)
    for r in xrange(n+1):
        for item in itertools.combinations(Items, r):
            yield list(item)

test = genPset([1, 2, 3])
for n in test:
	print n