# mutable means that can be changed in the memory
# immutable means that cannot be changed in the memory

# python dosumentation
# data model 3 
# read 3.1

# The value of some objects can change. Objects whose value can change are said to be mutable; objects whose value is 
# unchangeable once they are created are called immutable. (The value of an immutable container object that contains 
# a reference to a mutable object can change when the latter’s value is changed;
# however the container is still considered immutable, because the collection of objects it contains cannot be changed. 
# So, immutability is not strictly the same as having an unchangeable value, it is more subtle.) An object’s mutability 
# is determined by its type; for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.

# Objects are never explicitly destroyed; 
# however, when they become unreachable they may be garbage-collected. 
# An implementation is allowed to postpone garbage collection or omit it altogether — 
# it is a matter of implementation quality how garbage collection is implemented, 
# as long as no objects are collected that are still reachable.