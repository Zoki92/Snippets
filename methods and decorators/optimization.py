"""
Check if items are in list
"""


def has_invalid_fields(fields):
    for field in fields:
        if field not in ['foo', 'bar']:
            return True
    return False


def has_invalid_fields2(fields):
    return bool(set(fields) - set(['foo', 'bar']))


""" set eliminates duplicates """


""" Code is valid but it will a variation of the example
many times """


def add_animal_in_family(species, animal, family):
    if family not in species:
        species[family] = set()
    species[family].add(animal)


species = {}
add_animal_in_family(species, 'cat', 'felidea')

# import collections


def add_animal_in_family2(species, animal, family):
    species[family].add(animal)


species = collections.defaultdict(set)
add_animal_in_family2(species, 'cat', 'felidea')

""" Each time you try try to access a nonexistent item from 
your dict the defaultdict will use the function that was 
passed as argument to its constructor to build a new 
value instead of raising a KeyError. In this case the
set() function is used to build a new set each time we
need it.
"""


# Ordered list and bisect

""" Sorted lists use a bisecting algorithm for lookup 
to achieve a retrieve time of O(logn). The idea is to split
the list in half and look on which side, left or right, the 
item must appear in and so which side should be searched next.
We need to import bisect
"""


farm = sorted(['haystack', 'needle', 'cow', 'pig'])
bisect.bisect(farm, 'needle')


""" bisect.bisect() returns the position where an element
should be inserted to keep the list sorted. Only works if
the list is properly sorted to begin with.
Using bisect module you could also create a special SortedList
class inheriting from list to create a list that is always 
sorted,"""


class SortedList(list):
    def __init__(self, iterable):
        super(SortedList, self).__init__(sorted(iterable))

    def insort(self, item):
        bisect.insort(self, item)

    def extend(self, other):
        for item in other:
            self.insort(item)

    @staticmethod
    def append(o):
        raise RuntimeError("Cannot append to a sorted list")

    def index(self, value, start=None, stop=None):
        place = bisect.bisect_left(self[start:stop], value)
        if start:
            place += start
        end = stop or len(self)
        if place < end and self[place] == value:
            return place
        raise ValueError(f'{value} is not in list')


""" In python regular objects store all of their attributes inside
a dictionary and this dictionary is itself store in the __dict__
attribute """


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
p.__dict__

"""  {'y': 2, 'x': 1} 
Instead we can use __slots__ that will turn this dictionary into
list, the idea is that dictionaries are expensive for memory but
lists are less, only works for classes that inherit from object, 
or when we have large number of simple objects
"""


class Foobar(object):
    __slots__ = ('x',)

    def __init__(self, x):
        self.x = x


""" However this limits us to them being immutable. Rather than 
having to reference them by index, namedtuple provides the ability to
retrieve tuple elements by referencing a named attribute.

import collections 
Foobar = collections.namedtuple('Foodbar', [x])
Foobar(42)

Foobar(42).x
42


Its a little bit less efficient than __slots__ but gives
the ability to inde by name
"""


# Memoization


""" Its an optimization technique used to speed up function 
calls by caching their results. The results of a function 
can be cached only if the function is pure. 
functools module provides a least recently used LRU cache
decorator. This provides the same functionality as memoization
but with the benefit that it limits the number of entries in the cache
removing the least recently used one when the cache reaches its 
maximum size. Also provides statistics.>>> import functools
>>> import math
>>> @functools.lru_cache(maxsize=2)
... def memoized_sin(x):
...     return math.sin(x)
...
>>> memoized_sin(2)
0.9092974268256817
>>> memoized_sin.cache_info()
CacheInfo(hits=0, misses=1, maxsize=2, currsize=1)
>>> memoized_sin(2)
0.9092974268256817
>>> memoized_sin.cache_info()
CacheInfo(hits=1, misses=1, maxsize=2, currsize=1)
>>> memoized_sin(3)
0.1411200080598672
>>> memoized_sin.cache_info()
CacheInfo(hits=1, misses=2, maxsize=2, currsize=2)
>>> memoized_sin(4)
-0.7568024953079282
>>> memoized_sin.cache_info()

"""
