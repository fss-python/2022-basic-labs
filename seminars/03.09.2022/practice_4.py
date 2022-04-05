a = []
a = [1, 2, 3, []]

a[2]

a[-1]

a.append(2)

c = [2]
a.extend([2])

a.extend(c)

a.insert(0, 2)

print(a)

idx_to_remove = 7
if idx_to_remove < len(a):
    a.pop(0)
else:
    print('Unable to remove element by index', idx_to_remove)

print(a)

for i in a:

    if i == 3:
        print('break on 3')
        break

    if i == 2:
        print('continue on 2')
        continue

    print('Element is: ', i)

for i in a:

    if i == 3:
        print('break on 3')
        break

    if i == 2:
        print('continue on 2')
        continue

    print('Element is: ', i)


def print_hello_x_times(times, name):  # declaration of function
    print(times)
    print(name)


print('Before function')
hello_quantity = 6
print_hello_x_times(hello_quantity, 'Tim')  # call of function
print('After function')


def sum_two_numbers(a, b):
    res = a + b
    print('In sum_two_numbers', res)
    return res


result = sum_two_numbers(10, 20)

print(result)


def count_even_numbers(numbers):
    print('In count_even_numbers', numbers)

    count_even = 0
    for element in numbers:
        if element % 2 == 0:
            count_even = count_even + 1  # count_even += 1

    return count_even


a = [1, 2, 3, 4, 5, 6, 7, 8]
res = count_even_numbers(a)
print(res)  # 4
