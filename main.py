# Set items are enclosed in curly brackets{}
# Set is unordered
# Set is mutable, can contain only immutable
# Set elements are unique
# Elements can contain only immutable items

'''
Sets can be used for mathematical set operation such as union, intersection, difference and symmetric difference.

http://en.wikipedia.org/wiki/Ser_(mathematics)
'''

'''
Python Set Attributes
'''

# print(dir(set))

'''
Creating Python Sets
'''
set= {1,2,3}
print(set)

# initialize a with {}
empty= {}
print(type(empty))# Output => <class 'dict'>

# initialize a with set () 
# empty= set()
# print(type(empty)) # Output => <class'set'>

'''
Modifying a set in Python
'''

set_example= {'Hello', 'world'}
# set_example[0]
# print(set_example) # output => TypeError
# you cannot call using indexing
# TypeError 'set' object is not subscriptable

# using add and update methods
set_example= {'Hello', 'world'}
set_example.add('yay!')
set_example.add(('hey!'))
set_example.update([1,2,3])
print(set_example) # output => {'Hello',1,2,3, 'yay!','hey', 'world'}


'''
Removing elements from a set
'''
# discard an element
set_example= {1,2,3,4}
set_example.discard(3)
print(set_example) # => {1,2,4}

# using remove
set_example= {1,2,3,4}
set_example.remove(1)
print(set_example) # => {2,3,4}

# pop an element
set_example= {1,2,3,4}
set_example.pop
print(set_example)# output => random element

# clear the set
set_example= {1,2,3,4}
set_example.clear()
print(set_example) # output => set()

# set do not allow duplicate words
set= {'hello','hello','hello','world'}
print(set) # => {'hello','world'}


'''
Set Union Operations
'''

# use union | operator
a = {1,2,3,6,7}
b = {4,5,6,7,8,9}
print(a | b)
print(a.union(b))
# output => {1,2,3,4,5,6,7,8,9}

'''
Set Intersection Operations
'''

# using & operator
a = {1,2,3,6,7}
b = {4,5,6,7,8,9}
print(a & b )
print(a.intersection(b))# output => {6,7}


'''
Set difference Operations
'''
# using - operator
a = {1,2,3,4,6,7,9}
b = {2,5,6,7,8,9}

print(a - b) # output => {1,3,4}
print(a.difference(b)) # output => {1,3,4}

print( b - a )
print(b.difference(a))# output => {8,5}

'''
Set Symmetric difference
'''

#  using ^ operator

a = {1,2,3,4,6,7,9}
b = {2,5,6,7,8,9}
print(a ^ b) # output => {1,3,4,5,8}
print(a.symmetric_difference(b)) # =>{1,3,4,5,8}


'''
Set Methods
'''

print(dir(set))



