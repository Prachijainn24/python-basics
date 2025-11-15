#print n to 1 backwards
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)

#factorial using recusion
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
    
print(fact(5))   

#sum of n natural numbers using recursion
def calcnatural(n):
       if(n==0):
        return 0
       return  calcnatural(n-1)+n
   
sum=calcnatural(5)
print(sum)

#print all elements using resursion
elements=["a","b","c","d"]
def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print(list,idx+1)

print_list(elements)    