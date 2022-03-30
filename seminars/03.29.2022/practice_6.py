print(None == None)
print(None is None)

print(float('-inf'))

x = 10
if float('-inf') < float(x) < float('inf'):
    print('is number')

print(float('nan') == float('nan'))

print(float('nan'))

print(float(3))

# dictionary - mutable unordered collection of elements with access via a key
# dictionary - mutable associative array
# dictionary - mutable mapping from keys to values

d = {}

a = 'keys'

d = {a: [1, 2, 3], 'age': 19, 'name': 'Tom', 120: 560, None: '', True: '', False: ''}
print(d)

months = {
    1: 'January',
    2: 'February',
}
print(months[1])
print(d['age'])
print(d['keys'][1])

d = dict(name='Tom', age=19)
print(d)

if 'height' in d:
    print(d['height'])
else:
    print('No such a key')

# 1. Add new elements
d['height'] = 180
print(d)

student = {
    'group': 'FSS-2022',
    'university': 'UNN',
    'height': 200
}

d.update(student)
print(d)

# 2. Edit existing elements
d['height'] = 190
print(d)

d['height2'] = 290
print(d)

# 3. Delete elements
del d['height2']
print(d)

res = d.pop('group')
print(res)
print(d)

d = dict(name='Tom', age=19)
for key in d:  # ~ for key in d.keys():
    print(key, d[key])  # Tom name (name, Tom)
    # 19  age  (age, 19)

for key in d.keys():
    print(key, d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

keys = []
for key in d.keys():
    keys.append(key)
print(keys)

print(list(d.keys()))

a = [
    "http://abc.com/1.jpg",
    "http://abc.com/2.jpg",
    "http://abc.com/3.jpg",
    "http://abc.com/4.jpg",
]

import random

print(random.choice(a))

tom_list = ['Tom', 19, 200]

tom_list[2]
tom_dict = {'name': 'Tom', 'age': 19, 'height': 200}
tom_dict['height']


# Task 1. Implement a function that accepts a dict and returns a quantity of pairs
def collect_elements_quantity(dictionary: dict):
    return len(list(dictionary.keys()))


tom_dict = {'name': 'Tom', 'age': 19, 'height': 200}
print(collect_elements_quantity(tom_dict))


# Task 2. Implement a function that accepts two lists and returns dict with keys from
# the first and values from the second
# [Tom, Mary, John]
# [19, 21, 18]
# {Tom: 19, Mary: 21, John: 18}
def join_to_dict(list_keys, list_values):
    result = {}
    for index_key in range(len(list_keys)):
        a = list_keys[index_key]
        b = list_values[index_key]
        result[a] = b
    return result


print(join_to_dict(['Tom', 'Mary', 'John'], [19, 21, 18]))
