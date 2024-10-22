n=int(input("Размер массива:"))
mass=[]
if n>0 and n < 10000:
     for i in range(n):
      num=int(input(f"Введите число {i+1}: " ))
      mass.append(num)
     print("Наш массив", mass)  

j=0
for i in range(len(mass)):
    j+=mass[i]
print(j) 

summ_number=sum(mass)
print(summ_number)