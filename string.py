#string concatination
str1="this is my second lecture\n"
len1=len(str1)
str2="and this is all about string\n"
len2=len(str2)
str3="taking lectures from apna college"
print(str1+str2+str3)

final_str=str1+" "+str2
print(final_str)
print(len(final_str))

#indexing
str="apna college lectures"
ch=str[0]
print(ch)
print(str[3])

#slicing
str="ram is playing"
print(str[:4])
print(str[4:])
print(str.count("p"))

#negative indexing
str="apple"
print(str[-3:-1])

#string functions
str="i am a coder"
print(str.endswith("er")) #true
print(str.capitalize()) #I am a coder
print(str.find("a"))