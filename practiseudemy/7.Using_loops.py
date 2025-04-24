
student_name = "alvin"
new_name = 'W'

for itr in student_name:
    if itr.lower() == "h":
        new_name += itr.upper()
    else :
        new_name += itr
print (student_name, "to", new_name)
     
# a = 1
# b = 2
# b += 4
# print(f"a= {a}" , f"b= {b}")

code = "Chipmunk"
for itr in code[::2]:
    print(itr)

print(code[-1])
code[len(code)-1]
print(code[len(code)-1])

work_tip = "Save your work tho oo"
print("\n", work_tip)
print('the number of w\'s in work_tip:', work_tip.count("w"))
print('the location of o\'s in work_tip:', work_tip.find("o"))

print ("\n",)
location = work_tip.find("o")
location = work_tip.find("o", location +1)
while location >= 7:
    print ("the location of o\'s in work_tip:", location)

    location = work_tip.find("o", location +1);
print ("no more") ;