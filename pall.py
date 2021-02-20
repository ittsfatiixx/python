'''
compute pallindrome and count no.
of chars to add for making pall..

'''
a=input('enter a word: ')
i=0;  j=len(a)-1
while i<j:
       if a[i]!=a[j]:
              x=a[:i+1]
              c=len(x)
              i+=1;   j=len(a)-1
       else:
              i+=1;   j-=1
print(c)

