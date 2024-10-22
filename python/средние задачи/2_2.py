m=str(input("Введите строку:"))
mass=list(m)
print(mass)
n=len(mass)
for i in range(len(mass)):
    if mass[i] == mass[n]:
        h=1
    else:
        h=2
    i+=1
    n-=1
if h == 1:
    print("yes")
else:
    print("no")
