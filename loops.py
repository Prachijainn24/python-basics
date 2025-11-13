count=1
while(count<=5):
    print("hello")
    count+=1
#reverse print
    i=5
    while(i<=1):
        i-=1
        print(i)
#mulitiplication of a number n
n=2
i=1
while i<= 10 :
    i+=1
    print(n*i)
  
  #print following numbers in list using loop
nums=[1,4,9,16,25,36,49,64,81,100]

idx=0
while(idx<len(nums)):
    print(nums[idx])
    idx+=1

#search x in tuple using loop
nums=(1,4,9,16,25,36,49,64,81,100)

x=16

i=0
while i<len(nums):
    if(nums[i]==x):
         print("found at",i)
    i+=1
