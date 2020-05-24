"""
https://docs.python.org/3/library/bisect.html

bisect.bisect_left(a, x, lo=0, hi=len(a))
    Locate the insertion point for x in a to maintain sorted order.
    If x is already present in a, the insertion point will be before (to the left of) any existing entries.

bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x, lo=0, hi=len(a))
    Similar to bisect_left(), but returns an insertion point which comes after (to the right of) any existing entries of x in a.
"""
from bisect import bisect


def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]


ans = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(ans)





def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
