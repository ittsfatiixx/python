n=int(input("enter: "))
for i in range(1,n+1):
       for j in range((n-i),0,-1):
              print('    ',end='')
       for k in range(((2*i)-1),i-1,-1):
              print(k,' ',end='')
              k-=1
       for k in range(i+1,2*i):
              print(k,' ',end='')
       print()
