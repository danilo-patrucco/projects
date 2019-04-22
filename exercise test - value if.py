'''
Danilo Patrucco
1INF103 601HY Section 01
HW0, Jan 29, 2017
'''
#Exercise C to F with temp control
'''
Set the variables to 0.0 (float)
in future comment C will mean Celsius and F Farhenheit
'''
celsius = float(0)
fahrenheit = float(0)
celsius = input('Please input the Celsius degrees to conver to Fahrenheit:')
'''
apply the conversion formula from C to F keeping the type as float
'''
fahrenheit = float(celsius)*9/5+32
print ('This is your Fahrenheit Temperature :')
'''
display the F value
'''
print(fahrenheit)

if fahrenheit > 80:
    print ('heath warning')
elif fahrenheit < 60:
    print('cover yourself')
else:
    print ('Good Temperature')
