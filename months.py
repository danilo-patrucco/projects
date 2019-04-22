#INF103
#Danilo Patrucco
#exercise 1
#Months

def main ():
    inFile = ''
    #location = str(input('Write file location'))
    inFile = open ('SomeMonths.txt', 'r')
    for Line in inFile :
        month = str(Line)
        if 'r' in Line or :
            outfile = ''
            outfile = open ('OutputMonth.txt','w')
            Line = Line.strip('\n')
            outfile.write(str(Line)+ '\n')
            outfile.close()
    inFile.close()
            
main()

