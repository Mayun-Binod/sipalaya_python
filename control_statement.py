# Control Statements:
# 1. break
# 2. continue
# 3. pass


# break
for i in range(10):
    if i == 5:
        break
    else:
        print(i)


# continue
for i in range(10):
    if i == 5:
        continue
    else:
        print(i)


# pass
for i in range(5):
    pass


# if 2==2:
    pass
print('hello')



a = [1,2,3,4,5]

for i in a:
    if i%2==0:
        print(i)


[print(i) for i in a if i%2==0]
