#wap to check if a list contains a palindrome of elements 
list = [ 1 , 2, 3,2, 1]
list1 = list.copy()
list1.reverse()
if (list1 == list):
    print("palidrome")
else : 
    print("not palirdrome ")
