a=float(input("enter the number1:"))
b=float(input("enter the secondnum2:"))
print("sum",a+b)
print("sub",a-b)
print("mul",a*b)
print("div",a/b)

name="binod"
age=22
address="lalitpur"
# print("my name is "+name+ "and age is" +age+"address",+address) #it means it gives error while converting string or any data type
# print("my name is ",name "and age is", age,"address",address) gives error

# f-string/format string
print(f"my name is {name} and age is {age}and also address is {address}")