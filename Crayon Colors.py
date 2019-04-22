#INF103
#Danilo Patrucco
#Crayon Colors

def main ():
    #open the DB with the crayola colors
    inFile = open ('ShortColors.txt','r')
    #create a loop to read every single record
    for Line in inFile:
        #assign the string to a variable
        colors = str(Line)
        #assign the lenght of every record to a variable
        col_len= len(colors)
        #if the lenght is more than 6 is not going to write it in the new file
        if col_len <= 6:
              #create the outfile varibale that is going to contain the result db
              #content
              outfile = ''
              #assign a name to the result DB
              outfile = open('crayola_out.txt','a')
              #write the records that are 6 digit long or less in new db
              outfile.write(str(colors))
              #close out file
              outfile.close()
    #close origin DB
    inFile.close()
              
main ()

            
        
