#inf 103
#danilo patrucco
# Math Quiz
import random

def main():
    in1 = random.randint(1,300)
    in2 = random.randint(1,300)
    intot = in1 + in2
    print (in1,"+",in2)
    inanswer = int ( input ("insert result of sum of the values displayed above \t"))
    compare(intot,inanswer)
    
                            

def compare(v1,v2):
    if v1 == v2 :
        print ("Good answer!")
    else :
        print ("Wrong Answer!")
    
main()
