server_1 = "172.10.33.26"
server_2 = "172.10.33.26"

servers = ["172.10.33.27", "172.10.33.55", True, "Ansible", 1020, 500, False, "Hello World"]
print(type(servers), servers, server_1)

server_1 = servers[0]
print("Server 1 IP is:" , server_1)
server_2 = servers[1]
print(server_2)

# slicing (start_index:end_index: step_size)
simple_slice = servers[1:7:2] #[1, 1+2, 3+2, 5+2 ]
print(simple_slice)

#Negative slicing
negative_slice = servers[-1:-4:-2]
print(negative_slice)

#Find length of a list
print("Length of List:" ,len(servers))

# List is a mutable datatype
# Mutable: Once defined, can change at any time eg. Lists, Dictionaries
# Immutable: Once defined, cannot be changed eg. tuples, sets

print("Before Modify:", servers)
servers[-1] = "Hello"
print("After Modification:" , servers)

# print("List of Operations:", dir(servers))

""" 
['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'] """
# To append a value in a list
servers.append("abcd")
print(servers, len(servers))

# To append a list in a list
servers.append(["a","b"])
print(servers, len(servers))

# Multi indexing
print(servers[-1][0])

# extend
servers.extend(["c","d"])
print(servers, len(servers))

#to print the index of a value in list
print(servers.index(True))

# insert (index, new_value)
servers.insert(0, 12)
print(servers)

# remove
servers.remove(False)
print(servers)

# reverse
servers.reverse()
print(servers)

servers = servers[::-1]
print(servers)

#sort
servers_1 = [1, 5, 7, 2, 9, 4, 3]
servers2 = sorted(servers_1)
print(servers2, servers_1)

#copy
servers_3 = servers_1.copy()
servers_3.remove(1)
print(servers_3)
servers_3.sort()
print(servers_3)