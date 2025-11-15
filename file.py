f=open("demo.txt","r")
data=f.read(5)
print(data)
print(type(data))


#readline
line1=f.readline()
print(line1)

#write a file
f=open("demo.txt","w")
data=f.write("hello world") #overwrite the entire file
f.close()

#append a file
f=open("demo.txt","a")
 
f.write("\nthen i'll move to reactjs")
f.close()

#
f=open("demo.txt","r+")
#f.write("abc")
print(f.read())
f.close()

#w+
f=open("demo.txt","w+")
print(f.read())
f.write("abc")
f.close() 

#with Syntax
with open("demo.txt","r") as f:
    data=f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("new data entered")

#deleting a file
#import os

#os.remove("demo.txt")