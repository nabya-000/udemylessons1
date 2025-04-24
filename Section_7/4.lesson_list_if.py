#  sortling data
# names = ["shorty", " lengthy", "Zachary", "alice", "Yohan"]
# short_name = ""
# long_name = ""

# for shortlist in names:
#     if len(shortlist) <= 5:
#         short_name += shortlist + "\n"
#     else:
#         long_name += shortlist
# print("shortlist:\n", short_name)
# print("longerlist:\n", long_name)

#  using square brackets
# short_name = []
# long_name = []

# for shortlist in names:
#     if len(shortlist) <= 5:
#         short_name += shortlist 
#     else:
#         long_name += shortlist
# print("shortlist:\n", short_name)
# print("longerlist:\n", long_name)

# counting number of a's in the bracket
Cities = ["Australia","Tokoyo", "San_francisco", "Delhi", "Hyderabad"]
Letter = "a"
List = 0

for nu_cities in Cities:
    List += nu_cities.lower().count(Letter)
    print(List)

print("List : \n", List)

# using iteration to find cities:

def city_search (search_item, cities= ["Australia","Tokoyo", "San_francisco", "Delhi", "Hyderabad"]):
    for number_cities in cities:
        if number_cities.lower() == search_item.lower():
           return True
        else:
            pass
    return False

Visited_cities = ["Australia","Tokoyo", "San_francisco", "Delhi", "Hyderabad", "NL", "Berlin"]
search = input("Enter the city visited:")
print()

print(search.title(), "the default city", city_search(search) )
print(search.title(), "the selected city", city_search(search, Visited_cities) )
