# Numbers

### Numbers contains integer, float, fractions, set(some difference), boolean (0 or 1)

### always take precaution that operation doesnot perform on two different datatypes

### repr() method -> buitl-in method -> goal is to have unambiguous
### Return a string containing a printable representation of an object.

### >>> repr('4')
### "'4'"
### >>> repr(4)
### '4'
### >>> repr(2.33)
### '2.33'

### string -> built-in method -> for readbility
### returns the string version of the object 


### The major difference between repr and str
### >>> str('3') == str(3)
### True
### >>> repr('3') == repr(3)
### False

### print()
### print(*objects, sep=' ', end='\n', file=None, flush=False)
### Print objects to the text stream file, separated by sep and followed by end. 
### sep, end, file, and flush, if present, must be given as keyword arguments.
### If no objects are given, print() will just write end.