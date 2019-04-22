#inf 103
#danilo patrucco
#even or odd
import random

def randomnum(i1):
    i1 = int(random.randint(1,1000))
    print (i1)
    if (i1 % 2) == 0:
        return True
    else:
        return False

def main ():
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    for var2 in range (var2,100):
        if randomnum(var1) == True:
            var3 += 1
        else:
            var4 += 1             
    print ("odd numbers counted:",var3)
    print ("even numbers counted:",var4)
          
main ()

