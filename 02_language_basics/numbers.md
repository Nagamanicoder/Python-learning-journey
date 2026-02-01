# Numbers

### Numbers contains integer, float, fractions, set(some difference), boolean (0 (False) or 1(True ))

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

### math functions

### import math
### floor-> gives closest number to it
### >>> math.floor(3.5)
### 3
### >>> math.floor(-3.5)
### -4

### trunc -> gives number that leads towards zero
### >>> math.trunc(3.5)
### 3
### >>> math.trunc(-3.5)
### -3

## complex numbers 
### >>> (2 + 1j) * 3
### (6+3j)

## bin, oct, hex
### >>> 0o20
### 16
### >>> 0xFF
### 255
### >>> 0b1000
### 8
### >>> oct(64)
### '0o100'
### >>> hex(4)
### '0x4'
### >>> bin(64)
### '0b1000000'

## other methods to convert the number into bin, hex, oct 
### >>> int('64' , 8)
### 52
### >>> int('64', 16)
### 100
### >>> int('1000', 2)
### 8

## random methods
### import random 
### >>> random.random()
### 0.2524879772380241

### random.randint(1, 10)
### 2
### >>> random.randint(1, 10)
### 1
### >>> l1 = [1,2,3,4,5,6,7]
### >>> random.choice(l1)
### 1
### >>> random.choice(l1)
### 2
### >>> random.choice(l1)
### 1
### >>> random.choice(l1)
### 3

## decimal functions
### >>> from decimal import Decimal
### >>> 0.1 +0.1 + 0.1             
### 0.30000000000000004
### >>> 0.1 + 0.1 + 0.1 -0.3
### 5.551115123125783e-17
### >>> Decimal('0.1') + Decimal('0.1') + ### Decimal('0.1')
### Decimal('0.3')
### >>> Decimal('0.1') + Decimal('0.1') + ### Decimal('0.1') - Decimal('0.3')
### Decimal('0.0')

## fractions
### >>> from fractions import Fraction  
### >>> myFra = Fraction(2,7)
### >>> myFra
### Fraction(2, 7)

## set
### setOne = {1, 2, 3, 4}
### >>> setOne
### {1, 2, 3, 4}
### >>> setOne - {1, 2, 3, 4}
### set()
### >>> setOne & {1, 2, 3, 4}
### {1, 2, 3, 4}
### >>> setOne & {4, 5, 6, 8}
### {4}
### >>> setOne | {4, 5, 7, 1, 2, 3}
### {1, 2, 3, 4, 5, 7}

### >>> type({})
### <class 'dict'>


###  True == 1
### True
### >>> False == 0
### True
### >>> True + 1
### 2
### >>> False + 0
### 0
### >>> False + 1
### 1

### True is 1
### <stdin>:1: SyntaxWarning: "is" with a ### literal. Did you mean "=="?
### False

## True is treated as 1 
## True and 1 are different objectsin the memory