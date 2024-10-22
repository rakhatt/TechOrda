a=int(input("Введите число a:"))
b=int(input("Введите число b:"))
c=int(input("Введите число c:"))

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(a, b, c)

#sum = a + b + c
#max= (a + b + abs(a - b))/2
#max= (max + c + abs(max - c))/2
#min= (a + b - abs(a - b))/2
#min= (min + c - abs(min - c))/2
#middle= sum - max - min
#print(min, middle, max)