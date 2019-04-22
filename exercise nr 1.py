#INF103
#danilo patrucco
#exercise nr 1

class pet :
    #constructor ; it is instantly executed
    def __init__(self,name,animal_type,age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    #class method (setters)
    def set_name (self,name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animla_type
    def set_age(self, age):
        self.__age = age

    #class methods (getter)

    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age (self):
        return self.__age
    
        
        
        
