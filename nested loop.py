#danilo Patrucco
#inf103
#c2f
repeat = 'y'

while repeat != 'n':  
    celTemp = int(input('Celsius from 0 to ... '))
    print('Celsius \t Fahrenheit')
    #for loop
    for celsius in range(celTemp+1):
        fahrenheit = (9/5)*celsius +32
        print (celsius,'\t\t',fahrenheit)
#remember the indentation to be able to loop it
    repeat = input('repeat pgm? y or n : ')
