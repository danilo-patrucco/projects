'''
Danilo Patrucco
1INF103 601HY Section 01
HW0, Jan 29, 2017
'''
#Exercise 10
#Ver. 1.0
'''
When user input the amount of cookies they want the program
calculate the amount of ingredients needed
-
ask for how many cookies the user want to prepare
'''
cookies = input('How many cookies you want to prepare')
cookies = float (cookies)
'''
Calculate the amount of ingredient needed in cups.
The formula used is x1 : x2 = x3 : x4, where i know three variables
X1 is the amount of flour/sugar/butter needed for 48 cookies
X2 is 48 cookies
X3 is my unknown value
X4 is the amount of cookies i want to bake
the formula end up being X3 = X4 * X1 / X2
'''
sugar = (cookies) * 1.5 / 48
butter = (cookies) * 1 / 48
flour = (cookies) * 2.75 / 48
print (' Here is the ingredient quantity in cups')
print ('Sugar:')
print (sugar)
print ('Butter:')
print (butter)
print ('Flour:')
print (flour)
'''
program run correctly no errors
'''
