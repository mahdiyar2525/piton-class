x = int(input('enter the number'))

for i in range(x):
    z = int(input('enter the score'))

    if 20>=z>=10:
        print('T')
    
    else:
        if z>20:
            print('INCORRECT')
        else:
            print('F')
            