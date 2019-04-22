#INF103
#danilo patrucco
#exe 1 call class

from exercise_nr_1 import *

name = input ('Enter pet name:')
animal_type = input ('Enter animal type:')
age = input ('enter animal age:')
#instanciate

myPet = pet(name,animal_type,age)
myFavouritePet = pet ('Frank','Cat','4')

print(myPet.get_name())
print(myPet.get_animal_type())
print(myPet.get_age())

myPet.set_name('Norma')
print(myPet.get_name())
print(name)
print (myFavouritePet.get_name())
#print(myPet.__name)

