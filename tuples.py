# to define a tuple
t = ()
t1 = tuple()

sample = ('a', 'b', 1234, "Terraform", 123.56, "172.168.0.1")
print(type(sample), sample)

# tuple is immutable
print(sample[0])
print(sample[0:2])
print(sample[-1])
# sample[0] = 12 # cannot be modified in tuple
# print(sample)

envs_list = ("DEV", "PROD", "QA")

print(dir(tuple))
"""
['count', 'index']
"""
sample = (1, 2, 3, 4, 5 ,5 ,6, 6 ,8)
print(sample.count(5), sample.count(1))
print(sample.index(5))

# Data type conversion ( Type Casting )
sample = ('a', 'b', 1234, "Terraform", 123.56, "172.168.0.1")
sample_l = list(sample) # it convert a tuple into list
print(type(sample_l))
print(sample_l)
sample_t = tuple(sample_l) # it converts a list into tuple
print(type(sample_t))
print(sample_t)