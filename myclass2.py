#myclass 2

class MyClass:
    # two underscore in the back and two in the front means that
    #the function is special
    def __init__(self,message):
        #two underscores before the variable means that is not supposed to be
        #accessed outside the program
        self.__message = message
    def foo(self):
        return self.__message
        
