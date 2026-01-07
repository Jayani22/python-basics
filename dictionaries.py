# to define a dictionary
d = {}
d_1 = dict()

# dictionary are in key:value pair based
#also known as hashmaps

sample = {'a': 1, 'b': 2}
print(sample['a'], sample.get('b'))

#dictionaries are mutable data type
sample['a'] = 10
print(sample)

# Keys in dictionaries, once defined cant be changed
# Hence they should be of immutable datatype

sample = { ("a", "b"): 1, "b": 2}
print(sample)

# print(dir(sample))

print(sample.keys(), sample.values(), sample.items())
#item will give both key and value pairs

sample_list = [(('a','b'), 1), ('b', 2)]
sample_dict = dict(sample_list)
print(sample_dict)
