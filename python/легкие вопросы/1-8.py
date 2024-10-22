n=int(input("Размер массива:"))
mass=[]
if 0 < n and n < 10000:
   for i in range(n):
     num = int(input(f"Введите число {i+1}: " ))
     mass.append(num)
   print("Наш массив", mass)  
else:
  print("Условие не выполняется")
#print("Наш массив", mass)