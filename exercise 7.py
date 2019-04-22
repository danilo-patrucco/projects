'''
Danilo Patrucco
INF103 601HY Section 01
HW0, Jan 25, 2017
'''
#Exercise 7
#Ver. 1.0
'''
Calculate MPG using miles and Gallons data from user
'''
miles = 0
gallongs = 0
mpg = 0
'''
Set the starting point of all variables 
'''
miles = input('How many miles did one full tank allowed you to run your car?')
gallons = input('How many gallons your tank can hold')
'''
the variables are entered at this point but they are set as a string, so when
deviding them i will have to convert them to float.
The reason why i use float is becuase it will allow me to devide float numbers
'''
print('These are the MPG of your car')
mpg = (float(miles) / float(gallons))
print(mpg)
'''
program run correctly no errors
'''
