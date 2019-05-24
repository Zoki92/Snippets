# Pure functions


""" Regular non-pure function """


def remove_last_item(mylist):
    mylist.pop(-1)


""" Pure """


def butlast(mylist):
    return mylist[:-1]


""" Advantages
Modularity:
Writing with a functional style forces a certain degree
of separation in solving your individual problems and makes
 sections of code easier to resuse in other context. Since
 the function doesn't depend on any external variable or state
 calling it from a different piece of code is straightforward
Brevity:
Its often less verbose than other paradigms
Concurrency:
Purely functional functions are thread-safe and can run
concurrently. Some functonal languages do this automatically,
which can be  abig help if you ever need to scale your
application, but its not quite the case yet with Python
Testability:
Testing a functional program is easy, all you need is
 a set of inputs and an expected set of outputs. They are
 idempotent meaning that calling the same function over and
 over with the same arguments will always return the same result.


"""


def shorten(string_list):
    length = len(string_list[0])
    for s in string_list:
        length = yield s[:length]


mystringlist = ['loremipsum', 'dolorsit', 'ametfoobar']
shortstringlist = shorten(mystringlist)

result = []
try:
    s = next(shortstringlist)
    result.append(s)
    while True:
        number_of_vowels = len(list(filter(
            lambda letter: letter in 'aeiou', s)))
        s = shortstringlist.send(number_of_vowels)
        result.append(s)
except StopIteration:
    pass


# print(result)

""" The length of each truncated string is equal to the number
of vowels in the previous string. A yield statement also can
return a value in the same way as a function call. This allows
us to pass a value toa a generator by calling its send() method.
To inspect if a function is a generator use
inspect.isgeneratorfunction()
"""

# Map

""" map() takes the form map(function, iterable) and applies
function to each item in iterable to return a iterable
"""

map(lambda x: x + "bzz!", ["I think", "I'm good"])
(x + "bzz!" for x in ["I think", "I'm good"])

# Filter

""" The filter() takes the form filter(function or None, iterable)
and filters the items in iterable based on the result returned
by the function.
Returns an iterable
"""
filter(lambda x: x.startswith("I"), ["I think", "I'm good"])
[x for x in ["I think", "I'm good"] if x.startswith("I")]


# first function
""" from first import first, however it's not built in python"""
first([-1, 0, 1, 2], key=lambda x: x > 0)
