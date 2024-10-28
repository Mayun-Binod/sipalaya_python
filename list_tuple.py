# List
# collection of data enclosed within big brackets []
# each data is separated by comma ,

# Features:
# 1. mutable / original data can be changed or modified
# 2. allow duplicates
# 3. allow indexing
# 4. ordered

a = [1,2,3]
print(type(a))

# duplicate/ ordered
a = [6,3,2,1,'hari',[9,4,'ram'],1,2,3,6]
print(a)

# indexing
a = [6,3,2,1,'hari',[9,4,'ram'],1,2,3,6]
print(a[5][2][1])

# mutable
a = [1,4,5,7,9]
a[0]=0
print(a)


# Slicing: self study


# Methods:
# list.methodName()

a = [4,5,3,2,1]

# .append() -> for adding only one data in list
a.append(6)
print(a)

# .extend() -> for adding multiple data
a.extend([6,7,8])
print(a)

# .pop()    -> removes last index value
a.pop()
a.pop(2)
print(a)

# .clear()  -> clears the list
a.clear()
print(a)


del a
print(a)

# .copy()   -> makes a copy of list
b = a.copy()
print(b)


# .count()  -> counts how many time a data is repeated in the list
print(a.count(4))


print(a.index(5))


# .sort()   -> sorts values in ascending order
a.sort(reverse=True)
print(a)


a.remove(4)
print(a)


print(len(a))
print(sum(a))
print(min(a))
print(max(a))



# Tuple:
# collection of data separated by comma inside small brackets
# Features:
# 1. immutable/ original data cannot be changed
# 2. allow duplicates
# 3. allow indexing
# 4. ordered

# uses less methods than list thats why it is faster

a = (1,8,5,3,1,5,3)
print(type(a))
print(a[0])
a[0] = 0


print(a.count(5))
print(a.index(8))

print(len(a))
print(sum(a))
print(min(a))
print(max(a))


# Loop:
# doing same tasks repeatedly is called loop

# 1. for loop
# 2. while loop


# 1. for loop
# syntax:
# for variable in iterable/collection data:
    # code

a = [4,5,3,2,1]
a = 'hello'

for i in a:
    # print(i)
    if i%2==0:
        print(i)


# range
# syntax:
# range(start,stop,step)

for i in range(5):
    # print(f"{i} Sorry for the delay")
    print('hello')


a = ['hari','ram']

for i in a:
    # print(i)
    for j in i:
        print(j)








