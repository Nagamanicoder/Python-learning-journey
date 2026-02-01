### "" , '', """ """ (this one contains the exact formats as it is like line break, tab spaces)

### slicing

### numbers = [1, 2,3,4,5,6,7,8,9]
### >>> numbers[:-1]
### [1, 2, 3, 4, 5, 6, 7, 8]
### >>> numbers[-4:-1]
### [6, 7, 8]
### >>> numbers[-8:-1
### ... ]
### [2, 3, 4, 5, 6, 7, 8]
### >>> numbers[-9:-1]
### [1, 2, 3, 4, 5, 6, 7, 8]
### >>> numbers[-9:-2]
### [1, 2, 3, 4, 5, 6, 7]
### >>> numbers[::-1] 
### [9, 8, 7, 6, 5, 4, 3, 2, 1]
### >>> numbers[0:10:2]
### [1, 3, 5, 7, 9]
### when stepping happens, the step is not inclusive like the if 2 stepcount is given then, only the 1 number is hopped out

### Functions in strings like lower, upper, strip, replace, join, find, count

### chai = 'Ginger Chai'
### >>> chai.lower()

### 'ginger chai'
###  chai.upper()  

### 'GINGER CHAI'
### >>> chai.strip()

### 'Ginger Chai'
### >>> chai = "  MAsala chai  "
### >>> chai
### '  MAsala chai  '
### >>> chai.strip()

### 'MAsala chai'
### >>> chai = "Lemon Chai"

### >>> chai.replace("Lemon", "Ginger")
### 'Ginger Chai'
### >>> chai
### 'Lemon Chai'

### chai = "Lemon, Ginger, Masala, Mint"
### >>> chai.split()
### ['Lemon,', 'Ginger,', 'Masala,', 'Mint']

### >>> chai.split(',') -> separator
### ['Lemon', ' Ginger', ' Masala', ' Mint']

### chai = "Ginger chai"
### print(chai.find("chai"))
### 7

### print(chai.find("Chai"))
### -1

### chai = "Masala chai chai chai chaichai"
### >>> chai.count("chai")
### 5

### Plcaeholder practice: {}
### 
### chai_type = "Ginger"
### >>> quantity = 2
### >>> order = "I ordered {} cups of {} chai"
### >>> order
### 'I ordered {} cups of {} chai'
### >>> order.format(quantity, chai_type)
### 'I ordered 2 cups of Ginger chai'


### chai_variety = ["Lemon" ,"Masala", "Ginger" ]
### >>> chai_variety

### ['Lemon', 'Masala', 'Ginger']
### >>> "".join(chai_variety)
### 'LemonMasalaGinger'

### >>> " ".join(chai_variety)
### 'Lemon Masala Ginger'

### >>> chai = "Nagamani"
### >>> len(chai)
### 8

### name = "Nagamani"
### >>> for char in name:
### ...     print(char)
### ... 
### N
### a
### g
### a
### m
### a
### n
### i

### raw text
### sentence = "Masala\nChai"
### sentence
### 'Masala\nChai'
### >>> print(sentence)
### Masala
### Chai
### >>> sentence = r"Masala\nChai"
### >>> sentence
### 'Masala\\nChai'
### >>> print(sentence)
### Masala\nChai