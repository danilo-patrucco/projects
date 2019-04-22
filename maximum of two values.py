#inf 103
#danilo patrucco
#maximum of two values

def main ():
    tt = input ('input value 1 ')
    tt2 = input ('input value 2 ')
    if max(tt,tt2):
        print('this is the greater value 1',tt)
    else:
        print('this is the greater value 2',tt2)
        
def max (t1,t2):
    if t1 > t2:
        return True

main ()

