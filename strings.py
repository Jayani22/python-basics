sample = "hello , How are you?"

sample_1 = "abc"
print(sample_1[1])
print(sample)
print(sample[0])

# sample_1[0] = "h" # it wont modify because string is immutable datatype
#print(sample_1)

print(dir(sample))

print(sample.capitalize())

print(sample.casefold())

print(sample.center(50, "#"))

#Reverse a string
print(sample[::-1])

print(tuple(sample_1), list(sample_1)) #type casting

sample = "hello, How is your work?"
print(sample.split(" "))
print("#".join(sample.split(" ")))

#concatenation : joining 2 strings
print("a" + "b") #ab