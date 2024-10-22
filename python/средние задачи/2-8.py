y=int(input("Введите год:"))
m=int(input("Введите число месяца:"))
d=int(input("Введите день"))
mass1=[1,3,5,7,8,10,12]
mass2=[4,6,9,11]
massl=[6,7,8]
masso=[9,10,11]
massv=[3,4,5]
massz=[12,1,2]
l=str("лето")
z=str("Зима")
o=str("Осень")
v=str("Весна")
k=str
if m in massl:
      k=l
elif m in massz:
      k=z
elif m in masso:
      k=o
elif m in massv:
      k=v
if 0 < m and m in mass1:
      if d > 0 and d <=31:
            print(d,m,y,k)
      else:
            print("Дата не верна")
elif m >0 and m in mass2:
      if d > 0 and d <= 30:
            print(d,m,y,k)
      else:
            print("Дата не верна")
elif m == 2:
      if y%4 == 0 and d > 0 and d <= 29 and y%100 > 0:
            print(d,m,y,k)
      elif y%4 > 0 and d > 0 and d <= 28:       
            print(d,m,y,k)
      else:
            print("Дата не верна ")
else:
      print("Дата не верна") 