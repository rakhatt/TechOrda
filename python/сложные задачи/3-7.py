array = list(map(int, input("Введите элементы массива через пробел: ").split()))

left_sum = 0
total_sum = sum(array)

for i in range(len(array)):
    
    right_sum = total_sum - left_sum - array[i]
    
    if left_sum == right_sum:
        print(True)
        break
    
    left_sum += array[i]
else:
    print(False)