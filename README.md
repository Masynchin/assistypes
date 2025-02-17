# assistypes

## Установка
С помощью командной консоли и git
```
git clone https://github.com/Masynchin/assistypes.git
cd assistypes
python setup.py install
```

## Разделы
- [Lists](https://github.com/Masynchin/assistypes#Lists)
  - [StructuredList](https://github.com/Masynchin/assistypes#StructuredList)
- [Dicts](https://github.com/Masynchin/assistypes#Dicts)
  - [AttributedDict](https://github.com/Masynchin/assistypes#AttributedDict)
- [Ranges](https://github.com/Masynchin/assistypes#Ranges)
  - [FloatRange](https://github.com/Masynchin/assistypes#FloatRange)
  - [RoundedRange](https://github.com/Masynchin/assistypes#RoundedRange)

### Lists
#### StructuredList
```python
from assistypes.list import StructuredList
from pprint import pprint

keyboard = StructuredList([f"Button {i}" for i in range(1, 13)])

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
### Dicts
#### AttributedDict
```python
from assistypes.dict import AttributedDict

order = AttributedDict({
    "id": 123,
    "customer_id": 456,
    "products": {
        "bread": {"cost": 50},
        "milk": {"cost": 100},
    }
})

total = sum(product.cost for product in order.products.values())
# 150

del order.products.bread
order.products.cereal = {"cost": 150}

# AttributedDict({
#     "id": 123,
#     "customer_id": 456,
#     "products": {
#         "cereal": {"cost": 150},
#         "milk": {"cost": 100},
#     }
# })
```
### Ranges
#### FloatRange
```python
from assistypes.range import FloatRange

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
from assistypes.range import FloatRange, RoundedRange

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
