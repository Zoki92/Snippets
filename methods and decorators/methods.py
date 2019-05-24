# Static method


import abc


class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x+y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)


""" Static methods can be overridden in subclasses. If instead of a static method
we use a mix_ingredients() function defined at the top level of our module, a class
inheriting from Piza wouldn't be able to change the way we mix ingredients for our
pizza without overriding the cook() method itself. With static methods,
the subclasses can override the method for their own purposes.
"""

# Class methods

""" They are bound to a class rather than its instances. That means that those
methods cannot the state of the object but only the state and methods of the
class. They are useful for creatingfactory methods which instantiate objects
using a different signature than __init__
"""


def Pizza1(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())


""" If we used @staticmethod here instead of a @classmethod, we wouldhave to hardcode the Pizza
class name in our method making any class inheriting from Pizza unable to use our factory
for its own purposes. In this case however we provide a from_fridge() factory method that
we can pass a Fridge object to. Any time you write a method that cares only about the class
of the object and not about the object's state, it shold be declared as a class method
"""


# Abstract methods

""" An abstract method is defined in an abstract base class that may 
not itself provide any implementation. Whne a class has an abstract
method, it cannot be instantiated. As a consequence, an abstract
class(defined as a class that has at least one abstract method) must
be used as a parent class by another class. This subclass will be in
charge of implementing the abstract method, making it possible to 
instantiate the parent class.
"""


class Pizza3(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError


""" Won't raise error until you instantiate the class and call the method
"""


class BasePizza(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_radius(self):
        """ Method should do something """


# super()
""" Multiple inheritances are used in many places, particularly in 
code invling a mixin pattern. A mixin is a class that inherits from 
two or more other classes, combining their features.
Super() is a constructor and you instantiate a super object everytime
time you call it. It takes either one or two arguments, the first argument
is a class and the second optional argument is either a subclass or an
instance of the firs argument. 
"""
