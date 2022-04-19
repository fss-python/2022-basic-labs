# Variable Scopes - Области видимости

a = 10

names = ['Tom', 'Peter', 'Slava']

for name in names:
    print('Hello, ' + name + '! Welcome to club!')
    print(', '.join(['Hello', name]))
    print('Hello, ***. You are !!!'.replace('***', name).replace('!!!', str(19)))

    age = 19
    print(f'Hello, {name}! Welcome to club! You are {str(age)}')
    print(f'Hello, {name}! Welcome to club! You are {age}')
    print('Hello, {name}! Welcome to club!')

print('-----' * 3)


# LEGB
# Scopes are:
# local - локальная - тело и аргументы функции
# enclosing - объемлющая - когда функция внутри функции
# global - глобальная - область видимости модуля
# builtin - встроенная

def say_hello():
    global name
    name = 'Peter'
    print(f'Hello, {name}')


name = 'Tom'
say_hello()

print(name)
