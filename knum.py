a=input('enter a 4 dig num: ')
def sort(a):
       x=sorted(str(a))
       y=[]
       for i in range(len(x)-1,-1,-1):
              y.append(x[i])
       a=''.join(x)
       b=''.join(y)
       a=int(a)
       b=int(b)
       return a,b
c=0
count=0
def fun(x,y,z,count):
       if z!=6174:
              z=y-x
              print(z)
              count+=1
              print(count)
              x,y=sort(z)
              fun(x,y,z,count)
       else:
              print( count,' : final count')
if a==str(a[0])*4:
       print("Can't reach Kaprekar's constnt 6174")
else:
       m,n=sort(a)
       fun(m,n,c,count)

