#INF103
#Danilo Patrucco
#mary little lamb

def main():
    #ask for the DB name
    database = str(input('Type the database name without extension: '))
    #add the extension
    database += '.txt'
    #intialize variable used as counter
    line_nr = 1
    #verify that the database name is the same as the one created
    if database == 'mary.txt':
        #open the DB
        inFile = open (database,'r')
        Line = ''
        mary = ''
        outfile = ''
        #ask user to input the output file name
        outfile_name = str(input ('Type the target database name without extension: '))
        outfile_name += '.txt'
        #create a loop to read all the lines and number them
        for Line in inFile:
            #create a new variable and make it a string that will contain
            #the line number as a string
            line_nr_str = str(line_nr)
            #create a list (i cheated here) to add together all the fields
            mary = ['/* ',line_nr_str,' */',' ',Line]
            #turn the list into a string
            mary = ''.join(mary)
            #open the outfile and load the string of data
            outfile = open(outfile_name,'a')
            outfile.write(str(mary))
            #increase the counter 
            line_nr += 1
            #close the out file
            outfile.close()
        #close the input file
        inFile.close()
        
        

main()
                   
