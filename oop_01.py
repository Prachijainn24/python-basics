class Student:               #class
    name="prachi jain"

s1=Student()                 #object
print(s1.name)

s2=Student()                 #object
print(s2.name)


class Cars:
        color="blue"

car1=Cars()
print(car1.color)       

#constructor(__init__function)
#default constructor
class Student:
      def __init__(self):  
            self.name="VRANDA"
            self.marks=100
s1=Student()           
print(s1.name,s1.marks)

#parameterized constructor
class Doctor:
      def __init__(self,dname,Did):
            self.dname=dname
            self.Did=Did
            print("adding doctor database")

s3=Doctor("rahul",101)
print(s3.dname,s3.Did)


#que-print class student with name and marks of 3 subjects and create method tob print marks average
class Student:
    def __init__(self,name,marks):
          self.name=name
          self.marks=marks
           

    def get_avg(self):
          sum=0
          for val in self.marks:
            sum+=val
            print("hii",self.name,"your score is:",sum/3)
s1=Student("shreya",[99,98,97])          
s1.get_avg() 

#que-create an account in which 2 attributes to be balance and account no. and also create a method conataining credit,debit and balance of that person's account
class Account:
    def __init__ (self,bal,acc):
     self.bal=bal
     self.acc=acc

    def debit(self,amount):
      self.bal -= amount
      self.bal += amount
      print("RS",amount,"was debited")

    def credit(self,amount):
     self.bal=+amount
     print("RS",amount,"was credited")

    def balance(self,amount):
     return self.balance
     print("RS",amount,"total balance")     

acc1=Account(10000,12345678)
acc1.debit(10000)
acc1.credit(20000)
print(acc1.bal,acc1.acc)
