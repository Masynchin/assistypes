# my_types

## Установка
Пока что, я не знаю, как это сделать

## Типы
* [StructuredList](https://github.com/Masynchin/my-types-python#StructuredList)

### StructuredList
```python
from my_types import StructuredList
from pprint import pprint

keyboard = StructuredList([f'Button {i}' for i in range(1, 13)])

keyboard.resize((3,4))
pprint(keyboard)

# [['Button 1', 'Button 2', 'Button 3', 'Button 4'],
#  ['Button 5', 'Button 6', 'Button 7', 'Button 8'],
#  ['Button 9', 'Button 10', 'Button 11', 'Button 12']]

keyboard.resize((4,3))
pprint(keyboard)

# [['Button 1', 'Button 2', 'Button 3'],
#  ['Button 4', 'Button 5', 'Button 6'],
#  ['Button 7', 'Button 8', 'Button 9'],
#  ['Button 10', 'Button 11', 'Button 12']]
```
