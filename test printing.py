inFile = open ('data_sample.txt','r')
for Line in inFile :
    value = str(Line)
    print (value)
    #firstLine = inFile.readline()
    #fLineStripped = firstLine.strip('\n') # stirp remove leading an trailing edges
    #print (fLineStripped)

inFile.close()
