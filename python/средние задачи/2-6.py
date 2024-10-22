c=int(input("Введите число: "))
m = c+1
a=0 
b=1
for i in range(m):
   a, b = b , a + b
   if a == c:
    print(f"Число {c} относичтся к Фибоначи")       
 