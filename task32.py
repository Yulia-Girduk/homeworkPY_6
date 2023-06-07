# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

listItem = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

numberMin = int(input('Введите значение минимума: '))
numberMax = int(input('Введите значение максимума: '))
listIndex = []
for i in range(len(listItem)):
    if numberMin <= listItem[i] <= numberMax:
        listIndex.append(i)
print(listIndex)        
