n=int(input("Введите число:"))
if n > 0 and (n%2)==0:
    print("число четное")
elif n > 0 and (n%2) > 0:
    print("число не четное")
else :
    print("Не число")