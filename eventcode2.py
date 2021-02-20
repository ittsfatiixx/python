z=''
'''for i in 'C:\ittsfatiixx\sem2\hello.txt':
	z+=str(ord(i))+' '
print(z)'''

f=open('c.txt')
z=f.read()
'''
for i in z:
       print(i)
'''
print(z)
y=[]
for i in range(0,len(z),2):
       y.append(z[i]+z[i+1])

print(y)


