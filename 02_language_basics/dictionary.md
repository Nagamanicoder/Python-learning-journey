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
for key, values in chai_types.items():
...     print(key,values)
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