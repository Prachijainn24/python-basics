#list
marks=[94.4,87.1,95.2,66.4,45.1]
print(marks)
print(type(marks))
print(marks[0])
print(len(marks))

student=["prachi",20,"bca"]
print(student[0])
student[0]= "arjun" #change from prachi to arjun
print(student)

#list slicing
marks1=[85,90,20,76,95]
print(marks1[1:4])
print(marks1)

#list methods
list=[2,1,3]
list.append(4) #append
print(list)
print(list.sort()) #sorting aesc or desc
print(list.sort(reverse=True))
print(list)
list.insert(1,5) 
print(list)
list.remove(1)
print(list)
list.pop(2)
print(list)