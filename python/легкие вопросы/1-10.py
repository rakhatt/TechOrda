n=int(input("Размер массива:"))
mass=[]
if n>0 and n < 10000:
     for i in range(n):
      num=int(input(f"Введите число {i+1}: " ))
      mass.append(num)
     print("Наш массив", mass) 

j=0
for i in range(len(mass)):
   for j in range(len(mass)-1-i): 
       if mass[j] > mass[j+1]:
          mass[j],mass[j+1]=mass[j+1], mass[j]
print(mass)   