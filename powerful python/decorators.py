# def printlog(func):
#     def wrapper(arg):
#         print(f'CALLING: {func.__name__}')
#         return func(arg)
#     return wrapper


# @printlog
# def foo(x):
#     print(x+2)


# foo(3)
# @printlog
# def baz(x, y):
#     return x**y

# won't execute because wrapper only takes 1 positional argument


# def printlog(func):
#     def wrapper(*args, **kwargs):
#         print(f'Calling: {func.__name__}')
#         return func(*args, **kwargs)
#     return wrapper


# @printlog
# def baz(x, y):
#     return x ** y


# print(baz(2, 3))

# Prototypical form of Python decorators

def prototype_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def running_average(func):
    data = {"total": 0, "count": 0}

    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("Average of {} so far: {:.01f}".format(
            func.__name__, data['total'] / data['count']
        ))
        return func(*args, **kwargs)
    return wrapper


@running_average
def foo(x):
    return x + 2


@running_average
def bar(x):
    return x * 10

# decorator that allows us to peak into accumulated data


def collectstatic(func):
    data = {"total": 0, "count": 0}

    def wrapper(*args, **kwargs):
        val = func(*args, **kwargs)
        data["total"] += val
        data["count"] += 1
        print("Average of {} so far: {:.01f}".format(
            func.__name__, data['total'] / data['count']
        ))
        return func(*args, **kwargs)
    wrapper.data = data
    return wrapper

# decorator that counts how many times a function has been called


def countcalls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'# of calls: {count}')
        return func(*args, **kwargs)
    return wrapper


"""count += 1 is modifying the value of the count variable itself, and whenever you modify instead of read
   a variable that was created in a larger score Python requires you to declare that's what you want, 
   with global or nonlocal. data["count"] += 1 is not actually modifying data, or rather is not modifying 
   the variable named data, which points to a dictionary object. Instead the statement invokes a method on
   the data object. This does change the state of the dictionary but it doesn't make data point to a different
   dictioanary. count += 1 makes count point to a different integer, so we use nonlocal there. 
"""


# Decorators that take arguments
def add(increment):
    def decorator(func):
        def wrapper(n):
            return func(n) + increment
        return wrapper
    return decorator
