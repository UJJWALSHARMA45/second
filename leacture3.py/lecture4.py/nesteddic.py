student= {
    "name ": "ujjwal shrma" ,
    "subjects" : {
        "phy": 97 ,
        "chem": 68,
        "maths":23
    }
}
# print(student["subjects"]["chem"])

# #dictinary methods 
# #mydict.keys() #returns of all keys 
# print(len(student))
# print(list(student.keys()))

# # mydict.values() #returns all values 
# print(student.values())

## mydict.items()#returns all ( key , val ) pairs as tuples 
#  # print(student.items())
#      pair = list(student.items())
#  print(pair[0])


# mydict.get("key") #return the key according to value 
      #


# mydict. update(newdict) #insert the specified item to the dictionairy
  #print(student.update({"city":"delhi"}))
 new_dict = {"city" : "delhi"}
student.udpate(new_dict)
print(student)