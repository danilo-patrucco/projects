'''
Danilo Patrucco
1INF103 601HY Section 01
HW0, Jan 29, 2017
'''
#Exercise 8
#Ver. 1.0
'''
Calculate total cost of lunch/dinner, the 7% tax value, 18% tip and total
-
Set the starting value of all variables 
'''
appetizer = 0
fdish = 0
entree = 0
dessert = 0
drinks = 0
total = 0
totalwtax = 0
totalwtip = 0
'''
Ask to input all the variables value
'''
appetizer = input('How much you spent for the appetizer ?')
fdish = input('How much you spent for the first dish ?')
entree = input('How much you spent for the entree ?')
dessert = input('How much you spent for the dessert ?')
drinks = input('How much you spent for the drinks ?')
'''
start with the calculation of the total cost of the dinner/lunch
'''
print('This is the cost of your dinner w/o taxes and tip')
total = (float(appetizer)+ float(fdish) + float(entree) + float(dessert)
         + float(drinks))
print(total)
'''
calculate the taxes amount
'''
print ('This is the amount of taxes you are going to pay on the total')
totalwtax = ( float(total)*(0.07))
print (totalwtax)
'''
calculate the tip amount over the cost of the dinner/lunch + the taxes
'''
print('This is the amount of tip you are going to pay on the total + taxes')
totalwtip = (float ((totalwtax)+(total))*(0.18))
print (totalwtip)
'''
calculate the amount in total, dinner/lunch + tax + tip
to simplify the value is converted from float to int in order
to show an int number
'''
print ('This is the total amount of the check')
total = ((total)+(totalwtip)+(totalwtax))
print (total)
print ('This is the round down value')
print (int(total))
'''
program run correctly no errors
'''


