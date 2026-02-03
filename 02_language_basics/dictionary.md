### chai_types = {"Masala" : "spicy", "Ginger" : "Zesty", "Green" : "mild"}
### >>> chai_types
### {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'mild'}
### chai_types["Masala"]
### 'spicy'

### chai_types.get("Gingery")
### >>> chai_types["Gingery"]    
### Traceback (most recent call last):
 ###  File "<stdin>", line 1, in <module>
### KeyError: 'Gingery'

 ### chai_types
### {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'mild'}
### >>> chai_types["Green"] = "Fresh"
### >>> chai_types
### {'Masala': 'spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}

### when wew iterate over the dictionary, then we will get the keys of it not the values

### gives key and values
for key, value in chai_types.items():
...     print(key,value)
... 
Masala spicy
Ginger Zesty
Green Fresh

### gives keys
for key in chai_types:
...     print(key)
... 
Masala 
Ginger 
Green 

```
len can also be used for dictionary
>>> len(chai_types)
3
```
```
using pop by providing the key, it returns the value of that key
pop can be used to remove any element in dictionary
>>> chai_types.pop("Ginger")
'Zesty'
```
```
the popitem removes the last item from the dictionary and returns it
 chai_types.popitem()
('Green', 'Fresh')
```
```
removes the element entirely from the memory
del chai_types['Green']
```
```
the copy is created using the copy() method
the change in the copy doesnot reflect in the original
chai_types_copy = chai_types.copy()
>>> chai_types_copy
{'Masala': 'spicy'}
>>> chai_types
{'Masala': 'spicy'}
>>> chai_types_copy['Green'] = 'Fresh'
>>> chai_types_copy
{'Masala': 'spicy', 'Green': 'Fresh'}
>>> chai_types
{'Masala': 'spicy'}
```
```
list comprehension like in dictionary
 squared_num = {x:x**2 for x in range(10)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```
```
to clear the dictionary
 squared_num.clear()
 squared_num
 {}
 ```

 

