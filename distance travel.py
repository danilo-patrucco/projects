#danilo patrucco
#inf103
##4. distance traveled

#get user input
speed = int ( input ('what is the speed of the vehicle?'))
time = int ( input ('how many hours have you travelled ?'))

#intialize years

starttime = 1

print ('Hour \t Distance Traveled')

while starttime <= time:
    dtravel = speed * starttime
    print ( starttime, '\t',dtravel)
    starttime = starttime + 1
    #the final value of the starttime will be always different to accept the
    #boolean formula
