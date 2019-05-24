import functools
"""
A decorator is a function that takes another functionas an argument and
replaces it with a new, modified function. 
The primary use case for decorators is in factoring common code that needs
to be called before, after, or around multpiple
functios. 
"""


class Store(object):
    def get_food(self, username, food):
        if username != 'admin':
            raise Exception('This user is not allowed to get food')
        return self.storage.get(food)

    def put_food(self, username, food):
        if username != 'admin':
            raise Exception("This user is not allowed to put food")
        self.storage.put(food)


""" Now instead of having a method that we call everytime we need to check
    when the user is admin we can use decorators
"""


def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowd to put food")
        return f(*args, **kwargs)
    return wrapper


""" Now the decorated class will look """


class StoreDecorated(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)


# Stacking decorators

def check_user_is_not(username):
    def user_check_decorator(f):
        def wrapper(*args, **kwargs):
            if kwargs.get('username') == username:
                raise Exception("This user is not allowed to get food")
            return f(*args, **kwargs)
        return wrapper
    return user_check_decorator


class StoreStacked(object):
    @check_user_is_not('admin')
    @check_user_is_not("user123")
    def get_food(self, username, food):
        return self.storage.get(food)


""" Here check_user_is_not() is a factory function for the decorator
user_check_decorator(). It creates a function decorator that depends on
the username variable and then returns that variable.
The decorator list is applied from top to bottom so the decorators closest
to the def keyword will be applied first and executed last. In the example
above the program willl check for admin first and then for user123.
"""


# Class decorators

""" Class decorators are often used for wrapiing a function that's storing
a state. The following example wraps the print() function to check how 
many times it has been called in a session
"""


class CountCalls(object):
    def __init__(self, f):
        self.f = f
        self.called = 0

    def __call__(self, *args, **kwargs):
        self.called += 1
        return self.f(*args, **kwargs)


@CountCalls
def print_hello():
    print("Hello")


print(print_hello.called)
print_hello()
print(print_hello.called)

""" Decorators replace the original function with a new one built on the fly. 
However, this new function lacks many of the attributes of the original
 function, such as its docstring and its name. 
This can be fixed with functools.update_wrapper()
"""


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper


class Store2(object):
    @check_is_admin
    def get_food(self, username, food):
        """ Get food from storage. """
        return self.storage.get(food)


#
