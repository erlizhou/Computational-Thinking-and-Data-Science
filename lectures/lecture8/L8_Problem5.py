import itertools
def genPset(Items):
    n = len(Items)
    for i in range(n + 1):
        for item in itertools.combinations(Items, i):
            yield list(item)

test = genPset([1, 2, 3])
for n in test:
	print n