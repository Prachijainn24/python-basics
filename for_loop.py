nums=[1,2,3,4,5] #list
for val in nums:
    print(val) 

tup=("hii","this ","is","a","python","code") #TUPLES

for nums in tup:
        print(nums)

str="forloop"

for char in str:
      if(char=='o'):
            print("o found")
            break
      print(char)
else:
      print("end")

#q print the elements of the following list using a loop
list=[1,4,9,16,25,36,49,64,81,100]

for num in list:
      print(num)

#q2 search for a number x in the following tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100)
x = 49

idx = 0
for num in tup:
    if num == x:
        print("found at index", idx)
    idx += 1

#range
seq=range(5)
print(seq[0])
print(seq[1])

seq=range(4)

for i in seq:
      print(i)

for i in range(2,5): #range(start,stop)
    print(i)

for i in range(2,5,1):
     print(i)

#odd numbers
for i in range(1,100,2):
     print(i)

#multiplication of n
n=int(input("enter the number"))
for i in range(1,11):
        print(n*i)

#pass in python for loop 
for i in range(5):
     pass #empty

print("some useful work")