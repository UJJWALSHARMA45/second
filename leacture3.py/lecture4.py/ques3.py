#wap to enter marks of 3 sub from the user and store them in a dic . start with an  empty dictonaryand add one by one . use subject as key and marks as value 
dic = {}
x = int(input("enter the marks  of physics : "))
dic.update({"phy": x})

x = int(input("enter the marks  of chemistry : "))
dic.update({"chem" : x})

x = int(input("enter the marks  of maths : "))
dic.update({"maths" : x})

print(dic)