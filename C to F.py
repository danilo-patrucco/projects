#danilo Patrucco
#inf 103
#c to f table
#set variables
celsius = 0
#set max temp as final value
maxtemp = 21
#test = 1
#while celsius is different than maxtemp then loop
#while test == 1:
while celsius != maxtemp:
        #compute the temperature
    fahrenheit = format((9/5)*celsius+32,'.2f')
    print (celsius,'\t',fahrenheit)
    celsius = celsius + 1
    #test = int(input('test Value'))
    #if test != 1:
        #celsius = 0
#print (celsius)
