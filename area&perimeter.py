import os

def header():
    print(f'========={'WELCOME':^40}=============')

def inputUser():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))

    return length,width

def calcArea(length,width):
    area = length*width
    return area

def calcPerimeter(length,width):
    perimeter = 2*(length+width)
    return perimeter

while True:
    os.system('cls')
    header()
    print('1.Calculate Area\n2.Calculate Perimeter')
    choices = int(input('Choose: '))
    length,width = inputUser()
    if choices == 1:
      area = calcArea(length,width)
      print(f'Area: {area}')
    elif choices == 2:
      perimeter = calcPerimeter(length,width)
      print(f'Perimeter: {perimeter}')
    else:
       print('not available')

    isDone = input('Do you want to stop?(Y/N): ')
    if isDone == 'Y':
       print('=='*16+'\nThank you for using this system!\n'+'=='*16)
       break

    


   
    
    


