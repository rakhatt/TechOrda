n=int(input("Введите число: "))

if n > 0 and n > 1:
    i=1
    for i in range (1,n):
      if i > 0 and (n%i) == 0 and i > 1:
       f = 1 
#       print(f"число не простое {i}")
       break 
      else:
       f=2
#       print(f"число простое {i}")
      i+=1
   
    if f == 2:
       print(f"Число {n} простое")
    elif f == 1:
       print(f"Число {n} не простое")
    else:
       print("Не число")