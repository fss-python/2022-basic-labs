print('Hello, World!')
a = 12
b = [1, 2, 3]

# b.len
# def # function declaration

len(b)

print(len)  # Error, declaration (def etc.)
print(len(b))  # 3


# Task 1
# Implement a function that returns a mean of
# values in the list of numbers

def calculate_average_of_numbers(numbers):
    average = 0
    for number in numbers:
        average = average + number
    return average / len(numbers)


c = [1, 2, 3, 4]
print(calculate_average_of_numbers(c))

average_result = calculate_average_of_numbers(c)
print(average_result)


# Task 2
# Implement a function that accepts a list and
# returns a new list
# that does not contain duplicates

def find_unique_elements(elements):
    unique_elements = []
    for i in elements:
        if i not in unique_elements:
            unique_elements.append(i)
    return unique_elements


next_list = [1, 2, 1, 2, 3, 4, 5]
result = find_unique_elements(next_list)
print(result)


def find_maximum(numbers):
    maximum = 0
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


elements = [1, 2, 3, 2, -1]
max_value = find_maximum(elements)
print(max_value)

# Strings - ordered immutable sequence of symbols for storing
# text information

a = 'Hello, World!'
a = "Hello, World!"
a = '''Hello, World!'''
a = """Hello, World!"""
a = """Hello, World!"""

a = 'Tom\'s cat'
a = "Tom's cat"
a = 'C:\\Users\\demidovs\\Downloads\\archive'
a = r'C:\Users\demidovs\Downloads\archive'

a = "Tom said: \"I want to buy coffee\""
a = 'Tom said: "I want to buy coffee"'

a = """Tom's cat said: "MEOW" """

a = str(10)  # "10"

# SOME COMMENT

a = """
print(10)
print(None)
print(10)
print(10)
"""

a = 'abcd'
print(a[1])
print(a[-1])

print(a[1:])  # bcd

# mutability?
# concatenation -> joining lists together

# lists - sequences
# ordered -> get by index
# len
# in
# iterable -> for loop

# strings - sequences
# ordered -> get by index
# len
# in
# iterable -> for loop

a = 'abcd'
a[0]  # 'a'

len(a)  # 4

if 'e' in a:
    print('e is in a')
else:
    print('e is not in a')

print(a.index('a'))

if 'y' in a:
    print(a.index('y'))

a = 'abc' + 'def'

print(a)

a = '*!&' * 3

print(a)

a = "Reding"

b = a[0] + a[1] + 'a' + a[2:]
print(a)

res = ''.join([a[0], a[1], 'a', a[2:]])
print(res)

res = ''.join([a[0], str(100), 'a', a[2:]])
print(res)

a = """
123
346
345
567
578
"""

lines = a.split('\n')
print(lines)

numbers = []
# lines: ['', '123', '346', '345', '567', '578', '']
for line in lines:
    if line == '':
        continue
    numbers.append(int(line))
print(numbers)
