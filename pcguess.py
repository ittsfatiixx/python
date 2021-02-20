x=input('Enter a random 3 digit num: ')
s='0123456789'
a=''

for i in s:
       if len(a)<len(x):
              print('trying the num: ',i*3)
              c=0
              for j in x:
                     if i==j:
                            a=a+i
                            c+=1
              print('no of correct digits: ',c)

for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
               if(i!=j and j!=k and i!=k):
                     y=a[i]+a[j]+a[k]
                     print('trying the num: ',y)
                     
                     if y==x:


