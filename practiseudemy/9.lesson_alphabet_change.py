# changing the talphabets of the texts.

#  by converting the data type
company_name = "Techcorp"
print(company_name)        # printing
name_char = list(company_name)
name_char[0] = 'j'
modified_name = ''.join(name_char)
print(modified_name)        # printing

#  by joining the strings
print("\n joining the strings")
company_name = "Techcorp"
print(company_name)        # printing
# company_name[0] - 'j'
modified_name = 'h' + company_name[1:]
print(modified_name)

# finding something in a string
log_text = "error 404: this is not found"
error_position = log_text.find("404")
print (error_position)
error_replace = log_text.replace("this", "this file")
print (error_replace)