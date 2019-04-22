#INF103
#Danilo Patrucco
#read, write, append
'''
test = open ('data_sample.txt','r')
file_content = str(test.readline())
test.close()
print = (file_content)
'''

inFile = open ('data_sample.txt','r')
firstLine = inFile.readline()
fLineStripped = firstLine.strip('\n') # stirp remove leading an trailing edges
inFile.close()
print (fLineStripped)
inFile = open ('write_sample.txt','a')
#write overwrite the file completely
#append it does append
test1 = input('give me a number:')
inFile.write(str(test1)+ '\n')
#cannot use comma in write, only the concatenation
inFile.close()



