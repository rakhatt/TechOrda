n=int(input("Введите чиисло:"))
b=int(input("Введите степень:"))
j=1
i=1
if n>0:
   for i in range(b):
    j=j*n
    i+=1
print(j)