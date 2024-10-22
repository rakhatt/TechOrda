m=1000
for i in range(m+1): 
      l=0
      for j in range(1,i):
          if (i%j) == 0:
            l=l+j
          if i == l and i/2 == j:
           print(f"Число {i} совершенное")
          j+=1
i+=1 
