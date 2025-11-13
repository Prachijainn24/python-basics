collection={1,2,3,4,"hello","world"}
print(collection)
print(type(collection))
print(len(collection))
collection=set()#empty set
print(type(collection))
#
collection.add(1)
collection.add(5)
print(collection)
collection.remove(1)
print(collection)
collection={"hello","we","are","learning","python"}
print(collection.pop())

#set union and set intersection
set1={1,2,3,4,5}
set2={6,7,8,9,0,1}

print(set1.union(set2))
print(set1.intersection(set2))