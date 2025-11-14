def calcsum(a,b):  #function defination,parameters
     sum=a+b
     print(sum)
     return sum

calcsum(2,3) #function call,arguments
calcsum(3,5) #function call
calcsum(6,3) #function call

#print hello
def print_hello():
     print("hello")

print_hello()

#avg of 3 numbers
def calc_avg(a,b,c):
     sum=a+b+c
     avg=sum/3
     print(avg)

calc_avg(4,8,10)

#multiplication of two numbers
def calc_mult(a=1,b=4):
      mult=a*b
      print(mult)

calc_mult()    

#calculate length of list on using function
cities = ["jaipur", "hydrabad", "gurgaon"]

def print_list(lst):
    print(len(lst))

print_list(cities)

print(cities[0], end=" ")
print(cities[2], end=" ")

def print_lst(list):
    for item in list:
         print(item,end=" ")

print_lst(cities)    

#calculate factorial of n as paramenter in function
def  calcfact(n):
     fact=1
     for i in range(1,n+1):
          fact *=i
          print(fact)

calcfact(5)         
      
#convert USD to INR
def convertor(usd_val):
     inr_val=usd_val*83
     print(usd_val,"USD",inr_val,"INR")

convertor(56)     