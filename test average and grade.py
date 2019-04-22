#INF 103
#Danilo PAtrucco
#Test Average and Grade

def calc_average ():
    #grab all variables for grades
        tg1 = int(input (" What was your score for test nr.1"))
        tg2 = int(input (" What was your score for test nr.2"))
        tg3 = int(input (" What was your score for test nr.3"))
        tg4 = int(input (" What was your score for test nr.4"))
        tg5 = int(input (" What was your score for test nr.5"))
#return the value to a variable
        return ((tg1+tg2+tg3+tg4+tg5)/5)

def determine_grade (i0):
    #condition to return the right grade depending on the total of the grades
    if i0 >= 90:
        return "A"
    elif i0 >= 80 and i0 <=89:
        return "B"
    elif i0 >= 70 and i0 <=79:
        return "C"
    elif i0 >= 60 and i0 <=69:
        return "D"
    elif i0 >= 0 and i0 <=59:
        return "F"

def main ():
    #set up initial value of variable that will be filled with
    #the average value of the grades
    var1 = 0
    #Assign to variable the average value
    var1 = calc_average ()
    #verify if the insertion of the grade was correct
    if var1 >= 101:
            #print error because the grade were inserted incorrectly
            print ("One or multiple grades were inserted incorrectly")
    
    else:
            #print grade with definition
            print("Your average grade is >>>\t",determine_grade (var1))

main ()
