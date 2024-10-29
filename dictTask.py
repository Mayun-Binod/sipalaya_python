# 1. Given the dictionary person = {'name': 'Suman', 'age': 23, 'city': 'Kathmandu'}, add a new key-value pair 'job': 'Developer' to the dictionary. 
# Then update the value of the 'name' key to 'Ram Bahadur' and 'age' to 29.
# 2. Given a dictionary:
# my_details = {
#     'name':'Suman',
#     'grade': 0,
#     'address':'ktm',
#     'hobbies':{
#         'sports':'running',
#         'game':'pubg',
#         'novel':'xyz',
#         'anime':'one piece',
#     },
#     'email':'suman@gmail.com'
# }
# Change the value of 'novel' key from 'xyz' to 'Harry Potter'

# 3. Write a Python code to check whether a given key already exists in a dictionary.
# 4. Write a Python code to generate and print a dictionary that contains a number from 1 to 10 in the form x : x^2
# example: { 1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25.....so on }
# 5. Write a Python program to sum all the values in a dictionary (suppose all the values are integer).
# -----------------------------
# 1. Given the dictionary person = {'name': 'Suman', 'age': 23, 'city': 'Kathmandu'}, add a new key-value pair 'job': 'Developer' to the dictionary. 
# Then update the value of the 'name' key to 'Ram Bahadur' and 'age' to 29.

person={
    'name': 'Suman',
      'age': 23, 
      'city': 'Kathmandu',
}
person['job']='Developer'
print(person)
person['name']='Ram Bahadur'
print(person)

# 2. Given a dictionary:
# my_details = {
#     'name':'Suman',
#     'grade': 0,
#     'address':'ktm',
#     'hobbies':{
#         'sports':'running',
#         'game':'pubg',
#         'novel':'xyz',
#         'anime':'one piece',
#     },
#     'email':'suman@gmail.com'
# }
# Change the value of 'novel' key from 'xyz' to 'Harry Potter'
my_details = {
    'name':'Suman',
    'grade': 0,
    'address':'ktm',
    'hobbies':{
        'sports':'running',
        'game':'pubg',
        'novel':'xyz',
        'anime':'one piece',
    },
    'email':'suman@gmail.com'
}
my_details['hobbies']['novel']='Harry Porter'
print(my_details)

# 3. Write a Python code to check whether a given key already exists in a dictionary.
user=input("enter a key:")
# print(user in my_details)
if user in my_details:
    print('it is exists')
else:
    print("it is not exists")

# 4. Write a Python code to generate and print a dictionary that contains a number from 1 to 10 in the form x : x^2
# example: { 1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25.....so on }

empty_dict={}
for store in range(1,11):
    empty_dict[store]=store**2
print(empty_dict)

# 5. Write a Python program to sum all the values in a dictionary (suppose all the values are integer).
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
total_sum = sum(my_dict.values())

print("Sum of all values is:", total_sum)





