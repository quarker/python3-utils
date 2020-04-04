# ~1 == flip all bits (i.e. 0 to 1 and 1 to 0) == ~(0001) == 1110 == representation of (-2) in computer
# because computer uses two's complement to represent signed integers
# two's complement of 2 == ~(0010) + 1 == 1101 + 1 == 1110

s = [x for x in range(10)]
ns = []
for i in range(10):
    ns.append(s[~i])

assert ns == s[::-1]    # reverse s
