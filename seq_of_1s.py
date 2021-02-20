print('Enter str of 0s and 1s: ')


def getinput():
       h=input()
       for i in h:
              if i!='0' and i!='1':
                     print('Please anter only 0s and 1s: ')
                     h=getinput()
                     break
       return h
 
x=getinput() #func defined above to get i/p
x='0'+x
a='011'
c=0
for i in range(len(x)-2):
       b=x[i]+x[i+1]+x[i+2]
       if a==b:
              c+=1
print("No of continous 1's : ",end=' ')
print(c)
