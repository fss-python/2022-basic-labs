

def print_hello_x_times(times, name):
    print(times)
    print(name)
hello_quanitity = 6
print_hello_x_times(hello_quanitity, 'Tim')

def sum_two_numbers(a, b):
    print(a + b)
    return a+b
result = sum_two_numbers(18, 20)
print(result)

#Функция, которая считает количество четных чисел внутри списка
def count_even_numbers (numbers):
    print('In count_even_numbers', numbers)
    even = 0
    for i in numbers:
         if i % 2 != 0:
            continue
         else:
            even = even + 1
    return even

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = count_even_numbers(a)
print(res)

def find_average(numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    res = sum / len(numbers)
    return res


c = [1, 2, 3, 4]


result = find_average(c)
print(result)











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

upd_list = [1, 2, 1, 2, 3, 4, 5]
max = find_maximum(upd_list)
print(max)



ms=[0]
    rr=[0]
    ecg_rr=[]
    for i in range(len(maximums)):
        if maximums[i] == 1:
            ms.append(times[i])
    for i in range(len(ms)):
        rr.append(ms[i]-ms[i-1])
        for i in range(len(rr)):
            if rr[i] > 400:
                ecg_rr.append(rr[i])

    return ecg_rr

