#set is collection of unordered items . its is unquie and immutable
collection = {1,2,3,4}
print(collection)
print(len(collection))
#colleaction = set() #sytax for empty set

print(collection.add(5))
print(collection)

collection.add(5)
print(collection)

collection.remove(1)
print(collection)

#collection.clear()
#print(collection)

collection.pop() #they remoove any random value from set
print(collection)

set1 = {1,2,3}
set2 = {7,8,9}
print(set1.union(set1))
print(set1)
print(set1.intersection(set2))