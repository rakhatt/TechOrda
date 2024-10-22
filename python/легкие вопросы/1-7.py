n=int(input("Размер массива:"))
mass=[]
if 0 < n and n < 10000: 
   for i in range(n):
     num = int(input(f"Введите число {i+1}: " ))
     mass.append(num)
print("Наш массив", mass)


j=0
for i in range(len(mass)):
    if mass[i]> j:
        j=mass[i]
        i+=1

print(j)