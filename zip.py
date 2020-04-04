x = [1, 2, 3]
y = [4, 5, 6]

assert list(zip(x, y)) == [(1, 4), (2, 5), (3, 6)]

z = zip(x, y)
x1, y1 = zip(*z)    # x1 and y1 are tuples
assert list(x1) == x
assert list(y1) == y

m = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

x, y, z = zip(*m)
assert list(x) == [1, 4, 7]
assert list(y) == [2, 5, 6]
assert list(z) == [7, 8, 9]