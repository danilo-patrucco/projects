#INF103
#Danilo Patrucco
#USPres

def main ():
    #initialize variables
    lowpres = 0
    highpres = 0
    #request input of lower range and higher range value
    lowpres = int ( input ('Insert the lower range: \t'))
    highpres = int (input ('insert the higher range: \t'))
    #verify the values if they are correctly used.
    #if the lower is higher than the higher or they pass 0 and/or 45 it
    #gives an error
    if lowpres < 0 or lowpres > 45 or highpres < 0 or highpres > 45 or lowpres > highpres:
        #if the values are not right then return error and close the program
        print ('Invalid Value used')
    else:
        #otherwise it will run a function
        presrange (lowpres,highpres)

# Function
def presrange (i1,i2):
    #open the database file
    inFile = open ('USPres.txt','r')
    #set up a counter to calculate the president number
    datanum = 1
    #start a loop in python
    for Line in inFile:
        #assign the string to a variable
        prezname = str(Line)
        #use if statement to verify if intialized counter varibale is
        #lower or higher then the lower and higher range
        if datanum >= i1 and datanum <= i2:
            #intialization of variable that will contain the name of database created
            #to write info into it
            outfile = ''
            #set up the destination DB and use append and not write to add info
            outfile = open ('PresidentOut.txt','a')
            #clear the info read from the start database from \n if in the beginning and in the end
            prezname = prezname.strip('\n')
            #write the president name in the db and add \n
            outfile.write(str(prezname)+'\n')
            #close the text file.
            outfile.close()
        #increase the counter to terminate correctly the if statement
        datanum = datanum + 1
    #close the DB from where it was reading info
    inFile.close()
    
#run main
main ()
