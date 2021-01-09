num_1 = int(input('Type the number: \n'))
num_2 = int(input('Type the number2: \n'))

print('#### OPERATIONS      ####')
print('#### 1. Addition     ####')
print('#### 2. Divition     ####')
print('#### 3. Substraction ####')
print('#### 4. Multiplication ####')

print('#### RANDOM CHANGE ####')

print('#### RANDOM CHANGE 2 ####')


operation = int(input('Choose an operation: \n'))


if operation == 1:
    # Clear terminal
    print(chr(27) + "[2J")
    print('### ADDITION ###')
    print ('the operation result is: \n')
    result = num_1 + num_2
    if result == 420 : 
        print(f'Happy {result}')
    else: 
        print (result)
elif operation == 2:
    # Clear terminal
    print(chr(27) + "[2J")
    print('### DIVITION ###')
    print ('the operation result is: \n')
    result = num_1 / num_2
    if result == 420 : 
        print(f'Happy {result}')
    else: 
        print (result)
elif operation == 3:
    # Clear terminal
    print(chr(27) + "[2J")
    print('### SUBSTRACTION ###')
    print ('the operation result is: \n')
    result = num_1 - num_2
    if result == 420 : 
        print(f'Happy {result}')
    else: 
        print (result)
elif operation == 4:
    # Clear terminal
    print(chr(27) + "[2J")
    print('### MULTIPLICATION ###')
    print ('the operation result is: \n')
    result = num_1 * num_2
    if result == 420 : 
        print(f'Happy {result}')
    else: 
        print (result)