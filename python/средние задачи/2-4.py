y=int(input("Введите год:"))
m=int(input("Введите число месяца:"))
d=int(input("Введите день"))
mass1=[1,3,5,7,8,10,12]
mass2=[4,6,9,11]
if 0 < m and m in mass1:
      if d > 0 and d <=31:
            print(d,m,y)
      else:
            print("Дата не верна")
elif m >0 and m in mass2:
      if d > 0 and d <= 30:
            print(d,m,y)
      else:
            print("Дата не верна")
elif m == 2:
      if y%4 == 0 and d > 0 and d <= 29:
            print(d,m,y)
      elif y%4 > 0 and d > 0 and d <= 28:       
            print(d,m,y)
      else:
            print("Дата не верна")
else:
      print("Дата не верна")      