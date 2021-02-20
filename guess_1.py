'''
   *random  num         :  ****
   guess the num       :
   no. of correct digs :
   no. of attepmts      :

   'Check'            'Restart'
   'Giveup'           'Quit'

   Enter a 4 dig num



*   1. Random number should be generated(r)
   2. Repeat 3,4,5 until user doesnt press 'R' 'G' 'Q' or r==a
   3.   User can enter a num(a) and press 'CHECK'
   4.   Show 'no. of correct digs'(d)
   5.   Increment the counter (c) for 'no. of attepmts'
   6. If 'GIVEUP' print the random number and exit
   7. if 'RESTART' start again
   8. if 'QUIT' exit
'''



def main():
    print('Guess the number!!!!')
    import random
    print('''
          C -Check
          R -Restart
          G -Giveup
          Any other key -Quit
                ''')
    print('Random number : ****')
    r=str(int(random.random()*10000))
    #print(r)
    d=0
    c=0
    control='C'
    a=''
    while((control=='c' or control=='C') and r!=a):
        a=input('Guess the num : ')
        if (len(a)!=4):
            print('Enter a 4 digit number!!')
            a=input('Guess the num : ')
        control=input('C/R/G/Q ?  Enter your choice: ')
        if (control=='C' or control=='c'):
            for i in range(0,4):
                if(r[i]==a[i]):
                    d=d+1
               #     print(r[i],'  ',i)
            if d==4:
                print('CORRECT ANSWER..!!!')
            print('NO. of correct digits : ',d)
            c=c+1
            print('No. of attempts : ',c)
            d=0
    if (control=='r' or control=='R'):
        main()
    if (control=='g' or control=='G'):
        print('YOU GAVE UP!!!')
        print('Random number : ',r)
        print('Your number : ',a)
  
main()
