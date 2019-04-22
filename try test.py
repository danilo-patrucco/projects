#inf 103
#danilo Patrucco
#try test



try:
    #inFile = open ('somefile.txt')
    number = 5/0
    print (number)
except FileNotFoundError:
    print ('file does not exist')
except ZeroDivisionError:
    print('you cannot devide by zero')
          

