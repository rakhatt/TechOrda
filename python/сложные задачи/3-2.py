import time

current_year = time.localtime().tm_year
print(f"Текущий год: {current_year}")

y=int(input("Введите год:"))
k=0
i=1
while i <= y:

    if (i % 4 == 0 and i%100 != 0) or (y%400 == 0):
        k+=1
   #     print(i)
    i+=1

print(k)    