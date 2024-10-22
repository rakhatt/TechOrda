m=int(input("Введите число:"))

if m > 0 and m < 10000 and m%2 == 0 and m > 2:
    k=int(m/2)
    l=0
    for i in range(1,k+1):
        if (m%i) == 0:
            l=l+i
 #       print(i, l)
    i+=1

    if m == l and m > 2:
      print(f"Число {m} совершенное")
    else:
      print(f"Число {m} не совершенне")
else:
  print(f"Число {m} не совершенне")
 
