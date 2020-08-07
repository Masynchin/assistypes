# my_types

## Установка
Пока что, я не знаю, как это сделать

## Разделы
- [Lists](https://github.com/Masynchin/my-types-python#Lists)
  - [StructuredList](https://github.com/Masynchin/my-types-python#StructuredList)
- [Ranges](https://github.com/Masynchin/my-types-python#StructuredRanges)
  - [FloatRange](https://github.com/Masynchin/my-types-python#FloatRange)
  - [RoundedRange](https://github.com/Masynchin/my-types-python#RoundedRange)

### Lists
#### StructuredList
```python
from my_types import StructuredList
from pprint import pprint

keyboard = StructuredList([f'Button {i}' for i in range(1, 13)])

print(keyboard.size)
# (12,)

keyboard.resize((3,4))
pprint(keyboard)

# [['Button 1', 'Button 2', 'Button 3', 'Button 4'],
#  ['Button 5', 'Button 6', 'Button 7', 'Button 8'],
#  ['Button 9', 'Button 10', 'Button 11', 'Button 12']]

print(keyboard.size)
# (3, 4)

keyboard.resize((2,2,3))
pprint(keyboard)

# [[['Button 1', 'Button 2', 'Button 3'], ['Button 4', 'Button 5', 'Button 6']],
#  [['Button 7', 'Button 8', 'Button 9'], ['Button 10', 'Button 11', 'Button 12']]]

print(keyboard.size)
# (2, 2, 3)
```
### Ranges
#### Float Range
```python
from my_types import FloatRange

for i in FloatRange(1, 10, 1.5):
	print(i)

# 1.0
# 2.5
# 4.0
# 5.5
# 7.0
# 8.5

for i in FloatRange(10, 1, -1.5):
	print(i)

# 10.0
# 8.5
# 7.0
# 5.5
# 4.0
# 2.5
```

#### RoundedRange
```python
from my_types import FloatRange, RoundedRange

for i in FloatRange(1, 10, 1.333):
	print(i)

# 1.0
# 2.333
# 3.6660000000000004
# 4.9990000000000006
# 6.332000000000001
# 7.665000000000001
# 8.998000000000001

for i in RoundedRange(1, 10, 1.333):
	print(i)

# 1.0
# 2.333
# 3.666
# 4.999
# 6.332
# 7.665
# 8.998
```
