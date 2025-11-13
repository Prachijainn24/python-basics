#q1 wap to ask user about their 3 fav. mlcvies and sort them into the ,lists
'''movies=[]
mov=input("enter 1st movie:")
movies.append(mov)
mov=input("enter 2nd movie:")
movies.append(mov)
mov=input("enter 3rd movie:")
movies.append(mov)'''

#wap to check if a list is containing a palindrom of elements
list1=[1,2,1]
list2=[1,2,3]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
        print("palindrome")
else:
        print("not a palindrome")

 #wap to count no. of students having A grade in following list.
grade=["c","d","a","a","b","b","a"]  
print(grade.count("a"))  

#wap to sort list from a to d the following list
grade=["c","d","a","a","b","b","a"]  
grade.sort()
print(grade)