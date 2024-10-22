array1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))

array2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

set1 = set(array1)
missing_numbers = [num for num in array2 if num not in set1]
missing_numbers.sort()

print(missing_numbers)