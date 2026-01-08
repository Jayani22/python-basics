# for loop and while loop

#For while loop we need to specify condition
#continue, break

value = 0

while value < 10:
    print("Value :" , value)
    value = value + 1

# break

value = 1
while value < 11:
    if value == 6:
        break
    print("Break:", value)
    value = value + 1

# continue , when we use continue need to give condition

value = 1
while value < 11:
    if value == 6:
        value = value + 1 # incrementing is very important
        continue
    print("Continue:", value)
    value = value + 1

sample = ["server1", "server2","server3", "server4", "server5", 123]

idx = 0
 
while idx < len(sample):
    print("while:", sample[idx])
    idx += 1 # idx = idx + 1

# for loop
# in -> membership operator( checks whether that element is present or not)
print(1 in sample) # it checks whether the element is present in sample or not. # False
print("server1" in sample) # True

#ele -> call it as iterator
# sample -> iterable
for ele in sample:
    print("for:", ele)

# access elements inside a list with index using for loop

# range, enumerate
# range is a function in python, (start(inclusive/optional), stop(exclusive/mandatory), step) need to specify

# print(list(range(1,101)))

#range

for idx in range(len(sample)):
    print("range:", sample[idx])


for idx in range(len(sample)):
    ele = sample[idx]
    print("range:", idx, ele )

#enumerate
print(enumerate(sample))
for idx, val in enumerate(sample):
    print(idx, val)

#tuple unpacking
# a, b = (1, 2)
# print(a, b)