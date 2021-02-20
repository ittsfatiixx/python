dict={'a':('_yy_','y__y','yyyy','y__y','y__y'),
'b':('yyy_','y__y','yyy_','y__y','yyy_'),
'c':('_yy','y__','y__','y__','_yy'),
'd':('yyy_','y__y','y__y','y__y','yyy_'),
'e':('yyyy','y___','yyy_','y___','yyyy'),
'f':('yyyy','y___',"yyy_",'y___','y___'),
'g':('_yyy','y___','y_yy','y__y','_yy_'),
'h':('y__y','y__y','yyyy','y__y','y__y'),
'i':('y','y','y','y','y'),
'j':('yyyy','___y_','___y_','y_y_','_y__'),
'k':('y__y','y_y_','yy__','y_y_','y__y'),
'l':('y__','y__','y__','y__','yyy'),
'm':('y___y','yy_yy','y_y_y','y___y','y___y'),
'n':('y___y','yy__y','y_y_y','y__yy','y___y'),
'o':('_yy_','y__y','y__y','y__y','_yy_'),
'p':('yyy_','y__y','yyyy','y___','y___'),
'q':('_yy_','y__y','y__y','_yy_','___y'),
'r':('yyy_','y__y','yyy_','y_y_','y__y'),
's':('_yyy','y___','_yy_','___y','yyy_'),
't':('yyy','_y_','_y_','_y_','_y_'),
'u':('y__y','y__y','y__y','y__y','_yy_'),
'v':('y___y','y___y','y___y','_y_y_','__y__'),
'w':('y___y','y___y','y_y_y','yy_yy','y___y'),
'x':('y___y','_y_y_','__y__','_y_y_','y___y'),
'y':('y___y','_y_y_','__y__','__y__','__y__'),
'z':('yyyyy','___y_','__y__','_y___','yyyyy'),
      ' ':('   ','   ','   ','   ','   ')}


print()
#name=input('Enter_your_name: ')
name='heyyyy'
for line in range(5):
       for alph in name:
              temp=dict[alph]
              print(temp[line],end='  ')
       print()
