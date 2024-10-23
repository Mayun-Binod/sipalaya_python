# Reverse a string.
string="BinodShrestha"
reverse_string=string[::-1]
print(reverse_string)

# Check if a string is a palindrome.
string_palidrome="racecar"
print(string_palidrome==string_palidrome[::-1])

# Count the occurrences of a character in a string.
string_occur="python is a programming language python"
print(string_occur.count("python"))

# Convert a string "HELLO WORLD" to lowercase.
convert_string="HELLO WORLD"
print(convert_string.casefold())

# Capitalize the first letter of each word in a sentence.
capitalized="my name is hari"
print(capitalized.title())

# Check if a string contains only numbers.
string_contains_number="12345"
string_contains_number2=12345
print(string_contains_number == string_contains_number2)

# Replace spaces with underscores in a string.
replace_spaces="hello my name"
print(replace_spaces.replace("my","_"))

# Check if a string is a valid number.
string_valid="hello i am valid"
print(string_valid.isdigit())


# Count words in a sentence. hint used split and len
string_count="hello binod shrestha"
change_in_list=string_count.split()
print(len(change_in_list))

# Count the number of occurrences of a word in a sentence.
number_of_occurences="hello i am occurences hello i am"
print(number_of_occurences.count("hello"))

# Convert the string str = "apple banana cherry" to a list of fruits.
str = "apple banana cherry"
convert_into_list=str.split()
print(convert_into_list)

# 13. Replace the substring "World" with "Python" in the string str = "Hello World" to form a new string "Hello Python".
str="Hello World"
print(str.replace("World","Python"))

# 14.convert capital letter to small and small letter to capital
capital_letter="HELLO binod"
print(capital_letter.swapcase())

# 12.Given a list of string names = ['ram','shyam','hari','manoj'] . Convert the list into string separated by comma. Like this:  ram,shyam,hari,manoj hint:join
names=['ram','shyam','hari','manoj']
print(','.join(names))

# .split()=> converts string into list
# .join()=> converts list into string