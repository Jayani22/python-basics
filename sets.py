#sample = set() # This is the only way to define a set

sample = {'a', 'b', 'a'}
print(sample) # b,a

# sets are unordered collection
# sets removes duplicates and stores unique values

#print(dir(sample))

"""
 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""

sample.add(20)
print(sample)

# print(sample[0]) 
# Ordered collection such as list, tuple, dict supports indexing
# Undordered collection doesnt support indexing

s1 = {1,2,3,4}
s2 = {2,4,6,8}
print(s1.difference(s2)) # {1,3}
s1.difference_update(s2)
print(s1)
