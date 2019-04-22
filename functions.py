'''
# in the parenthesys there are the parameters
# function need to be written first and then called

def addition (num1,num2):
    total=num1+num2
    print (total)
t1 = int(input ('t1=?'))
t2 = int(input ('t2=?'))

addition(t1,t2)

# when calling the function inside of the parenthesys there are the arguments

def multiplication (x,y):
    total = x*y
    return total
ml=multiplication (8,2)
print (ml)


#first example is void return variable second is return variable. First does 
#not return any value the second one return a value to the program that ran it.
'''

def isEven(n):
    if n%2 == 0 :
        #print ('number is even')
        return True
#    else:
#       #print ('number is odd')
#       return False
#   return

num = int(input ('number'))
if isEven (num):
    print('even')
else:
    print('odd')

# def can be used as true or false statement


