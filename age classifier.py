#danilo patrucco
#jan 13
#age classifier

age = int(input('insert age of the user'))

if age <= 1 and age >= 0:
    print ('You are an infant, this is madness')
elif age > 1 and age < 13:
    print ('you are a child, stop playing')
elif age >= 13 and age < 20:
    print ('You are a teenager')
elif age >= 20:
    print ('you are an adult, go ahead')
else:
    print ('go home you are drunk')



