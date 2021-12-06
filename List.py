
# friends = ["Kevin", "Lara", "Jim", "Tom", "Toby"]
# #             0        1       2     3       4
# print(friends)
# print(friends[1])
# print(friends[1:]) #print after 1
# print(friends[1:3]) # print 1-3

#-------------------------------------------------
#list function
lucky_number = [4,5,20,36,40,25,36]
friends = ["Kevin", "Lara", "Jim", "Tom", "Toby"]

# friends.extend(lucky_number) #add two list
# print(friends)

friends.append("Creed") #add new list item
print(friends)

friends.insert(2, "Kelly") #insert item for middle of the list
print(friends)

friends.remove("Jim") #remove list item
print(friends)

# friends.clear() #clear list(all item in the list)
# print(friends)

friends.pop() #remove last element
print(friends)

print(friends.index("Tom")) #get index of list item

friends.sort() #sort list in asc order
print(friends)

friends.reverse()
lucky_number.reverse()
print(friends) #desc order
print(lucky_number)

friends2 = friends.copy() #copy list
print(friends2)

