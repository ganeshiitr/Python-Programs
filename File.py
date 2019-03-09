#Open File in writing mode , + means create if not exist
f=open("sample.txt","w+")
#write content in file
for i in range(10):
  f.write("line no: " + str(i+1)+"\n")
#close file before end 
f.close()
