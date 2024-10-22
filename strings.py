# string 
# collecton of characters,letters,symbols,numbers,etc. inside quotation

# characteristics
# 1. immutable./not changeable/non-primitive which does n't allow to change the original value

# ordered data is printed in the order they are stored in
# allow indexing  allow accessing data using index
# allow duplicate . allow us to store same value multiple times

# wap to take string as input from user and print true if it's palindrome otherwise false (hint:use slicing)
sentence = input("Enter a string: ")
print(sentence == sentence[::-1])

