
#  different types of data can be put in a list

num = 20
data = [num, "book", [2, "hard"], 80]
print(data[1])
print (data[2][0])
inner_line = data[2]
print(inner_line[1])

#  altering the input in the list
data[0] =200
print(data)
# data[4]= "True"
# print(data)

# Understanding how list works
# a = [3, 5]
# b = a
# print("the value of a[0]: {}, b[0]: {}".format(a[0], b[0]))
# print("the location of a[0]: {}, b[0]: {}".format(id(a[0]), id(b[0])))
# a[0]= 20 # automatically assigning vale of b[0]
# print("the value of a[0]: {}, b[0]: {}".format(a[0], b[0]))
# print("the location of after reassigning value of a- a[0]: {}, b[0]: {}".format(id(a[0]), id(b[0])))


# #  adding to the list using appped
# data.append(67)
# print(data)
# data.append("Helllow")
# print(data)

# # alternate adding 
# party_list = ["Tobia", "Jerry", "Austin"]
# print("before list:", party_list, "/n")
# party_list[2] = party_list[2] + ", Zachary"
# print("after list:", party_list, "/n")
# party_list.insert(0, "Alice")
# print(party_list)

# #  removing fron list using pop()- by default removes last value
# data.pop()
# print("\nremoving the items from list:")
# print(data)

# removing using try and excerpt method:

games= ["soccer", "football", "batminton", "cricket"]

# try: 
#     games.remove("soccor")
# except:
#     print("the item does not exists")
# print("\n",games)

# using conditional statements:
# if "cricket" in games:
#     print("Game is in the list")
# if "Hockey" not in games:
#     print("Not found in the list")

# print('soccer' in games)   # outputs True

#  Sorting the list

nums =[5, 7, 9 ,10 , 3, 2]
# sorted_num = sorted(nums)
# print(nums, sorted_num)     # 1st style
# nums.sort()
# print("\n",nums)
extened_list = nums.extend([9])
print(f"list is : {extened_list}, {nums}, \n {nums.extend([4])}")