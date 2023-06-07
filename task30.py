# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести 
# с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstItem = int(input('Введите первый элемент арифметической прогрессии: '))
difference = int(input('Введите разность арифметической прогрессии: '))
numberItem = int(input('Введите количество элементов арифметической прогрессии: '))

listItems = []
listItems.append(firstItem)
for i in range(2, numberItem+1):
    item = firstItem + (i - 1) *difference
    listItems.append(item)  
print(listItems)