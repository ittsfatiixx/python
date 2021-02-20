a=[
[0, 0, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0]
       ]

print('input')
for i in a:
       print(i)
print()      

def gof(a):
       b=[[],[],[],[],[]]
       a.insert(0,[0,0,0,0,0])
       a.append([0,0,0,0,0])
       for i in range(0,len(a)):
                     a[i].insert(0,0)
                     a[i].append(0)
                          
       for i in range(1,6):
              for j in range (1,6):
                     x=a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
                     if x<2 or x>3:
                            b[i-1].insert(j-1,0)
                     elif x==2:
                            b[i-1].insert(j-1,a[i][j])
                     elif x==3:
                            b[i-1].insert(j-1,1)
       return b

n=int(input('how many gens? '))
print('output')
for i in range(n):
       b=gof(a)
       a=b
       for i in b:
              print(i)
       print()

