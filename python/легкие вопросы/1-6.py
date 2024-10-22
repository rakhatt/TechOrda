n=int(input("Введите срок в количество месяцев:"))
b=int(input("Введите процент:"))
j=int(input("Введите сумму:"))
i=1
if n>0:
   for i in range(n):
    j+=j*(b/100)
    i+=1
print(j)