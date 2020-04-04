from collections import defaultdict

d = defaultdict(lambda: defaultdict(int))
assert d[0] == {}
assert d == {0: {}}

assert d[0][0] == 0
assert d == {0: {0: 0}}
