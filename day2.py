name=input("enter the name:")
print(type(name))

# data type of python

# numeric data type
# 1.integer
# 2.float
# 3.complex

# 1.integer
#123455,36736437,0,-64532764287
a=5663488
print(type(a))

# 2.float
b=5663488.6666
print(type(b))


# 3.complex
c=3j
d=2+5j
print(type(c))
print(type(d))

# sequence data type
# 1.String
# 2.List
# 3.Tuple
# 4.Range

# 1.string
first_name="my name is name1"
second_name='binod shrestha'
print(type(first_name))
print(type(second_name))

"""my
 name 
  is 
   binod shrestha""" #this is multiline comment

variable="""my
 name 
  is 
   binod shrestha"""
print(type(variable))

# boolean date type
# 1.True(1)
# 2.False(0)

# set data type
# 1.set
# 2.frozenset
set1={1,2,3,4,5}
print(type(set1))

# 2.frozenset
set2=frozenset(set1)
print(type(set2))

# 3.binary data type
# 1.bytearray
# 2.bytes
# 3.memoryview

dict={
    'name':'binod',
    'another_dict':{
        'first':'binod22',
        'second':'shrestha33'
    }
}