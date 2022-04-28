import pathlib

x = 10


def f():
    global x
    x = 30


# print(x)
f()
# print(x)

# File System

# C:\Users\админ\PycharmProjects\2022-basic-labs\seminars\04.26.2022\test.txt
# /usr/local/bin/test.txt
# /Users/Admin/Documents/test.txt
file_to_open = 'C:\\Users\\админ\\PycharmProjects\\2022-basic-labs\\seminars\\04.26.2022\\test.txt'
file_to_open = r'C:\Users\админ\PycharmProjects\2022-basic-labs\seminars\04.26.2022\test.txt'  # raw
with open(file_to_open) as my_file:  # context manager
    res = my_file.read()
    print(res)

file_to_open = pathlib.Path('../../..') / 'test.txt'  # raw, str(1), list('abc')
file_to_open = pathlib.Path(file_to_open) / 'test.txt'  # raw, str(1), list('abc')
file_to_open = pathlib.Path(__file__).parent / 'test.txt'  # raw, str(1), list('abc')
print(pathlib.Path(__file__))
print(file_to_open.resolve())

with open(file_to_open) as my_file:  # context manager
    res = my_file.read()
    print(res)

project_root_path = pathlib.Path(__file__).parent.parent.parent
project_root_path = pathlib.Path(r'C:\Users\админ\PycharmProjects\2022-basic-labs')
print(project_root_path)
test_rrs_path = project_root_path / 'lab_1' / 'tests' / 'test_data' / 'test_rrs.txt'
print(test_rrs_path)

with open(test_rrs_path) as my_file:  # context manager
    res = my_file.read()
print(res)

file_to_open = pathlib.Path(__file__).parent / 'new_test.txt'
print(file_to_open)

a = [
    'Hello, Peter',
    'Hello, Sam',
    'Hello, John',
]
content = ''
for index, item in enumerate(a):
    content += item
    if index < len(a):
        content += '\n'

content = '\n'.join(a)

with open(file_to_open, 'w') as my_file:  # context manager
    my_file.write(content)

file = open(file_to_open)
file.read()
file.close()
