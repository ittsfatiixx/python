b=input('enter ref str:  ')
a=input('enter rotated str: ')
bl,br=b,b
l,r=0,0
while a!=bl and a!=br:
       bl=bl[1:]+bl[0];l+=1
       br=br[len(b)-1]+br[:len(b)-1];r+=1

if a==bl:
       print('left  ',l)
elif a==br:
       print('right  ',r)
else:
       print('no shift.. ')
       
