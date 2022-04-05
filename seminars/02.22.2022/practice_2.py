a = 2  # int - integer number
b = 2.3  # float - floating point number
print(a)
print(b)

a = int('2')  # cast/casting
b = float('2.5')
print(a, b)

print('Arithmetical operations')
print(a * b)
print(a + b)
print(a - b)
print((a - b) ** 3)

print('Division')
print(a / b)
print(type(a / b))
print(a // b)
print(type(int(a / b)))
print(5 % 2)  # modulo

if 0 != 0:  # False/True
    print('Even number')
elif 5 > 2:
    print('a is bigger than b')
elif 5 > 2 * 2:
    print('a is bigger than twice b')
else:
    print('Some strange behavior')

print('Something next...')

a = '9'
if type(a) == int:
    print('Is int')
else:
    print('Not int!!')
    print('It is ', type(a))
