print('convert numbers into words')

def itoau(i):
    a=i
    if a==1:
        x='one'
    elif a==2:
        x='two'
    elif a==3:
        x='three'
    elif a==4:
        x='four'
    elif a==5:
        x='five'
    elif a==6:
        x='six'
    elif a==7:
        x='seven'
    elif a==8:
        x='eight'
    elif a==9:
        x='nine'
    else:
        x=''
    return x

def itoat(j):
    a=j
    if a==2:
        x='twenty'
    elif a==3:
        x='thirty'
    elif a==4:
        x='forty'
    elif a==5:
        x='fifty'
    elif a==6:
        x='sixty'
    elif a==7:
        x='seventy'
    elif a==8:
        x='eighty'
    elif a==9:
        x='ninety'
    else:
        x=''
    return x

def tens(k):
    a=k
    if a==10:
        x='ten'
    elif a==11:
        x='eleven'
    elif a==12:
        x='twelve'
    elif a==13:
        x='thirteen'
    elif a==14:
        x='fourteen'
    elif a==15:
        x='fifteen'
    elif a==16:
        x='sixteen'
    elif a==17:
        x='seventeen'
    elif a==18:
        x='eighteen'
    elif a==19:
        x='nineteen'
    else:
        x=itoat(a//10)+' '+itoau(a%10)
    return x

def main():
    n=int(input('Enter a valid 9 or less dig num: '))
    q=''
    if n in range(0,1000000000):
        if n==0:
            q='Zero'
        if n//1!=0 or n//10!=0:
            q=tens(n%100)
        n=n//100
        if n//1!=0 and n%10 :
            q=itoau(n%10)+' hundred '+q
        n=n//10
        if (n//1!=0 or n//10!=0) and n%100!=0:
            q=tens(n%100)+' thousand '+q
        n=n//100
        if (n//1!=0 or n//10!=0) and n%100!=0:
            q=tens(n%100)+' lakh '+q
        n=n//100
        if (n//1!=0 or n//10!=0) and n%100!=0:
            q=tens(n%100)+' crore '+q
        n=n//100
        print(q.title())
    else:
        print('Error: Enter proper value of 9 or less digs')

main()
