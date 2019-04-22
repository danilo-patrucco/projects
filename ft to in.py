#inf 103
#danilo patrucco
#feet to inches

def main():
    value = float (input ('insert the value of feet'))
    print('this is the inches value',format(feet_to_inches(value),'.2f'))
                  
def feet_to_inches (feet):
    inches = feet * 12
    return inches
                  
main()
