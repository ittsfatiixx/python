a=input('enter n1: ')
b=input('enter n2: ')
s=0

a=set(a)
b=set(b)
#for no repetition

for i in a:
   if(i not in b):
       s=s+1
for i in b:
    if (i not in a):
        s=s+1
print(s)

f=['f','l','a','m','e','s']
x=s
i=1
while i<len(f):
    if(x<=len(f)):
        f=f[x:]+f[:(x-1)]
    else:
        y=x
        while(y>len(f)):
            y=y-len(f)    
        f=f[y:]+f[:(y-1)]       
print(f)

    
input()
