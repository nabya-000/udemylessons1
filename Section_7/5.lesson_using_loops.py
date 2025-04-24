# using loops

# for num in range(5):
#     print("Value:{}".format(num))

# for num in range(2,10, 3):
#     print("Value:{}\n".format(num))  # using range

# for num in range(5):
#     if num ==3:
#         continue
#     print(num)                   #using continue

#print("\n")

# for num in range(5):
#     if num ==3:
#         break
#     print(num)        #using break

# nested list

# Students = [
#     ['John', [80, 60, 98]]
#     ['Emma', [78, 87, 95]]
#     ['Michel' [88, 77, 90]]
#     ['Clara' [80, 89, 95]]
# ]

# assessing the items in the list:

Grocery_list = [
    ['milk',3],
    ['bread',1],
    ['biscuit',3],
    ['eggs',12]
]
# MODIFYING THE QUANTITY OF AN ITEM
change_item = input("enter the item that needs to be changed:")
item_found= False

for i,(items, quantity) in enumerate (Grocery_list):
    if items[i] == change_item:
        change_quant =int(input(f"enter the new quantity of {change_item}:"))
        Grocery_list[i][0] = change_quant
        item_found = True
    break

if item_found:
    for items, quantity in Grocery_list:
        print(f"the updated list:{Grocery_list}\n")
        print(f"{quantity}-{items}-{'s' if quantity > 0 else ''}")  
else:
     print(f"{quantity} is not found in Groceries list") 

