array = list(map(int, input("Введите элементы массива через пробел: ").split()))
if not array:
    print(None)
else:
    array.sort()
    n = len(array)
    
    # Если длина массива четная, выводим левую медиану
    if n % 2 == 0:
        print(array[(n // 2) - 1])
    else:
        # Если длина нечетная, выводим средний элемент
        print(array[n // 2])