# List - ordered mutable collection (sequence) of objects of different types

a = []

#   -6 -5   -4   -3         -2         -1
#    0  1   2     3         4         5
a = [1, 2, 3.0, 'hello', {1, 2, 3}, {'key': 12}]

# 0-indexing, zero-index
print(a[0])
print(a[2])

print(len(a))

i = 3 + 3
if i < len(a):
    print(a[i])

print(a[-1])
print(a[-2])
# print(a[-12])

# print('After error')

b = [1, 2, 3]

# 1. Add new elements

b.append('hello')
print(b)

b.insert(0, True)
print(b)
print(b[0])

b.insert(100, True)
print(b)

c = ['a', 'b']
b.append(c)
print(b)

b.extend(c)
print(b)

# 2. Delete elements from list

b.pop(0)
print(b)

b.pop(-1)
print(b)

b.pop(len(b) - 1)
print(b)

i = 100
if i < len(b):
    b.pop(i)
print(b)

b.remove(3)
print(b)

if 3 in b:
    b.remove(3)
print(b)

d = [3, 4, 4, 3, 3, 3]
d.remove(3)
d.remove(3)
print(d)

del b[0:3]  # slicing
print(b)

# 3. Edit existing elements

b[1] = 'Bye-bye'
print(b)

# len(b) -> length of collection
# if 3 in b -> check if element exist in list
# index(3) -> index of element
# a + b -> concatenation
# for i in a: -> loops

d = [3, 4, 4, 3, 3, 3]
print(d.index(3))

a = [1, 3]
b = ['v', 'a']

c = a + b
print(c)

a.extend(b)
print(a)


d = [3, 4, 5, 6, 7, 8]

#   i~loop variable d~iterable
# for run in runs:
for i in d:  # head of loop
    print(i)

    if i % 2 != 0 and i != 7:
        print('Skipping', i)
        continue

    if i == 7:
        print('OMG it is ', 7)
        break

    print(i**2)         # v body of loop

a = [
    [1, 2, 3, 5, 7],
    [4, 5, 6],
    [7, 8, 9]
]
print(a[1][2])
