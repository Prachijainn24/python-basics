info={
    "name":"prachi",
    "subjects":["python","c++","java"],
    "topics":("dict","sets"),
    12:94.3,
    "cgpa":8.90
}
info["name"]="prachi jain" #modify values in dictionary
info["surname"]='jain' #added both key and value
print(info)

#nested student
student={
    "name":"prachi",
    "subjects":{
            "python":90,
            "maths":85,
            "dbms":95   
              }
}
print(student["subjects"]["python"])

#returns all keys in dictionary
print(list(info.keys()))
#print all values in dictionary
print(list(student.values()))
#print keys and values in form of tuples
pairs=list(student.items())
print(pairs[(0)])
#print keys according to values
print(student.get("name"))
#uppdate method
student.update({"city":"delhi"})
print(student)