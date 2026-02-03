## Tuples are designed with the same features of lists but immutable

```
len(tea_types)
3
```

```
adding elements into the tuple
tea_types += ('Ginger', 'Mytea')
>>> tea_types
('Black', 'Green', 'Oolang', 'Ginger', 'Mytea')

all_tea = more_tea + tea_types 
>>> all_tea
('Herbal', 'Earl Grey', 'Black', 'Green', 'Oolang')
```
```
to count the number of values in the tuple
tea_types.count('Oolang')
1
```
```
tupple unpacking: the variables at the left has to be the same number as the number of elements in the tuple
 tea_types
('Black', 'Green', 'Oolang', 'Ginger', 'Mytea')
(black, green, oolang, ginger, mytea) = tea_types
>>> black
'Black'
>>> green
'Green'
>>> mytea
'Mytea'
```