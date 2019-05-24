# function for transforming list into dict


from operator import attrgetter
from operator import itemgetter
from collections import defaultdict


def list2dict(flattened):
    assert len(flattened) % 2 == 0, \
        'Input must be list of key value pairs'
    unflattened = dict()
    for i in range(0, len(flattened), 2):
        key, value = flattened[i], flattened[i+1]
        unflattened[key] = value
    return unflattened


names = ['banana', 0.86, 'bok choy', 1.56,
         'cantaloupe', 0.63, 'orange', 0.7, 'coconuts', 1.06]


names1 = ['banana', 0.86, 'bok choy', 1.56,
          'cantaloupe', 0.63, 'orange', 0.7, 'coconuts']

# print(list2dict(names1))


# max in list of strings

nums = ["12", "7", "30", "14", "3"]


def max_by_int_values(items):
    biggest = items[0]
    for item in items[1:]:
        if int(item) > int(biggest):
            biggest = item
    return biggest


# print(max_by_int_values(nums))

# list of dicts

student_joe = {'gpa': 3.7, 'major': 'physics',
               'name': 'Joe Smith'}
student_jane = {'gpa': 3.8, 'major': 'chemistry',
                'name': 'Jane Jones'}
student_zoe = {'gpa': 3.4, 'major': 'literature',
               'name': 'Zoe Fox'}
students = [student_joe, student_jane, student_zoe]


def max_by_gpa(items):
    biggest = items[0]
    for item in items[1:]:
        if item['gpa'] > biggest['gpa']:
            biggest = item
    return biggest


# print(max_by_gpa(students))

# combined

def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest


def get_gpa(who):
    return who['gpa']


# print(max_by_key(students, get_gpa))
# print(sorted(students, key=get_gpa))

# itemgetter does the same function as get_gpa but it's dynamic and can accept other key fields
# print(sorted(students, key=itemgetter('gpa')))

student_rows = [
    ("Joe Smith", "physics", 3.7),
    ("Jane Jones", "chemistry", 3.8),
    ("Zoe Fox", "literature", 3.4),
]

# print(max(student_rows, key=itemgetter(2)))
# print(sorted(student_rows, key=itemgetter(1)))


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return f'{self.name}: {self.gpa}'


student_obj = [
    Student("Joe Smith", "physics", 3.7),
    Student("Jane Jones", "chemistry", 3.8),
    Student("Zoe Fox", "literature", 3.4)
]

# attrgetter is useful for when the sequence elements are instances of your own class
print(sorted(student_obj, key=attrgetter('gpa')))
