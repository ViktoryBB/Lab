numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = 4  # индекс пропущенного элемента
sum_n = sum(numbers[:index]) + sum(numbers[index + 1:])  # сумма чисел
len_n = len(numbers)  # количество элементов
average = sum_n / len_n  # среднее арифметическое
numbers[index] = average  # замена пропущенного индекса средним арифметическим
print("Измененный список:", numbers)
