# # Managing a shopping list and grocery items
# # 1. Checking if an itme is in the list
# # 2. Adding an item to the list
# # 3. Removing an item from the list
# # 4. Accessing an item by index
# # 5. Modifying the quantity of an item in the nested grocery list

# # Shopping list
# shopping_list = ['milk', 'eggs', 'bread', 'cheese', 'apples']

# # Print the list
# print("Shopping List: ")
# print(shopping_list)

# # Checking if an item is in the list
# item_to_check = input("Enter an itme to check if it's in the shopping list: ")
# if item_to_check in shopping_list:
#     print(f"{item_to_check.capitalize()} is in the shopping list.")
# else:
#     print(f"{item_to_check.capitalize()} is not in the shopping list.")

# # Adding a new item to the list
# new_item = input("Enter a new item to add to the shopping list: ")
# shopping_list.append(new_item)
# print(f"Added {new_item} to the shopping list.")
# print(shopping_list)

# # Removing and item from the list
# item_to_remove = input("Enter an item to remove from the list: ")
# if item_to_remove in shopping_list:
#     shopping_list.remove(item_to_remove)
#     print(f"Removed {item_to_remove} from the shopping list")
# else:
#     print(f"{item_to_remove.capitalize()} is not in the shopping list")
#     print(shopping_list)

# # Sort the list alphabetically
# shopping_list.sort()
# print("Shopping list sorted alphabetically:")
# print(shopping_list)

# # Accessing an item by index
# index = int(input("Enter an index to access the item in the list:"))
# try:
#     print(f"The item at index {index} is {shopping_list[index]}")
# except IndexError:
#     print("Invalid index, list out of bounds!")

# # Nested list - Grocery items with quantities
# grocery_items = [
#     ['milk', 2],
#     ['eggs', 1],
#     ['cheese', 3],
#     ['apples', 5]
# ]

# # Accessing nested list items
# print("Grocery items with quantities: ")
# for item, quantity in grocery_items:
#     print(f"{quantity}{item}{'s' if quantity > 1 else ''}")

# Modify the quantity of an item
grocery_items = [
['milk', 2],
['eggs', 1],
['cheese', 3],
['apples', 5]
]

# Modify the quantity of an item
item_to_modify = input("Enter an item to modify its quantity: ")
item_found = False
for i, (item, quantity) in enumerate(grocery_items):
    if item == item_to_modify:
        new_quantity = int(input(f"Enter the new quantity for {item}: "))
        grocery_items[i][1] = new_quantity
        item_found = True
        break

if item_found:
    print("Updated grocery items with quantities:")
    for item, quantity in grocery_items:
        print(f"{quantity} {item}{'s' if quantity > 1 else ''}")
else:
    print(f"{item_to_modify.capitalize()} is not in the grocery list.")