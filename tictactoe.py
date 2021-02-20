#input
a=[[1,0,0],
   [0,0,1],
   [1,1,1]
       ]



s='tie'
x=[]
y=[]

def check(x,y):
       if (x[0]==x[1] and x[1]==x[2]):
              s=x[0]
              return s,s
       elif y[0]==y[1] and y[1]==y[2]:
              s=y[0]
              return s,s
       y=[]
       x=[]
       return x,y

for i in range(0,3):
       for j in range(0,3):
              x.append(a[i][j])
              y.append(a[j][i])
       x,y=check(x,y)
       s=x
       if s==[]:
              for j in range(0,3):
                     x.append(a[j][j])
                     y.append(a[j][2-j])
              x,y=check(x,y)
              s=x
       if s=='x':
              s='player 1 is winner'
              break
       elif s=='o':
              s='player 2 is winner'
              break
       
print(s)
       
