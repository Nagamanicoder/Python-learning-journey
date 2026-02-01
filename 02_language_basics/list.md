 ### srings are treated as lists
 ### lists are ordered
 ### so, some of the methods that can be applied to strings are applied to the lists
 ### slice 
 ### tea_varities = ["white", "black", "green", "Oolang"]
 ### tea_varities[1:2] = "Herbal" -> the input string is treated as the an array
### >>> tea_varities
### ['white', 'H', 'e', 'r', 'b', 'a', 'l', 'green', 'Oolang']
### tea_varities
### ['white', 'black', 'green', 'Oolang']
### >>> tea_varities[1:3] = ["Masala"] -> so the input string should be included in the []
### >>> tea_varities
### ['white', 'Masala', 'Oolang']

### >>> tea_varities[1:1] = ["test", "test"] -> started at 1st index and inserted the values, 
### >>> tea_varities                          -> sutomatic shift of the other values
### ['white', 'test', 'test', 'Masala', 'Oolang'] 


###  tea_varities[1:3] =[] -> insert nothing at the slicing position
### >>> tea_varities
### ['white', 'Masala', 'Oolang']

### list methods
### append -> to add element at end
### pop -> to remove element from end
### insert -> position and element to give tea_varities(postion, element)

## interview question
### to make the copy of list
### tea_variety = ["green", "black", "white", "masala"]
### tea_variety_copy = tea_variety -> here, both will refer the same list in the memory
### tea_variety_copy = tea_variety.copy() -> this method avoids refering the same list by the two
### tea_varities = ["green", "black", "white", "masala"]
### >>> tea_varities_copy = tea_varities.copy()
### tea_varities_copy.append("Lemon") 
### >>> tea_varities_copy
### ['green', 'black', 'white', 'masala', 'Lemon']
### >>> tea_varities
### ['green', 'black', 'white', 'masala']

### list comprehension
### squared_nums = [x**2 for x in range(10)]
### >>> squared_nums
### [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]